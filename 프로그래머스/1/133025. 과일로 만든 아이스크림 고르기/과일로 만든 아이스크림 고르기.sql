select flavor
from FIRST_HALF 
where flavor in (
    select flavor
    from ICECREAM_INFO 
    where INGREDIENT_TYPE = 'fruit_based'
) and TOTAL_ORDER > 3000
order by TOTAL_ORDER desc