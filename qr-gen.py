import qrcode

# 1. Your WhatsApp link (International format: 254...)
# This will open a chat with you immediately when scanned
data = "https://wa.me/254731056675" 

# 2. Setting up the QR code design
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 3. Adding your WhatsApp link to the QR generator
qr.add_data(data)
qr.make(fit=True)

# 4. Creating the image (Black code on White background)
img = qr.make_image(fill_color="black", back_color="white")

# 5. Saving the file to your laptop
# It will appear in the folder as 'my_whatsapp_qr.png'
img.save("my_whatsapp_qr.png")

print("--------------------------------------------")
print("DONE! Your WhatsApp QR code has been created.")
print("Look for 'my_whatsapp_qr.png' in your folder.")
print("--------------------------------------------")