# Guion de la defensa v3 · Navegación y exploración autónoma de interiores

Va con `slides-v3.pptx`: 34 láminas visibles y 13 ocultas (un índice y 12 respaldos, de la 35 a la 47). El mismo texto está en las notas del orador de cada lámina, para leerlo en la vista del moderador.

Cada `[CLIC]` hace aparecer la parte siguiente de la lámina. El número de clics de cada lámina coincide con sus animaciones. El video de la lámina 2 parte solo al entrar. Las seis portadas azules no tienen clics: el ícono del tema viaja solo, con la transición Morph, hasta la cabecera de la lámina siguiente.

Duración estimada de la narración: 25 min 38 s a 130 palabras por minuto (3333 palabras). Con pausas naturales debe quedar bajo el límite de 30 minutos. `generar_audio_guion.py` imprime la duración real del audio de ensayo.

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

Lámina 18 · Paso 1: medir revela que cada motor es único (40 s)

¿Cómo logré que cada rueda responda tan bien? Con un método de cuatro pasos, automatizado en Python. El primero es medir. [CLIC] Sin controlador, Python aplica el mismo pulso de potencia a los dos motores y los encoders graban cómo acelera cada rueda. [CLIC] Al acercar la vista a la velocidad final aparece algo valioso: son motores económicos del mismo modelo, pero cada uno tiene su propio carácter. [CLIC] La medición lo detecta desde el primer minuto, y por eso cada rueda recibe su propia calibración.

Datos para preguntas (no se leen en voz alta): Pulso fijo de PWM 143 de 255 (≈56 % del máximo) desde t = 1 s, sin controlador. Captura de 10 s, una muestra cada 0,1 s. Velocidad final media (t ≥ 3 s): ≈0,130 m/s la izquierda y ≈0,127 m/s la derecha, unos 2 % de diferencia. La izquierda va más rápido en 86 % de las muestras (chart-control-data.csv). Modelos identificados: Km 0,000913 y 0,000890 m/s por unidad de PWM, τ 0,33 y 0,35 s. Motores JGA25-370 de 12 V con encoder. Tesis, Sec. 4.4.5 (Captura de respuesta en lazo abierto).

Lámina 19 · Paso 2: un gemelo matemático por motor (40 s)

Segundo paso: con esa medición construyo un gemelo matemático de cada motor. Python prueba miles de combinaciones hasta que la curva del gemelo calza con la medición real, como una ingeniería inversa. [CLIC] Captura su reacción: arranca casi al instante. [CLIC] Su rapidez: acelera en un tercio de segundo. [CLIC] Y su fuerza: cuánta velocidad entrega con la potencia aplicada. [CLIC] Lo mejor es que cada gemelo captura hasta la diferencia de fuerza entre ruedas. Desde aquí, cada prueba ocurre en el computador y el robot queda intacto.

Datos para preguntas (no se leen en voz alta): Modelo de primer orden con retardo (FOPDT). Izquierda / derecha: Km 0,000913 / 0,000890 m/s por PWM, τ 0,329 / 0,349 s, L 0,0001 / 0,069 s. L es menor que el muestreo de 0,1 s y se cuantiza a cero muestras: en la práctica el modelo es de primer orden. τ es el tiempo en llegar al 63 % de la velocidad final. «Un tercio de segundo» es τ redondeado. 1.er PSO: 50 partículas, 150 generaciones, costo = error cuadrático medio de identificación. Ajusta la medición suavizada con una media móvil de 5 muestras, por eso la curva del gemelo va algo detrás de los puntos al arrancar. No es el gemelo digital de Gazebo de la lámina 15: este modela solo cómo responde cada motor. Tesis, Sec. 4.4.5 y Anexo de identificación FOPDT.

Lámina 20 · Paso 3: la automatización calibra (40 s)

Tercer paso: dejar que la automatización calibre. [CLIC] El gemelo de cada motor corre con el mismo programa de control del Arduino. [CLIC] Una búsqueda automática evalúa miles de calibraciones y se queda con la que sigue mejor la velocidad pedida sin pasarse. [CLIC] El resultado es una calibración estable para cada rueda, lista para cargar sin riesgo. [CLIC] Y el proyecto gana tres cosas: calibra en el computador, saca lo mejor de motores económicos y se repite con los mismos scripts si mañana cambian motores o ruedas.

Datos para preguntas (no se leen en voz alta): La simulación corre a 30 Hz (período de 33 ms) con la misma ley PI incremental del firmware, sobre el modelo de cada rueda. 2.º PSO: 50 partículas × 150 generaciones = 7 500 evaluaciones por rueda. Costo: error cuadrático medio con peso 1 más sobreimpulso con peso 3. No penaliza el tiempo de subida ni el esfuerzo de control. Semilla entregada: Kp 12,48 / 10,10, Kd 34,69 / 36,70 (el costo evalúa Kd hasta 25), Ki ≈ 0,00001. La tesis no mide el tiempo de cómputo del PSO ni el de un ajuste manual. Por eso la lámina no da tiempos. Tesis, Sec. 4.4.5, Anexo de protocolos de sintonización y Anexo de resultados PSO.

Lámina 21 · Paso 4: ajuste final en el piso (45 s)

Cuarto paso: el toque final en el piso real. [CLIC] El piso aporta lo que ningún modelo simple ve: la fricción del suelo y la zona muerta del driver. Con eso reforcé el arranque y emparejé la respuesta de cada rueda. [CLIC] En gris, la calibración simulada. En color, el ajuste final, que llega antes y limpio a la meta. [CLIC] Ahora cada rueda alcanza la velocidad pedida en menos de un segundo y medio, cerca de un segundo antes y sin sobrepasarse. La simulación entrega la base estable y el piso aporta el toque final.

Datos para preguntas (no se leen en voz alta): Velocidad pedida: 0,13 m/s, misma prueba en el piso antes y después. Con el ajuste final: subida del 10 al 90 % en 0,8 s (izquierda) y 1,4 s (derecha), error final 0,002 y 0,000 m/s, sin sobreimpulso significativo. Margen de fase 41° a 57°. Con la semilla del PSO: la izquierda se queda en 0,12 m/s (error ≈0,01 m/s) y la derecha se detiene cerca de 0,11 m/s y se mantiene en la meta recién después de 6 s. La tesis resume: «la referencia se alcanza cerca de un segundo antes». Cambios: Kp sube 28 % y 63 % (a 16,00 y 16,42), Kd baja 41 % y 45 % (a 20,30 y 20,05), Ki izquierdo a 0,075 (el derecho, 0,001, no tiene efecto en la ley ejecutada). Zona muerta del driver L298N: con poca potencia el motor no gira. La resolución de la medición es 0,01 m/s, por eso la rueda izquierda muestra pequeños saltos. Por qué no «4× más rápido»: comparaba cuándo la rueda se queda en la meta (≈6 s) con el tiempo de subida (1,4 s), dos métricas distintas. Tesis, Sec. 4.4.5 (Refinamiento experimental), Sec. 5.2 y Tabla de indicadores de la respuesta al escalón.

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
| 38 | R3 | Control | El control se mantiene estable con holgura |
| 39 | R4 | Control | Sin IMU y sin costo extra, mapas a 3,4 cm del plano |
| 40 | R5 | Hardware | L298N hoy y DRV8871 para una versión compacta |
| 41 | R6 | Hardware | Un margen de 15 cm abre paso por pasillos de 58 cm |
| 42 | R7 | Proyecto | Software abierto probado y piezas clave propias |
| 43 | R8 | Proyecto | Repartir la carga protege el tiempo real |
| 44 | R9 | Resultados | Los 5 mapas calzan con el plano real a 3,4 cm |
| 45 | R10 | Alternativas | Plataforma: ganó ROS 2 |
| 46 | R11 | Alternativas | Mapeo: ganó SLAM Toolbox |
| 47 | R12 | Alternativas | Navegación y exploración: ganaron A* + DWB y fronteras |

## Respuestas breves

R1 · El robot corrige sus ruedas 30 veces por segundo (lámina 36)

Cada 33 milisegundos, es decir, 30 veces por segundo, el Arduino repite cuatro pasos: mide la velocidad con los encoders, la compara con la pedida, calcula un ajuste pequeño y lo suma a la potencia que el motor ya tenía. Mientras hay error, la potencia sube un poco en cada ciclo. Cuando el error llega a cero, se mantiene sin caer. Por eso corrige de forma suave, sin tirones.

Datos para preguntas (no se leen en voz alta): Ciclo de control de 33 ms en el Arduino Nano, unas 30 veces por segundo. Ley incremental: PWM nuevo = PWM anterior + corrección. La salida se limita a ±255 y el integrador deja de acumular en el tope. Tesis, Sec. 4.4.3.

R2 · Ley PI estándar: simple, sin ruido y lista para ROS 2 (lámina 37)

Es la ley PI estándar en robótica, en su forma incremental. Elimina el error porque acumula ajustes hasta llegar a la velocidad pedida. Frena sin ruido porque no usa derivada, que amplificaría los pulsos del encoder. Y es segura al tope: deja de acumular al llegar al máximo de potencia. Se calibró con una semilla en simulación y un ajuste fino en el piso, y lleva cada rueda a la velocidad pedida en menos de un segundo y medio, sin sobrepasarse. Ya viene integrada con diffdrive_arduino en ROS 2.

Datos para preguntas (no se leen en voz alta): Ganancias finales, izquierda / derecha: Kp 16,00 / 16,42 (firmeza del arranque), Kd 20,30 / 20,05 (en esta ley actúa sobre la medición y suaviza la respuesta), Ki 0,075 / 0,001 (solo la izquierda lo usa para quitar el error final), Ko 50 (escala común). Equivalen a un PI clásico con Kc = Kd ÷ Ko ≈ 0,41 / 0,40 y Ti ≈ 42 / 40 ms. Modelo izquierda / derecha: Km 0,000913 / 0,000890 m/s por PWM, τ 0,33 / 0,35 s, L 0,0001 / 0,07 s. Semilla del PSO: Kp 12,48 / 10,10, Kd 34,69 / 36,70, Ki ≈ 0. Tope de salida ±255: al llegar, el integrador deja de acumular (anti-windup natural). En el piso: subida 0,8 / 1,4 s, error final 0,002 / 0,000 m/s, sin sobreimpulso significativo. Tesis, Sec. 4.4.3, 4.4.5 y Anexo de ecuaciones del PID.

R3 · El control se mantiene estable con holgura (lámina 38)

Lo probé de tres formas: un análisis discreto a 33 milisegundos sobre el modelo de cada rueda, un barrido de 625 combinaciones y la prueba real. El control se mantiene estable con holgura: tolera al menos 0,3 segundos de retardo extra, admite más de cuatro veces la ganancia sin oscilar y su sensibilidad queda en la zona recomendada, sin sobreimpulso.

Datos para preguntas (no se leen en voz alta): Análisis discreto a 33 ms sobre el modelo de cada rueda, con 0 y 0,1 s de retardo, más la prueba real a 0,13 m/s. Margen de retardo: 0,42 a 0,45 s sin retardo y 0,32 a 0,35 s con 0,1 s. Margen de ganancia: 38,9 a 39,4 dB sin retardo y 13,1 a 13,4 dB (≈4,5 veces) con 0,1 s. Margen de fase: 53° a 57° sin retardo y 41° a 44° con 0,1 s. Sensibilidad máxima Ms 1,35 a 1,85, dentro del rango típico de 1,2 a 2,0. Barrido de 625 combinaciones de ganancia del motor (0,1 a 10 veces) y constante de tiempo (0,05 a 3 s): sin retardo, las 625 son estables. Con 0,1 s se inestabilizan las de ganancia mayor que 4,4 veces (2,8 veces en la rueda izquierda si Ki se trata como lineal), 102 de 625. Son modelos lineales: no incluyen saturación, zona muerta ni aritmética entera, y no son una garantía global. Tesis, Sec. 4.4.3 y Anexo de estabilidad.

R4 · Sin IMU y sin costo extra, mapas a 3,4 cm del plano (lámina 39)

Sin sensor de giro, el ángulo sale de las ruedas, que al girar resbalan un poco: cerca de 3 por ciento por vuelta completa. El láser con SLAM Toolbox corrige ese desvío en vivo y deja los muros a 3,4 cm del plano real. Así el prototipo base no necesita hardware extra, y una IMU con filtro de Kalman queda como mejora al escalar a recintos grandes, como bodegas.

Datos para preguntas (no se leen en voz alta): Sin IMU el ángulo sale solo de las ruedas: 11,7° medios por vuelta de 360° (3,24 %, precisión 96,8 %), con repeticiones de 4,0° y 4,3°. SLAM Toolbox corrige ese desvío con el láser: muros a 3,4 cm del plano medido con cinta. Para escalar a recintos grandes: IMU + filtro de Kalman. Tesis, Sec. 3.4, 5.1 y 5.3.

R5 · L298N hoy y DRV8871 para una versión compacta (lámina 40)

El L298N resolvió el prototipo: es robusto, trae borneras, tiene más de cinco veces la corriente que piden los motores en marcha y cuesta unos 3 000 pesos. El TB6612FNG quedó descartado porque queda al límite de voltaje y en los picos de arranque. Para una versión más compacta, dos DRV8871 son la mejora natural: más eficientes, con menos calor y una etapa de potencia más pequeña.

Datos para preguntas (no se leen en voz alta): Consumo del motor JGA25-370: ~0,35 A en marcha y hasta 2,5 A al arrancar. Batería de 12,6 V. L298N: 2 A continuos por canal y 46 V. Frente a 0,35 A en marcha, más de 5 veces de holgura. Costo ≈ $3.000 CLP. TB6612FNG: 1,2 A continuos y 13,5 V recomendados frente a 12,6 V de la batería, al límite. Los picos de arranque superan su corriente continua. DRV8871: 3,6 A y 45 V, caída ≈0,2 V. Menos calor y etapa de potencia más pequeña. Fuentes: hojas de datos de ST, Toshiba y TI, y tesis (Anexo de costos).

R6 · Un margen de 15 cm abre paso por pasillos de 58 cm (lámina 41)

Los pasillos miden 58 cm. Con un margen de 15 cm por lado, el robot conserva paso libre y recorre todo el recinto. Si el margen fuera del tamaño de su esquina, las rutas se bloquearían. La próxima mejora es evaluar el contorno completo del robot al girar.

Datos para preguntas (no se leen en voz alta): Radio de inflado: 15 cm desde el centro del robot. La esquina del robot está a 24 cm del centro. Paso libre para el centro: 58 − 2 × 15 = 28 cm. Con 24 cm: 58 − 2 × 24 = 10 cm, y las rutas se bloquean. El planificador revisa el centro y no el contorno: el roce breve del video ocurre en este compromiso. Tesis, Sec. 4.5.4.

R7 · Software abierto probado y piezas clave propias (lámina 42)

Integré software abierto probado, como ROS 2, Nav2, SLAM Toolbox y Gazebo, y adapté cuatro proyectos abiertos, todos citados. Lo propio está en las piezas clave de ingeniería: el modelo URDF del robot real, el nodo del láser, la identificación de motores con PSO, el análisis de estabilidad y los protocolos de medición. Todo está publicado en el repositorio del proyecto.

Datos para preguntas (no se leen en voz alta): Los 4 proyectos adaptados (articubot_one, diffdrive_arduino, ROSArduinoBridge y explore_lite) se citan en la tesis. Código publicado con licencia MIT. Tesis, Introducción (Justificación) y Anexo de entorno de ejecución.

R8 · Repartir la carga protege el tiempo real (lámina 43)

El robot hace solo lo urgente y el portátil lo pesado. Así el tiempo real queda protegido en el Arduino y la Raspberry Pi 4, el cómputo pesado corre en un portátil de gama media sin encarecer el robot, y RViz2 permite supervisar en vivo por una red Wi-Fi dedicada, con IP fijas.

Datos para preguntas (no se leen en voz alta): ROS 2 Foxy con CycloneDDS. Red Wi-Fi dedicada con IP fijas. En el robot: Arduino Nano y Raspberry Pi 4 de 8 GB. En el portátil: SLAM Toolbox, Nav2 y el explorador. Tesis, Anexo de entorno de ejecución.

R9 · Los 5 mapas calzan con el plano real a 3,4 cm (lámina 44)

Superpuse los 5 mapas sobre el plano medido con cinta métrica, sin reescalarlos. La distancia media es de 3,4 cm, entre 3,1 y 3,7 por mapa: menos que una celda de 5 cm. La escala es real y el mapa sirve para levantar planos.

Datos para preguntas (no se leen en voz alta): 5 mapas alineados sobre el plano medido con cinta, sin reescalar. Distancia media 3,4 cm, entre 3,1 y 3,7 cm por mapa. Celda del mapa: 5 cm. Tesis, Sec. 5.3 y Anexo de comparación con el plano.

R10 · Plataforma: ganó ROS 2 (lámina 45)

ROS 1 depende de un nodo maestro: si cae, cae todo. YARP no trae mapeo ni navegación móvil. Orocos RTT es para control de brazos, sin mapeo 2D ni rutas. LCM solo transporta mensajes y obliga a programar todo desde cero. ROS 2 es distribuido y trae Nav2 y SLAM Toolbox listos para integrar.

Datos para preguntas (no se leen en voz alta): ROS 2 es distribuido y trae Nav2 y SLAM Toolbox listos para integrar. Tesis, Cap. 1 (Estado del arte) y tablas comparativas de plataformas.

R11 · Mapeo: ganó SLAM Toolbox (lámina 46)

GMapping no corrige el mapa al volver a un lugar conocido. Hector SLAM exige un láser más caro y deriva en recintos grandes. Cartographer es más difícil de ajustar y el que más CPU usa entre los métodos 2D comparados. SLAM Toolbox corrige el mapa al volver, lo guarda y corre en un portátil de gama media.

Datos para preguntas (no se leen en voz alta): SLAM Toolbox cierra lazos, guarda el mapa y es liviano. Cartographer es el que más CPU usa entre los métodos 2D comparados. Tesis, Cap. 1 (Estado del arte) y Sec. 1.4.

R12 · Navegación y exploración: ganaron A* + DWB y fronteras (lámina 47)

En navegación, RRT sirve más en espacios continuos o brazos, y en una grilla 2D A* es más directo. Pure Pursuit responde peor ante obstáculos cercanos y MPPI pide mucho más cómputo que DWB. En exploración, la ganancia de información y el SLAM activo agregan cálculo y complejidad sin beneficio en interiores planos. Las fronteras son livianas y usan directo el mapa.

Datos para preguntas (no se leen en voz alta): Navegar es trazar y seguir la ruta a una meta. Explorar es elegir la próxima meta. Tesis, Cap. 1 (Estado del arte) y tablas comparativas de navegación y exploración.

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
