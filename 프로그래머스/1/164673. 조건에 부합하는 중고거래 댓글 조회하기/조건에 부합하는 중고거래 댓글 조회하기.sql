-- 코드를 입력하세요
SELECT TITLE, t1.BOARD_ID, REPLY_ID, t2.WRITER_ID, t2.CONTENTS,
DATE_FORMAT(t2.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
FROM used_goods_board t1 INNER JOIN used_goods_reply t2
ON t1.board_id = t2.board_id
WHERE t1.created_date LIKE '2022-10%'
ORDER BY t2.created_date , title 
