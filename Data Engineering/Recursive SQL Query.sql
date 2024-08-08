--Question: Retrieve a hierarchical list of employees and their managers, starting from the top-level manager?
-- Create Table:
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    ManagerID INT NULL,
    EmployeeName NVARCHAR(100),
    Designation VARCHAR(100)
);
-- Insert Sample Data:
INSERT INTO Employees (EmployeeID, ManagerID, EmployeeName, Designation) VALUES
(1, NULL, 'Alice Smith', 'CEO'),
(2, 1, 'Bob Johnson', 'CTO'),
(3, 1, 'Carol Davis', 'CFO'),
(4, 2, 'Dave Wilson', 'Lead Developer'),
(5, 2, 'Eva Brown', 'Senior Developer'),
(6, 3, 'Frank White', 'Finance Manager'),
(7, 4, 'Grace Green', 'Developer'),
(8, 5, 'Hank Black', 'Developer');

--Solution:
-- Recursive Query
WITH RecursiveOrgChart AS (
    -- Anchor Member: Start with top-level managers
    SELECT EmployeeID, ManagerID, EmployeeName, Designation, 0 AS Level
    FROM Employees
    WHERE ManagerID IS NULL

    UNION ALL

    -- Recursive Member: Get employees reporting to those in the previous level
    SELECT e.EmployeeID, e.ManagerID, e.EmployeeName, e.Designation, ro.Level + 1 AS Level
    FROM Employees e
    INNER JOIN RecursiveOrgChart ro ON e.ManagerID = ro.EmployeeID
)
-- Final Query: Retrieve and display the hierarchy

SELECT EmployeeID, ManagerID, EmployeeName, Designation, Level
FROM RecursiveOrgChart
ORDER BY Level, ManagerID, EmployeeID;
