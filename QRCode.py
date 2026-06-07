import qrcode

def main():
    data = "https://github.com/Matin-python/"
    # data = "SMSTO:+989123456789: Hi, How are you doing?"

    qr = qrcode.make(data)

    qr.save("QR Code Output.png")
    qr.show()

if __name__ == "__main__":
    main()
