-- SQLite
--this is a sql notebook of the process i use in the morning 
--to help me automate my morning routine with the dashboard
--i am aware there is other ways of automating this 
--feel free to use this as a template for your own automation

-- i do appreciate any feed back on how to improve this process 
-- pull requests are welcome

--Thanks for being here :)


--delete all data from the database 
-- i do this because the report i run has the same data but just added rows
-- throughout the month the number of rows just gets bigger so in order to avoid
--dealing with duplicates its simpler for me at least to just remove data 
--and repopulate it with the new CSV file
DELETE FROM employees;
delete from employee1;
delete from employee2;
DELETE from employee3;
delete from employee4;
delete from employee5;

--repopulate data in termincal sqlite3
cd /WORKCSV/newfold/apps

sqlite3 
.open
.mode csv
.import employee.csv employees

--after the above step please delete all employee tables 
--in sql browser GUI is where i do this process as it is just there



--seperate  data into employee tables

CREATE TABLE employee1 AS
SELECT * FROM employees
WHERE employee = 'Employee Name1';

CREATE TABLE employee2 AS
SELECT * FROM employees
WHERE employee = 'Employee Name2';

CREATE TABLE employee3 AS
SELECT * FROM employees
WHERE employee = 'Employee Name3';

CREATE TABLE employee4 AS
SELECT * FROM employees
WHERE employee = 'Employee Name4';

CREATE TABLE employee5 AS
SELECT * FROM employees
WHERE employee = 'Employee Name5';

--at this point the program is ready to run with the following command
-- "streamlit run app.py"


--date 06/29/23
--data updated 