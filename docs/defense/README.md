# Defensa

Material para la defensa de la tesis.

- `slides-v3.pptx`: la presentación vigente. Tiene 40 láminas visibles y 18 ocultas: un índice, 16 respaldos (R1 a R16) para las preguntas y un glosario. Las láminas 5, 6 y 10 comparan el robot con equipos que entran donde es riesgoso para una persona (rescate, plantas tras un accidente, zonas con gases), y la 37 muestra la minería como horizonte. Las láminas 13 y 14 presentan el alcance como contexto de trabajo, la percepción del LIDAR 2D y las oportunidades de mejora. La sección Diseño, de la 16 a la 28, va de lo grande a lo pequeño: el prototipo, sus componentes, la arquitectura, ROS 2 como red de nodos, Gazebo, el control, el mapa y la navegación, con una barra «Recorrido» al pie y la transición Morph entre láminas. Las láminas 22 a 25 explican el ajuste del control en cuatro pasos. Cada lámina de la sección Diseño y de los respaldos nuevos define sus siglas al pie, y todas las láminas de contenido tienen un botón «Glosario» que abre la lámina 58 y vuelve con «Volver». Cada respaldo es una tarjeta de respuesta rápida: el título es la conclusión y una animación corta parte sola al abrirlo. Los respaldos R10 a R16 comparan cada alternativa con un diagrama de cómo funciona. Las cifras exactas que salen de pantalla quedan en las notas del orador, bajo «DATOS PARA PREGUNTAS». Seis portadas azules separan los temas y su ícono viaja con la transición Morph hasta la cabecera de la lámina siguiente. Trae el video de demostración incrustado, animaciones por clic, transiciones y el guion en las notas del orador.
- `slides-v3.pdf`: la misma presentación en PDF, con las láminas ocultas al final. El video aparece como imagen fija.
- `script-v3.md`: el guion de la v3, lo que se dice en cada lámina, el mapa de las láminas de respaldo con sus respuestas breves y un glosario.
- `generar_audio_guion.py`: lee `script-v3.md` y genera audio de ensayo con la voz `es-CL-LorenzoNeural` de edge-tts: un MP3 por lámina, `defensa_completa.mp3` y `respaldos_respuestas.mp3`, en `audio_guion/`. Requiere `pip install edge-tts==7.3.1` e internet. Los MP3 no se suben a git porque se regeneran con un comando.
- `slides-v2.pptx` y `script.md`: la versión anterior, de 28 láminas, y su guion.
- `images/`: todas las imágenes que usan las láminas, nombradas por la primera lámina de la v2 donde aparecen, más `images/logos/`. Las imágenes que solo existían dentro de la presentación se extrajeron byte a byte, así que conservan la calidad guardada en el `.pptx`.
- `images/v3/`: lo que agrega la v3. Logos (`logo-*`) y fotos (`photo-*`) de empresas y equipos, copias reducidas de figuras de la tesis (`backup-*`), la imagen fija del video, los gráficos de control (`chart-control-*.svg`, dibujados por `chart-control.py` desde los datos medidos en `chart-control-data.csv`, en capas del mismo tamaño para animar cada parte por separado), los diagramas explicativos (`diagram-*.svg` y el dibujo `drawing-l298n.svg`, generados por `diagrams.py`, también en capas `-layer-N` cuando se animan por partes) e íconos SVG dibujados a mano (`icon-*.svg`, con `-white` los de trazo blanco). Para cambiar el dibujo del L298N por una foto, guárdala como `images/v3/photo-l298n.jpg` y en PowerPoint usa «Cambiar imagen» sobre el dibujo del respaldo R5.
- `images/icons/`: íconos de Lucide, Tabler y Simple Icons bajados de Iconify, nombrados `{set}-{icono}-{color}.svg`. Autores y licencias en `docs/credits.md`.

El video de la lámina 2 es una copia comprimida y sin audio del video público del ensayo en YouTube (decisión 0004). El archivo original queda en `videos/`, fuera de git. Las grabaciones de los ensayos y su feedback son privados y quedan solo en el computador del autor.

La v3 se generó con un script de Python que no forma parte del repositorio. `slides-v3.backup.pptx`, `script-v3.backup.md` y los archivos `*.pre-refinamiento.*`, `*.pre-cierre.*`, `*.pre-split-control.*`, `*.pre-didactico.*` y `*.pre-comercial.*` son copias locales de versiones anteriores y no se suben a git, porque el historial ya las guarda.

## Imágenes por lámina, v3

Todas las láminas muestran además el logo de la UTEM, `images/logos/utem-logo-color.png`, salvo la 40. Las rutas son relativas a esta carpeta. Las láminas de la 41 a la 58 están ocultas.

| Lámina | Estado | Imágenes |
|-------|-------|--------|
| 1 | visible | `images/slide-01-prototype-three-quarter-cutout.png` |
| 2 | visible | `images/v3/slide-02-demo-poster.jpg` (imagen fija del video incrustado), `images/slide-15-low-poly-robot-cutout.png` |
| 3 | visible | `images/icons/lucide-triangle-alert-ffffff.svg`, `images/icons/lucide-layers-ffffff.svg`, `images/icons/lucide-target-ffffff.svg`, `images/icons/lucide-cpu-ffffff.svg`, `images/icons/lucide-bar-chart-3-ffffff.svg`, `images/icons/lucide-circle-check-ffffff.svg` |
| 4 | visible | `images/icons/lucide-triangle-alert-ffffff.svg` |
| 5 | visible | `images/icons/lucide-triangle-alert-ffffff.svg`, `images/v3/photo-hector-rescue.jpg`, `images/icons/lucide-siren-004eaa.svg`, `images/v3/photo-packbot-fukushima.jpg`, `images/icons/lucide-radiation-004eaa.svg`, `images/v3/photo-exr2.png`, `images/icons/lucide-flame-004eaa.svg` |
| 6 | visible | `images/icons/lucide-triangle-alert-ffffff.svg`, `images/icons/lucide-siren-ffffff.svg`, `images/v3/photo-smokebot.jpg`, `images/icons/lucide-route-004eaa.svg`, `images/icons/lucide-radar-004eaa.svg`, `images/icons/lucide-flame-004eaa.svg`, `images/icons/lucide-graduation-cap-ffffff.svg`, `images/v3/photo-turtlebot3-burger.png`, `images/v3/logo-robotis.svg`, `images/icons/lucide-book-open-004eaa.svg`, `images/icons/lucide-bot-ffffff.svg`, `images/slide-01-prototype-three-quarter-cutout.png`, `images/icons/lucide-cpu-004eaa.svg` |
| 7 | visible | `images/icons/lucide-triangle-alert-ffffff.svg`, `images/slide-01-prototype-three-quarter-cutout.png`, `images/icons/lucide-radar-ffffff.svg`, `images/icons/lucide-map-pinned-ffffff.svg`, `images/icons/lucide-gauge-ffffff.svg`, `images/icons/lucide-route-ffffff.svg` |
| 8 | visible | `images/icons/lucide-layers-ffffff.svg` |
| 9 | visible | `images/icons/lucide-layers-ffffff.svg`, `images/icons/lucide-gauge-ffffff.svg`, `images/slide-08-robot-car.png`, `images/icons/lucide-radar-ffffff.svg`, `images/slide-08-lidar.png`, `images/icons/lucide-map-pinned-ffffff.svg`, `images/slide-08-pose-path.png`, `images/icons/lucide-route-ffffff.svg`, `images/slide-08-map-outline.png` |
| 10 | visible | `images/icons/lucide-layers-ffffff.svg`, `images/v3/photo-packbot-fukushima.jpg`, `images/v3/photo-turtlebot3-burger.png`, `images/slide-01-prototype-three-quarter-cutout.png`, `images/icons/lucide-lock-open-004eaa.svg`, `images/icons/lucide-route-004eaa.svg`, `images/icons/lucide-ruler-004eaa.svg`, `images/icons/lucide-coins-004eaa.svg` |
| 11 | visible | `images/icons/lucide-target-ffffff.svg` |
| 12 | visible | `images/icons/lucide-target-ffffff.svg`, `images/icons/lucide-bot-004eaa.svg`, `images/icons/lucide-map-004eaa.svg`, `images/icons/lucide-compass-004eaa.svg`, `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-map-pinned-004eaa.svg` |
| 13 | visible | `images/icons/lucide-target-ffffff.svg`, `images/icons/lucide-building-2-004eaa.svg`, `images/icons/lucide-map-004eaa.svg`, `images/icons/lucide-target-004eaa.svg`, `images/icons/lucide-wifi-004eaa.svg`, `images/icons/lucide-circle-check-004eaa.svg`, `../../figures/06-results/experimental-environment.jpg` |
| 14 | visible | `images/icons/lucide-target-ffffff.svg`, `images/icons/lucide-radar-ffffff.svg`, `images/v3/diagram-lidar-plane-base.svg`, `images/v3/diagram-lidar-plane-layer-1.svg`, `images/v3/diagram-lidar-plane-layer-2.svg`, `images/v3/diagram-lidar-surfaces.svg`, `images/icons/lucide-trending-up-ffffff.svg`, `images/icons/lucide-camera-3b6e10.svg`, `images/icons/lucide-compass-3b6e10.svg`, `images/icons/lucide-expand-3b6e10.svg`, `images/icons/lucide-refresh-cw-3b6e10.svg` |
| 15 | visible | `images/icons/lucide-cpu-ffffff.svg` |
| 16 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/slide-01-prototype-three-quarter-cutout.png`, `images/icons/lucide-printer-004eaa.svg`, `images/icons/lucide-circle-dot-004eaa.svg`, `images/icons/lucide-zap-004eaa.svg` |
| 17 | visible | `images/slide-08-encoder.png`, `images/slide-08-lidar.png`, `images/slide-08-arduino.png`, `images/slide-08-motor.png`, `images/slide-08-raspberry-pi.png`, `images/icons/lucide-cpu-ffffff.svg`, `../../figures/05-implementation/prototype-left-side.jpg`, `images/v3/diagram-lidar-rays.svg`, `images/v3/diagram-encoder-pulses.svg` |
| 18 | visible | `images/slide-08-encoder.png`, `images/slide-08-motor.png`, `images/slide-08-robot-car.png`, `images/slide-08-lidar.png`, `images/slide-08-arduino.png`, `images/slide-08-raspberry-pi.png`, `images/slide-08-robot-on-screen.png`, `images/slide-08-navigation-arrow.png`, `images/slide-08-pose-path.png`, `images/slide-08-map-outline.png`, `images/slide-08-desktop-computer.png`, `images/icons/lucide-cpu-ffffff.svg` |
| 19 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/slide-08-lidar.png`, `images/slide-08-map-outline.png`, `images/slide-08-navigation-arrow.png`, `images/slide-08-pose-path.png`, `images/slide-08-raspberry-pi.png`, `images/slide-08-arduino.png` |
| 20 | visible | `images/icons/lucide-cpu-ffffff.svg`, `../../figures/05-implementation/prototype-left-side.jpg`, `../../figures/05-implementation/gazebo-laser-robot.png`, `images/v3/logo-gazebo.svg`, `images/icons/lucide-ruler-004eaa.svg`, `images/icons/simple-icons-ros-172435.svg`, `images/icons/lucide-flask-conical-004eaa.svg`, `images/icons/lucide-wrench-3b6e10.svg`, `images/icons/lucide-bot-004eaa.svg` |
| 21 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/icons/lucide-calculator-6b7280.svg`, `images/icons/lucide-circle-plus-3b6e10.svg`, `images/icons/lucide-trending-up-004eaa.svg`, `images/icons/lucide-puzzle-004eaa.svg`, `images/icons/lucide-shield-check-004eaa.svg` |
| 22 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/v3/logo-python.svg`, `images/icons/tabler-wave-square-ffffff.svg`, `images/icons/lucide-gauge-ffffff.svg`, `images/v3/chart-control-step-output.svg`, `images/v3/chart-control-step-output-curves.svg`, `images/v3/chart-control-step-output-zoom.svg`, `images/icons/lucide-lightbulb-004eaa.svg` |
| 23 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/v3/logo-python.svg`, `images/v3/chart-control-fopdt.svg`, `images/v3/chart-control-fopdt-measured.svg`, `images/v3/chart-control-fopdt-model.svg`, `images/v3/chart-control-fopdt-l.svg`, `images/v3/chart-control-fopdt-tau.svg`, `images/v3/chart-control-fopdt-km.svg`, `images/v3/icon-pso-swarm-white.svg`, `images/icons/lucide-lightbulb-004eaa.svg` |
| 24 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/v3/logo-python.svg`, `images/icons/lucide-cpu-ffffff.svg`, `images/v3/icon-pso-swarm-white.svg`, `images/icons/lucide-check-3b6e10.svg`, `images/icons/lucide-sprout-ffffff.svg`, `images/icons/lucide-timer-reset-3b6e10.svg`, `images/icons/lucide-split-3b6e10.svg`, `images/icons/lucide-repeat-3b6e10.svg` |
| 25 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/v3/logo-python.svg`, `images/v3/chart-control-closed-loop.svg`, `images/v3/chart-control-closed-loop-after.svg`, `images/icons/lucide-trophy-3b6e10.svg` |
| 26 | visible | `images/icons/lucide-cpu-ffffff.svg`, `images/slide-08-lidar.png`, `images/slide-08-encoder.png`, `images/icons/lucide-grid-3x3-004eaa.svg`, `images/icons/lucide-refresh-cw-004eaa.svg` |
| 27 | visible | `images/icons/lucide-cpu-ffffff.svg` |
| 28 | visible | `images/icons/lucide-cpu-ffffff.svg` |
| 29 | visible | `images/icons/lucide-bar-chart-3-ffffff.svg` |
| 30 | visible | `images/icons/lucide-bar-chart-3-ffffff.svg`, `../../figures/06-results/experimental-environment.jpg`, `images/icons/lucide-circle-check-004eaa.svg`, `images/icons/lucide-route-004eaa.svg`, `images/icons/lucide-ruler-004eaa.svg`, `images/icons/tabler-dimensions-004eaa.svg` |
| 31 | visible | `images/icons/lucide-bar-chart-3-ffffff.svg`, `images/icons/lucide-gauge-ffffff.svg`, `images/icons/lucide-ruler-ffffff.svg`, `images/icons/lucide-radar-ffffff.svg`, `images/icons/lucide-map-3b6e10.svg` |
| 32 | visible | `images/icons/lucide-bar-chart-3-ffffff.svg`, `images/slide-14-occupancy-map-82-9.png`, `images/slide-14-occupancy-map-53-4.png`, `images/icons/lucide-repeat-3b6e10.svg`, `images/icons/lucide-frame-004eaa.svg` |
| 33 | visible | `images/icons/lucide-bar-chart-3-ffffff.svg`, `images/icons/lucide-refresh-cw-004eaa.svg` |
| 34 | visible | `images/icons/lucide-circle-check-ffffff.svg` |
| 35 | visible | `images/icons/lucide-circle-check-ffffff.svg`, `images/icons/lucide-bot-004eaa.svg`, `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-map-pinned-004eaa.svg`, `images/icons/lucide-compass-004eaa.svg` |
| 36 | visible | `images/icons/lucide-circle-check-ffffff.svg`, `images/icons/lucide-bot-3b6e10.svg`, `images/icons/lucide-gauge-3b6e10.svg`, `images/icons/lucide-map-pinned-3b6e10.svg`, `images/icons/lucide-compass-3b6e10.svg`, `images/icons/lucide-check-3b6e10.svg`, `images/icons/lucide-trending-up-ffffff.svg`, `images/icons/lucide-compass-004eaa.svg`, `images/icons/lucide-warehouse-004eaa.svg`, `images/icons/lucide-target-004eaa.svg`, `images/icons/lucide-factory-ffffff.svg`, `images/icons/lucide-thermometer-d99a00.svg`, `images/icons/lucide-shield-d99a00.svg`, `images/icons/simple-icons-ros-172435.svg` |
| 37 | visible | `images/icons/lucide-circle-check-ffffff.svg`, `images/v3/photo-elios-3.png`, `images/icons/lucide-hard-hat-004eaa.svg`, `images/v3/logo-codelco.svg`, `images/v3/photo-spot-inspection.jpg`, `images/icons/lucide-scan-search-004eaa.svg`, `images/v3/logo-glencore.svg`, `images/v3/logo-vale.png`, `images/v3/logo-emesent.svg`, `images/v3/logo-kinamics.png`, `images/icons/lucide-map-004eaa.svg` |
| 38 | visible | `images/icons/lucide-circle-check-ffffff.svg`, `images/icons/lucide-puzzle-004eaa.svg`, `images/icons/lucide-box-0e7490.svg`, `images/icons/lucide-sliders-horizontal-cb6b22.svg`, `images/icons/lucide-shield-check-3b6e10.svg` |
| 39 | visible | `images/icons/lucide-circle-check-ffffff.svg`, `images/icons/simple-icons-github-172435.svg`, `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-network-004eaa.svg`, `images/icons/lucide-circle-check-004eaa.svg` |
| 40 | visible | `images/slide-19-lidar-robot-line-illustration.png` |
| 41 | oculta | Ninguna |
| 42 | oculta | `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-target-004eaa.svg`, `images/icons/lucide-sliders-horizontal-004eaa.svg`, `images/icons/lucide-zap-004eaa.svg` |
| 43 | oculta | `images/icons/lucide-lock-004eaa.svg`, `images/v3/diagram-windup-base.svg`, `images/v3/diagram-windup-layer-1.svg`, `images/v3/diagram-windup-layer-2.svg` |
| 44 | oculta | `images/icons/lucide-timer-004eaa.svg`, `images/icons/lucide-battery-medium-004eaa.svg`, `images/icons/lucide-activity-004eaa.svg` |
| 45 | oculta | `images/icons/tabler-rotate-360-004eaa.svg`, `images/icons/lucide-radar-004eaa.svg`, `images/icons/lucide-piggy-bank-004eaa.svg` |
| 46 | oculta | `images/v3/drawing-l298n.svg`, `images/v3/photo-tb6612fng.jpg`, `images/v3/photo-drv8871.jpg` |
| 47 | oculta | `images/icons/lucide-trending-up-004eaa.svg` |
| 48 | oculta | `images/icons/lucide-wrench-3b6e10.svg`, `images/icons/simple-icons-github-172435.svg`, `images/icons/simple-icons-ros-172435.svg` |
| 49 | oculta | `images/slide-08-robot-car.png`, `images/slide-08-raspberry-pi.png`, `images/icons/lucide-wifi-4b5563.svg`, `images/slide-08-desktop-computer.png`, `images/slide-08-robot-on-screen.png`, `images/icons/lucide-shield-check-ffffff.svg`, `images/icons/lucide-split-004eaa.svg`, `images/icons/lucide-wifi-004eaa.svg`, `images/icons/lucide-network-004eaa.svg`, `images/icons/lucide-monitor-004eaa.svg`, `images/icons/lucide-trending-up-ffffff.svg`, `images/icons/lucide-piggy-bank-3b6e10.svg`, `images/icons/lucide-activity-3b6e10.svg`, `images/icons/lucide-bug-3b6e10.svg`, `images/icons/lucide-trending-up-3b6e10.svg` |
| 50 | oculta | `images/v3/backup-maps-vs-floor-plan.png`, `images/icons/lucide-circle-check-3b6e10.svg` |
| 51 | oculta | `images/v3/diagram-ros1-base.svg`, `images/v3/diagram-ros1-layer-1.svg`, `images/v3/diagram-ros2-base.svg`, `images/v3/diagram-ros2-layer-1.svg`, `images/icons/lucide-circle-x-c2410c.svg`, `images/icons/lucide-circle-check-3b6e10.svg` |
| 52 | oculta | `images/icons/lucide-check-3b6e10.svg`, `images/icons/lucide-circle-x-c2410c.svg` |
| 53 | oculta | `images/v3/diagram-gmapping.svg`, `images/v3/diagram-pose-graph-base.svg`, `images/v3/diagram-pose-graph-layer-1.svg`, `images/icons/lucide-circle-x-c2410c.svg`, `images/icons/lucide-circle-check-3b6e10.svg` |
| 54 | oculta | `images/v3/diagram-hector.svg`, `images/v3/diagram-cartographer.svg`, `images/icons/lucide-circle-x-c2410c.svg` |
| 55 | oculta | `images/v3/diagram-astar-base.svg`, `images/v3/diagram-astar-layer-1.svg`, `images/v3/diagram-astar-layer-2.svg`, `images/v3/diagram-rrt.svg`, `images/icons/lucide-circle-check-3b6e10.svg`, `images/icons/lucide-circle-x-c2410c.svg` |
| 56 | oculta | `images/v3/diagram-dwb.svg`, `images/v3/diagram-pure-pursuit.svg`, `images/v3/diagram-mppi.svg`, `images/icons/lucide-circle-check-3b6e10.svg`, `images/icons/lucide-circle-x-c2410c.svg` |
| 57 | oculta | `images/v3/diagram-frontier.svg`, `images/v3/diagram-info-gain.svg`, `images/v3/diagram-active-slam.svg`, `images/icons/lucide-circle-check-3b6e10.svg`, `images/icons/lucide-circle-x-c2410c.svg` |
| 58 | oculta | Ninguna |

## Imágenes por lámina, v2

Todas las láminas muestran además el logo de la UTEM, `images/logos/utem-logo-color.png`. Las rutas son relativas a esta carpeta. Tres láminas reutilizan figuras de la tesis desde `figures/`.

| Lámina | Estado | Imágenes |
|-------|-------|--------|
| 1 | visible | `images/slide-01-prototype-three-quarter-cutout.png` |
| 2 | visible | Ninguna |
| 3 | visible | Ninguna |
| 4 | visible | `images/slide-04-perception.svg`, `images/slide-04-localization.svg`, `images/slide-04-control.svg`, `images/slide-04-planning.svg` |
| 5 | visible | Ninguna |
| 6 | visible | `images/slide-06-robot.svg`, `images/slide-04-control.svg`, `images/slide-06-map.svg`, `images/slide-06-compass.svg` |
| 7 | visible | Ninguna |
| 8 | visible | `images/slide-08-encoder.png`, `images/slide-08-motor.png`, `images/slide-08-robot-car.png`, `images/slide-08-lidar.png`, `images/slide-08-arduino.png`, `images/slide-08-raspberry-pi.png`, `images/slide-08-robot-on-screen.png`, `images/slide-08-navigation-arrow.png`, `images/slide-08-pose-path.png`, `images/slide-08-map-outline.png`, `images/slide-08-desktop-computer.png` |
| 9 | visible | `images/slide-09-prototype-top-view.png`, `images/slide-01-prototype-three-quarter-cutout.png` |
| 10 | visible | Ninguna |
| 11 | visible | Ninguna |
| 12 | visible | `images/slide-12-ruler.svg`, `images/slide-12-speedometer.svg`, `images/slide-12-floor-plan.svg`, `images/slide-12-finish-flag.svg` |
| 13 | visible | Ninguna |
| 14 | visible | `images/slide-14-occupancy-map-82-9.png`, `images/slide-14-occupancy-map-53-4.png` |
| 15 | visible | `images/slide-15-real-navigation-capture.jpg`, `../../figures/06-results/real-navigation-exploration-part4.png`, `images/slide-15-low-poly-robot-cutout.png` |
| 16 | visible | Ninguna |
| 17 | visible | Ninguna |
| 18 | visible | Ninguna |
| 19 | visible | `images/slide-19-lidar-robot-line-illustration.png` |
| 20 | oculta | Ninguna |
| 21 | oculta | `images/slide-21-gazebo-laser-robot.jpg`, `images/slide-21-experimental-environment.jpg` |
| 22 | oculta | Ninguna |
| 23 | oculta | Ninguna |
| 24 | oculta | `images/slide-12-speedometer.svg`, `images/slide-24-algorithm.svg`, `images/slide-06-robot.svg`, `images/slide-24-tuning.svg` |
| 25 | oculta | `../../figures/06-results/final-step-response.png`, `../../figures/06-results/final-step-response-pso.png` |
| 26 | oculta | `images/slide-26-measure.svg`, `images/slide-26-wall.svg`, `images/slide-26-wider.svg` |
| 27 | oculta | `images/slide-27-true-value.svg`, `images/slide-27-idea.svg` |
| 28 | oculta | `images/slide-06-map.svg`, `images/slide-04-localization.svg`, `images/slide-04-planning.svg`, `images/slide-28-fixed-goal.svg`, `images/slide-28-saved-map.svg`, `images/slide-28-success-measure.svg` |
