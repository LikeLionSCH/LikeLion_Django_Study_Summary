## 7주차 - 4. API 실습

### 1. [네이버 클라우드 플랫폼](https://www.ncloud.com) 회원가입

### 2. 네이버 Maps API 이용 신청 하기

### 3. 어플리케이션 등록 (Web Dynamic Map 사용)

### 4. 인증 정보 확인 및 저장

### 5. 예시 코드 사용해보기
`Client_id`에는 인증 정보에 있는 값 사용<br/>

**지도 띄워보기**
```html
...

<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
    <title>간단한 지도 표시하기</title>
    <script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=Client_id"></script>
</head>

<body>

    ...

    <div id="map" style="width:50%;height:400px;"></div>

    <script>
        var mapOptions = {
            center: new naver.maps.LatLng(37.3595704, 127.105399),
            zoom: 12
        };

        var map = new naver.maps.Map('map', mapOptions);
    </script>
</body>

</html>
```

**마커 및 위치 정보 띄워보기**
```html
...

<!DOCTYPE html>
<html>

<head>
    ...
</head>

<body>

    ...

    <div id="map" style="width:50%;height:400px;"></div>

    <script>
    var HOME_PATH = window.HOME_PATH || '.';

    var cityhall = new naver.maps.LatLng(37.5666805, 126.9784147),
        map = new naver.maps.Map('map', {
            center: cityhall.destinationPoint(0, 500),
            zoom: 10
        }),
        marker = new naver.maps.Marker({
            map: map,
            position: cityhall
        });

    var contentString = [
        '<div class="iw_inner">',
        '   <h3>서울특별시청</h3>',
        '   <p>서울특별시 중구 태평로1가 31 | 서울특별시 중구 세종대로 110 서울특별시청<br />',
        '       <img src="' + HOME_PATH + '/img/example/hi-seoul.jpg" width="55" height="55" alt="서울시청" class="thumb" /><br />',
        '       02-120 | 공공,사회기관 &gt; 특별,광역시청<br />',
        '       <a href="http://www.seoul.go.kr" target="_blank">www.seoul.go.kr/</a>',
        '   </p>',
        '</div>'
    ].join('');

    var infowindow = new naver.maps.InfoWindow({
        content: contentString
    });

    naver.maps.Event.addListener(marker, "click", function(e) {
        if (infowindow.getMap()) {
            infowindow.close();
        } else {
            infowindow.open(map, marker);
        }
    });

    infowindow.open(map, marker);
    </script>
</body>

</html>
```
