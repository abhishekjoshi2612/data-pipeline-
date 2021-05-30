try:

    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from airflow.utils.dates import days_ago
    from datetime import date, timedelta,datetime
    import os
    import json
    import random
    

print("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))

def file_maker(name,dates):
    final_name = name + "@tribes.ai"
    name_of_file = name + "." +str(dates) + ".json"
    cur_sum = 0
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
                         "usage_date" : str(dates),
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
    with open(str(name_of_file),"w") as out_file:
        out_file.write(json_object)

  
    
    


    
    

    

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
    

def create_files():
    delta = timedelta(days=1)

    end_date = date.today()
    start_date = end_date - delta*30
    while start_date<end_date:
        vinit_30_days(start_date)
        guilermo_30_days(start_date)
        christian_30_days(start_date)
        eily_30_days(start_date)
        abhishek_30_days(start_date)
        start_date += delta
def create_today_files(dates):
    vinit_today(dates)
    guilermo_today(dates)
    christian_today(dates)
    eily_today(dates)
    abhishek_today(dates)

def create_last_days():
    curr_path = os.getcwd()
    path = os.path.join(curr_path,"stored_30_days_files")
    os.mkdir(path)
    os.chdir(path)
    create_files()
    os.chdir(curr_path)
   



def checker():
    if os.path.exists(('stored_30_days_files')) == False:
        create_last_days()
    

    


with DAG(
        dag_id="checker",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=20),
            "start_date": days_ago(1),
        },
        catchup=False) as f:

    checker = PythonOperator(
        task_id="checker",
        python_callable=checker,
        
    )

    second_function_execute = PythonOperator(
        task_id="create_today_files",
        python_callable=create_today_files,
        
    )

checker >> create_today_files
