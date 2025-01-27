# P
import RPi.GPIO as GPIO
import socket
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

UDP_IP = "192.168.1.100" 
UDP_PORT = 1234

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

input_pins = [5, 7, 12, 13, 16, 21, 25]    


for pin in input_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        for i, input_pin in enumerate(input_pins):
            input_state = GPIO.input(input_pin)
            if input_state == False:
                TALLY = (f'Tally {i + 1} OFF')
                print(TALLY)
                bTALLY = TALLY.encode()
                sock.sendto(bTALLY, (UDP_IP, UDP_PORT))
                time.sleep(0.1)
            else:
                TALLY = (f'Tally {i + 1} ON')
                print(TALLY)
                bTALLY = TALLY.encode()
                # b'TALLY=0\n'
                sock.sendto(bTALLY, (UDP_IP, UDP_PORT))
                time.sleep(0.1)
            
                
except KeyboardInterrupt:
        GPIO.cleanup()
finally:
        GPIO.cleanup()
