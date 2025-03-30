with F1 as (SELECT count(*) as fish_count , fish_type
FROM fish_info
GROUP By 2)

select fish_count, fish_name FROM  F1 left join fish_name_info f2
ON F1.fish_type=f2.fish_type
ORDER BY fish_count DESC