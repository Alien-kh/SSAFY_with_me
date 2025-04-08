-- 1. zoo 테이블에 species 열을 추가한다. 값은 Text를 받을 수 있어야 한다.
ALTER TABLE
  zoo
ADD COLUMN
  species VARCHAR NOT NULL DEFAULT 'default value';

-- 2. zoo 테이블에 삽입되어 있는 모든 데이터에 species 값을 추가하여 수정
UPDATE
  zoo
SET
  -- 바꿀 종 이름. (사진 참고)
  species = 'Cebut capucinus'
WHERE
  -- 나는 name 값 기준으로 바꿨음. ex) Lion, Elephant, Giraffe, Monkey
  name = 'Monkey';

-- 3. 모든 데이터의 height 값을 2.54가 곱해진 값으로 수정.
UPDATE
  zoo
SET
  height = height * 2.54;

SELECT
  *
FROM
  zoo;