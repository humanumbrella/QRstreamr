import pyqrcode

from qrtools import QR
# qr = pyqrcode.create("HORN O.K. PLEASE.")
# qr.png("horn.png", scale=6)

# for i in range (0,10):
    # qr = pyqrcode.create(str(i)+" s")
    # qr.png(str(i)+".png",scale=6)

big_code = pyqrcode.create('0987654321', error='L', version=40, mode='binary')
big_code.png('code.png', scale=6)
big_code.show()


my_QR = QR(filename="code.png")
my_QR.decode()
print my_QR.data