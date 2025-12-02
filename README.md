# Follow these steps to run your Medical Store Management System project successfully.
1) Install Required Dependencies

   Make sure you have Python installed (Phycharm).
   
   pip install mysql-connector-python

   pip install tkinter

2) Set Up MySQL Database

   Open MySQL Workbench or phpMyAdmin (XAMPP) or Command Line.

   Run the following SQL query to create a database:

   "CREATE DATABASE chetanvarade123; "
   
   Update the database connection in your Python program:

   Change "database="chetanvarade123" in self.create_db() method if needed.

   Create necessary tables automatically (handled in create_db() function).

3) Run this Python Program
