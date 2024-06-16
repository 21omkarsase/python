# Self Join
	A self-join is when a table is joined with itself. This can be useful when you have hierarchical data or need to compare rows within the same table.

	CREATE TABLE employees (
	    employee_id INT PRIMARY KEY,
	    employee_name VARCHAR(50),
	    manager_id INT,
	    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
	);

	To get employees and their manager names

	SELECT e1.employee_name AS employee, e2.manager AS manager FROM employee as e1 
	SELF JOIN
	employee AS e2 ON e1.manager_id == e2.employee_id

# Corss Join
	A CROSS JOIN returns the Cartesian product of two tables. It combines every row from the first table with every row from the second table, resulting in a large result set.

	SELECT c.customer_name, o.order_id FROM customer AS c 
	CORSS JOIN orders