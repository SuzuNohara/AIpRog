# Agentes

## funciones
## sensores
## actuadores

# Agentes reactivos simples

Los agentes reactivos simples son un tipo de agente en inteligencia artificial que selecciona sus acciones basándose únicamente en sus percepciones actuales, sin tener en cuenta las percepciones históricas. Este tipo de agente sigue una lógica de "si-entonces" para tomar decisiones rápidas y directas.

## Funcionamiento de los Agentes Reactivos Simples
- Percepción: El agente percibe su entorno a través de sensores. Estas percepciones proporcionan información sobre el estado actual del entorno.

- Reglas de Condición-Acción: El agente tiene un conjunto de reglas predefinidas que relacionan condiciones específicas con acciones. Estas reglas son del tipo "si-entonces" (por ejemplo, "si hay un obstáculo enfrente, entonces gira a la derecha").

- Acción: Basado en las percepciones actuales y las reglas de condición-acción, el agente selecciona y ejecuta una acción. No se considera el historial de percepciones anteriores.

## Ventajas
- Simplicidad: Son fáciles de diseñar e implementar debido a su estructura simple.
- Rapidez: Pueden tomar decisiones rápidamente ya que no necesitan procesar información histórica.
## Desventajas
- Limitación en Entornos Complejos: No son adecuados para entornos donde las decisiones dependen de una secuencia de eventos o de un contexto histórico.
- Falta de Adaptabilidad: No pueden aprender de experiencias pasadas ni adaptarse a cambios en el entorno que no estén contemplados en las reglas predefinidas.

# Agente basado en objetivos

Los agentes basados en objetivos son un tipo de agente en inteligencia artificial que selecciona sus acciones no solo basándose en sus percepciones actuales, sino también en un conjunto de objetivos que desea alcanzar. Este tipo de agente evalúa diferentes acciones posibles y elige la que mejor le permita alcanzar sus objetivos.

## Funcionamiento de los Agentes Basados en Objetivos

1. **Percepción**: El agente percibe su entorno a través de sensores. Estas percepciones proporcionan información sobre el estado actual del entorno.

2. **Objetivos**: El agente tiene un conjunto de objetivos que desea alcanzar. Estos objetivos guían el comportamiento del agente y le permiten evaluar la efectividad de diferentes acciones.

3. **Evaluación de Acciones**: El agente evalúa las posibles acciones que puede tomar en función de cómo contribuyen al logro de sus objetivos. Esta evaluación puede implicar la consideración de múltiples pasos y la planificación a futuro.

4. **Selección de Acción**: Basado en la evaluación de las acciones, el agente selecciona y ejecuta la acción que considera más efectiva para alcanzar sus objetivos.

## Ventajas

- **Flexibilidad**: Pueden adaptarse a diferentes situaciones y entornos cambiantes, ya que sus decisiones están guiadas por objetivos y no solo por reglas predefinidas.
- **Capacidad de Planificación**: Pueden planificar a largo plazo y considerar múltiples pasos para alcanzar sus objetivos.

## Desventajas

- **Complejidad**: Son más complejos de diseñar e implementar debido a la necesidad de evaluar y planificar acciones en función de objetivos.
- **Requiere Más Recursos**: La evaluación y planificación de acciones pueden requerir más recursos computacionales y tiempo de procesamiento.

# Agentes basados en utilidad

Los agentes basados en utilidad son un tipo de agente en inteligencia artificial que selecciona sus acciones no solo basándose en sus percepciones actuales y objetivos, sino también en una función de utilidad que evalúa la "bondad" de las posibles acciones. Este tipo de agente busca maximizar su utilidad, es decir, seleccionar la acción que le proporcione el mayor beneficio o satisfacción.

## Funcionamiento de los Agentes Basados en Utilidad

1. **Percepción**: El agente percibe su entorno a través de sensores. Estas percepciones proporcionan información sobre el estado actual del entorno.

2. **Objetivos**: El agente tiene un conjunto de objetivos que desea alcanzar. Estos objetivos guían el comportamiento del agente.

3. **Función de Utilidad**: El agente utiliza una función de utilidad para evaluar las posibles acciones. Esta función asigna un valor numérico a cada acción en función de su "bondad" o utilidad.

4. **Evaluación de Acciones**: El agente evalúa las posibles acciones utilizando la función de utilidad. Esta evaluación puede implicar la consideración de múltiples pasos y la planificación a futuro.

5. **Selección de Acción**: Basado en la evaluación de las acciones, el agente selecciona y ejecuta la acción que maximiza su utilidad.

## Ventajas

- **Optimización**: Pueden seleccionar la mejor acción posible en función de una evaluación cuantitativa de la utilidad.
- **Flexibilidad**: Pueden adaptarse a diferentes situaciones y entornos cambiantes, ya que sus decisiones están guiadas por una función de utilidad.

## Desventajas

- **Complejidad**: Son más complejos de diseñar e implementar debido a la necesidad de definir y calcular una función de utilidad.
- **Requiere Más Recursos**: La evaluación y planificación de acciones pueden requerir más recursos computacionales y tiempo de procesamiento.

## Ejemplo

Un ejemplo de un agente basado en utilidad es un sistema de recomendación de productos en una tienda en línea. Sus objetivos podrían ser:

- Maximizar la satisfacción del cliente.
- Aumentar las ventas.
- Minimizar los costos de envío.

El sistema evaluaría diferentes recomendaciones de productos utilizando una función de utilidad que considere factores como la probabilidad de compra, la satisfacción del cliente y los costos de envío. Seleccionaría la recomendación que maximice la utilidad total.

## Funcionamiento de los Agentes Basados en Utilidad

1. **Percepción**: El agente percibe su entorno a través de sensores. Estas percepciones proporcionan información sobre el estado actual del entorno.

2. **Objetivos**: El agente tiene un conjunto de objetivos que desea alcanzar. Estos objetivos guían el comportamiento del agente.

3. **Función de Utilidad**: El agente utiliza una función de utilidad para evaluar las posibles acciones. Esta función asigna un valor numérico a cada acción en función de su "bondad" o utilidad.

4. **Evaluación de Acciones**: El agente evalúa las posibles acciones utilizando la función de utilidad. Esta evaluación puede implicar la consideración de múltiples pasos y la planificación a futuro.

5. **Selección de Acción**: Basado en la evaluación de las acciones, el agente selecciona y ejecuta la acción que maximiza su utilidad.

## Ventajas

- **Optimización**: Pueden seleccionar la mejor acción posible en función de una evaluación cuantitativa de la utilidad.
- **Flexibilidad**: Pueden adaptarse a diferentes situaciones y entornos cambiantes, ya que sus decisiones están guiadas por una función de utilidad.

## Desventajas

- **Complejidad**: Son más complejos de diseñar e implementar debido a la necesidad de definir y calcular una función de utilidad.
- **Requiere Más Recursos**: La evaluación y planificación de acciones pueden requerir más recursos computacionales y tiempo de procesamiento.

## Ejemplo

Un ejemplo de un agente basado en utilidad es un sistema de recomendación de productos en una tienda en línea. Sus objetivos podrían ser:

- Maximizar la satisfacción del cliente.
- Aumentar las ventas.
- Minimizar los costos de envío.

El sistema evaluaría diferentes recomendaciones de productos utilizando una función de utilidad que considere factores como la probabilidad de compra, la satisfacción del cliente y los costos de envío. Seleccionaría la recomendación que maximice la utilidad total.