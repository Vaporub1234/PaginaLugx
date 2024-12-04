import http.server
import socketserver
import cgi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PORT = 8085

# Función para enviar el correo
def send_coupon(email):
    from_email = "leomya1906@gmail.com"  # Tu correo electrónico
    password = "xybj zqez bfmh ymgs"  # Tu contraseña o app password si usas Gmail

    # Crear el mensaje
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = email
    msg["Subject"] = "¡Tu cupón de descuento!"

    body = """
    ¡Gracias por suscribirte! Aquí tienes tu cupón de descuento exclusivo:
    
    CUPON20 - 20% de descuento en tu próxima compra.
    
    ¡Disfruta de tus compras!
    """
    msg.attach(MIMEText(body, "plain"))

    # Conexión al servidor SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, email, msg.as_string())
    server.quit()

# Clase que maneja la solicitud POST
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/subscribe':  # Ruta donde recibirás los datos del formulario
            # Procesar los datos del formulario
            ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                email = fields.get('email')[0]  # Obtener el correo electrónico

                # Enviar el correo
                send_coupon(email)

                # Enviar una respuesta al cliente
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f'¡Gracias por suscribirte! Revisa tu correo para obtener tu cupón.')

# Ejecutar el servidor
Handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print(f"Server running on port {PORT}")
httpd.serve_forever()
