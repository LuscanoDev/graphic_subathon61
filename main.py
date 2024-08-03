import matplotlib.pyplot as plt
import requests
import numpy as np
from time import sleep, strftime
import os
import shutil

timeList = []
x = 0

folder = 'images'
if os.path.exists(folder):
    shutil.rmtree(folder, ignore_errors=False, onerror=None)
os.makedirs(folder)

def getTime():
    try:
        url = 'https://subathon-api.justdavi.dev/api/time-left'
        headers = {
            'User-Agent': 'graph-lexpdev-xyz'
        }
        responseTL = requests.get(url, headers=headers)
        responseTL.raise_for_status()
        milissecondsLeft = int(responseTL.json()['timeLeft'])
        hoursLeft = milissecondsLeft / 3600000
        return round(hoursLeft, 3)
    except:
        return 'error'

while True:
    time = getTime()
    if not time == 'error':
        print(f'{time}, time {x}')
        timeList.insert(x, time)
        ypoints = np.array(timeList)
        x = x + 1
        plt.plot(ypoints, color='black')
        
        # Adiciona o horário no topo superior direito
        current_time = strftime("%H:%M:%S")
        plt.text(0.95, 0.95, current_time, transform=plt.gca().transAxes,
                 fontsize=12, verticalalignment='top', horizontalalignment='right')
        
        plt.savefig(f'{folder}/graph_{x}.png')
        plt.clf()  # Limpa a figura para o próximo loop
    sleep(30)
