## Objetivo: 
Diseñar e implementar una política de limpieza para una aspiradora inteligente que opere en un mundo bidimensional (una cuadrícula), tomando en cuenta:
### Obstáculos
- Distribución aleatoria de suciedad (normal y muy sucia)
- Restricciones de batería
- Múltiples puntos de interés (por ejemplo, celdas muy sucias)
- Métricas de rendimiento enfocadas en número de acciones, eficiencia energética y tiempo total de limpieza

Esta práctica busca que el agente tome decisiones óptimas para maximizar la eficiencia de limpieza y minimizar acciones innecesarias.

### Descripción:
#### Dimensiones: 
El mundo se representa como una cuadrícula de tamaño M x N (por ejemplo, 5×5 o 10×10, según se requiera). Cada celda puede tener uno de los siguientes estados: Limpia, Sucia (requiere 1 acción de limpieza), Muy sucia (requiere 2 acciones de limpieza) y Obstáculo (celda intransitable).
#### Distribución inicial: 
Se genera aleatoriamente la ubicación de un número determinado de celdas sucias y muy sucias. Se colocan obstáculos de forma aleatoria (con una densidad que el usuario pueda configurar). Se debe garantizar que haya al menos una celda libre para colocar a la aspiradora. 
#### Posición Inicial de la Aspiradora: 
Colocada en una celda libre (no obstáculo) al inicio de la simulación. La celda inicial también se considera la estación de carga.

### Acciones disponibles: 
- limpiar(): Limpia la celda actual. Si la celda está "muy sucia", se requiere ejecutar esta acción dos veces para dejarla completamente limpia.
- mover(dirección): El agente puede moverse hacia arriba, abajo, izquierda o derecha (siempre que no sea obstáculo y esté dentro de los límites de la cuadrícula).
- cargar(): Si la batería se agota, el agente debe regresar a la celda de inicio para recargarse.
- mover_cargador(): Se puede mover el punto de carga, cada celda movida, se considera un desgaste de dos acciones.
#### Restricción de Batería: 
La aspiradora tiene un máximo de 20 acciones (o un número configurable) antes de requerir recarga. Una acción puede ser un movimiento o una acción de limpieza. Para recargar la batería, el agente debe ir a la posición inicial y ejecutar la acción de carga.
### Métrica de Evaluación: 
- Total de acciones ejecutadas, movimientos, limpiezas y recargas
- Eficiencia energética, cantidad de celdas limpiadas por ciclo de batería;
- Tiempo total hasta la limpieza completa (o número de pasos total de simulación).

Se pueden incorporar métricas como la distancia total recorrida o el tiempo que pasa entre recargas.
Condición de Terminación: La simulación concluye cuando todas las celdas alcanzables (no bloqueadas por obstáculos) están limpias.
