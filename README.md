# Josephus Problem
Tiene un origen histórico:
Se cuenta que los soldados judíos, cuando eran acorralados por el soldados romanos, diseñaron un mecanismo para matarse entre ellos, evitando el suicidio, para no ser capturados. La idea es la siguiente:

Se forman en un círculo y el primero mata al de su izquierda y el siguiente vivo mata también al de su izquierda, así hasta quedar uno solo, quien debía suicidarse para no ser capturado.

La historia dice que Josephus prefería ser capturado que morir. ¿En qué posición del círculo debe ubicarse para no morir, suponiendo que la posición número uno comienza mantando?

## Code
La función `josephus_winner(n)` recibe un numero natural, correspondiente a la cantidad de soldados en el círculo, y retorna la posición que sobrevive.
