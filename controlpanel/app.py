from yoctopuce.yocto_voltage import *
from yoctopuce.yocto_api import *
from yoctopuce.yocto_current import *

errmsg = YRefParam()

if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

sensor = YVoltage.FirstVoltage()
m = sensor.get_module()
target = m.get_serialNumber()
voltageSensor = YVoltage.FindVoltage(target + '.voltage1')
print(voltageSensor.get_currentValue())

sensor = YCurrent.FirstCurrent()
m = sensor.get_module()
target = m.get_serialNumber()
currentSensor = YCurrent.FindCurrent(m.get_serialNumber() + '.current1')
print(currentSensor.get_currentValue())
