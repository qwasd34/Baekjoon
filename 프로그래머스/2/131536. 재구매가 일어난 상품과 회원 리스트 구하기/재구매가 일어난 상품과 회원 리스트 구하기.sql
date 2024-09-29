-- 코드를 입력하세요
WITH tmp AS
(SELECT user_id, product_id , count(*) as cnt
FROM online_sale 
GROUP BY 1,2
Having cnt>=2
ORDER BY user_id)


SELECT user_id, product_id FROM tmp
ORDER BY 1 , 2 DESC