# import RPi.GPIO as GPIO
from pn532 import PN532_SPI
from Data import api

class NFCscanner:
    def __init__(self, pn532):
        self.pn532 = pn532
        self.api = api.API()
        self.code = ""

    def on_connect(self, tag):
        print(f"Tag connected: {tag}")

    def on_release(self, tag):
        print(f"Tag released: {tag}")

    def scan(self):
        try:
            ic, ver, rev, support = self.pn532.get_firmware_version()
            print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

            # Configure PN532 to communicate with MiFare cards
            self.pn532.SAM_configuration()

            print(' Waiting for RFID/NFC card...')
            while True:
                # Check if a card is available to read
                uid = self.pn532.read_passive_target(timeout=0.5)
                print('', end="")
                # Try again if no card is available.
                if uid is None:
                    continue

                self.code = "".join(str(i) for i in uid)
                print(self.code)

                # Add your custom actions with the UID, for example, call a function or send it to a server.
            self.api.login("tnc.banh1@ad-academie.nl", "20qKy_u}5R")
            student = self.api.get_student_by_tag_id(self.code)

            print(student)
            return student

        except KeyboardInterrupt:
            print("NFC scanning stopped.")
        except Exception as e:
            print(e)
        finally:
            GPIO.cleanup()