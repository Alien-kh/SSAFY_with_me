-- 1. invoiceid, invoiceDate 열만 조회.
SELECT
  invoiceid, invoiceDate
FROM
  invoices;

-- 2. BillingCountry 가 USA 이고, Total이 10보다 큰 레코드 조회
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'USA' AND Total >= 10;

-- 3. BillingCity 가 London 이거나, Berlin 인 레코드 조회
SELECT
  *
FROM
  invoices
WHERE
  BillingCity = 'London' OR BillingCity = 'Berlin';

-- 4. Total이 가장 큰 레코드 조회
SELECT
  *
FROM
  invoices
ORDER BY
  Total DESC
LIMIT
  1;

-- 5. InvoiceDate가 2013년 3월 31일 이후이면서 Total이 3보다 큰 레코드 조회
SELECT
  *
FROM
  invoices
WHERE
  InvoiceDate > '2013-03-31' AND Total > 3;

-- 6. "BillingCountry"이 'USA'이고 "BillingState"가 'California'(CA)이며 "Total"이 10보다 큰 레코드를 조회
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'USA' AND BillingState = 'CA' AND Total > 10;

-- 7. BillingCountry"이 'Canada'이고 "BillingState"이 'Ontario'(ON)이며 "BillingCity"가 'Toronto'인 레코드를 조회
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'Canada' AND BillingState = 'ON' AND BillingCity ='Toronto';

-- 8. "InvoiceDate"가 2023년 1월 1일 이전이고 ("Total"이 50보다 이상이거나 "BillingCountry"이 'Brazil'인) 레코드를 조회
SELECT
  *
FROM
  invoices
WHERE
  InvoiceDate < '2023-01-01' AND (Total >= 50 or BillingCountry = 'Brazil');