# https://open-meteo.com/
# https://api.open-meteo.com/v1/forecast?latitude=-38.16&longitude=145.15&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,snow_depth,windspeed_10m,uv_index,uv_index_clear_sky,is_day&forecast_days=1&timezone=Australia%2FSydney
import requests
import json
import ics


preferences = []

#http_proxy  = "http://190.61.88.147:8080"
#proxyDict = {
#  "http": http_proxy,
#  "https": http_proxy
#}
#a = requests.get('https://example.com', proxies=proxyDict, verify=False)
location = ['-38.16','145.15']
#a = requests.get('https://example.com', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36'})


weather = json.loads(requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,snow_depth,windspeed_10m,uv_index,uv_index_clear_sky,is_day&forecast_days=1&timezone=Australia%2FSydney').text)

high = max(weather["hourly"]["temperature_2m"])
low =  min(weather["hourly"]["temperature_2m"])

print(f'Today high of {high}. and low of {low}')


compass = requests.get("http://bentleighsc-vic.compass.education/download/sharedCalendar.aspx?uid=9160&key=83de6e6e-54e3-47fd-8719-e00c01f19628&c.ics").text

c = ics.Calendar(compass)
#for i in c.events:
#    print(f"you have class {i.name} in {i.location} with {i.description} at {i.begin}")


#import imaplib
#import email
#from email.header import decode_header
#import webbrowser
#import os

# account credentials
#username = "hgol3@schools.vic.edu.au"
#password = "0987Po@!"
# use your email provider's IMAP server, you can look for your provider's IMAP server on Google
# or check this page: https://www.systoolsgroup.com/imap/
# for office 365, it's this:
#imap_server = "imap-mail.outlook.com"

#def clean(text):
#    # clean text for creating a folder
#    return "".join(c if c.isalnum() else "_" for c in text)
webbrowser.open(url, new=0, autoraise=True)
