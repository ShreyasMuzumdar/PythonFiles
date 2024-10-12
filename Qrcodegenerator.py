import os
import segno
folder_path = "/Users/shreyas/Documents/PythonFiles/QRcodes"
data = input("Enter the data you would like to turn into a qr code:")
qrcode = segno.make_qr(data)
file_path = os.path.join(folder_path, "qrcode.png")
qrcode.save(
    file_path,
    scale=10,
    border=0,
    light="white"
)