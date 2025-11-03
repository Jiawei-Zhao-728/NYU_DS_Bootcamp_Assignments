-- SQL Solution for LeetCode 185: Department Top Three Salaries
-- Use DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) to rank salaries within each department
WITH RankedSalaries AS (
    SELECT
        e.name,
        e.salary,
        e.departmentId,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Employee e
)
SELECT
    d.name AS Department,
    r.name AS Employee,
    r.salary AS Salary
FROM RankedSalaries r
JOIN Department d ON r.departmentId = d.id
WHERE r.salary_rank <= 3;

