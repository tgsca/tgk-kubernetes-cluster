import socket
from subprocess import check_output
from .lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont

class Oled96:
    """ This class is responsible for displaying information on OLED96 displays """
    """
    To get this work please see also the tutorial on:
    https://indibit.de/raspberry-pi-oled-display-128x64-mit-python-ansteuern-i2c/
    """

    def __init__(self):
        self.hostname = socket.gethostname()
        self.ip = check_output(['hostname', '-I']).decode("utf-8").split(' ')[0]

        # Display einrichten
        self.i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
        self.oled = ssd1306(self.i2cbus)

        # Schriftarten festlegen
        self.FreeSans12 = ImageFont.truetype('./fonts/FreeSans.ttf', 12)
        self.FreeSans20 = ImageFont.truetype('./fonts/FreeSans.ttf', 20)

    def clear(self):
        # Display zum Start löschen
        self.oled.cls()
        self.oled.display()

    def show(self, status: str = 'Running...'):
        # Ausgaben definieren
        self.oled.canvas.text((0, 0), f'{self.hostname}', font=self.FreeSans20, fill=1)
        self.oled.canvas.text((0, 22), f'{self.ip}:5000', font=self.FreeSans12, fill=1)
        self.oled.canvas.text((0, 40), f'{status}', font=self.FreeSans20, fill=1)
        # Ausgaben auf Display schreiben
        self.oled.display()
