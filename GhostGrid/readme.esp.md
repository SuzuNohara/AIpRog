# Ghost Grid - Definición del Sistema

## 1. Mundo

El mundo es una **red de nodos interconectados** organizada en capas numeradas desde **0 hasta n**, representando distintos niveles de seguridad o distancia en el entorno.

### 1.1 Estructura del Mundo

- Cada **nodo** tiene una lista de **conexiones** a otros nodos, con valores de **distancia** entre **1 y 10**.
  - **Distancia corta (1 a 5):** Ghost puede ver qué hay en el nodo de destino.
  - **Distancia larga (6 a 10):** Ghost no puede ver qué hay en el nodo de destino.
- Las **conexiones entre nodos son bidireccionales**.
- Un nodo pertenece a una **capa específica (0 a n)** y las conexiones pueden subir hasta **3 capas**.
- El botín total del juego es **100 unidades** y puede dividirse en fracciones enteras.
- No puede haber conexiones entre nodos de la capa **0** a la capa **n**.

### 1.2 Condiciones Iniciales

- **Ghost:**
  - Aparece en un nodo aleatorio de la capa **0**.
  - Comienza con **100 de botín total**, dividido entre los Ghosts al inicio del juego.
  - Tiene una energía base equivalente a la **distancia promedio de los caminos más cortos entre la capa 0 y la capa n**.
  - Puede **replicarse solo en el primer turno**, dividiendo el botín entre sus copias.
- **Sentinel:**
  - Aparece en un nodo aleatorio de la capa **n - 1**.
  - No tiene botín inicial.
  - Su cantidad siempre es **tres veces el número de Ghosts**.
  - Tiene **tres veces la energía base de Ghost**.
  - Puede recargar energía si **se encuentra en el mismo nodo con otro Sentinel**, recuperando **5% de energía por turno**.

---

## 2. Percepciones

Cada agente tiene diferentes capacidades de percepción sobre el entorno.

### 2.1 Percepciones Generales (Todos los agentes)

- Pueden ver los **nodos conectados** desde su posición actual.
- Pueden ver la **capa** del nodo destino.
- Pueden conocer la **distancia** del camino entre nodos conectados.

### 2.2 Percepciones de Ghost

- **Conocimiento de Réplicas:** No sabe dónde están sus réplicas a menos que estén en el mismo nodo.
- **Visibilidad del Botín:**
  - Puede ver si **hay botín en su nodo actual**.
  - Puede ver si **hay botín en los nodos accesibles con una distancia corta (1-5)**.
  - **Recuerda** en qué nodos dejó botín.
  - Puede compartir esta información **solo cuando dos Ghosts se encuentran en el mismo nodo** (reunión estratégica).

### 2.3 Percepciones de Sentinel

- **Posición Aliada:** Puede ver dónde están los demás Sentinels en todo momento.
- **Detección de Botín:** Puede detectar si hay botín en el nodo en el que se encuentra.
- **Patrullaje Estructurado:** Puede marcar nodos como "revisados" para optimizar su búsqueda.
- **Detección de Ghosts:**
  - Si un Sentinel entra en un nodo donde hay un Ghost **con botín**, puede capturarlo inmediatamente.
  - Si el Ghost **no tiene botín**, el Sentinel sabe que hay un Ghost en el nodo pero **no puede aprehenderlo**.

---

## 3. Funciones y Acciones

Cada agente tiene un conjunto de acciones disponibles.

### 3.1 Acciones de Ghost

- **Movimiento:** Puede trasladarse a un nodo conectado, gastando energía **equivalente** a la distancia.
- **Depositar botín:** Puede dejar una fracción o la totalidad del botín en el nodo actual.
- **Tomar botín:** Puede recoger botín del nodo en el que se encuentra.
- **Replicarse:** Puede crear una copia de sí mismo **solo en el primer turno**, dividiendo el botín entre los Ghosts activos al inicio del juego.

### 3.2 Acciones de Sentinel

- **Movimiento:** Puede trasladarse a un nodo conectado, gastando energía **equivalente** a la distancia.
- **Recargar energía:** Si hay **dos o más Sentinels en el mismo nodo**, cada uno recupera **5% de energía por turno**.
- **Captura de Ghosts:** Si entra en un nodo donde hay un Ghost **con botín**, lo atrapa inmediatamente.
- **Recuperación de Botín:** Puede tomar el botín de un nodo, pero después de hacerlo, **no puede moverse durante el resto de la persecución**.
- **Patrullaje Estructurado:** Puede marcar nodos como revisados para optimizar la búsqueda de Ghosts.
- **Barrera de escape:** Sentinel no puede entrar en la capa \*\*n\*\*&#x20;

---

## 4. Interacciones y Reacciones

### 4.1 Encuentros entre Ghost y Sentinel

- Si un Sentinel entra en un nodo donde hay un Ghost **con botín**, lo atrapa inmediatamente.
  - Si el botín atrapado supera **50**, el Sentinel se convierte en un Ghost y esos **50 de botín se pierden**.
- Si un Sentinel entra en un nodo donde hay un Ghost **sin botín**, no puede atraparlo.
  - Sin embargo, **sabe que un Ghost está ahí**.
  - Si el Ghost no tiene energía para moverse, **queda atrapado en el nodo**.

### 4.2 Distribución de Recompensas

- **Ghost:** La recompensa aumenta mientras más botín logre llevar hasta la capa **n**, pero se divide entre los Ghosts **al inicio del juego**.
- **Sentinel:** La recompensa aumenta con la cantidad de botín recuperado y **se multiplica** por la cantidad de Ghosts atrapados.

---

## 5. Condiciones de Victoria y Derrota

El juego finaliza en los siguientes escenarios:

1. **Tiempo límite alcanzado:** **5n turnos** (donde **n** es la cantidad de capas de nodos).
2. **Botín completamente distribuido:** Cuando los **100 de botín están repartidos** entre:
   - Ghosts que lograron llevar botín a la capa **n**.
   - Sentinels que recuperaron botín capturado.

### 5.1 Criterios de Victoria

- **Victoria de Ghost:** Si al menos **uno** logra llevar botín hasta la capa **n**.
- **Victoria de Sentinel:** Si los Sentinels logran **capturar a todos los Ghosts** o recuperar la **mayoría del botín**.
- **Empate:** Si la cantidad de botín recuperado por Sentinels y el botín transportado por Ghosts es **cercana al 50%-50%**.

