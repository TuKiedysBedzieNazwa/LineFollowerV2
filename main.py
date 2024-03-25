import machine, time

sensor1 = machine.ADC(machine.Pin(34))
sensor2 = machine.ADC(machine.Pin(39))
sensor3 = machine.ADC(machine.Pin(36))
sensor4 = machine.ADC(machine.Pin(35))
sensor5 = machine.ADC(machine.Pin(32))
sensor6 = machine.ADC(machine.Pin(33))

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

# engineSpeed1.write(178)
# engineSpeed2.write(178)


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
		sensor1.read() > sensorTriggerValue,
		sensor2.read() > sensorTriggerValue,
		sensor3.read() > sensorTriggerValue,
		sensor4.read() > sensorTriggerValue,
		sensor5.read() > sensorTriggerValue,
		sensor6.read() > sensorTriggerValue
	]

	if sensor[0] and sensor[1] and sensor[2] and not sensor[3] and sensor[4] and sensor[5]: leftEngine()
	elif sensor[0] and sensor[1] and sensor[2] and not sensor[3] and not sensor[4] and sensor[5]: leftEngine()
	elif sensor[0] and sensor[1] and sensor[2] and not sensor[3] and not sensor[4] and not sensor[5]: leftEngine()
	elif sensor[0] and sensor[1] and sensor[2] and sensor[3] and not sensor[4] and sensor[5]: leftEngine()
	elif sensor[0] and sensor[1] and sensor[2] and sensor[3] and not sensor[4] and not sensor[5]: leftEngine()
	elif sensor[0] and sensor[1] and sensor[2] and sensor[3] and sensor[4] and not sensor[5]: leftEngine()

	elif sensor[0] and sensor[1] and not sensor[2] and sensor[3] and sensor[4] and sensor[5]: rightEngine()
	elif sensor[0] and not sensor[1] and not sensor[2] and sensor[3] and sensor[4] and sensor[5]: rightEngine()
	elif not sensor[0] and not sensor[1] and not sensor[2] and sensor[3] and sensor[4] and sensor[5]: rightEngine()
	elif sensor[0] and not sensor[1] and sensor[2] and sensor[3] and sensor[4] and sensor[5]: rightEngine()
	elif not sensor[0] and not sensor[1] and sensor[2] and sensor[3] and sensor[4] and sensor[5]: rightEngine()
	elif not sensor[0] and sensor[1] and sensor[2] and sensor[3] and sensor[4] and sensor[5]: rightEngine()

	elif sensor[0] and sensor[1] and not sensor[2] and not sensor[3] and sensor[4] and sensor[5]: goStaight()
	# if       sensor[0] and     sensor[1] and not sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: goStaight()
	# if       sensor[0] and     sensor[1] and     sensor[2] and not sensor[3] and     sensor[4] and     sensor[5]: goStaight()
	elif sensor[0] and sensor[1] and sensor[2] and sensor[3] and sensor[4] and sensor[5]: findLine()

	print(sensor)
	# time.sleep(0.3)