from datetime import datetime
from time import sleep
from NBIOT.configuration import start_up_nbiot
from NBIOT.send_cmd import send_cmd
from serial import Serial



NBIOT_port = Serial(port='COM19', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5)

cmd_response = send_cmd("AT", NBIOT_port,  print_response=True, ms_of_delay_after=100)

response = start_up_nbiot(NBIOT_port)

while True:
    cmd_response = send_cmd("AT+CSQ", NBIOT_port, print_final_response=False)
    
    # m_of_delay = 
    # s_of_delay = m_of_delay/60

    s_of_delay = 1

    sleep(s_of_delay)

NBIOT_port.close()