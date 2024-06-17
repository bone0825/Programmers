-- 코드를 입력하세요

-- order by 순서 조심
select * from(
SELECT AI.NAME, AI.DATETIME
FROM ANIMAL_INS AI, ANIMAL_OUTS AO
WHERE AI.ANIMAL_ID = AO.ANIMAL_ID(+)
and AO.animal_id is null
order by 2 )
where ROWNUM <= 3;