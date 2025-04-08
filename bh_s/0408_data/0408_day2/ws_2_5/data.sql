INSERT INTO
  employees (name, salary, age, departmentId)
VALUES
  ('김구', 126000, 29, 2),
  ('유관순', 82000, 41, 4),
  ('이규보', 1700, 77, 1),
  ('이순신', 23000, 37, 3);

SELECT
  departments.name,
  employees.name AS 'oldest_employee', 
  MAX(employees.age) AS 'max_age',
  AVG(age) AS 'avg_age'
FROM
  employees
INNER JOIN departments
  ON employees.departmentId = departments.id
GROUP BY
  departments.name;


SELECT
  departments.name,
  employees.name AS 'highest_paid_employee', 
  MAX(employees.salary) AS 'max_salary'
FROM
  employees
INNER JOIN departments
  ON employees.departmentId = departments.id
GROUP BY
  departments.name;




SELECT
  departments.name,
  CASE 
    WHEN employees.age < 30 THEN 'Under 30'
    WHEN employees.age BETWEEN 30 AND 40 THEN 'BETWEEN 30-40'
    ELSE 'Over 40'
  END AS age_group,
  COUNT(*) AS num_employees
FROM
  employees
JOIN departments
  ON employees.departmentId = departments.id
GROUP BY
  departments.name,
  CASE 
    WHEN employees.age < 30 THEN 'Under 30'
    WHEN employees.age BETWEEN 30 AND 40 THEN 'BETWEEN 30-40'
    ELSE 'Over 40'
  END;


SELECT 
  departments.name AS department_name,
  AVG(employees.salary) AS avg_salary_excluding_max
FROM 
  employees
JOIN 
  departments ON employees.departmentId = departments.id
WHERE 
  employees.salary < (
    SELECT MAX(sub_employees.salary)
    FROM employees AS sub_employees
    WHERE sub_employees.departmentId = employees.departmentId
  )
GROUP BY 
  departments.name;