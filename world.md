# Ghost grid

## Mundo

El mundo es un sistema de nodos interconectados entre si, cada nodo tiene una lista de conexiones a otros nodos, las cuales tendran un valor, el cual sera interpretado como una distancia entre nodos, cada nodo tendra un id de la capa en la que se encuentra, las cuales van desde la 0 hasta la n, estas capas se ordenan de izquierda a derecha, las conexiones entre nodos pueden subir de 0 hasta 3 capas, estas conexiones son bidireccionales. 

La distancia entre nodos sera de 1 a 10, donde de 1 a 5 se considera una distancia corta, y de 6 a 10 es una distancia larga. Para el caso de una distancia corta, esta permitira a los agentes ver que hay del otro lado del nodo.

El mundo tendra un botin total de 100, que representa el porcentaje del botin total, este botin puede ser dividido en partes enteras

## Agentes

El agente ladron "ghost" que tratara de llevarse el botin desde el nodo 0, hasta el nodo n

El agente policial "sentinel" que tratara de recuperar el botin, asi como atrapar a todos los ladrones. 

## Condiciones iniciales

Enerigia base: Cantidad de energia equivalente a la distancia minima entre cualquier nodo de la capa 0 hasta cualquier nodo de la capa n

El agente "ghost" iniciara con 100 de botin en cualquier nodo de la capa 0 y con dos unidades de energia base. El agente "ghost" podra auto replicarse, pero esto dividira el botin final en la candiad de replicas.

El agente "sentinel" iniciara con 0 de botin en cualquier nodo de la capa n - 1 y con tres unidades de energia base. El agente "sentinel" siempre tendra tres veces la cantidad de agentes que "ghost"

## Percepciones

Todos los agenes pueden ver todos los nodos que se conectan al nodo en el cual se encuentran, para el caso de los nodos, la percepcion de los nodos permite al agente saber a que capa pertenece el nodo de destino, tambien podran saber la distancia que hay.

### Percepciones de ghost

Ghost no podra saber en donde se encuentran sus replicas, salvo que estas se encuentren en el mismo nodo.

Ghost podra saber si alguna de sus replicas ha dejado parte del botin en el nodo en el que se encuentra actualmente o en alguno de los nodos que puede alcanzar desde su nodo actual.

### Percepciones de sentinel

Sentinel podra saber en todo momento donde se encuentran los demas sentinels

Sentinel podra darse cuenta si en el nodo en el que se encuentra hay parte del botin.

Sentinel no podra ver si hay botin guardado en los nodos conectados a su nodo actual.

## Acciones

Ghost podra moverse de un nodo a otro, lo cual lo hara perder la energia equivalente al valor del camino tomado

Ghost podra dejar una fraccion o la totalidad del botin que lleva encima en el nodo en el que se encuentre actualmente

Ghost podra tomar parte o la totalidad del botin que se encuentre en el nodo en el que se encuentre actualmente

Sentinel podra viajar entre los nodos que tenga disponibles, lo cual lo hara perder la energia equivalente al valor del camino tomado.

Sentinel puede volver a la capa n - 1 para poder recargar su energia

Sentinel puede tomar el botin del nodo en el que se encuentre actualmente, pero hecho esto, no podra moverse de ese nodo en lo que resta de la persecucion

## Reacciones

Si un ghost y un sentinel se encuentran en el mismo nodo, sentinel podra atrapar a ghost si este tiene botin encima, si este botin supera el 50, el sentinel se convertira en un ghost y los 50 de botin se perderan por completo

Si un ghost y un sentinel se encuentran en el mismo nodo, y el ghost no lleva botin encima, sentinel no podra aprehender al ghost

La recompenza de sentinel sera mayor mientras mas parte del botin recupere, pero se multiplicara por la cantidad de ghosts que atrape

La recompenza de ghost sera mayor mientras mas parte del botin logre llevar a la capa n, pero se dividira mientras mas ghost haya requerido para la labor