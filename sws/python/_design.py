#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import func

print("Content-Type: text/html\n")

func.menu()

print("""
			</header>
		</body>
	</html>
	"""
	)
