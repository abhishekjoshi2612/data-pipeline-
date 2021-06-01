from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import date, timedelta,datetime
import os
import json
import 
#importing a job to run from another file
from neo_4j import runit

#function to create file in current directory takes name of file and  date supplied
def file_maker(name,dates):
    final_name = name + "@tribes.ai"
    #name of each file = name of person + . + current date + .json
    name_of_file = name + "." +str(dates) + ".json"
    cur_sum = 0
    #assigning values to minute used variable for apps
    google_driver = random.randint(0,180)
    cur_sum = google_driver
    slacker = random.randint(0,min(480 - cur_sum,180))
    cur_sum = cur_sum + slacker
    gmailer = random.randint(0, min(480 - cur_sum,180))
    cur_sum = cur_sum + gmailer
    jirar =  random.randint(0, min(480 - cur_sum,180))
    cur_sum = cur_sum + jirar
    chromer = random.randint(0, min(480 - cur_sum,180))
    cur_sum = cur_sum + chromer
    spotifyer = random.randint(0,min(480 - cur_sum,180))

    
    my_json_data =  {"user_id" : final_name,
                         "usages_date" : str(dates),
                         "device" : {
                             "os" : "ios",
                             "brand" : "apple"

                                     },
                         "usages":[

                                {
                                    "app_name" : "slack",
                                    "minutes_used": slacker,
                                    "app_category" : "communication"
                                },
                                {
                                    "app_name" : "gmail",
                                    "minutes_used": gmailer,
                                    "app_category" : "communication"
                                },
                                {
                                    "app_name" : "jira",
                                    "minutes_used": jirar,
                                    "app_category" : "task_management"
                                },
                                {
                                    "app_name" : "google drive",
                                    "minutes_used": google_driver,
                                    "app_category" : "file_management"
                                },
                                {
                                    "app_name" : "chrome",
                                    "minutes_used": chromer,
                                    "app_category" : "web_browser"
                                },
                                {
                                    "app_name" : "spotify",
                                    "minutes_used": spotifyer,
                                    "app_category" : "entertainment_music"
                                }
                               ]

                    }

    json_object = json.dumps(my_json_data,indent = 4)
    print(os.getcwd())
    with open(str(name_of_file),"w") as out_file:
        out_file.write(json_object)

  
    
    


    
    

    
#functions to call when 30 days files not made
def vinit_30_days(dates):
    file_maker("vinit",dates)
def guilermo_30_days(dates):
    file_maker("guilermo",dates)
def christian_30_days(dates):
    file_maker("christian",dates)
    
def eily_30_days(dates):
    file_maker("eily",dates)
    
def abhishek_30_days(dates):
    file_maker("abhishek",dates)
#functions to call for today files
def vinit_today(dates):
    file_maker("vinit",dates)
    
def guilermo_today(dates):
    file_maker("guilermo",dates)
    
def christian_today(dates):
    file_maker("christian",dates)
    
def eily_today(dates):
    file_maker("eily",dates)
    
def abhishek_today(dates):
    file_maker("abhishek",dates)
    
#this function get called after checker finds that last 30 days file not made
def create_files():
    delta = timedelta(days=1)

    end_date = date.today()
    start_date = end_date - delta*30
    #using a while loop to create last 30 day files
    while start_date<end_date:
        vinit_30_days(start_date)
        guilermo_30_days(start_date)
        christian_30_days(start_date)
        eily_30_days(start_date)
        abhishek_30_days(start_date)
        start_date += delta
#this function get called for creating file containing today date        
def create_today_files():
    dates = date.today()
    print("hello")
    vinit_today(dates)
    guilermo_today(dates)
    christian_today(dates)
    eily_today(dates)
    abhishek_today(dates)

def create_last_days():
    curr_path = os.getcwd()
    #last 30 day files stored in folder named stored_30_day_files
    path = os.path.join(curr_path,"stored_30_days_files")
    os.mkdir(path)
    os.chdir(path)
    #directory changed to /stored_30_days_files/
    create_files()
    #now for creating today files directory again changed so that it looks like => today_files stored_30_day_files(folder)
    os.chdir(curr_path)
   


#this function calls  create_files if 30 days file required    
def checker():
    if os.path.exists(('stored_30_days_files')) == False:
    
        create_last_days()
    
    

    


with DAG(
        dag_id="json_loader",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=20),
            "start_date": datetime(2021, 5, 31),
        },
        catchup=False) as f:
    # this job is for creating 30 day files if doesnt exists
    checker = PythonOperator(
        task_id="checker",
        python_callable=checker,
        provide_context=True,
        
    )
    #this job is for creating today files
    create_today_files = PythonOperator(
        task_id="create_today_files",
        python_callable=create_today_files,
        provide_context=True,
        
    )
    #this job is for loading data into neo4j database
    runit = PythonOperator(
        task_id = "runit",
        python_callable=runit,
        provide_context=True
    )


    

checker >> create_today_files >> runit
