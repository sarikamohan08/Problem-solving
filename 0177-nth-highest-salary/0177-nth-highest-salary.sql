CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare x int;
set x=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select salary from Employee group by salary order by salary desc limit x,1
  );
END