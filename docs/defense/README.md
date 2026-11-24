# Defensa

Material para la defensa de la tesis.

- `slides-v3.pptx`: la presentación vigente. Tiene 24 láminas visibles y 12 ocultas: un índice y 11 respaldos para las preguntas. Trae el video de demostración incrustado, animaciones por clic, transiciones y el guion en las notas del orador.
- `slides-v3.pdf`: la misma presentación en PDF, con las láminas ocultas al final. El video aparece como imagen fija.
- `script-v3.md`: el guion de la v3, lo que se dice en cada lámina, el mapa de las láminas de respaldo y un glosario breve.
- `slides-v2.pptx` y `script.md`: la versión anterior, de 28 láminas, y su guion.
- `images/`: todas las imágenes que usan las láminas, nombradas por la primera lámina de la v2 donde aparecen, más `images/logos/`. Las imágenes que solo existían dentro de la presentación se extrajeron byte a byte, así que conservan la calidad guardada en el `.pptx`.
- `images/v3/`: lo que agrega la v3. Logos (`logo-*`) y fotos (`photo-*`) de empresas y equipos, copias reducidas de figuras de la tesis (`backup-*`), la imagen fija del video e íconos SVG dibujados a mano (`icon-*.svg`, con `-white` los de trazo blanco).
- `images/icons/`: íconos de Lucide, Tabler y Simple Icons bajados de Iconify, nombrados `{set}-{icono}-{color}.svg`. Autores y licencias en `docs/credits.md`.

El video de la lámina 2 es una copia comprimida y sin audio del video público del ensayo en YouTube (decisión 0004). El archivo original queda en `videos/`, fuera de git. Las grabaciones de los ensayos y su feedback son privados y quedan solo en el computador del autor.

La v3 se generó con un script de Python que no forma parte del repositorio. `slides-v3.backup.pptx` y `script-v3.backup.md` son copias locales de la versión anterior y no se suben a git, porque el historial ya la guarda.

## Imágenes por lámina, v3

Todas las láminas muestran además el logo de la UTEM, `images/logos/utem-logo-color.png`, salvo la 24. Las rutas son relativas a esta carpeta. Las láminas de la 25 a la 36 están ocultas.

| Lámina | Estado | Imágenes |
|-------|-------|--------|
| 1 | visible | `images/slide-01-prototype-three-quarter-cutout.png` |
| 2 | visible | `images/v3/slide-02-demo-poster.jpg` (imagen fija del video incrustado) |
| 3 | visible | `images/icons/lucide-triangle-alert-ffffff.svg`, `images/icons/lucide-layers-ffffff.svg`, `images/icons/lucide-target-ffffff.svg`, `images/icons/lucide-cpu-ffffff.svg`, `images/icons/lucide-bar-chart-3-ffffff.svg`, `images/icons/lucide-circle-check-ffffff.svg` |
| 4 | visible | `images/icons/lucide-triangle-alert-ffffff.svg`, `images/v3/photo-elios-3.png`, `images/icons/lucide-hard-hat-004eaa.svg`, `images/v3/logo-codelco.svg`, `images/v3/photo-spot-inspection.jpg`, `images/icons/lucide-scan-search-004eaa.svg`, `images/v3/logo-glencore.svg`, `images/v3/logo-vale.png`, `images/slide-14-occupancy-map-82-9.png`, `images/icons/lucide-map-004eaa.svg` |
| 5 | visible | `images/icons/lucide-factory-ffffff.svg`, `images/v3/photo-spot-inspection.jpg`, `images/v3/logo-boston-dynamics.svg`, `images/v3/logo-emesent.svg`, `images/v3/logo-kinamics.png`, `images/icons/lucide-route-004eaa.svg`, `images/icons/lucide-box-004eaa.svg`, `images/icons/lucide-gamepad-2-004eaa.svg`, `images/icons/lucide-graduation-cap-ffffff.svg`, `images/v3/photo-turtlebot3-burger.png`, `images/v3/logo-robotis.svg`, `images/icons/lucide-radar-004eaa.svg`, `images/icons/lucide-book-open-004eaa.svg`, `images/icons/lucide-bot-ffffff.svg`, `images/slide-01-prototype-three-quarter-cutout.png`, `images/icons/lucide-cpu-004eaa.svg` |
| 6 | visible | `images/slide-01-prototype-three-quarter-cutout.png`, `images/icons/lucide-radar-ffffff.svg`, `images/icons/lucide-map-pinned-ffffff.svg`, `images/icons/lucide-gauge-ffffff.svg`, `images/icons/lucide-route-ffffff.svg` |
| 7 | visible | `images/icons/lucide-layers-ffffff.svg`, `images/icons/lucide-gauge-ffffff.svg`, `images/slide-08-robot-car.png`, `images/icons/lucide-radar-ffffff.svg`, `images/slide-08-lidar.png`, `images/icons/lucide-map-pinned-ffffff.svg`, `images/slide-08-map-outline.png`, `images/icons/lucide-route-ffffff.svg`, `images/slide-08-navigation-arrow.png` |
| 8 | visible | `images/v3/photo-spot-inspection.jpg`, `images/v3/photo-turtlebot3-burger.png`, `images/slide-01-prototype-three-quarter-cutout.png`, `images/icons/lucide-lock-open-004eaa.svg`, `images/icons/lucide-route-004eaa.svg`, `images/icons/lucide-ruler-004eaa.svg`, `images/icons/lucide-coins-004eaa.svg` |
| 9 | visible | `images/icons/lucide-target-ffffff.svg`, `images/icons/lucide-bot-004eaa.svg`, `images/icons/lucide-map-004eaa.svg`, `images/icons/lucide-compass-004eaa.svg`, `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-map-pinned-004eaa.svg`, `images/icons/lucide-square-check-big-004eaa.svg`, `images/icons/lucide-target-004eaa.svg` |
| 10 | visible | `images/slide-08-encoder.png`, `images/slide-08-motor.png`, `images/slide-08-robot-car.png`, `images/slide-08-lidar.png`, `images/slide-08-arduino.png`, `images/slide-08-raspberry-pi.png`, `images/slide-08-robot-on-screen.png`, `images/slide-08-navigation-arrow.png`, `images/slide-08-pose-path.png`, `images/slide-08-map-outline.png`, `images/slide-08-desktop-computer.png` |
| 11 | visible | `../../figures/05-implementation/prototype-left-side.jpg`, `../../figures/05-implementation/prototype-top-view.jpg`, `images/icons/lucide-printer-004eaa.svg`, `images/icons/lucide-cog-004eaa.svg`, `images/icons/lucide-radar-004eaa.svg`, `images/icons/lucide-zap-004eaa.svg`, `../../figures/05-implementation/gazebo-laser-robot.png`, `images/icons/lucide-box-004eaa.svg` |
| 12 | visible | `images/icons/lucide-layers-004eaa.svg`, `images/icons/simple-icons-ros-172435.svg`, `images/icons/lucide-radar-004eaa.svg`, `images/slide-08-lidar.png`, `images/icons/lucide-map-pinned-004eaa.svg`, `images/slide-08-map-outline.png`, `images/icons/lucide-route-004eaa.svg`, `images/slide-08-navigation-arrow.png`, `images/icons/lucide-box-004eaa.svg` |
| 13 | visible | `images/icons/lucide-activity-ffffff.svg`, `images/icons/tabler-chart-dots-3-ffffff.svg`, `images/icons/lucide-sliders-horizontal-ffffff.svg` |
| 14 | visible | `images/icons/lucide-radar-004eaa.svg`, `images/icons/lucide-rotate-cw-004eaa.svg`, `images/icons/lucide-grid-3x3-004eaa.svg`, `images/icons/lucide-refresh-cw-004eaa.svg` |
| 15 | visible | Ninguna |
| 16 | visible | `../../figures/06-results/experimental-environment.jpg`, `images/icons/lucide-circle-check-004eaa.svg`, `images/icons/lucide-route-004eaa.svg`, `images/icons/lucide-ruler-004eaa.svg`, `images/icons/tabler-dimensions-004eaa.svg` |
| 17 | visible | `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-ruler-3b6e10.svg`, `images/icons/tabler-rotate-360-c2410c.svg` |
| 18 | visible | `images/slide-14-occupancy-map-82-9.png`, `images/slide-14-occupancy-map-53-4.png`, `images/icons/lucide-scan-004eaa.svg`, `images/icons/lucide-frame-004eaa.svg`, `images/icons/lucide-ruler-004eaa.svg` |
| 19 | visible | `images/icons/lucide-timer-ffffff.svg`, `images/icons/lucide-map-004eaa.svg`, `images/icons/lucide-target-004eaa.svg`, `images/icons/lucide-route-004eaa.svg`, `../../figures/06-results/real-navigation-exploration-part3.png` |
| 20 | visible | `images/icons/lucide-circle-check-ffffff.svg`, `images/icons/lucide-bot-004eaa.svg`, `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-map-pinned-004eaa.svg`, `images/icons/lucide-compass-004eaa.svg` |
| 21 | visible | `images/icons/lucide-circle-check-ffffff.svg`, `images/icons/lucide-bot-3b6e10.svg`, `images/icons/lucide-gauge-3b6e10.svg`, `images/icons/lucide-map-pinned-3b6e10.svg`, `images/icons/lucide-compass-3b6e10.svg`, `images/icons/lucide-check-3b6e10.svg`, `images/icons/lucide-trending-up-ffffff.svg`, `images/icons/lucide-arrow-right-004eaa.svg`, `images/icons/lucide-factory-ffffff.svg`, `images/icons/lucide-arrow-right-d99a00.svg` |
| 22 | visible | `images/icons/lucide-network-004eaa.svg`, `images/icons/lucide-box-004eaa.svg`, `images/icons/lucide-sliders-horizontal-004eaa.svg`, `images/icons/lucide-shield-check-004eaa.svg`, `images/icons/lucide-compass-3b6e10.svg`, `images/icons/lucide-target-3b6e10.svg`, `images/icons/lucide-refresh-cw-3b6e10.svg`, `images/icons/lucide-list-checks-3b6e10.svg` |
| 23 | visible | `images/icons/lucide-ruler-004eaa.svg`, `images/icons/lucide-network-004eaa.svg`, `images/icons/lucide-lock-open-004eaa.svg` |
| 24 | visible | `images/slide-19-lidar-robot-line-illustration.png` |
| 25 | oculta | Ninguna |
| 26 | oculta | Ninguna |
| 27 | oculta | `images/icons/lucide-timer-004eaa.svg`, `images/icons/lucide-gauge-004eaa.svg`, `images/icons/lucide-activity-004eaa.svg`, `images/icons/lucide-shield-check-004eaa.svg` |
| 28 | oculta | `images/icons/lucide-activity-004eaa.svg`, `images/icons/tabler-chart-dots-3-004eaa.svg`, `images/icons/lucide-bot-004eaa.svg`, `images/icons/lucide-sliders-horizontal-004eaa.svg`, `images/icons/lucide-zap-off-004eaa.svg`, `images/icons/lucide-binary-004eaa.svg` |
| 29 | oculta | `../../figures/06-results/final-step-response.png`, `../../figures/06-results/final-step-response-pso.png` |
| 30 | oculta | `images/icons/lucide-rotate-ccw-c2410c.svg`, `images/icons/tabler-rotate-360-c2410c.svg`, `images/icons/lucide-ruler-3b6e10.svg`, `images/icons/lucide-compass-3b6e10.svg` |
| 31 | oculta | `images/v3/backup-circuit-diagram.png`, `images/icons/lucide-audio-waveform-004eaa.svg`, `images/icons/lucide-battery-charging-004eaa.svg`, `images/icons/lucide-shield-004eaa.svg`, `images/icons/lucide-cpu-6b7280.svg`, `images/v3/photo-tb6612fng.jpg` |
| 32 | oculta | Ninguna |
| 33 | oculta | `images/icons/lucide-wrench-3b6e10.svg`, `images/icons/simple-icons-github-172435.svg`, `images/icons/simple-icons-ros-172435.svg` |
| 34 | oculta | `images/slide-08-robot-car.png`, `images/slide-08-raspberry-pi.png`, `images/icons/lucide-wifi-4b5563.svg`, `images/slide-08-desktop-computer.png`, `images/slide-08-robot-on-screen.png` |
| 35 | oculta | `images/v3/backup-maps-vs-floor-plan.png`, `images/icons/lucide-ruler-3b6e10.svg`, `images/icons/lucide-grid-3x3-004eaa.svg`, `images/icons/lucide-layers-004eaa.svg`, `images/icons/lucide-scan-004eaa.svg` |
| 36 | oculta | `images/icons/lucide-layers-004eaa.svg`, `images/icons/lucide-map-004eaa.svg`, `images/icons/lucide-route-004eaa.svg`, `images/icons/lucide-compass-004eaa.svg` |

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
