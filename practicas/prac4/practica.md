# Micromouse

**Descripción**: 
El laberinto es una matriz de 10x10 celdas, cada una identificada por su posición. Cada celda puede tener paredes al norte, sur, este u oeste. Existe al menos una ruta posible desde la celda de inicio hasta la celda objetivo (de salida).

**Agente**: 
El ratón es un agente que puede:
- **Moverse**: una celda a la vez (arriba, abajo, izquierda, derecha), si no hay pared.
- **Percibir**: en cada celda, puede detectar la presencia o ausencia de paredes en las cuatro direcciones.
- **Memorizar**: puede construir un mapa interno del laberinto durante su recorrido.
- **Tomar decisiones**: con base en la información recolectada, el agente decide hacia dónde moverse.

**Objetivo**: 
Llegar desde el inicio hasta la meta en el menor número de movimientos posibles.

**Condiciones**: 
Se tienen dos intentos, uno para memorizar el mapa y otro para probar la ruta encontrada.