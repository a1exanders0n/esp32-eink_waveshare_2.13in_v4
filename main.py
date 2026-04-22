from machine import Pin, SPI
import framebuf
import epd2in13_V4 as epd

# =========================
# INIT DISPLAY
# =========================
display = epd.EPD()
display.init()

# =========================
# FRAMEBUFFER
# =========================
buffer = bytearray(display.width * display.height // 8)
fb = framebuf.FrameBuffer(buffer, display.width, display.height, framebuf.MONO_HLSB)

fb.fill(1)
fb.text("HELLO HELLO HELLO HELLO HELLO HELLO HELLO HELLO HELLO HELLO HELLO HELLO HELLO ", 10, 10, 0)

# =========================
# DISPLAY
# =========================

display.display(buffer)