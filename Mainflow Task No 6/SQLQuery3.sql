CREATE TABLE Employees (
  EmployeeID INT PRIMARY KEY,
  Name VARCHAR(50),
  DepartmentID INT,
  SalCode VARCHAR(10),
);

CREATE INDEX idx_employees_salcode ON Employees(SalCode);
