## 2주차 - 1. REST Architecture

### REST란?
**RE**presentational **S**tate **T**ransfer의 약자<br/>
`HTTP`를 이용해 통신하는 네트워크 상에서 정한 **약속**<br/>
분산 하이퍼미디어 시스템(**인터넷**, **웹**)을 위한 소프트웨어 설계 형식<br/>

> 자원 : 인터넷에서 제공하고 얻을 수 있는 모든 것

| 명칭                   | 해석                        |
|:---------------------- |:--------------------------- |
| **RE**presentational   | 자원을 대표하는 식별자로    |
| **S**tate **T**ransfer | 자원의 상태를 전송하는 방법 |

**자원**을 **이름으로 구분**하여 **상태**를 **전송**하는 방법<br/>

### REST가 필요한 이유
우리의 인터넷은 계속해서 발전해왔고 앞으로도 발전<br/>
**프로토콜**도 계속해서 발전해야한다.<br/>

1. 기존의 약속들 깨뜨리지 않고 **독립적 발전**을 하기위해 필요하다.

#### REST 설계 조건
**REST**가 되기 위한 필요충분 조건<br/>
1. Server-Client
2. STATELESS
    - Client의 **이전 상태**를 기록하지 않아야한다.
    - `HTTP`가 대표적인 STATELESS **프로토콜**
3. Cache
4. Uniform Interface
5. Layered System
6. Code-On-Demand
    - `JavaScript`와 같이 원격지에서 보낸 코드로 메소드 실행 가능

### API란?
**A**pplication **P**rogram **I**nterface의 약자<br/>
**Request**와 **Response**로 오가는 **구조화**된 데이터<br/>

| Example |  Client   |            Server             |
|:-------:|:---------:|:-----------------------------:|
| Before  | 식당 손님 | 원하는 요리를 만들어주는 사람 |
|  After  | 식당 손님 |            요리사             | 

여기서 **API**는 웨이터로 비유할 수 있다.<br/>
**Server**와 **Client**사이의 메신저로 **특정 형식**에 맞게 전달한다.<br/>

> 형식 : API 문서

### REST API란?
**REST Architecture** 스타일을 따르는 **API**<br/>
**REST API**를 제공하는 웹서비스는 **RESTful**하다.<br/>

> MicroSoft REST API Guidelines
> 1. URI는 http://{{servicce root}}/{collection}/id 형식
> 2. GET, PUT, DELETE, POST, HEAD, PATCH, OPTIONS를 지원
> 3. 등등

간단하게 **REST** 설계 조건에 맞는 **API**<br/>
현대 대부분의 서비스들은 모든 설계 조건을 지키지 못하고 있다.<br/>
왜냐하면 **JSON**을 이용해 통신을 하기 때문이다.<br/>
**JSON**은 모든 태그가 만들어져 있지 않고 **정의하기 나름**이기 때문이다.<br/>

또한 **REST** 설계 조건중 4번째 **Uniform Interface**는 아래와 같은 조건이 있다.<br/>
1. Resource가 URI로 식별이 되어야한다.
2. CRUD를 `HTTP`메세지로 수행 가능해야한다.
3. 메세지는 자체로 모든 것이 설명 가능해야한다.
4. 어플리케이션의 상태는 하이퍼링크를 이용해 전이되야한다.(**HATEOAS**)

요즘 **API**는 앞의 두가지만 잘 지켜 **REST**하지 못하다고 한다.<br/>

#### 3. 메세지는 자체로 모든 것이 설명 가능해야한다.
**JSON**에 Host 도메인, Content type 헤더, JSON 명세 등을 포함해야한다.<br/>
대부분의 **API**에는 위의 내용들을 포함하지 않고 있다.

#### 4. HATEOAS
전이의 예측가능성, 투명한 정보 전이를 위해 만들어진 원칙<br/>
**JSON**이 어디에서 어떤 링크를 타고 오고 이동하는지에 대한 정의<br/>
요즘은 잘 지켜지고 있지 않다.<br/>

현대의 **API**는 그렇게 **RESTful**하지 않다.<br/>
