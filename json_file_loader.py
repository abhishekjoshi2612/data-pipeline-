try:




    from datetime import date, timedelta,datetime
    import os
    

    print("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))
def file_maker(name,dates):
    name_of_file = name + "." +str(dates) + ".json"
    name_of_file = open(name_of_file,"w")
    

    pass
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
    
def vinit_today():
    file_maker("vinit",dates)
    
def guilermo_today():
    file_maker("guilermo",dates)
    
def christian_today():
    file_maker("christian",dates)
    
def eily_today():
    file_maker("eily",dates)
    
def abhishek_today():
    file_maker("abhishek",dates)
    

def create_files():
    delta = timedelta(days=1)

    end_date = date.today()
    start_date = end_date - delta*30
    for dates in range(start_date,end_date+delta):
        vinit_30_days(dates)
        guilermo_30_days(dates)
        christian_30_days(dates)
        eily_30_days(dates)
        abhishek_30_days(dates)
def create_today_files():
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
    

    


first_job()



    


