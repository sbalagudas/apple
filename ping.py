#!/usr/bin/python

import os
import time
import sys
import threading as td

IP_HEAD = "192.168.2."

def countDown(seconds):
    for i in range(seconds):
        sys.stdout.write("#"+"\b") 
        sys.stdout.flush()
        time.sleep(0.5)

def killProcess():
    print "exiting the process"
    exit()
    print "process exited..."

class MyThread(td.Thread):
    def __init__(self,ip):
        super(MyThread,self).__init__()
        #self.arg = arg
        self.ip = ip

    def ipTest(ip):
        print "ping "+ip+"started..."
        os.system("ping "+ip)


for i in range(1,5):
    #ipTest = td.Thread(target=ipTest,args=(IP_HEAD+"129"))
    kp = td.Thread(target=killProcess,args=())

    ipTest = MyThread(ip=4)

    ipTest.start()

    #ipTest.join(5)
    #kp.start()
    #p1 = os.popen("ping 1.18.60.66").readlines()
    #p = os.popen("ls -l /home/signorina/share/ | grep ^d").readlines()


   
