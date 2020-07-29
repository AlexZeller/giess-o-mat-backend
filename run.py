import logging
from giessomat import Database
from giessomat import LightControl
from giessomat import VentilationControl
from giessomat import IrrigationControl

# Set up logging
logging.basicConfig(filename='giessomat.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
log = logging.getLogger(__name__)

log.info('Starting run...')

# Read sensor values and write to database
try:
    db = Database.Database('/home/pi/Giess-o-mat/giessomat_db.db')
    db.sensordata2database()
except:
    log.critical('Failed to read sensor values/write to database')

# Execute control functions according to settings
try:
    light_control = LightControl.LightControl(
        '/home/pi/Giess-o-mat-Webserver/light_settings.json')
    light_control.execute()
except:
    log.critical('Failed to execute light control')
try:
    ventilation_control = VentilationControl.VentilationControl(
        '/home/pi/Giess-o-mat-Webserver/ventilation_settings.json')
    ventilation_control.execute()
except:
    log.critical('Failed to execute ventilation control')
try:
    irrigation_control = IrrigationControl.IrrigationControl(
        '/home/pi/Giess-o-mat-Webserver/irrigation_settings.json')
except:
    log.critical('Failed to execute irrigation control')
    irrigation_control.execute()

log.info('Finished!')
