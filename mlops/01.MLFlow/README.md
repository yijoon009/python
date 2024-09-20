## 1. Project Directory

-   1. MLFlow

## 2. 가상 환경 구축

(mac)

> python3.10 -m venv .venv
> source .venv/bin/activate

-   poetry => venv보다 관리가 편한 부분이 있다.

## 3. MLFlow Install

> pip install mlflow
> mlflow ui

## Q&A

가상환경 종료는?

> deactivate

conda로 설치할땐? 3.10 버전 이상이면 pip install mlflow만 해도 된다.

> python -m venv .venv
> python3 -m venv .venv

> conda create --name 'mlops-project' python=3.10
> conda activate mlops-project
> conda deactivate

-   conda 같은 경우는 글로벌 가상환경이라고 보면 된다.

-   virtualenv로 글로벌 가상환경 하는 방법
    > pip install virtualenv
    > virtualenv --python=python3.10 mlops-project-virtual
    > source .venv/bin/activate

가상환경 구축

1. venv 모듈 사용
2. virtualenv 사용
3. conda 사용
4. poetry
