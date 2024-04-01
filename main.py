import qrcode as qr

img = qr.make("https://www.w3schools.com/python/")
img.save("W3school_python.png")