# Guion de la defensa v3 · Navegación y exploración autónoma de interiores

Va con `slides-v3.pptx`: 24 láminas visibles y 18 ocultas (un índice y 17 respaldos, de la 25 a la 42). El mismo texto está en las notas del orador de cada lámina, para leerlo en la vista del moderador.

Cada `[CLIC]` hace aparecer la parte siguiente de la lámina. El número de clics de cada lámina coincide con sus marcas. El video de la lámina 2 parte solo al entrar.

Duración estimada de la narración: 24 min 30 s a 130 palabras por minuto. Con pausas naturales queda entre 25 y 27 minutos, bajo el límite de 30.

## Apertura

Lámina 1 · Navegación y exploración autónoma de interiores utilizando un robot móvil de tracción diferencial (25 s)

Buenas tardes, profesores. Muchas gracias por su tiempo. Mi nombre es Sebastián Valderas Neculqueo y presento mi trabajo de titulación de Ingeniería Civil Electrónica: Navegación y exploración autónoma de interiores utilizando un robot móvil de tracción diferencial, guiado por el profesor Patricio Galarce Acevedo. Antes de entrar en detalles, quiero mostrarles qué hace este robot.

Lámina 2 · ¿Qué logra este prototipo? (60 s)

[El video parte solo al entrar a la lámina. Narrar con calma.] Lo que ven es un ensayo real en el recinto de pruebas. A la izquierda está el robot que diseñé y construí, moviéndose sin control remoto. A la derecha está lo que el computador interpreta en ese momento. Fíjense en tres cosas. Primero, a medida que avanza, el láser de arriba detecta los muros y el mapa crece en pantalla. Segundo, la línea verde es la ruta que el robot calcula solo hacia las zonas grises, que todavía no conoce. Tercero, el borde morado y celeste es un margen de seguridad que el robot respeta junto a los muros: por eso gira y corrige su camino sin chocar. Al final, el robot construyó solo el mapa del recinto. Ahora les explico para qué sirve esto, cómo lo construí y qué resultados medí.

Lámina 3 · Estructura de la defensa (15 s)

La presentación tiene seis partes: el problema que aborda este trabajo, el estado del arte, los objetivos y el alcance, el diseño del sistema, los resultados medidos en el robot real y las conclusiones.

## 01 · Problema

Lámina 4 · ¿Para qué sirve? Entrar donde es riesgoso o lento hacerlo a pie (80 s)

[CLIC] Una pregunta legítima al ver un prototipo de laboratorio es para qué sirve en la práctica. Antes de medir, inspeccionar o trasladar algo, una máquina necesita tres cosas: saber dónde está, dibujar el lugar y decidir adónde ir. [CLIC] El caso más cercano para Chile es la minería subterránea. Hay frentes donde la norma prohíbe entrar a una persona. En El Teniente, Codelco ya usa un dron con láser que mapea solo, sin GPS, y hace en cinco minutos una inspección que antes tomaba medio día. [CLIC] Lo mismo pasa en la inspección de plantas: robots como Spot o ANYmal recorren instalaciones de Glencore y Vale con sensores. Su precio es solo a cotización. [CLIC] Y una aplicación directa de este trabajo es el levantamiento de planos: el robot dibuja el plano de un recinto, y los mapas que obtuve quedan a 3.4 centímetros del plano medido con huincha. [CLIC] Todas estas aplicaciones parten de la misma base: un robot que se ubica, mapea y decide solo. Eso es lo que construí.

Lámina 5 · El mercado ya existe: industria y docencia (80 s)

El mercado para esto ya existe, en dos niveles. [CLIC] Arriba están los equipos industriales. Spot, de Boston Dynamics, hace misiones autónomas de inspección y Glencore lo usa en una mina en Canadá. Hovermap mapea en 3D sin GPS y se usa en más de treinta minas. En Chile, el robot Arkytas de la empresa Kinamics inspecciona frentes en El Teniente, pero lo maneja una persona a distancia. Estos equipos se venden solo a cotización y su funcionamiento interno no siempre es accesible. [CLIC] En el otro extremo están los robots didácticos, como el TurtleBot 3 Burger, que cuesta 681 dólares sin envío ni impuestos y trae un sensor de giro y motores integrados. [CLIC] Este prototipo se ubica entre ambos: usa piezas separadas, explora solo un recinto desconocido y mide su propio desempeño. Hay que decirlo claro: no tiene sensor de giro, así que no equivale al Burger. [CLIC] La idea es esta: el mismo objetivo que persigue la industria, mapear y decidir sin operador, con el costo de un kit didáctico y con resultados medidos.

Lámina 6 · ¿Qué aporta? Que 4 subsistemas funcionen juntos (70 s)

Lograr que un robot sea autónomo no es resolver una sola pieza. Hay que hacer que cuatro subsistemas trabajen juntos. [CLIC] Primero, la percepción: medir la distancia a los muros con el láser y el giro de cada rueda con los encoders, que son sensores que cuentan las vueltas. [CLIC] Segundo, la localización y el mapeo: que el robot sepa dónde está mientras dibuja el plano. [CLIC] Tercero, el control de las ruedas: que cada rueda gire a la velocidad que se le pide. [CLIC] Y cuarto, la planificación y exploración: decidir adónde ir y cómo llegar sin chocar. Los equipos comerciales traen esto integrado de fábrica y los proyectos abiertos suelen resolver piezas sueltas. Integrar las cuatro y medirlas en un robot real es el aporte de este trabajo. [CLIC] De ahí nace la pregunta central: ¿es posible construir un robot diferencial que, con componentes accesibles y herramientas de código abierto, mapee, navegue y explore interiores de forma autónoma?

## 02 · Estado del arte

Lámina 7 · Estado del arte: qué se eligió en cada subsistema (80 s)

Para responder la pregunta revisé el estado del arte en esos mismos cuatro subsistemas. [CLIC] En la base, la tracción diferencial usa dos ruedas con motor y una rueda de soporte, y puede girar sobre su propio eje. Un vehículo tipo automóvil no gira en el lugar y uno omnidireccional es mecánicamente más complejo. [CLIC] En percepción, elegí un LIDAR 2D, un sensor láser que mide distancias en 360 grados. Una cámara de profundidad o un láser 3D dan más datos, pero exigen más cálculo y cuestan más. En un piso plano, basta con un plano de medición. [CLIC] Para el mapa usé SLAM Toolbox. SLAM significa mapear y ubicarse al mismo tiempo. SLAM Toolbox corrige el mapa cuando el robot vuelve a un lugar conocido y permite guardarlo. GMapping no detecta ese regreso y Cartographer es el que más usa el procesador en una comparación de cinco métodos. [CLIC] Y para explorar elegí la exploración por fronteras: ir siempre al borde entre lo conocido y lo desconocido. Es liviana y usa directamente el mapa.

Lámina 8 · Costo: por debajo del kit didáctico de entrada (55 s)

También comparé el costo con las plataformas más usadas en docencia. [CLIC] Los materiales montados en el robot suman 444 643 pesos, unos 462 dólares. El proyecto completo, con red dedicada, cargador y baterías de repuesto, llega a 582 447 pesos. [CLIC] El TurtleBot 3 Burger cuesta 656 092 pesos y el Waffle Pi supera el millón seiscientos mil, en ambos casos sin envío ni impuestos de internación. [CLIC] El robot cuesta un 32 por ciento menos que el Burger, y el proyecto completo un 11 por ciento menos. [CLIC] Quiero ser transparente: el Burger trae un sensor de giro y motores con controlador integrados. El prototipo logra el ahorro con piezas separadas y sin ese sensor. Cuesta menos, pero no ofrece exactamente lo mismo.

## 03 · Objetivos

Lámina 9 · Objetivo general y objetivos específicos (65 s)

[CLIC] El objetivo general fue diseñar e implementar un robot diferencial de bajo costo, basado en ROS 2, que es el software estándar para robots, capaz de construir un mapa 2D mediante SLAM y de navegar solo hacia destinos que genera una estrategia de exploración de fronteras. [CLIC] Para lograrlo definí cuatro objetivos específicos. El primero, construir el robot y validarlo antes en un gemelo digital en el simulador Gazebo Classic. El segundo, controlar las ruedas: modelo de movimiento, odometría con encoders y control de velocidad en lazo cerrado. [CLIC] El tercero, mapear, ubicarse y navegar con SLAM Toolbox y Nav2. Y el cuarto, explorar sin ayuda, con metas que se generan automáticamente. [CLIC] El alcance son interiores de piso plano, evaluando la navegación sobre las metas del explorador. Quedaron fuera las metas fijas que marca un operador y la ubicación sobre un mapa guardado.

## 04 · Diseño

Lámina 10 · Arquitectura: el robot controla, el computador piensa (70 s)

Para usar hardware de bajo costo sin sobrecargar la electrónica del robot, repartí el trabajo en dos equipos. [CLIC] En el robot va lo que no puede esperar. El láser mide distancias en 360 grados y los encoders cuentan las vueltas de cada rueda. Un Arduino Nano controla la velocidad de cada rueda cada 33 milisegundos y, como protección, frena los motores si pasan dos segundos sin recibir órdenes. Sobre él, una Raspberry Pi 4 conecta todo con ROS 2 y calcula la odometría, es decir, cuánto avanzó el robot según sus ruedas. [CLIC] Ambos equipos se comunican por una red Wi-Fi dedicada: el robot envía los barridos del láser y la odometría, y recibe las órdenes de velocidad. [CLIC] En un computador portátil va lo que exige más cálculo: SLAM Toolbox dibuja el mapa y ubica al robot, Nav2 traza la ruta y ordena las velocidades, el explorador elige la próxima meta y RViz2 lo muestra todo en pantalla.

Lámina 11 · El robot real y su gemelo digital (65 s)

[CLIC] Este es el robot construido. El chasis está impreso en 3D en PLA+, a partir de una plataforma abierta de referencia. Se mueve con dos motores de 12 volts con encoder y se apoya en una rueda de soporte. Arriba va el láser RPLidar A1, con vista libre en 360 grados. En lo eléctrico, separé la potencia de 12 volts de los motores del riel regulado de 5 volts que alimenta la electrónica, para evitar interferencias y reinicios. [CLIC] A la derecha está su gemelo digital: una copia virtual del robot en el simulador Gazebo Classic, descrita en URDF, que es el formato estándar para describir las piezas y uniones de un robot. Tiene el mismo radio de rueda y la misma distancia entre ruedas que el real. Con él probé el movimiento, los sensores y la comunicación antes de pasar al robot físico.

Lámina 12 · Cinco decisiones de diseño y su razón (70 s)

Estas son las cinco decisiones que ordenan la plataforma, pensando en bajo costo, compatibilidad y que todo corra en un computador portátil. [CLIC] Como software base elegí ROS 2, que organiza el robot en programas independientes, sin uno central, y trae un sistema de navegación completo. Usé la versión Foxy porque todos los paquetes del robot funcionan con ella. Como sensor, un LIDAR 2D: barato, suficiente en piso plano y con menos cálculo que la visión 3D. [CLIC] Para el mapa, SLAM Toolbox, que corrige el mapa al volver a un lugar y lo guarda. Para navegar, Nav2 con dos piezas: A estrella, que busca el camino más corto sobre el mapa, y DWB, que prueba trayectorias cortas según la velocidad actual y elige la que sigue la ruta lejos de los obstáculos. [CLIC] Por último, Gazebo Classic, compatible con el software del robot, y la exploración por fronteras, que elige metas mirando solo el mapa.

Lámina 13 · Control de velocidad: medir, buscar y ajustar en el robot (100 s)

Un punto central para nuestra especialidad es cómo se controla la velocidad de cada rueda. Cada 33 milisegundos, el Arduino corrige la potencia de cada motor con un controlador PI, que combina una acción proporcional y una integral. Para ajustar sus valores seguí tres pasos. [CLIC] Primero, medir. Apliqué a cada rueda un escalón fijo de potencia, un PWM de 143 sobre 255, durante 10 segundos, y registré su velocidad cada 0.1 segundos. El PWM indica cuánta potencia recibe el motor. Con esa curva obtuve un modelo simple de cada motor, de primer orden con retardo. [CLIC] Segundo, buscar. Usé PSO, optimización por enjambre de partículas: 50 candidatos prueban combinaciones de los parámetros durante 150 rondas sobre ese modelo. La búsqueda premia seguir la referencia y castiga tres veces más pasarse de la velocidad. El resultado fue un punto de partida estable. [CLIC] Tercero, ajustar en el robot. El modelo no ve la zona muerta del driver L298N: con poca potencia el motor simplemente no arranca. Por eso hice el ajuste final sobre el piso, a 0.13 metros por segundo. [CLIC] El resultado se ve en las curvas. Antes, la rueda derecha se detenía en 0.11 y llegaba a la referencia recién a los 6 segundos. Después del ajuste, ambas ruedas suben en 0.8 y 1.4 segundos, sin sobreimpulso significativo.

Lámina 14 · ¿Cómo dibuja el mapa? SLAM en 4 pasos (65 s)

Antes de ver los resultados, les explico cómo el robot construye el mapa que vimos en el video. [CLIC] Mientras se mueve, el láser gira y mide la distancia a cada muro que tiene a la vista. [CLIC] Al mismo tiempo, los encoders le dicen al sistema cuánto avanzó y giró el robot entre una medición y otra. [CLIC] Como las ruedas pueden resbalar, SLAM Toolbox no confía solo en ellas: compara cada nuevo barrido del láser con los anteriores para alinearlos. Con eso pinta una grilla de cuadros de 5 por 5 centímetros: blanco donde hay espacio libre, negro donde hay un muro y gris donde todavía no ha visto nada. [CLIC] Y si el robot vuelve a ver un lugar por donde ya pasó, el algoritmo reconoce la coincidencia, lo que se llama cierre de lazo, y corrige el error acumulado de todo el recorrido.

Lámina 15 · ¿Qué es una meta y cómo explora solo? (65 s)

Ahora, ¿cómo decide el robot hacia dónde moverse si nadie le entregó un mapa ni una ruta? Aquí entran dos ideas: las fronteras y las metas. [CLIC] Una frontera es el borde entre el espacio libre que ya conoce, en blanco, y lo desconocido, en gris. El explorador las busca en el mapa en vivo. [CLIC] Una meta es un punto con coordenadas x e y sobre una de esas fronteras. El explorador la elige solo, equilibrando cercanía y tamaño de la zona por descubrir. No es una lista de puntos que alguien programó antes. [CLIC] Esa meta pasa a Nav2, que deja un margen de seguridad de 15 centímetros junto a cada muro, el borde morado del video, y traza la ruta verde hasta la meta. [CLIC] Cuando el explorador ya no encuentra fronteras alcanzables, da por terminado el recorrido y detiene el robot por sí solo.

## 05 · Resultados

Lámina 16 · En el robot real: explora solo y mapea con precisión (65 s)

Todas las mediciones que presento se hicieron en el robot físico, en este recinto con pasillos y tabiques internos, pensado para exigir giros y espacios estrechos. Hice seis exploraciones completas. En la segunda el robot no generó mapa, así que la excluí de los promedios. [CLIC] En lo operativo, 5 de 6 exploraciones terminaron solas, sin ninguna intervención humana, deteniéndose al terminar el mapa. En total, Nav2 condujo al robot 21.9 metros en 12.7 minutos de operación autónoma, sin colisiones. [CLIC] ¿Y qué tan fiel es el mapa? Al compararlo con un plano del recinto medido con huincha, la diferencia media en la posición de los muros fue de 3.4 centímetros, menos que el tamaño de un cuadro del mapa, que es de 5. Además, el área libre mapeada fue muy estable: 3.50 metros cuadrados en promedio, con una desviación de solo 0.03.

Lámina 17 · Precisión del movimiento: control, rectas y giros (65 s)

Para entender qué sostiene esos mapas, medí por separado el control y la precisión del movimiento. [CLIC] En el control de velocidad, a 0.13 metros por segundo, las ruedas suben en 0.8 y 1.4 segundos, sin sobreimpulso significativo. El error final, de 0.002 y 0 metros por segundo, es menor que la resolución del sensor. [CLIC] En línea recta, con cinco repeticiones de 2 metros medidas con cinta métrica, la odometría tuvo un error medio de 3.63 por ciento, unos 7 centímetros en 2 metros. [CLIC] En giros completos de 360 grados, la desviación media fue de 11.7 grados, un 3.24 por ciento de la vuelta. Girar es más sensible: las ruedas resbalan y el robot no tiene sensor de giro. Por eso es importante que SLAM no dependa solo de las ruedas y alinee los barridos del láser para construir el mapa.

Lámina 18 · Los mapas se repiten y calzan con el plano (55 s)

[CLIC] Este gráfico muestra el área libre mapeada en las cinco exploraciones válidas. El eje parte en 3.40 para que se vean las diferencias: entre la mayor y la menor hay solo 0.06 metros cuadrados. [CLIC] A la derecha hay un detalle que conviene aclarar. El índice de cobertura varía entre 53 y 83 por ciento, lo que podría parecer inconsistente. Pero la exploración 1 y la 6 mapearon casi la misma superficie, 3.51 y 3.48 metros cuadrados. [CLIC] El índice cambia porque mide qué parte de la imagen es espacio libre, y cada imagen incluye más o menos gris de afuera según cómo quedó orientado el mapa. Por eso la evidencia del mapeo es el área en metros cuadrados y la comparación con el plano real.

Lámina 19 · Las metas se renuevan mientras el robot avanza (55 s)

Al revisar los registros de navegación apareció algo que conviene explicar bien. [CLIC] El explorador revisa el mapa cada 3.3 segundos. Si el robot avanzó y apareció una frontera mejor, envía una meta nueva sin cancelar la anterior, y esta versión de Nav2 anota ese reemplazo como «abortado». [CLIC] Por eso, de 60 metas, 54 figuran como abortadas, pero 53 de ellas coinciden justo con la llegada de la meta siguiente: el robot no se detuvo, cambió de destino mientras avanzaba. Soy cuidadoso en esto: el registro no permite descartar otras causas caso a caso, y por eso no lo uso como tasa de éxito. [CLIC] La síntesis es que los cuatro subsistemas funcionaron juntos en el robot real: control y odometría, mapa, navegación y exploración.

## 06 · Conclusiones

Lámina 20 · Cumplimiento de los objetivos (85 s)

Reviso ahora los cuatro objetivos específicos. [CLIC] El primero, construir el robot y su gemelo digital, está logrado: el robot se construyó y su gemelo se verificó antes en Gazebo Classic. [CLIC] El segundo, el control de las ruedas, está logrado en lo que se ensayó: encoders, odometría y un control PI estable a 0.13 metros por segundo. En la tesis lo marqué como cumplido parcialmente porque lo evalué en un solo punto de operación. El próximo paso es probar otras velocidades, giros lentos y cambios de sentido. [CLIC] El tercero, mapear, ubicarse y navegar, también está logrado en lo ensayado: mapas a 3.4 centímetros del plano y 21.9 metros de navegación autónoma. Lo marqué parcial porque no medí una tasa de éxito con metas fijas, que estaba fuera del alcance. Ese es el próximo paso. [CLIC] Y el cuarto, explorar sin ayuda, está logrado: las metas se generan solas y la exploración terminó sin ayuda en 5 de 6 ensayos. En resumen, el objetivo general se cumple en lo funcional. Las dos marcas de parcial son una decisión de rigor, para no inflar los indicadores.

Lámina 21 · Para competir: lo que ya está demostrado y lo que falta (75 s)

Si quisiera competir con lo que ya existe, el precio no basta. La pregunta es qué resultados exige quien lo usaría y cuáles ya demostré. [CLIC] Mapear sin GPS con precisión: ya está demostrado, con 3.4 centímetros frente al plano. Falta hacerlo en recintos grandes. Explorar sin operador: 5 de 6 exploraciones terminaron solas. Falta medir la tasa de éxito con metas fijas, con 6 a 10 repeticiones. [CLIC] Operar sin incidentes: 21.9 metros sin colisiones ni intervención. Falta medir horas de operación y duración de batería. Resultados repetibles: el área varió solo 0.03 metros cuadrados. Falta repetir en otros recintos. [CLIC] Y para un terreno real como una mina, el prototipo todavía trabaja en piso plano: haría falta un sensor de giro, un sensor 3D y un chasis resistente. [CLIC] Entonces, el aporte no es solo el precio. La cadena completa de autonomía ya está medida en un robot real, y cada brecha se puede cerrar por partes sobre esta misma base.

Lámina 22 · Aporte de ingeniería y trabajo futuro (65 s)

[CLIC] El aporte central no es haber escrito un firmware desde cero: el firmware y la interfaz del Arduino se adaptaron de proyectos abiertos, debidamente citados. El aporte es la integración completa, documentada y verificada en el robot real: el modelo geométrico del robot, la identificación de cada motor, el ajuste del control con PSO y refinamiento en el robot, el análisis de estabilidad de la ley que realmente se ejecuta, y los protocolos de ensayo con la comparación contra el plano. [CLIC] Como trabajo futuro, primero, sumar un sensor de giro para reducir la desviación en los giros. Segundo, ensayar metas fijas con 6 a 10 repeticiones en un recinto mayor. [CLIC] Tercero, migrar a una versión mantenida de ROS 2 y de Gazebo. Y cuarto, cancelar cada meta antes de enviar la siguiente, para separar los reemplazos de los fallos reales.

Lámina 23 · Conclusión (35 s)

[CLIC] Vuelvo a la pregunta del inicio. Sí: es viable construir un robot diferencial de bajo costo que mapea, navega y explora interiores de forma autónoma, y lo respaldo con mediciones en el robot real. [CLIC] Me quedo con tres ideas. Un control de ruedas bien ajustado sostiene mapas fieles. Repartir el trabajo entre el robot y el computador hace viable la autonomía con hardware accesible. Y queda una base abierta y medida, lista para docencia o para sumar sensores de inspección.

Lámina 24 · Muchas gracias (5 s)

Muchas gracias por su atención. Quedo atento a sus preguntas y comentarios. [Para mostrar un respaldo: clic en «Respaldo», abajo a la derecha, y elegir el tema.]

## Láminas de respaldo

Están ocultas: no aparecen al avanzar. Para abrir una, haz clic en «Respaldo» en la lámina 24, o escribe 25 y Enter para ir al índice. Cada respaldo tiene «Volver al índice».

| Lámina | Código | Tema | Qué responder en breve |
|---|---|---|---|
| 26 | R1 | Ley PI del Arduino | La ley heredada de ROSArduinoBridge es incremental: equivale a un PI con la acción proporcional sobre la medición. Se mantuvo por compatibilidad con diffdrive_arduino. |
| 27 | R2 | Estabilidad del lazo | Sobre el modelo lineal con 0.1 s de demora, los márgenes siguen en rangos habituales. No incluye la zona muerta ni el truncamiento entero. |
| 28 | R3 | Identificación y PSO | El PSO dio un punto de partida estable. El ajuste final en el robot compensó lo que el modelo no ve. |
| 29 | R4 | PSO antes y después | Antes y después del ajuste en el robot real, a 0.13 m/s. |
| 30 | R5 | Giros sin IMU | Sin IMU, el ángulo sale solo de la diferencia de avance entre ruedas, y cualquier resbalón queda en el ángulo. Por eso los giros (11.7°) son menos precisos que las rectas (3.63%). La mejora es una IMU fusionada con los encoders mediante robot_localization, y repetir el ensayo con ángulo fijo. |
| 31 | R6 | Esquema eléctrico | Dos dominios: 12 V de la batería para los motores a través del L298N, y un conversor DC-DC de 25 W que entrega 5 V regulados a la Raspberry, el Arduino y el láser. Con interruptor y portafusible. Como mejora, un driver MOSFET con menos pérdidas que el L298N. |
| 32 | R7 | Raspberry y Arduino | La Raspberry y el Arduino hablan por USB serial con comandos de texto cortos. Si pasan 2 segundos sin órdenes, el Arduino frena. La lectura de encoders no es atómica, quedó documentada y su arreglo es directo. |
| 33 | R8 | Margen de 15 cm | Los pasillos miden 58 cm. Con un margen igual a la esquina del robot, 24 cm por lado, el centro tendría solo 10 cm de paso. Con 15 cm quedan 28 cm. El límite es que el planificador revisa el centro y no el contorno, y eso quedó documentado. |
| 34 | R9 | Láser y enfoque clásico | El nodo del láser lo escribí para leer el sensor por el puerto serie y revisar su salud antes de publicar. Tiene un detalle documentado en la marca de tiempo. Sobre aprendizaje por refuerzo: el enfoque clásico es interpretable y no requiere entrenamiento. Esta base permite probar esas políticas después. |
| 35 | R10 | Aporte propio | Reutilicé la infraestructura estándar de ROS 2 y adapté cuatro paquetes abiertos, todos citados. Mi desarrollo propio está en la integración, el modelo del robot, el nodo del láser, el paquete de identificación y PSO, el análisis de estabilidad y los protocolos de ensayo. |
| 36 | R11 | Red y computador externo | Repartí el trabajo para que el robot haga solo lo urgente y el computador lo pesado. La red es dedicada, con IP estáticas, y ROS 2 usa CycloneDDS. Como siguiente paso, se puede llevar todo a la Raspberry de 8 GB después de medir su carga. |
| 37 | R12 | Camino a un producto | Si la escuela quisiera usarlo como equipo de laboratorio, haría tres etapas: robustez, validación y producto docente. Es una propuesta, no algo evaluado en la tesis. |
| 38 | R13 | Las 60 metas | Las 60 metas se reconstruyeron por su identificador único. 53 de los 54 abortos ocurren cuando llega la meta siguiente, con una mediana de 3.3 s entre metas. El criterio no descarta fallos simultáneos, por eso no lo uso como tasa de éxito. |
| 39 | R14 | Mapa frente al plano | Los mapas se ubican sobre el plano sin escalarlos. Distancia media 3.4 cm, menor que un cuadro de 5 cm. |
| 40 | R15 | Intervalos de confianza | Con cinco repeticiones, unas cifras son precisas y otras no. Por eso propongo 6 a 10 repeticiones. |
| 41 | R16 | Metas fijas y AMCL | Las metas fijas y AMCL quedaron fuera del alcance declarado. Se dejó el protocolo para medirlas. |
| 42 | R17 | Alternativas descartadas | Cada elección se comparó con sus alternativas. La razón común: integración directa con ROS 2 y bajo costo de cómputo para un computador portátil. |

## Mini glosario

Una frase por término, para responder sin jerga.

- **LIDAR 2D:** sensor láser que gira y mide la distancia a lo que lo rodea, en un plano.
- **Encoder:** sensor que cuenta cuánto gira cada rueda.
- **Odometría:** estimar cuánto avanzó y giró el robot contando el giro de sus ruedas.
- **IMU:** sensor de giro y aceleración. Este robot no lo tiene.
- **SLAM:** construir el mapa y ubicarse en él al mismo tiempo.
- **Cierre de lazo:** cuando SLAM reconoce un lugar ya visto y corrige el error acumulado.
- **ROS 2:** software estándar para robots, organizado en programas que se envían mensajes.
- **Nav2:** el sistema de navegación de ROS 2: traza la ruta y ordena las velocidades.
- **A\* (A estrella):** busca el camino más corto en el mapa, sumando lo recorrido y una estimación de lo que falta.
- **DWB:** prueba trayectorias cortas posibles según la velocidad actual y elige la que sigue la ruta lejos de los obstáculos.
- **Frontera:** el borde entre el espacio libre conocido y lo desconocido.
- **Meta:** el punto (x, y) en una frontera hacia donde el explorador manda al robot.
- **PWM:** la forma de dosificar la potencia del motor, de 0 a 255 en este Arduino.
- **PI:** control con una parte proporcional al error y otra que acumula el error pasado.
- **FOPDT:** modelo simple de un motor: cuánto responde, qué tan rápido y con cuánto retardo.
- **PSO:** optimización por enjambre de partículas: muchos candidatos prueban combinaciones y se acercan a la mejor.
- **URDF:** formato estándar que describe las piezas y uniones de un robot.
- **AMCL:** método para ubicarse dentro de un mapa ya guardado. Quedó fuera del alcance.
- **Gemelo digital:** copia virtual del robot en el simulador.

## Cómo ensayar

1. No memorices palabra por palabra. Fija las ideas clave de cada lámina y la frase de paso a la siguiente.
2. Ensaya con la presentación corriendo y un cronómetro, al menos tres veces, para calzar cada clic con tu voz.
3. Grábate una vez en audio y escucha si se cuelan muletillas.
