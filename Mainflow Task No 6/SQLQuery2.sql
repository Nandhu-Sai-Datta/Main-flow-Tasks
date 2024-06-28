
select * from Customers
INSERT INTO Customers (CustomerID, CustomerName, Email, Phone)
VALUES (1001, 'John Doe', 'john.doe@example.com', '123-456-7890');

UPDATE Customers
SET Email = 'jane.smith@example.com'
WHERE CustomerID = 1002;

DELETE FROM Customers
WHERE Phone = '123-456-7890';


SELECT CustomerName, Email
FROM Customers;

SELECT *
FROM Customers
WHERE CustomerName LIKE '%Smith%';


SELECT *
FROM Customers
WHERE Color = 'Red';

