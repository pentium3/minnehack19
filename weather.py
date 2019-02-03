import os
import pycurl
from io import BytesIO
import json

url="http://api.apixu.com/v1/current.json?key=0dfa9b06e0f549ab86055800190302&q=55455" 
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()
jj = json.loads(body)
humidity = jj['current']['humidity']
temp = jj['current']['temp_c']
precip = jj['current']['precip_mm']


