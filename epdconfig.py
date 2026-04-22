from machine import Pin, SPI
import time

# === PINS ===
RST_PIN  = Pin(2, Pin.OUT)
DC_PIN   = Pin(3, Pin.OUT)
CS_PIN   = Pin(4, Pin.OUT)
BUSY_PIN = Pin(5, Pin.IN)

# SPI (!!!)
spi = SPI(2,
          baudrate=2000000,
          polarity=0,
          phase=0,
          sck=Pin(15),
          mosi=Pin(14),
          miso=None)

# === FUNC ===

def digital_write(pin, value):
    pin.value(value)

def digital_read(pin):
    return pin.value()

def delay_ms(ms):
    time.sleep_ms(ms)

def spi_writebyte(data):
    spi.write(bytearray(data))

def spi_writebyte2(data):
    spi.write(bytearray(data))

def module_init():
    return 0

def module_exit():
    pass