-- 데이터 조회용
SELECT
  *
FROM
  invoices;

-- 1. "BillingCountry"를 기준으로 그룹화하고, 각 나라별 총판매액을 계산하여 조회
SELECT
  BillingCountry, SUM(Total) AS 'TotalSales'
FROM
  invoices
GROUP BY
  BillingCountry

-- 2. "InvoiceDate"를 연도별로 그룹화하고, 각 연도별 총판매액을 계산하여 조회
SELECT
  strftime('%Y', InvoiceDate) AS 'InvoiceYear',
  SUM(Total) AS 'TotalSales'
FROM
  invoices
GROUP BY
  strftime('%Y', InvoiceDate)

-- 3.  "BillingCountry"이 'USA'이고 "InvoiceDate"가 2010년 01월 01 이후인 레코드를 "BillingState"를 기준으로 그룹화하고, 각 주별로 총 주문 금액을 계산하여 조회
SELECT
  BillingState,
  SUM(Total) AS TotalSales
FROM
  invoices
WHERE
  InvoiceDate > '2010-01-01' AND BillingCountry = 'USA'
GROUP BY
  BillingState;

-- 4. "BillingCountry"이 'Germany'이거나 "BillingCountry"이 'France'인 레코드를 "BillingCountry"를 기준으로 그룹화하고, 각 나라별로 최대 주문 금액을 계산하여 조회
SELECT
  BillingCountry,
  MAX(Total) AS 'MaxOrderAmount'
FROM
  invoices
WHERE
  BillingCountry = 'Germany' OR BillingCountry = 'France'
GROUP BY
  BillingCountry