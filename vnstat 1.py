import os
import sys
import time

while True:
   # print("the  total data consumed is :/n") 
    os.system("sh vnstat.sh")
    time.sleep(8)
    os.system("sh clear.sh")
    
    os.system("sh memory.sh")
    time.sleep(8)
    os.system("sh clear.sh")
    
    os.system("sh storage.sh")
    time.sleep(8)
    os.system("sh clear.sh")
    
    os.system("sh cpu.sh")
    time.sleep(8)
    os.system("sh clear.sh")
    time.sleep(0)
    y = int( os.system("sh processes.sh") )
    os.system("sh clear.sh")
    print(" TOTAL NO OF PROCESSES RUNNING = ")
    time.sleep(1)
    os.system("sh processes.sh")
    time.sleep(8)
    os.system("sh clear.sh")
    
    time.sleep(2)

