-- 코드를 입력하세요
SELECT animal_id, name
FROM ANIMAL_INS
WHERE name LIKE '%EL%' and animal_type = 'dog'
ORDER BY 2