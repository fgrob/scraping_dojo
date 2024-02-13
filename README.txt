

░██████╗░█████╗░██████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░  ██████╗░░█████╗░░░░░░██╗░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░  ██╔══██╗██╔══██╗░░░░░██║██╔══██╗
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝██║██╔██╗██║██║░░██╗░  ██║░░██║██║░░██║░░░░░██║██║░░██║
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██║██║╚████║██║░░╚██╗  ██║░░██║██║░░██║██╗░░██║██║░░██║
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░██║██║░╚███║╚██████╔╝  ██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░░╚════╝░░╚════╝░░╚════╝░

Aplicación de scraping creada como proyecto para certificación en Python.
Esta aplicación lo que hace es tomar algún link que le pases, y revisar cada x cantidad de tiempo si la página tiene cambios. En caso de que hayan cambios, la aplicación sacará un pantallazo de la página y avisará por correo.

Configuración de Correo:

Configuración de Celery:

1. Instalar todos los paquetes contenidos en 'requerimientos.txt' en un nuevo ambiente virtual.
2. Instalar el entorno de lenguaje ERLANG en la carpeta del proyecto. El instalador está en erlang.org.
3. Para el funcionamiento de Celery, se requiere instalar un 'Message Broker', en este caso RABBITMQ
Instalar con el installer desde su pagina oficial, en la carpeta del proyecto.

4. Abrir dos terminales (y activar el ambiente en cada una). Situarse en la carpeta raiz del proyecto.
En una activa el 'worker' de celery (administrador de eventos) con el siguiente codigo:
celery -A scraping_dojo worker -l info -P gevent 

En la otra terminal, activa celery beat, que se encarga de mandar las tareas al broker cada x segundos
celery -A scraping_dojo beat --loglevel=info

Listo!!

Notas: Scraping Dojo está configurado para usar Chrome a la hora de tomar Screenshots. En caso de que uses otro navegador, es necesario descargar el WebDriver correspondiente:

selenium.dev/documentation/webdriver/getting_started/install_drivers/

Guarda el exe en la carpeta webdriver que está dentro de la carpeta recurrencia_app, y modifica la siguiente linea en el archivo task.py (recurrencia_app):

driver = webdriver.Chrome('recurrencia_app/webdriver/chromedriver.exe') #acá habría que poner el webdriver y su path

*Si tienes problemas con Chrome, chequea que versión tienes y descarga el webdriver acorde a su versión


Configurar recurrencia:
Para editar el tiempo en que buscara cambios, ir a carpeta Scraping_dojo (mismo nivel que el settings.py), abrir celery.py y editar:
'schedule': timedelta(seconds=10),

Configuración envío de correos
Cada usuario que utilice esta aplicación recibirá un correo de respuesta que indica que en el sitio web que ha consultado se han realizado cambios.

1.Debes editar la configuración del servidor del correo electrónico en el settings.py del proyecto, agregando la siguiente información
EMAIL_HOST= 'smtp.email.com' #dependiendo del correo que elijas
EMAIL_PORT = 587 #En este caso es el estandar de Gmail
EMAIL_USE_TLS = True 
DEFAULT_FROM_EMAIL = 'correo@email.com' #Dirección de correo que has decidido agregar al proyecto
SERVER_EMAIL = 'root@localhost' #Estandar para Gmail
EMAIL_HOST_USER ="correo@email.com" #Esta dirección de correo electrónica, será la dirección que emite cada correo del proyecto
EMAIL_HOST_PASSWORD = "xxxx-xxxx-xxxx" #Para ejecutar este proyecto desde django, debes activar la contraseña para aplicaciones de Gmail que puedes encontrar en https://support.google.com/accounts/answer/185833?hl=es-419



