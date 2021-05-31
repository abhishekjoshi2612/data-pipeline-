from neo4j import GraphDatabase
from datetime import date, timedelta,datetime
import json
def worker():
         f = open('abhishek.2021-05-31.json') 
         data = json.load(f)
         print(data['usages'][1])
         return data
class HelloWorldExample:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
       

    def print_greeting(self, message,abc):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message,abc)
            print(greeting)
    
    @staticmethod
    def _create_and_return_greeting(tx, message,data):
        #print(abc)
        mapper = {'slack' : 0,'gmail' : 1,'jira' : 2,'google drive': 3,'chrome' : 4,'spotify' : 5}
        no_of_app = mapper[]
        result = tx.run("CREATE (u:user{IdMaster: $user_id})  "
                        "CREATE (ap:App{IdMaster: $app_name,AppCategory: $app_category})"
                        "CREATE(de:Device{IdMaster: $os})"
                        "CREATE(BR:Brand{IdMaster: $brand})"
                        "CREATE(ope:opera{os:$os}) "
                        "CREATE rel = (u)-[used:USED{TimeCreated:$cur_time,TimeEvent: $usage_date,UsageMinutes: $minutes_used}]->(ap)-[on:ON{TimeCreated: $cur_time}]->(de)-[ha:HAVING{TimeCreated: $cur_time}]->(ope) RETURN rel",
                         user_id = data['user_id'],app_name = data['usages'][0]['app_name'],os = data['device']['os'],brand = data['device']['brand'],minutes_used = data['usages']['minutes_used'],
                         cur_time = datetime.now(),usage_date = data['usages_date']
                         )
        return result.single()


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "a")
    h = worker()
    greeter.print_greeting("hello, world",h)
    greeter.close()
