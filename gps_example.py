import GNSS.get_NMEA_msg as gps_get
from serial import Serial

from constants import GPS_SERIAL_PORT

GNSSPort = Serial(GPS_SERIAL_PORT, 9600, timeout=3)

GNSS_msg = gps_get.NMEA_message(GNSSPort)
print (GNSS_msg["raw_data"])
print (GNSS_msg["parsed_data"])

GNSSPort.close()