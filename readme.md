# 예제로 배우는 Django 4 & 5
### 저자: 안토니오 멜레

해당 책 내용 클론 코딩

### 디렉터리 구분
- mysite : 블로그 애플리케이션 (1~3 장)

### Docker 실행
- PostGreSQL : ` docker compose -f postgres-docker-compose.yml up -d`

### .env
- 각 디렉토리별 example_env.txt 파일 참조

### Fixtures
- 각 디렉토리별 json 데이터 참조

### Django 명령어
- 개발 서버 시작 : `python manage.py runserver`
- 쉘 시작 : `python manage.py shell`
- 마이그레이션 make : `python manage.py makemigrations`
- 마이그레이션 : `python manage.py migrate`
- 데이터 덤프 : `python manage.py dumpdata --indent=2 --output={filename}.json`
- 데이터 덤프 UTF-8 : `python -Xutf8 manage.py dumpdata --indent=2 --output={filename}.json`
- 데이터 가져오기 : `python manage.py loaddata {fixtures}`

### 참조 URL
- 플루언트 Reader 다운로드 링크 : https://github.com/yang991178/fluent-reader/releases

### 참고 개념
트라이그램 유사성: 트라이그램은 세 개의 연속된 문자 그룹.
두 문자열이 공유하는 트라이그램 수를 세어 두 문자열의 유사성을 측정이 가능하다.
많은 언어에서 단어의 유사성을 측정하는데 매우 효과적이다.
