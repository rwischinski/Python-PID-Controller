#!/usr/bin/python


from PID import PID



# PID Controller Parameters
DIRECT = 0
REVERSE = 1

AUTOMATIC = 1
MANUAL = 0
# PID controller's output limits
OUTMIN = 0.0
OUTMAX = 250.0
# Default tuning constances
Kp = 1.0
Ki = 0.02
Kd = 0.1

fTemp = 70.0 # Input (e.g. from temperature sensor)

# Temperature Controller: PID(setpoint, Kp, Ki, Kd, Mode)
pid = PID(70.0,100.0,0.15,0.0,DIRECT)
pid.SetOutputLimits(OUTMIN, OUTMAX)
pid.SetSampleTime(1000)
pid.SetMode(AUTOMATIC)
pid.SetTunings(Kp, Ki, Kd) # Change tuning parameters

while powerON == 1:
    # Temperature Control
    pid.myInput = fTemp
    pid.mySetpoint = 65.7

    if pid.Compute() == True:
        Output = pid.myOutput

