import csv 
import sys
 
f = open(sys.argv[1], "rb")
reader = csv.reader(f)
for row in reader:
  print "\""+row[0] + "\"=\"" + row[1]+"\""
f.close()