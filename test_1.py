from PSU.ConPSU import DMM
from Dmm.ConDMM import dmm
import pytest

def test_1():
    v = '15'
    DMM.Set_volt(v,'ON','2')
    #dmm.Mess_DMM()
    b = dmm.Mess_DMM()
    print ('voltage Measured:' + b + 'V')
    assert b == v

def test_2():
    v = '12'
    DMM.Set_volt(v,'ON','2')
    #dmm.Mess_DMM()
    b = dmm.Mess_DMM()
    print ('voltage Measured:' + b + 'V')
    assert b == v

def test_3():
    v = '10'
    DMM.Set_volt(v,'ON','2')
    #dmm.Mess_DMM()
    b = dmm.Mess_DMM()
    print ('voltage Measured:' + b + 'V')
    assert b == v

def test_4():
    v = '9'
    DMM.Set_volt(v,'ON','2')
    #dmm.Mess_DMM()
    b = dmm.Mess_DMM()
    print ('voltage Measured:' + b + 'V')
    assert b == v

def test_5():
    v = '8'
    DMM.Set_volt(v,'ON','2')
    #dmm.Mess_DMM()
    b = dmm.Mess_DMM()
    print ('voltage Measured:' + b + 'V')
    assert b == v

def test_6():
    v = '6'
    DMM.Set_volt(v,'ON','2')
    #dmm.Mess_DMM()
    b = dmm.Mess_DMM()
    print ('voltage Measured:' + b + 'V')
    assert b == v

def test_7():
    v = '4'
    DMM.Set_volt(v,'ON','2')
    #dmm.Mess_DMM()
    b = dmm.Mess_DMM()
    print ('voltage Measured:' + b + 'V')
    assert b == v
