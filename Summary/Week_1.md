### 1주차 - 1.기본환경 셋팅
**사전작업**
1. `git` 설치하기
2. 작업 디렉토리 만들기
3. `python` 설치 확인하기

**VENV 생성 & 가상환경 실행**
```
python -m venv myvenv(가상환경명)
```

**가상환경 실행하기**
```
source myvenv/Scripts/activate
source myvenv/bin/activate
```

강의에서는 `Scripts`폴더의 `activate`파일을 실행하라고 하였으나<br/>
본인의 경우에 `Scripts`폴더가 존재하지 않고 `bin`폴더에 `activate`파일 존재<br/>
`source`명령어 대신 `.`을 입력해도 된다,

**가상환경 종료하기**
```
deactivate
```

**Django 설치하기**
> 가상환경을 실행하고 설치

```
pip install django
```

<br/>

### 1주차 - 2.Hello World 이론
