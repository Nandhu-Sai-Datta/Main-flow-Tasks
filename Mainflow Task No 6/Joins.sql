-- Sample Tables (Assuming a store database)

CREATE TABLE Customers1 (
  CustomerID INT PRIMARY KEY,
  CustomerName VARCHAR(50),
  City VARCHAR(50)
);

CREATE TABLE Orders (
  OrderID INT PRIMARY KEY,
  CustomerID INT,  -- Foreign key referencing Customers.CustomerID
  OrderDate DATE,
  Amount DECIMAL(10,2),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Inner Join Example

SELECT Customers.CustomerName, Orders.OrderID, Orders.OrderDate, Orders.Amount
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
