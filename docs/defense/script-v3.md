# Guion de la defensa v3 · Navegación y exploración autónoma de interiores

Va con `slides-v3.pptx`: 34 láminas visibles y 13 ocultas (un índice y 12 respaldos, de la 35 a la 47). El mismo texto está en las notas del orador de cada lámina, para leerlo en la vista del moderador.

Cada `[CLIC]` hace aparecer la parte siguiente de la lámina. El número de clics de cada lámina coincide con sus animaciones. El video de la lámina 2 parte solo al entrar. Las seis portadas azules no tienen clics: el ícono del tema viaja solo, con la transición Morph, hasta la cabecera de la lámina siguiente.

Duración estimada de la narración: 26 min 34 s a 130 palabras por minuto (3463 palabras). Con pausas naturales debe quedar bajo el límite de 30 minutos. `generar_audio_guion.py` imprime la duración real del audio de ensayo.

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

Lámina 18 · Paso 1: medir cada rueda (40 s)

¿Cómo llegué a esas ganancias? En cuatro pasos, automatizados en Python. El primero es medir cómo responde cada rueda. [CLIC] Sin ningún controlador, Python envía a cada motor un pulso fijo de potencia, cerca del 56 por ciento del máximo, durante 10 segundos. [CLIC] Mientras tanto, los encoders graban la velocidad real de cada rueda cada décima de segundo. Ambas suben rápido y se estabilizan cerca de 0,13 m/s. [CLIC] El hallazgo inmediato es que, aunque los dos motores son del mismo modelo, cada rueda responde distinto. Por eso modelé cada una por separado.

Lámina 19 · Paso 2: los 3 rasgos del motor (60 s)

Segundo paso: de esa curva real extraigo tres rasgos que describen cada motor. Un primer enjambre de partículas, el PSO, prueba combinaciones en Python hasta que la curva simulada calza con la medida. [CLIC] El primer rasgo es el retardo: el motor despega casi al instante, en menos de una décima de segundo. [CLIC] El segundo es la rapidez: llega al 63 por ciento de su velocidad final en unos 0,3 segundos. [CLIC] El tercero es la fuerza, o ganancia: cuánta velocidad final entrega por cada unidad de potencia aplicada. [CLIC] El hallazgo clave: ambas ruedas reaccionan casi al instante y aceleran en un tercio de segundo, pero con distinta fuerza. La copia virtual de cada motor captura esa diferencia, y con ella puedo simular antes de tocar el robot.

Lámina 20 · Paso 3: simular y buscar (50 s)

Tercer paso: buscar las ganancias en simulación. [CLIC] Python reemplaza el motor físico por su copia virtual y prueba la misma ley PI del Arduino, a 30 hertz. [CLIC] Un segundo enjambre PSO prueba 7 500 combinaciones de ganancias en segundos: 50 partículas durante 150 rondas. Premia llegar rápido a la velocidad pedida y castiga con peso triple pasarse de ella. [CLIC] El hallazgo: entrega un punto de partida estable para cada rueda, listo para cargar sin vibraciones ni riesgo para los motores. [CLIC] Automatizarlo en Python reduce la prueba y error, compensa las diferencias entre motores económicos, da un punto de partida seguro y se puede repetir si se cambian motores o ruedas.

Lámina 21 · Paso 4: ajuste en el piso real (70 s)

Cuarto paso: probar esas ganancias en el robot real, a 0,13 m/s. [CLIC] ¿Por qué retocarlas? Porque la copia virtual no ve la fricción del suelo ni la zona muerta del driver L298N, donde con poca potencia el motor no arranca. Por eso subí Kp para un arranque más firme, bajé Kd para un movimiento parejo y subí Ki en la rueda izquierda para quitar el error final. [CLIC] El gráfico compara ambas corridas en el piso. En gris, con la semilla, la rueda izquierda se quedaba corta y la derecha tardaba unos 6 segundos. En color, con el ajuste final, las ruedas llegan en 0,8 y 1,4 segundos. [CLIC] El salto es de cuatro veces: de unos 6 segundos a menos de 1,5, con precisión y sin sobreimpulso. Y la lección práctica: simular ahorra horas, pero la fricción del piso y la zona muerta siempre exigen un ajuste real.

Lámina 22 · Cómo dibuja el mapa (55 s)

Ahora, cómo el robot construye el mapa del video. [CLIC] Mientras se mueve, el láser gira y mide la distancia a cada muro que tiene a la vista. [CLIC] Al mismo tiempo, los encoders dicen cuánto avanzó y giró el robot entre una medición y otra: es la odometría. [CLIC] Como las ruedas pueden resbalar, SLAM Toolbox compara cada nuevo barrido del láser con los anteriores y así corrige la deriva de la odometría. Con eso pinta una grilla de cuadros de 5 cm: blanco libre, negro muro y gris sin explorar. [CLIC] Y si el robot vuelve a ver un lugar por donde ya pasó, reconoce la coincidencia, lo que se llama cierre de lazo, y corrige el error acumulado del recorrido.

Lámina 23 · Metas y exploración (70 s)

Ahora, ¿cómo decide el robot hacia dónde moverse si nadie le entregó un mapa ni una ruta? Aquí entran dos ideas: las fronteras y las metas. [CLIC] Una frontera es el borde entre el espacio libre que ya conoce, en blanco, y lo desconocido, en gris. El explorador las busca en el mapa en vivo. [CLIC] Una meta es un punto con coordenadas x e y sobre una de esas fronteras. El explorador la elige solo, equilibrando cercanía y tamaño de la zona por descubrir. No es una lista de puntos que alguien programó antes. [CLIC] Esa meta pasa a Nav2, que deja un margen de seguridad de 15 cm junto a cada muro, el borde morado del video. A estrella calcula la ruta verde y DWB la recorre con curvas seguras. [CLIC] Cuando el explorador ya no encuentra fronteras alcanzables, da por terminado el recorrido y detiene el robot por sí solo.

## 05 · Resultados

Lámina 24 · Portada 05 · Resultados (4 s)

Quinto, lo que medí en el robot real.

Lámina 25 · En el robot real (65 s)

Todas las mediciones que presento se hicieron en el robot físico, en este recinto con pasillos y tabiques internos, pensado para exigir giros y espacios estrechos. Hice seis exploraciones completas. En la segunda el robot no generó mapa, así que la excluí de los promedios. [CLIC] En lo operativo, 5 de 6 exploraciones terminaron solas, deteniéndose al completar el mapa. En total, Nav2 condujo al robot 21,9 metros en 12,7 minutos, con navegación y recuperación autónoma en pasillos estrechos de 58 cm, sin atascos ni intervención humana. [CLIC] ¿Y qué tan fiel es el mapa? Al compararlo con un plano del recinto medido con cinta métrica, la diferencia media en la posición de los muros fue de 3,4 cm, menos que un cuadro del mapa, que mide 5. Además, el área libre mapeada fue muy estable: 3,50 m² en promedio, con una variación de solo 0,03.

Lámina 26 · Tres capas (55 s)

Tres capas sostienen esos mapas. [CLIC] La primera es el control estable que vimos: sin sobreimpulso y con margen de fase entre 41 y 57 grados. [CLIC] La segunda es una odometría repetible: en cinco rectas de 2 metros medidas con cinta métrica, el error medio fue de 3,63 por ciento. [CLIC] La tercera es el láser, que corrige los giros. En vueltas de 360° la desviación media fue de 11,7°, porque las ruedas patinan más al girar y no hay sensor de giro. SLAM Toolbox realinea los muros en vivo. [CLIC] El resultado es un plano fiel al real, a 3,4 cm. [CLIC] ¿Y si la odometría falla? SLAM corrige la deriva, pero necesita una base estable: mejor control y odometría significan menos corrección y mapas más firmes.

Lámina 27 · Mapas repetibles (65 s)

[CLIC] Este gráfico muestra el área libre mapeada en las cinco exploraciones válidas. El eje parte en 3,40 para que se vean las diferencias: entre la mayor y la menor hay solo 0,06 m². [CLIC] A la derecha están la exploración 1 y la 6. Su índice de cobertura es de 83 y 53 por ciento, lo que podría parecer inconsistente, pero mapearon casi la misma superficie: 3,51 y 3,48 m². [CLIC] De aquí salen dos lecturas. Primero, confiabilidad operativa: con 3,50 ± 0,03 m², el robot mapea el recinto completo igual en cada ejecución. Segundo, el índice no indica error: solo mide qué parte de la imagen es espacio libre, y cada imagen incluye más o menos gris de afuera según cómo quedó orientado el mapa. La evidencia del mapeo es el área y la comparación con el plano real.

Lámina 28 · Navegación adaptativa (60 s)

Al revisar los registros de navegación apareció algo que conviene explicar bien. [CLIC] El robot avanza hacia una meta A. [CLIC] El explorador revisa el mapa cada 3,3 segundos, y aquí el láser descubre una zona mayor. [CLIC] Entonces envía una meta B, mejor, sin cancelar la anterior. [CLIC] Esta versión de Nav2 anota ese reemplazo como «abortado», aunque el robot nunca se detuvo: cambió de destino mientras avanzaba, buscando más mapa en menos recorrido. [CLIC] Por eso, de 60 metas, 54 figuran como abortadas, pero 53 coinciden justo con la llegada de la meta siguiente. Soy cuidadoso en esto: el registro no permite descartar otras causas caso a caso, y por eso no lo uso como tasa de éxito. La síntesis es que los cuatro subsistemas funcionaron juntos en el robot real.

## 06 · Conclusiones

Lámina 29 · Portada 06 · Conclusiones (4 s)

Y para cerrar, qué se logró y qué sigue.

Lámina 30 · Cumplimiento de objetivos (65 s)

Reviso ahora los cuatro objetivos específicos. [CLIC] El primero, construir el robot y su gemelo digital, está logrado y verificado antes en Gazebo Classic. [CLIC] El segundo, el control de las ruedas, está logrado en lo ensayado: encoders, odometría y un control PI estable a 0,13 m/s. En la tesis lo marqué parcial porque lo evalué en un solo punto de operación. El próximo paso es probar otras velocidades. [CLIC] El tercero, mapear, ubicarse y navegar, también está logrado en lo ensayado: mapas a 3,4 cm del plano y 21,9 metros autónomos. Lo marqué parcial porque las metas fijas quedaron fuera del alcance. [CLIC] Y el cuarto, explorar sin ayuda, está logrado: la exploración terminó sola en 5 de 6 ensayos. El objetivo general se cumple en lo funcional. Las marcas de parcial son una decisión de rigor, para no inflar los indicadores.

Lámina 31 · De prototipo a solución de campo (55 s)

Si quisiera llevar esto a una solución de campo, el precio no basta. La pregunta es qué ya está demostrado y qué falta. [CLIC] La etapa 1 es la base demostrada hoy: mapas a 3,4 cm del plano, 21,9 metros autónomos, 5 de 6 exploraciones cerradas solas y una plataforma abierta. [CLIC] La etapa 2 es el escalamiento técnico: sensor de giro, recintos amplios y metas fijas con 6 a 10 repeticiones. [CLIC] Y la etapa 3 sería la aplicación de campo: sensores de gases, temperatura o láser 3D, un chasis industrial y una versión vigente de ROS 2. Las etapas 2 y 3 son una propuesta. La cadena completa de autonomía ya está medida, y cada brecha se puede cerrar sobre esta misma base.

Lámina 32 · Aporte de ingeniería (40 s)

[CLIC] El aporte de ingeniería es la integración completa y publicada: hardware, firmware, modelo URDF y scripts abiertos para replicar y mejorar la plataforma. El firmware y la interfaz del Arduino se adaptaron de proyectos abiertos, debidamente citados. [CLIC] El gemelo digital parametrizado permite probar algoritmos o cambios físicos en simulación antes de tocar el robot, ahorrando tiempo y daños. [CLIC] La sintonización automatizada por rueda calibra motores económicos distintos de forma repetible, sin partir a ciegas. [CLIC] Y la estabilidad del control quedó verificada: las ruedas responden sin oscilar, aun con retardos del sistema.

Lámina 33 · Conclusión (50 s)

[CLIC] Vuelvo a la pregunta del inicio. Sí: es viable construir un robot diferencial de bajo costo que mapea, navega y explora interiores de forma autónoma, y lo respaldo con mediciones en el robot real. [CLIC] Todo el trabajo está publicado en nuestro repositorio de GitHub, ros2-indoor-exploration-robot: código ROS 2, firmware, piezas 3D y scripts de ajuste, con licencia MIT, listo para docencia o para sumar sensores de inspección. [CLIC] Me quedo con tres ideas. Un control de ruedas bien ajustado sostiene mapas fieles. Repartir el trabajo entre el robot y el computador hace viable la autonomía con hardware accesible. Y la evidencia está medida en hardware real.

Lámina 34 · Gracias (5 s)

Muchas gracias por su atención. Quedo atento a sus preguntas y comentarios. [Para mostrar un respaldo: clic en «Respaldo», abajo a la derecha, y elegir el tema.]

## Láminas de respaldo

Están ocultas: no aparecen al avanzar. Para abrir una, haz clic en «Respaldo» en la lámina 34, o escribe 35 y Enter para ir al índice. Cada respaldo tiene «Volver al índice».

| Lámina | Código | Grupo | Tema |
|---|---|---|---|
| 35 | Índice | | Láminas de respaldo |
| 36 | R1 | Control | El robot corrige sus ruedas 30 veces por segundo |
| 37 | R2 | Control | Ley PI estándar: simple, sin ruido y lista para ROS 2 |
| 38 | R3 | Control | Control probado en 625 escenarios, sin oscilar |
| 39 | R4 | Control | Sin IMU, el láser logra mapas a 3,4 cm del plano |
| 40 | R5 | Hardware | L298N hoy y 2 DRV8871 para una versión compacta |
| 41 | R6 | Hardware | Margen de 15 cm para pasillos de 58 cm |
| 42 | R7 | Proyecto | Software abierto probado y piezas clave propias |
| 43 | R8 | Proyecto | Repartir la carga protege el tiempo real |
| 44 | R9 | Resultados | Los 5 mapas calzan con el plano real a 3,4 cm |
| 45 | R10 | Alternativas | Plataforma: ganó ROS 2 |
| 46 | R11 | Alternativas | Mapeo: ganó SLAM Toolbox |
| 47 | R12 | Alternativas | Navegación y exploración: ganaron A* + DWB y fronteras |

## Respuestas breves

R1 · El robot corrige sus ruedas 30 veces por segundo (lámina 36)

Cada 33 milisegundos, es decir, 30 veces por segundo, el Arduino repite cuatro pasos: mide la velocidad con los encoders, la compara con la pedida, calcula un ajuste pequeño y lo suma a la potencia que el motor ya tenía. Mientras hay error, la potencia sube un poco en cada ciclo. Cuando el error llega a cero, se mantiene sin caer. Por eso corrige de forma suave, sin tirones.

R2 · Ley PI estándar: simple, sin ruido y lista para ROS 2 (lámina 37)

Es la ley PI estándar en robótica, en su forma incremental. Elimina el error porque acumula ajustes hasta llegar a la velocidad pedida. Frena sin ruido porque no usa derivada, que amplificaría los pulsos del encoder. Y es segura al tope: deja de acumular al llegar al máximo de potencia. Ya viene integrada con diffdrive_arduino en ROS 2. Las ganancias finales son Kp 16,00 y 16,42, Kd 20,30 y 20,05, y Ko 50. Equivale a un PI clásico con ganancia proporcional de 0,41 y 0,40 y tiempo integral de 42 y 40 milisegundos.

R3 · Control probado en 625 escenarios, sin oscilar (lámina 38)

Lo probé de tres formas: un análisis discreto a 33 milisegundos sobre el modelo de cada rueda, un barrido de 625 combinaciones de ganancia y rapidez del motor, y la prueba real a 0,13 m/s. Ante demoras, tolera entre 0,32 y 0,45 segundos de retardo extra sin oscilar. Ante cambios de batería o de piso, soporta unas 4,5 veces más ganancia. Y su pico de sensibilidad queda entre 1,35 y 1,85, dentro del rango típico, sin sobreimpulso. Sin retardo, los 625 casos son estables. Con 0,1 segundos de retardo, las combinaciones más extremas sí se inestabilizan, 102 de 625, y por eso el margen que reporto es el de 4,5 veces.

R4 · Sin IMU, el láser logra mapas a 3,4 cm del plano (lámina 39)

Sin sensor de giro, el ángulo sale solo de las ruedas, que al girar resbalan un poco: en vueltas de 360 grados la desviación media fue de 3,24 por ciento, una precisión de 96,8 por ciento. Ese es el compromiso. El láser con SLAM Toolbox corrige ese deslizamiento en vivo y deja los muros a 3,4 cm del plano real. Así no hace falta encarecer el prototipo base. Una IMU con filtro de Kalman conviene al escalar a recintos grandes, como bodegas.

R5 · L298N hoy y 2 DRV8871 para una versión compacta (lámina 40)

El L298N resolvió el prototipo: es robusto, entrega 2 amperes continuos por canal frente a unos 0,35 en marcha, trae borneras y cuesta unos 3 000 pesos. El TB6612FNG quedó descartado porque queda al límite: 13,5 volts recomendados frente a 12,6 de la batería, y picos de arranque sobre su corriente continua. Para una versión más compacta conviene usar dos DRV8871: más eficientes, con solo 0,2 volts de caída, menos calor y una etapa de potencia más pequeña.

R6 · Margen de 15 cm para pasillos de 58 cm (lámina 41)

Los pasillos miden 58 cm. Con un margen de 15 cm por lado quedan 28 cm de paso libre para el centro del robot, y recorre todo el recinto. Con 24 cm, el tamaño de su esquina, quedarían solo 10 cm y las rutas se bloquean. El límite es que el planificador revisa el centro y no el contorno. El siguiente paso es evaluar el contorno rotado completo al girar.

R7 · Software abierto probado y piezas clave propias (lámina 42)

Integré software abierto probado, como ROS 2, Nav2, SLAM Toolbox y Gazebo, y adapté cuatro proyectos abiertos, todos citados. Lo propio está en las piezas clave de ingeniería: el modelo URDF del robot real, el nodo del láser, la identificación de motores con PSO, el análisis de estabilidad y los protocolos de medición. Todo está publicado en el repositorio del proyecto.

R8 · Repartir la carga protege el tiempo real (lámina 43)

El robot hace solo lo urgente y el portátil lo pesado. Así el tiempo real queda protegido en el Arduino y la Raspberry Pi 4, el cómputo pesado corre en un portátil de gama media sin encarecer el robot, y RViz2 permite supervisar en vivo por una red Wi-Fi dedicada, con IP fijas.

R9 · Los 5 mapas calzan con el plano real a 3,4 cm (lámina 44)

Superpuse los 5 mapas sobre el plano medido con cinta métrica, sin reescalarlos. La distancia media es de 3,4 cm, entre 3,1 y 3,7 por mapa: menos que una celda de 5 cm. La escala es real y el mapa sirve para levantar planos.

R10 · Plataforma: ganó ROS 2 (lámina 45)

ROS 1 depende de un nodo maestro: si cae, cae todo. YARP no trae mapeo ni navegación móvil. Orocos RTT es para control de brazos, sin mapeo 2D ni rutas. LCM solo transporta mensajes y obliga a programar todo desde cero. ROS 2 es distribuido y trae Nav2 y SLAM Toolbox listos para integrar.

R11 · Mapeo: ganó SLAM Toolbox (lámina 46)

GMapping no corrige el mapa al volver a un lugar conocido. Hector SLAM exige un láser más caro y deriva en recintos grandes. Cartographer es más difícil de ajustar y el que más CPU usa entre los métodos 2D comparados. SLAM Toolbox corrige el mapa al volver, lo guarda y corre en un portátil de gama media.

R12 · Navegación y exploración: ganaron A* + DWB y fronteras (lámina 47)

En navegación, RRT sirve más en espacios continuos o brazos, y en una grilla 2D A* es más directo. Pure Pursuit responde peor ante obstáculos cercanos y MPPI pide mucho más cómputo que DWB. En exploración, la ganancia de información y el SLAM activo agregan cálculo y complejidad sin beneficio en interiores planos. Las fronteras son livianas y usan directo el mapa.

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
