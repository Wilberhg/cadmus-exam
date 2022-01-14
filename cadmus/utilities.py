from datetime import datetime
import os

class Utilities:
    def __init__(self, error):
        self.error = error

    def register_log(self):
        dt_today = datetime.now()
        dt_now = dt_today.strftime('%d_%m_%Y')
        hr_now = dt_today.strftime('%H:%M:%S')
        os.makedirs('./logs', exist_ok=True)
        with open(f'./logs/Log_{dt_now}.txt', 'a+') as arqv:
            arqv.write(f'{hr_now} ::: {self.error}\n')