import subprocess
import time

services = ['MicrosoftSearchInBing','Spooler']


def res_serv(servName):
    try:
        stop_comm = f'net stop {servName}'
        subprocess.run(stop_comm, check=True, shell=True)

        time.sleep(6)

        start_comm = f'net start {servName}'
        subprocess.run(start_comm, check=True, shell=True)

        print(f'Successfull in restarting {servName}')
    except subprocess.CalledProcessError as er:
        print(f'Failed to restart the service {servName}: {er}')


for serv in services:
    res_serv(serv)
