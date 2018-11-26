# F18 DMD Project

Gleb Petrakov (g.petrakov@innopolis.ru)  
Ali Akhmetbek (a.ahmetbek@innopolis.ru)  


#### Project structure

This project contains ER-diagram, database schema, database build and population scripts, SELECT queries and Dash-based frontend on Python to show SELECT queries.

**queries/**  
Contains all queries in separate files


**domain/**  
Contains ER-diagram and database schema


**db_population/**  
Contains scripts to populate database with sample data


**db_creation.sql**  
Script to create Postgres database


**db_queries.sql**  
All SELECT queries asked to be implemented

**main.py**  
Main interface to communicate with db by provided queries, based on Dash

**requrements.txt**  
Python requrements for the project


#### Project overview

Database chosen for implementation of ER-diagram is PostgreSQL v11.  
Queries implemented using plain SQL.  
GUI provided with Dash visualization in main.py file, just run 'python3 main.py' to start the project, install requirements first  


Database with data will be available and running till the end of semester with this credentials:


| param    | value                 |
|----------|-----------------------|
| host     | gleb.page             |
| port     | 5432                  |
| database | postgres              |
| user     | postgres              |
| password | ThisPostgresIsAwesome |


And the GUI will be awailable on **gleb.page:8050**

If it fails, write Gleb to deploy it again.

There is also Dockerfile available if you want to deploy it by yourself.
Run **docker-run.sh** to automatically build and run docker container