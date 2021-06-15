import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=2)
#here we have to give link for which we want to generate qr
qr.add_data("https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg")
qr.make(fit=True)

#customizing qr
img = qr.make_image(fill_color="orange",back_color="black")
#making qr in another file as advanced.png
img.save("Advanced.png")
