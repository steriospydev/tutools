import qrcode
import cv2
"""
Requirements:
    qrcode
    opencv-python
"""

data = {
    'id': 12,
    'name': 'Test text',
    'quantity': 34,
    'bin' : 'A-B014F',
    'url': 'https://www.google.gr'
}

formated_data = f"""
    The {data['name']} with id {data['id']} in bin
    {data['bin']} has {data['quantity']} left in stock.
    Please follow this link for details {data['url']}.

"""

img = qrcode.make(formated_data)
img.save("test_qrcode.png")

d = cv2.QRCodeDetector()

## Django implementation
# import cv2
# from django.shortcuts import render
# from .models import Product

# def scan_qr(request):
#     if request.method == 'POST':
#         # Get the image file from the form data
#         image_file = request.FILES['image']

#         # Read the image using cv2
#         image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

#         # Decode the QR code using cv2
#         d = cv2.QRCodeDetector()
#         data, bbox, _ = d.detectAndDecode(image)

#         # If a QR code was detected, update the Product model
#         if bbox is not None:
#             product = Product.objects.get(pk=data['id'])
#             product.quantity += int(data['quantity'])
#             product.save()

#     return render(request, 'scan_qr.html')