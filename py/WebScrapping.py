import http.client

# Conexión HTTP al servidor
conn = http.client.HTTPConnection("https://www.facebook.com/")

# Realizar solicitud GET
conn.request("GET", "/")

# Obtener la respuesta
response = conn.getresponse()
html = response.read().decode()

# Verificar el código de estado HTTP
if response.status == 200:
    print("Página cargada correctamente.")
    # Aquí podrías analizar manualmente el HTML (por ejemplo, buscando cadenas específicas)
    if "<div class='producto'>" in html:
        print("Productos encontrados en la página.")
    else:
        print("No se encontraron productos en la página.")
else:
    print(f"Error al cargar la página: {response.status}")

# Cerrar la conexión
conn.close()

