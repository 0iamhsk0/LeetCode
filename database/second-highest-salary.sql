WITH ranked AS (
  SELECT
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
)
select case
    when exists (select 1 from ranked where rnk = 2)
    then (select salary from ranked where rnk = 2 limit 1)
    else NULL
        end as SecondHighestSalary
