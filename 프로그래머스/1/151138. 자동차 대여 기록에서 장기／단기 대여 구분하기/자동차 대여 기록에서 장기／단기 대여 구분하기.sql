-- 코드를 입력하세요
SELECT  HISTORY_ID,
        CAR_ID, 
        to_char(START_DATE,'yyyy-mm-dd') as START_DATE, 
        to_char(END_DATE,'yyyy-mm-dd') as END_DATE,
CASE 
    WHEN (END_DATE+ 1 - START_DATE) >= 30 THEN '장기 대여'
    ELSE '단기 대여' 
END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE to_char(START_DATE,'yyyymm') = '202209'
order by 1 desc