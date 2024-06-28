CREATE TABLE Library (
  BookID INT PRIMARY KEY,
  Title VARCHAR(255),
  Author VARCHAR(100),
  BorrowerName VARCHAR(50),  -- Not normalized (redundancy)
  BorrowerPhone CHAR(12)     -- Not normalized (redundancy)
);

CREATE TABLE Books (
  BookID INT PRIMARY KEY,
  Title VARCHAR(255),
  Author VARCHAR(100)
);

CREATE TABLE Borrowers (
  BorrowerID INT PRIMARY KEY,
  BorrowerName VARCHAR(50),
  Phone CHAR(12)
);
CREATE TABLE Loans (
  LoanID INT PRIMARY KEY,
  BookID INT FOREIGN KEY REFERENCES Books(BookID),
  BorrowerID INT FOREIGN KEY REFERENCES Borrowers(BorrowerID),
  BorrowedDate DATE
);
