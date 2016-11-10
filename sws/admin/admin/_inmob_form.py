#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import func
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='sws')

form = cgi.FieldStorage() # se instancia solo una vez
usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')

print("""
	<html>
	<head>		
        <meta charset="utf-8">
        <script type="text/javascript" src="../js/load.js"></script>
        <link rel="stylesheet" href="../css/style_ad.css">
        <link rel="shortcut icon" type="image/x-icon" href="../../sws/icono.png">
        <title>Panel de Administrador</title>
	</head>
	<body>
    <header>
        <nav>
			<ul>
                <li><a href="_inmob.py">Inmobiliaria</a></li>
                <li><a>Panel de Control</a></li>
                <li><a>Archivos</a></li>
                <li><a href="../../python/_main.py">Cerrar Sesion</a></li>
            </ul>
        </nav>
    </header>
    <section class="main">
        <div id = "barra">
            <p>Escritorio</p>
""")

men = ["Registrar un Inmueble","Multimedias","Enlaces","Paginas","Comentarios","Ventas","Alquiler","Apariencia","Usuarios","Herramientas","Ajustes"];
func.printls(men)

print("""
        </div>
        <div class="articles">
		</div>
    </section>
    <footer>
    	<p> Maldonado-Cutipa-Ttito - sws.com</p>
    </footer>

	</body>
</html>
""")