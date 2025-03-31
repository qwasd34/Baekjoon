SELECT SUM(score) as score, he.emp_no, he.emp_name, he.position, he.email
FROM hr_employees he right join hr_grade hg
ON he.emp_no=hg.emp_no
GROUP BY 2 
order BY 1 DESC
limit 1
