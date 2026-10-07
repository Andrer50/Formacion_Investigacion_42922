# Taxonomía y Caracterización — Documentación paso a paso (guía de Resultados Q3-Q2)

Corpus congelado: **N = 110** (`project/metodologia/outputs/corpus_included_final.csv`). Guía: `assets/taxonomia_y_caracterizacion/documents/Guía_de_Resultados_...pdf`.
Artículo en formato IEEE: `Taxonomia_y_Caracterizacion_IEEE.docx`. Borrador anterior: `borrador_previo_main.md`.

## Estado por paso de la guía

| Paso | Qué pide la guía | Qué se hizo | Evidencia | Estado |
|:-:|:--|:--|:--|:-:|
| 1 | Congelar el corpus | N = 110 fijo; ID `[S###]` | `matriz_extraccion.csv` | Hecho (ver NOTAS §1–5) |
| 2 | Declarar método de síntesis por pregunta | PD1–PD3, PI1, PI4: mapeo sistemático / conteos; PI2–PI3 fuera de alcance | Intro del docx | Hecho |
| 3 | Matriz de extracción + doble codificación 20 % | Codificación automática (título+resumen+keywords) con término de evidencia por celda; muestra de 22 estudios | `matriz_extraccion.csv`, `muestra_doble_codificacion.csv` | Parcial: κ manual vs auto hecho; falta κ entre 2 humanos |
| 4 | Bibliometría (año, fuentes, países, redes) | Tablas II–III, Fig. 1–2, red de keywords Fig. 7 (umbral ≥ 4) | `outputs/tablas`, `outputs/figuras` | Hecho (países solo WoS) |
| 5 | Clasificar diseños metodológicos | Tabla IV | `T_PD3_diseno.csv` | Hecho (automático) |
| 6 | Reportar calidad QA, κ ponderado | El corpus no tiene puntajes QA por estudio | — | **Pendiente** |
| 7 | Aplicar la síntesis (mapeo burbujas) | Fig. 6 enfoque × tipología | `T_mapeo_enfoque_x_tipologia.csv` | Hecho |
| 8 | Sensibilidad | Proxy por pertinencia (N = 75), no por QA | `T_sensibilidad_enfoque.csv` | Hecho (proxy) |
| 9 | GRADE-CERQual | Requiere juicio de revisores | — | **Pendiente** |
| 10 | Tabla y figura por pregunta | 8 tablas, 7 figuras, 300 ppp, 8 pt | docx | Hecho |
| 11 | Redactar (apertura, desarrollo, contraste, cierre) | Secciones A–G del docx | docx | Hecho |
| 12 | Verificar trazabilidad | Cifras generadas por script; citas `[S###]`; "Anexo A" = matriz | scripts | Hecho |
| 13 | Publicar en OSF/Zenodo + DOI | Carpeta lista para subir | — | Pendiente (equipo) |

## Pregunta → tabla/figura
PD1: Tabla II, Fig. 1 · PD2: Tabla III, Fig. 2 · PD3: Tabla IV, Fig. 3 · PI1: Tabla V, Fig. 4 · inputs: Tabla VI · PI4: Tabla VII, Fig. 5–6 · sensibilidad: Tabla VIII.

## Cómo reproducir
```
python project/taxonomia_y_caracterizacion/scripts/01_codificar_corpus.py
python project/taxonomia_y_caracterizacion/scripts/02_analisis_tablas_figuras.py
python project/taxonomia_y_caracterizacion/scripts/03_muestra_kappa.py generar   # luego calcular
python project/taxonomia_y_caracterizacion/scripts/04_generar_docx_ieee.py
```
Requiere pandas, matplotlib, networkx, python-docx, xlrd. Si se corrige el corpus, todo se regenera.

## Cómo cerrar los pendientes
1. Dos revisores llenan sin verse `muestra_doble_codificacion.csv` (columnas A_ y B_) → `03_muestra_kappa.py calcular` → pegar κ en el docx (amarillo).
2. Codificar a mano S001, S003, S004 (sin resumen).
3. Revisar `alerta_pertinencia.csv`; si se excluyen estudios, actualizar PRISMA y rerun.
