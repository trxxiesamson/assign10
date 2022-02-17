import qrcode

features = qrcode.QRCode(version = 1, 
                        error_correction = qrcode.constants.ERROR_CORRECT_L,
                        box_size = 40,
                        border = 3)

features.make(fit = True)
generate_image = features.make_image(fill_color = "black", back_color = "white")

generate_image = qrcode.make("Contact Person Details \n \n Name: Trixie\nAge: 18 years old\nResiding Address: 06 Empty Rd St, Bonifacio Global City, Taguig City\nContact No: +6399477075000\nEmail Address: trxxiesamson@gmail.com\nVaccine Status: Fully Vaccinated")

generate_image.save('qrcode_trx.png')