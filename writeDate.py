from crontab import CronTab
import datetime

i = 1
while i < 11:
    with open('crontest.txt','a+') as file:
        file.write('\n'+str(datetime.datetime.now()))
    i += 1    

with open('crontest.txt','r') as file:
    for line in file:
        print(line)