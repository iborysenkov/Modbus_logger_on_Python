#import os
import time
import pandas as pd
from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="192.168.1.130", auto_open=True, auto_close=True)
ID_for_input = 0

while True:
    regs = c.read_holding_registers(0, 5)
    if regs:
        current_time = time.strftime("%H:%M:%S", time.localtime())

        print(ID_for_input, {current_time}, regs[0], regs[1])
        ID_for_input += 1
        ID_for_input_string = str(ID_for_input)
        #os.system('cls')

        data = {
           'ID': ID_for_input_string,
           'Date_and_time': current_time,
           'Parameter1': regs[0],
           'Parameter2': regs[1],
           'Parameter3': regs[2],
           'Parameter4': regs[3],
           'Parameter5': regs[4],
        }
        df = pd.DataFrame([data])
        with open('timestamp.csv', 'a', newline='') as f:
            # Write the new row to the file
            df.to_csv(f, index=False, header=False)

    else:
        print("read error")
