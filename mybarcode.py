import barcode
from barcode.writer import ImageWriter

# The barcode data must be a 13-digit string for EAN-13
number = "4120108576798"

# Get the EAN13 barcode class and generate the barcode
ean = barcode.get_barcode_class('ean13')
ean_barcode = ean(number, writer=ImageWriter())

# Save the barcode image to a file (e.g., "barcode.png")
filename = ean_barcode.save("barcode")
print(f"Barcode saved as {filename}.png")
