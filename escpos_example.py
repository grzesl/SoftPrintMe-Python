from escpos.printer import Network
from escpos.constants import GS
import six
import time
from datetime import datetime

printer = Network("192.168.1.100") #Printer IP Address
printer.set(align='center')
printer.set(font='a', height=2, align='center')
printer.text("\n")
printer.text("This is SoftPrintMe\n")
printer.text("Printout date time:" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "\n")
printer.text("Integration with python-escpos library\n")
printer.text("\n")
printer.image("python.png")
printer.set(font='a', height=1, align='center')
printer.text("\n")
printer.text("python.org\n")
printer.text("\n")
printer.qr("support@softprint.me")
printer.text("\n")
printer.barcode('softprint.me', 'CODE128', function_type="B")
printer.text("\n")
printer.set(font='a', height=1, align='left') #uninit
printer._raw(GS + b'V' + six.int2byte(66) + b'\x00') #Cut not working in this library

time.sleep(1) #take some time before close