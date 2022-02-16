

░██████╗░█████╗░██████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░  ██████╗░░█████╗░░░░░░██╗░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░  ██╔══██╗██╔══██╗░░░░░██║██╔══██╗
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝██║██╔██╗██║██║░░██╗░  ██║░░██║██║░░██║░░░░░██║██║░░██║
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██║██║╚████║██║░░╚██╗  ██║░░██║██║░░██║██╗░░██║██║░░██║
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░██║██║░╚███║╚██████╔╝  ██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░░╚════╝░░╚════╝░░╚════╝░



1. Instalar todos los paquetes contenidos en 'requerimientos.txt' en un nuevo ambiente virtual
2. Instalar el entorno de lenguaje ERLANG. El instalador está en erlang.org
3. Para el funcionamiento de Celery, se requiere instalar un 'Message Broker', en este caso RABBITMQ 
Instalar con el installer desde su pagina oficial (rabbitmq.com)

4. Abrir dos consolas, en una activaremos el 'worker' de celery (administrador de eventos) con el siguiente codigo:
celery -A scraping_dojo worker -l info -P gevent 

En la otra consola, activaremos celery beat, que se encarga de mandar las tareas al broker cada x segundos
celery -A scraping_dojo beat --loglevel=info

listo!

*Si estás scrapeando una pagina en el localhost, abrir una tercera terminal y runserver