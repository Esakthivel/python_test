import pyvisa
import time

def open(visa_add):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(visa_add)
    return inst

def write(inst,cmd):
    inst.write(cmd)

def read(inst):
    response = inst.read()
    return response

def close(inst):
    inst.close()

Device= pyvisa.ResourceManager()

Res = Device.list_resources()

for i in Res:
    if 'ASRL6::INSTR' in i:
       psu_add = i


class DMM:

    def Set_volt(V,S,C):
        psu = open(psu_add)
        write(psu,'INSTrument:SELect OUT'+C)
        write(psu,'SOURce:VOLTage:LEVel:IMMediate:AMPLitude '+ V )
        write(psu,'SOURce:CURRent:LEVel:IMMediate:AMPLitude 0.5')
        write(psu,'OUTPut:STATe '+ S)
        close(psu)

#time.sleep(1)


'''
psu_res = []

write(psu,'MEAS:VOLT?')
psu_res.append(float(read(psu)))

write(psu,'MEAS:CURR?')
psu_res.append(float(read(psu)))

print (psu_res)

'''
