Задание 1.
SELECT
employees.id AS employee_id,
employees.name AS employee_name,
ARRAY_AGG(departments.id) AS parent_department_ids
FROM
employees
INNER JOIN
departments
ON
employees.department_id = departments.parent_id
GROUP BY
employees.id, employees.name;


