import qrcode

def get_user_input():
    data = input("Enter the data or URL to generate QR code: ").strip()
    output_file_name = input("Enter the output file name to save the QR code image (with .png extension): ").strip()
    return data, output_file_name


# Generate QR code
def generate_qr_code(data, output_file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file_name)
    print(f"QR code generated and saved as {output_file_name}.")

data, output_file_name = get_user_input()
generate_qr_code(data, output_file_name)