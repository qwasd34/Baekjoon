SELECT count(*) as FISH_COUNT , MONTH(time) as MONTH  FROM fish_info 
#where length is not null
GROUP BY 2
ORDER BY 2
