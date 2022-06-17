import os

import requests

site = ["http://api.open-notify.org/astros.json", "https://mercedes-benz.com"]
times = os.environ ['times']

TOTAL= 0
for i in range(len(site)):
    if int(TOTAL) < int(times):
        p = requests.get(site[i])
        total = p.elapsed #time taken to hit a website
        
        print ('The site is:' , site[i])
        print ("The time is: ", total)
        print ('The total of number of-hits is:', times)
     