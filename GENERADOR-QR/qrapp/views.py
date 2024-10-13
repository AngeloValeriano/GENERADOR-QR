from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.core.files.base import ContentFile
import base64

# Página de inicio
def index(request):
    return render(request, 'qrapp/index.html')

# Función para generar el código QR
def generar_qr(request):
    if request.method == 'POST':
        data = request.POST.get('data')  # Obtener el texto ingresado

        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Convertir la imagen a base64 para mostrar en la web
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return render(request, 'qrapp/index.html', {'img_str': img_str, 'data': data})

    return render(request, 'qrapp/index.html')
