/* 3.4 */
select t.date
from transactions as t,
     customers as c
where name = (%s)
  AND t.type = 'Charge';