import qrcode

def main():

    song= "https://youtu.be/g8SQa3icsj4?si=Rv_GwxzWybNihgF-"
    qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,border=5,)
    qr.add_data(song)
    qr.make(fit=True)
    img = qr.make_image(fill_color="DarkCyan", back_color="white")
    img.save("myqr-code.png")
if __name__ =="__main__":
    main()
