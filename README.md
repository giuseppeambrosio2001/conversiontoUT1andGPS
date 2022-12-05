# conversiontoUT1andGPS
This repository will allow you to convert from UTC to UT1 and GPS time scales.
#UT1
The table is downloaded from the internet, then all lines are read: the modified julian date and the corresponding bull (to be used for the conversion) are saved in arrays.
#GPS
The table is downloaded from the internet, then all lines are read: the year and the corresponding bull (to be used for the conversion) are saved in arrays.
#input & output
No input is needed for the routine, since it automatically downloads the conversion tables.
As for the output, data (modified julian date, bull for UT1, year, bull for GPS) will be stored in arrays. This data can later be used to implement the conversion, and they are returned by the function as outputs. All outputs are "float".
~~~
MJDUT1, bullUT1, yearGPS, bullGPS=timeconversions() #this is how the function should be used in a python script
~~~
