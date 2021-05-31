from neo4j import GraphDatabase
from datetime import date, timedelta,datetime
import os
import json
def worker():
         file_name = "abhishek" + "." + str(date.today()) + ".json"
         file = open(file_name) 
         data = json.load(file)
         return data
class data_processor:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
       

    def fire_up(self, abc):
        with self.driver.session() as session:
            session.write_transaction(self.for_apps,abc)
            session.write_transaction(self.for_users,abc)
            session.write_transaction(self.create_relationship,abc)
            
            
    
    @staticmethod
    def for_apps(tx,data):
        
        for i in range(0,6):
            results = tx.run("CREATE (ap:App{IdMaster: $app_name,AppCategory: $app_category})"
                                ,app_name = data['usages'][i]['app_name'],app_category = data['usages'][i]['app_category']
                             )
        return results.single()
    
    @staticmethod
    def for_users(tx,data):
        print("yes its running")
        
        
        result = tx.run("CREATE (u:user{IdMaster: $user_id})  "
                        "CREATE(de:Device{IdMaster: $os}) "
                        "CREATE(BR:Brand{IdMaster: $brand})"
                         "CREATE(ope:opera{os:$os}) "
                          ,user_id = data['user_id'] , os = data['device']['os'] , brand = data['device']['brand']
                         )
        return result.single()
    @staticmethod
    def create_relationship(tx,data):
        
        for i in range(0,6):
             result = tx.run(
                             "CREATE bc =  (u)-[used:USED{TimeCreated:$cur_time,TimeEvent: $usages_date,UsageMinutes: $minutes_used}]->(ap)-[on:ON{TimeCreated: $cur_time}]->(de)-[ha:HAVING{TimeCreated: $cur_time}]->(ope) "
                                , os = data['device']['os'] , cur_time = datetime.today() , usages_date = data['usages_date'], minutes_used = data['usages'][i]['minutes_used']

                        
                             )
        return result.single()


        
        


   


def runit():

    intialize = data_processor("bolt://localhost:7687", "neo4j", "a")
    to_process = worker()
    intialize.fire_up(to_process)
    intialize.close()
