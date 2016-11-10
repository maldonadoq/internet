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
codigo = form.getfirst('codigo', 'empty')
nombre = form.getfirst('nombre', 'empty')
ruc = form.getfirst('ruc', 'empty')
email = form.getfirst('email', 'empty')
direccion = form.getfirst('direccion', 'empty')
telefono = form.getfirst('telefono', 'empty')
celular = form.getfirst('celular', 'empty')


if(usuario !='empty' and password != 'empty' and codigo!='empty' and nombre!='empty' and ruc!='empty' and email!='empty' and direccion!='empty' and telefono!='empty' and celular!='empty'):
	insertar = db.cursor()
	insertar.execute("insert into inmobiliarias values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (usuario,password,codigo,nombre,ruc,email,direccion,telefono,celular))
	db.commit()
	print ("ID de ultimo registro insertado: %s<br>" % insertar.lastrowid)
	insertar.close()

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
                <li><a href="_admin.py">Administrador</a></li>
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

men = ["Registrar una Inmobiliaria","Multimedias","Enlaces","Paginas","Comentarios","Ventas","Alquiler","Apariencia","Usuarios","Herramientas","Ajustes"];
func.printls(men)

print("""
        </div>
        <div class="articles">
	        <form action="for_reg.py" method="post" name="miform">
				<input type="text" placeholder="Usuario" name="usuario"/><br>
				<input type="text" placeholder="Password" name="password"/><br>
				<input type="text" placeholder="Codigo" name="codigo"/><br>
				<input type="text" placeholder="Nombre" name="nombre"/><br>
				<input type="text" placeholder="Ruc" name="ruc"/><br>
				<input type="text" placeholder="Email" name="email"/><br>
				<input type="text" placeholder="Direccion" name="direccion"/><br>
				<input type="text" placeholder="Telefeono" name="telefono"/><br>
				<input type="text" placeholder="Celular" name="celular"/><br>
				<input type="submit" name="value" value="Registrar" id="but">
			</form>
		</div>
    </section>
    <footer>
    	<p> Maldonado-Cutipa-Ttito - sws.com</p>
    </footer>

	</body>
</html>
""")