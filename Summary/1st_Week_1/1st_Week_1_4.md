## 1.5주차 - MTV 패턴

### MTV란?
`Model`, `Template`, `View`의 약자<br/>

**Model**
+ `Data Base`를 다뤄주는 역할
+ 데이터 탐색 담당

**Template**
+ 사용자에게 보여지는 `html`화면
+ 보여주기 담당

**View**
+ `함수`들이 모여있는 곳
+ 처리 담당

`M`, `T`, `V` 각각 **독립적** 임무 수행으로 `Django`가 작동

### MVC패턴
`MTV`가 차용한 방식으로 더 **일반적인** 패턴<br/>
`Model`, `View`, `Controller`의 약자

**Model**
+ `Data Base` 담당
+ `MTV`의 `Model`과 같다.

**View**
+ 사용자에게 보여지는 화면 담당
+ `MTV`의 `Template`와 같다.

**Controller**
+ 중간관리 담당
+ `MTV`의 `View`와 같다.
