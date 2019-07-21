## 2.5주차 - Git

**개발자**로서 `Git`을 다루는 능력은 필수<br/>
명령어가 **어떤 기능을 하는지**만 알고가자

### Git
분산 버전 관리 시스템<br/>
1. 내 코드를 저장해주고
2. 이전 상태로 되돌려주고
3. 여럿이 같이 개발할 수 있게 해줌

### Github
`Git`을 이용한 **오픈소스** 저장소<br/>

오픈소스
> (저작자의 권리는 인정하는) 너, 나, 우리의 코드

### Git - Basic
프로젝트 작업 공간 ➤ Staging Area<br/>
`Add` 한다.<br/>

Staging Area ➤ Repository(저장소)<br/>
`Commit` 한다.

**Commit**
> 저장소의 Check point 어떤 변경사항들이 저장되었는지 기록

### 명령어 정리
`Git` 저장소 초기화 (프로젝트 초기에 한 번만)
```
$ git init
```

저장소 상태 체크, 현재 프로젝트 변경사항 확인
```
$ git status
```

모든 파일을 staging area로 올리기
```
$ git add .
$ git add -A
$ git add --all
```

특정 파일을 staging area로 올리기
```
$ git add <file name>
```

저장소로 `commit` 하기
```
$ git commit -m <comment>
```

로컬 Repository ➤ 온라인 Repository
```
$ git remote add origin <깃헙 주소>
$ git push (-u origin master)
```

### gitignore
`Git`에 올리고 싶지 않은 것들을 미리 필터링


### 추가로 알면 좋은 것
협업을 위한 도구로서의 `Git`<br/>
ex) branch, merge...
