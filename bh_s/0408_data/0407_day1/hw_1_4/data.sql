SELECT
  *
FROM
  tracks
WHERE
  Name LIKE '%love%';

SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1 AND Milliseconds >= 300000
ORDER BY
  UnitPrice DESC;

SELECT
  GenreId, COUNT(GenreId) AS 'TotalTracks'
FROM
  tracks
GROUP BY
  GenreId;

SELECT
  GenreId, SUM(UnitPrice) AS 'TotalPrice'
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;