-- 코드를 작성해주세요
WITH ecoli AS (SELECT id, parent_id, size_of_colony, YEAR(differentiation_date) as date FROM ecoli_data)

SELECT t3.date as YEAR, (t1.max_c-t3.size_of_colony) as YEAR_DEV, t3.ID
FROM (SELECT date, 
      MAX(size_of_colony) as max_c FROM ecoli GROUP BY 1) t1 
      JOIN ecoli t2 ON t1.date=t2.date
      AND 
      t1.max_c=t2.size_of_colony
      RIGHT JOIN ecoli t3 ON t1.date=t3.date
ORDER BY 1 , 2 