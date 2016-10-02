def menu():
	print("""
		<!DOCTYPE HTML>
		<html lang="es">
			<head>
				<meta charset="utf-8">
				<script type="text/javascript" src="../js/load.js"></script>
				<link rel="stylesheet" href="../css/style.css">
				<link rel="shortcut icon" type="image/x-icon" href="../sws/icono.png">
				<title>Alquiler y Venta de Inmuebles</title>
			</head>
			<body>
				<header>
					<nav>
	""")

	me = ["SWS","Inmuebles","Venta","Alquiler","Servicios","Blog","Registrate","Ingresar"];
	print ("<ul>")
	for i in range(0,len(me)):
		print ("<li><a>"+str(me[i])+"</a></li>")
	print ("<ul>")