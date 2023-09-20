import qrcode

website_address = "https://www.ksbanalytica.com/"

# Create a QR code instance
qr_code = qrcode.QRCode(version=1, box_size=10, border=4)

# Add data to the QR code
qr_code.add_data(website_address)

# Generate the QR code as an image
qr_code.make(fit=True)
qr_code_image = qr_code.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_code_image.save("qr_code.png")
