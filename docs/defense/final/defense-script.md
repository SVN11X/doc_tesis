# Guion de la defensa v3 · Navegación y exploración autónoma de interiores

## Apertura

Lámina 1 · Portada (25 s)

Buenas dias, profesores. Muchas gracias por su tiempo. Mi nombre es Sebastián Valderas Neculqueo y presento mi trabajo de titulación de Ingeniería Civil Electrónica: Navegación y exploración autónoma de interiores utilizando un robot móvil de tracción diferencial, guiado por el profesor Patricio Galarce Acevedo. Antes de entrar en detalles, quiero mostrarles una premisa.

Lámina 2 · Video de demostración (65 s)

[El video parte solo al entrar a la lámina. Narrar con calma.] Lo que ven es un ensayo real del robot en el recinto de pruebas. A la izquierda está el robot que diseñé. A la derecha está lo que el computador interpreta en el moviemiento y su entorno. Fíjense en tres cosas. [CLIC] Primero, a medida que avanza, el láser de arriba detecta los muros y el mapa crece en pantalla. El borde morado y celeste es un margen de seguridad que el robot respeta junto a los muros. [CLIC] Segundo, la línea verde es la ruta que el robot calcula solo hacia las zonas grises, que todavía no conoce. Tercero, fíjense en la navegación y recuperación autónoma en pasillos estrechos de 58 cm, sin atascos ni intervención humana. Al final, el robot construyó solo el mapa del recinto. Ahora les explico qué problema resuelve, cómo lo construí y qué resultados medí.

Lámina 3 · Estructura (15 s)

La presentación tiene seis partes: el problema que aborda este trabajo, el estado del arte, los objetivos y el alcance, el diseño del sistema, los resultados medidos en el robot real y las conclusiones.

## 01 · Problema

Lámina 4 · Portada 01 · Problema (4 s)

Primero, el problema: para qué sirve y qué hay que resolver.

Lámina 5 · ¿Para qué sirve? (55 s)

¿Para qué sirve un prototipo de este tipo? [CLIC] Antes de inspeccionar o rescatar, una máquina debe localizarse, construir un mapa del lugar y decidir hacia dónde avanzar. [CLIC] La primera es el rescate en edificios dañados: en la liga RoboCup Rescue, los robots exploran y mapean de forma autónoma antes del ingreso de los rescatistas. [CLIC] La segunda, las plantas después de un accidente: en 2011, dos robots PackBot ingresaron a los reactores de Fukushima para medir radiación. [CLIC] La tercera, las zonas con gases o humo: el robot ExR-2 realiza rondas autónomas en plantas con atmósferas explosivas. Esa base común es la que desarrollé en este trabajo.

Datos para preguntas (no se leen en voz alta): RoboCup Rescue Robot League: el equipo Hector (TU Darmstadt) publicó su software de mapeo y navegación para ROS. En 2012, 3 de los 4 mejores equipos lo usaban. Los mapas se puntúan por completitud y exactitud. Fuente: Kohlbrecher et al., SSRR 2012. Hector SLAM nace de ese trabajo y la tesis lo compara en el Cap. 1 (R13). Fukushima Daiichi, abril de 2011: dos PackBot de iRobot ingresaron a las unidades 1 y 3, y al día siguiente a la 2. Midieron radiación, temperatura y oxígeno, operados a distancia. Fuente: IEEE Spectrum, 2011. ExR-2 de ExRobotics: certificado ATEX e IECEx zona 1 para atmósferas explosivas. Realiza rondas de inspección autónomas con LIDAR. Fuente: PC&NE, 30-06-2021. SmokeBot: proyecto Horizonte 2020 de la UE (CORDIS 645101), coordinado por la Universidad de Örebro. Radar 3D, cámara térmica y sensores de gases para baja visibilidad. Se demostró en un cuartel de bomberos de Dortmund. Los equipos de minería (Elios 3, Spot, Hovermap, Arkytas) están en la lámina 37, como horizonte del proyecto.

Lámina 6 · Mercado actual (45 s)

Este mercado ya existe, en dos niveles. [CLIC] En el nivel superior están los equipos de inspección y rescate. El PackBot se opera a distancia, el ExR-2 realiza rondas autónomas y SmokeBot apoya a bomberos. Son equipos especializados: un PackBot superaba los 125 000 dólares. [CLIC] En el otro extremo están los robots didácticos, como el TurtleBot 3, de 681 dólares. [CLIC] Este prototipo se ubica entre ambos: explora de forma autónoma un recinto desconocido y mide su desempeño, con un costo cercano al de un kit didáctico.

Datos para preguntas (no se leen en voz alta): PackBot 510: más de 125 000 USD por sistema, según un contrato de 2010 citado por IEEE Spectrum. ExR-2: sin precio público, se cotiza. SmokeBot: prototipo de investigación, no se vende. TurtleBot 3 Burger: 681 USD sin envío ni impuestos (ROBOTIS). Incluye IMU y motores con controlador integrados. Este prototipo no tiene IMU, por lo que no equivale exactamente al Burger. Materiales de este prototipo: 444 643 CLP, unos 462 USD (tesis, Anexo de costos).

Lámina 7 · Cuatro subsistemas (70 s)

Lograr que un robot sea autónomo no es resolver una sola pieza. Hay que hacer que cuatro subsistemas trabajen juntos. [CLIC] Primero, la percepción: medir la distancia a los muros con el láser y el giro de cada rueda con los encoders, que son sensores que cuentan las vueltas. [CLIC] Segundo, la localización y el mapeo: que el robot sepa dónde está mientras dibuja el plano. [CLIC] Tercero, el control de las ruedas: que cada rueda gire a la velocidad que se le pide. [CLIC] Y cuarto, la planificación y exploración: decidir adónde ir y cómo llegar con seguridad. Los equipos comerciales traen esto integrado y los proyectos abiertos suelen resolver piezas sueltas. Integrar las cuatro y medirlas en un robot real es el aporte. [CLIC] De ahí nace la pregunta central: ¿es posible construir un robot diferencial que, con componentes accesibles y herramientas de código abierto, mapee, navegue y explore interiores de forma autónoma?

## 02 · Estado del arte

Lámina 8 · Portada 02 · Estado del arte (4 s)

Segundo, cómo se resuelve hoy y cómo se compara este prototipo.

Lámina 9 · Estado del arte (60 s)

Revisé el estado del arte en esos cuatro subsistemas. [CLIC] La tracción diferencial usa dos ruedas con motor y una rueda pivote, y gira sobre su propio eje. Un automóvil no gira en el lugar y un omnidireccional es más complejo. [CLIC] En percepción predomina el LIDAR 2D, un láser que mide en 360 grados. La visión 3D da más datos, pero cuesta más cálculo y dinero. [CLIC] En mapeo, SLAM significa mapear y ubicarse al mismo tiempo. GMapping usa filtros de partículas y los métodos actuales, como SLAM Toolbox, corrigen el mapa al volver a un lugar conocido. [CLIC] En navegación dominan las arquitecturas modulares, como ROS 2 con Nav2, y la exploración por fronteras. [CLIC] La tendencia es clara: más capacidad trae más costo y complejidad. Cada elección de este trabajo busca lo suficiente para un interior plano.

Lámina 10 · Comparativa de valor (50 s)

Comparo ahora el valor, no solo el precio. [CLIC] A la izquierda, los robots de inspección y rescate. Al centro, el kit didáctico TurtleBot 3. A la derecha, este prototipo. [CLIC] En apertura, todo el prototipo se puede modificar. [CLIC] En autonomía, el PackBot se opera a distancia y el ExR-2 realiza rondas autónomas. Este prototipo explora de forma autónoma un lugar desconocido: 5 de 6 exploraciones terminaron sin intervención. [CLIC] En precisión, cuenta con un dato verificado: 3,4 cm respecto del plano real. [CLIC] En costo, los materiales suman unos 462 dólares, un 32 por ciento menos que el TurtleBot 3, que además incluye un sensor de giro.

Datos para preguntas (no se leen en voz alta): PackBot 510: más de 125 000 USD (contrato de 2010, IEEE Spectrum). ExR-2: rondas autónomas de inspección (PC&NE, 2021). TurtleBot 3 Burger: 681 USD sin envío ni impuestos. Prototipo: 444 643 CLP, unos 462 USD, un 32 % menos. 3,4 cm: distancia media de los muros del mapa al plano medido (tesis, Sec. 5.3).

## 03 · Objetivos

Lámina 11 · Portada 03 · Objetivos (4 s)

Tercero, qué me propuse y hasta dónde llega el trabajo.

Lámina 12 · Objetivos (55 s)

[CLIC] El objetivo general fue diseñar e implementar un robot diferencial de bajo costo, basado en ROS 2, que es el software estándar para robots, capaz de construir un mapa 2D mediante SLAM y de navegar solo hacia destinos que genera una estrategia de exploración de fronteras. [CLIC] Para lograrlo definí cuatro objetivos específicos. El primero, construir el robot y validarlo antes en un gemelo digital en el simulador Gazebo Classic. El segundo, controlar las ruedas: modelo de movimiento, odometría con encoders y control de velocidad en lazo cerrado. [CLIC] El tercero, mapear, ubicarse y navegar con SLAM Toolbox y Nav2. Y el cuarto, explorar sin ayuda, con metas que se generan automáticamente.

Lámina 13 · Alcance: contexto de trabajo (40 s)

Antes del diseño, el alcance del prototipo. [CLIC] Opera en interiores de piso plano, como los edificios y plantas de la lámina 6. [CLIC] Construye un mapa en dos dimensiones, una vista en planta, mientras se desplaza. [CLIC] Las metas las genera el propio sistema de exploración, sin intervención humana. [CLIC] El control de las ruedas se ejecuta a bordo y el mapeo, en un computador portátil conectado por una red Wi-Fi dedicada. [CLIC] La validación se hizo en dos etapas: primero en simulación y después en este recinto real, con pasillos y tabiques.

Datos para preguntas (no se leen en voz alta): Tesis, Introducción (Alcances y limitaciones): interiores de piso plano, RPLidar A1 y odometría por encoders. No orientado a exteriores, suelos irregulares ni obstáculos dinámicos rápidos. Fuera del alcance: metas fijas de un operador y localización sobre un mapa guardado con AMCL. Validez: un recinto de 3,50 m² de área libre y 5 exploraciones válidas. Los resultados son descriptivos. Red Wi-Fi dedicada con IP estáticas (Anexo de entorno de ejecución).

Lámina 14 · LIDAR 2D y oportunidades de mejora (50 s)

El sensor principal es un LIDAR 2D, sigla de Light Detection and Ranging: un sensor láser que mide distancias. [CLIC] Ciertas superficies también dificultan la medición: el espejo y el metal pulido desvían el haz, el vidrio lo deja pasar y las superficies muy oscuras lo absorben. [CLIC] La tesis plantea oportunidades de mejora concretas: una cámara 3D o térmica, una IMU, que es un sensor de giro y aceleración, recintos más amplios con metas fijas y una versión vigente de ROS 2. [CLIC] Es un contexto acotado y medido, con un camino claro de crecimiento.

Datos para preguntas (no se leen en voz alta): Sec. 3.3.1: el LIDAR 2D no detecta objetos fuera de su plano de barrido y se degrada ante superficies muy absorbentes o reflectantes. El vidrio es un ejemplo de superficie difícil, no un ensayo de la tesis. Sin IMU, cámara ni fusión sensorial (Introducción). El láser corrige la deriva de los giros (R4). ROS 2 Foxy y Gazebo Classic 11 ya no tienen soporte. La migración es trabajo futuro (Conclusiones).

## 04 · Diseño

Lámina 15 · Portada 04 · Diseño (4 s)

Cuarto, cómo lo construí y cómo funciona.

Lámina 16 · Prototipo construido (35 s)

Comienzo por el prototipo construido. [CLIC] Es compacto: 24,5 por 23 centímetros y 17,4 de altura. [CLIC] El chasis está impreso en 3D en PLA+, un plástico de impresión rígido. Usa tracción diferencial: dos ruedas motrices y una rueda de apoyo, lo que le permite girar sobre su propio eje. La alimentación está separada: 12 volts para los motores y 5 volts para la electrónica, para evitar interferencias. [CLIC] El costo de los materiales a bordo es de unos 462 dólares.

Datos para preguntas (no se leen en voz alta): Cotas del gemelo digital (Anexo): chasis de 24,5 × 23 cm y 17,4 cm de altura total. Radio de rueda 3,35 cm, separación entre ruedas 18,8 cm. Materiales a bordo: 444 643 CLP, unos 462 USD (Anexo de costos). El chasis toma como referencia una plataforma diferencial abierta (Sec. 4.1).

Lámina 17 · Componentes y su función (45 s)

Veamos cada componente. [CLIC] El LIDAR 2D es el sensor de distancia: mide en 360 grados. [CLIC] Los encoders son sensores de giro: miden cuánto gira cada rueda. [CLIC] Los motores de corriente continua son los actuadores, y el driver L298N les entrega la potencia de la batería. [CLIC] La Raspberry Pi 4 es el computador a bordo: ejecuta ROS 2 y se comunica con el portátil. [CLIC] El Arduino Nano es el controlador de bajo nivel: regula la velocidad de cada rueda cada 33 milisegundos. [CLIC] Elegí un LIDAR 2D por su bajo costo y porque es suficiente en interiores de piso plano.

Datos para preguntas (no se leen en voz alta): RPLidar A1: mide por triangulación y cubre 360°. Encoders de cuadratura: 1980 pulsos por vuelta (valor unificado). Motorreductores JGA25-370 de 12 V. Driver L298N (respaldo R5). La Raspberry Pi 4 ejecuta ROS 2 Foxy y calcula la odometría. El Arduino Nano ejecuta el control PI cada 33 ms. Tesis, Sec. 3.3, 4.1 y 4.3.

Lámina 18 · Arquitectura distribuida (60 s)

Estos componentes se distribuyen entre dos equipos. [CLIC] En el robot se ubica lo que requiere respuesta inmediata: el LIDAR mide distancias en 360 grados y los encoders miden el giro de cada rueda. [CLIC] El Arduino Nano regula la velocidad de cada rueda cada 33 milisegundos mediante un control PI, proporcional-integral. [CLIC] La Raspberry Pi 4 conecta todo mediante ROS 2 y calcula la odometría, es decir, el avance estimado a partir del giro de las ruedas. [CLIC] Ambos equipos se comunican por una red Wi-Fi dedicada. [CLIC] En un computador portátil se ubica lo que exige más cálculo. SLAM Toolbox construye el mapa y estima la posición del robot. [CLIC] Nav2, el sistema de navegación, calcula la ruta y las velocidades. [CLIC] El explorador elige la próxima meta. [CLIC] Y RViz2, el visualizador, muestra todo en pantalla.

Lámina 19 · ROS 2: red de nodos (60 s)

Los componentes se coordinan con ROS 2, sigla de Robot Operating System. ROS 2 organiza el robot como una red de programas llamados nodos, que publican datos en canales con nombre, llamados tópicos. Sigamos la información. [CLIC] El nodo del LIDAR publica las distancias a los obstáculos, y SLAM Toolbox las recibe. [CLIC] SLAM publica el mapa. [CLIC] El explorador analiza el mapa y entrega una meta. [CLIC] Nav2 calcula la velocidad necesaria para llegar a esa meta y la envía a la Raspberry Pi. [CLIC] La Raspberry Pi la convierte en la velocidad de cada rueda y la envía al Arduino, que ajusta la potencia de los motores. [CLIC] Los encoders informan la velocidad real y la Raspberry Pi calcula la odometría, que vuelve a SLAM. Así se cierra el ciclo. [CLIC] Cada nodo funciona de forma independiente: si uno se detiene, los demás continúan. Por eso elegí ROS 2.

Datos para preguntas (no se leen en voz alta): ROS 2 Foxy sobre Ubuntu 20.04, con rmw_cyclonedds_cpp (DDS) y ROS_DOMAIN_ID 0, igual en el robot y en el portátil (Anexo de entorno de ejecución). Tópicos: /scan (distancias del LIDAR), /map (mapa), /cmd_vel (velocidad pedida) y /odom (odometría). La meta del explorador llega a Nav2 como una acción de ROS 2. La Raspberry Pi ejecuta ros2_control con diffdrive_arduino y conversa con el Arduino por puerto serie USB. Tesis, Sec. 3.2 y 4.3.5. Alternativas: respaldos R10 y R11.

Lámina 20 · Gazebo: entorno virtual (40 s)

Antes de usar el hardware, validé el diseño en Gazebo, un modelo virtual, con el LIDAR simulado. [CLIC] se generaron mismas medidas, descritas en un archivo URDF, y el mismo software ROS 2. [CLIC] El método fue probar en Gazebo, corregir y luego llevarlo al robot real. [CLIC] La calibración final se realiza en el robot real, como se verá en la lámina 25.

Datos para preguntas (no se leen en voz alta): Gazebo Classic 11.11.0 con gazebo_ros_pkgs 3.5.3 (Anexo de entorno de ejecución). Se usa Gazebo Classic porque lo emplean los complementos de simulación y de ros2_control del paquete base, disponibles para ROS 2 Foxy (Cap. 2). La simulación no reproduce del todo fricción, zona muerta del driver, ruido ni latencias (Conclusiones). Tesis, Sec. 3.1.2 y 4.2.

Lámina 21 · Por qué un PI incremental (80 s)

Un punto central para nuestra especialidad es el control de velocidad de cada rueda. Cada 33 milisegundos, el Arduino ajusta la potencia sumando solo el cambio necesario. [CLIC] Un PID tradicional, posicional, recalcula la potencia total en cada ciclo, y su parte derivativa suele amplificar el ruido de los encoders. El PI incremental de este robot calcula solo el incremento de PWM y lo suma al valor anterior, con la acción proporcional sobre la medición. [CLIC] Lo elegí por tres razones. Primero, sin derivada no amplifica el ruido de los pulsos, y es el esquema probado en robótica móvil. Segundo, la referencia entra solo por la integral: no hay saltos al cambiar la consigna, y al llegar al tope de 255 deja de acumular, un anti-windup natural. Tercero, es liviano y ya viene integrado con diffdrive_arduino en ROS 2. [CLIC] En el robot real, a 0,13 m/s, las ruedas suben en 0,8 y 1,4 segundos, sin sobreimpulso, con error final de hasta 0,002 m/s y un margen de fase entre 41 y 57 grados.

Lámina 22 · Paso 1: medir revela que cada motor es único (40 s)

¿Cómo logré que cada rueda responda bien a su ejecucion? Con un método de cuatro pasos, automatizado en Python. El primero es medir. [CLIC] Sin controlador, Python aplica el mismo pulso de potencia a los dos motores y los encoders graban cómo acelera cada rueda. [CLIC] Al acercar la vista a la velocidad final aparece diferencias de valores.

Lámina 23 · Paso 2: un gemelo matemático por motor (40 s)

Segundo paso: con esa medición construyo un gemelo matemático de la señal obtenida. Python prueba miles de combinaciones hasta que la curva del gemelo calza con la medición real, como una ingeniería inversa. [CLIC] Captura su reacción: arranca casi al instante. [CLIC] Su rapidez: acelera en un tercio de segundo. [CLIC] Y su fuerza: cuánta velocidad entrega con la potencia aplicada. [CLIC] Lo mejor es que cada gemelo captura hasta la diferencia de fuerza entre ruedas. Desde aquí, cada prueba ocurre en el computador y el robot queda intacto.

Lámina 24 · Paso 3: la automatización calibra (40 s)

Tercer paso: dejar que la automatización calibre. [CLIC] El gemelo de cada motor corre con el mismo programa de control del Arduino. [CLIC] Una búsqueda automática evalúa miles de calibraciones y se queda con la que sigue mejor la velocidad pedida sin pasarse. [CLIC] El resultado es una calibración estable para cada rueda, lista para cargar sin riesgo. [CLIC] Y el proyecto gana tres cosas: calibra en el computador, saca lo mejor de motores económicos y se repite con los mismos scripts si mañana cambian motores o ruedas.

Datos para preguntas (no se leen en voz alta): La simulación corre a 30 Hz (período de 33 ms) con la misma ley PI incremental del firmware, sobre el modelo de cada rueda. 2.º PSO: 50 partículas × 150 generaciones = 7 500 evaluaciones por rueda. Costo: error cuadrático medio con peso 1 más sobreimpulso con peso 3. No penaliza el tiempo de subida ni el esfuerzo de control. Semilla entregada: Kp 12,48 / 10,10, Kd 34,69 / 36,70 (el costo evalúa Kd hasta 25), Ki ≈ 0,00001. La tesis no mide el tiempo de cómputo del PSO ni el de un ajuste manual. Por eso la lámina no da tiempos. Tesis, Sec. 4.4.5, Anexo de protocolos de sintonización y Anexo de resultados PSO.

Lámina 25 · Paso 4: ajuste final en el piso (45 s)

Cuarto paso: el toque final en el piso real. [CLIC] El piso aporta lo que ningún modelo simple ve: la fricción del suelo y la zona muerta del driver. Con eso reforcé el arranque y emparejé la respuesta de cada rueda. [CLIC] En gris, la calibración simulada. En color, el ajuste final, que llega antes y limpio a la meta. [CLIC] Ahora cada rueda alcanza la velocidad pedida en menos de un segundo y medio, cerca de un segundo antes y sin sobrepasarse. La simulación entrega la base estable y el piso aporta el toque final.

Datos para preguntas (no se leen en voz alta): Velocidad pedida: 0,13 m/s, misma prueba en el piso antes y después. Con el ajuste final: subida del 10 al 90 % en 0,8 s (izquierda) y 1,4 s (derecha), error final 0,002 y 0,000 m/s, sin sobreimpulso significativo. Margen de fase 41° a 57°. Con la semilla del PSO: la izquierda se queda en 0,12 m/s (error ≈0,01 m/s) y la derecha se detiene cerca de 0,11 m/s y se mantiene en la meta recién después de 6 s. La tesis resume: «la referencia se alcanza cerca de un segundo antes». Cambios: Kp sube 28 % y 63 % (a 16,00 y 16,42), Kd baja 41 % y 45 % (a 20,30 y 20,05), Ki izquierdo a 0,075 (el derecho, 0,001, no tiene efecto en la ley ejecutada). Zona muerta del driver L298N: con poca potencia el motor no gira. La resolución de la medición es 0,01 m/s, por eso la rueda izquierda muestra pequeños saltos. Por qué no «4× más rápido»: comparaba cuándo la rueda se queda en la meta (≈6 s) con el tiempo de subida (1,4 s), dos métricas distintas. Tesis, Sec. 4.4.5 (Refinamiento experimental), Sec. 5.2 y Tabla de indicadores de la respuesta al escalón.

Lámina 26 · Construcción del mapa (55 s)

Para construir el mapa se usa SLAM, sigla de localización y mapeo simultáneos: el robot construye el mapa y estima su posición al mismo tiempo. [CLIC] Mientras avanza, el LIDAR mide la distancia a los muros visibles. [CLIC] Al mismo tiempo, los encoders estiman cuánto avanzó y giró el robot: es la odometría. [CLIC] Como las ruedas pueden deslizar, SLAM Toolbox alinea cada nuevo barrido con los anteriores y corrige la odometría. Con eso actualiza una grilla de celdas de 5 cm: blanco libre, negro ocupado y gris sin explorar. [CLIC] Cuando el robot reconoce un lugar ya visitado, aplica un cierre de lazo y corrige el error acumulado. [CLIC] Elegí SLAM Toolbox porque corrige y guarda el mapa.

Datos para preguntas (no se leen en voz alta): Celdas de 0,05 m. SLAM Toolbox 2.4.1 en modo asíncrono. Tesis, Sec. 3.8 y 4.5.1. Alternativas: respaldos R12 y R13.

Lámina 27 · Navegación con Nav2 (45 s)

Con el mapa disponible, falta llegar a la meta sin colisionar. Esto lo resuelve Nav2, el sistema de navegación de ROS 2. [CLIC] Primero, Nav2 mantiene un margen de seguridad de 15 cm respecto de los muros, la zona morada del video. [CLIC] Luego, el algoritmo A estrella calcula la ruta global: recorre la grilla desde el robot hacia la meta y obtiene el camino más corto. Su función es análoga a la de un navegador GPS. [CLIC] Al avanzar, el controlador DWB evalúa varias trayectorias cortas y elige la más segura frente a obstáculos. [CLIC] Elegí A estrella y DWB porque son simples y suficientes en una grilla de interiores.

Datos para preguntas (no se leen en voz alta): Planificador global: NavFn con A* habilitado. Controlador local: DWB (Sec. 4.5.3). Radio de inflación de 0,15 m (Sec. 4.5.4). Tesis, Sec. 3.10. Alternativas: respaldos R14 y R15.

Lámina 28 · Exploración por fronteras (50 s)

¿Cómo decide el robot hacia dónde avanzar si no tiene un mapa previo ni una ruta? [CLIC] Una frontera es el borde entre la zona libre conocida, en blanco, y la desconocida, en gris. El explorador las identifica en el mapa en tiempo real. [CLIC] Una meta es un punto x, y sobre una frontera. El explorador la elige según la cercanía y el tamaño de la zona por descubrir. No se programa de antemano. [CLIC] Esa meta se entrega a Nav2, que conduce al robot como se vio en la lámina anterior. [CLIC] Cuando no quedan fronteras alcanzables, la exploración termina de forma automática. [CLIC] Elegí la exploración por fronteras porque es liviana y usa directamente el mapa.

Datos para preguntas (no se leen en voz alta): Explorador: explore_lite (proyecto m-explore), adaptado a este robot. Tesis, Sec. 3.11 y 4.5.6. Alternativas: respaldo R16.

## 05 · Resultados

Lámina 29 · Portada 05 · Resultados (4 s)

Quinto, lo que medí en el robot real.

Lámina 30 · En el robot real (65 s)

Todas las mediciones que presento se hicieron en el robot físico, en este recinto con pasillos y tabiques internos, pensado para exigir giros y espacios estrechos. Hice seis exploraciones completas. En la segunda el robot no generó mapa, así que la excluí de los promedios. [CLIC] En lo operativo, 5 de 6 exploraciones terminaron solas, deteniéndose al completar el mapa. En total, Nav2 condujo al robot 21,9 metros en 12,7 minutos, con navegación y recuperación autónoma en pasillos estrechos de 58 cm, sin atascos ni intervención humana. [CLIC] ¿Y qué tan fiel es el mapa? Al compararlo con un plano del recinto medido con cinta métrica, la diferencia media en la posición de los muros fue de 3,4 cm, menos que un cuadro del mapa, que mide 5. Además, el área libre mapeada fue muy estable: 3,50 m² en promedio, con una variación de solo 0,03.

Lámina 31 · Tres capas (55 s)

Tres capas sostienen esos mapas. [CLIC] La primera es el control estable que vimos: sin sobreimpulso y con margen de fase entre 41 y 57 grados. [CLIC] La segunda es una odometría repetible: en cinco rectas de 2 metros medidas con cinta métrica, el error medio fue de 3,63 por ciento. [CLIC] La tercera es el láser, que corrige los giros. En vueltas de 360° la desviación media fue de 11,7°, porque las ruedas patinan más al girar y no hay sensor de giro. SLAM Toolbox realinea los muros en vivo. [CLIC] El resultado es un plano fiel al real, a 3,4 cm. [CLIC] ¿Y si la odometría falla? SLAM corrige la deriva, pero necesita una base estable: mejor control y odometría significan menos corrección y mapas más firmes.

Lámina 32 · Mapas repetibles (65 s)

[CLIC] Este gráfico muestra el área libre mapeada en las cinco exploraciones válidas. El eje parte en 3,40 para que se vean las diferencias: entre la mayor y la menor hay solo 0,06 m². [CLIC] A la derecha están la exploración 1 y la 6. Su índice de cobertura es de 83 y 53 por ciento, lo que podría parecer inconsistente, pero mapearon casi la misma superficie: 3,51 y 3,48 m². [CLIC] De aquí salen dos lecturas. Primero, confiabilidad operativa: con 3,50 ± 0,03 m², el robot mapea el recinto completo igual en cada ejecución. Segundo, el índice no indica error: solo mide qué parte de la imagen es espacio libre, y cada imagen incluye más o menos gris de afuera según cómo quedó orientado el mapa. La evidencia del mapeo es el área y la comparación con el plano real.

Lámina 33 · Navegación adaptativa (60 s)

Al revisar los registros de navegación apareció algo que conviene explicar bien. [CLIC] El robot avanza hacia una meta A. [CLIC] El explorador revisa el mapa cada 3,3 segundos, y aquí el láser descubre una zona mayor. [CLIC] Entonces envía una meta B, mejor, sin cancelar la anterior. [CLIC] Esta versión de Nav2 anota ese reemplazo como «abortado», aunque el robot nunca se detuvo: cambió de destino mientras avanzaba, buscando más mapa en menos recorrido. [CLIC] Por eso, de 60 metas, 54 figuran como abortadas, pero 53 coinciden justo con la llegada de la meta siguiente. Soy cuidadoso en esto: el registro no permite descartar otras causas caso a caso, y por eso no lo uso como tasa de éxito. La síntesis es que los cuatro subsistemas funcionaron juntos en el robot real.

## 06 · Conclusiones

Lámina 34 · Portada 06 · Conclusiones (4 s)

Y para cerrar, qué se logró y qué sigue.

Lámina 35 · Cumplimiento de objetivos (65 s)

Reviso ahora los cuatro objetivos específicos. [CLIC] El primero, construir el robot y su gemelo digital, está logrado y verificado antes en Gazebo Classic. [CLIC] El segundo, el control de las ruedas, está logrado en lo ensayado: encoders, odometría y un control PI estable a 0,13 m/s. En la tesis lo marqué parcial porque lo evalué en un solo punto de operación. El próximo paso es probar otras velocidades. [CLIC] El tercero, mapear, ubicarse y navegar, también está logrado en lo ensayado: mapas a 3,4 cm del plano y 21,9 metros autónomos. Lo marqué parcial porque las metas fijas quedaron fuera del alcance. [CLIC] Y el cuarto, explorar sin ayuda, está logrado: la exploración terminó sola en 5 de 6 ensayos. El objetivo general se cumple en lo funcional. Las marcas de parcial son una decisión de rigor, para no inflar los indicadores.

Lámina 36 · De prototipo a solución de campo (55 s)

Si quisiera llevar esto a una solución de campo, el precio no basta. La pregunta es qué ya está demostrado y qué falta. [CLIC] La etapa 1 es la base demostrada hoy: mapas a 3,4 cm del plano, 21,9 metros autónomos, 5 de 6 exploraciones cerradas solas y una plataforma abierta. [CLIC] La etapa 2 es el escalamiento técnico: sensor de giro, recintos amplios y metas fijas con 6 a 10 repeticiones. [CLIC] Y la etapa 3 sería la aplicación de campo: sensores de gases, temperatura o láser 3D, un chasis industrial y una versión vigente de ROS 2. Las etapas 2 y 3 son una propuesta. La cadena completa de autonomía ya está medida, y cada brecha se puede cerrar sobre esta misma base. Esa etapa 3 apunta a un horizonte concreto, que muestro ahora.

Lámina 37 · Horizonte: minería (40 s)

Por último, el horizonte de crecimiento. [CLIC] Las mismas capacidades, localización, mapeo y decisión autónoma, se aplican hoy en minería, el entorno más exigente. [CLIC] En El Teniente, Codelco usa un dron con láser que realiza en cinco minutos una inspección que antes tomaba medio día. [CLIC] Los robots Spot y ANYmal ya recorren instalaciones de Glencore y Vale. [CLIC] Y Hovermap realiza mapeo 3D en más de treinta minas. [CLIC] Para llegar a ese nivel, los próximos pasos son una IMU, un LIDAR 3D, sensores de inspección y un chasis robusto. La base ya está demostrada.

Datos para preguntas (no se leen en voz alta): Codelco (27-03-2026): en El Teniente, el dron Elios 3 realiza en 5 minutos una inspección que tomaba medio día. Mining Technology (23-07-2025): Spot y ANYmal operan en instalaciones de Glencore y Vale. CSIRO (2025): Hovermap, de Emesent, mapea en 3D sin GPS en más de 30 minas. Reporte Minero (27-02-2026): Arkytas, de Kinamics, inspecciona frentes en El Teniente operado a distancia. Las etapas 2 y 3 de la lámina 36 son una propuesta de la tesis (Trabajo futuro).

Lámina 38 · Aporte de ingeniería (40 s)

[CLIC] El aporte de ingeniería es la integración completa y publicada: hardware, firmware, modelo URDF y scripts abiertos para replicar y mejorar la plataforma. El firmware y la interfaz del Arduino se adaptaron de proyectos abiertos, debidamente citados. [CLIC] El gemelo digital parametrizado permite probar algoritmos o cambios físicos en simulación antes de tocar el robot, ahorrando tiempo y daños. [CLIC] La sintonización automatizada por rueda calibra motores económicos distintos de forma repetible, sin partir a ciegas. [CLIC] Y la estabilidad del control quedó verificada: las ruedas responden sin oscilar, aun con retardos del sistema.

Lámina 39 · Conclusión (50 s)

[CLIC] Vuelvo a la pregunta del inicio. Sí: es viable construir un robot diferencial de bajo costo que mapea, navega y explora interiores de forma autónoma, y lo respaldo con mediciones en el robot real. [CLIC] Todo el trabajo está publicado en nuestro repositorio de GitHub, ros2-indoor-exploration-robot: código ROS 2, firmware, piezas 3D y scripts de ajuste, con licencia MIT, listo para docencia o para sumar sensores de inspección. [CLIC] Me quedo con tres ideas. Un control de ruedas bien ajustado sostiene mapas fieles. Repartir el trabajo entre el robot y el computador hace viable la autonomía con hardware accesible. Y la evidencia está medida en hardware real.

Lámina 40 · Gracias (5 s)

Muchas gracias por su atención. Quedo atento a sus preguntas y comentarios. [Para mostrar un respaldo: clic en «Respaldo», abajo a la derecha, y elegir el tema.]

## Láminas de respaldo

Están ocultas: no aparecen al avanzar. Para abrir una, haz clic en «Respaldo» en la lámina 40, o escribe 41 y Enter para ir al índice. Cada respaldo tiene «Volver al índice» y una animación corta que parte sola al abrirlo. El glosario (lámina 58) se abre con el botón «Glosario» de cada lámina, y su botón «Volver» regresa a la lámina desde donde se abrió.

| Lámina | Código | Grupo | Tema |
|---|---|---|---|
| 41 | Índice | | Láminas de respaldo |
| 42 | R1 | Control | El robot corrige sus ruedas 30 veces por segundo |
| 43 | R2 | Control | El lazo deja de acumular al tope y cada rueda tiene su calibración |
| 44 | R3 | Control | El control se mantiene estable con holgura |
| 45 | R4 | Control | Sin IMU y sin costo extra, mapas a 3,4 cm del plano |
| 46 | R5 | Hardware | L298N hoy y DRV8871 para una versión compacta |
| 47 | R6 | Hardware | Un margen de 15 cm abre paso por pasillos de 58 cm |
| 48 | R7 | Proyecto | Software abierto probado y piezas clave propias |
| 49 | R8 | Proyecto | Repartir la carga: buenas prácticas y ventajas |
| 50 | R9 | Resultados | Los 5 mapas calzan con el plano real a 3,4 cm |
| 51 | R10 | Alternativas | ROS 2 frente a ROS 1 |
| 52 | R11 | Alternativas | YARP, Orocos RTT y LCM |
| 53 | R12 | Alternativas | SLAM Toolbox frente a GMapping |
| 54 | R13 | Alternativas | Hector SLAM y Cartographer |
| 55 | R14 | Alternativas | A* frente a RRT |
| 56 | R15 | Alternativas | DWB frente a Pure Pursuit y MPPI |
| 57 | R16 | Alternativas | Fronteras frente a ganancia de información y SLAM activo |
| 58 | Glosario | | Términos y siglas |

## Respuestas breves

R1 · El robot corrige sus ruedas 30 veces por segundo (lámina 42)

Cada 33 milisegundos, es decir, 30 veces por segundo, el Arduino repite cuatro pasos: mide la velocidad con los encoders, la compara con la pedida, calcula un ajuste pequeño y lo suma a la potencia que el motor ya tenía. Mientras hay error, la potencia sube un poco en cada ciclo. Cuando el error llega a cero, se mantiene sin caer. Por eso corrige de forma suave, sin tirones.

Datos para preguntas (no se leen en voz alta): Ciclo de control de 33 ms en el Arduino Nano, unas 30 veces por segundo. Ley incremental: PWM nuevo = PWM anterior + corrección. La salida se limita a ±255 y el integrador deja de acumular en el tope. Tesis, Sec. 4.4.3.

R2 · Protección anti-saturación y calibración por rueda (lámina 43)

Cada 33 milisegundos, el controlador de cada rueda compara la velocidad pedida con la medida, ignora errores mínimos mediante una banda muerta, suma un ajuste pequeño a la potencia anterior y la limita a más o menos 255 unidades de PWM, la modulación por ancho de pulso. Si la potencia alcanza ese límite, el acumulador deja de crecer: es la protección anti-saturación, que evita sobreimpulsos al salir de la saturación. Cada rueda tiene su propia calibración: la izquierda presentaba un error estacionario y recibió más acción integral, la derecha no. Ambas requirieron una mayor ganancia de arranque por la zona muerta del driver. Resultado: alcanzan la velocidad pedida en menos de 1,5 segundos, sin sobreimpulso.

Datos para preguntas (no se leen en voz alta): Ley ejecutada (Sec. 4.4.3): incremento = (Kp·error − Kd·cambio de la medición + estado integral) ÷ Ko. El estado integral solo se actualiza si la salida sin limitar es menor que 255 en valor absoluto. Salida = límite ±255 de la salida anterior más el incremento. Banda muerta sobre el error: 2 pulsos por ciclo en la rueda izquierda y 1 en la derecha (Anexo). Ganancias finales, izquierda / derecha: Kp 16,00 / 16,42, Kd 20,30 / 20,05, Ki 0,075 / 0,001, Ko 50. Sin Ki equivalen a un PI con ganancia proporcional 0,41 / 0,40 PWM por pulso por ciclo. Semilla del PSO: Ki casi nulo y Kp y Kd cercanos a 11 y 35. En el piso: Ki izquierdo a 0,075 por error estacionario, Kp sube por la zona muerta del driver, Kd baja porque la velocidad medida viene cuantizada. El gráfico es un esquema ilustrativo, no una medición. Tesis, Sec. 4.4.3, 4.4.5 y Anexo de ecuaciones del controlador.

R3 · El control se mantiene estable con holgura (lámina 44)

Lo probé de tres formas: un análisis discreto a 33 milisegundos sobre el modelo de cada rueda, un barrido de 625 combinaciones y la prueba real. El control se mantiene estable con holgura: tolera al menos 0,3 segundos de retardo extra, admite más de cuatro veces la ganancia sin oscilar y su sensibilidad queda en la zona recomendada, sin sobreimpulso.

Datos para preguntas (no se leen en voz alta): Análisis discreto a 33 ms sobre el modelo de cada rueda, con 0 y 0,1 s de retardo, más la prueba real a 0,13 m/s. Margen de retardo: 0,42 a 0,45 s sin retardo y 0,32 a 0,35 s con 0,1 s. Margen de ganancia: 38,9 a 39,4 dB sin retardo y 13,1 a 13,4 dB (≈4,5 veces) con 0,1 s. Margen de fase: 53° a 57° sin retardo y 41° a 44° con 0,1 s. Sensibilidad máxima Ms 1,35 a 1,85, dentro del rango típico de 1,2 a 2,0. Barrido de 625 combinaciones de ganancia del motor (0,1 a 10 veces) y constante de tiempo (0,05 a 3 s): sin retardo, las 625 son estables. Con 0,1 s se inestabilizan las de ganancia mayor que 4,4 veces (2,8 veces en la rueda izquierda si Ki se trata como lineal), 102 de 625. Son modelos lineales: no incluyen saturación, zona muerta ni aritmética entera, y no son una garantía global. Tesis, Sec. 4.4.3 y Anexo de estabilidad.

R4 · Sin IMU y sin costo extra, mapas a 3,4 cm del plano (lámina 45)

Sin sensor de giro, el ángulo sale de las ruedas, que al girar resbalan un poco: cerca de 3 por ciento por vuelta completa. El láser con SLAM Toolbox corrige ese desvío en vivo y deja los muros a 3,4 cm del plano real. Así el prototipo base no necesita hardware extra, y una IMU con filtro de Kalman queda como mejora al escalar a recintos grandes, como bodegas.

Datos para preguntas (no se leen en voz alta): Sin IMU el ángulo sale solo de las ruedas: 11,7° medios por vuelta de 360° (3,24 %, precisión 96,8 %), con repeticiones de 4,0° y 4,3°. SLAM Toolbox corrige ese desvío con el láser: muros a 3,4 cm del plano medido con cinta. Para escalar a recintos grandes: IMU + filtro de Kalman. Tesis, Sec. 3.4, 5.1 y 5.3.

R5 · L298N hoy y DRV8871 para una versión compacta (lámina 46)

El L298N resolvió el prototipo: es robusto, trae borneras, tiene más de cinco veces la corriente que piden los motores en marcha y cuesta unos 3 000 pesos. El TB6612FNG quedó descartado porque queda al límite de voltaje y en los picos de arranque. Para una versión más compacta, dos DRV8871 son la mejora natural: más eficientes, con menos calor y una etapa de potencia más pequeña.

Datos para preguntas (no se leen en voz alta): Consumo del motor JGA25-370: ~0,35 A en marcha y hasta 2,5 A al arrancar. Batería de 12,6 V. L298N: 2 A continuos por canal y 46 V. Frente a 0,35 A en marcha, más de 5 veces de holgura. Costo ≈ $3.000 CLP. TB6612FNG: 1,2 A continuos y 13,5 V recomendados frente a 12,6 V de la batería, al límite. Los picos de arranque superan su corriente continua. DRV8871: 3,6 A y 45 V, caída ≈0,2 V. Menos calor y etapa de potencia más pequeña. Fuentes: hojas de datos de ST, Toshiba y TI, y tesis (Anexo de costos).

R6 · Un margen de 15 cm abre paso por pasillos de 58 cm (lámina 47)

Los pasillos miden 58 cm. Con un margen de 15 cm por lado, el robot conserva paso libre y recorre todo el recinto. Si el margen fuera del tamaño de su esquina, las rutas se bloquearían. La próxima mejora es evaluar el contorno completo del robot al girar.

Datos para preguntas (no se leen en voz alta): Radio de inflado: 15 cm desde el centro del robot. La esquina del robot está a 24 cm del centro. Paso libre para el centro: 58 − 2 × 15 = 28 cm. Con 24 cm: 58 − 2 × 24 = 10 cm, y las rutas se bloquean. El planificador revisa el centro y no el contorno: el roce breve del video ocurre en este compromiso. Tesis, Sec. 4.5.4.

R7 · Software abierto probado y piezas clave propias (lámina 48)

Integré software abierto probado, como ROS 2, Nav2, SLAM Toolbox y Gazebo, y adapté cuatro proyectos abiertos, todos citados. Lo propio está en las piezas clave de ingeniería: el modelo URDF del robot real, el nodo del láser, la identificación de motores con PSO, el análisis de estabilidad y los protocolos de medición. Todo está publicado en el repositorio del proyecto.

Datos para preguntas (no se leen en voz alta): Los 4 proyectos adaptados (articubot_one, diffdrive_arduino, ROSArduinoBridge y explore_lite) se citan en la tesis. Código publicado con licencia MIT. Tesis, Introducción (Justificación) y Anexo de entorno de ejecución.

R8 · Reparto de cómputo: buenas prácticas y ventajas (lámina 49)

El robot ejecuta solo las tareas inmediatas y el computador portátil, las de mayor cálculo. Se aplican buenas prácticas de ingeniería: el control en tiempo real de las ruedas está separado del cómputo del mapa, la red es una Wi-Fi dedicada con direcciones IP fijas, la comunicación usa ROS 2 con DDS y la supervisión con RViz2 está separada de la ejecución. Las ventajas son prácticas: menor costo, peso y consumo a bordo, los picos de cómputo del SLAM no afectan el control de las ruedas, la depuración se hace en vivo y el portátil se puede reemplazar por un computador embebido sin rehacer el robot.

Datos para preguntas (no se leen en voz alta): ROS 2 Foxy con CycloneDDS, ROS_DOMAIN_ID 0, misma distribución en ambos equipos. Red Wi-Fi dedicada con IP estáticas. En el robot: Arduino Nano y Raspberry Pi 4. En el portátil (Intel Core i7-10610U, 32 GB): SLAM Toolbox, Nav2, el explorador y RViz2. Las ventajas son de diseño: la tesis no mide consumo ni carga de cómputo (Cap. 5). Tesis, Anexo de entorno de ejecución.

R9 · Los 5 mapas calzan con el plano real a 3,4 cm (lámina 50)

Superpuse los 5 mapas sobre el plano medido con cinta métrica, sin reescalarlos. La distancia media es de 3,4 cm, entre 3,1 y 3,7 por mapa: menos que una celda de 5 cm. La escala es real y el mapa sirve para levantar planos.

Datos para preguntas (no se leen en voz alta): 5 mapas alineados sobre el plano medido con cinta, sin reescalar. Distancia media 3,4 cm, entre 3,1 y 3,7 cm por mapa. Celda del mapa: 5 cm. Tesis, Sec. 5.3 y Anexo de comparación con el plano.

R10 · ROS 2 frente a ROS 1 (lámina 51)

ROS 1 depende de un nodo maestro central: cada módulo se registra en él para encontrar a los demás, y si el maestro se detiene, los módulos ya no pueden encontrarse. ROS 2 es distribuido: con DDS, sigla de Data Distribution Service, cada módulo descubre a los demás por la red, sin un centro. Por eso no tiene un punto único de falla, e incluye Nav2 y SLAM Toolbox.

Datos para preguntas (no se leen en voz alta): La tesis elige ROS 2 por su arquitectura distribuida sin nodo maestro y por su ecosistema de mapeo, navegación y exploración. El fin de soporte de ROS 1 no se usa como criterio, porque ROS 2 Foxy también está fuera de soporte. Tesis, Cap. 1 (Plataformas y middleware) y Cap. 2 (Selección de tecnologías).

R11 · YARP, Orocos RTT y LCM (lámina 52)

Las tres alternativas resuelven una parte del problema. YARP conecta módulos y abstrae dispositivos, Orocos RTT realiza control determinista por componentes y LCM es una mensajería de baja latencia. Ninguna incluye mapeo ni navegación para un robot móvil: esas partes habría que programarlas desde cero. ROS 2 las incluye con SLAM Toolbox y Nav2.

Datos para preguntas (no se leen en voz alta): YARP: sin pila propia de navegación móvil. Orocos RTT: no distribuye módulos de mapeo ni de planificación. LCM: no incluye percepción, mapeo ni navegación. Tesis, Cap. 1, tabla de plataformas y middleware.

R12 · SLAM Toolbox frente a GMapping (lámina 53)

GMapping es un filtro de partículas: mantiene muchas hipótesis de la trayectoria, cada una con su propio mapa. Depende de una odometría consistente y no tiene cierre de lazo. SLAM Toolbox construye un grafo de poses: relaciona cada barrido con los anteriores mediante una red y, al volver a un lugar conocido, cierra el lazo y corrige todo el mapa. Además guarda el mapa y está integrado con ROS 2.

Datos para preguntas (no se leen en voz alta): GMapping: buen desempeño en tiempo real y memoria acotada en escenas pequeñas, pero sin cierre de lazo y con menor portabilidad a ROS 2. SLAM Toolbox: en modo asíncrono puede omitir mediciones si el procesamiento de la anterior se retrasa. Tesis, Cap. 1 (Percepción y mapeo) y Sec. 3.8.

R13 · Hector SLAM y Cartographer (lámina 54)

Hector SLAM alinea cada barrido con el anterior, casi sin usar la odometría, pero requiere un LIDAR de alta frecuencia y presenta deriva en recintos extensos. Cartographer, de Google, construye submapas y los optimiza en conjunto, con buena consistencia global, pero es más difícil de ajustar y, en una comparación independiente de cinco métodos 2D, fue el de mayor uso de CPU.

Datos para preguntas (no se leen en voz alta): Hector SLAM nace del equipo Hector de RoboCup Rescue (lámina 5). Tesis, Cap. 1, tabla de alternativas de SLAM 2D.

R14 · A* frente a RRT (lámina 55)

A estrella recorre la grilla del mapa desde el robot hacia la meta, sumando lo recorrido y una estimación de lo que falta, y obtiene el camino más corto. Opera directamente sobre el mapa de ocupación y replanifica con bajo costo. RRT, sigla de Rapidly-exploring Random Tree, genera ramas aleatorias en el espacio hasta alcanzar la meta. Es más adecuado para espacios continuos de muchas dimensiones o con restricciones de movimiento, como un brazo robótico.

Datos para preguntas (no se leen en voz alta): En Nav2 se usa el planificador NavFn con A* habilitado (Sec. 4.5.3). Tesis, Cap. 1 (Navegación y exploración) y Sec. 3.10.

R15 · DWB frente a Pure Pursuit y MPPI (lámina 56)

DWB evalúa un conjunto de trayectorias posibles según la velocidad actual y elige la mejor, lejos de los obstáculos. Es habitual en robots diferenciales por su bajo costo y su buena respuesta ante obstáculos cercanos. Pure Pursuit sigue un punto ubicado más adelante sobre la ruta: es más simple, pero responde peor ante obstáculos imprevistos. MPPI simula cientos de trayectorias futuras considerando la dinámica del robot, a costa de mucho más cómputo.

Datos para preguntas (no se leen en voz alta): Nav2 permite combinar planificadores como NavFn y Smac con controladores como DWB, Regulated Pure Pursuit y MPPI. Tesis, Cap. 1 (Navegación y exploración).

R16 · Fronteras frente a ganancia de información y SLAM activo (lámina 57)

La exploración por fronteras dirige al robot al borde entre lo conocido y lo desconocido. Es liviana y usa directamente el mapa de ocupación con Nav2. La ganancia de información puntúa cada candidato según cuánto podría observarse desde ahí, pero requiere modelos y cálculos adicionales. El SLAM activo elige rutas que también mejoran el mapa y la localización: toma decisiones más informadas, con mucho más cómputo.

Datos para preguntas (no se leen en voz alta): Explorador usado: explore_lite (proyecto m-explore), port a ROS 2. Tesis, Cap. 1 (Exploración autónoma) y Cap. 2 (Selección de tecnologías).

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
- **Nodo:** un programa de ROS 2 con una sola tarea, como ver, mapear o navegar.
- **Tópico:** un canal con nombre donde un nodo publica mensajes y otros los escuchan.
- **DDS:** el estándar de comunicación que usa ROS 2 para que los nodos se encuentren solos en la red.
- **Anti-saturación:** cuando la potencia llega al tope, el controlador deja de acumular error para no pasarse después.
- **RRT:** planificador que lanza ramas al azar hasta tocar la meta. Sirve en espacios continuos de muchas dimensiones.
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
