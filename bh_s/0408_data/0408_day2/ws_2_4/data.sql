CREATE TABLE transactions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  amount VARCHAR,
  transaction_date DATE,
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO
  transactions(amount, transaction_date, user_id)
VALUES
  (500, '2024-03-15', 1),
  (700, '2024-03-16', 2),
  (200, '2024-03-17', 1),
  (1000, '2024-03-18', 3);

SELECT
  first_name, last_name, amount, transaction_date
FROM
  users
INNER JOIN
  transactions ON users.id = transactions.user_id;

SELECT
  first_name, last_name, amount, transaction_date
FROM
  users
INNER JOIN
  transactions ON users.id = transactions.user_id
WHERE
  transaction_date > '2024-03-16';

SELECT
  first_name, last_name, SUM(amount) AS 'total_amount'
FROM
  users
INNER JOIN
  transactions ON users.id = transactions.user_id
GROUP BY
  user_id;