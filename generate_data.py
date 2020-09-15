import os
import datetime
import time
import json



# directory to generate files
dir = "/home/derrick/data/"

# change working directory to file directory
os.chdir(dir)

while 1:

    # get current time
    today = datetime.datetime.today()
    today= str(today)
    current_date = today[0:10]
    current_time = today[11:19]
    current_hour = today[11:13]
    current_minute = today[14:16]
    current_sec = today[17:19]

    # defining a filename with time
    new_file_name = "genfile-" + current_date.replace("-", "") + "-" + current_hour + "-" + current_minute + "-" + current_sec + "." + "json"
    
    data = {"date": current_date, "time": current_time, "message": "Test Message"}

    print(data)

    with open(new_file_name, 'w') as outfile:
        json.dump(data, outfile)


    time.sleep(1)