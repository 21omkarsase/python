# Joins
	Joins in SQL are used to combine rows from two or more tables based on a related column between them. 

## Inner Join
	An INNER JOIN returns only the rows that have matching values in both tables.

	SELECT o.order_id, c.customer_name 
	FROM orders AS o
	INNER JOIN customers AS c
	ON o.customer_id = c.customer_id


## Left Join
	A LEFT JOIN returns all the rows from the left table (table1), and the matched rows from the right table (table2). The result will contain NULL values for columns from the right table if there is no match.

	SELECT c.customer_name, c.customer_id, o.order_id, o.order_stats
	FROM customers AS c
	LEFT JOIN orders As o 
	ON c.customer_id == o.customer_id


# Right Join
	A RIGHT JOIN returns all the rows from the right table (table2), and the matched rows from the left table (table1). The result will contain NULL values for columns from the left table if there is no match.

	SELECT c.customer_name, c.customer_id, o.order_id, o_order_status 
	FROM customers AS c
	RIGHT JOIN orders AS o 
	ON c.customer_id == o.customer_id


# FULL JOIN
    A RIGHT JOIN returns all the rows from the right table (table2), and the matched rows from the left table (table1). The result will contain NULL values for columns from the left table if there is no match.


	SELECT c.customer_name, c.customer_id, o.order_id, o_order_status 
    FROM customers AS c
    FULL JOIN orders AS o 
    ON c.customer_id == o.order_id
