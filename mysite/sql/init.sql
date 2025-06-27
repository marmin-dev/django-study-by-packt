# 유저 생성
CREATE USER blog WITH PASSWORD 'password';

# 블로그 데이터베이스 삭제
DROP database blog;

# 데이터 베이스 생성
CREATE DATABASE blog OWNER blog ENCODING 'UTF-8';

# blog 데이터베이스 사용
psql blog;

# 트라이그램 확장 사용
CREATE EXTENSION pg_trgm;