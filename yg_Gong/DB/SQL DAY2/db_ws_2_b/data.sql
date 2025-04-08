--result_01
SELECT
  InvoiceId,
  InvoiceDate
FROM invoices;

--result_02
SELECT *
FROM invoices
WHERE 
  BillingCountry = 'USA' AND
  Total > 10;

--result_03
SELECT *
FROM invoices
WHERE 
  BillingCity = 'London' OR
  BIllingCity = 'Berlin';

--result_04
SELECT *
FROM invoices
WHERE Total = ( SELECT max(total)
                FROM invoices);

--result_05
SELECT *
FROM invoices
WHERE
  InvoiceDate > '2013-03-31' AND
  Total >3;

--result_06
SELECT *
FROM invoices
WHERE 
  BillingCountry = 'USA' AND
  BillingState = 'CA' AND
  Total >= 10;
--result_07
SELECT *
FROM invoices
WHERE 
  BillingCountry = 'Canada' AND
  BillingState = 'ON' AND
  BillingCity = 'Toronto';

--result_08
SELECT *
FROM invoices
WHERE
  InvoiceDate < '2023-01-01' AND
  (Total >= 50 OR
   BillingCountry = 'Brazil');