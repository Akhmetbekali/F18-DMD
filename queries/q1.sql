/* 3.1 */
select car.car_id
from cars as car,
     orders as o,
     transactions as t,
     customers as c
where c.name = 'Joo Lee'
  AND c.customer_id = t.customer_id
  AND t.transaction_id = o.transaction_id
  AND car.car_id = o.car_id
  AND car.color = 'white'
  AND car.plate_number like '%AA%';