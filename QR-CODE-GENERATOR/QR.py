import qrcode as qr  # imported qrcode library to make QR

LINK = input("enter the link u want to make QR of :")   # input of the link we want to make QR of 

img = qr.make(LINK)  # QR is saved in the img variable 
name = input("enter the name of the image u want to store it as :") # input to give name to the image(QR) which will be stored in the desired folder 
img.save(fr"F:\CODING\PROJECTS\QR\SAVED QRCODE\{name}.png")  # storing the image in the desired location
img.show()  # this will open the image in the default system viewer