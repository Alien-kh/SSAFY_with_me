ALTER TABLE
  zoo
ADD COLUMN
  species NOT NULL DEFAULT '';


UPDATE zoo
SET species = 'Panthera leo'
WHERE 
  id = 1;
UPDATE zoo
SET species = 'Loxodonta africana'
WHERE 
  id = 2;
UPDATE zoo
SET species = 'Giraffa camelopardalis'
WHERE 
  id = 3;
UPDATE zoo
SET species = 'Cebus capucinus'
WHERE 
  id = 4;

UPDATE zoo
SET height = height * 2.54;

SELECT *
FROM zoo;
  