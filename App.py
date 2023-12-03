from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Configuración de la cadena de conexión a SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-O05DAMB;DATABASE=dbUrpi;UID=sa;PWD=VG2023'

# Función para insertar los datos en la base de datos
def insertar_cancion(names, artist, gender, archive):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = "INSERT INTO Audio (names, artist, gender, archive) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (names, artist, gender, archive))
    conn.commit()
    cursor.close()
    conn.close()

# Verificar la conexión a la base de datos
def verificar_conexion():
    try:
        conn = pyodbc.connect(connection_string)
        conn.close()
        print("Conexión a la base de datos establecida correctamente.")
    except pyodbc.Error as e:
        print("Error al establecer la conexión a la base de datos:", str(e))

#importante
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        names = request.form['frmNames']
        artist = request.form['frmArtist']
        gender = request.form['frmGender']
        archive = request.files['frmAudio'].filename
        insertar_cancion(names, artist, gender, archive)
        return 'Canción insertada en la base de datos'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    verificar_conexion()  # Verificar la conexión antes de ejecutar la aplicación Flask
    app.run(port=3000, debug=True)