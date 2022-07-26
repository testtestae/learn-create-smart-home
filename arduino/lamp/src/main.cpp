#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <MQTT.h>

const char ssid[] = "101";
const char pass[] = "it123456";
char MQTTClientId[] = "lamp"; 
char MQTTBrockerPath[] = "";
char MQTTLogin[] = "";
char MQTTPassword[] = "";
char MQTTTopicSubscribe[] = "";
char MQTTTopicPublish[] = "";

WiFiClient net;
MQTTClient client;

unsigned long lastMillis = 0;

void connect() {
  Serial.print("checking wifi...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }

  Serial.print("\nconnecting...");
  while (!client.connect(MQTTClientId, MQTTLogin, MQTTPassword)) {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("\nconnected!");

  client.subscribe(MQTTTopicSubscribe);
}


void messageReceived(String &topic, String &payload) {
  // Serial.println("incoming: " + topic + " - " + payload);
  digitalWrite(2, payload.toInt());
  Serial.println(payload);
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, pass);

  client.begin(MQTTBrockerPath, net);
  client.onMessage(messageReceived);

  connect();

  pinMode(2, OUTPUT);
}

void loop() {
  client.loop();
  delay(10);

  if (!client.connected()) {
    connect();
  }

  // if (millis() - lastMillis > 1000) {
  //   lastMillis = millis();
  //   client.publish(MQTTTopicPublish, "world");
  // }
}