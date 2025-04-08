SELECT
  *
FROM
  users
WHERE
  age >= 30 AND balance >= 1000;

SELECT
  *
FROM
  users
WHERE
  balance <= 1000 AND age <= 20;

SELECT
  *
FROM
  users
WHERE
  first_name LIKE '현%' AND country = '제주특별자치도'
ORDER BY
  age DESC
LIMIT
  1;

SELECT
  *
FROM
  users
where
  last_name ='박' AND age >= 25
ORDER BY
  age
LIMIT
  1;

SELECT
  *
FROM
  users
WHERE
  first_name = '재은' OR first_name = '영일'
ORDER BY
  balance DESC
LIMIT
  1;

SELECT
  first_name, last_name, age, phone, country, balance AS 'max_balance'
FROM
  users
GROUP BY
  country
HAVING
  MAX(balance)
ORDER BY
  max_balance DESC;

SELECT
  *
FROM
  users
WHERE
  -- 서브 쿼리. 나이가 30세 이상이면서 balance가 30세 이상인 사람들의 평균 balance값보다 높은 조건.
  age >= 30 AND balance > (SELECT AVG(balance) FROM users WHERE age >= 30);