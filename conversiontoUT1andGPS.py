import numpy as np
import requests
#numpy and requests are the only libraries needed 

def timeconversions():

    r=requests.get("https://maia.usno.navy.mil/ser7/finals2000A.daily", allow_redirects=True)
    open('conversiontableUT1.dat', 'wb').write(r.content) #the table is downloaded from the web and loaded on a file
    file=open('conversiontableUT1.dat','r')
    total_lines_UT1 = sum(1 for line in file) #how many lines are in the file
    file.close()
    MJDUT1=np.zeros(shape=total_lines_UT1) #to save the date
    bullUT1=np.zeros(shape=total_lines_UT1) #to save the bull
    counter=0
    file=open('conversiontableUT1.dat','r')
    while counter < total_lines_UT1: #the loop allows to read all lines of the file 
        line=file.readline() #read the line
        if line: #check the line is not empty
            MJDUT1[counter]= float(line[7:15]) #the modified julian date is saved
            bullUT1[counter]=float(line[58:68]) #the bull of the error for the corresponding date is saved
        else:
            counter=total_lines_UT1 #if line is empty, the loop is exited
        counter=counter+1
    file.close()
    r=requests.get("https://maia.usno.navy.mil/ser7/tai-utc.dat", allow_redirects=True)
    open('conversiontableGPS.dat', 'wb').write(r.content) #the table is downloaded from the web and loaded on a file
    file=open('conversiontableGPS.dat','r')
    total_lines_GPS = sum(1 for line in file) #how many lines are in the file
    file.close()
    yearGPS=np.zeros(shape=total_lines_GPS) #to save the year
    bullGPS=np.zeros(shape=total_lines_GPS) #to save the bull
    counter=0
    file=open('conversiontableGPS.dat','r')
    while counter < total_lines_GPS: #the loop allows to read all lines of the file 
        line=file.readline() #read the line
        if line: #check the line is not empty
            yearGPS[counter]=float(line[1:5]) #the year is saved
            bullGPS[counter]=float(line[38:48]) #the bull of the error for the corresponding year is saved
        else:
            counter=total_lines_GPS #if line is empty, the loop is exited
        counter=counter+1
    file.close()
    return MJDUT1, bullUT1, yearGPS, bullGPS

