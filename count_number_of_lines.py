# Omid Mohajearni
# Count number of lines in all files in directory and saves in output.csv
import os
os.chdir('/tmp/sample')
for dirpath,dirnames,filenames in os.walk('.'):
    for file in filenames:
        with open(file,encoding='cp1252') as f:
            lines = f.readlines()
            print( "%s  %d " %(file,len(lines)))
        with open('/tmp/output.csv','a') as f2:
                f2.write("%s , %d \n"%(file,len(lines)))
