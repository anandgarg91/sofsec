# SCADA is the control interface, talking and giving instructions to all PLCs
from HMI.HMI import *

class H:
	def __init__(self):
		# Whole PLANT
		self.PLANT = HMI_plant()
		self.P1 = HMI_phase()
		self.P2 = HMI_phase()
		self.P3 = HMI_phase()
		self.P4 = HMI_phase()
		self.P5 = HMI_phase()
		self.P6 = HMI_phase()
		# P1
		self.LIT101 = HMI_LIT()
		self.MV101  = HMI_mv()
		self.FIT101 = HMI_FIT()
		self.P101   = HMI_pump()
		self.P102   = HMI_pump()
		self.P_RAW_WATER_DUTY = HMI_duty2()
		# P2
		self.MV201 = HMI_mv()
		self.LS201 = HMI_LS()
		self.LS202 = HMI_LS()
		self.LSL203 = HMI_LS()
		self.LSLL203 = HMI_LS()
		self.P201  = HMI_pump()
		self.P202  = HMI_pump()
		self.P203  = HMI_pump()
		self.P204  = HMI_pump()
		self.P205  = HMI_pump()
		self.P206  = HMI_pump()
		self.P207  = HMI_pump()
		self.P208  = HMI_pump()
		self.P_NACL_DUTY = HMI_duty2()
		self.P_HCL_DUTY  = HMI_duty2()
		self.P_NAOCL_FAC_DUTY = HMI_duty2()
		self.FIT201 = HMI_FIT()
		self.AIT201 = HMI_ait(950.0, 260.0, 250.0,50.0)
		self.AIT202 = HMI_ait(12.0, 7.05,6.95,3.0)
		self.AIT203 = HMI_ait(750.0,480.0,440.0,100.0)
		# self.P3
		self.Mid_P602_AutoInp = 0 # This a variable shared and mostly read by P6 PLC, it's not HMI variable(maybe from SCADA, people can't change)  --PF
		self.Cy_P3 = HMI_Ultralfiltration_Cycle()
		self.LIT301 = HMI_LIT()
		self.P301   = HMI_pump()
		self.P302   = HMI_pump()
		self.P_UF_FEED_DUTY = HMI_duty2()
		self.FIT301 = HMI_FIT()
		self.PSH301 = HMI_PSH()
		self.DPSH301 = HMI_DPSH()
		self.DPIT301 = HMI_DPIT()
		self.MV301 = HMI_mv()
		self.MV302 = HMI_mv()
		self.MV303 = HMI_mv()
		self.MV304 = HMI_mv()
		# self.P4
		self.LS401 = HMI_LS()
		self.LIT401 = HMI_LIT() 
		self.P401  = HMI_pump() 
		self.P402  = HMI_pump() 
		self.P403  = HMI_pump() 
		self.P404  = HMI_pump() 
		self.UV401 = HMI_uv()
		self.P_NAHSO3_ORP_DUTY = HMI_duty2()
		self.P_RO_FEED_DUTY   = HMI_duty2()
		self.AIT401 = HMI_ait(100.0, 80.0, 0.0, 0.0)
		self.AIT402 = HMI_ait(800.0, 300.0, 250.0, 200.0)
		self.FIT401 = HMI_FIT() 
		# self.P5
		self.Mid_P603_AutoInp = 0 # This a variable shared and mostly read by P6 PLC, it's not HMI variable(maybe from SCADA, people can't change),but in our current PLC coding, Phase 5 is not writing to this variable, it keeps 0  --PF

		self.Cy_P5  = HMI_ReverseOsmosis_Cycle()
		self.AIT501 = HMI_ait(0.0,0.0,0.0,0.0) 
		self.AIT502 = HMI_ait(300.0, 250.0, 0.0,0.0) 
		self.AIT503 = HMI_ait(500.0,260.0,250.0,0.0) 
		self.AIT504 = HMI_ait(15.0,12.0,0.0,0.0) 
		self.PIT501 = HMI_PIT()
		self.PIT502 = HMI_PIT() 
		self.PIT503 = HMI_PIT() 
		self.FIT501 = HMI_FIT() 
		self.FIT502 = HMI_FIT() 
		self.FIT503 = HMI_FIT() 
		self.FIT504 = HMI_FIT() 
		self.MV501 = HMI_mv()
		self.MV502 = HMI_mv()
		self.MV503 = HMI_mv()
		self.MV504 = HMI_mv()
		self.P_RO_HIGH_DUTY = HMI_duty2()
		self.P501 = HMI_VSD()
		self.P502 = HMI_VSD()
		# self.P6
		self.LSL601 = HMI_LSL() 
		self.LSL602 = HMI_LSL() 
		self.LSL603 = HMI_LSL() 
		self.LSH601 = HMI_LSH() 
		self.LSH602 = HMI_LSH() 
		self.LSH603 = HMI_LSH() 
		self.P601 = HMI_pump()
		self.P602 = HMI_pump()
		self.P603 = HMI_pump()
		self.FIT601 = HMI_FIT() 


