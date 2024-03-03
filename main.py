import machine, time

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)

# if not wlan.isconnected():
#     wlan.connect(dotenv.WIFI, dotenv.PASSWORD)

#     while not wlan.isconnected():
#         time.sleep(1)
#         pass

# print(wlan.ifconfig())

# sensor1 = machine.ADC(machine.Pin(34))
sensor2 = machine.ADC(machine.Pin(39))
sensor3 = machine.ADC(machine.Pin(36))
sensor4 = machine.ADC(machine.Pin(35))
sensor5 = machine.ADC(machine.Pin(32))
# sensor6 = machine.ADC(machine.Pin(33))

right = machine.Pin(27, machine.Pin.OUT)
rightBack = machine.Pin(13, machine.Pin.OUT)
left = machine.Pin(12, machine.Pin.OUT)
leftBack = machine.Pin(14, machine.Pin.OUT)

sensorTriggerValue = 800

lastSensor = -1
# 0 = right engine
# 1 = left engine

# engineSpeed1 = machine.DAC(machine.Pin(25))
# engineSpeed2 = machine.DAC(machine.Pin(26))

def goStaight():
	left.on()
	right.on()
def leftEngine():
	global lastSensor
	right.off()
	left.on()
	lastSensor = 1
def rightEngine():
	global lastSensor
	left.off()
	right.on()
	lastSensor = 0

def findLine():
	if lastSensor == 0:
		rightEngine()
	elif lastSensor == 1:
		leftEngine()
	else:
		right.off()
		left.off()


while True:

	sensor=[
		# sensor1.read(), # > sensorTriggerValue,
		sensor2.read() > sensorTriggerValue,
		sensor3.read() > sensorTriggerValue,
		sensor4.read() > sensorTriggerValue,
		sensor5.read() > sensorTriggerValue,
		# sensor6.read() # > sensorTriggerValue
	]

	if sensor[0] and not sensor[1] and not sensor[2] and sensor[3]:       goStaight()
	if sensor[0] and sensor[1] and not sensor[2] and sensor[3]:           goStaight()
	if sensor[0] and not sensor[1] and sensor[2] and sensor[3]:           goStaight()

	elif sensor[0] and not sensor[1] and not sensor[2] and not sensor[3]: leftEngine()
	elif sensor[0] and sensor[1] and not sensor[2] and not sensor[3]:     leftEngine()
	elif sensor[0] and sensor[1] and sensor[2] and not sensor[3]:         leftEngine()

	elif not sensor[0] and not sensor[1] and not sensor[2] and sensor[3]: rightEngine()
	elif not sensor[0] and not sensor[1] and sensor[2] and sensor[3]:     rightEngine()
	elif not sensor[0] and sensor[1] and sensor[2] and sensor[3]:         rightEngine()

	elif sensor[0] and sensor[1] and sensor[2] and sensor[3]:             findLine()

	# print(sensor)
	# time.sleep(0.3)

	# print(postData)
	# data = (ujson.dumps(postData)).encode()
	# headers = {'Content-Type': 'application/json'}

	# try:
	#     res = urequests.post(
	#         "http://192.168.8.111:5173/api/linefollower",
	#         headers=headers,
	#         data=data)

	#     res.close()
	#     print("request send")

	# except Exception as e:
	#     print("Error:", e)