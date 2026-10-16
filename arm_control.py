from machine import PWM, Pin
import time
servo_1 = PWM(Pin(4), freq=50, duty_u16=0)
servo_2 = PWM(Pin(5), freq=50, duty_u16=0)

from machine import ADC

from encoder import Count
count1 = Count(32,39)
count2 = Count(25,33)

current_pos_1 = 0
last_pos_1 = 0
current_pos_2 = 0
last_pos_2 = 0

servo_pwm_1 = 1500
servo_pwm_2 = 1500

while True:
    current_pos_1 = count1.value()
    current_pos_2 = count2.value()
    print(count1.value())
    print(count2.value())

    if current_pos_1 > last_pos_1:
        #add
        servo_pwm_1 = min(servo_pwm_1 + 50, 2500)

        #if above, set to max


        #set servo pos
        servo_1.duty_ns(servo_pwm_1 * 1000)
    elif current_pos_1 < last_pos_1:
        #subtract
        servo_pwm_1 = max(servo_pwm_1 - 50, 500)

        #set servo pos
        servo_1.duty_ns(servo_pwm_1 * 1000)
    else:
        pass


    if current_pos_2 > last_pos_2:
        #add
        servo_pwm_2 = min(servo_pwm_2 + 50, 2500)

        #if above, set to max


        #set servo pos
        servo_2.duty_ns(servo_pwm_2 * 1000)
    elif current_pos_2 < last_pos_2:
        #subtract
        servo_pwm_2 = max(servo_pwm_2 - 50, 500)

        #set servo pos
        servo_2.duty_ns(servo_pwm_2 * 1000)
    else:
        pass

    last_pos_1 = current_pos_1
    last_pos_2 = current_pos_2
    time.sleep(0.1)
