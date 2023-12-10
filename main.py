import machine, network, urequests, ujson, esp32, time, dotenv

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)

# if not wlan.isconnected():
#     wlan.connect(dotenv.WIFI, dotenv.PASSWORD)

#     while not wlan.isconnected():
#         time.sleep(1)
#         pass

# print(wlan.ifconfig())

sensor1 = machine.ADC(machine.Pin(34))
sensor2 = machine.ADC(machine.Pin(39))
sensor3 = machine.ADC(machine.Pin(36))
sensor4 = machine.ADC(machine.Pin(35))
sensor5 = machine.ADC(machine.Pin(32))
sensor6 = machine.ADC(machine.Pin(33))

light1 = machine.Pin(23, machine.Pin.OUT)
light2 = machine.Pin(22, machine.Pin.OUT)
light3 = machine.Pin(1, machine.Pin.OUT)
light4 = machine.Pin(3, machine.Pin.OUT)
light5 = machine.Pin(21, machine.Pin.OUT)
light6 = machine.Pin(19, machine.Pin.OUT)

left = machine.Pin(13, machine.Pin.OUT)
leftBack = machine.Pin(12, machine.Pin.OUT)
right = machine.Pin(27, machine.Pin.OUT)
rightBack = machine.Pin(14, machine.Pin.OUT)

sensorTriggerValue = 800

lastSensor = -1
ticks = 0


while True:

    sensor=[
        sensor1.read() > sensorTriggerValue,
        sensor2.read() > sensorTriggerValue,
        sensor3.read() > sensorTriggerValue,
        sensor4.read() > sensorTriggerValue,
        sensor5.read() > sensorTriggerValue,
        sensor6.read() > sensorTriggerValue
    ]

    if sensor[0]: light1.on()
    else: light1.off()
    if sensor[1]: light2.on()
    else: light2.off()
    if sensor[2]: light3.on()
    else: light3.off()
    if sensor[3]: light4.on()
    else: light4.off()
    if sensor[4]: light5.on()
    else: light5.off()
    if sensor[5]: light6.on()
    else: light6.off()


    if sensor[4]:
        lastSensor = 4
        right.on()
    else: right.off()

    if sensor[1]:
        lastSensor = 1
        left.on()
    else: left.off()

    if not sensor[4] and not sensor[1]:
        left.on()
        right.on()

        ticks += 1
        if ticks >= 20000:
            left.off()
            right.off()

            break
    
    else: ticks = 0


    # print(sensor)
    # time.sleep(1)

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

    # time.sleep(2)
