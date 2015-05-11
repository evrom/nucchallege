import json
from bottle import request, abort
from controlpanel.power import currentSensor, voltageSensor
from controlpanel.percent import percent_from_voltage
from controlpanel.timeremaining import time_remaining
from controlpanel.cpu import cpu_frequency, cpu_usage
from controlpanel.maxclockspeed import cpu_high, cpu_low


def battery():
    voltage = voltageSensor.get_currentValue()
    current = currentSensor.get_currentValue()
    percent = percent_from_voltage(voltage)
    remaining = time_remaining(100, current/1000)
    return json.dumps(dict(
        current=current,
        voltage=voltage,
        percent=percent,
        remaining=remaining
    ))


def cpu():
    return json.dumps(dict(
        frequencies=cpu_frequency(),
        usages=cpu_usage()
    ))


def clockspeed():
    body = request.json
    if body['speed'] == 'high':
        cpu_high()
        return dict(status='high')
    if body['speed'] == 'low':
        cpu_low()
        return dict(status='low')
    else:
        return abort(500)
