-- -- 코드를 입력하세요
-- SELECT I.ANIMAL_ID, I.NAME
-- from ANIMAL_INS I, ANIMAL_OUTS O
-- where I.ANIMAL_ID = O.ANIMAL_ID and I.DATETIME > O.DATETIME
-- order by I.DATETIME

select I.ANIMAL_ID, I.NAME
from ANIMAL_INS I
where exists (select 'x'
             from ANIMAL_OUTS
             where ANIMAL_ID = I.ANIMAL_ID and
                I.DATETIME > DATETIME)
order by I.DATETIME