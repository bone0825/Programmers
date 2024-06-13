-- 코드를 입력하세요
SELECT order_id, product_id, to_char(out_date,'yyyy-mm-dd') AS out_date, '출고완료' AS 출고여부
FROM FOOD_ORDER
WHERE out_date <= '01/MAY/22'

UNION

SELECT order_id, product_id, to_char(out_date,'yyyy-mm-dd') AS out_date, '출고미정' AS 출고여부
FROM FOOD_ORDER
WHERE out_date IS NULL

UNION

SELECT order_id, product_id, to_char(out_date,'yyyy-mm-dd') AS out_date, '출고대기' AS 출고여부
FROM FOOD_ORDER
WHERE out_date > '01/MAY/22'

ORDER BY 1;