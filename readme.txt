* Introduction
* Requirements
* Recommended Modules
* Installation
* VERY IMPORTANT NOTE
* Configuration
* Maintainer


INTRODUCTION 
-------------
This program is used for running a data pipeline using APACHE AIRFLOW ,NEO4J DATABASE and python scripts.

Program was originally made on/using :-
Python = 3.8
AIRFLOW = 2.1.0(requires python version <= 3.8)
NEO4J = 4.1
OS = UBUNTU 20.04.2 LTS


REQUIREMENTS
-------------
for Airflow Installation and checking requirements consider :-
https://airflow.apache.org/docs/apache-airflow/stable/installation.html

for Neo4j Installation and checking requirements consider :-
https://neo4j.com/docs/operations-manual/current/installation/
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-neo4j-on-ubuntu-20-04

for Python Installation and checking requirements consider :-
https://docs.python.org/3/using/index.html



RECOMMENDED MODULES
-------------------

NEO4J :- pip install neo4j (IMPORTANT )

apache-airflow :- pip install apache-airflow

VERY IMPORTANT NOTE
-------------------
Consider changing Neo4j password before first run and intialize it into neo_4j.py file line 95 (IMPORTANT)


CONFIGURATION
-------------
Consider having admin privileges while installation

Change Neo4j password before first run and intialize it into neo_4j.py file line 95 (IMPORTANT)

Use "airflow users create " command for creating user for first time

Use "cypher-shell" command for setting password for first time(IMPORTANT)

Have neo_4j.py and json_file_maker.py in same directory (IMPORTANT)

Files Should preferably in same directory as airflow.cfg file in the dags folder 

Example :-   airflow.cfg  dags
In dags :- neo_4j json_file_maker

MAINTAINER 
----------
For any additonal info 
CONTACT :- https://www.linkedin.com/in/abhishek-joshi-9350111b3
CREATER_GITHUB :- github.com/abhishekjoshi2612










