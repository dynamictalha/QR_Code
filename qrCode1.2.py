import qrcode
# Data to encode
data = "https://www.programiz.com/cpp-programming/online-compiler/"
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'green',
                    back_color = 'black')
 
img.save('CppCompoler.png')
