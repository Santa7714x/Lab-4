import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led(delay):
    # Led Blink
    led.init()
    switch.init()
    if switch.read_slide_switch() ==0:
        while switch.read_slide_switch()==0:
            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)
            time.sleep(0.1)
            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)
            time.sleep(0.1)


    if switch.read_slide_switch()==1:
        while switch.read_slide_switch()==1:
            led.set_output(0, 1)
            time.sleep(delay)
            led.set_output(0, 0)
            time.sleep(delay)
            led.set_output(0, 1)
            time.sleep(delay)
            led.set_output(0, 0)
            time.sleep(delay)

    if switch.read_slide_switch() ==0:
        for i in range (10):
            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)
            time.sleep(0.1)
            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)

def main():

    led.init()

    switch.init()

    print(switch.read_slide_switch())

    sleep(1.0)

    blink_led(0.25)


if __name__ == "__main__":
    main()