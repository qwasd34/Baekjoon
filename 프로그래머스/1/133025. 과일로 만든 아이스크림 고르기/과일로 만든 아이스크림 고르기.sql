-- 코드를 입력하세요
SELECT t1.flavor
FROM first_half t1 LEFT JOIN icecream_info t2 
ON t1.flavor = t2. flavor 
WHERE total_order >3000 and ingredient_type='fruit_based'
ORDER BY total_order desc

# SELECT *
# FROM first_half
# WHERE total_order > 3000