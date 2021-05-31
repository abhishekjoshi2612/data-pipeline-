from neo4j import GraphDatabase
from datetime import date, timedelta,datetime
import json
def worker():
         f = open('abhishek.2021-05-31.json') 
         data = json.load(f)
         print(data['user_id'])
         print(data['device']['os'])
         print(data['usages'][1])
         return data
class HelloWorldExample:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
       

    def print_greeting(self, message,abc):
        with self.driver.session() as session:
            another_greeting = session.write_transaction(self.for_apps,abc)
            greeting = session.write_transaction(self._create_and_return_greeting,abc)
           
            print(another_greeting)
            print(greeting)
    
    @staticmethod
    def for_apps(tx,data):
        mapper = {'slack' : 0,'gmail' : 1,'jira' : 2,'google drive': 3,'chrome' : 4,'spotify' : 5}
        for i in range(0,6):
            results = tx.run("CREATE (ap:App{IdMaster: $app_name,AppCategory: $app_category})"
                                ,app_name = data['usages'][i]['app_name'],app_category = data['usages'][i]['app_category']
                             )
        return results.single()
    
    @staticmethod
    def _create_and_return_greeting(tx,data):
        #print(data['user_id'])
        
        
        result = tx.run("CREATE (u:user{IdMaster: $user_id})  "
                        "CREATE(de:Device{IdMaster: $os}) "
                        "CREATE(BR:Brand{IdMaster: $brand})"
                          ,user_id = data['user_id'] , os = data['device']['os'] , brand = data['device']['brand']
                         )
        return result.single()
    @staticmethod
    def create_relationship(tx,data):

        result = tx.run("CREATE(ope:opera{os:$os}) "
                        "CREATE rel = (u)-[used:USED{TimeCreated:$cur_time,TimeEvent: $usages_date,UsageMinutes: $minutes_used}]->(ap)-[on:ON{TimeCreated: $cur_time}]->(de)-[ha:HAVING{TimeCreated: $cur_time}]->(ope) RETURN rel"
                        , os = data['device']['os'] , cur_time = datetime.today() , usages_date = data['usages_date']
                        
                        )

        
        


   


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "a")
    h = worker()
    greeter.print_greeting("hello, world",h)
    greeter.close()
