# Intro
CIS556 Databases Course (UMICH).

The Course project is STARRS application for Database University.

# Summary task
The project is to implement an on-line admissions and graduation clearance system for graduate students applying 
to the University. 

The current system allows students to apply online but the process by which the faculty reviews the applications 
is a paper process. For simplicity, in this project your team will design and build a system that will automate 
the workflow process in the admissions, registration and graduation system for Master’s degree students. 

You can implement this project using any DBMS the team has access to, you must be able to demo the application 
in the final presentation.

# STARRS Implementation
STARRS implemented as Windows Python application. 

We're using PySide for UI and sqlite for the database. 

This setup provides extremely easy workflow with full functionality of the project. All components, front end, back end 
and database are ready to go without any extra steps (you just need to install pyside and sqlite to your Python).

In UI we are using data models tables that gives interactivity while retrieve or update data. Each table has 
it's own class that defines wat we see in the table and how we can change the data.

# How to run STARRS
### Install Pytnon
Go to the Random folder on Google Drive, navigate to Random/application/source/python 

Extract Pyton27.zip to C:/ and place python27.dll to C:/Windows/System32

### Download STARRS
On this page there is a green button "Code", press the button, download zip file somewhere and extract to any location 
on your HDD where you would like to keep the STARRS application, e.g. D:/projects/CIS556-main/

### Launching STARRS
Go to you app folder, e.g. D:/projects/CIS556-main/starrs/ and double click launcher.bat

Hopefully the STARRS main window will be launched and the database file will be created in 
D:/projects/CIS556-main/starrs/data/database.db
