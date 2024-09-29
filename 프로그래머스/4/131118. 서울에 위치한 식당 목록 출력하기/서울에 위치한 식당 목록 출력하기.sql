-- 코드를 입력하세요
SELECT t1.REST_ID, t1.REST_NAME, t1.FOOD_TYPE, t1.FAVORITES,
t1.ADDRESS, ROUND(AVG(t2.review_score),2) as SCORE
FROM rest_info t1 LEFT JOIN rest_review t2
ON t1.rest_id = t2.rest_id
GROUP BY 1
HAVING address LIKE('서울%') AND score IS NOT NULL
ORDER BY SCORE DESC , favorites DESC

# SELECT *
# FROM rest_info t1 LEFT JOIN rest_review t2
# ON t1.rest_id = t2.rest_id
# WHERE address LIKE('%서울%')