import RPi.GPIO as GPIO
import time

# Configurar el pin PWM de prueba
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 200)
pwm.start(0)
pwm_duty = 30  # 10550 = 800uS, 30000 = 2200uS
pwm.ChangeDutyCycle(pwm_duty)

GPIO.setup(12, GPIO.IN)

# Variables para el temporizador y el estado de detección
detected = False

# Función para manejar la detección de la señal
def handle_detection(channel):
    global detected
    detected = False

# Configurar la detección en el pin
GPIO.add_event_detect(12, GPIO.RISING, callback=handle_detection, bouncetime=5)

while True:
    while GPIO.input(12) == GPIO.LOW:
        pass

    start = time.time()

    while GPIO.input(12) == GPIO.HIGH:
        pass

    end = time.time()
    duration = (end - start) * 1e6
    
    if duration > 1400 and duration < 1500:
        print('on hold', duration)
    elif duration < 1500 and duration > 990:
        print('backwards', duration)
    else:
        print('forward', duration) 
        
    
    if duration > 1000:
        print("ON")
        detected = True
        #GPIO.add_event_detect(12, GPIO.RISING, callback=handle_detection, bouncetime=5)
    else:
        if detected:
            print("OFF")
        else:
            print("On hold")

