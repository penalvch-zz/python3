import datetime
import os.path
import requests
import sys
import time
# arg[1]=url
# arg[2]=user agent
# arg[3]=filepath
# arg[4]=filename
url=sys.argv[1]
ua=sys.argv[2]
fp=sys.argv[3]
fn=sys.argv[4]
if not os.path.exists(fp):
    os.mkdir(fp)
file_path = os.path.join(fp, fn)
try:
    req = requests.get(url,headers = {'user-agent': ua},stream=True)
except requests.exceptions.RequestException as e:
    currenttime = datetime.datetime.now().strftime("%Y%m%d%H%M")
    errorfilename=currenttime+"pythonfiledownloaderror.txt"
    errorfile_path = os.path.join("c:\\scripts\\logs\\", errorfilename)
    file = open(errorfile_path,'w')
    file.write(str(e))
    file.close()
    print("1")
    quit()
file = open(file_path,'wb')
# chunk_size=32768 20mbps,16384 10mbps
for data in req.iter_content(chunk_size=3072):
    file.write(data)
    time.sleep(0.001)
file.close()