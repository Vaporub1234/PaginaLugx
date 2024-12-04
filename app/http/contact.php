<?php
// Verificamos si el formulario ha sido enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Datos recibidos del formulario
    $name = "prueba";
    $email = $_POST['email'];
    echo $email;
    $subject = "suscripcion exitosa";
    $message = "Gracias por suscribirse";

    // Correo de destino (tu correo electrónico)
    $receiving_email_address = 'leomya1906@gmail.com';

    // Configuración de Gmail SMTP
    $smtp_host = 'smtp.gmail.com';
    $smtp_user = 'leomya1906@gmail.com';
    $smtp_password = 'xybj zqez bfmh ymgs';
    $smtp_port = 587; // O 465 si usas SSL

    // Asunto y cuerpo del mensaje
    $mail_subject = $subject;
    $mail_body = "
        Nombre: $name\n
        Correo: $email\n
        Mensaje: $message
    ";

    // Cabeceras
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Intentamos enviar el correo usando la función mail() de PHP
    if (mail($receiving_email_address, $mail_subject, $mail_body, $headers)) {
        echo "Correo enviado correctamente.";
    } else {
        echo "Error al enviar el correo.";
    }
}
?>
