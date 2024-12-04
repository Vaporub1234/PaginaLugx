from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Ruta para la página de suscripción
@app.route("/", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        email = request.form["email"]
        send_coupon(email)  # Enviar el cupón al correo ingresado
        return "¡Gracias por suscribirte! Revisa tu correo para obtener tu cupón."
    return render_template("index.html")

# Función para enviar el cupón por correo
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

if __name__ == "__main__":
    app.run(debug=True)
