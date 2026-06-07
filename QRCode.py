import qrcode

qr = qrcode.make("https://github.com/Matin-python/")
# qr = qrcode.make("SMSTO:+989123456789: Hi, How are you doing?")


qr.save("QR Code Output.png")
qr.show()