
import urllib.request
from datetime import datetime
import json

# 百度服务器默认返回为美国时间， 需要加上八个小时时差才为北京时间，用来做时间校验会有八个小时误差
def get_web_server_time():
    url = "http://www.baidu.com"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')

    ts = response.getheader('date')  # 获取http头date部分
    print(ts)
    date_format = "%a, %d %b %Y %H:%M:%S %Z"
    parsed_datetime = datetime.strptime(ts, date_format)

    return parsed_datetime
