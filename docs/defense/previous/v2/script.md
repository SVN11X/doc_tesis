# Guion de la defensa · Navegación y exploración autónoma de interiores

La presentación tiene 18 láminas visibles y 8 de respaldo ocultas, de la 19 a la 26.

## Inicio

Lámina 1 · Portada (35 s)
"Buenas tardes, y gracias a la comisión por su tiempo. Mi nombre es Sebastián Valderas y presento mi trabajo de titulación llamado Navegación y exploración autónoma de interiores utilizando un robot móvil de tracción diferencial, y fue guiado por el profesor Patricio Galarce. En pocas palabras, construí un robot que dibuja un mapa y lo explora por sí solo."

Lámina 2 · Estructura de la defensa (10 s)
"La presentación tiene cinco partes. De las cuales estan el Por qué construir un robot propio, qué me propuse lograr, cómo lo armé, qué tan bien funcionó y qué queda por hacer."

Lámina 3 · Separador 01 (5 s)
"Empiezo por el problema."

Lámina 4 · Un robot propio exige integrar 4 subsistemas (60 s)
"Que un robot se mueva solo dentro de una casa o una oficina no es un solo problema. Son cuatro, y hay que resolverlos a la vez. Percibir el entorno con un láser y con sensores en las ruedas, saber dónde está mientras dibuja el mapa, mover cada rueda a la velocidad pedida y decidir adónde ir y cómo llegar. Un robot comercial trae todo eso resuelto de fábrica, pero cerrado. Las piezas abiertas existen y cada una resuelve una parte. El trabajo está en integrarlas en un robot propio.

De ahí nace la pregunta central. ¿Es posible construir un prototipo de robot diferencial que, usando componentes accesibles y herramientas de código abierto, sea capaz de mapear, navegar y explorar entornos interiores de manera autónoma?"

Lámina 5 · Separador 02 (5 s)
"Para responderla, me propuse lo siguiente."

Lámina 6 · Un objetivo general y cuatro específicos (70 s)
"El objetivo general, tal como aparece en la tesis, es diseñar e implementar un prototipo de robot móvil de tracción diferencial de bajo costo, basado en ROS 2, capaz de construir un mapa 2D de su entorno mediante SLAM y navegar de forma autónoma hacia destinos por explorar, generados automáticamente por una estrategia de exploración de fronteras.

Los específicos son cuatro, y en palabras simples son estos. Construir el robot, probándolo antes en un robot virtual en el simulador Gazebo. Controlar las ruedas, es decir, medir cuánto avanza el robot y lograr que cada rueda gire a la velocidad pedida. Mapear y llegar a destino, con SLAM Toolbox y Nav2. Y explorar sin ayuda, con un método que elige solo la próxima zona por visitar.

El alcance son interiores de piso plano. Quedan fuera dos cosas, la navegación hacia metas fijas definidas por una persona y ubicarse en un mapa ya guardado."

Lámina 7 · Separador 03 (10 s)
"Veamos cómo lo hice. Trabajé por etapas. Primero probé el diseño en el robot virtual, y después llevé todo al robot real, donde hice todas las mediciones."

Lámina 8 · Control en el robot, mapeo en el PC (55 s)
"Este es el sistema completo, repartido en dos equipos. En el robot, el Arduino Nano mide cuánto gira cada rueda y controla su velocidad, y si deja de recibir órdenes detiene los motores. La Raspberry Pi 4 coordina el robot, calcula cuánto ha avanzado y lee el láser, un RPLidar A1. En el computador corre lo más exigente. SLAM Toolbox dibuja el mapa y ubica al robot en él, Nav2 traza la ruta y guía al robot, el explorador elige la próxima zona por visitar y RViz2 muestra todo en pantalla. Los dos equipos se comunican por ROS 2 en una red Wi-Fi propia."

Lámina 9 · El prototipo real (35 s)
"Este es el robot construido. El chasis está impreso en 3D en PLA+, a partir de un diseño abierto. Lo mueven dos motores de 12 volts con sensores que miden el giro de cada rueda, por arriba esta el láser. En la vista en planta se ve además un visualizador de tensión y corriente. Es un prototipo funcional, no un producto."

Lámina 10 · Cada pieza se eligió por ROS 2 y bajo costo (80 s)
"Esta tabla resume qué elegí y por qué. Todas las piezas funcionan en un computador modesto. Se eligio ROS 2, porque conecta los programas del robot sin depender de uno central y trae Nav2 para navegar. Usé la versión Foxy y la mantuve fija desde el inicio, porque todos los paquetes del robot funcionan con ella. Un láser 2D, porque es más barato y basta en interiores de piso plano. SLAM Toolbox, porque corrige el mapa cuando el robot vuelve a un lugar y lo puede guardar. Nav2, porque planifica directamente sobre el mapa que dibuja el robot. Gazebo, porque es compatible con el software base que adapté. Y la exploración por fronteras, porque elige metas mirando solo el mapa.

Abajo está mi aporte en el control. Medí cómo responde cada rueda y usé un algoritmo de optimización, el engambre por particula, para obtener un punto de partida de los tres valores del control a la vez, en vez de partir por prueba y error. El ajuste final lo hice en el robot real."

Lámina 11 · Separador 04 (5 s)
"Vamos a los resultados."

Lámina 12 · El robot mide bien su avance y explora sin ayuda (60 s)
"Estos cuatro números resumen el desempeño, y todos se midieron en el robot real. Primero, la odometría, que es cómo el robot calcula cuánto ha avanzado. En cinco rectas de dos metros se equivoca en 3.63 por ciento en promedio. Segundo, la velocidad. Pedí 0.13 metros por segundo y la diferencia con la velocidad real fue de 0.002 como máximo. Tercero, los mapas. Los muros quedan a 3.4 centímetros en promedio comparado con el recinto real, menos que el tamaño de una celda del mapa, que es de 5 centímetros. Y cuarto, cinco de seis exploraciones terminaron solas, sin zonas pendientes y sin que nadie interviniera. Es por ello que medir bien el avance y controlar cada rueda es la base para que los mapas calcen con el plano."

Lámina 13 · Cada exploración mapeó unos 3.5 m² de espacio libre (55 s)
"Paso a la exploración, el corazón del trabajo. Cada 3.3 segundos el explorador busca los bordes entre lo conocido y lo desconocido del mapa, que se llaman fronteras, elige uno y Nav2 lleva al robot hasta allí. Cuando ya no quedan fronteras, la exploración termina por sí sola. El gráfico muestra el espacio libre que mapeó cada exploración. Las barras azules quedan sobre el promedio y las verdes bajo él, pero entre la mayor y la menor hay solo 0.06 metros cuadrados. El eje del grafico parte en 3.40 para que esas diferencias se vean. El promedio es 3.50 metros cuadrados, con una variación de 0.8 por ciento, y por esa estabilidad el área libre es mi evidencia principal."

Lámina 14 · Misma área libre, distinto índice (45 s)
"Hay otro indicador, el índice de cobertura, que varía mucho más, entre 53 y 83 por ciento. Estos dos mapas reales explican por qué. En la leyenda, el blanco es espacio libre, el negro son muros y el gris es lo que quedó sin explorar. La exploración 1 tiene un índice de 82.9 por ciento y la 6, de 53.4, pero su área libre es casi igual, 3.51 y 3.48 metros cuadrados. Lo que cambia es cuánto gris queda dentro de la imagen. Por eso el índice depende de la imagen y no de lo que el robot mapeó."

Lámina 15 · El robot explora, traza su ruta y dibuja el mapa a la vez (35 s)
"Acá se ve todo funcionando junto en el robot real, en dos momentos de la exploración. En cada captura, a la izquierda está la cámara desde arriba, y a la derecha la misma escena en RViz2, con el mapa que crece y, en verde, la ruta que traza Nav2 hacia el borde de lo explorado."

Lámina 16 · La odometría se validó y lo demás se comprobó funcionando (80 s)
"Esta tabla resume el estado de cada parte, y quiero usar dos palabras con precisión. Validar es comparar con una medición externa. Comprobar es verificar que funciona en el robot. La odometría es lo único validado, porque la comparé con una distancia medida. El control de velocidad está comprobado en el robot y en el modelo. El SLAM funciona y sus mapas se compararon con el plano. La localización la resuelve SLAM Toolbox mientras dibuja el mapa. Y Nav2 y la exploración están comprobadas en funcionamiento.

Un dato que conviene leer bien. De las 60 metas, solo una figura como exitosa y 54 como abortadas. Abortada no significa que el robot falló. El explorador revisa su destino cada 3.3 segundos y, si encuentra uno mejor, manda una meta nueva antes de llegar a la anterior, y Nav2 registra la anterior como abortada. Así ocurrió en 53 de los 54 abortos. Por eso ese 1 de 60 no mide el éxito real. Para medirlo hacen falta metas fijas, que quedaron fuera del alcance."

Lámina 17 · Separador 05 (5 s)
"Para terminar, las conclusiones."

Lámina 18 · Mapear y explorar con bajo costo es posible (130 s)
"Cierro con tres ideas. Primero, los objetivos. Dos se cumplieron por completo, construir el robot y explorar sin ayuda. Los otros dos se cumplieron en parte. El control, porque lo probé a una sola velocidad y su estabilidad la comprobé solo en el modelo. Y la navegación, porque llevó al robot a las metas del explorador, pero todavía no tiene un indicador que la mida.

Segundo, el aporte. El firmware y la conexión con el hardware los adapté de proyectos abiertos que cito en la tesis. Lo propio es haber integrado y ajustado todo el sistema en hardware de bajo costo, con el control ajustado rueda por rueda en el robot real.

Tercero, lo que falta. Hice pocas repeticiones en un solo recinto pequeño, el cálculo del avance se desvía con el tiempo porque no hay sensor de giro, y el explorador cambia de meta sin cancelar la anterior. Ninguna de estas limitaciones invalida lo medido, pero acotan hasta dónde se puede generalizar. El trabajo futuro es medir la navegación con metas fijas en un recinto mayor, llegar a entre 6 y 10 repeticiones por ensayo, cancelar cada meta antes de reemplazarla, comparar con un PID incremental estándar, sumar un sensor de giro y migrar a una versión de ROS 2 con soporte vigente.

Y vuelvo a la pregunta del inicio. Para mapear y explorar el recinto ensayado, la respuesta es sí, con evidencia medida en el robot real. Con piezas accesibles y decisiones justificadas, la autonomía en interiores deja de ser una caja tan cerrada."

Lámina 19 · Gracias y preguntas (5 s)
"Muchas gracias. Quedo atento a sus preguntas y comentarios."

---

## Láminas de respaldo (ocultas)

Mapa rápido. Alternativas de plataforma y SLAM, 20. Simulación y robot real, 21. Control PI, 22. Estabilidad, 23. PSO, 24. Ajuste antes y después, 25. Plano medido, 26. Número de ensayos, 27. Metas fijas y mapa guardado, 28.

Para llegar a una oculta, escribe su número y presiona Enter.

Lámina 20 · ROS 2 y SLAM Toolbox frente a sus alternativas. Úsala si preguntan por qué no ROS 1, YARP u otro SLAM.

"Antes de construir, revisé qué existía. Arriba están las plataformas, el software que conecta los programas del robot. ROS 1 depende de un programa central, YARP no trae navegación propia, Orocos está pensado para tiempo real, sin mapa ni rutas, y LCM solo envía mensajes. Solo ROS 2 conecta sus programas sin uno central y trae Nav2. Abajo están las opciones de SLAM. GMapping no corrige el mapa al volver a un lugar, Hector SLAM necesita un láser muy rápido y Cartographer es complejo y exige más al computador. SLAM Toolbox corrige el mapa como Cartographer, pero exige menos y además lo guarda. Las piezas existen, y el reto fue integrarlas."

No digas que elegiste ROS 2 porque ROS 1 perdió soporte. Foxy también está fuera de soporte.

Lámina 21 · De la simulación al robot real. Úsala si preguntan por el robot virtual o por qué el control se midió solo en el robot real.

"A la izquierda está el robot virtual en el simulador Gazebo, con el mismo tamaño de ruedas y la misma distancia entre ellas que el robot real, y un láser equivalente, pero perfecto y sin ruido. A la derecha está el recinto real donde hice todas las pruebas. Son mundos distintos. El simulador sirvió para revisar el diseño antes de usar el robot físico, no para comparar mapas. Además, no reproduce bien el roce, la potencia mínima que necesita el motor para arrancar ni el ruido del láser, y en Gazebo las ruedas no pasan por el Arduino. Por eso el control de velocidad lo medí solo en el robot real."

Lámina 22 · El control de las ruedas funciona en la práctica como un PI. Observación 1 de la profesora Bárzaga.

"El control de las ruedas usa la fórmula que trae el firmware ROSArduinoBridge, sin cambiar su forma. Esa fórmula suma cada corrección a la salida anterior, y por eso cada valor cumple un papel distinto al que sugiere su nombre. Kp actúa como la parte integral, Kd como la parte proporcional y Ki como una segunda integración. No hay parte derivativa. En la práctica es un PI, una forma clásica de la familia PID, y por eso lo llamo así. Equivale a una ganancia proporcional de 0.41 y 0.40 y a un tiempo integral de 42 y 40 milisegundos, en la rueda izquierda y la derecha. La mantuve por tres razones. Es muy usada en robots móviles, el paquete diffdrive_arduino ya trabaja con ese firmware y su forma facilita que la parte integral no siga acumulando cuando el motor ya está al máximo. No la elegí comparándola con otras fórmulas, y esa comparación queda como trabajo futuro."

No digas que se comporta igual que un PID con otro escalamiento. La fórmula corre en el Arduino, no en ROS 2.
Ko divide la salida para llevarla a la escala del motor y es igual en ambas ruedas.
El OE2 queda parcial porque la estabilidad se revisó solo en el modelo y el desempeño se midió a una sola velocidad, no por el nombre PI. Eso está en la 23.

Lámina 23 · El control de velocidad es estable según el modelo. Observaciones 1 y 2 de la profesora Bárzaga.

"Revisé la estabilidad con el modelo de cada rueda, los valores finales del control y el ciclo del Arduino, de 33 milisegundos. El control es estable en ambas ruedas. Sin retraso adicional, el margen de fase, que indica cuánta holgura tiene el control, va de 53 a 57 grados, y el control tolera entre 0.42 y 0.45 segundos de retraso extra antes de volverse inestable. Probé además un caso con 0.1 segundos de retraso, porque mis mediciones se tomaban cada 0.1 segundos y no puedo descartar un retraso menor. Ahí el margen baja a entre 41 y 44 grados y sigue estable. La sensibilidad, que resume qué tan robusto es el control, queda entre 1.35 y 1.85, dentro del rango habitual de 1.2 a 2. Es un análisis sobre un modelo simplificado. No incluye el límite de potencia del motor, la potencia mínima para arrancar ni las velocidades bajas, y por eso el OE2 queda parcial."

El caso de 0.1 s es una prueba de sensibilidad, no un límite medido. No digas que el retraso real es cero ni que es menor que 0.1 s.

Lámina 24 · El PSO dio un punto de partida, no el ajuste final. Observación 3 de la profesora Bárzaga.

"El PSO es un algoritmo que prueba muchas combinaciones y se queda con la mejor. Lo usé para buscar los tres valores del control a la vez sobre el modelo de cada rueda. Propuso Kp de 12.48 y 10.10, Kd de 34.69 y 36.70 y Ki casi cero. Al cargarlos en el robot, la velocidad quedó bajo la pedida y el arranque fue lento. En el ajuste subí Kp entre 28 y 63 por ciento, bajé Kd entre 41 y 45 por ciento y subí Ki en varios órdenes de magnitud. Hubo que ajustar por tres causas. El modelo no incluye la potencia mínima que necesita el motor para arrancar ni los cálculos con números enteros del Arduino. La prueba del PSO usa un solo cambio de velocidad y no castiga el esfuerzo del motor. Y el algoritmo no limitó su resultado, así que el Kd que entregó supera el límite de 25 con que se evaluó. Aun así, los valores del PSO son estables, del mismo orden que los finales y se obtuvieron sobre la fórmula que de verdad se usa. Por eso su aporte fue un punto de partida."

Si piden ver cómo respondía el robot, salta a la 25.

Lámina 25 · El ajuste en el robot real corrigió el PSO. Complementa la 24.

"A la izquierda está la respuesta con los valores del PSO. La rueda izquierda queda unos 0.01 metros por segundo bajo la velocidad pedida, y la derecha se detiene cerca de 0.11 y recién la alcanza después de los seis segundos. El modelo no anticipaba ese error ni el arranque lento, porque no incluye la potencia mínima que necesita el motor para arrancar. Por eso subí Kp, que en esta fórmula acelera la corrección mientras dura el error, bajé Kd y subí Ki en la rueda izquierda. A la derecha está la respuesta con los valores finales. La diferencia queda en 0.002 metros por segundo como máximo, la detención desaparece y ambas ruedas llegan a la velocidad en menos de un segundo y medio. Con estos valores el control sigue estable en el modelo, aun con 0.1 segundos de retraso. El PSO fue el punto de partida, y el ajuste final se hizo en el robot real."

Lámina 26 · Los mapas quedan a 3.4 cm del plano medido. Observación 6 del profesor González.

"Que el área se repita no prueba que el mapa esté bien, porque un error que se repite en todas las pruebas no cambia el área. Por eso medí el recinto con huincha y armé un plano. Ubiqué cada mapa sobre el plano solo girándolo y moviéndolo, sin cambiar su tamaño, para que un error de escala se notara. Después tomé un punto cada centímetro a lo largo de los muros del plano y medí su distancia al muro más cercano del mapa, el mismo método que usan Trejos y otros. La distancia media es de 3.4 centímetros, entre 3.17 y 3.72 según la exploración, menos que una celda del mapa, de 5 centímetros. Las diferencias más grandes, de 6 a 9 centímetros, están en los tabiques cortos, que el mapa dibuja con pocas celdas. Y sumando los tres pasillos, el mapa sale 12 centímetros más ancho que el plano. El grosor de los muros explica como máximo 4 de esos centímetros. El resto puede venir de la huincha o del mapa, y estos datos no permiten separarlo."

No digas que los 5 cm de la celda son un límite del error. La tesis dice que no lo son.

Lámina 27 · Con cinco repeticiones, unas cifras son precisas y otras no. Observación 5 del profesor González.

"Para cada cifra calculé el rango en que estaría el valor real, con 95 por ciento de confianza. Con cinco repeticiones, las cifras que varían poco quedan precisas. El error de odometría queda entre 3.08 y 4.18 por ciento, el área libre entre 3.46 y 3.53 metros cuadrados y la distancia al plano entre 3.1 y 3.7 centímetros. En cambio, el índice de cobertura, de 46 a 78 por ciento, y el error de giro, de 1.8 a 21.6 grados, quedan poco precisos. Con cinco exploraciones completas de seis, solo puedo afirmar con 95 por ciento de confianza que la proporción supera el 36 por ciento. El control de velocidad se midió una vez con cada conjunto de valores, así que no tiene rango. Por eso la tesis habla de una comprobación en el recinto ensayado y no de una tasa de éxito. Lo recomendable serían entre 6 y 10 repeticiones válidas por ensayo, y eso es trabajo futuro."

No digas que los resultados están validados estadísticamente.

Lámina 28 · Las metas fijas y el mapa guardado quedaron fuera del alcance. Observación 4 del profesor González.

"No se hizo. Lo que compromete el objetivo general es navegar hacia los destinos que genera el explorador, y así se evaluó. Con esas metas, Nav2 llevó al robot 21.9 metros en 12.7 minutos, sin intervención. Una prueba con metas fijas exige definir las metas, marcarlas en el recinto con medidas y registrar por separado dónde terminó el robot, y esas mediciones no se hicieron. Por eso quedó fuera del alcance, y la tesis no informa una tasa de éxito ni el error al llegar. El programa para esa prueba quedó preparado, pero no tiene registros, no mide el error al llegar y sus metas solo existen en el simulador. AMCL, que sirve para ubicarse en un mapa ya guardado, está instalado con su configuración por defecto, pero no se ajustó ni se usó en las pruebas. La ubicación del robot la entregó SLAM Toolbox mientras dibujaba el mapa. Hacer esa prueba es el primer trabajo futuro."

Nunca digas que la comisión se confundió.
