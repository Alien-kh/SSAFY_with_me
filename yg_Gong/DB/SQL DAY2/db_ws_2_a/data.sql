--result_01
SELECT *
FROM artists;

--result_02
SELECT
  count(*)
FROM artists;

--result_03
SELECT
  ArtistId,
  Name
FROM artists
WHERE name = 'AC/DC';

--result_04
SELECT
  artistId,
  Name
FROM artists;

--result_05
SELECT 
  ArtistId,
  Name
FROM artists
WHERE 
  Name = 'Gilberto Gil' OR
  Name = 'Ed Motta';

--result_06
SELECT *
FROM artists
ORDER BY name DESC;

--result_07
SELECT
  ArtistId
FROM artists
WHERE 
  artistId >=50 AND
  artistId <= 70;