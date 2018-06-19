"""
NI ELVIS III Pulse Width Modulation (PWM) Example
This example illustrates how to generate a PWM signal to an external
peripheral through the PWM channels. To create an PWM session, you need to
define two required parameters: bank and channel. To configure a PWM signal,
you need to define two required parameters: frequency and duty_cycle.

Output:
    Generate a PWM signal from DIO0 on bank B.
"""
import time
import NIELVISIIIAcademicIO
from NIELVISIIIEnum import Bank, DIOChannel

# specify bank and channel to generate the PWM signal
bank = Bank.B
channel = DIOChannel.DIO0

# open an PWM session, and set initial values for the parameters
with NIELVISIIIAcademicIO.PWM(bank, channel) as PWM:
    # specify the frequency settings for the PWM signal
    frequency = 160
    # specify the percentage of time the PWM signal remains high over one PWM
    # cycle
    duty_cycle = 0.7

    # output the PWM signal
    PWM.configure(frequency, duty_cycle)
    # the signal outputs 20 times
    for i in range(0, 20):
            time.sleep(0.01)
            print "outputting PWM signal.."