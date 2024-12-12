import socket
import time
import random
import sense_hat


sense = sense_hat.SenseHat()

def GetData():
    temp = sense.temp * 20
    return int(temp)

def ShowDataOnPi(value):
    sense.show_message('CO2: ' + str(value))

SENSOR_ID = 1
BROADCAST_IP = '<broadcast>'
PORT = 5005
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket to broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    value = GetData()
    MSG = bytes(str(SENSOR_ID) + " " + str(value), 'utf-8')
    sock.sendto(MSG, (BROADCAST_IP, PORT))
    ShowDataOnPi(value)
    time.sleep(1)