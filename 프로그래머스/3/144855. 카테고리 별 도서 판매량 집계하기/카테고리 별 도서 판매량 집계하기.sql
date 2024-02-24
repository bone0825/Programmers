-- 코드를 입력하세요
select B.CATEGORY, sum(SALES) AS TOTAL_SALES from BOOK AS B left join BOOK_SALES AS S on  B.book_id=S.book_id 
where SALES_DATE like "2022-01%" group by B.CATEGORY order by 1