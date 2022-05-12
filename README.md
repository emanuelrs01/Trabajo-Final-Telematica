# Trabajo-Final-Telematica
_Aqui estaran todos los pasos y comandos necesarios para el ~PROYECTO FINAL~_

Para dar inicio a la practica deberas clonar el _Repositorio_ con el siguiente comando: $ git clone
https://github.com/emanuelrs01/Trabajo-Final-Telematica.git

Paso1: Para inicar el _Contenedor_ se ejecuta el siguiente comando: sudo docker build -t trabajofinal:01 .

Paso2: Para ejecutar el _Servicio_ se usa el siguiente comando: sudo docker run -it -p 80:80 trabajofinal:01 python3 app.py

NOTA: _El parametro -it es utilizado para ver de forma interactiva el proceso y asi interactuar con la maquina por comandos, tambien puede ser cambiado por el parametro -d para que para que se inicie por memoria ram, es decir por background_
