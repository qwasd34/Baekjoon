-- 코드를 작성해주세요
WITH tmp AS (SELECT t2.ID, t1.fish_type, t1.max_length
FROM (SELECT fish_type, max(length) as max_length FROM fish_info GROUP BY 1) t1 INNER JOIN fish_info t2
ON t1.fish_type = t2.fish_type AND t1.max_length = t2.length)

SELECT ID, fish_name, max_length as length
FROM tmp t JOIN fish_name_info fname
ON t.fish_type = fname.fish_type



