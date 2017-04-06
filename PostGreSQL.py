import subprocess
from subprocess import check_output
from subprocess import call
import csv
import time 
from datetime import datetime
import os



host = "10.10.1.200"
port = "5432"
exName = "pgbench-postgreSQL"
dbname = "ali"
scaligFactor = "50"
fillFactor = "100"
DB_size = scaligFactor+" x 16MB"
parconn = str(10) #parallel connections
threads = str(2)
transactions = str(100)


##Temp Parameters
par = 50 #transaction
par2 = 5 #threads
par3 = 10 #Clients


#Function
def print_factors(x):
   # This function takes a number and prints the factors
   listf = [] 
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           listf.append(i)
   return listf

csvfile = open("/vagrant/Data/pgbench/pgbench_%s.csv"% datetime.now(), 'w')

fieldnames = ['count','Date','ExpName', 'DB Size','Parallel Clients','Num_Threads','Num_Transactions/client','#TransActuallyProcessed','TPS/incConn','TPS/excConn','Avg Latency/AllStatments(ms)']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()



##./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=127.0.0.1" -p "redis.port=6379" -p "threadcount=10"
## mvn -pl com.yahoo.ycsb:redis-binding -am clean package
## recordcount=1000
## operationcount=1000


#os.chdir(["sudo","-u", "postgres"])
#print "===================Directory Changed to YCSB !!==========================================\n\n"
#call(["sudo", "-u", "postgres"])
print "================================Postgres Terminal=======================================\n\n"
print "================================Initializing Test=======================================\n\n"

#pgbench -i -h 10.10.1.200 -p 5432 ali -s 10 -F 20
#subprocess.call(["sudo", "-u", "postgres","pgbench", "-i","-h", host,"-p",port ,dbname,"-s",scaligFactor,"-F",fillFactor],stdout=subprocess.PIPE)
print "================================PGBENCH TEST Initialized=======================================\n\n\n"

print "================================Pgbench TEST will bench postgresql Server =======================================\n\n\n"

#pgbench -h 10.10.1.200 -p 5432 -c 10 -j 2 -t 10000 ali  

for num in range (0,101):
      print "================ New Run ================= \n\n"
      if num % 20 == 0 :
         par3 = par3 + 10
         parconn = str(par3)
         factors = print_factors(par3)
         for fac in range(0,len(factors)):
           if factors[fac] > par2:
              par2 = factors[fac]
              break
         threads = str(par2)
         
      transactions = str(par)
      test_out = check_output(["sudo", "-u", "postgres","pgbench","-h", host,"-p",port ,"-c",parconn,"-j",threads,"-t",transactions,"-r",dbname])
      #print test_out
      a = test_out.split('\n')
      
      for s in range(0, len(a)):
         if a[s] == 'statement latencies in milliseconds:':
            x = s + 1
      
      list = []
      for d in range(x, len(a)-1):
	 list.append(a[d])  

      listl = []
      lat = 0
      for g in range(0, len(list)):
         c = list[g].split("\t")
         listl.append(float(c[1]))
	 lat = lat + listl[g]
         # Latency = lat

      f = a[6].split(" ")
      f = f[len(f)-1]

      u = ""
      y = ""
      for h in range(0,len(f)):
         if f[h] != '/' and h < len(f)/2 :
           u = str(u) + f[h]
         if f[h] != '/' and h > len(f)/2 :
           y = str(y) + f[h] 

      ## float(u) = number of transactions actually processed 

      m1 = a[7].split(" ")
      m2 = a[8].split(" ")

      m1 = float(m1[2]) # TPS including connections establishing
      m2 = float(m2[2]) # TPS excluding connections establishing



      print num,"=====","c=",parconn,"=====","t=",transactions,"====","j=",threads,"====",float(u),"====", m1 , "====" , m2, "=====", lat
      writer.writerow({'count':num,'Date':time.strftime("%d/%m/%Y"),'ExpName':exName,'DB Size':DB_size,'Parallel Clients': parconn ,'Num_Threads':threads,'Num_Transactions/client':transactions,'#TransActuallyProcessed':float(u),'TPS/incConn':m1,'TPS/excConn':m2,'Avg Latency/AllStatments(ms)':float(lat)})

	 
      par = par + 50
      #par2 = par2 + 2
      time.sleep(2)

print "pgbench !! Benchmark is finished !!"
