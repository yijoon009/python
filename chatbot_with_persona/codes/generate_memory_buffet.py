import argparse
import math
import multiprocessing
import os
import re
import time
from operator import itemgetter

import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from tqdm import tqdm

from constants import api_key

os.environ["OPENAI_API_KEY"] = api_key


template = """
I want you to create a multi turn conversation between a friend and Warren Buffett, a famous American businessman and investor.

- The conversation should consisted at 1-3 turns each.
- The conversation should include the line "Buffett: {query}"
- The friend must initiate the conversation.
- When generating Buffett's line, I want you respond and answer like Warren Buffett using the tone, manner, and the vocabulary of Warren Buffett would use.
- Note that Warren Buffett is businessman born in 1930.
    He is one of the best-known investors in the world, and seventh-richest person in the world

[example A]
### Given line: We enjoy the process far more than the proceeds.
friend: What is more important, between process and the proceeds?
Buffett: We enjoy the process far more than the proceeds.
friend: How does that affect your decision-making in investments?
Buffett: It means we focus on understanding and enjoying the journey of investment, which often leads to better long-term results, rather than being solely fixated on the immediate financial outcomes.


[Generate]
### Given line: {query}
friend:
"""

template_valid = """
This is conversation between famous businessman and interviewer.

{result}

1. Do you think this businessman is someone you know? If so, who? ([format] person: enter here)
2. If you choose one of the below businessman to be the interviewee, who whould it be? Answer with reason. ([format] person: enter here, reason: enter here)
    - Robert Kiyosaki
    - Steve Jobs
    - Warren Buffett
    - Charles Munger
    - None of the above
3. Reflecting above answers, who do you think this businessman is? ([format] person: enter here)
"""


def remove_clues(conv):
    re_buffett = "warren buffett|buffett|warren"
    result = re.sub(re_buffett, "businessman", conv.lower())
    return {"result": result, "orig": conv}


def generate_answer(queries):
    llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")
    prompt = ChatPromptTemplate.from_template(template)
    prompt_valid = ChatPromptTemplate.from_template(template_valid)

    validate_chain = (
        prompt
        | llm
        | StrOutputParser()
        | remove_clues
        | {
            "validation": prompt_valid | llm | StrOutputParser(),
            "conversation": itemgetter("orig"),
        }
    )

    result = []
    idx = 0
    pbar = tqdm(total=len(queries) - idx + 1)
    while idx < len(queries):
        query = queries[idx]
        try:
            answer = validate_chain.invoke({"query": query})
            result.append(answer)
            idx += 1
        except Exception as exp:
            print(exp)
            time.sleep(60)
            continue
        pbar.update(1)

    result_df = pd.DataFrame({"query": queries, "chain_result": result})
    result_df[["validation", "conversation"]] = result_df.apply(
        lambda row: (
            row["chain_result"]["validation"],
            row["chain_result"]["conversation"],
        ),
        axis=1,
        result_type="expand",
    )

    return result_df


def main(num_process):
    with open("../dataset/buffett_quotes.txt", "r") as f:
        queries = f.readlines()
    queries = list(set(queries))

    num_queries = len(queries)
    window = math.ceil(num_queries / (num_process * 10)) * 10
    print(num_queries, window)
    inputs = [(queries[idx : idx + window],) for idx in range(0, num_queries, window)]

    pool = multiprocessing.Pool(processes=num_process)
    result = pool.starmap(generate_answer, inputs)
    result = pd.concat(result).reset_index(drop=True)
    result.to_json("../dataset/buffet_conversations_test.json", orient="index")

    pool.close()
    pool.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract and process scripts from documents."
    )
    parser.add_argument(
        "--process", type=int, default=8, help="Number of processes to use"
    )

    args = parser.parse_args()
    main(args.process)
