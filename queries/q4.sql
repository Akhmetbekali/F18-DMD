/* 3.4 */
select t.date
from transactions as t,
     customers as c
where name = 'Manuel Mazzara'
  AND t.type = 'Charge';