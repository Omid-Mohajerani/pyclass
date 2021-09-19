import mysql.connector
import datetime
import requests
import json
from requests.auth import HTTPBasicAuth

callback_acceptable_seconds = 7200

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 6)

filename = f'PCMC_CALLBACKREPORT-{today}.csv'


api_base_url = 'https://10.33.4.88/stats/rest/index.php?entity=reports'
api_usename = 'admin'
api_password = 'myrestpass'
report = '/unanswered_calls_detail'
startdate = f"{yesterday}"
enddate = f"{yesterday}"
fullurl = api_base_url+report+'&start='+startdate+'&end='+enddate
response = requests.get(fullurl,auth=HTTPBasicAuth(api_usename, api_password),verify=False)
response = response.json()



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="omidreza",
  database="callmeback"
)

mycursor = mydb.cursor()

sql_query = f"SELECT archives.id,archives.created_at,archives.clid,users.fname,users.lname from archives LEFT JOIN users ON archives.user_id = users.id WHERE archives.created_at LIKE '{yesterday}%'"
mycursor.execute(sql_query)

myresult = mycursor.fetchall()

unanswered_calls = response['rows']
count = 0
with open(filename, 'w') as file_object:
    file_object.write("QC,CallDate,CallTime,CallBackTime,Time Diff,Customer Number,Agent Name\n")

for unanswered_call in unanswered_calls:
    if unanswered_call['queueName'] == 'General' and int(unanswered_call['waitTime']) > 30 and len(unanswered_call['callerid']) > 7 :
        for calls in myresult:
            if unanswered_call['callerid'] == calls[2]:
                calldate = unanswered_call['datetime'][:10]
                calltime = unanswered_call['datetime'][-8:]
                callbacktime = str(calls[1])
                callbacktime = callbacktime[-8:]
                FMT = '%H:%M:%S'
                tdelta = datetime.datetime.strptime(callbacktime, FMT) - datetime.datetime.strptime(calltime, FMT)
                tdelatseconds = tdelta.total_seconds()
                if tdelatseconds < callback_acceptable_seconds:
                    callbackQC = "PASS"
                else:
                    callbackQC = "FAIL"
                print(f"{callbackQC},{calldate},{calltime},{callbacktime},{tdelta},{calls[2]},{calls[3]} {calls[4]}")
                with open(filename, 'a') as file_object:
                    file_object.write(f"{callbackQC},{calldate},{calltime},{callbacktime},{tdelta},{calls[2]},{calls[3]} {calls[4]}\n")



        count+=1


#
