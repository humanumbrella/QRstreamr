import pyqrcode
qr = pyqrcode.create("HORN O.K. PLEASE.")
qr.png("horn.png", scale=6)
import qrtools
qr = qrtools.QR()
qr.decode("horn.png")
print qr.data
