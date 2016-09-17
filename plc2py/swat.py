#  This is the Main function
import sys,os
sys.path.insert(0,os.getcwd())
from io_plc.IO_PLC import DI_WIFI
from SCADA import H
from IO import *
from plc import plc1,plc2,plc3,plc4,plc5,plc6
from plant_ode.plant_ode import plant 

maxstep = 200*60*30#*60#*2 # time is counted in 0.005 seconds, 200*x*y, x unit seconds, y unit minutes
# Initiating Plant
Plant = plant(maxstep) 
# Defining I/O
IO_DI_WIFI = DI_WIFI()
IO_P1 = P1()
IO_P2 = P2()
IO_P3 = P3()
IO_P4 = P4()
IO_P5 = P5()
IO_P6 = P6()
print "Initializing SCADA HMI"
HMI = H()
print "Initializing PLCs\n"
PLC1 = plc1.plc1(HMI)
PLC2 = plc2.plc2(HMI)
PLC3 = plc3.plc3(HMI)
PLC4 = plc4.plc4(HMI)
PLC5 = plc5.plc5(HMI)
PLC6 = plc6.plc6(HMI)
print "Now starting Simulation"
# Main Loop Body
for time in range(maxstep):	
#Second, Minute and Hour pulse
	Sec_P = not bool(time%(200))
	Min_P = not bool(time%(200*60))
	Hrs_P = not bool(time%(200*60*60))
#solving out plant odes in 5 ms
	Plant.Actuator(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6)
	Plant.Plant(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6,time)
#PLC working
	PLC1.Pre_Main_Raw_Water(IO_DI_WIFI,IO_P1,HMI,Sec_P,Min_P,Hrs_P)
	PLC2.Pre_Main_UF_Feed_Dosing(IO_DI_WIFI,IO_P2,HMI,Sec_P,Min_P,Hrs_P)	
	PLC3.Pre_Main_UF_Feed(IO_DI_WIFI,IO_P3,HMI,Sec_P,Min_P,Hrs_P)
	PLC4.Pre_Main_RO_Feed_Dosing(IO_DI_WIFI,IO_P4,HMI,Sec_P,Min_P,Hrs_P)
	PLC5.Pre_Main_High_Pressure_RO(IO_DI_WIFI,IO_P5,HMI,Sec_P,Min_P,Hrs_P)
	PLC6.Pre_Main_Product(IO_DI_WIFI,IO_P6,HMI,Sec_P,Min_P,Hrs_P)
	print '{0}\r'.format(Plant.result[time][2:]),
print IO_P3.P301.DI_Run or IO_P3.P302.DI_Run and IO_P3.MV301.DI_ZSC and IO_P3.MV302.DI_ZSO and IO_P3.MV303.DI_ZSC and IO_P3.MV304.DI_ZSC and IO_P6.P602.DI_Run 
print HMI.Cy_P3.UF_FILTRATION_MIN

