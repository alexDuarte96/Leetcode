SELECT MAX(salary) SecondHighestSalary
FROM Employee
WHERE
  salary NOT IN(
    SELECT MAX(Salary)
    FROM Employee
  )
