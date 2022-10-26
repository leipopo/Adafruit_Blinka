"""Pin definitions for the Odroid M1."""

from adafruit_blinka.microcontroller.amlogic.s922x import pin

GPIO3C_6 = pin.GPIO118
GPIO3C_7 = pin.GPIO119
GPIO3D_0 = pin.GPIO120
GPIO3D_1 = pin.GPIO121
GPIO3D_2 = pin.GPIO122
GPIO3D_3 = pin.GPIO123
GPIO3D_4 = pin.GPIO124
GPIO3D_5 = pin.GPIO125
GPIO3D_6 = pin.GPIO126
GPIO3D_7 = pin.GPIO127
GPIO3B_2 = pin.GPIO106
GPIO3B_5 = pin.GPIO109
GPIO3B_6 = pin.GPIO110
GPIO0B_3 = pin.GPIO11
GPIO0B_4 = pin.GPIO12
GPIO0B_5 = pin.GPIO13
GPIO0B_6 = pin.GPIO14
GPIO0C_0 = pin.GPIO16
GPIO0C_1 = pin.GPIO17
GPIO2D_0 = pin.GPIO88
GPIO2D_1 = pin.GPIO89
GPIO2D_2 = pin.GPIO90
GPIO2D_3 = pin.GPIO91
GPIO4B_6 = pin.GPIO142
GPIO4C_1 = pin.GPIO145

GPIODV_24 = pin.GPIO110
GPIODV_25 = pin.GPIO109
GPIODV_26 = pin.GPIO12
GPIODV_27 = pin.GPIO11

for it in pin.i2cPorts:
    globals()["SCL" + str(it[0])] = it[1]
    globals()["SDA" + str(it[0])] = it[2]

# Set second i2c bus as default for backward compatibility.
SCL = pin.i2cPorts[1][1]
SDA = pin.i2cPorts[1][2]

SCLK = pin.SPI0_SCLK
MOSI = pin.SPI0_MOSI
MISO = pin.SPI0_MISO
SPI_CS0 = pin.GPIO90


D16 = GPIO118  # PIN_16
D18 = GPIO119  # PIN_18
D12 = GPIO120  # PIN_12
D22 = GPIO121  # PIN_22
D26 = GPIO122  # PIN_26
D32 = GPIO123  # PIN_32
D36 = GPIO124  # PIN_36
D35 = GPIO125  # PIN_35
D8 = GPIO126  # PIN_8
D10 = GPIO127  # PIN_10
D15 = GPIO106  # PIN_15
D5 = GPIO109  # PIN_5
D3 = GPIO110  # PIN_3
D28 = GPIO11  # PIN_28
D27 = GPIO12  # PIN_27
D33 = GPIO13  # PIN_33
D7 = GPIO14  # PIN_7
D11 = GPIO16  # PIN_11
D13 = GPIO17  # PIN_13
D21 = GPIO88  # PIN_21
D19 = GPIO89  # PIN_19
D24 = GPIO90  # PIN_24
D23 = GPIO91  # PIN_23
D31 = GPIO142  # PIN_31
D29 = GPIO145  # PIN_29
