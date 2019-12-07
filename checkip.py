#!/usr/bin/env python

# Siguiendo a: http://www.diegor.it/2014/06/19/howto-schedule-repeating-events-with-python/

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sched  
import datetime, time



# -------------------------------------

# quita los mensajes de warning porque servimos en un https sin certificados (por ahora)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# -------------------------------------

class PeriodicScheduler(object):                                                  
    def __init__(self):                                                           
        self.scheduler = sched.scheduler(time.time, time.sleep)                   
                                                                            
    def setup(self, interval, action, actionargs=()):                             
        action(*actionargs)                                                       
        self.scheduler.enter(interval, 1, self.setup,                             
                        (interval, action, actionargs))                           
                                                                        
    def run(self):                                                                
        self.scheduler.run()


def checkurl(url):
    try:
        resp = requests.get(url, verify=False)
        status = 'up'
    except:
        status = 'down'
    return status


# -------------------------------------

# url = 'https://185.105.39.34'

#f = open("checkIp.logs", "a")

# This is the event to execute every time  
def periodic_event():  
    url = 'https://'+requests.get('https://api.ipify.org').text
    status = checkurl(url)
    # print(datetime.datetime.now(), " --> ", url, "--> status: ", status)
    f = open("checkIp.logs", "a")
    f.write("%s --> %s --> status: %s\n" % (datetime.datetime.now(), url, status))
    f.close()


INTERVAL = 10 * 60 # cada 10 minutos (va en segundos)
periodic_scheduler = PeriodicScheduler()  
periodic_scheduler.setup(INTERVAL, periodic_event) # it executes the event just once  
periodic_scheduler.run() # it starts the scheduler  