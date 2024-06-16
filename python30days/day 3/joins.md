# employee table
  | employee_id | employee_name | department_id |
  |-------------|---------------|---------------|
  | 1           | John Doe      | 1             |
  | 2           | Jane Smith    | 2             |
  | 3           | Bob Johnson   | 1             |
  | 4           | Mary Davis    | 3             |

  | department_id | department_name |
  |---------------|-----------------|
  | 1             | Sales           |
  | 2             | Marketing       |
  | 3             | Finance         |
  

## Write a SQL query to retrieve the names of employees along with their corresponding department names.

    SELECT e.employee_name, d.department_name 
    FROM employee as e
    INNER JOIN department
    ON e.employee_id == d.department_id


  | product_id | product_name | price   |
  |------------|--------------|---------|
  | 1          | Product A    | 10.00   |
  | 2          | Product B    | 15.00   |
  | 3          | Product C    | 20.00   |

  | order_id | product_id | quantity |
  |----------|------------|----------|
  | 101      | 1          | 2        |
  | 102      | 2          | 3        |
  | 103      | 3          | 1        |
  | 104      | 1          | 1        |


## Write a SQL query to retrieve the order IDs, product names, and total order amounts (price * quantity).
    
    SELECT p.product_name, p.price, p.product_name, o.order_id
    FROM product AS p
    INNTER JOIN order AS o
    ON p.product_id == o.product_id