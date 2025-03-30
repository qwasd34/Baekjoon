-- 코드를 입력하세요
SELECT car_id, ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) as average_duration
FROM car_rental_company_rental_history
GROUP bY 1
HAVING average_duration>=7
ORDER By 2 DESC , 1 DESC

#with t1 as (SELECT history_id, car_id, datediff(end_date,start_date)as dd from car_rental_company_rental_history)
#SELECT * from t1