import os
import sys
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR+"/elka/modules/ws2812-spi")
sys.path.append("/home/kirill/PycharmProjects/elka/modules/ws2812-spi")

#print(BASE_DIR+"/elka/modules/ws2812-spi")

import spidev
import ws2812
spi = spidev.SpiDev()
spi.open(1,0)
ws2812.write2812(spi, [[10,0,0], [0,10,0], [0,0,10], [10, 10, 0]])