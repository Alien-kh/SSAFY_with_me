CREATE TABLE transactions(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  amount TEXT,
  transaction_date DATE,
  FOREIGN KEY (user_id)
    REFERENCES users(id)
);

PRAGMA foreign_keys = ON;

INSERT INTO transactions(
  user_id,
  amount,
  transaction_date
)
VALUES(
  1,
  '500',
  '2024-03-15'
),
(
  2,
  '700',
  '2024-03-16'
),
(
  1,
  '200',
  '2024-03-17'
),
(
  3,
  '1000',
  '2024-03-18'
);

SELECT
  u.first_name,
  u.last_name,
  t.amount,
  t.transaction_date
FROM users u
JOIN transactions t
  ON t.user_id = u.id;

SELECT 
  u.first_name,
  u.last_name,
  t.amount,
  t.transaction_date
FROM users u
JOIN transactions t
  ON u.id = t.user_id
WHERE
  transaction_date > '2024-03-16';

SELECT 
  u.first_name,
  u.last_name,
  SUM(t.amount) as total_amount
FROM users u
JOIN transactions t
  ON u.id = t.user_id
GROUP BY t.user_id;