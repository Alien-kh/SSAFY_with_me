SELECT
  genre, COUNT(*)
FROM
  songs
GROUP BY
  genre;

SELECT
  genre, COUNT(*), AVG(duration)
FROM
  songs
GROUP BY
  genre;