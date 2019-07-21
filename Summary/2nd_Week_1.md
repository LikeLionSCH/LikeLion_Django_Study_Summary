## 1주차 - 1. JSON

### JSON 이란?
**J**ava **S**cript **O**bject **N**otation의 약자<br/>

**데이터의 송수신**을 자바스크립트의 문법으로 표현된 객체로서<br/>
수행할 수 있게 하는 **가벼운 문자열 데이터 표현식**<br/>

> 자바스크립트를 사용하지 않아도 사용 가능

웹에서 **Server**와 **Client**사이에는 아래와 같은 항목들을 주고 받는다.<br/>
1. 구조를 나타내는 **HTML**
2. 스타일을 표현하는 **CSS**
3. 논리를 구현하는 **Javascript**

앞으로 배울 강의들은 데이터인 **JSON**만 주고 받는다.<br/>
**JSON**과 비슷한 데이터 형식으로는 **XML**이 있다.<br/>

#### 앞으로 배울 과정
1. **Restful API** Server를 구성
2. **Request**에 따른 JSON **Response** 보내는 과정

### JSON 문법 형식
Python의 **딕셔너리**와 비슷한 구조<br/>
**name** : **value**로 구성되어 있다.<br/>
**숫자**, **문자(열)**, **Boolean,** **배열**, **객체**로 구성이 가능하다.<br/>

```json
json_example = {
    "string_name": "something",
    "number_name": 3,
    "null_name": null,
    "bool_name": true
}
```

### JSON으로 표현하기

| 일기 NO. 3                                   |
| -------------------------------------------- |
| 제목 : 어벤져스 엔드게임을 봤다.             |
| 본문 : 어벤져스 엔드게임을 봤다. ... 귀찮다. |

위와 같은 내용의 일기장 데이터를 **JSON**형식으로 보내고 싶은 경우 아래와 같다.<br/>

```json
{
    "id": 3,
    "title": "어벤져스 엔드게임을 봤다.",
    "body": "어벤져스 엔드게임을 봤다. ... 귀찮다."
}
```

### 자바스크립트 객체로 그냥 보내면 되나?
데이터를 받는 모든 상대방은 **JSON**인지 알 수 없다.<br/>
따라서 모든 수신자가 알 수 있는 **공통 자료형**으로 바꾸어 보내야 한다.<br/>

모두가 아는 자료형은 **문자열**이 있다.<br/>
따라서 **JSON**데이터를 보낼 때에는 **직렬화**(Serialization)과정을 거쳐<br/>
**JSON**데이터를 **문자열**로 바꾸어 상대방에게 보낸다.<br/>

**< JSON 객체 >**
```json
{
"string_name": "something",
"number_name": 3,
"null_name": null,
"bool_name": true
}
```

**< 직렬화 후 문자열 >**
```
"{
\"string_name\": \"something\",
\"number_name\": 3,
\"null_name\": null,
\"bool_name\": true
}"
```

정리하자면 데이터를 **보낼 때**에는 **JSON을 문자열**로 바꾸어 보내고<br/>
데이터를 **받을때**는 **문자열을 JSON**으로 바꾸어 받는다.<br/>

### Python에서 JSON다루기
Python은 **JSON**을 처리하는 **라이브러리**를 제공한다.
`json`라이브러리를 `import`해서 사용해주면 된다.
```python
import json
```

아래와 같은 Python **딕셔너리 자료형**을 변환해보자.
```python
diary = {
    "id": 3,
    "title": "I'm starving..",
    "body": "On nana On na On nanana deal car",
}

print(diary)
print(type(diary))
```

**Output**<br/>
```
{'id': 3, 'title': "I'm starving..", 'body': 'On nana On na On nanana deal car'}
<class 'dict'>
```

#### Dict to JSON

`json`의 `dumps`함수를 이용해 변환을 진행한다.<br/>
아래의 과정은 데이터를 **송신할 때** 사용할 수 있다.
```python
diary_s = json.dumps(diary)

print(diary_s)
print(type(diary_s))
```

**Output**<br/>
`dumps`함수를 사용한 결과 `dict`자료형이 `str`으로 변환되었다.<br/>
```
{"id": 3, "title": "I'm starving..", "body": "On nana On na On nanana deal car"}
<class 'str'>
```

#### JSON to Dict

`json`의 `loads`함수를 이용해 변환을 진행한다.<br/>
아래의 과정은 데이터를 **수신할 때** 사용할 수 있다.
```python
diary_back = json.loads(diary_s)

print(diary_back)
print(type(diary_back))
```

**Output**<br/>
`loads`함수를 사용한 결과 `str`자료형이 `dict`로 변환되었다.<br/>
```
{'id': 3, 'title': "I'm starving..", 'body': 'On nana On na On nanana deal car'}
<class 'dict'>
```

[[코드 확인하기]](https://github.com/LikeLionSCH/LikeLion_Study_Summary/blob/master/Week_1_JSON.py)
