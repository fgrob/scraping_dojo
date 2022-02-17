

░██████╗░█████╗░██████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░  ██████╗░░█████╗░░░░░░██╗░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░  ██╔══██╗██╔══██╗░░░░░██║██╔══██╗
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝██║██╔██╗██║██║░░██╗░  ██║░░██║██║░░██║░░░░░██║██║░░██║
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██║██║╚████║██║░░╚██╗  ██║░░██║██║░░██║██╗░░██║██║░░██║
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░██║██║░╚███║╚██████╔╝  ██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░░╚════╝░░╚════╝░░╚════╝░



1. Instalar todos los paquetes contenidos en 'requerimientos.txt' en un nuevo ambiente virtual
2. Instalar el entorno de lenguaje ERLANG. El instalador está en erlang.org
3. Para el funcionamiento de Celery, se requiere instalar un 'Message Broker', en este caso RABBITMQ 
Instalar con el installer desde su pagina oficial.

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
