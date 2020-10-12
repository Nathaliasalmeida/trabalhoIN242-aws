import time
import paho.mqtt.client as mqtt
import json


print("Conectando ao MQTT Broker...")
mqtt_client = mqtt.Client()
mqtt_client.connect('localhost', 1883)


from pynput import keyboard

count = 0

def on_press(key):
    global count

    if key == keyboard.Key.space:
        count += 1
        print(count)
        mensagem = {
            'qts': 'pessoa(s)',
            'total': count
        }
        mqtt_client.publish('in242', json.dumps(mensagem))

def main():
    with keyboard.Listener(on_press=on_press) as listener:
         listener.join()

if __name__ == '__main__':
    main()