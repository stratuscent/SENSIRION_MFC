import time
from sensirion_shdlc_driver.errors import ShdlcDeviceError
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sfc5xxx import Sfc5xxxShdlcDevice, Sfc5xxxScaling, \
    Sfc5xxxValveInputSource, Sfc5xxxUnitPrefix, Sfc5xxxUnit, \
    Sfc5xxxUnitTimeBase, Sfc5xxxMediumUnit
import logging

logging.basicConfig(level=logging.INFO)

class MFC:
    def __init__(self, port):
        _ = ShdlcSerialPort(port=port, baudrate=115200)
        self.device = Sfc5xxxShdlcDevice(ShdlcConnection(_), slave_address=0)
        self.unit = Sfc5xxxMediumUnit(
        Sfc5xxxUnitPrefix.MILLI,
        Sfc5xxxUnit.STANDARD_LITER,
        Sfc5xxxUnitTimeBase.MINUTE)
    
        self.device.set_user_defined_medium_unit(self.unit)

        print(f'Version: {self.device.get_product_name()}\nProduct Name: {self.device.get_product_name()}\nArticle Code: {self.device.get_article_code()}')

    def run(self):
        self.val = 0
        while self.val != 999:
            # self.val = int(input('Type in a number to set the flow rate, or type in 999 to exit the command system: '))
            self.val = int(input('Type in 0 to turn off, 1 to turn on, 999 to exit the system: '))
            if self.val == 999:
                break
            else:
                self.set_value(self.val)
        self.exit_procedure()
    
    def exit_procedure(self):
        self.set_value(0)
        logging.info("Exiting the system")
        

    def set_value(self, val):
        if val == 0:
            _ = 0
            logging.info("Turning MFC Off")
        else:
            _ = 500
            logging.info("Turning MFC On")
        self.device.set_setpoint(_, Sfc5xxxScaling.USER_DEFINED)
        logging.info(f"New setpoint of {val}")
        


if __name__ == "__main__":
    A = MFC("/dev/ttyUSB4")
    A.run()



