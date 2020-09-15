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







    # # checking if file already exist
    # if not os.path.exists('backup/'+zip_file_name):
    #     # changing file name without spaces
    #     os.rename(original_name, file_name)
    #     # creating zip file using system command
    #     os.system("zip "+zip_file_name+" "+file_name)
    #     #moving zip file in backup directory using system command
    #     os.system("mv "+zip_file_name+" backup")
    #     # changing filename to its original name
    #     os.rename(file_name, original_name)

    time.sleep(1)