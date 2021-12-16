import os
import sys
import time
from datetime import date
from datetime import datetime
import calendar
import pytz	
from timeit import default_timer as timer
t = timer()
ist = pytz.timezone('Asia/Kolkata')
def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))   
    dayNumber = calendar.weekday(year, month, day)
    days =["Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])

while True:
    now = datetime.now(ist)
    d1 = str(now.strftime("%d %m %Y"))
    d2 = now.strftime("%B %d, %Y")
   
    print('         Date =',d2,end = "    ||    ")
    print('Day =',findDay(d1))
    

    time.sleep(5)


    print(" ")
    current_time = now.strftime("%I:%M:%S %p")
    print("                        Time =", current_time)

    time.sleep(5)
    t1 = timer()
    print(" ")
    h, rem = divmod((t1 - t), 3600)
    m, sec = divmod(rem, 60)
    
    if(h<=23):
    	#print("Bot up time = "+h "Hrs : " Min:%s Sec",{int(h),int(m),int(sec)})
    	print("         Bot up time = {} Hrs : {} Mins : {}Secs".format(int(h),int(m), int(sec)))
    if(h>23):
    	h1 = int(h/24)
    	
    	x = h % 24
    	if(h1 == 1):
    	   print("         Bot up time = {} Day".format(h1),end = " -> ")
    	if(h1 > 1):
    	   print("         Bot up time = {} Days".format(h1),end = " -> ")    	   
    	#print("Bot up time = %d:%d:%d",int(x),int(m),int(sec))
    	print("{} Hrs : {} Mins : {} Secs".format(int(x),int(m), int(sec)))
    
    
    
   # print("the  total data consumed is :/n") 
    os.system("sh vnstat.sh")
    time.sleep(8)
    #os.system("sh clear.sh")
    print(' ')
    
    os.system("sh memory.sh")
    time.sleep(8)
    #os.system("sh clear.s")
    print(' ')
    os.system("sh storage.sh")
    time.sleep(8)
   # os.system("sh clear.sh")
    print(' ')
    os.system("sh cpu.sh")
    time.sleep(8)
   # os.system("sh clear.sh")
    time.sleep(1)
    
    print(' ')
    print(" TOTAL NO OF PROCESSES RUNNING = ")
    time.sleep(1)

    os.system("sh processes.sh")
    time.sleep(8)
    print(' ')
    #os.system("sh clear.sh")
    
    time.sleep(2)

