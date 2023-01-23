from machine import Pin 
from machine import Pin, I2C
import machine
import ssd1306 
import dht
import time

i2c = I2C(scl=Pin(22), sda=Pin(21))   #inisiasi pin OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)

p15 = Pin(27, Pin.IN)     #inisiasi pin DHT22
d=dht.DHT22(p15)

while True:
  d.measure()   #pengukuran suhu dan kelembaban
  t=d.temperature()    #pembacaan suhu
  h=d.humidity()       #pembacaan kelembaban
  print('Temperature =', t, 'C', 'Humidity =', h, '%')   #menampilkan suhu dan kelembaban pada serial monitor
  time.sleep(1)      #delay 1 detik
  oled.fill(0)
  oled.text("Temperature", 20, 10)  #menampilkan suhu pada OLED
  oled.text(str(t), 40, 20)
  oled.text("C", 60, 20)
  oled.text("Humidity", 30, 40)    #menampilkan kelembaban pada OLED
  oled.text(str(h), 40, 55)
  oled.text("%", 60, 55)
  oled.show()