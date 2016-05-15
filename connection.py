import httplib

conn = httplib.HTTPConnection("localhost:8003")
conn.request("GET", "/llb.L5K")
r1 = conn.getresponse()
print r1.status

data =r1.read() 

print data 

file = open("newfile.txt", "w")

file.write(data)

file.close()

def main():
      file = open("newfile.txt","r")
      lines = file.readlines()
      file.close()
 
      for line in lines:
       if( (line.find("SerialNumber")!=-1) or (line.find("ProcessorType")!=-1) or (line.find("NodeAddress")!=-1)):
          line = line.strip()
          print ( line )

main()
