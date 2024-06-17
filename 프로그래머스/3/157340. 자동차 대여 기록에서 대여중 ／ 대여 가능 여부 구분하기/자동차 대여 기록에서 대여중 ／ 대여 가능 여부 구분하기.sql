select car_id,case when sum(CASE
            WHEN END_DATE < to_date('2022-10-16', 'yyyy-mm-dd') or START_DATE > to_date('2022-10-16', 'yyyy-mm-dd')
            THEN 0
            else 1
           END) > 0 then '대여중' else '대여 가능' end AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by 1 desc