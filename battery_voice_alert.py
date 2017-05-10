#This python script provides solution for voice alerting during low laptop battery
#this script will be running in background and whenever our battery charge status is false and battery is below 40% and greater than 10%,It will alert with voice notification in every 15 minutes.once battery charge percentage will reach below 10%,It will alert with voice notification in every 2 mins.




#this package provide utility to check battery status
import psutil
#this package provide sleep facility
import time
#this package provide text to audio  conversion facility
from espeak import espeak 


#This method helps to get the status of battery and return battery status and charge percentage of battery
def btrystatus():
  battery1 = psutil.sensors_battery()
  battery = str(battery1)
  percent = battery.find('=')
  firstSeperator = battery.find(',')
  actualPercentage = battery[percent+1:firstSeperator]
  status = battery.rfind('=')
  actualStatus = battery[status+1:len(battery)-1]
  return (actualStatus,actualPercentage)


#This method helps to generate voice alert
def voicealert(msg):
  espeak.synth(msg)  
  return;

#loop for continuously checking battery status
while True:


  btrStatus,btrCharge = btrystatus()
  btrPercentage = float(btrCharge)

  #loop for voice alert according to condition
  while btrStatus == "False":

    #condition for voice alert between 10 to 40 percentage of battery 
    if btrPercentage >= 10 and btrPercentage < 40:
       voicealert("you Laptop Battery is below 40 percentage")
       time.sleep(720)

    #condition for voice alert below 10 percentage of battery
    elif btrPercentage < 10:
       voicealert("your battery is below 10 percentage.Please plugin your charger")
       time.sleep(120)
    else:
       pass

    #updating battery status value for next loop
    btrStatus,btrCharge = btrystatus()
    btrPercentage = float(btrCharge)
     



