# import boto3
# import os

# s3 = boto3.client('s3')

# def download_dir(local_path, model_name):
#     s3_prefix='ml-models/'+model_name
#     os.makedirs(local_path, exist_ok=True)

#     paginator = s3.get_paginator('list_objects_v2')
    
#     for result in paginator.paginate(Bucket='my-mlops'):
#         if 'Contents' in result:
#             for key in result['Contents']:
#                 s3_key = key['Key']
#                 print(f's3 key: {s3_key}')
#                 # local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_prefix))    # 로컬에 저장
#                 local_file = os.path.join('ml-models', s3_key)
#                 print(f'local_file: {local_file}')
#                 bucket_name = 'my-mlops'
#                 s3.download_file(bucket_name, s3_key, local_file)

# 1안
import boto3
import os
s3 = boto3.client("s3")
def download_dir(local_path, model_name):
    s3_prefix = os.path.join("ml-models", model_name)
    os.makedirs(local_path, exist_ok=True)
    paginator = s3.get_paginator("list_objects_v2")
    paget_iterator = paginator.paginate(Bucket="my-mlops")
    for result in paget_iterator:
        if "Contents" in result:
            for key in result["Contents"]:
                print(key)
                s3_key = key["Key"]
                local_file = os.path.join("ml-models", s3_key)
                s3.download_file("my-mlops", s3_key, local_file)


# 2안은 그냥 os.path.relpath(s3_key, s3_prefix) 이부분을 그냥 s3_key로 바꾸면 되네요