# parsering script

import glob
for filename in glob.glob('*.L5K'):

 def main():
      file = open(filename ,"r")
      lines = file.readlines()
      file.close()
 
      for line in lines:
        if( (line.find("SerialNumber := 16#00c1_9819")!=-1) or (line.find("ProcessorType")!=-1) or (line.find("NodeAddress")!=-1)):
          line = line.strip()
          print ( line )

 print (filename)
 main()
