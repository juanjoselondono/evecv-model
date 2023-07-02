import RPi.GPIO as GPIO
import time

# Configurar los pines de entrada
pin_pwm1 = 12
pin_pwm2 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pwm1, GPIO.IN)
GPIO.setup(pin_pwm2, GPIO.IN)

# Variables para el temporizador y el estado de detección
detected1 = False
detected2 = False
# Variable onHold para parar motores
onHold = True
# Función para manejar la detección de la señal
def handle_detection1(channel):
    global detected1
    detected1 = False

def handle_detection2(channel):
    global detected2
    detected2 = False
    
def smooth_data(value, window_size):
    data = [value] * window_size
    smoothed_value = sum(data) / window_size
    return int(smoothed_value)

def init():  
      
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(pin_pwm1, GPIO.IN)
    GPIO.setup(pin_pwm2, GPIO.IN)
    
def forward(sec):
    
    init()
    GPIO.output(27, False)
    GPIO.output(22, True)
    GPIO.output(23, True)
    GPIO.output(24, False)
    time.sleep(sec)
    GPIO.cleanup() 
    
def reverse(sec):
    
    init()
    GPIO.output(27, True)
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(sec)
    GPIO.cleanup()

def left_turn(sec):
    init()
    GPIO.output(27, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(24, False)
    time.sleep(sec)
    GPIO.cleanup()

def right_turn(sec):
    
    init()
    GPIO.output(27, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(sec)
    GPIO.cleanup()
# Configurar la detección en los pines
GPIO.add_event_detect(pin_pwm1, GPIO.RISING, callback=handle_detection1, bouncetime=5)
GPIO.add_event_detect(pin_pwm2, GPIO.RISING, callback=handle_detection2, bouncetime=5)


while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_pwm1, GPIO.IN)
    GPIO.setup(pin_pwm2, GPIO.IN)
    while GPIO.input(pin_pwm1) == GPIO.LOW:
        pass
    start1 = time.time()

    while GPIO.input(pin_pwm1) == GPIO.HIGH:
        pass

    end1 = time.time()
    duration1 = (end1 - start1) * 1e6
    duration1 = smooth_data(duration1, 30)

    if duration1 > 1000 and duration1 < 1500:
        print('on hold 1', duration1)
    elif duration1 < 1000:
        print('backwards 1', duration1)
        reverse(0.1)
    elif duration1 > 1800:
        print('forward 1', duration1)
        forward(0.1)

    # while GPIO.input(pin_pwm2) == GPIO.LOW:
        # pass
    # start2 = time.time()

    # while GPIO.input(pin_pwm2) == GPIO.HIGH:
        # pass

    # end2 = time.time()
    # duration2 = smooth_data((end2 - start2) * 1e6, 20)

    # if duration2 > 600 and duration2 < 950:
        # print('right', duration2)
    # elif duration2 < 350:
        # print('left', duration2)
    # time.sleep(0.25)
