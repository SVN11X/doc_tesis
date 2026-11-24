# Defensa

Material para la defensa de la tesis.

- `slides-v3.pptx`: la presentación vigente. Tiene 24 láminas visibles y 18 ocultas: un índice y 17 respaldos para las preguntas. Trae el video de demostración incrustado, animaciones por clic, transiciones y el guion en las notas del orador.
- `slides-v3.pdf`: la misma presentación en PDF, con las láminas ocultas al final. El video aparece como imagen fija.
- `script-v3.md`: el guion de la v3, lo que se dice en cada lámina, el mapa de las láminas de respaldo y un glosario breve.
- `slides-v2.pptx` y `script.md`: la versión anterior, de 28 láminas, y su guion.
- `images/`: todas las imágenes que usan las láminas, nombradas por la primera lámina de la v2 donde aparecen, más `images/logos/`. Las imágenes que solo existían dentro de la presentación se extrajeron byte a byte, así que conservan la calidad guardada en el `.pptx`.
- `images/v3/`: lo que agrega la v3. Íconos SVG dibujados para esta presentación, nombrados `icon-*.svg` (con `-white` los de trazo blanco), una copia reducida del esquema eléctrico de la tesis y la imagen fija del video.

El video de la lámina 2 es una copia comprimida y sin audio del video público del ensayo en YouTube (decisión 0004). El archivo original queda en `videos/`, fuera de git. Las grabaciones de los ensayos y su feedback son privados y quedan solo en el computador del autor.

La v3 se generó con un script de Python que no forma parte del repositorio. Los cambios siguientes se hacen directamente en PowerPoint.

## Imágenes por lámina, v3

Todas las láminas muestran además el logo de la UTEM, `images/logos/utem-logo-color.png`, salvo la 24. Las rutas son relativas a esta carpeta. Las láminas de la 25 a la 42 están ocultas.

| Lámina | Estado | Imágenes |
|-------|-------|--------|
| 1 | visible | `images/slide-01-prototype-three-quarter-cutout.png` |
| 2 | visible | `images/v3/slide-02-demo-poster.jpg` (imagen fija del video incrustado) |
| 3 | visible | Ninguna |
| 4 | visible | `images/v3/icon-mining-helmet.svg`, `images/v3/icon-inspection.svg`, `images/v3/icon-floor-plan.svg` |
| 5 | visible | `images/v3/icon-drone-white.svg`, `images/v3/icon-education-white.svg`, `images/v3/icon-open-lock-white.svg` |
| 6 | visible | `images/slide-06-robot.svg` |
| 7 | visible | Ninguna |
| 8 | visible | Ninguna |
| 9 | visible | `images/slide-06-robot.svg`, `images/slide-12-speedometer.svg`, `images/slide-06-map.svg`, `images/slide-06-compass.svg` |
| 10 | visible | `images/v3/icon-laser-white.svg`, `images/v3/icon-repeat-white.svg`, `images/v3/icon-chip-white.svg`, `images/v3/icon-bolt-white.svg`, `images/v3/icon-wrench-white.svg`, `images/v3/icon-wifi.svg`, `images/v3/icon-floor-plan-white.svg`, `images/v3/icon-route-white.svg`, `images/v3/icon-target-white.svg`, `images/v3/icon-laptop-white.svg` |
| 11 | visible | `../../figures/05-implementation/prototype-left-side.jpg`, `../../figures/05-implementation/prototype-top-view.jpg`, `../../figures/05-implementation/gazebo-laser-robot.png` |
| 12 | visible | Ninguna |
| 13 | visible | `images/v3/icon-inspection.svg`, `images/slide-24-algorithm.svg`, `images/slide-24-tuning.svg`, `../../figures/06-results/final-step-response-pso.png`, `../../figures/06-results/final-step-response.png` |
| 14 | visible | `images/v3/icon-laser.svg`, `images/v3/icon-repeat.svg`, `images/v3/icon-floor-plan.svg`, `images/v3/icon-replan.svg` |
| 15 | visible | Ninguna |
| 16 | visible | `../../figures/06-results/experimental-environment.jpg`, `images/v3/icon-check.svg`, `images/v3/icon-route.svg`, `images/v3/icon-floor-plan.svg`, `images/v3/icon-repeat.svg` |
| 17 | visible | `images/slide-12-speedometer.svg`, `images/slide-12-ruler.svg`, `images/slide-06-compass.svg` |
| 18 | visible | `images/slide-14-occupancy-map-82-9.png`, `images/slide-14-occupancy-map-53-4.png` |
| 19 | visible | `images/v3/icon-check.svg` |
| 20 | visible | Ninguna |
| 21 | visible | Ninguna |
| 22 | visible | Ninguna |
| 23 | visible | `images/slide-12-speedometer.svg`, `images/v3/icon-link.svg`, `images/v3/icon-open-lock.svg` |
| 24 | visible | `images/slide-19-lidar-robot-line-illustration.png` |
| 25 | oculta | Ninguna |
| 26 | oculta | Ninguna |
| 27 | oculta | Ninguna |
| 28 | oculta | `images/slide-12-speedometer.svg`, `images/slide-24-algorithm.svg`, `images/slide-06-robot.svg`, `images/slide-24-tuning.svg` |
| 29 | oculta | `../../figures/06-results/final-step-response.png`, `../../figures/06-results/final-step-response-pso.png` |
| 30 | oculta | `../../figures/06-results/rotation-drift-bars.png` |
| 31 | oculta | `images/v3/backup-circuit-diagram.png` |
| 32 | oculta | Ninguna |
| 33 | oculta | Ninguna |
| 34 | oculta | Ninguna |
| 35 | oculta | Ninguna |
| 36 | oculta | `images/v3/icon-chip-white.svg`, `images/v3/icon-wifi-white.svg`, `images/v3/icon-laptop-white.svg` |
| 37 | oculta | Ninguna |
| 38 | oculta | Ninguna |
| 39 | oculta | `images/slide-26-measure.svg`, `images/slide-26-wall.svg`, `images/slide-26-wider.svg` |
| 40 | oculta | `images/slide-27-true-value.svg`, `images/slide-27-idea.svg` |
| 41 | oculta | `images/slide-06-map.svg`, `images/slide-04-localization.svg`, `images/slide-04-planning.svg`, `images/slide-28-fixed-goal.svg`, `images/slide-28-saved-map.svg`, `images/slide-28-success-measure.svg` |
| 42 | oculta | Ninguna |

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
