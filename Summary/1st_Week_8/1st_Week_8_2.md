## 8주차 - 2. app 재사용 실습

### 1. 새로운 폴더 생성

### 2. 재사용할 앱 폴더로 이동

### 3. 필요한 파일 생성
**README.rst**</br>
앱 기능 명시

**LICENSE**<br/>
코드의 라이센스 명시

**setup.py**<br/>
패키지 설치 과정 명시

**MANIFEST.in**<br/>
파이썬 파일 이외의 파일 명시

### 4. 패키징 진행
```
$ python setup.py sdist
```

### 5. 패키징한 앱 설치 및 사용하기
**폴더의 위치**를 잘 파악해 압축된 앱 설치
```
$ pip install dist/login-0.1.tar.gz
```
