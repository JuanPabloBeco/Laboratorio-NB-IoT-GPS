from serial import Serial
from pynmeagps import NMEAReader

from constants import GPS_SERIAL_PORT

stream = Serial(GPS_SERIAL_PORT, 9600, timeout=3)

nmr = NMEAReader(stream)
(raw_data, parsed_data) = nmr.read()
print(parsed_data)

stream.close()