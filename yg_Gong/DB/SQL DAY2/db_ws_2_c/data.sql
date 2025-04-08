--result_a
SELECT 
  BillingCountry,
  SUM(total) as TotalSales
FROM invoices
GROUP BY BillingCountry;

--result_b
SELECT 
  strftime('%Y', InvoiceDate) as Year,
  SUM(total) as TotalSales
FROM invoices
GROUP BY Year;

--result_c
SELECT 
  BillingState,
  SUM(Total) as TotalSales
FROM invoices
WHERE 
  BillingCountry = 'USA' AND
  InvoiceDate >= '2010-01-01'
GROUP BY BillingState;

--result_d
SELECT 
  BillingCountry,
  Max(total) as MaxOrderAmount
FROM invoices
WHERE 
  BillingCountry = 'Germany' OR
  BillingCountry = 'France'
GROUP BY "BillingCountry";