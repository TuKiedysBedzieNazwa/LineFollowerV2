import machine

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

rightSpeed = machine.DAC(machine.Pin(25))
leftSpeed = machine.DAC(machine.Pin(26))

rightSpeed.write(255)
leftSpeed.write(255)

time = 0

minEnginesSpeed = 255

leftSpeedAjustValue = minEnginesSpeed
rightSpeedAjustValue = minEnginesSpeed


def goStaight():
	rightSpeed.write(255)
	leftSpeed.write(255)

	left.on()
	right.on()

def leftEngine():
	rightSpeed.write(255)
	leftSpeed.write(255)

	global lastSensor
	rightBack.off()
	leftBack.off()
	right.off()
	left.on()
	lastSensor = 1

def leftEngineAjust(value: int):
	global time, leftSpeedAjustValue, rightSpeedAjustValue, lastSensor
	leftSpeed.write(255)

	if time % 1000 == 0:
		if leftSpeedAjustValue > value:
			leftSpeedAjustValue -= 1
		elif leftSpeedAjustValue < minEnginesSpeed:
			leftSpeedAjustValue += 1

	rightSpeed.write(leftSpeedAjustValue)
	rightSpeedAjustValue = minEnginesSpeed

	rightBack.off()
	leftBack.off()
	right.on()
	left.on()
	lastSensor = 1

def rightEngine():
	rightSpeed.write(255)
	leftSpeed.write(255)

	global lastSensor
	rightBack.off()
	leftBack.off()
	left.off()
	right.on()
	lastSensor = 0

def rightEngineAjust(value: int):
	global time, leftSpeedAjustValue, rightSpeedAjustValue, lastSensor
	rightSpeed.write(255)

	if time % 1000 == 0:
		if rightSpeedAjustValue > value:
			rightSpeedAjustValue -= 1
		elif rightSpeedAjustValue < minEnginesSpeed:
			rightSpeedAjustValue += 1

	leftSpeed.write(rightSpeedAjustValue)

	leftSpeedAjustValue = minEnginesSpeed

	global lastSensor
	rightBack.off()
	leftBack.off()
	left.on()
	right.on()
	lastSensor = 0

def findLine():
	if lastSensor == 0:
		rightEngine()
		leftBack.on()
	elif lastSensor == 1:
		leftEngine()
		rightBack.on()
	else:
		right.off()
		left.off()


while True:

	if time == 100000: time = 0
	time += 1

	sensor=[
		sensor1.read() > sensorTriggerValue,
		sensor2.read() > sensorTriggerValue,
		sensor3.read() > sensorTriggerValue,
		sensor4.read() > sensorTriggerValue,
		sensor5.read() > sensorTriggerValue,
		sensor6.read() > sensorTriggerValue
	]

	if       sensor[0] and     sensor[1] and not sensor[2] and not sensor[3] and     sensor[4] and     sensor[5]: goStaight()
	elif     sensor[0] and     sensor[1] and not sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: goStaight()
	elif     sensor[0] and     sensor[1] and     sensor[2] and not sensor[3] and     sensor[4] and     sensor[5]: goStaight()
	# elif not sensor[0] and not sensor[1] and not sensor[2] and not sensor[3] and not sensor[4] and not sensor[5]: goStaight()

	elif     sensor[0] and     sensor[1] and     sensor[2] and not sensor[3] and not sensor[4] and     sensor[5]: leftEngineAjust(152)
	elif     sensor[0] and     sensor[1] and     sensor[2] and     sensor[3] and not sensor[4] and     sensor[5]: leftEngineAjust(38)
	elif     sensor[0] and     sensor[1] and     sensor[2] and not sensor[3] and not sensor[4] and not sensor[5]: rightEngine()
	elif     sensor[0] and     sensor[1] and     sensor[2] and     sensor[3] and not sensor[4] and not sensor[5]: leftEngine()
	elif     sensor[0] and     sensor[1] and     sensor[2] and     sensor[3] and     sensor[4] and not sensor[5]: leftEngine()

	elif     sensor[0] and not sensor[1] and not sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: rightEngineAjust(152)
	elif     sensor[0] and not sensor[1] and     sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: rightEngineAjust(38)
	elif not sensor[0] and not sensor[1] and not sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: rightEngine()
	elif not sensor[0] and not sensor[1] and     sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: rightEngine()
	elif not sensor[0] and     sensor[1] and     sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: rightEngine()

	elif     sensor[0] and     sensor[1] and     sensor[2] and     sensor[3] and     sensor[4] and     sensor[5]: findLine()