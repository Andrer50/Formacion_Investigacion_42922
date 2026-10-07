# Taxonomía y Caracterización — Documentación paso a paso

**Curso:** Formación para la Investigación (UTP 2026-1) · **Corpus congelado:** N = 110 estudios primarios (`project/metodologia/outputs/corpus_included_final.csv`)
**Guía seguida:** *Guía de Resultados para Revisiones Sistemáticas Q3-Q2 PAIREF* (`assets/taxonomia_y_caracterizacion/documents/`, 15 diapositivas, 13 pasos)
**Entregable en formato IEEE:** `Taxonomia_y_Caracterizacion_IEEE.docx` · **Datos:** `Corpus_congelado_N110.xlsx` · **Borrador previo:** `borrador_previo_main.md`

Preguntas cubiertas: **PD1** (producción anual), **PD2** (fuentes, países, autores), **PD3** (diseño y base de validación), **PI1** (arquitecturas y enfoques algorítmicos), **PI4** (tipologías documentales y sistemas empresariales). PI2 y PI3 requieren extracción de métricas a texto completo y no corresponden a esta sección.

## Resumen del estado de cumplimiento de la guía

| Paso | Exigencia de la guía | Estado | Dónde está |
|:-:|:--|:-:|:--|
| 1 | Congelar el corpus y asignar IDs | Cumplido (con observaciones, ver §Paso 1) | Excel hoja *Corpus* |
| 2 | Declarar método de síntesis por pregunta | Cumplido | Paso 2 |
| 3 | Matriz de extracción y doble codificación 20 % | **Parcial:** κ manual vs. automática hecho; falta κ entre 2 humanos | Pasos 3 y 6 |
| 4 | Análisis bibliométrico y red de co-ocurrencia | Cumplido | Paso 4 |
| 5 | Clasificar diseños y bases de validación | Cumplido (automático, preliminar) | Paso 5 |
| 6 | Fiabilidad (κ) y calidad (QA) | **Parcial:** κ hecho; **QA no existe en los datos** | Paso 6 |
| 7 | Síntesis temática y mapeo | Cumplido | Paso 7 |
| 8 | Análisis de sensibilidad | Cumplido con criterio de pertinencia (no QA) | Paso 8 |
| 9 | Certeza GRADE-CERQual | Cumplido como propuesta; **falta consenso** | Paso 9 |
| 10 | Una tabla y figura por pregunta (IEEE) | Cumplido | Paso 10 |
| 11 | Redacción por bloques (apertura, desarrollo, contraste, cierre) | Cumplido | Paso 11 |
| 12 | Trazabilidad de cada cifra | Cumplido | Paso 12 |
| 13 | Publicación con DOI (OSF/Zenodo) | **Pendiente (equipo)** | Paso 13 |

---

## Paso 1. Congelar el corpus
- Se usa el corpus de `corpus_included_final.csv` (N = 110), con identificadores `[S001]–[S110]` que se citan en todo el texto. El Excel `Corpus_congelado_N110.xlsx` conserva la versión de trabajo.
- Origen: 65 estudios de Scopus y 45 de Web of Science; 2020–2025.
- **Observación crítica (ver Paso 8 y Notas):** una revisión manual de la muestra mostró que 12 de 22 estudios (55 %) no tratan documentos (EEG, agricultura, vacunación, etc.), porque la sigla «ERP» de la ecuación también recupera *Event-Related Potential*. Un filtro de dominio estricto deja **75 de 110** estudios en dominio.

## Paso 2. Declarar el método de síntesis por pregunta
| Pregunta | Método | Producto |
|:--|:--|:--|
| PD1 | Conteo descriptivo por año | Tabla II, Fig. 1 |
| PD2 | Conteo de fuentes, países, autores y citas | Tabla III, Fig. 2 |
| PD3 | Clasificación del diseño y la base de validación | Tabla IV, Fig. 3 |
| PI1 | Síntesis temática (mapeo sistemático) por enfoque algorítmico | Tabla V, Fig. 4 |
| PI4 | Mapeo de tipología documental y sistema empresarial | Tablas VI–VII, Fig. 5–6 |

Las categorías no son mutuamente excluyentes; los porcentajes se calculan sobre N y no suman 100 %. «No reporta» = sin evidencia en título/resumen/palabras clave.

## Paso 3. Matriz de extracción
- Script `scripts/01_codificar_corpus.py` → `outputs/matriz_extraccion.csv`.
- Cada estudio se codifica con diccionarios de términos aplicados a título + resumen + palabras clave; **cada celda guarda el término que disparó la categoría** (columnas `*_evidencia`). No se usaron las columnas PI1–PI4 del corpus de metodología porque están asignadas por posición en el script `generate_corpus_110.py`, no por lectura.
- Esquema de clasificación:

| Eje | Categorías |
|:--|:--|
| Enfoque algorítmico | Reglas/plantillas · Secuencial · Grafo · Multimodal/generativo |
| Inputs de datos | Textual · Layout · Visual · Hand-crafted |
| Tipología documental | Facturas · Recibos · Formularios · Contratos · Otros financieros · Tablas |
| Sistema empresarial | ERP (excluye *Event-Related Potential*) · CRM · DMS · Contabilidad/finanzas |
| Base de validación | Benchmark público · Dataset privado/real · Mixta |
| Diseño | Artefacto · Benchmark/experimento · Caso real · Revisión |

- Limitaciones: 3 estudios (incluidos 3 nucleares: S001, S003, S004) no tienen resumen en la exportación y se codificaron solo con el título; requieren codificación manual.
- Doble codificación del 20 %: `outputs/muestra_doble_codificacion.csv` (22 estudios, semilla 2026), con columnas A_ y B_ para dos revisores humanos y M_ (codificación manual ya hecha).

## Paso 4. Análisis bibliométrico (PD1–PD2)
**Tabla II. Distribución anual**

| Año | n | % |
|---|---|---|
| 2020 | 2 | 1,8 |
| 2021 | 4 | 3,6 |
| 2022 | 6 | 5,5 |
| 2023 | 13 | 11,8 |
| 2024 | 17 | 15,5 |
| 2025 | 68 | 61,8 |

![Fig. 1. Distribución de estudios por año.](outputs/figuras/fig1_produccion_anual.png)

*Fig. 1. Distribución de estudios por año.* Fuente: elaboración propia a partir de [S001]–[S110].

**Tabla III. Fuentes más frecuentes** (87 fuentes; 77 aparecen una sola vez)

| Fuente | n | % |
|---|---|---|
| Lecture Notes in Computer Science | 10 | 9,1 |
| International Journal on Document Analysis and Recognition | 4 | 3,6 |
| IEEE Access | 4 | 3,6 |
| Lecture Notes in Networks and Systems | 3 | 2,7 |
| Electronics (Switzerland) | 2 | 1,8 |

**Países** (solo 55 estudios con afiliación, porque el export de Scopus no la trae)

| País | n | % |
|---|---|---|
| China | 14 | 25,5 |
| Alemania | 8 | 14,5 |
| Turquía | 8 | 14,5 |
| India | 6 | 10,9 |
| Malasia | 3 | 5,5 |
| Canadá | 3 | 5,5 |
| Arabia Saudita | 3 | 5,5 |
| Taiwán | 2 | 3,6 |

![Fig. 2. Países de afiliación.](outputs/figuras/fig2_paises.png)

*Fig. 2. Países de afiliación.* Fuente: elaboración propia a partir de [S001]–[S110].

- Autores: 29 autores aparecen en más de un estudio (máximo 3). Citas: mediana 2, máximo 174, 19 sin citas (n = 107).
- **Red de co-ocurrencia de palabras clave** (alternativa a VOSviewer; umbral ≥ 4, sinónimos unificados, solo estudios sin señal de otro dominio):

![Fig. 7. Red de co-ocurrencia de palabras clave de autor.](outputs/figuras/fig7_coocurrencia_keywords.png)

*Fig. 7. Red de co-ocurrencia de palabras clave de autor.* Fuente: elaboración propia a partir de [S001]–[S110].

- Advertencia: el corpus se armó con un puntaje de palabras clave y luego se ordenó por año, por lo que la distribución anual (68 estudios en 2025) **no mide la evolución del campo**.

## Paso 5. Diseño y base de validación (PD3)
**Tabla IV-a. Diseño**

| Categoría | n | % |
|---|---|---|
| Desarrollo de artefacto / sistema | 92 | 83,6 |
| Benchmark / experimento comparativo | 81 | 73,6 |
| Estudio de caso real | 29 | 26,4 |
| Revisión / survey | 6 | 5,5 |
| No reporta | 6 | 5,5 |

**Tabla IV-b. Base de validación**

| Categoría | n | % |
|---|---|---|
| Benchmark público | 30 | 27,3 |
| Dataset privado / datos reales | 18 | 16,4 |
| Mixta (público + privado) | 13 | 11,8 |
| No reporta | 49 | 44,5 |

![Fig. 3. Base de validación.](outputs/figuras/fig5_base_validacion.png)

*Fig. 3. Base de validación.* Fuente: elaboración propia a partir de [S001]–[S110].

## Paso 6. Fiabilidad de la codificación (κ de Cohen) y calidad (QA)
Un revisor codificó manualmente la muestra del 20 % leyendo cada resumen (`scripts/05_kappa_manual_y_dominio.py`). κ entre la codificación manual y la automática:

| subconjunto | variable | acuerdo_% | kappa_manual_vs_auto | interpretacion |
|---|---|---|---|---|
| Muestra completa (n=22) | enfoque_dominante | 40,9 | 0,34 | Inaceptable: reformular categorías (k <= 0,60) |
| Muestra completa (n=22) | tipologia_dominante | 22,7 | 0,14 | Inaceptable: reformular categorías (k <= 0,60) |
| Muestra completa (n=22) | base_validacion | 22,7 | 0,00 | Inaceptable: reformular categorías (k <= 0,60) |
| Solo estudios en dominio (n=10) | enfoque_dominante | 90,0 | 0,85 | Casi perfecto / aceptable (k >= 0,80) |
| Solo estudios en dominio (n=10) | tipologia_dominante | 50,0 | 0,38 | Inaceptable: reformular categorías (k <= 0,60) |
| Solo estudios en dominio (n=10) | base_validacion | 50,0 | 0,17 | Inaceptable: reformular categorías (k <= 0,60) |

- Umbrales de la guía: κ ≥ 0,80 continuar · 0,61–0,79 reconciliar · ≤ 0,60 reformular categorías.
- **Resultado:** solo el enfoque algorítmico en estudios en dominio alcanza el umbral. La tipología documental y la base de validación **no** lo alcanzan, por lo que se reportan como preliminares y deben codificarse manualmente en su totalidad.
- **Pendiente:** κ entre dos revisores humanos independientes (columnas A_ y B_; luego `python scripts/03_muestra_kappa.py calcular`).
- **Calidad (QA):** el corpus no contiene puntajes de calidad por estudio; no se inventan. Si el equipo aplica una lista de verificación a texto completo, el Paso 8 puede rehacerse con ese criterio.

## Paso 7. Síntesis temática y mapeo (PI1, PI4)
**Tabla V. Enfoque algorítmico y distribución por periodo**

| Categoría | n | % |
|---|---|---|
| Reglas / plantillas | 19 | 17,3 |
| Secuencial | 53 | 48,2 |
| Grafo | 16 | 14,5 |
| Multimodal / generativo | 48 | 43,6 |
| No reporta | 25 | 22,7 |

| Periodo | N | Reglas / plantillas | Secuencial | Grafo | Multimodal / generativo |
|---|---|---|---|---|---|
| 2020-2022 | 12 | 0 | 4 | 5 | 6 |
| 2023-2024 | 30 | 6 | 14 | 8 | 12 |
| 2025 | 68 | 13 | 35 | 3 | 30 |

![Fig. 4. Enfoque algorítmico.](outputs/figuras/fig3_enfoque.png)

*Fig. 4. Enfoque algorítmico.* Fuente: elaboración propia a partir de [S001]–[S110].

**Tabla VI. Inputs de datos**

| Categoría | n | % |
|---|---|---|
| Textual | 62 | 56,4 |
| Layout / posición | 49 | 44,5 |
| Visual | 73 | 66,4 |
| Hand-crafted | 3 | 2,7 |
| No reporta | 20 | 18,2 |

**Tabla VII-a. Tipología documental**

| Categoría | n | % |
|---|---|---|
| Facturas | 46 | 41,8 |
| Recibos | 28 | 25,5 |
| Formularios | 37 | 33,6 |
| Contratos | 3 | 2,7 |
| Otros documentos financieros | 25 | 22,7 |
| Tablas | 16 | 14,5 |
| No reporta | 28 | 25,5 |

![Fig. 5. Tipología documental.](outputs/figuras/fig4_tipologia.png)

*Fig. 5. Tipología documental.* Fuente: elaboración propia a partir de [S001]–[S110].

**Tabla VII-b. Sistema empresarial**

| Categoría | n | % |
|---|---|---|
| ERP | 15 | 13,6 |
| CRM | 1 | 0,9 |
| DMS / gestión documental | 4 | 3,6 |
| Contabilidad / finanzas | 10 | 9,1 |
| No reporta | 84 | 76,4 |

**Mapeo enfoque × tipología**

| Enfoque | Facturas | Recibos | Formularios | Contratos | Otros documentos financieros | Tablas |
|---|---|---|---|---|---|---|
| Reglas / plantillas | 8 | 7 | 5 | 0 | 7 | 6 |
| Secuencial | 23 | 18 | 20 | 1 | 18 | 10 |
| Grafo | 10 | 5 | 5 | 0 | 1 | 5 |
| Multimodal / generativo | 25 | 17 | 17 | 1 | 15 | 8 |

![Fig. 6. Mapeo enfoque × tipología.](outputs/figuras/fig6_mapeo_enfoque_tipologia.png)

*Fig. 6. Mapeo enfoque × tipología.* Fuente: elaboración propia a partir de [S001]–[S110].

- Nota sobre el borrador previo: la afirmación de que los grafos predominaban antes de 2021 y de que lo multimodal es «emergente» no se sostiene con estos datos (solo 12 estudios en 2020–2022). Debe moverse a Introducción/Discusión con cita externa.

## Paso 8. Análisis de sensibilidad
- No hay puntajes QA; se usó un criterio de pertinencia: se excluyen revisiones, estudios de otro dominio, sin término documental y sin evidencia de enfoque ni tipología (N = 75).
- El filtro de dominio estricto (≥ 2 términos documentales) coincidió con la revisión manual en 22 de 22 estudios de la muestra.
- El orden de los enfoques se mantiene:

| Enfoque | n (N=110) | % (N=110) | n (N=75) | % (N=75) |
|---|---|---|---|---|
| Reglas / plantillas | 19 | 17,3 | 19 | 25,3 |
| Secuencial | 53 | 48,2 | 43 | 57,3 |
| Grafo | 16 | 14,5 | 13 | 17,3 |
| Multimodal / generativo | 48 | 43,6 | 41 | 54,7 |

- Lista de estudios a revisar: `outputs/alerta_pertinencia.csv` y `outputs/dominio_estricto_110.csv`.
- **Reconstrucción posible:** de los 866 estudios únicos 2020–2025 del cribado, 520 cumplen el filtro; el corpus puede rehacerse en dominio (decisión del equipo; actualizar PRISMA y volver a correr los scripts).

## Paso 9. Certeza de la evidencia (GRADE-CERQual) — propuesta
| Hallazgo | Limit. metodológicas | Coherencia | Adecuación | Relevancia | Certeza |
|:--|:--|:--|:--|:--|:-:|
| Enfoque algorítmico (PI1) | Moderadas | Sin dudas | Moderada | Sin dudas | Moderada |
| Inputs de datos | Moderadas | Sin dudas | Moderada | Sin dudas | Moderada |
| Tipología documental (PI4) | Graves (κ bajo) | Sin dudas | Moderada | Sin dudas | Baja |
| Sistema empresarial (PI4) | Graves | Menores | Grave (76 % sin dato) | Sin dudas | Baja |
| Base de validación (PD3) | Graves (κ bajo) | Menores | Grave (45 % sin dato) | Sin dudas | Baja |
| Producción anual y países | Moderadas | Sin dudas | Grave (selección; países 50 %) | Moderada | Baja |

Calificación propuesta por un revisor; **debe consensuarse entre los autores**.

## Paso 10. Tablas y figuras (formato IEEE)
8 tablas + Tabla I (esquema) y Tabla IX (GRADE) y 7 figuras en `outputs/figuras` (300 ppp, 8 pt, título de tabla arriba, de figura abajo, fuente al pie). Todas nacen de `outputs/tablas/*.csv`.

## Paso 11. Redacción por bloques
Texto de la sección III (generado desde los datos; versión final con formato en el `.docx`):


> Esta sección reporta la caracterización del corpus congelado de N = 110 estudios primarios [S001]–[S110], 65 recuperados de Scopus y 45 de Web of Science. Se responden las preguntas descriptivas PD1–PD3 y las preguntas temáticas PI1 (arquitecturas y enfoques algorítmicos) y PI4 (tipologías documentales y sistemas empresariales). Las preguntas PI2 y PI3 requieren la extracción de métricas a texto completo y quedan fuera del alcance de esta sección.

> Se aplicó mapeo sistemático con codificación por categorías: las preguntas PD1–PD3 se abordaron mediante conteos descriptivos y las preguntas PI1 y PI4 mediante una taxonomía de dos ejes (enfoque algorítmico e inputs de datos), más la tipología documental y la base de validación (Tabla I). La codificación se efectuó con diccionarios de términos aplicados al título, el resumen y las palabras clave de cada estudio; 3 estudios no disponían de resumen en la exportación y se codificaron solo con el título. Las categorías no son mutuamente excluyentes, por lo que los porcentajes se calculan sobre N y no suman 100 %. La categoría «No reporta» indica ausencia de evidencia en los campos analizados, no ausencia de la característica en el texto completo. Para estimar la fiabilidad de la codificación, un revisor codificó manualmente una muestra aleatoria del 20 % (n = 22; semilla fija) a partir del resumen y se calculó el κ de Cohen frente a la codificación automática. Sobre los estudios del dominio documental (n = 10), se obtuvo κ = 0,85 para el enfoque algorítmico, κ = 0,38 para la tipología documental y κ = 0,17 para la base de validación; solo el enfoque algorítmico alcanzó el umbral κ ≥ 0,80, por lo que la tipología documental, el sistema empresarial y la base de validación se reportan como resultados preliminares. En esa muestra, 12 de 22 estudios (54,5 %) no correspondían al dominio documental. [PENDIENTE: κ entre dos revisores humanos independientes].

> La distribución anual del corpus (PD1; Tabla II, Fig. 1) fue de 2 estudios en 2020, 4 en 2021, 6 en 2022, 13 en 2023, 17 en 2024 y 68 en 2025; este último año concentró el 61,8 % del corpus (n = 68). Los estudios de 2020 corresponden a [S001], [S050].

> Respecto a los canales de difusión (PD2), el corpus se distribuyó en 87 fuentes distintas, de las cuales 77 (88,5 %) aportaron un único estudio. La fuente más frecuente fue Lecture Notes in Computer Science (n = 10; 9,1 %), seguida de International Journal on Document Analysis and Recognition (n = 4) e IEEE Access (n = 4) (Tabla III). Los datos de afiliación estuvieron disponibles para 55 estudios (50,0 %), procedentes de la exportación de Web of Science; entre ellos, China registró 14 estudios (25,5 %), Alemania 8 (14,5 %), Turquía 8 (14,5 %) e India 6 (10,9 %) (Fig. 2). 29 autores figuraron en más de un estudio, con un máximo de 3 estudios por autor. Entre los 107 estudios con dato de citas, la mediana fue de 2 citas (máximo = 174) y 19 no registraron citas.

> En cuanto al diseño metodológico y los datos de validación (PD3; Tabla IV, Fig. 3), 92 (83,6 %) estudios presentaron desarrollo de un artefacto o sistema, 81 (73,6 %) incluyeron comparación experimental o benchmark y 29 (26,4 %) se asociaron a datos o entornos reales; 6 (5,5 %) correspondieron a revisiones. Sobre la base de validación, 30 (27,3 %) emplearon benchmarks públicos, 18 (16,4 %) datasets privados o datos reales y 13 (11,8 %) ambos tipos, mientras que 49 (44,5 %) no reportaron la base en los campos analizados. Esta última proporción limita la comparación entre la validación sobre benchmarks controlados y sobre flujos empresariales reales.

> El corpus se clasificó en cuatro enfoques algorítmicos (PI1; Tabla V, Fig. 4). El enfoque secuencial fue el más frecuente (n = 53; 48,2 %), seguido del multimodal/generativo (n = 48; 43,6 %), el basado en reglas y plantillas (n = 19; 17,3 %) y el basado en grafos (n = 16; 14,5 %); 25 (22,7 %) estudios no reportaron un enfoque identificable. 41 estudios (37,3 %) se asignaron a más de una categoría, por ejemplo, arquitecturas que combinan grafos con representaciones secuenciales. Los enfoques secuencial y multimodal/generativo se identificaron mediante términos como transformer, modelo de lenguaje y LayoutLM, y el enfoque en grafos mediante términos como graph neural network y graph attention.

> En contraste, la composición por periodo difirió: el enfoque en grafos representó el 41,7 % de los estudios de 2020-2022 (5 de 12) y el 4,4 % de los de 2025 (3 de 68), mientras que el enfoque secuencial pasó de 33,3 % a 51,5 %. El periodo 2020–2022 contiene solo 12 estudios, por lo que sus proporciones tienen baja estabilidad.

> Respecto a las modalidades de entrada, 73 (66,4 %) estudios emplearon información visual, 62 (56,4 %) textual, 49 (44,5 %) de layout o posición y 3 (2,7 %) características hechas a mano; 20 (18,2 %) no reportaron la modalidad (Tabla VI). 37 estudios (33,6 %) combinaron simultáneamente las tres modalidades textual, de layout y visual.

> En relación con las tipologías documentales (PI4; Tabla VII, Fig. 5), las facturas fueron el tipo más frecuente (n = 46; 41,8 %), seguidas de los formularios (n = 37; 33,6 %), los recibos (n = 28; 25,5 %), otros documentos financieros (n = 25; 22,7 %) y las tablas (n = 16; 14,5 %); los contratos aparecieron en 3 (2,7 %) estudios [S014], [S073], [S082]. En cuanto al sistema empresarial, 15 (13,6 %) mencionaron ERP, 10 (9,1 %) contabilidad o finanzas, 4 (3,6 %) gestión documental y 1 (0,9 %) CRM, mientras que 84 (76,4 %) no identificaron un sistema empresarial en título, resumen o palabras clave.

> El cruce entre enfoque y tipología (Fig. 6) mostró la mayor concentración en la combinación facturas con enfoque multimodal / generativo (n = 25); los contratos sumaron 2 asignaciones de enfoque (secuencial: 1; multimodal/generativo: 1) y ninguna al enfoque basado en reglas.

> El análisis de co-ocurrencia de palabras clave de autor, aplicado a los 78 estudios con palabras clave que no presentaron señales de otro dominio, con un umbral de 4 apariciones, produjo 14 nodos (Fig. 7). Los términos más frecuentes fueron «information extraction» (n = 16), «deep learning» (n = 13) y «optical character recognition» (n = 10). Se emplearon sinónimos unificados (p. ej., OCR y optical character recognition) y un layout de fuerza dirigida.

> Se recalcularon las frecuencias del enfoque algorítmico excluyendo temporalmente 35 estudios: revisiones o encuestas, estudios con señales de otro dominio (p. ej., neurociencia o manufactura), estudios sin término documental en título o palabras clave y estudios sin evidencia de enfoque ni de tipología. Con N = 75, el orden de los enfoques se mantuvo (Tabla VIII): secuencial 57,3 %, multimodal/generativo 54,7 %, reglas y plantillas 25,3 % y grafos 17,3 %. Este análisis se basó en criterios de pertinencia porque el corpus no incluye puntajes de calidad por estudio. Un filtro de dominio con al menos 2 términos documentales en título, resumen o palabras clave coincidió con la revisión manual en la muestra (22 de 22) y retuvo 75 de los 110 estudios. La certeza de los hallazgos se calificó con GRADE-CERQual (Tabla IX). [PENDIENTE: consenso de los revisores sobre la calificación].


## Paso 12. Trazabilidad
- Cada cifra del texto se calcula en `scripts/04_generar_docx_ieee.py` desde `outputs/tablas/*.csv` y `estadisticas.json`; ninguna se escribe a mano.
- Cada categoría de la matriz muestra el término de evidencia; cada afirmación sobre pocos estudios cita `[S###]`; si son muchos remite al Anexo A (`matriz_extraccion.csv`).
- Reproducción:
```
python scripts/01_codificar_corpus.py
python scripts/02_analisis_tablas_figuras.py
python scripts/03_muestra_kappa.py generar        # una sola vez
python scripts/05_kappa_manual_y_dominio.py
python scripts/04_generar_docx_ieee.py
python scripts/06_generar_main_md.py
```
Requiere pandas, matplotlib, networkx, python-docx, xlrd.

## Paso 13. Publicación
Pendiente del equipo: subir a OSF/Zenodo la carpeta `project/taxonomia_y_caracterizacion/` (scripts, matriz, tablas, figuras, Excel) para obtener DOI.

## Pendientes antes de entregar
1. κ entre dos revisores humanos (y verificar la codificación manual de la muestra).
2. Codificar manualmente S001, S003, S004 (sin resumen) y las variables tipología y base de validación.
3. Decidir sobre el corpus (35 estudios fuera de dominio) y actualizar PRISMA.
4. Consensuar GRADE-CERQual.
5. Corregir en metodología los valores sin respaldo (κ 0,86/0,91, QA 4,12, cifras PRISMA) — ver `NOTAS_PARA_EL_EQUIPO.md`.
6. Publicar en OSF/Zenodo.
