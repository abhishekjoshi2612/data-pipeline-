from neo4j import GraphDatabase
from datetime import date, timedelta,datetime
import os
import json
#functions for loading and sending data for processing into neo4j database
def abhishek():
         file_name = "abhishek" + "." + str(date.today()) + ".json"
         file = open(file_name) 
         data = json.load(file)
         return data
def vinit():
         file_name = "vinit" + "." + str(date.today()) + ".json"
         file = open(file_name) 
         data = json.load(file)
         return data
def christian():
         file_name = "christian" + "." + str(date.today()) + ".json"
         file = open(file_name) 
         data = json.load(file)
         return data
def guilermo():
         file_name = "guilermo" + "." + str(date.today()) + ".json"
         file = open(file_name) 
         data = json.load(file)
         return data
def eily():
         file_name = "eily" + "." + str(date.today()) + ".json"
         file = open(file_name) 
         data = json.load(file)
         return data

#class which processes or intialize data into neo4j db
class data_processor:
#intialize function which takes password and username
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
       
#function for running all the transactions first generating nodes for apps then for users then create relationship 
    def fire_up(self, data):
        with self.driver.session() as session:
            session.write_transaction(self.for_apps,data)
            session.write_transaction(self.for_users,data)
            session.write_transaction(self.create_relationship,data)
            
            
    
    @staticmethod
    def for_apps(tx,data):
    #create nodes for all 6 apps
        for i in range(0,6):
            results = tx.run("CREATE (ap:App{IdMaster: $app_name,AppCategory: $app_category})"
                                ,app_name = data['usages'][i]['app_name'],app_category = data['usages'][i]['app_category']
                             )
        return results.single()
    
    @staticmethod
    def for_users(tx,data):
        
        
    #create nodes for all 5 users and operating system node
        result = tx.run("CREATE (u:user{IdMaster: $user_id})  "
                        "CREATE(de:Device{IdMaster: $os}) "
                        "CREATE(BR:Brand{IdMaster: $brand})"
                         "CREATE(ope:opera{os:$os}) "
                          ,user_id = data['user_id'] , os = data['device']['os'] , brand = data['device']['brand']
                         )
        return result.single()
    @staticmethod
    #create relationship between all these for one user at a time
    def create_relationship(tx,data):
        
        for i in range(0,6):
             result = tx.run(
                             "CREATE bc =  (u)-[used:USED{TimeCreated:$cur_time,TimeEvent: $usages_date,UsageMinutes: $minutes_used}]->(ap)-[on:ON{TimeCreated: $cur_time}]->(de)-[ha:HAVING{TimeCreated: $cur_time}]->(ope) "
                                , os = data['device']['os'] , cur_time = datetime.today() , usages_date = data['usages_date'], minutes_used = data['usages'][i]['minutes_used']

                        
                             )
        return result.single()


        
        


   


def runit():
#intialize the function my password is "a" and username was "neo4j" 
    intialize = data_processor("bolt://localhost:7687", "neo4j", "a")
#now for each user load their data in "to_process" variable and then feed to class function intialize.fire_up
    to_process = abhishek()
    intialize.fire_up(to_process)
    to_process = vinit()
    intialize.fire_up(to_process)
    to_process = guilermo()
    intialize.fire_up(to_process)
    to_process = eily()
    intialize.fire_up(to_process)
    to_process = christian()
    intialize.fire_up(to_process)
#finally call the function to close after processing all data
    intialize.close()
