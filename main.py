import machine, network, urequests, ujson, esp32, time, dotenv

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    wlan.connect(dotenv.WIFI, dotenv.PASSWORD)

    while not wlan.isconnected():
        time.sleep(1)
        pass

print(wlan.ifconfig())
machine.Pin(2, machine.Pin.OUT).on()

headers = {'content-type': 'application/json'}

while True:
    postData = ujson.dumps([esp32.raw_temperature()])

    try:
        res = urequests.post("http://192.168.8.109:5173/api/test", headers=headers, data=postData)
        print("success")
        res.close()

    except Exception as e:
        print("Error:", e)
