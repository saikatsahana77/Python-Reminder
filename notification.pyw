import xlrd
import time
import datetime
import os
from notifypy import Notify


jobs,timings = [],[]
flag = True

def update():
    global flag
    flag = False
    print(flag)

def remLeadZeros(st):
    if (st.startswith("0")):
        return st[1:]
    else:
        return st

exl_file = xlrd.open_workbook("Reminders.xlsx")

k = datetime.datetime.today().weekday()

xcl_sheet = exl_file.sheet_by_index(k)

for i in range (2,xcl_sheet.nrows):
    jobs.append(xcl_sheet.cell_value(i, 0))
    k = xcl_sheet.cell_value(i,1)
    k = int(k*24*3600)
    k = datetime.time(k//3600, (k%3600)//60, k%60)
    timings.append(k)

while (1):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    cur_timing = datetime.time(int(remLeadZeros(current_time[:2])),int(remLeadZeros(current_time[3:5])),int(remLeadZeros(current_time[6:])))
    for i in range(len(timings)):
        if (timings[i]==cur_timing):
            notification = Notify()
            notification.title = "Reminder!"
            notification.message = jobs[i]
            if os.name == 'nt':
                notification.icon = "icon.ico"
            notification.audio = "ting.wav"
            notification.send(block=False)
            time.sleep(1)
    if (flag == False):
        break

