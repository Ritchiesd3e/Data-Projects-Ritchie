--Problem Statement
You have a SalesData table with Year, Quarter, and Revenue. To summarize revenue by year and quarter:

--create table
CREATE TABLE SalesData (
    Year INT,
    Quarter VARCHAR(2),
    Revenue DECIMAL(10, 2)
);

--Insert
INSERT INTO SalesData (Year, Quarter, Revenue) VALUES
(2023, 'Q1', 5000),
(2023, 'Q2', 7000),
(2023, 'Q3', 8000),
(2023, 'Q4', 6000),
(2024, 'Q1', 5500),
(2024, 'Q2', 7200);

--solution:
SELECT Year,
       [Q1], [Q2], [Q3], [Q4]
FROM 
    (SELECT Year, Quarter, Revenue
     FROM SalesData) AS SourceTable
PIVOT
    (SUM(Revenue)
     FOR Quarter IN ([Q1], [Q2], [Q3], [Q4])) AS PivotTable;
