-- 1. 모든 아티스트 정보 조회
SELECT
  *
FROM
  artists;

-- 2. 모든 데이터 수를 조회.
SELECT
  COUNT(*)
FROM
  artists;

-- 3. Name이 AC/DC인 정보 조회.
SELECT
  *
FROM
  artists
WHERE
  Name ='AC/DC';

-- 4. artistid와 Name만 출력.
SELECT
  artistid, Name
FROM
  artists;

-- 5. Name이 Gilberto Gil 이거나 Ed Motta
SELECT
  *
FROM
  artists
WHERE
  Name ='Gilberto Gil' OR Name = 'Ed Motta';

-- 6. Name 기준 내림차순 정렬
SELECT
  *
FROM
  artists
ORDER BY
  Name DESC;

-- 7. 이름이 Vinicius로 시작, 2개까지만 출력.
SELECT
  *
FROM
  artists
WHERE
  Name like 'Vinícius%'
LIMIT
  2;

-- 8. ArtistId가 50번부터 70번 까지 데이터 조회, ArtistsId만 출력
SELECT
  artistid
FROM
  artists
WHERE
  artistid BETWEEN 50 AND 70;