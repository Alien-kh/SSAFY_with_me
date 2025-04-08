-- 1. 현재 hotels 전체 데이터 조회
SELECT
  *
FROM
  hotels;

-- 2. grade 필드 값을 모두 대문자로 수정. (UPPER 함수 이용)
UPDATE
  hotels
SET
  grade = UPPER(grade);

SELECT
  grade
FROM
  hotels

CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR,
  email VARCHAR
);

-- 3. reservations 테이블을 생성
-- reservations 테이블은 hotels 테이블과 N:1 
-- hotels 테이블의 room_num 필드를 FOREIGN KEY 로 설정
-- reservations 테이블은 customers 테이블과 N:1 의 관계를 맺는다
-- ustomers 테이블의 id 필드를 FOREIGN KEY 로 설정
CREATE TABLE reservations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
  room_num INTEGER,
  check_in DATE,
  check_out DATE,
  FOREIGN KEY (room_num) REFERENCES hotels(room_num),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO
  customers (name, email)
VALUES
  ('홍길동', 'john@example.com'),
  ('박지영', 'jane@example.com'),
  ('김미영', 'alice@example.com'),
  ('이철수', 'bob@example.com');

INSERT INTO
  reservations (customer_id, room_num, check_in, check_out)
VALUES
  (1, 101, '2024-03-20','2024-03-25'),
  (2, 202, '2024-03-21','2024-03-24'),
  (3, 303, '2024-03-22','2024-03-26'),
  (4, 404, '2024-03-23','2024-03-27');

SELECT
  *
FROM
  customers;

SELECT
  *
FROM
  reservations;