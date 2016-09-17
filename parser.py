# parsering script

def main():
      file = open("llb.L5K","r")
      lines = file.readlines()
      file.close()
 
      for line in lines:
        if( (line.find("SerialNumber")!=-1) or (line.find("ProcessorType")!=-1) or (line.find("NodeAddress")!=-1)):
          line = line.strip()
          print ( line )

main()
