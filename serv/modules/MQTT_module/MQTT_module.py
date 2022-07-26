import time
from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt

broker = "hatebutterfly129.cloud.shiftr.io"
port = 1883
# topic = "mqtt_task_stack"
client_id = "serv"
username = 'hatebutterfly129'
password = "Dl8vTnX4IqNBCiCO"


client = mqtt_client.Client(client_id)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


async def MQTT_module(stacks):
    clientRun = connect_mqtt()
    clientRun.loop_start()
    mqtt_task_stack = stacks
    while True:
        for i in mqtt_task_stack:
            topic = i["device"]
            value = i["setState"]

            result = client.publish(topic, value)


            result: [0, 1]
            status = result[0]
            if status == 0:
                mqtt_task_stack.pop(0)
                print(f"Отправлено `{value}` в топик `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")

