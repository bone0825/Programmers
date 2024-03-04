-- 코드를 입력하세요
SELECT MEMBER_ID , MEMBER_NAME, GENDER, concat(substr(DATE_OF_BIRTH,1,11))
from MEMBER_PROFILE 
where TLNO is not null and substr(DATE_OF_BIRTH,6,2) = 3 and GENDER = 'W'
order by MEMBER_ID