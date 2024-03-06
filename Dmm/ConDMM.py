import pyvisa
import time



def open(visa_add):
    rm = pyvisa.ResourceManager()
    inst1 = rm.open_resource(visa_add)
    return inst1

def write(inst1,cmd):
    inst1.write(cmd)

def read(inst1):
    response = inst1.read()
    return response

def close(inst1):
    inst1.close()

Device= pyvisa.ResourceManager()

Res = Device.list_resources()

for i in Res:
    if 'MY53221663' in i:
        Dmm_add = i


class dmm:
    
    def Mess_DMM():
        dmm = open(Dmm_add)
        write(dmm,'MEAS:VOLT:DC? 15,0.001')
        time.sleep(1)
        a = str(float(read(dmm))).split(".")[0]
        close(dmm)
        return(a)



   