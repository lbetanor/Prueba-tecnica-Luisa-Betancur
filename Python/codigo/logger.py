import logging 
import sys
import os
import datetime

# Logger configuration
app_name = 'prueba_tecnica_luisa_betancur'
log = logging.getLogger(app_name)
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# FileHandler
path = os.path.abspath(".")
fecha = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_file_path = os.path.join(path, f'logs_{fecha}.log')
fh = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
log.addHandler(fh)

# StreamHandler
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
log.addHandler(ch)