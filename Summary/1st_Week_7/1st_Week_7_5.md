## 7.5주차 - 썸네일 만들기

### Thumbnail
이미지 파일을 **대표**하는 이미지

### 기능 장점
1. Thumbnail 파일 지정 용이
2. 파일 용량 관리 용이
3. 파일 분류에 효율적

### 실습
1. 기본적인 **Media 파일** 사용 설정
    + `models.py`에 `model`정의
    + `settings.py`에 경로 설정
    + `urls.py`에 `path` 추가
    + `admin.py`에 `model`등록
    + **migrate** 진행
    + `views.py`의 함수 이미지를 사용하도록 수정
    + `html`에 전달 받은 이미지 출력
2. pip **패키지** 설치

```
$ pip install pillow django-imagekit
```
3. settings.py에 앱 추가

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    ...

    # Imagekit
    'imagekit'
]
```
4. models.py에 model 수정

필요한 모듈 추가<br/>
`imagekit.models`의 `ImageSpecField`함수 이용<br/>
`source`인자는 **이미지 주소**, 이미지 **크기를 조정**하기 위하여<br/>
`processors`인자에 `list`형식으로 `ResizeToFill`함수 사용
```python
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blog_img")
    image_thumbnail = ImageSpecField(
        source="image", processors=[ResizeToFill(120, 60)]
    )

```

5. html에 Thumbnail 띄우기

기존의 이미지를 띄우는 것과 동일<br/>
이미지를 띄울땐 뒤에 **꼭** `.url`을 붙여야한다.
```html
<img src="{{ blog.image_thumbnail.url }}">
```

### ImageSpecField함수 속성
확장자 지정
```python
thumbnail = ImageSpecField(..., format='JPEG')
```

압축 방식 지정
```python
thumbnail = ImageSpecField(..., options={
    'quality': 60,
})
```

...etc
