-- 코드를 입력하세요
SELECT  r.REST_ID,
        i.REST_NAME,
        i.FOOD_TYPE,
        FAVORITES as FAVORITES,
        i.ADDRESS,
        round(avg(r.REVIEW_SCORE),2) as SCORE
        
from REST_INFO i, REST_REVIEW r

where    i.REST_ID = r.REST_ID 
         and ADDRESS like '서울%'
group by r.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.ADDRESS, FAVORITES
order by SCORE desc, FAVORITES desc