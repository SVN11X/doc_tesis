# Guion de la defensa v3 · Navegación y exploración autónoma de interiores

Va con `slides-v3.pptx`: 32 láminas visibles y 13 ocultas (un índice y 12 respaldos, de la 33 a la 45). El mismo texto está en las notas del orador de cada lámina, para leerlo en la vista del moderador.

Cada `[CLIC]` hace aparecer la parte siguiente de la lámina. El número de clics de cada lámina coincide con sus animaciones. El video de la lámina 2 parte solo al entrar. Las seis portadas azules no tienen clics: el ícono del tema viaja solo, con la transición Morph, hasta la cabecera de la lámina siguiente.

Duración estimada de la narración: 25 min 04 s a 130 palabras por minuto (3271 palabras). Con pausas naturales queda entre 24 y 26 minutos, bajo el límite de 30.

Para ensayar con audio: `python generar_audio_guion.py` en esta carpeta crea los MP3 en `audio_guion/`.

## Apertura

Lámina 1 · Portada (25 s)

Buenas tardes, profesores. Muchas gracias por su tiempo. Mi nombre es Sebastián Valderas Neculqueo y presento mi trabajo de titulación de Ingeniería Civil Electrónica: Navegación y exploración autónoma de interiores utilizando un robot móvil de tracción diferencial, guiado por el profesor Patricio Galarce Acevedo. Antes de entrar en detalles, quiero mostrarles qué hace este robot.

Lámina 2 · Video de demostración (65 s)

[El video parte solo al entrar a la lámina. Narrar con calma.] Lo que ven es un ensayo real en el recinto de pruebas. A la izquierda está el robot que diseñé y construí, moviéndose sin control remoto. A la derecha está lo que el computador interpreta en ese momento. Fíjense en tres cosas. [CLIC] Primero, a medida que avanza, el láser de arriba detecta los muros y el mapa crece en pantalla. El borde morado y celeste es un margen de seguridad que el robot respeta junto a los muros. [CLIC] Segundo, la línea verde es la ruta que el robot calcula solo hacia las zonas grises, que todavía no conoce. Tercero, fíjense en la navegación y recuperación autónoma en pasillos estrechos de 58 cm, sin atascos ni intervención humana. Al final, el robot construyó solo el mapa del recinto. Ahora les explico qué problema resuelve, cómo lo construí y qué resultados medí.

Lámina 3 · Estructura (15 s)

La presentación tiene seis partes: el problema que aborda este trabajo, el estado del arte, los objetivos y el alcance, el diseño del sistema, los resultados medidos en el robot real y las conclusiones.

## 01 · Problema

Lámina 4 · Portada 01 · Problema (4 s)

Primero, el problema: para qué sirve y qué hay que resolver.

Lámina 5 · ¿Para qué sirve? (65 s)

Una pregunta legítima al ver un prototipo de laboratorio es para qué sirve en la práctica. [CLIC] Antes de medir, inspeccionar o trasladar algo, una máquina necesita saber dónde está, dibujar el lugar y decidir adónde ir. [CLIC] El caso más cercano para Chile es la minería subterránea, con frentes donde la norma prohíbe entrar a una persona. En El Teniente, Codelco ya usa un dron con láser que mapea solo y hace en cinco minutos una inspección que antes tomaba medio día. [CLIC] En inspección de plantas, robots como Spot o ANYmal recorren instalaciones de Glencore y Vale. [CLIC] Y una aplicación directa de este trabajo es el levantamiento de planos: los mapas que obtuve quedan a 3,4 cm del plano medido con cinta métrica. Todo parte de la misma base: un robot que se ubica, mapea y decide solo. Eso es lo que construí.

Lámina 6 · El mercado ya existe (65 s)

El mercado para esto ya existe, en dos niveles. [CLIC] Arriba están los equipos industriales. Spot, de Boston Dynamics, hace misiones autónomas de inspección y Hovermap mapea en 3D sin GPS en más de treinta minas. En Chile, el robot Arkytas de Kinamics inspecciona frentes en El Teniente, pero lo maneja una persona a distancia. Se venden solo a cotización y su funcionamiento interno no siempre es accesible. [CLIC] En el otro extremo están los robots didácticos, como el TurtleBot 3 Burger, que cuesta 681 dólares sin envío ni impuestos y trae un sensor de giro y motores integrados. [CLIC] Este prototipo se ubica entre ambos: usa piezas separadas, explora solo un recinto desconocido y mide su propio desempeño. No tiene sensor de giro, así que no equivale al Burger. Persigue el mismo objetivo que la industria, con el costo de un kit didáctico.

Lámina 7 · Cuatro subsistemas (70 s)

Lograr que un robot sea autónomo no es resolver una sola pieza. Hay que hacer que cuatro subsistemas trabajen juntos. [CLIC] Primero, la percepción: medir la distancia a los muros con el láser y el giro de cada rueda con los encoders, que son sensores que cuentan las vueltas. [CLIC] Segundo, la localización y el mapeo: que el robot sepa dónde está mientras dibuja el plano. [CLIC] Tercero, el control de las ruedas: que cada rueda gire a la velocidad que se le pide. [CLIC] Y cuarto, la planificación y exploración: decidir adónde ir y cómo llegar con seguridad. Los equipos comerciales traen esto integrado y los proyectos abiertos suelen resolver piezas sueltas. Integrar las cuatro y medirlas en un robot real es el aporte. [CLIC] De ahí nace la pregunta central: ¿es posible construir un robot diferencial que, con componentes accesibles y herramientas de código abierto, mapee, navegue y explore interiores de forma autónoma?

## 02 · Estado del arte

Lámina 8 · Portada 02 · Estado del arte (4 s)

Segundo, cómo se resuelve hoy y cómo se compara este prototipo.

Lámina 9 · Estado del arte (60 s)

Revisé el estado del arte en esos cuatro subsistemas. [CLIC] La tracción diferencial usa dos ruedas con motor y una rueda pivote, y gira sobre su propio eje. Un automóvil no gira en el lugar y un omnidireccional es más complejo. [CLIC] En percepción predomina el LIDAR 2D, un láser que mide en 360 grados. La visión 3D da más datos, pero cuesta más cálculo y dinero. [CLIC] En mapeo, SLAM significa mapear y ubicarse al mismo tiempo. GMapping usa filtros de partículas y los métodos actuales, como SLAM Toolbox, corrigen el mapa al volver a un lugar conocido. [CLIC] En navegación dominan las arquitecturas modulares, como ROS 2 con Nav2, y la exploración por fronteras. [CLIC] La tendencia es clara: más capacidad trae más costo y complejidad. Cada elección de este trabajo busca lo suficiente para un interior plano.

Lámina 10 · Comparativa de valor (50 s)

Ahora comparo el valor, no solo el precio. [CLIC] A la izquierda, los equipos industriales. Al centro, el kit didáctico TurtleBot 3. A la derecha, este prototipo. [CLIC] En apertura, aquí el hardware, el firmware y el software se pueden intervenir completos. [CLIC] En autonomía, este prototipo explora solo: 5 de 6 exploraciones terminaron sin ayuda. [CLIC] En precisión, tiene un dato verificado: 3,4 cm frente al plano real. [CLIC] Y en costo, los materiales suman 444 643 pesos, unos 462 dólares, un 32 por ciento menos que el Burger sin envío ni impuestos. Quiero ser transparente: el Burger trae sensor de giro y motores con controlador integrados. Este prototipo cuesta menos, pero no ofrece exactamente lo mismo.

## 03 · Objetivos

Lámina 11 · Portada 03 · Objetivos (4 s)

Tercero, qué me propuse y hasta dónde llega el trabajo.

Lámina 12 · Objetivos (65 s)

[CLIC] El objetivo general fue diseñar e implementar un robot diferencial de bajo costo, basado en ROS 2, que es el software estándar para robots, capaz de construir un mapa 2D mediante SLAM y de navegar solo hacia destinos que genera una estrategia de exploración de fronteras. [CLIC] Para lograrlo definí cuatro objetivos específicos. El primero, construir el robot y validarlo antes en un gemelo digital en el simulador Gazebo Classic. El segundo, controlar las ruedas: modelo de movimiento, odometría con encoders y control de velocidad en lazo cerrado. [CLIC] El tercero, mapear, ubicarse y navegar con SLAM Toolbox y Nav2. Y el cuarto, explorar sin ayuda, con metas que se generan automáticamente. [CLIC] El alcance son interiores de piso plano, evaluando la navegación sobre las metas del explorador. Quedaron fuera las metas fijas que marca un operador y la ubicación sobre un mapa guardado.

## 04 · Diseño

Lámina 13 · Portada 04 · Diseño (4 s)

Cuarto, cómo lo construí y cómo funciona.

Lámina 14 · Arquitectura (65 s)

Para usar hardware de bajo costo, repartí el trabajo en dos equipos. [CLIC] En el robot va lo que no puede esperar: el láser mide distancias en 360 grados y los encoders cuentan las vueltas de cada rueda. [CLIC] Un Arduino Nano controla la velocidad de cada rueda cada 33 milisegundos con un control PI y frena los motores si pasan dos segundos sin órdenes. [CLIC] Sobre él, una Raspberry Pi 4 conecta todo con ROS 2 y calcula la odometría, es decir, cuánto avanzó el robot según sus ruedas. [CLIC] Ambos equipos se comunican por una red Wi-Fi dedicada. [CLIC] En un computador portátil de gama media va lo que exige más cálculo. SLAM Toolbox dibuja el mapa y ubica al robot. [CLIC] Nav2 traza la ruta y ordena las velocidades. [CLIC] El explorador elige la próxima meta. [CLIC] Y RViz2 lo muestra todo en pantalla.

Lámina 15 · Del diagrama al robot real (70 s)

Este es el robot construido. [CLIC] Arriba va el láser RPLidar A1, con vista libre en 360 grados, y abajo, dos motores de 12 volts con encoder. [CLIC] Dentro van la Raspberry Pi 4 y el Arduino, los mismos bloques del diagrama anterior. [CLIC] A la derecha está su gemelo digital: una copia virtual en el simulador Gazebo Classic, descrita en URDF, el formato estándar para describir las piezas y uniones de un robot. Tiene la misma geometría de ruedas que el real, y con él probé movimiento, sensores y comunicación antes del robot físico. [CLIC] En lo mecánico, el chasis está impreso en 3D en PLA+, a partir de una plataforma abierta de referencia, y se apoya en dos ruedas con motor y una rueda pivote. En lo eléctrico, separé la potencia de 12 volts de los motores del riel regulado de 5 volts que alimenta la electrónica, para evitar interferencias y reinicios.

Lámina 16 · Cinco decisiones de diseño (70 s)

Estas son las cinco decisiones de la plataforma, pensando en bajo costo, compatibilidad y un computador portátil de gama media. [CLIC] Como software base, ROS 2, que organiza el robot en programas independientes y trae navegación completa, en su versión Foxy. [CLIC] Como sensor, un LIDAR 2D: barato y suficiente en piso plano. [CLIC] Para el mapa, SLAM Toolbox, que lo dibuja en vivo, lo corrige al volver a un lugar conocido y lo guarda. [CLIC] Para navegar, Nav2 con dos piezas. A estrella es el planificador global: recorre la grilla del mapa y encuentra la ruta más corta sumando lo ya recorrido y una estimación de lo que falta, y la recalcula rápido cuando el mapa cambia. DWB es el control local: prueba trayectorias cortas y elige la que sigue la ruta lejos de los obstáculos. [CLIC] Por último, Gazebo Classic para simular y la exploración por fronteras, que elige metas mirando solo el mapa.

Lámina 17 · Por qué un PI incremental (80 s)

Un punto central para nuestra especialidad es el control de velocidad de cada rueda. Cada 33 milisegundos, el Arduino ajusta la potencia sumando solo el cambio necesario. [CLIC] Un PID tradicional, posicional, recalcula la potencia total en cada ciclo, y su parte derivativa suele amplificar el ruido de los encoders. El PI incremental de este robot calcula solo el incremento de PWM y lo suma al valor anterior, con la acción proporcional sobre la medición. [CLIC] Lo elegí por tres razones. Primero, sin derivada no amplifica el ruido de los pulsos, y es el esquema probado en robótica móvil. Segundo, la referencia entra solo por la integral: no hay saltos al cambiar la consigna, y al llegar al tope de 255 deja de acumular, un anti-windup natural. Tercero, es liviano y ya viene integrado con diffdrive_arduino en ROS 2. [CLIC] En el robot real, a 0,13 m/s, las ruedas suben en 0,8 y 1,4 segundos, sin sobreimpulso, con error final de hasta 0,002 m/s y un margen de fase entre 41 y 57 grados.

Lámina 18 · Identificación del motor (65 s)

¿Cómo se obtienen esas ganancias? Con un flujo automatizado en Python. [CLIC] Paso 1, la captura en lazo abierto: sin controlador, apliqué a cada motor un escalón fijo de PWM 143 sobre 255 durante 10 segundos y grabé cada 0,1 segundos la velocidad real de cada rueda. [CLIC] Paso 2, un primer PSO, optimización por enjambre de partículas: 50 candidatos durante 150 generaciones hacen ingeniería inversa sobre esa curva y encuentran un modelo de primer orden con retardo para cada rueda. [CLIC] El modelo tiene tres constantes. Km, la ganancia, es la meseta dividida por el PWM: 0,000913 y 0,000890 m/s por unidad de PWM. τ, la constante de tiempo, fija qué tan rápido sube: 0,33 y 0,35 segundos. Y L, el retardo, es menor que una muestra. Con este modelo puedo simular el escalón sin tocar el robot.

Lámina 19 · Optimización y ajuste fino (65 s)

[CLIC] Paso 3: sobre ese modelo, un segundo PSO simula el PI del Arduino a 30 hertz y busca Kp, Kd y Ki, minimizando el error más tres veces el sobreimpulso. Entrega una semilla estable. Después afiné en el piso, a 0,13 m/s, para compensar la zona muerta del driver L298N y la fricción, que el modelo no ve. Así Kp pasó de 12,48 y 10,10 a 16,00 y 16,42, y Kd de unos 35 a 20,30 y 20,05. [CLIC] El gráfico compara ambas corridas en el robot real. En gris, con la semilla, la rueda derecha se quedaba en 0,11 y llegaba recién a los 6 segundos. Con las ganancias finales, las ruedas suben en 0,8 y 1,4 segundos, sin sobreimpulso. [CLIC] Automatizarlo en Python reduce la prueba y error, compensa motores distintos, da un punto de partida seguro y se puede repetir si se cambian los motores.

Lámina 20 · Cómo dibuja el mapa (55 s)

Ahora, cómo el robot construye el mapa del video. [CLIC] Mientras se mueve, el láser gira y mide la distancia a cada muro que tiene a la vista. [CLIC] Al mismo tiempo, los encoders dicen cuánto avanzó y giró el robot entre una medición y otra: es la odometría. [CLIC] Como las ruedas pueden resbalar, SLAM Toolbox compara cada nuevo barrido del láser con los anteriores y así corrige la deriva de la odometría. Con eso pinta una grilla de cuadros de 5 cm: blanco libre, negro muro y gris sin explorar. [CLIC] Y si el robot vuelve a ver un lugar por donde ya pasó, reconoce la coincidencia, lo que se llama cierre de lazo, y corrige el error acumulado del recorrido.

Lámina 21 · Metas y exploración (70 s)

Ahora, ¿cómo decide el robot hacia dónde moverse si nadie le entregó un mapa ni una ruta? Aquí entran dos ideas: las fronteras y las metas. [CLIC] Una frontera es el borde entre el espacio libre que ya conoce, en blanco, y lo desconocido, en gris. El explorador las busca en el mapa en vivo. [CLIC] Una meta es un punto con coordenadas x e y sobre una de esas fronteras. El explorador la elige solo, equilibrando cercanía y tamaño de la zona por descubrir. No es una lista de puntos que alguien programó antes. [CLIC] Esa meta pasa a Nav2, que deja un margen de seguridad de 15 cm junto a cada muro, el borde morado del video. A estrella calcula la ruta verde y DWB la recorre con curvas seguras. [CLIC] Cuando el explorador ya no encuentra fronteras alcanzables, da por terminado el recorrido y detiene el robot por sí solo.

## 05 · Resultados

Lámina 22 · Portada 05 · Resultados (4 s)

Quinto, lo que medí en el robot real.

Lámina 23 · En el robot real (65 s)

Todas las mediciones que presento se hicieron en el robot físico, en este recinto con pasillos y tabiques internos, pensado para exigir giros y espacios estrechos. Hice seis exploraciones completas. En la segunda el robot no generó mapa, así que la excluí de los promedios. [CLIC] En lo operativo, 5 de 6 exploraciones terminaron solas, deteniéndose al completar el mapa. En total, Nav2 condujo al robot 21,9 metros en 12,7 minutos, con navegación y recuperación autónoma en pasillos estrechos de 58 cm, sin atascos ni intervención humana. [CLIC] ¿Y qué tan fiel es el mapa? Al compararlo con un plano del recinto medido con cinta métrica, la diferencia media en la posición de los muros fue de 3,4 cm, menos que un cuadro del mapa, que mide 5. Además, el área libre mapeada fue muy estable: 3,50 m² en promedio, con una variación de solo 0,03.

Lámina 24 · Tres capas (55 s)

Tres capas sostienen esos mapas. [CLIC] La primera es el control estable que vimos: sin sobreimpulso y con margen de fase entre 41 y 57 grados. [CLIC] La segunda es una odometría repetible: en cinco rectas de 2 metros medidas con cinta métrica, el error medio fue de 3,63 por ciento. [CLIC] La tercera es el láser, que corrige los giros. En vueltas de 360° la desviación media fue de 11,7°, porque las ruedas patinan más al girar y no hay sensor de giro. SLAM Toolbox realinea los muros en vivo. [CLIC] El resultado es un plano fiel al real, a 3,4 cm. [CLIC] ¿Y si la odometría falla? SLAM corrige la deriva, pero necesita una base estable: mejor control y odometría significan menos corrección y mapas más firmes.

Lámina 25 · Mapas repetibles (65 s)

[CLIC] Este gráfico muestra el área libre mapeada en las cinco exploraciones válidas. El eje parte en 3,40 para que se vean las diferencias: entre la mayor y la menor hay solo 0,06 m². [CLIC] A la derecha están la exploración 1 y la 6. Su índice de cobertura es de 83 y 53 por ciento, lo que podría parecer inconsistente, pero mapearon casi la misma superficie: 3,51 y 3,48 m². [CLIC] De aquí salen dos lecturas. Primero, confiabilidad operativa: con 3,50 ± 0,03 m², el robot mapea el recinto completo igual en cada ejecución. Segundo, el índice no indica error: solo mide qué parte de la imagen es espacio libre, y cada imagen incluye más o menos gris de afuera según cómo quedó orientado el mapa. La evidencia del mapeo es el área y la comparación con el plano real.

Lámina 26 · Navegación adaptativa (60 s)

Al revisar los registros de navegación apareció algo que conviene explicar bien. [CLIC] El robot avanza hacia una meta A. [CLIC] El explorador revisa el mapa cada 3,3 segundos, y aquí el láser descubre una zona mayor. [CLIC] Entonces envía una meta B, mejor, sin cancelar la anterior. [CLIC] Esta versión de Nav2 anota ese reemplazo como «abortado», aunque el robot nunca se detuvo: cambió de destino mientras avanzaba, buscando más mapa en menos recorrido. [CLIC] Por eso, de 60 metas, 54 figuran como abortadas, pero 53 coinciden justo con la llegada de la meta siguiente. Soy cuidadoso en esto: el registro no permite descartar otras causas caso a caso, y por eso no lo uso como tasa de éxito. La síntesis es que los cuatro subsistemas funcionaron juntos en el robot real.

## 06 · Conclusiones

Lámina 27 · Portada 06 · Conclusiones (4 s)

Y para cerrar, qué se logró y qué sigue.

Lámina 28 · Cumplimiento de objetivos (65 s)

Reviso ahora los cuatro objetivos específicos. [CLIC] El primero, construir el robot y su gemelo digital, está logrado y verificado antes en Gazebo Classic. [CLIC] El segundo, el control de las ruedas, está logrado en lo ensayado: encoders, odometría y un control PI estable a 0,13 m/s. En la tesis lo marqué parcial porque lo evalué en un solo punto de operación. El próximo paso es probar otras velocidades. [CLIC] El tercero, mapear, ubicarse y navegar, también está logrado en lo ensayado: mapas a 3,4 cm del plano y 21,9 metros autónomos. Lo marqué parcial porque las metas fijas quedaron fuera del alcance. [CLIC] Y el cuarto, explorar sin ayuda, está logrado: la exploración terminó sola en 5 de 6 ensayos. El objetivo general se cumple en lo funcional. Las marcas de parcial son una decisión de rigor, para no inflar los indicadores.

Lámina 29 · De prototipo a solución de campo (55 s)

Si quisiera llevar esto a una solución de campo, el precio no basta. La pregunta es qué ya está demostrado y qué falta. [CLIC] La etapa 1 es la base demostrada hoy: mapas a 3,4 cm del plano, 21,9 metros autónomos, 5 de 6 exploraciones cerradas solas y una plataforma abierta. [CLIC] La etapa 2 es el escalamiento técnico: sensor de giro, recintos amplios y metas fijas con 6 a 10 repeticiones. [CLIC] Y la etapa 3 sería la aplicación de campo: sensores de gases, temperatura o láser 3D, un chasis industrial y una versión vigente de ROS 2. Las etapas 2 y 3 son una propuesta. La cadena completa de autonomía ya está medida, y cada brecha se puede cerrar sobre esta misma base.

Lámina 30 · Aporte de ingeniería (40 s)

[CLIC] El aporte de ingeniería es la integración completa y publicada: hardware, firmware, modelo URDF y scripts abiertos para replicar y mejorar la plataforma. El firmware y la interfaz del Arduino se adaptaron de proyectos abiertos, debidamente citados. [CLIC] El gemelo digital parametrizado permite probar algoritmos o cambios físicos en simulación antes de tocar el robot, ahorrando tiempo y daños. [CLIC] La sintonización automatizada por rueda calibra motores económicos distintos de forma repetible, sin partir a ciegas. [CLIC] Y la estabilidad del control quedó verificada: las ruedas responden sin oscilar, aun con retardos del sistema.

Lámina 31 · Conclusión (50 s)

[CLIC] Vuelvo a la pregunta del inicio. Sí: es viable construir un robot diferencial de bajo costo que mapea, navega y explora interiores de forma autónoma, y lo respaldo con mediciones en el robot real. [CLIC] Todo el trabajo está publicado en nuestro repositorio de GitHub, ros2-indoor-exploration-robot: código ROS 2, firmware, piezas 3D y scripts de ajuste, con licencia MIT, listo para docencia o para sumar sensores de inspección. [CLIC] Me quedo con tres ideas. Un control de ruedas bien ajustado sostiene mapas fieles. Repartir el trabajo entre el robot y el computador hace viable la autonomía con hardware accesible. Y la evidencia está medida en hardware real.

Lámina 32 · Gracias (5 s)

Muchas gracias por su atención. Quedo atento a sus preguntas y comentarios. [Para mostrar un respaldo: clic en «Respaldo», abajo a la derecha, y elegir el tema.]

## Láminas de respaldo

Están ocultas: no aparecen al avanzar. Para abrir una, haz clic en «Respaldo» en la lámina 32, o escribe 33 y Enter para ir al índice. Cada respaldo tiene «Volver al índice».

| Lámina | Código | Grupo | Tema |
|---|---|---|---|
| 33 | Índice | | Láminas de respaldo |
| 34 | R1 | Control | Ley PI: el ciclo cada 33 ms |
| 35 | R2 | Control | Por qué el firmware actúa como un PI |
| 36 | R3 | Control | Robustez del control |
| 37 | R4 | Control | Giros: el láser mantiene el mapa recto |
| 38 | R5 | Hardware | Eléctrico: L298N y MOSFET |
| 39 | R6 | Hardware | Margen de seguridad de 15 cm |
| 40 | R7 | Proyecto | Aporte propio |
| 41 | R8 | Proyecto | Red dedicada y computador externo |
| 42 | R9 | Resultados | Mapa frente al plano real |
| 43 | R10 | Alternativas | Alternativas de plataforma |
| 44 | R11 | Alternativas | Alternativas de mapeo |
| 45 | R12 | Alternativas | Alternativas de navegación y exploración |

## Respuestas breves

R1 · Ley PI: el ciclo cada 33 ms (lámina 34)

Cada 33 milisegundos el Arduino repite cuatro pasos: mide la velocidad con los encoders, la compara con la velocidad pedida, calcula una corrección y la suma a la potencia que el motor ya tenía. Mientras hay error, el PWM sube un poco en cada ciclo. Cuando el error llega a cero, la corrección es cero y la potencia se mantiene sin caer. Eso es acción integral.

R2 · Por qué el firmware actúa como un PI (lámina 35)

En la ley del firmware, la corrección es Kp por el error, menos Kd por el cambio de la medición, más un término acumulado, todo dividido por Ko, y se suma al PWM anterior. Al acumularse, Kp actúa como integral, Kd como proporcional sobre la medición y Ki como doble integral, prácticamente inactiva porque ese término es entero y se trunca. Equivale a un PI clásico con ganancia proporcional Kd sobre Ko, de 0,41 y 0,40, y tiempo integral de 42 y 40 milisegundos. Se mantuvo por compatibilidad con diffdrive_arduino.

R3 · Robustez del control (lámina 36)

Hice tres pruebas. Un análisis discreto a 33 milisegundos en Python, con AnalisisEstabilidadPID.py, sobre el modelo identificado de cada rueda, sin retardo y con 0,1 segundos de retardo. Un barrido de 625 combinaciones de ganancia y constante de tiempo: sin retardo, las 625 son estables. Y la verificación en el robot real a 0,13 m/s. El control tolera entre 0,32 y 0,45 segundos de retardo extra, unas 4,5 veces más ganancia y su pico de sensibilidad queda entre 1,35 y 1,85, en el rango típico. Con 0,1 segundos de retardo, las combinaciones más extremas del barrido sí se inestabilizan, 102 de 625, y por eso el margen útil es el de 4,5 veces. El análisis es lineal: no incluye la zona muerta ni el truncamiento entero.

R4 · Giros: el láser mantiene el mapa recto (lámina 37)

Sin IMU, el ángulo sale solo de la diferencia de avance entre ruedas, y cualquier resbalón queda en el ángulo. Aun así, la desviación media fue de 11,7° por vuelta, un 3,24 por ciento, con repeticiones de solo 4,0° y 4,3°, y otras de hasta 20°. El gran hallazgo es que SLAM Toolbox alinea cada barrido del láser y absorbe ese deslizamiento en vivo: los muros quedan a 3,4 cm del plano. Sumar una IMU con filtro de Kalman, mediante robot_localization, conviene al escalar a trayectos largos o pasillos sin referencias cercanas.

R5 · Eléctrico: L298N y MOSFET (lámina 38)

Hay dos dominios: 12 volts de la batería para los motores a través del L298N, y un conversor de 25 watts que entrega 5 volts regulados a la Raspberry, el Arduino y el láser, con interruptor y portafusible. ¿Por qué L298N? Entrega 2 amperes continuos por canal frente a 0,35 en marcha, soporta hasta 46 volts, tiene protección térmica, cuesta unos 3 000 pesos y trae borneras. El TB6612FNG, más eficiente, queda justo: 1,2 amperes continuos y 13,5 volts recomendados, frente a 12,6 volts de la batería y arranques sobre 1,2 amperes. La migración viable son dos DRV8871: 3,6 amperes pico, límite de corriente y protección térmica, con solo 0,2 volts de caída y menos calor.

R6 · Margen de seguridad de 15 cm (lámina 39)

Los pasillos miden 58 cm. Con un margen igual a la esquina del robot, 24 cm por lado, el centro tendría solo 10 cm de paso. Con 15 cm quedan 28 cm y el robot recorre todos los pasillos. El límite es que el planificador revisa el centro y no el contorno, y eso quedó documentado.

R7 · Aporte propio (lámina 40)

Reutilicé la infraestructura estándar de ROS 2 y adapté cuatro paquetes abiertos, todos citados. Mi desarrollo propio está en la integración, el modelo del robot, el nodo del láser, el paquete de identificación y PSO, el análisis de estabilidad y los protocolos de ensayo. Todo está publicado en el repositorio del proyecto.

R8 · Red dedicada y computador externo (lámina 41)

Repartí el trabajo para que el robot haga solo lo urgente y el computador lo pesado. Así el tiempo real queda protegido en el Arduino y la Raspberry Pi 4, el cómputo pesado corre en un computador portátil de gama media sin encarecer el robot, y RViz2 permite supervisar y diagnosticar en vivo. La red Wi-Fi es dedicada, con IP fijas, y ROS 2 usa CycloneDDS.

R9 · Mapa frente al plano real (lámina 42)

Los mapas se ubican sobre el plano sin escalarlos. La distancia media es de 3,4 cm, entre 3,1 y 3,7 cm por mapa, menor que un cuadro de 5 cm. El plano se midió con cinta métrica.

R10 · Alternativas de plataforma (lámina 43)

Un middleware robótico conecta sensores, motores y algoritmos. ROS 1 depende de un nodo maestro: si cae, se detiene todo. YARP comunica módulos, pero no trae mapeo ni navegación. Orocos RTT es para control determinista de brazos, sin mapeo 2D ni rutas. LCM solo transporta mensajes. ROS 2 es distribuido y trae Nav2 y SLAM Toolbox listos para integrar.

R11 · Alternativas de mapeo (lámina 44)

GMapping no cierra lazos y es menos portable a ROS 2. Hector SLAM exige un láser más rápido y caro, y deriva en recintos grandes. Cartographer cierra lazos, pero cuesta más ajustarlo y es el que más CPU usa entre los métodos 2D comparados. SLAM Toolbox cierra lazos, guarda el mapa y corre bien en un computador portátil de gama media.

R12 · Alternativas de navegación y exploración (lámina 45)

En navegación, RRT sirve más en espacios continuos o brazos, Pure Pursuit responde peor ante obstáculos cercanos y MPPI pide mucho más cómputo. A estrella con DWB es directo en la grilla 2D. En exploración, la ganancia de información y el SLAM activo agregan modelos y cálculo extra. Las fronteras son livianas y usan directamente el mapa.

## Mini glosario

Una frase por término, para responder sin jerga.

- **LIDAR 2D:** sensor láser que gira y mide la distancia a lo que lo rodea, en un plano.
- **Encoder:** sensor que cuenta cuánto gira cada rueda.
- **Odometría:** estimar cuánto avanzó y giró el robot contando el giro de sus ruedas.
- **IMU:** sensor de giro y aceleración. Este robot no lo tiene.
- **SLAM:** construir el mapa y ubicarse en él al mismo tiempo.
- **Cierre de lazo:** cuando SLAM reconoce un lugar ya visto y corrige el error acumulado.
- **Middleware robótico:** software que conecta sensores, motores y algoritmos para que trabajen como un solo sistema.
- **ROS 2:** middleware estándar para robots, organizado en programas que se envían mensajes.
- **Nav2:** el sistema de navegación de ROS 2: traza la ruta y ordena las velocidades.
- **A\* (A estrella):** busca el camino más corto en la grilla del mapa, sumando lo recorrido y una estimación de lo que falta.
- **DWB:** prueba trayectorias cortas posibles según la velocidad actual y elige la que sigue la ruta lejos de los obstáculos.
- **Frontera:** el borde entre el espacio libre conocido y lo desconocido.
- **Meta:** el punto (x, y) en una frontera hacia donde el explorador manda al robot.
- **Rueda pivote:** rueda libre que solo apoya el chasis y gira hacia donde la empujan.
- **PWM:** la forma de dosificar la potencia del motor, de 0 a 255 en este Arduino.
- **PI:** control con una parte proporcional al error y otra que acumula el error pasado.
- **FOPDT:** modelo simple de un motor con tres parámetros: Km (cuánta velocidad entrega por PWM), τ (qué tan rápido responde) y L (retardo).
- **PSO:** optimización por enjambre de partículas: muchos candidatos prueban combinaciones y convergen hacia la mejor.
- **URDF:** formato estándar que describe las piezas y uniones de un robot.
- **AMCL:** método para ubicarse dentro de un mapa ya guardado. Quedó fuera del alcance.
- **Gemelo digital:** copia virtual del robot en el simulador.

## Cómo ensayar

1. No memorices palabra por palabra. Fija las ideas clave de cada lámina y la frase de paso a la siguiente.
2. Escucha `audio_guion/defensa_completa.mp3` una vez siguiendo la presentación, para fijar el orden y los clics.
3. Ensaya con la presentación corriendo y un cronómetro, al menos tres veces, para calzar cada clic con tu voz.
4. Repasa las respuestas breves con `audio_guion/respaldos_respuestas.mp3`.
5. Grábate una vez en audio y escucha si se cuelan muletillas.
