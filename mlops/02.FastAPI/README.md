## FastAPI

FastAPI 특징이 뭐라고 생각하세요?

- 첫 번째, 데이터 타입 체크가 가능합니다. => pydantic
- 두 번째, 비동기 방식으로 구동됩니다. => asyncio
  => python 3.5 버전에서 async/await
- 동기와 비동기의 차이는 무엇인가요?
  ex) 스타벅스 카페 - 맨 앞에 있는 사람이 자바칩프라프치노벤티얼음많이초콜렛많이시럽추가 - 그 다음 사람이 기다려야 하면

  - 동기: 알바생 1명
  - 비동기: 알바생 N명 (부하 많이 걸리는 커피를 주문해도, 다음 알바생이 주문을 받을 수 있는 구조)

- 벤치마킹 지수를 보시면 FastAPI 상위권에 위치.

### Install

> source .venv/bin/activate
> pip install "fastapi[standard]"
