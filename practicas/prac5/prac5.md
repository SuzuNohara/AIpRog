# 8-Puzzle

## Descripción
El tablero es una cuadrícula de 3x3 celdas que contiene ocho piezas móviles numeradas del 1 al 8 y una celda vacía. Las piezas pueden deslizarse hacia la celda vacía si están adyacentes a ella (arriba, abajo, izquierda o derecha). El objetivo es reordenar las piezas desde una configuración inicial aleatoria hasta alcanzar una disposición final ordenada (del 1 al 8), con la celda vacía ubicada en la esquina inferior derecha.

## Agente
El jugador (o agente) puede:
- **Mover piezas**: deslizar una ficha adyacente hacia la celda vacía.
- **Percibir**: observar la posición actual de cada pieza y la ubicación de la celda vacía.
- **Memorizar**: registrar mental o programáticamente los movimientos realizados y los estados visitados.
- **Tomar decisiones**: decidir qué movimiento realizar en función del estado actual del tablero y el objetivo.

## Objetivo
Reorganizar las piezas desde el estado inicial hasta la configuración ordenada en el menor número de movimientos posibles.

## Condiciones
Se tienen dos intentos:
1. Uno para memorizar el mapa.
2. Otro para probar la ruta encontrada.