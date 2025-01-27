import socket
import RPi.GPIO as GPIO


UDP_IP = "0.0.0.0" # escucha a todos
UDP_PORT = 1234 # puerto

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

output_pins = [5, 7, 12, 13, 16, 21, 25] 

for pin in output_pins:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


try:
    while True:
      data, addr = sock.recvfrom(512) 
      
      if data==b'Tally 1 ON':
        print("TALLY 1 ON")
        GPIO.output(5, GPIO.HIGH)
      elif data==b'Tally 1 OFF':
        print("TALLY 1 OFF")
        GPIO.output(5, GPIO.LOW)
      elif data==b'Tally 2 ON':
        print("TALLY 2 ON")
        GPIO.output(7, GPIO.HIGH)
      elif data==b'Tally 2 OFF':
        print("TALLY 2 OFF")
        GPIO.output(7, GPIO.LOW)
      elif data==b'Tally 3 ON':
        print("TALLY 3 ON")
        GPIO.output(12, GPIO.HIGH)
      elif data==b'Tally 3 OFF':
        print("TALLY 3 OFF")
        GPIO.output(12, GPIO.LOW)
      elif data==b'Tally 4 ON':
        print("TALLY 4 ON")
        GPIO.output(13, GPIO.HIGH)
      elif data==b'Tally 4 OFF':
        print("TALLY 4 OFF")
        GPIO.output(13, GPIO.LOW)
      elif data==b'Tally 5 ON':
        print("TALLY 5 ON")
        GPIO.output(16, GPIO.HIGH)
      elif data==b'Tally 5 OFF':
        print("TALLY 5 OFF")
        GPIO.output(16, GPIO.LOW)
      elif data==b'Tally 6 ON':
        print("TALLY 6 ON")
        GPIO.output(21, GPIO.HIGH)
      elif data==b'Tally 6 OFF':
        print("TALLY 6 OFF")
        GPIO.output(21, GPIO.LOW)
      elif data==b'Tally 7 ON':
        print("TALLY 7 ON")
        GPIO.output(25, GPIO.HIGH)
      elif data==b'Tally 7 OFF':
        print("TALLY 7 OFF")
        GPIO.output(25, GPIO.LOW)
                                
except KeyboardInterrupt:
        GPIO.cleanup()
finally:
        GPIO.cleanup()
