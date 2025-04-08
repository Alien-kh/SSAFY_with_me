SELECT
  *
FROM
  tracks;

SELECT
  Name, Milliseconds, UnitPrice
FROM
  tracks;

SELECT
  *
FROM
  tracks
ORDER BY
  -- 오름차순은 생략가능(기본값)
  name;

SELECT
  *
FROM
  tracks
LIMIT
  10;