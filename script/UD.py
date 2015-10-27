import re
import xlwt

fob=open('/Users/abhinoc/Desktop/INFO.txt','r')

lines = fob.readlines()
fob.close()

INFO = []
 
for line in lines:
    #words = line.split("-")
    words =  line.strip()
    SLOT = re.findall(r'NAME:\s.*?,', words)
    DESCR = re.findall(r'DESCR:\s\".*?"', words)
    PID = re.findall(r'PID:\s.*?\s', words) 
    SERIALNO = re.findall(r'SN:\s\w+.*', words)    
    
    
    SLEN=len(SLOT)
    DLEN=len(DESCR)
    PLEN=len(PID)
    SELEN=len(SERIALNO)
    
    
    
    if SLEN != 0:
        INFO.extend([SLOT])
    if DLEN != 0:
        INFO.extend([DESCR])
    if SELEN != 0:
        INFO.extend([SERIALNO])
    if PLEN !=0:
        INFO.extend([PID])
        
    print INFO


workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Abhi-Sheet")
#sheet.write(0, 0, 'Name')
#sheet.write(0, 1, 'Description')
#sheet.write(0, 2, 'Serial No')
Data = []
start = 0
for index in range(len(INFO)):     
    Data.extend([INFO[index]])
    start += 1
    if start > 3:
        start = 0
        print Data[0][0], Data[1][0], Data[2][0], Data[3][0]
        Data = []
nstart = 0 
id = 0       
for i,n in enumerate(INFO):
    sheet.write(id, nstart, n)
    id +=1
    if id > 3:
        nstart += 1
        id = 0
        
nstart = 0 
id = 0          
for i,n in enumerate(INFO):
    print id
    print nstart
    print "____"
    
    nstart += 1
    if nstart > 3:
         print "Condition MET"
         nstart = 0 
         id = 0
         
         
         
###

nstart = 0 
id = 0       
for i,n in enumerate(INFO):
    sheet.write(id, nstart, n)
    nstart +=1
    if nstart > 3:
        nstart = 0
        id += 1
        


