import qrcode

#Creamos un objeto qr
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)
#Agregamos la url que queremos que tenga el qr
qr.add_data('https://github.com/santiagohg619?tab=repositories')
qr.make(fit=True)

#Creamos una imagen
img = qr.make_image(fill_color = "black", back_color = "white")
img.save("repositoriosQR.png")