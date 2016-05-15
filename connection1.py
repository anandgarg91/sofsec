from bs4 import BeautifulSoup
import requests
import httplib


url = 'http://localhost:8003'
ext = 'L5K'

def main1():
	conn = httplib.HTTPConnection("localhost:8003")
	conn.request("GET", "/"+file1[-1])
	r1 = conn.getresponse()
	print r1.status
	
	data =r1.read() 

	#print data 

	file = open("newfile.txt"+file1[-1], "w")
        
	file.write(data)

	file.close()

	def main():
	      file = open("newfile.txt"+file1[-1],"r")
	      lines = file.readlines()
	      file.close()
 
	      for line in lines:
	       if( (line.find("SerialNumber")!=-1) or (line.find("ProcessorType")!=-1) or (line.find("NodeAddress")!=-1)):
	          line = line.strip()
	          print ( line )

	main()


def listFD(url, ext=''):
    page = requests.get(url).text
    #print page
    soup = BeautifulSoup(page, 'html.parser')
    print "***************"
    #print soup
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for file1 in listFD(url, ext):
    file1 = file1.split('/')
    main1()
    print file1[-1]





