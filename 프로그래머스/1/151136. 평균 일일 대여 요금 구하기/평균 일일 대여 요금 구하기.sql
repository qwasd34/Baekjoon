-- 코드를 입력하세요
SELECT round(sum(daily_fee)/count(*),0) as AVERAGE_FEE
FROM car_rental_company_car
WHERE car_type='SUV'
