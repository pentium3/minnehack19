import math
import os
import sys
import pycurl
from io import BytesIO
import json


def classify(PLANT, IP):
    if(IP=="127.0.0.1"):
        return("Madison|2.333")
    url="http://api.apixu.com/v1/current.json?key=0dfa9b06e0f549ab86055800190302&q="+IP
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    jj = json.loads(body)
    loc = jj['location']['name']
    humidity = jj['current']['humidity']
    temp = jj['current']['temp_c']
    precip = jj['current']['precip_mm']
    t=80
    ft =(4.6411e-09*math.pow(t,5) + -1.8590e-06*math.pow(t,4) + 2.0746e-04 * math.pow(t,3) - 0.0043*math.pow(t,2) + 0.0302 * t + 2.9369)/4.046
    ans = round(max(0, ft - precip),3)
    ret = loc + '|' +str(ans)
    print(ret)
    return(ret)

