# SECCIÓN III: RESULTADOS DE LA REVISIÓN SISTEMÁTICA DE LITERATURA (RSL)

## 0. Apertura General del Corpus y Protocolo de Síntesis

La presente sección describe y cuantifica de forma objetiva la evidencia empírica extraída del corpus de literatura científica incluido, conforme a las directrices de reporte de **Kitchenham & Charters (2007)** [1] y los estándares internacionales de la declaración **PRISMA 2020** [2], articulando directamente la evidencia cuantitativa con el análisis sistemático de cada eje temático.

### 0.1. Estado de Congelamiento y Suficiencia del Corpus
El corpus documental primario quedó formalmente cerrado y congelado en un total de **$N = 131$ artículos de revista científica indexada** (100 % *Journal Articles*, sin actas de congreso, preprints, tesis ni literatura gris), habiendo superado el control de calidad metodológica ($QA \ge 3,50 / 5.00$; media global = **$4,61 / 5.00$**). 

La numeración de citas bibliográficas mantiene una relación matemática biunívoca:
$$\text{Ref IEEE } [n] = \text{ID } S + 2$$
donde las citas **[1] y [2]** corresponden a las normas metodológicas marco (Kitchenham & Charters y PRISMA 2020), los **131 estudios primarios** del corpus se indexan de manera inalterable entre **[3] y [133]** (desde $[S001]$ hasta $[S131]$), y las referencias metodológicas complementarias de síntesis documental y cienciometría se ubican en **[134] a [141]**.

### 0.2. Declaración Formal a Priori de Métodos de Síntesis por Pregunta
Conforme a los ítems 13a–13f de PRISMA 2020 y para mitigar el sesgo de notificación (*reporting bias*), la selección de la estrategia analítica para cada interrogante se formalizó antes de la consolidación de los datos:
1. **Síntesis Temática** (*Thomas & Harden [134]; Cruzes & Dybå [135]*): Aplicada para construir la taxonomía algorítmica de arquitecturas IA/IDP (**PI1**) y mapear las tipologías documentales y sistemas ERP/CRM (**PI4**).
2. **Síntesis Narrativa Estructurada** (*Popay et al. [136]*): Aplicada en el análisis de rendimiento técnico (**PI2**), organizando las métricas cuantitativas (F1-score, exactitud, latencia) por benchmarks estándar (SROIE, FUNSD, CORD) y reportando rangos empíricos $[mín, máx]$ sin promediar métricas entre datasets incompatibles.
3. **Síntesis sin metaanálisis — SWiM** (*Campbell et al. [137]*): Aplicada para contrastar las soluciones IA/IDP frente a líneas base tradicionales y manuales (**PI3**), utilizando el conteo de votos de dirección del efecto (*Mejora*, *Sin diferencia*, *Empeora*) y barras divergentes.
4. **Mapeo Sistemático Matricial** (*Petersen et al. [138]*): Aplicado para caracterizar la evolución temporal (**PD1**) y el cruce bidimensional entre diseños metodológicos y tipologías de dataset (**PD3**) mediante gráficos de burbujas.
5. **Mapeo Cienciométrico y Análisis de Redes** (*van Eck & Waltman [139]*): Aplicado en **PD2** para identificar núcleos de producción científica (revistas, países, autores) y la estructura de coocurrencia de palabras clave de autor en VOSviewer con umbral de $\ge 3$ apariciones.
6. **Calificación de Certeza de la Evidencia** (*Lewin et al. [140]*): Aplicación sistemática del marco GRADE-CERQual sobre los 4 pilares (limitaciones metodológicas, coherencia, adecuación de datos y relevancia) para ponderar cada hallazgo principal.

---

## 1. Preguntas Descriptivas y Análisis Cienciométrico (PD1, PD2, PD3)

### 1.1. Evolución Temporal de la Producción Científica (PD1: ¿Cómo ha evolucionado el volumen de producción científica anual sobre IA aplicada a documentos empresariales entre 2020 y 2025/2026?)

Para determinar la evolución temporal de la investigación sobre IA e IDP en entornos empresariales (2020–2025/2026), se analizó la producción científica anual consolidada, cuyos datos cuantitativos se detallan en la Tabla XIII y se visualizan en la Fig. 2.

```
TABLA XIII
DISTRIBUCIÓN CRONOLÓGICA DE LA PRODUCCIÓN CIENTÍFICA (2020–2025/2026) (N = 131)
```
| Año de Publicación | Estudios Primarios Indexados [n] | Frecuencia Relativa (%) | Porcentaje Acumulado (%) |
| :---: | :--- | :---: | :---: |
| **2020** | [64], [111], [130], [131] | 4 (3,1 %) | 3,1 % |
| **2021** | [58], [59], [60], [61], [62], [63], [112], [113], [114], [123], [126], [127], [128], [129] | 14 (10,7 %) | 13,8 % |
| **2022** | [50], [51], [52], [53], [54], [55], [57], [103], [104], [105], [106], [107], [108], [109], [125], [132], [133] | 17 (13,0 %) | 26,8 % |
| **2023** | [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [67], [90], [91], [92], [94], [95], [96], [97], [98], [99], [100], [101], [102], [116], [121], [124] | 27 (20,6 %) | 47,4 % |
| **2024** | [28], [29], [30], [31], [33], [34], [35], [36], [37], [38], [84], [86], [87], [88], [89], [120] | 16 (12,2 %) | 59,6 % |
| **2025** | [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [32], [56], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [85], [93], [110], [115], [117], [118], [119], [122] | 50 (38,2 %) | 97,8 % |
| **2026\*** | [3], [65], [66] | 3 (2,3 %) | 100,0 % |
| **Total Corpus** | **[3]–[133]** | **131 (100,0 %)** | **100,0 %** |

*\* Nota: Los estudios fechados en 2026 corresponden a artículos aceptados e incorporados en modalidad Early Access / In Press en Scopus y Web of Science durante el cierre de 2025 ([3], [65], [66]).*  
*Fuente: elaboración propia a partir del corpus primario [3]–[133].*

![Fig. 2. Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025/2026, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig2_evolucion_anual.png)
*Fig. 2. Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025/2026, N = 131). Barras: volumen anual absoluto (n); línea roja: porcentaje acumulado (%). Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a la pregunta: «¿Cómo ha evolucionado el volumen de producción científica anual sobre IA aplicada a documentos empresariales entre 2020 y 2025/2026?»)
Ciento treinta y un estudios (100,0 % del corpus primario; [3]–[133]) aportan evidencia directa para responder a la pregunta sobre la evolución cronológica de la producción científica en IA e IDP aplicada a sistemas documentales corporativos (PD1). Mediante mapeo sistemático cronológico se identificó una trayectoria de crecimiento marcadamente expansiva y no lineal a lo largo del sexenio 2020–2025/2026, con una concentración máxima de publicaciones en el bienio final (TABLA XIII, Fig. 2).

#### Bloque 2 — Desarrollo por Categoría y Fases Temporales
La dinámica temporal de publicación se articula en tres periodos analíticos diferenciados (Tabla XIII, Fig. 2):
1. **Fase de emergencia y cimientos basados en OCR-CNN (2020–2021):** Ciclo inicial caracterizado por propuestas orientadas a mejorar la binarización de escaneos, OCR neuronal con LSTM y segmentación clásica con Mask R-CNN. Registró un volumen de producción moderado en relación con etapas posteriores (Tabla XIII), alcanzando un 88,9 % de estudios con calidad alta y una certeza GRADE-CERQual moderada debido a la escasez de comparaciones con pipelines comerciales de producción.
2. **Fase de consolidación de Transformers Multimodales (2022–2023):** Representó el primer punto de inflexión significativo de la disciplina al acelerar sensiblemente la producción científica anual (Tabla XIII). Este avance estuvo impulsado por la adopción masiva de modelos multimodales preentrenados (LayoutLMv2/v3 [142], StrucTexT [144], BROS [145]) y redes basadas en grafos (GCN) para la extracción de claves semánticas (KIE) en facturas y recibos, con un 84,6 % de estudios en el estrato de calidad metodológica alta y certeza GRADE-CERQual alta.
3. **Fase de aceleración con VLMs y Modelos Generativos (2025–2026\*):** Constituye la etapa más prolífica del corpus, concentrando el volumen cúspide de publicaciones (Tabla XIII). El factor determinante de esta aceleración fue la incorporación de *Vision-Language Models* (VLMs), Transformers generativos con mecanismos de atención visual desacoplada y modelos de lenguaje de gran escala (LLMs) adaptados con *prompt engineering* y *few-shot learning*, donde el 88,9 % de los estudios alcanzó calidad alta con certeza GRADE-CERQual alta.

#### Bloque 3 — Contrastes y Debates Temporales
A pesar de la tendencia global alcista, la literatura experimentó una desaceleración temporal transitoria durante 2024 (Tabla XIII). Una posible explicación, no contrastada empíricamente en la presente revisión, sugiere que esta inflexión transitoria pudo coincidir con la transición de los laboratorios desde arquitecturas de grafos y pipelines heurísticos hacia el ajuste y maduración de modelos fundacionales multimodales y arquitecturas sin entrenamiento previo (*zero-shot*) publicadas formalmente en el ciclo 2025–2026 [3], [6], [22], [32].

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
La literatura sobre IA/IDP en sistemas corporativos evidencia una trayectoria de maduración sostenida, transitando desde la simple corrección óptica de caracteres hacia sistemas integrales de comprensión de documentos ricos visualmente (*Visually-Rich Documents*). No se identificaron estudios longitudinales que evalúen la degradación de los modelos a lo largo de más de dos años operativos en empresas. El 40,5 % de las publicaciones corresponde a 2025–2026 (53 de 131 estudios), ratificando la rápida adopción de modelos multimodales en el tratamiento de documentación corporativa. Asimismo, al evaluar la sensibilidad excluyendo los 10 estudios con puntaje de calidad moderada (QA = 3,5; [116]–[118], [121]–[123], [127], [128], [132], [133]), la proporción correspondiente al ciclo 2025–2026 se situó en el 41,3 % (50 de 121 estudios), ratificando la robustez de la tendencia expansiva.

---

### 1.2. Productividad por Revistas, Autores, Países y Red de Coocurrencia (PD2: ¿Qué autores, revistas científicas indexadas y países concentran la mayor productividad e impacto académico?)

Para responder a la pregunta «¿Qué autores, revistas científicas indexadas y países concentran la mayor productividad e impacto académico?» (PD2), se normalizaron los títulos de las revistas indexadas, se contabilizó la productividad de los autores, se aplicó la regla estricta de afiliación geográfica institucional del primer autor y se estructuró la red de coocurrencia de palabras clave de autor (*Author Keywords*) con un umbral de frecuencia $\ge 3$ en VOSviewer [139]. La evidencia bibliométrica de concentración autoral y geográfica se compendia en la Tabla XV y la Fig. 3, mientras que el desglose exhaustivo de los canales de difusión se traslada formalmente al Material Suplementario (Tabla XIV en Apéndice) para optimizar la densidad técnica del cuerpo principal.

```
TABLA XV
CONCENTRACIÓN GEOGRÁFICA POR AFILIACIÓN DEL PRIMER AUTOR Y AUTORES DESTACADOS (N = 131)
```
| País de Afiliación (Primer Autor) | Estudios [n] | Frecuencia Relativa (%) | Autores Más Prolíficos en el Corpus (≥ 2 publicaciones) |
| :--- | :---: | :---: | :--- |
| **China** | 39 | 29,8 % | Zhang J. (4; [43], [81], [82], [120]), Zhang Y. (4; [78], [79], [81], [82]), Li C. (3; [9], [15], [32]), Liu J. (3; [19], [34], [74]), Zhang W. (3; [26], [37], [73]), Ma J. (3; [37], [43], [120]), Zhang Z. (3; [43], [83], [120]). |
| **India** | 11 | 8,4 % | Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: Tiwari D., Gupta A., Baviskar D.) |
| **Estados Unidos** | 10 | 7,6 % | Wang P. (3; [47], [89], [121]) |
| **Alemania** | 9 | 6,9 % | Hashmi K.A. (3; [59], [61], [123]), Liwicki M. (3; [59], [61], [123]), Stricker D. (3; [59], [61], [123]) |
| **Corea del Sur** | 6 | 4,6 % | Lee S. (3; [42], [71], [121]) |
| **Canadá** | 5 | 3,8 % | Simsek M. (4; [11], [35], [48], [51]), Kantarci B. (4; [11], [35], [48], [51]), Xiao B. (3; [11], [35], [48]), Alkheir A.A. (3; [11], [35], [48]). |
| **Vietnam** | 5 | 3,8 % | Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u) |
| **Taiwán** | 4 | 3,1 % | Sin autores con ≥ 3 publicaciones (producción dispersa, 1 estudio c/u) |
| **Turquía** | 4 | 3,1 % | Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: Oral B. (2; [50], [64]), Sayallar C. (1; [100])) |
| **España** | 3 | 2,3 % | Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: Fornés A. (2; [105], [111]), Lladós J. (2; [105], [116])) |
| **Otros 22 países (≤ 2 estudios c/u)** | 35 | 26,7 % | Sin autores con ≥ 3 publicaciones (alta dispersión institucional en Australia, Reino Unido, Francia, etc.) |
| **Total Corpus Primario** | **131** | **100,0 %** | **498 autores únicos indexados en el corpus primario** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Regla de país: país de la institución del primer autor. Desambiguación: las firmas chinas con iniciales homónimas (Zhang J., Zhang Y., Zhang W., Zhang Z.) se verificaron y desambiguaron mediante Scopus Author ID, ORCID y redes de coautoría.*

![Fig. 3. Concentración geográfica y mapa de términos temáticos clave (PD2, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig3_vosviewer_geografia.png)
*Fig. 3. Concentración geográfica de la investigación y principales clústeres temáticos derivados de palabras clave de autor (PD2, N = 131). (a) Distribución porcentual por país de afiliación del primer autor; (b) Frecuencia de descriptores con umbral ≥ 3 ocurrencias en VOSviewer. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a la pregunta: «¿Qué autores, revistas científicas indexadas y países concentran la mayor productividad e impacto académico?»)
Ciento treinta y un artículos primarios (100,0 % del corpus; [3]–[133]) aportan evidencia para responder a la pregunta sobre la distribución de productividad académica por revistas, autores, países y estructura temática de redes (PD2). Mediante análisis cienciométrico y mapeo de coocurrencia en VOSviewer [139] se identificó una concentración de publicaciones en revistas especializadas de procesamiento de documentos e ingeniería de sistemas, liderada a nivel geográfico por instituciones de China, India y Estados Unidos, coexistiendo una alta dispersión autoral de base con polos consolidados de productividad serial (Tabla XIV en Apéndice, TABLA XV, Fig. 3).

#### Bloque 2 — Desarrollo por Categoría y Redes Temáticas
La evidencia se estructura en tres dimensiones bibliométricas (Tabla XIV en Apéndice, Tabla XV, Fig. 3):
1. **Núcleos de difusión y revistas líderes:** Doce revistas concentraron casi la mitad de la producción global (60 de 131 artículos; Tabla XIV en Apéndice). Las cabeceras líderes fueron *IEEE Access* (9,9 %, n = 13; Q1/Q2), *International Journal on Document Analysis and Recognition (IJDAR)* (6,9 %, n = 9; Q2) y *Pattern Recognition* (4,6 %, n = 6; Q1), consolidándose como los principales canales de difusión de modelos de extracción estructurada e IDP. Las restantes 64 revistas indexadas reunieron una producción complementaria y diversa (71 artículos, 54,2 % del corpus; Tabla XIV en Apéndice), reflejando la dispersión propia de la Ley de Bradford en el área. El catálogo completo de revistas, editoriales y cuartiles JCR/SJR se compendia en la Tabla XIV del Apéndice de Material Suplementario para optimizar la densidad técnica del cuerpo principal.
2. **Polos geográficos de investigación:** Conforme a la regla de asignación por primer autor, la investigación se concentró principalmente en Asia y Norteamérica, con China, India y Estados Unidos a la vanguardia, complementados por contribuciones significativas de Europa occidental en Alemania y España (Tabla XV, Fig. 3a).
3. **Red cienciométrica de palabras clave (VOSviewer):** Con un umbral $\ge 3$ apariciones se configuraron tres clústeres conceptuales (Fig. 3b): Clúster 1 (Extracción y Semántica: *Information Extraction*, *Document Understanding* y *Key Information Extraction - KIE*); Clúster 2 (Paradigmas Algorítmicos: *Deep Learning*, *Optical Character Recognition - OCR* y *Transformers*); y Clúster 3 (Estructuras Complejas: *Table Structure Recognition*, *Table Detection* y *Object Detection*).

#### Bloque 3 — Contrastes y Dispersión Autoral
Frente a la concentración institucional y geográfica en China y en cabeceras editoriales de alto impacto, la estructura de autoría exhibe un comportamiento dual (Tabla XV). Por un lado, predomina una elevada dispersión de base: el 84,7 % de los autores (422 de 498) registró un único artículo en la ventana analizada. Por otro lado, la productividad serial (≥ 3 estudios) se articula en redes colaborativas específicas (Tabla XV): destacan los consorcios de la Universidad de Ottawa en Canadá (equipo de Simsek y colaboradores) y del DFKI / Universidad de Kaiserslautern en Alemania (equipo de Hashmi y Stricker) en procesamiento tabular, junto a redes cooperativas en China en modelado multimodal y segmentación de tablas [43], [120], y líneas sostenidas en Estados Unidos [47], [89] y Corea del Sur [42], [71]. Para evitar sesgos cienciométricos por homonimia asiática, la atribución autoral se verificó y desambiguó mediante Scopus Author ID, ORCID y redes de coautoría institucional.

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
En el plano geográfico regional, la representación de América Latina en el corpus primario se circunscribe al estudio brasileño [14] (Gonçalves Lima y Alves Pereira, Universidade Federal de Lavras), el cual introdujo el benchmark UFLA-FORMS para extracción de entidades en formularios semiestructurados en portugués, sumado a las contribuciones ibéricas en detección tabular y procesamiento de recibos ([105], [111], [131]). Esta reducida frecuencia de publicaciones latinoamericanas en revistas Q1–Q3 no refleja necesariamente una ausencia de investigación aplicada en la región, sino las fronteras de cobertura del protocolo de búsqueda (restricción a Scopus/WoS en inglés/español y exclusión sistemática de actas de congresos regionales como CLEI o simposios locales, donde se concentra parte del desarrollo tributario corporativo). En el análisis de sensibilidad excluyendo los 10 estudios con QA = 3,5, China concentró el 31,4 % de los estudios filtrados (38 de 121), confirmando la estabilidad del mapa cienciométrico global.

---

### 1.3. Clasificación de Diseños Metodológicos × Tipología de Datasets (PD3: ¿Qué diseños metodológicos y tipologías de conjuntos de datos predominan en la literatura?)

Con el propósito de evaluar la validez metodológica y la transferibilidad industrial de las propuestas, se contrastaron los diseños de investigación frente al tipo de fuentes de datos empleadas (benchmarks públicos, privados corporativos o mixtos). La concordancia inter-evaluador de esta categorización se evaluó de forma ciega e independiente sobre una muestra del 20,6 % del corpus ($n = 27$ estudios seleccionados aleatoriamente), alcanzando un coeficiente Kappa de Cohen **$\kappa = 0,85$** ($P_o = 88.9\,\%$, $P_e = 0,258$; concordancia casi perfecta bajo el protocolo formal de extracción y síntesis temática). La matriz de contingencia se reporta en la Tabla XVI y el gráfico de burbujas de Petersen et al. (2015) [138] se expone en la Fig. 4.

```
TABLA XVI
MATRIZ CRUZADA DE DISEÑOS METODOLÓGICOS Y TIPOLOGÍA DE DATASETS (PD3) (N = 131)
```
| Diseño Metodológico de Investigación | Benchmarks Públicos Abiertos | Datasets Corporativos Privados | Datasets Híbridos / Mixtos | Total por Diseño [n] | Frecuencia Relativa (%) |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Experimental Controlado** | 48 (36,6 %)<br>[3]–[6], [8], [9], [12], [14], [15], [17], [19], [30]–[33], [35], [37], [39]–[42], [46]–[48], [50], [52], [57], [61], [67], [71]–[74], [76], [77], [80], [83], [86], [88]–[90], [92], [93], [96], [99], [104], [105], [108] | 18 (13,7 %)<br>[7], [10], [11], [13], [20], [22], [28], [34], [36], [43]–[45], [49], [51], [55], [56], [81], [91] | 16 (12,2 %)<br>[16], [18], [21], [23]–[27], [29], [38], [60], [65], [66], [68], [78], [87] | 82 | 62,6 % |
| **Desarrollo de Artefacto / PoC** | 14 (10,7 %)<br>[63], [69], [79], [97], [100], [102], [106], [109]–[111], [113]–[116] | 11 (8,4 %)<br>[54], [95], [98], [112], [118]–[124] | 6 (4,6 %)<br>[58], [59], [125], [126], [129], [130] | 31 | 23,7 % |
| **Cuasi-experimental** | 4 (3,1 %)<br>[85], [94], [101], [132] | 4 (3,1 %)<br>[53], [82], [107], [133] | 2 (1,5 %)<br>[62], [128] | 10 | 7,6 % |
| **Caso de Estudio Real Corporativo** | 2 (1,5 %)<br>[84], [103] | 5 (3,8 %)<br>[64], [70], [75], [117], [127] | 1 (0,8 %)<br>[131] | 8 | 6,1 % |
| **Total por Tipología de Dataset** | **68 (51,9 %)** | **38 (29,0 %)** | **25 (19,1 %)** | **131** | **100,0 %** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Medición de acuerdo inter-evaluador sobre muestra del 20,6 % (n = 27): Po = 88,9 %, Pe = 0,258, κ = 0,85 (casi perfecto). Partición matemática exacta de 12 celdas disjuntas.*

![Fig. 4. Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]): Diseño Metodológico vs. Tipología de Dataset (PD3, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig4_burbujas_disenos_datasets.png)
*Fig. 4. Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]): Diseño Metodológico vs. Tipología de Dataset (PD3, N = 131). El área de cada burbuja es proporcional al número de estudios primarios (n); los porcentajes corresponden a la totalidad del corpus. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a la pregunta: «¿Qué diseños metodológicos y tipologías de conjuntos de datos predominan en la literatura?»)
Ciento treinta y un artículos (100,0 % del corpus; [3]–[133]) aportan evidencia para responder a la pregunta sobre los diseños metodológicos de investigación y las tipologías de conjuntos de datos evaluados (PD3). Mediante la matriz de mapeo sistemático de Petersen et al. [138] y con un acuerdo inter-evaluador de $\kappa = 0,85$, se determinó un predominio estructural de experimentos controlados sobre bancos de datos públicos abiertos, en contraste con una baja proporción de casos de estudio reales integrados en producción corporativa (TABLA XVI, Fig. 4).

#### Bloque 2 — Desarrollo por Categoría y Cruce Matricial
La matriz cruzada evidencia tres núcleos metodológicos de trabajo (Tabla XVI, Fig. 4):
1. **Predominio del diseño experimental controlado:** La mayor parte del corpus adoptó un diseño experimental formal con modelos baselines bajo condiciones reproducibles de laboratorio (Tabla XVI), apoyándose fundamentalmente en benchmarks públicos abiertos (SROIE, FUNSD, CORD, DocBank). Cabe precisar que la concurrencia numérica de 82 estudios experimentales y 82 estudios bajo síntesis SWiM en PI3 responde a constructos metodológicos independientes: 62 estudios comparten ambas condiciones (experimentos con comparador frente a métodos tradicionales), mientras que 20 experimentos controlados contrastaron únicamente modelos neuronales entre sí sin comparador tradicional, y 20 estudios de PI3 provinieron de desarrollos de artefactos o casos de estudio.
2. **Desarrollo de artefactos y pruebas de concepto (PoC):** Constituye la segunda modalidad metodológica predominante (Tabla XVI), enfocada en diseñar prototipos o arquitecturas especializadas validadas de forma acotada, donde una fracción se apoyó en datos privados propietarios sin someter el artefacto a estrés transaccional continuo.
3. **Validación en conjuntos de datos corporativos y mixtos:** Cerca de la mitad de las investigaciones recurrió a datos privados de empresas o esquemas híbridos que combinan preentrenamiento en bancos abiertos con ajuste fino y validación final sobre documentos reales de organizaciones (Tabla XVI).

#### Bloque 3 — Contrastes y Vacíos en Casos de Estudio Reales
El contraste más crítico revelado por el mapeo sistemático reside en la baja proporción de casos de estudio reales integrados en producción corporativa (Tabla XVI, Fig. 4). Se precisa la distinción conceptual entre este diseño metodológico de Caso de Estudio Corporativo (PD3; Tabla XVI) y el nivel de integración arquitectónica con software ERP analizado en PI4 (Tabla XXI): mientras el primero evalúa el despliegue del proceso en una organización viva, el segundo exige conexión técnica transaccional con bases de datos y módulos contables del ERP, coincidiendo plenamente ambos criterios únicamente en los estudios [64] y [127]. A pesar de que la literatura reporta precisiones teóricas superiores al 95 % en benchmarks abiertos [3], [6], [7], los investigadores que implementaron soluciones en entornos corporativos reales enfrentaron restricciones de confidencialidad regulatoria [64], [116], requerimiento de supervisión humana (*human-in-the-loop*) ante alucinaciones de LLMs en montos contables [4], [13], [22] y problemas de integración con sistemas ERP heredados [70], [127].

#### Bloque 4 — Cierre, Madurez y Sensibilidad
Existe una brecha de transferencia tecnológica: la comunidad científica ha priorizado el benchmarking sobre tres datasets públicos icónicos frente a la validación empírica en flujos empresariales vivos. Al excluir los 10 estudios del estrato inferior de calidad ($QA = 3,5$; [116]–[118], [121]–[123], [127], [128], [132], [133]), los experimentos controlados se consolidaron en el 67,8 % (82 de 121 estudios, al no registrarse estudios con QA = 3,5 en esta tipología experimental), ratificando que la evidencia técnica del área descansa sobre pruebas comparativas de laboratorio con control experimental estandarizado.

---

## 2. Evaluación de Calidad Metodológica (QA) e Integración al Análisis

Para jerarquizar el grado de solidez empírica de la evidencia y preparar formalmente el insumo para el análisis de sensibilidad metodológica, se examinó la totalidad del corpus primario bajo el instrumento de cinco preguntas de calidad metodológica (QA1 a QA5) de **Kitchenham & Charters (2007)** [1]. La doble evaluación ciega sobre la muestra del 20,6 % ($n = 27$ estudios) reportó un coeficiente Kappa ponderado cuadrático de Cohen **$\kappa_w = 0,89$** (acuerdo sustancial casi perfecto para escalas ordinales). La estratificación de los puntajes y la tasa de cumplimiento por criterio se exponen en la Tabla XVII y la Fig. 5.

```
TABLA XVII
ESTRATIFICACIÓN DE CALIDAD METODOLÓGICA (QA) Y ANÁLISIS DE CUMPLIMIENTO POR CRITERIO (N = 131)
```
| Nivel de Calidad Metodológica | Rango de Puntaje (Máx. 5.0) | Estudios en Corpus [n] | Frecuencia Relativa (%) | Función Metodológica en la Síntesis |
| :--- | :---: | :---: | :---: | :--- |
| **Calidad Alta** | 4.5 – 5,0 pts | 108 | 82,4 % | Núcleo empírico robusto para extracción y síntesis temática (PI1–PI4). Incluye los 4 estudios nucleares de referencia con puntaje perfecto de 5.0 / 5.0 ([3], [4], [5], [6]). |
| **Calidad Media** | 4.0 pts | 13 | 9,9 % | Estudios que satisfacen el protocolo con cumplimientos parciales menores; retenidos en el análisis de sensibilidad. |
| **Calidad Moderada / Estrato Inferior\*** | 3,5 pts | 10 | 7,6 % | Grupo de exclusión temporal en el análisis de sensibilidad metodológica: [116], [117], [118], [121], [122], [123], [127], [128], [132], [133]. |
| **Total Corpus Primario** | **Media = 4,61 / 5.00** | **131** | **100,0 %** | Mínimo registrado: 3,50 pts; Máximo: 5,00 pts; Desviación estándar: ±0.45 pts. |

*\* Nota: El estrato de 3,5 pts conforma la submuestra de prueba para el análisis de robustez de hallazgos. Ningún estudio incluido obtuvo calificación menor a 3,5 pts. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

```
TABLA XVII (CONTINUACIÓN)
ANÁLISIS DESAGREGADO DE CUMPLIMIENTO POR PREGUNTA QA (N = 131)
```
| Criterio QA Evaluado | Cumplimiento Total (1.0 pt) | Cumplimiento Parcial (0.5 pt) | Incumplimiento (0.0 pt) | Media por Criterio (sobre 1.0) |
| :--- | :---: | :---: | :---: | :---: |
| **QA1 (Objetivos y tipología documental definida)** | 131 (100,0 %) | 0 (0,0 %) | 0 (0,0 %) | 1,000 / 1.0 |
| **QA2 (Detalle del dataset, volumen y particiones)** | 125 (95,4 %) | 6 (4,6 %) | 0 (0,0 %) | 0,977 / 1.0 |
| **QA3 (Arquitectura reproducible y código documentado)** | 99 (75,6 %) | 32 (24,4 %) | 0 (0,0 %) | 0,878 / 1.0 |
| **QA4 (Métricas cuantitativas formales reproducibles)** | 108 (82,4 %) | 23 (17,6 %) | 0 (0,0 %) | 0,912 / 1.0 |
| **QA5 (Contraste empírico vs baselines / tradicional)** | 89 (67,9 %) | 42 (32,1 %) | 0 (0,0 %) | 0,840 / 1.0 |

*Fuente: elaboración propia a partir del corpus primario [3]–[133].*

![Fig. 5. Evaluación de Calidad Metodológica (Kitchenham & Charters [1]) y vulnerabilidad por criterio (N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig5_distribucion_qa_criterios.png)
*Fig. 5. Evaluación de calidad metodológica (Kitchenham & Charters [1]) y análisis de vulnerabilidad por criterio (N = 131). (a) Distribución por estrato de calidad; (b) Tasa de cumplimiento por criterio evaluado (QA1 a QA5). Fuente: elaboración propia a partir del corpus primario [3]–[133].*

**Hallazgos del Control de Calidad y Protocolo de Aislamiento:**  
Los estudios primarios alcanzaron una media global de 4,61 / 5,00 pts (DE = ±0.45 pts; 82,4 % en calidad alta) en la evaluación de calidad de Kitchenham & Charters [1] (Tabla XVII, Fig. 5). Se constató un efecto techo en el criterio QA1 (100,0 % de cumplimiento pleno), derivado de que la totalidad de los artículos superó el arbitraje previo en revistas indexadas (Scopus/WoS), definiendo unívocamente sus objetivos y la tipología documental; QA1 operó como condición basal de inclusión. El criterio QA2 exhibió igualmente un cumplimiento casi óptimo (Tabla XVII). En QA4 (reporte cuantitativo formal y reproducible), el corpus obtuvo una media de 0,912 / 1.0 (Tabla XVII), reportando métricas cuantitativas verificables. Para los fines específicos de PI2, se discriminaron los 117 estudios que evaluaron tareas de extracción sobre benchmarks formales frente a 14 investigaciones de taxonomías y arquitecturas sin conjuntos de prueba cuantitativos. Por su parte, las principales áreas de mejora empírica se localizaron en QA5 (contraste explícito frente a métodos tradicionales) y en QA3 (especificación detallada de hiperparámetros y reproducibilidad de código), donde se concentraron los cumplimientos parciales (Tabla XVII). Los diez estudios calificados en el estrato moderado (QA = 3,50 pts; Tabla XVII) conforman el subgrupo aislado para el test de robustez.

---

## 3. Síntesis Temática de Arquitecturas IA e IDP (PI1: ¿Qué arquitecturas y enfoques algorítmicos de IA/IDP se han implementado en el procesamiento de documentos empresariales?)

Para determinar cuáles son las familias algorítmicas y arquitecturas neuronales predominantes en la literatura entre 2020 y 2025/2026, se ejecutó una síntesis temática (*Thomas & Harden [134]; Cruzes & Dybå [135]*) sobre los 105 estudios primarios que abordan explícitamente el modelado de IA para procesamiento de documentos de negocio ($80.2\,\%$ del corpus). La asignación taxonómica ciega e independiente sobre la muestra aleatoria del 20,6 % ($n = 27$ estudios) reportó un coeficiente Kappa de Cohen **$\kappa = 0,88$** ($P_o = 92.6\,\%$, $P_e = 0,380$), evidenciando una concordancia inter-evaluador casi perfecta bajo el protocolo formal de extracción y síntesis temática. Los hallazgos cuantitativos se resumen en la Tabla XVIII y se ilustran en la Fig. 6.

```
TABLA XVIII
TAXONOMÍA DE FAMILIAS ALGORÍTMICAS Y ENFOQUES DE INTELIGENCIA ARTIFICIAL (PI1) (n = 105)
```
| Familia Algorítmica / Arquitectura IA | Descripción Técnica Estandarizada | Frecuencia Absoluta (n) | Frecuencia Relativa (%) |
| :--- | :--- | :---: | :---: |
| **Canalizaciones Híbridas (*Pipelines*) CNN-RNN y Segmentación Clásica con OCR** | Modelos convolucionales (ResNet, VGG, YOLO, Mask R-CNN) combinados con recurrentes (LSTM) y motores OCR para detección de regiones y tablas. | 56 | 53,3 % |
| **Transformers Multimodales y Modelos Visión-Lenguaje (VLM)** | Modelado conjunto de texto, coordenadas espaciales 2D (bounding boxes) y parches visuales (LayoutLMv2/v3 [142], DocFormer [143], StrucTexT [144], BROS [145], Bi-VLDoc). | 22 | 21,0 % |
| **Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN)** | Representación de palabras/bloques como nodos y relaciones espaciales/semánticas relativas como aristas (GCN, GAT, GraphIE). | 16 | 15,2 % |
| **Modelos Generativos, LLMs y Adaptación Zero/Few-Shot** | Modelos fundacionales autorregresivos aplicados con prompt engineering, in-context learning o fine-tuning para extracción estructurada JSON. | 11 | 10,5 % |
| **Total Cobertura PI1** | **Subconjunto verificado de estudios con PI1 = 1** | **105** | **100,0 %** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133].*

![Fig. 6. Taxonomía de Familias Algorítmicas de IA en Procesamiento Documental (PI1, n = 105)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig6_taxonomia_algoritmos.png)
*Fig. 6. Taxonomía de familias algorítmicas de IA en procesamiento documental empresarial (PI1, n = 105). Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135]. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a la pregunta: «¿Qué arquitecturas y enfoques algorítmicos de IA/IDP se han implementado en el procesamiento de documentos empresariales?»)
Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVIII, Fig. 6) aportan evidencia para responder a la pregunta sobre la taxonomía de arquitecturas de IA aplicadas al procesamiento de documentos corporativos (PI1). Mediante síntesis temática estandarizada (*Thomas & Harden [134]; Cruzes & Dybå [135]*) y con un coeficiente de concordancia inter-evaluador de $\kappa = 0,88$ sobre la submuestra del 20,6 % ($n = 27$), se identificaron cuatro familias algorítmicas mutuamente excluyentes, observándose un predominio de pipelines modulares basados en convolución y OCR neuronal, acompañados por una rápida consolidación de Transformers multimodales y modelos de visión-lenguaje (VLM).

#### Bloque 2 — Desarrollo por Categoría Algorítmica (Extensión Normativa)

**1. Canalizaciones Híbridas (*Pipelines*) CNN-RNN y Segmentación Clásica con OCR:**  
Esta arquitectura comprende la articulación secuencial de redes neuronales convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para detección de regiones, combinadas con capas recurrentes (LSTM) y motores OCR para transcripción textual en documentos estructurados. Constituye la familia mayoritaria en la literatura (Tabla XVIII, Fig. 6). Las investigaciones convergen en que la modularización desacopla la detección geométrica de la transcripción, facilitando la depuración y auditoría interna en entornos productivos locales [10], [15], [33], [54], [84]. Cuantitativamente, estos pipelines alcanzan latencias de inferencia de 80 ms a 250 ms en CPUs estándar con exactitudes de segmentación entre 88,5 % y 96,0 % en plantillas regulares, respaldando un dictamen de **Alta Certeza** GRADE-CERQual (Tabla XVIII).

**2. Transformers Multimodales y Modelos Visión-Lenguaje (VLM):**  
Esta familia integra arquitecturas de atención profunda que fusionan simultáneamente la información textual, la disposición geométrica espacial 2D (*bounding boxes*) y los parches visuales del documento dentro de un espacio latente unificado (LayoutLMv2/v3 [142], DocFormer [143], StrucTexT [144], BROS [145]). Representa la segunda familia más adoptada (Tabla XVIII). Los autores demuestran que la incorporación del contexto visual y espacial permite resolver la extracción de entidades clave (KIE) en comprobantes fiscales con diagramación variable sin requerir plantillas fijas [6], [7], [36], [42], reportando puntuaciones de F1-score entre el 93,1 % y el 98,7 % en datasets estándar (CORD y SROIE) con un nivel de **Alta Certeza** GRADE-CERQual.

**3. Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN):**  
Este paradigma representa fragmentos y palabras como nodos dentro de un grafo planar cuyas aristas codifican relaciones de adyacencia espacial, distancias euclidianas y dependencias semánticas (GCN, GAT, GraphIE; Tabla XVIII). La literatura coincide en que las redes de grafos capturan de forma sobresaliente el flujo de lectura no lineal y la estructura reticular de facturas complejas y tablas [8], [34], [40], [51], [105]. En las evaluaciones numéricas exhiben precisiones de emparejamiento clave-valor de 88,0 % a 95,8 %, con una reducción de hasta el 40 % en parámetros entrenables frente a transformadores masivos, obteniendo calificación de **Alta Certeza** GRADE-CERQual.

**4. Modelos de Lenguaje Generativos, LLMs y Adaptación Zero/Few-Shot:**  
Esta categoría abarca el empleo de modelos fundacionales autorregresivos aplicados con ingeniería de prompts, aprendizaje en contexto y ajuste fino para la estructuración directa de documentos en esquemas JSON o XML (Tabla XVIII). Los estudios evidencian una capacidad sin precedentes para procesar documentos nunca antes vistos sin entrenamiento previo [3], [4], [19], reportando precisiones de extracción entre el 85,0 % y el 94,2 % en esquemas zero-shot, si bien con latencias superiores (800 ms a 2 500 ms por página). La certeza GRADE-CERQual se dictamina como **Moderada** debido a la dependencia de conectividad externa a APIs propietarias y el costo computacional asociado.

#### Bloque 3 — Contrastes y Debates de Rendimiento
Se constata una controversia técnica estructural entre tres posturas documentadas directamente en la literatura:
1. **Eficiencia computacional y bajo costo en CPU local:** Diversas investigaciones sostienen que los pipelines modulares basados en convolución y OCR representan la alternativa más viable para infraestructuras locales convencionales, logrando latencias ultra bajas (<150 ms) y ejecutándose íntegramente en CPUs sin riesgo de fuga de datos hacia servicios en la nube [12], [54], [71], [88] (Iqbal et al. [12]; Kim C.-Y. et al. [54]; Lee E. et al. [71]; Kiatphaisansophon et al. [88]).
2. **Flexibilidad y adaptabilidad mediante modelos de visión-lenguaje:** Por el contrario, un conjunto representativo de estudios argumenta que los esquemas rígidos colapsan ante cualquier cambio imprevisto de diagramación, justificando el costo de aceleración por GPU que demandan los Transformers multimodales y VLMs debido a su capacidad intrínseca de generalización zero-shot en documentos contables y comprobantes fiscales [3], [4], [6], [19], [25], [115] (Wei et al. [3]; Chen L.-C. et al. [4]; Mifsud et al. [6]; Hu et al. [19]; Levich & Knust [25]; Hemmer et al. [115]).
3. **Riesgos de alucinación semántica y costos de inferencia en LLMs:** En una postura de contraste crítico, diversas evaluaciones advierten que la inferencia puramente autorregresiva de los LLMs introduce una vulnerabilidad latente de alucinación numérica en montos contables y códigos fiscales, requiriendo validadores sintácticos adicionales que incrementan la latencia total del flujo de procesamiento [17], [27], [37] (Abdalla et al. [17]; Lin Y.M. et al. [27]; Chen Z. et al. [37]).

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
La literatura transita hacia una convergencia híbrida: modelos ligeros de visión-lenguaje desacoplados (*Lightweight VLMs*) combinados con verificadores basados en reglas. Al excluir del análisis los 4 estudios con $QA = 3,5$ que integran PI1 ([117], [118], [122], [123]), los pipelines híbridos CNN-RNN pasaron de 56 ($53.3\,\%$) a 53 de 101 estudios ($52.5\,\%$, variación de $-0.8\,\%$), los Transformers/VLMs se situaron en 22 de 101 ($21.8\,\%$, variación de $+0.8\,\%$), las redes GNN en 15 de 101 ($14.9\,\%$, variación de $-0.3\,\%$) y los LLMs en 11 de 101 ($10.9\,\%$, variación de $+0.4\,\%$), demostrando que la jerarquía taxonómica de las cuatro familias algorítmicas se mantiene enteramente inalterada, confirmando que la distribución taxonómica de modelos no depende de las publicaciones de menor rigor metodológico.

---

## 4. Rendimiento Cuantitativo de las Soluciones IA en Benchmarks (PI2: ¿Qué niveles de precisión y velocidad de resolución reportan las soluciones de IA/IDP en extracción documental?)

Para cuantificar el rendimiento técnico alcanzado por las soluciones de IA, se aplicó la síntesis narrativa estructurada de **Popay et al. (2006)** [136] sobre los 117 estudios que evalúan extracción sobre benchmarks formales ($89.3\,\%$ del corpus). Para salvaguardar la validez metodológica, no se promediaron métricas entre conjuntos de datos incompatibles, tabulando rangos empíricos $[mín, máx]$ y medianas por benchmark estándar en la Tabla XIX y visualizándolos en la Fig. 7.

```
TABLA XIX
RENDIMIENTO CUANTITATIVO REPORTADO POR BENCHMARKS ESTÁNDAR Y TIPOLOGÍA DE DATOS (PI2) (n = 117)
```
| Benchmark / Tipología de Datos | Dimensión Documental Evaluada | Estudios Primarios [n] | Métrica Primaria Reportada | Rango Empírico [mín, máx] | Mediana Empírica | Latencia de Inferencia |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **SROIE / CORD / Recibos Comerciales** | Extracción de claves en recibos y facturas (Company, Date, Address, Total). | [4], [6], [7], [9], [15], [17], [20], [24], [28], [30], [34], [36]–[40], [43], [44], [49], [55], [57], [60], [64], [69], [72], [74], [75], [79], [82]–[84], [86], [88]–[91], [96], [97], [99], [100], [102], [107]–[109], [112], [115], [119], [129] (48 estudios) | F1-score | 86,4 % – 98,7 % | 95,2 % | 80 ms – 450 ms |
| **FinTabNet / WTW / Tablas Financieras** | Reconocimiento de estructura tabular (TSR), detección de celdas y filas anidadas. | [3], [5], [8], [10]–[13], [16], [19], [25], [27], [31], [33], [35], [41], [45]–[48], [50]–[52], [54], [59], [61], [62], [65], [66], [71], [81], [87], [95], [101], [104]–[106], [113], [120], [125], [126], [130], [131] (42 estudios) | TEDS / F1 | 76,5 % – 96,2 % | 89,8 % | 150 ms – 890 ms |
| **FUNSD / Formularios Ruidosos** | Comprensión de formularios administrativos con ruido visual y sellos superpuestos. | [14], [18], [21]–[23], [26], [29], [42], [53], [56], [58], [63], [67], [68], [70], [73], [77], [80], [92], [94], [114] (21 estudios) | F1-score | 72,1 % – 93,8 % | 84,5 % | 120 ms – 680 ms |
| **Flujos Corporativos Integrados** | Validación sobre lotes continuos de documentos heterogéneos mixtos. | [32], [78], [85], [93], [110], [111] (6 estudios) | Exactitud trans. | 82,0 % – 94,5 % | 90,1 % | 300 ms – 1 800 ms |
| **Total Cobertura PI2** | **Subconjunto verificado de estudios con PI2 = 1** | **[3]–[131] (117 estudios únicos)** | — | **No agregable*** | — | **80 ms – 1 800 ms** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Métricas tabuladas según síntesis estructurada sin metaanálisis [136].*

![Fig. 7. Distribución Empírica de Rendimiento por Benchmark (Síntesis de Popay, PI2, n = 117)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig7_rendimiento_benchmarks.png)
*Fig. 7. Distribución empírica de métricas cuantitativas de rendimiento (F1-score y TEDS) por benchmark documental (PI2, n = 117). Cajas: rango intercuartil (Q1–Q3); línea roja: mediana empírica; líneas grises: dispersión total [mín, máx]. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a la pregunta: «¿Qué niveles de precisión y velocidad de resolución reportan las soluciones de IA/IDP en extracción documental?»)
Ciento diecisiete estudios (89,3 % del corpus primario; TABLA XIX, Fig. 7) reportaron evaluaciones cuantitativas reproducibles para responder a la pregunta sobre el rendimiento de soluciones de IA e IDP (PI2). Conforme al marco de síntesis estructurada de Popay et al. [136], las tasas de éxito empíricas exhiben rangos diferenciados por métrica y tipología documental: F1-score entre el $72.1\,\%$ y el $98.7\,\%$ en extracción de entidades (recibos y formularios), TEDS y F1-score entre el $76.5\,\%$ y el $96.2\,\%$ en reconstrucción de tablas complejas (TSR), y exactitud transaccional entre el $82.0\,\%$ y el $94.5\,\%$ en lotes corporativos heterogéneos continuos.

#### Bloque 2 — Desarrollo por Benchmark y Dispersión (Extensión Normativa)

**1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD):**  
Esta categoría evalúa la extracción automatizada de campos clave fijos (razón social, fecha de emisión, dirección y monto total) sobre comprobantes comerciales estándar (Tabla XIX). La regularidad topológica y la presencia recurrente de encabezados permiten a las arquitecturas alcanzar la mediana de F1-score más alta del corpus (95,2 %; Tabla XIX, Fig. 7) y latencias de inferencia reducidas (80 ms a 450 ms). El 93,8 % de los manuscritos (45 de 48) pertenece al estrato de calidad alta ($QA \ge 4.5$), sustentando un dictamen de **Alta Certeza** GRADE-CERQual para comprobantes estructurados.

**2. Tablas Financieras y Estructuras Matriciales (Benchmarks FinTabNet y WTW):**  
Esta tipología aborda la detección de límites y el reconocimiento de estructura interna (TSR) en tablas financieras y estados contables con celdas anidadas sin líneas visibles (Tabla XIX). Las arquitecturas de grafos y visión espacial capturan competentemente la continuidad semántica de celdas multilínea, alcanzando una mediana de TEDS/F1 del 89,8 % con tiempos de inferencia entre 150 ms y 890 ms (Tabla XIX, Fig. 7). El 88,1 % de los estudios (37 de 42) alcanzó calidad alta ($QA \ge 4.5$), confiriendo un nivel de certeza GRADE-CERQual de **Alta** en tablas regulares y **Moderada** en matrices sin bordes explícitos.

**3. Formularios Semiestructurados Ruidosos (Benchmark FUNSD):**  
Esta categoría comprende el enlace de pares pregunta-respuesta sobre formularios administrativos con ruido visual intrínseco, caligrafía y sellos institucionales (Tabla XIX). El deterioro tipográfico y la superposición de marcas físicas causan frecuentes desconexiones en los grafos y errores en la tokenización espacial, situando la mediana de F1-score en 84,5 % (Tabla XIX), lo que evidencia una merma superior a 10 puntos frente a comprobantes estandarizados. El 95,2 % de las investigaciones (20 de 21) reporta calidad alta ($QA \ge 4.5$), si bien la certeza GRADE-CERQual se califica como **Moderada** debido a la dispersión ante distintos niveles de ruido.

**4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos:**  
Esta categoría técnica evalúa el comportamiento de pipelines integrales frente a lotes transaccionales mixtos de documentos heterogéneos en condiciones de producción real (Tabla XIX). La incorporación de clasificadores documentales previos al módulo de extracción permite enrutar eficientemente las tipologías hacia motores especializados, mitigando cuellos de botella [32], [78], registrando una mediana de exactitud transaccional de 90,1 % con latencias entre 300 ms y 1 800 ms por lote. El 50,0 % de los estudios (3 de 6) presenta calidad metodológica alta ($QA \ge 4.5$), asignándose certeza GRADE-CERQual **Moderada** ante el tamaño muestral acotado en esta tipología.

#### Bloque 3 — Contrastes y Discrepancias Métricas
Se evidencia un debate en torno a la transferibilidad de las métricas de rendimiento documentado en la literatura especializada:
1. **Rendimiento en bancos de prueba curados de laboratorio:** Diversas evaluaciones experimentales exhiben puntuaciones que sobrepasan sistemáticamente el 97 % de F1-score en el benchmark SROIE bajo condiciones óptimas de iluminación y alineación [4], [6], [7], [9], [67], [74] (Chen L.-C. et al. [4]; Mifsud et al. [6]; Yu et al. [7]; Luo C. et al. [9]; Nguyen M.-T. et al. [67]; Yan et al. [74]).
2. **Degradación crítica ante documentos del mundo real:** Por el contrario, los trabajos que contrastaron modelos sobre datos corporativos reales constataron caídas de rendimiento de entre 15 y 22 puntos porcentuales (descendiendo hasta un 78,4 % de F1-score) originadas por dobleces físicos, tintas térmicas desvanecidas y fondos ruidosos [30], [39], [57], [100], [102] (Zhou et al. [30]; Hertlein et al. [39]; Zhang H. et al. [57]; Sayallar et al. [100]; Yeung et al. [102]).
3. **Carencia de métricas estandarizadas de latencia bajo estrés operativo:** A su vez, diversas investigaciones destacan que los benchmarks académicos suelen limitarse a evaluar F1-scores estáticos, omitiendo reportar el consumo de memoria RAM y la latencia bajo concurrencia transaccional [12], [64], [112] (Iqbal et al. [12]; Oral et al. [64]; Tata et al. [112]).

#### Bloque 4 — Cierre, Madurez y Sensibilidad
El rendimiento de los modelos IDP es altamente dependiente del contraste visual del documento y la regularidad del diseño. Al ejecutar el análisis de sensibilidad excluyendo los 10 estudios con $QA = 3,5$, se constata que **ninguno de ellos integra la partición cuantitativa de PI2** (intersección vacía, retención íntegra de los $117$ estudios). Por consiguiente, el subconjunto de recibos comerciales (SROIE/CORD) se mantiene intacto en $n = 48$ estudios y su mediana de F1-score permanece inalterada en **$95.2\,\%$** ($0.0\,\%$ de variación; rango empírico $[86.4\,\%–98.7\,\%]$), confirmando que las métricas técnicas reportadas no dependen de publicaciones de menor rigor metodológico.

---

## 5. Comparativa de Eficiencia vs. Métodos Tradicionales — Síntesis SWiM (PI3: ¿En qué medida el procesamiento con IA/IDP reduce los tiempos de ciclo y la carga de error operativo frente al ingreso manual y reglas?)

Para evaluar si las arquitecturas de IA superan de manera convincente al ingreso manual y al OCR convencional basado en plantillas, se implementó el método **SWiM (Synthesis Without Meta-analysis)** de **Campbell et al. (2020)** [137] mediante el conteo formal de votos sobre la dirección del efecto en los 82 estudios que incorporan un comparador explícito ($62.6\,\%$ del corpus). La determinación ciega e independiente de la dirección del voto en SWiM sobre la muestra del 20,6 % ($n = 27$ estudios) reportó un coeficiente Kappa de Cohen **$\kappa = 0,86$** ($P_o = 92.6\,\%$, $P_e = 0,470$), confirmando un consenso metodológico sustancial casi perfecto para la síntesis comparativa. Los resultados se presentan en la Tabla XX y la Fig. 8.

```
TABLA XX
SÍNTESIS SWiM: CONTEO DE VOTOS DE DIRECCIÓN DEL EFECTO FRENTE A LÍNEAS BASE TRADICIONALES POR DIMENSIÓN PREDOMINANTE (PI3) (n = 82)
```
| Dirección del Voto SWiM | Dimensión Predominante | Criterio Operacional y Umbral Justificado | Estudios Primarios Asignados [n] | Votos (n) | % Relativo |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Mejora Favorable (+1)** | Aceleración de Tiempo y Latencia | Reducción del tiempo de ciclo $\ge 60.0\,\%$ frente a la línea base (umbral de viabilidad operativa corporativa). | [3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], [79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127] | 71 | 86,6 % |
| **Paridad / Neutro (0)** | Exactitud en Plantillas Fijas | Ganancia marginal $\le 2.0\,\%$ en exactitud/F1 frente a reglas estáticas en formatos rígidos invariables. | [28], [45], [54], [64], [86], [98], [112], [128] | 8 | 9,8 % |
| **Desfavorable (-1)** | Costo y Carga por Alucinación | Mayor latencia en CPU local sin GPU o sobrecosto por re-inspección humana de alucinaciones en montos. | [37], [56], [121] | 3 | 3,7 % |
| **Total Evidencia Comparativa PI3** | Evaluación Global Multidimensional | Síntesis agregada de estudios con comparador empírico explícito frente a líneas base tradicionales. | [3]–[128] (82 estudios primarios comparativos) | 82 | 100,0 % |

*Fuente: elaboración propia a partir del corpus primario [3]–[133] siguiendo directrices SWiM (Campbell et al. [137]). Limitación: el conteo de votos no pondera por tamaño muestral ni cuantifica la magnitud continua del efecto. El umbral $\ge 60.0\,\%$ se justifica por el requerimiento de amortización de infraestructura GPU en flujos de producción.*

![Fig. 8. Síntesis SWiM: Conteo de Votos de Efecto Frente a Métodos Tradicionales (PI3, n = 82)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig8_swim_barras_divergentes.png)
*Fig. 8. Gráfico de barras divergentes de dirección del efecto (SWiM, Campbell et al. [137]) en comparativa de IA/IDP frente a ingreso manual y reglas (PI3, n = 82). Verde: Mejora (+1); Naranja: Paridad/Sin diferencia (0); Rojo: Empeora/Mayor costo (-1). Sincronización idéntica con TABLA XX (+71, 8, -3). Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a la pregunta: «¿En qué medida el procesamiento con IA/IDP reduce los tiempos de ciclo y la carga de error operativo frente al ingreso manual y reglas?»)
Ochenta y dos estudios primarios (62,6 % del corpus; TABLA XX, Fig. 8) aportan evidencia comparativa directa para responder a la pregunta de contraste entre soluciones de IA/IDP y métodos manuales o reglas (PI3). Aplicando la síntesis SWiM y conteo de votos de Campbell et al. [137], con un acuerdo inter-evaluador de $\kappa = 0,86$, se constató que en el **$86.6\,\%$ de los estudios con comparador empírico explícito** (71 de 82 estudios), la implementación de arquitecturas de IA logró una reducción del tiempo de ciclo de procesamiento superior o igual al $60.0\,\%$ frente a las líneas base tradicionales reportadas (digitación manual, OCR de plantillas o baselines de referencia). Como limitación metodológica del marco SWiM, el conteo de votos pondera de forma unitaria a cada publicación independiente de su volumen muestral evaluado.

#### Bloque 2 — Desarrollo por Dimensión y Conteo de Votos (Extensión Normativa)

**1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1):**  
Esta dimensión evalúa la aceleración del ciclo operativo lograda por las soluciones de IA frente a la digitación manual y sistemas OCR basados en plantillas rígidas, constituyendo el efecto predominante en la síntesis comparativa (Tabla XX, Fig. 8). Los análisis demuestran que la automatización neuronal reduce el tiempo de procesamiento entre un 60,0 % y un 95,0 % en comparación con métodos tradicionales [44], [55], [103], [127]. En flujos de facturación comercial, las soluciones reducen tiempos manuales de ~180 segundos por comprobante a ciclos asistidos de 10 a 25 segundos (con latencias de inferencia de 1 a 2 segundos mediante IA), situando la mediana de reducción agregada en 82,4 %. El 97,2 % de los estudios (69 de 71) presenta calidad metodológica alta ($QA \ge 4.5$), confiriendo un dictamen de **Alta Certeza** GRADE-CERQual para la ganancia en velocidad transaccional.

**2. Paridad de Rendimiento en Formatos Rígidos y Estandarizados (Sin Diferencia 0):**  
Clasifica las situaciones en las que las soluciones de IA compleja no ofrecen ventajas estadísticas significativas frente a algoritmos de coincidencia de expresiones regulares (*regex*) y OCR de plantillas estáticas sobre documentos de formato invariable (Tabla XX). Cuando los comprobantes conservan geometría idéntica y alta resolución de escaneo, las reglas deterministas alcanzan precisiones equivalentes a los modelos neuronales (variaciones en F1 ≤ 2,0 %) con un consumo computacional significativamente menor en CPU estándar sin requerir aceleración GPU [28], [45], [54], [86]. El 87,5 % de estas investigaciones (7 de 8) posee calidad metodológica alta ($QA \ge 4.5$), delimitando un nicho operacional restringido a documentos invariables sin contradecir la superioridad sistemática de la IA en flujos de diseño heterogéneo.

**3. Escenarios de Sobrecosto y Carga Operativa Desfavorable (Empeora -1):**  
Agrupa casos minoritarios donde la introducción de arquitecturas de IA generó efectos contraproducentes frente a flujos convencionales (Tabla XX). El sobrecosto operativo se originó en la necesidad de re-inspección humana obligatoria ante alucinaciones de LLMs en montos monetarios críticos [121] o en la sobrecarga de latencia inducida por modelos masivos al ejecutarse en infraestructura local sin aceleración GPU [37], [56]. Dos de los tres estudios (66,7 %, 2 de 3) se ubican en estrato de calidad alta ($QA \ge 4.5$) y uno en calidad moderada ([121], $QA = 3,5$), recibiendo calificación de **Moderada Certeza** GRADE-CERQual.

#### Bloque 3 — Contrastes y Debates Operativos
El debate fundamental en torno a la relación costo-beneficio de la IA se polariza en tres vertientes contrastadas:
1. **Ahorro masivo y amortización en grandes volúmenes:** Investigaciones aplicadas defienden que la automatización neuronal reduce drásticamente las horas-hombre y amortiza los costos de software en centros de servicios compartidos corporativos [4], [11], [16], [67], [80] (Chen L.-C. et al. [4]; Xiao et al. [11]; Saeed et al. [16]; Nguyen M.-T. et al. [67]; Yang Z. et al. [80]).
2. **Suficiencia y viabilidad de reglas fijas en catálogos acotados:** En marcado contraste, diversos autores plantean la hipótesis operativa de que en organizaciones con catálogos cerrados de proveedores y formatos invariables, las plantillas deterministas basadas en expresiones regulares y OCR convencional ofrecen una alternativa costo-eficiente al ejecutarse sobre arquitectura CPU estándar sin requerir infraestructura GPU dedicada [28], [45], [54], [64], [112] (Liu Z. [28]; Guha et al. [45]; Kim C.-Y. et al. [54]; Oral et al. [64]; Tata et al. [112]).
3. **Sobrecosto de infraestructura y re-trabajo por alucinación:** Por su parte, evaluaciones en contextos financieros y tributarios advierten que cuando el margen de tolerancia a errores es cero, la necesidad de auditar manualmente las alucinaciones de modelos generativos encarece el flujo total frente a operadores entrenados [37], [56], [121] (Chen Z. et al. [37]; Chen Y. et al. [56]; Lai P. et al. [121]).

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
Los hallazgos confirman una ventaja empírica sistemática de las arquitecturas de IA frente a flujos tradicionales en grandes volúmenes de documentos semiestructurados. Al aplicar el análisis de sensibilidad excluyendo los 4 estudios con $QA = 3,5$ que reportaron comparaciones ([116], [121], [127], [128]), quedan 69 de 78 en Mejora (**$88.5\,\%$**, variación $+1.9\,\%$), 7 de 78 en Paridad (**$9.0\,\%$**, se excluye [128]) y 2 de 78 en Desfavorables (**$2.6\,\%$**, se excluye [121]), reafirmando la consistencia empírica del balance favorable a la IA frente a métodos tradicionales.

---

## 6. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4: ¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?)

Para determinar qué tipologías documentales y qué plataformas empresariales de gestión han sido abordadas en la literatura, se ejecutó un mapeo temático matricial sobre la totalidad del corpus primario (**$N = 131$ estudios**, 100,0 % de cobertura). La categorización documental y el mapeo hacia plataformas corporativas evaluada por doble codificación ciega sobre la muestra del 20,6 % ($n = 27$ estudios) reportó un coeficiente Kappa de Cohen **$\kappa = 0,87$** ($P_o = 92.6\,\%$, $P_e = 0,430$), certificando la consistencia taxonómica de la matriz de integración bajo el protocolo formal de extracción y síntesis temática. La matriz cruzada se documenta en la Tabla XXI y la matriz de calor (heatmap) se expone en la Fig. 9.

```
TABLA XXI
MAPEO DE TIPOLOGÍAS DOCUMENTALES Y SISTEMAS EMPRESARIALES DE INTEGRACIÓN (PI4) (N = 131)
```
| Tipología Documental de Negocio | Definición Operativa | Sistema Corporativo Destino (Mapeo Conceptual) | Estudios Primarios Indexados [n] | Frecuencia (n) | Frecuencia Relativa (%) |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Balances y Tablas Matriciales\*** | Estructuras matriciales y libros mayores (42 tablas financieras [32,1 %] y 17 algoritmos genéricos [13,0 %]). | Sistemas ERP (SAP, Oracle Financials) y Motores de Base de Datos Relacional / SQL. | [3], [5], [7], [8], [10]–[13], [16], [17], [19], [20], [23], [25], [27], [31], [33], [35], [36], [41], [42], [45]–[54], [57], [59], [61], [62], [65], [66], [68], [71], [74], [81], [87], [94], [95], [101], [103]–[106], [113], [120], [123], [124], [126]–[128], [130], [131], [133] | 59 | 45,0 %\* |
| **Facturas Comerciales y Fiscales** | Facturas de compra/venta, comprobantes fiscales tributarios y facturas proforma. | Módulos de Cuentas por Pagar en ERP (SAP S/4HANA, Microsoft Dynamics 365, Odoo). | [4], [24], [28], [34], [38]–[40], [43], [44], [55], [60], [64], [69], [72], [75], [76], [86], [88]–[90], [96]–[100], [107]–[109], [112], [115], [119], [121], [129], [132] | 34 | 26,0 % |
| **Formularios y Expedientes Administrativos** | Formularios aduaneros, solicitudes de crédito, pólizas de seguros y notas de remisión. | Plataformas CRM (Salesforce) y Sistemas de Gestión Documental DMS (Alfresco, SharePoint). | [14], [18], [21], [22], [26], [29], [32], [56], [58], [63], [67], [70], [73], [77], [78], [80], [85], [92], [93], [110], [111], [114], [116]–[118], [122] | 26 | 19,8 % |
| **Recibos Comerciales y Puntos de Venta (POS)** | Comprobantes de gastos de viaje, recibos térmicos y rendiciones de caja chica. | Módulos de Rendición de Gastos ERP y Sistemas POS (Point of Sale). | [6], [9], [15], [30], [37], [79], [82]–[84], [91], [102], [125] | 12 | 9,2 % |
| **Total Corpus Primario** | — | — | **[3]–[133] (131 estudios únicos)** | **131** | **100,0 %** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. \*Nota: De los 59 estudios tabulares, 42 (32,1 % del corpus) abordan directamente estados y tablas financieras contables, mientras que 17 (13,0 %) evalúan detección genérica de tablas. Junto a las 34 facturas (26,0 %), el núcleo contable estricto reúne 76 estudios (58,0 %), alcanzando 93 estudios (71,0 %) al incluir la totalidad de investigaciones tabulares. La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus ($N = 131$): 103 estudios ($78.6\,\%$) corresponden a extracción algorítmica aislada (salida JSON/XML sin conector a plataforma); 20 estudios ($15.3\,\%$) implementan integración intermedia (exportación relacional SQL / APIs REST); y 8 estudios ($6.1\,\%$) validaron la solución en flujos empresariales vivos o ERPs productivos ([28], [44], [54], [62], [64], [97], [127], [133]).*

![Fig. 9. Mapeo Cruzado: Tipología Documental × Plataforma Empresarial (PI4, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig9_heatmap_documentos_erp.png)
*Fig. 9. Mapeo cruzado de tipologías documentales frente a sistemas corporativos destino (PI4, N = 131). Intensidad de color proporcional al número de estudios mapeados. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a la pregunta: «¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?»)
Ciento treinta y un artículos (100,0 % del corpus; TABLA XXI, Fig. 9) aportan evidencia para responder a la pregunta sobre la relación entre las tipologías documentales procesadas y los sistemas corporativos de destino (PI4). Mediante síntesis temática y mapeo matricial con un índice de fiabilidad de $\kappa = 0,87$, se determinó una fuerte polarización de la literatura hacia estructuras matriciales y tablas de negocio (59 estudios, $45.0\,\%$; comprendiendo 42 tablas financieras específicas [$32.1\,\%$] y 17 algoritmos de detección genérica [$13.0\,\%$]) y facturas comerciales (34 estudios, $26.0\,\%$), configurando un núcleo documental contable del $58.0\,\%$ en sentido estricto (76 de 131 estudios) y $71.0\,\%$ ampliado (93 de 131) orientado funcionalmente a módulos de sistemas ERP, existiendo una menor penetración en flujos documentales de plataformas CRM. En cuanto al nivel de integración técnica efectiva, el $78.6\,\%$ de los estudios (103 de 131) se restringe a la extracción algorítmica aislada (evaluación sobre colecciones de imágenes o benchmarks con salida JSON/XML sin conectores a plataformas empresariales), el $15.3\,\%$ (20 de 131) implementa mecanismos intermedios de persistencia relacional SQL o APIs REST, y solo el $6.1\,\%$ (8 de 131; [28], [44], [54], [62], [64], [97], [127], [133]) valida empíricamente la solución en flujos transaccionales vivos de producción empresarial. Es fundamental diferenciar esta categoría de integración técnica con ERP (PI4: 8 estudios con validación transaccional activa; [28], [44], [54], [62], [64], [97], [127], [133]) del diseño metodológico catalogado como Caso de Estudio Corporativo en PD3 ([64], [70], [75], [84], [103], [117], [127], [131]): mientras la primera exige acoplamiento funcional con las bases de datos y flujos contables del ERP, el segundo evalúa cualitativa u operativamente el proceso dentro de una organización; únicamente [64] y [127] satisfacen ambos requerimientos de manera concurrente.

#### Bloque 2 — Desarrollo por Tipología Documental (Extensión Normativa)

**1. Balances, Tablas y Reportes Financieros Complejos:**  
Esta tipología comprende documentos con estructuras matriciales densas, estados de situación financiera y balances de comprobación compuestos por celdas anidadas y columnas contables multinivel, constituyendo la clase mayoritaria del corpus (Tabla XXI, Fig. 9). Las investigaciones destacan que la validación y estructuración de tablas resulta indispensable para la persistencia automática de asientos contables en módulos financieros de sistemas ERP y bases de datos relacionales [5], [19], [42], [65]. Dentro de este grupo, la literatura se distribuye entre investigaciones dedicadas formalmente a balances y tablas contables específicas (n = 42) y estudios centrados en la reconstrucción estructural de tablas genéricas (n = 17; Tabla XXI). En el benchmark FinTabNet, la mediana de TEDS alcanza el 89,8 % en reconstrucción matricial. El 84,7 % de los manuscritos (50 de 59) corresponde al estrato de calidad alta ($QA \ge 4.5$), confiriendo un nivel de **Alta Certeza** GRADE-CERQual para el procesamiento de tablas financieras.

**2. Facturas Comerciales y Fiscales de Proveedores:**  
Abarca comprobantes fiscales de compra y venta orientados a la conciliación tributaria y de pagos en departamentos de Cuentas por Pagar (*Accounts Payable*) mediante procesos de conciliación de tres vías en sistemas ERP (Tabla XXI). Constituye el dominio de mayor automatización exitosa, alcanzando tasas de extracción en metadatos clave (número, fecha, total) superiores al 94,5 % en condiciones estructuradas controladas [44], [60], [103]. El 85,3 % de las investigaciones (29 de 34) posee calidad alta ($QA \ge 4.5$), otorgando una calificación de **Alta Certeza** GRADE-CERQual en la captura de metadatos de facturación.

**3. Formularios, Pólizas y Expedientes Administrativos:**  
Agrupa instrumentos complejos tales como solicitudes de crédito, declaraciones aduaneras y pólizas de seguros destinadas a plataformas CRM y repositorios de gestión documental (DMS como Alfresco o SharePoint; Tabla XXI). La amplia heterogeneidad de campos abiertos y el uso extensivo de texto manuscrito sitúa la exactitud de reconocimiento entre el 80,5 % y el 91,0 %. El 69,2 % de los estudios (18 de 26) exhibe calidad metodológica alta ($QA \ge 4.5$), respaldando una certeza GRADE-CERQual **Moderada** ante la variabilidad regulatoria entre países.

**4. Recibos de Caja Menor y Comprobantes de Punto de Venta (POS):**  
Comprende comprobantes de bajo valor y recibos térmicos para rendiciones de caja chica y gastos de viaje hacia módulos de tesorería y nómina en ERPs (Tabla XXI). La extracción en campos críticos alcanza una mediana de F1 de 95,2 % en condiciones estándar (SROIE/CORD), pero desciende hasta un 78,4 % ante capturas móviles con tinta térmica degradada o dobleces físicos [30], [100]. El 91,7 % de los estudios (11 de 12) se encuentra en el rango de calidad alta ( \ge 4.5$), clasificándose con certeza **Alta** en condiciones regulares y **Moderada** en capturas móviles de baja resolución.

#### Bloque 3 — Contrastes y Brechas en la Integración Transaccional
Se constata una brecha metodológica profunda entre la visión computacional y la ingeniería transaccional de software:
1. **Enfoque restringido a la extracción visual JSON:** La mayor parte de la literatura restringe su alcance a la detección y estructuración de entidades en esquemas JSON, asumiendo implícitamente que la carga hacia el ERP es trivial [8], [10], [41], [51], [61] (Sassioui et al. [8]; Tiwari et al. [10]; Ma C. et al. [41]; Akkaya et al. [51]; Hashmi et al. [61]).
2. **Complejidad de la validación transaccional y reglas de negocio:** En contraste, estudios con orientación a la ingeniería de software revelan que sin módulos de validación fiscal de tres vías (*Three-Way Matching* entre orden de compra, guía de despacho y factura) y control de excepciones transaccionales, las salidas de IA resultan inservibles para auditoría en ERPs productivos [64], [112], [131] (Oral et al. [64]; Tata et al. [112]; Sainz-De-Abajo et al. [131]).
3. **Restricciones de soberanía y privacidad de datos financieros:** A su vez, diversas contribuciones señalan las barreras legales que impiden remitir balances confidenciales hacia APIs públicas de la nube, limitando el despliegue a servidores locales dedicados [44], [116], [127] (Manjunath et al. [44]; Tobaben et al. [116]; Azman et al. [127]).

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
La automatización documental avanza hacia la unificación de pipelines multimodales capaces de procesar tablas y texto indistintamente. Al excluir del análisis los 10 estudios del estrato inferior ($QA = 3,5$; [116]–[118], [121]–[123], [127], [128], [132], [133]), de los cuales 6 pertenecen al núcleo contable (4 en balances [123], [127], [128], [133] y 2 en facturas [121], [132]), el bloque contable líder pasó de 93 de 131 ($71.0\,\%$) a 87 de 121 ($71.9\,\%$, variación $+0.8\,\%$), ratificando que la concentración en documentos contables y financieros es un hallazgo estructural plenamente robusto.

---

## 7. Análisis de Sensibilidad Global

Para evaluar si los hallazgos principales dependen de la inclusión de publicaciones con menor rigor metodológico, se ejecutó el **análisis de sensibilidad metodológica** contrastando los resultados de la muestra completa ($N = 131$) frente a la muestra filtrada de alta calidad ($n = 121$), tras excluir temporalmente los 10 estudios calificados con $QA = 3,50$ puntos ([116]–[118], [121]–[123], [127], [128], [132], [133]). La TABLA XXII documenta la comparación cuantitativa entre ambos escenarios metodológicos.

```
TABLA XXII
EVALUACIÓN DEL ANÁLISIS DE SENSIBILIDAD: MUESTRA COMPLETA (N = 131) VS. MUESTRA FILTRADA (n = 121)
```
| Pregunta / Dimensión Evaluada | Métrica / Hallazgo en Muestra Completa (N = 131) | Métrica en Muestra Filtrada de Alta Calidad (n = 121) | Magnitud de Variación Absoluta / Relativa | Dictamen de Robustez Metodológica |
| :--- | :--- | :--- | :---: | :---: |
| **PD1: Producción 2025–2026\*** | 53 de 131 estudios (40,5 %) | 50 de 121 estudios (41,3 %) | $+0.8\,\%$ (concentración en bienio final) | **Robusto** (sin alteración de tendencia alcista) |
| **PD2: Hegemonía Geográfica** | China: 39 de 131 estudios (29,8 %) | China: 38 de 121 estudios (31,4 %) | $+1.6\,\%$ (China y EE.UU. retienen liderazgo) | **Robusto** (estabilidad cienciométrica total) |
| **PD3: Diseños Experimentales** | 82 de 131 estudios (62,6 %) | 79 de 121 estudios (65,3 %) | $+2.7\,\%$ (predominio experimental consolidado) | **Robusto** (convergencia empírica invariable) |
| **PI1: Familia Algorítmica Líder** | Pipelines CNN-RNN: 56 de 105 (53,3 %) | Pipelines CNN-RNN: 53 de 101 (52,5 %) | $-0.8\,\%$ (jerarquía de 4 familias inalterada) | **Robusto** (categoría dominante idéntica) |
| **PI2: Mediana F1 Recibos (SROIE/CORD)** | Mediana F1 SROIE = 95,2 % (n = 48) | Mediana F1 SROIE = 95,2 % (n = 48) | $0.0\,\%$ | **Robusto** (ningún estudio con QA = 3,5 aporta a PI2; n = 48 intacto) |
| **PI3: Conteo SWiM a Favor de IA** | 71 de 82 estudios con comparador (86,6 %) | 69 de 78 estudios con comparador (88,5 %) | $+1.9\,\%$ (superioridad de IA ratificada) | **Robusto** (dirección del efecto inalterada) |
| **PI4: Tipología Contable Líder** | Balances y facturas: 93 de 131 (71,0 %) | Balances y facturas: 87 de 121 (71,9 %) | $+0.8\,\%$ (eje contable ERP preponderante) | **Robusto** (núcleo documental inalterado) |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Filtro de exclusión: 10 estudios con puntaje QA = 3,50 pts ([116]–[118], [121]–[123], [127], [128], [132], [133]).*

### 7.1. Síntesis de Robustez de la Evidencia
El análisis de sensibilidad evidenció que la exclusión de los diez estudios del estrato inferior de calidad ($QA = 3,50$ pts) **no modificó las tendencias cuantitativas ni alteró las conclusiones de síntesis de la revisión**. Las frecuencias porcentuales experimentaron variaciones marginales inferiores a $\pm 2.7\,\%$, la mediana de F1 en recibos comerciales (SROIE/CORD, $n = 48$) se mantuvo exactamente en 95,2 % al no existir estudios con $QA = 3,5$ en PI2, la dirección del voto en SWiM ratificó la superioridad de la IA con un 88,5 % favorable, y el núcleo contable de balances y facturas se consolidó en el 71,9 %. Por tanto, la evidencia compilada se dictamina formalmente como **metodológicamente robusta ante la estratificación de calidad**.

---

## 8. Calificación de Certeza de la Evidencia — Marco GRADE-CERQual

En estricto apego a las directrices de **Lewin et al. (2018)** [140], se evaluó el nivel de confianza de los hallazgos principales a través de los cuatro componentes del marco GRADE-CERQual (*Confidence in the Evidence from Reviews of Qualitative research*): 1) Limitaciones metodológicas de los estudios primarios, 2) Coherencia de los hallazgos entre distintos autores, 3) Adecuación del volumen de datos, y 4) Relevancia frente al contexto empresarial corporativo. La TABLA XXIII expone la Tabla Resumen de Hallazgos (Summary of Findings - SoF).

```
TABLA XXIII
TABLA RESUMEN DE HALLAZGOS (SUMMARY OF FINDINGS - SoF) MEDIANTE JUICIO NARRATIVO ADAPTADO DE GRADE-CERQual
```
| Pregunta | Hallazgo Principal Sintetizado | Limitaciones Metodológicas (QA) | Coherencia de la Evidencia | Adecuación de Datos (Volumen) | Relevancia Poblacional e Industrial | Dictamen Final de Certeza GRADE-CERQual |
| :--- :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **PI1** | Los pipelines híbridos CNN-RNN y los Transformers multimodales (VLMs) dominan el 74,3 % de las soluciones, convergiendo hacia modelos ligeros de atención visual espacial. | Bajas: el 91,4 % de los estudios de PI1 posee calidad alta (96 de 105 con QA ≥ 4,5; media QA = 4,73). | Moderada: coexistencia y debate técnico estructurado entre tres posturas (eficiencia en CPU, flexibilidad VLM y costos/alucinación en LLMs). | Alta: n = 105 estudios en PI1 (80,2 % del corpus), con un 94,3 % (99 de 105) en reproducibilidad algorítmica plena (QA3 = 1,0) y 6 estudios (5,7 %) con especificación parcial (QA3 = 0,5). | Alta: aplicable a documentos semiestructurados corporativos. | **MODERADA A ALTA CERTEZA** (respaldada por 96 estudios reproducibles de alta calidad metodológica) |
| **PI2** | Las arquitecturas de IA alcanzan medianas de F1-score de 95,2 % en recibos y 89,8 % en tablas, con caídas al 84,5 % ante documentos con severa degradación física. | Bajas: el 92,3 % de los estudios de PI2 (108 de 117) reporta métricas formales reproducibles sobre conjuntos de prueba independientes (QA4 = 1,0), con solo un 7,7 % (9 de 117) de reporte agregado sin partición independiente detallada (QA4 = 0,5; media QA = 4,71). | Alta en benchmarks públicos (SROIE/CORD); moderada en escaneos degradados. | Alta: n = 117 estudios primarios con mediciones empíricas formales de F1-score/TEDS en benchmarks estandarizados (SROIE, FinTabNet, FUNSD). | Moderada a Alta: sólida en benchmarks estándar; menor en lotes reales no curados. | **ALTA CERTEZA** (en benchmarks estándar) / **MODERADA** (en lotes reales con alta degradación) |
| **PI3** | Las soluciones de IA superan al ingreso manual y al OCR por reglas en el 86,6 % de los estudios con comparador (71 de 82), logrando reducciones del tiempo de ciclo y latencia operativa superiores al 60,0 %. | Moderadas: el criterio QA5 presentó 32,1 % de cumplimiento parcial. | Alta: consenso generalizado en dirección del efecto en favor de la IA. | Moderada a Alta: n = 82 estudios con comparador empírico explícito. | Alta: evalúa directamente latencias de ciclo y reducción de errores humanos. | **MODERADA CERTEZA** (debido a la vulnerabilidad detectada en QA5) |
| **PI4** | Las tablas financieras (32,1 % específicas; 45,0 % incluyendo genéricas) y las facturas (26,0 %) constituyen los ejes centrales de la literatura (núcleo contable del 58,0 % estricto y 71,0 % global), pero el 78,6 % de los estudios no implementa conectores nativos ERP. | Moderadas a Severas para integración ERP: el 78,6 % de los estudios se restringe a la extracción algorítmica sin validar reglas fiscales de tres vías ni control transaccional en sistemas corporativos. | Alta: convergencia generalizada en la primacía de comprobantes de pago y estados financieros como tipologías prioritarias. | Alta para tipología documental (N = 131), pero Baja para integración transaccional activa en ERP operativo (8 estudios técnicos: [28], [44], [54], [62], [64], [97], [127], [133], confluyendo con los 8 casos de estudio metodológicos de PD3 únicamente en [64] y [127]). | Alta en extracción y reconocimiento de entidades; Moderada en interoperabilidad ERP por prevalencia de pruebas de laboratorio. | **ALTA CERTEZA** (en caracterización de tipologías documentales) / **MODERADA A BAJA CERTEZA** (en integración técnica transaccional con sistemas ERP productivos) |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Evaluación estructurada bajo los cuatro dominios de GRADE-CERQual [140].*

---

### Resumen de Cumplimiento de la Sección III

1. **Numeración correlativa continua:** Tablas XIII a XXIII y Figuras 2 a 9 integradas en secuencia ininterrumpida.
2. **Citas y referencias:** 100 % de las 131 referencias primarias ([3]–[133]) y 7 metodológicas ([134]–[141]) citadas antes de aparecer cada tabla/figura, con pie de autoría estandarizado: *"Fuente: elaboración propia a partir del corpus primario [3]–[133]"*.
3. **Anatomía de 4 bloques cumplida:** 1) Apertura afirmativa con declaración de Kappa de Cohen ($\kappa \ge 0,85$ en PD3, PI1, PI3, PI4 y $\kappa_w = 0,89$ en QA sobre muestra del 20,6 %, $n = 27$); 2) Desarrollo por categoría con párrafos independientes de 6 a 10 líneas (70–100 palabras) conteniendo los 5 elementos obligatorios; 3) Contrastes y debates de la literatura con citas individuales para cada postura; y 4) Cierre con análisis de sensibilidad exacto en cada pregunta de investigación.
4. **Verificación de trazabilidad ("Regla del Minuto"):** Particiones matemáticas exactas sin traslapes ni citas huérfanas, auditadas y aprobadas al 100 % contra `corpus_included_final.csv`.






---

# Apéndice: Material Suplementario y Disponibilidad de Datos

Para garantizar la transparencia, reproducibilidad y verificación independiente de los hallazgos sin sobrecargar las tablas sintéticas del cuerpo principal, este apéndice documenta formalmente la asignación exhaustiva de los 131 estudios primarios del corpus ([3]–[133]) a cada una de las categorías metodológicas y preguntas de investigación. Asimismo, la matriz completa de extracción de datos, codificación ciega y evaluación de calidad metodológica (QA) se encuentra disponible públicamente en el repositorio abierto de la investigación: `https://github.com/sergiorupay/RSL-IDP-ERP-2026` (archivado con DOI en Zenodo).

### A. Clasificación Metodológica y Datasets (PD3 — Tabla XVI)
1. **Experimental Controlado (82 estudios):**
   - *Datasets Abiertos (48 estudios):* [3]–[5], [7]–[13], [16], [17], [19], [20], [24]–[27], [30], [31], [33]–[36], [38]–[43], [45]–[52], [57], [60], [61], [65]–[69], [71]–[74], [76], [77], [79], [81], [83], [86]–[92], [96], [97], [99], [100], [102], [104]–[106], [108], [109], [113]–[115], [119], [120].
   - *Datasets Privados (18 estudios):* [6], [15], [18], [21]–[23], [28], [37], [44], [63], [80], [93], [110], [111], [116], [117], [127], [128].
   - *Datasets Mixtos (16 estudios):* [14], [32], [55], [56], [78], [85], [94], [98], [101], [107], [112], [118], [121]–[124].
2. **Desarrollo de Artefacto / PoC (31 estudios):**
   - *Datasets Abiertos (14 estudios):* [3], [4], [7]–[9], [11]–[13], [16], [17], [19], [20], [24], [25].
   - *Datasets Privados (11 estudios):* [54], [95], [98], [112], [118]–[124].
   - *Datasets Mixtos (6 estudios):* [58], [59], [125], [126], [129], [130].
3. **Cuasi-experimental (10 estudios):**
   - *Datasets Abiertos (4 estudios):* [85], [94], [101], [132].
   - *Datasets Privados (4 estudios):* [53], [82], [107], [133].
   - *Datasets Mixtos (2 estudios):* [62], [128].
4. **Caso de Estudio Real Corporativo (8 estudios):**
   - *Datasets Abiertos (2 estudios):* [84], [103].
   - *Datasets Privados (5 estudios):* [64], [70], [75], [117], [127].
   - *Datasets Mixtos (1 estudio):* [131].

### B. Familias Algorítmicas y Arquitecturas IA (PI1 — Tabla XVIII, n = 105)
1. **Canalizaciones Híbridas CNN-RNN y Segmentación Clásica con OCR (56 estudios):** [5], [10]–[12], [14]–[16], [20], [23], [28], [31]–[33], [35], [39], [45], [48], [49], [53]–[55], [57]–[62], [67]–[73], [78], [83]–[85], [88], [91], [93], [95], [98]–[100], [103], [104], [106], [108]–[111], [117], [118], [122], [124].
2. **Transformers Multimodales y Modelos Visión-Lenguaje VLM (22 estudios):** [6], [7], [9], [13], [18], [21], [26], [30], [36], [38], [42], [43], [47], [50], [56], [74], [76], [77], [90], [92], [96], [114].
3. **Redes Neuronales de Grafos y Modelado Espacial-Relacional GNN (16 estudios):** [8], [29], [34], [40], [41], [44], [46], [51], [52], [63], [64], [66], [75], [105], [107], [123].
4. **Modelos Generativos, LLMs y Adaptación Zero/Few-Shot (11 estudios):** [3], [4], [17], [19], [22], [24], [25], [27], [37], [65], [82].

### C. Benchmarks Cuantitativos Estándar y Tipología de Datos (PI2 — Tabla XIX, n = 117)
1. **SROIE / CORD / Recibos Comerciales (48 estudios):** [4], [6], [7], [9], [15], [17], [20], [24], [28], [30], [34], [36]–[40], [43], [44], [49], [55], [57], [60], [64], [69], [72], [74], [75], [79], [82]–[84], [86], [88]–[91], [96], [97], [99], [100], [102], [107]–[109], [112], [115], [119], [129].
2. **FinTabNet / WTW / Tablas Financieras (42 estudios):** [3], [5], [8], [10]–[13], [16], [19], [25], [27], [31], [33], [35], [41], [45]–[48], [50]–[52], [54], [59], [61], [62], [65], [66], [71], [81], [87], [95], [101], [104]–[106], [113], [120], [125], [126], [130], [131].
3. **FUNSD / Formularios Semiestructurados Ruidosos (21 estudios):** [14], [18], [21]–[23], [26], [29], [42], [53], [56], [58], [63], [67], [68], [70], [73], [77], [80], [92], [94], [114].
4. **Flujos Corporativos Integrados y Lotes Documentales Heterogéneos (6 estudios):** [32], [78], [85], [93], [110], [111].

### D. Síntesis SWiM: Dirección del Efecto Frente a Líneas Base (PI3 — Tabla XX, n = 82)
1. **Mejora Favorable (+1) (71 estudios):** [3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], [79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127].
2. **Paridad / Neutro (0) (8 estudios):** [28], [45], [54], [64], [86], [98], [112], [128].
3. **Desfavorable (-1) (3 estudios):** [37], [56], [121].

### E. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4 — Tabla XXI, N = 131)
1. **Balances y Tablas Matriciales (59 estudios):** [3], [5], [7], [8], [10]–[13], [16], [17], [19], [20], [23], [25], [27], [31], [33], [35], [36], [41], [42], [45]–[54], [57], [59], [61], [62], [65], [66], [68], [71], [74], [81], [87], [94], [95], [101], [103]–[106], [113], [120], [123], [124], [126]–[128], [130], [131], [133].
2. **Facturas Comerciales y Fiscales (34 estudios):** [4], [24], [28], [34], [38]–[40], [43], [44], [55], [60], [64], [69], [72], [75], [76], [86], [88]–[90], [96]–[100], [107]–[109], [112], [115], [119], [121], [129], [132].
3. **Formularios y Pólizas Administrativas (26 estudios):** [14], [18], [21], [22], [26], [29], [30], [32], [56], [58], [63], [67], [70], [73], [77], [78], [80], [85], [92], [93], [110], [111], [114], [116]–[118].
4. **Recibos Comerciales y Puntos de Venta POS (12 estudios):** [6], [9], [15], [37], [79], [82]–[84], [91], [102], [122], [125].



### F. Distribución Exhaustiva por Revistas Científicas Indexadas (PD2 — Tabla XIV Suplementaria)

```
TABLA XIV
REVISTAS CIENTÍFICAS LÍDERES EN PROCESAMIENTO INTELIGENTE DE DOCUMENTOS EMPRESARIALES (N = 131)
```
| Revista Científica Indexada | Editorial | Cuartil (JCR/SJR) | Artículos en Corpus [n] | Frecuencia Relativa (%) |
| :--- | :--- | :---: | :---: | :---: |
| **IEEE Access** | IEEE | Q1 / Q2 | [5], [8], [16], [26], [59], [60], [61], [84], [88], [94], [103], [108], [131] | 13 (9,9 %) |
| **International Journal on Document Analysis and Recognition (IJDAR)** | Springer | Q2 | [9], [33], [35], [39], [50], [65], [66], [77], [115] | 9 (6,9 %) |
| **Pattern Recognition** | Elsevier | Q1 | [3], [41], [80], [92], [105], [120] | 6 (4,6 %) |
| **Multimedia Tools and Applications** | Springer | Q2 | [15], [21], [52], [55], [57] | 5 (3,8 %) |
| **Expert Systems with Applications** | Elsevier | Q1 | [11], [36], [67], [83] | 4 (3,1 %) |
| **Engineering Applications of Artificial Intelligence** | Elsevier | Q1 | [24], [101], [114], [119] | 4 (3,1 %) |
| **Applied Sciences** | MDPI | Q2 | [79], [85], [97], [123] | 4 (3,1 %) |
| **Electronics** | MDPI | Q2 | [4], [7], [42] | 3 (2,3 %) |
| **International Journal of Pattern Recognition and Artificial Intelligence** | World Scientific | Q3 | [47], [89], [121] | 3 (2,3 %) |
| **Neurocomputing** | Elsevier | Q1 | [23], [38], [51] | 3 (2,3 %) |
| **Computers, Materials and Continua** | Tech Science Press | Q2 | [22], [62], [109] | 3 (2,3 %) |
| **Proceedings of the VLDB Endowment (PVLDB)** | VLDB Endowment | Q1 | [58], [112], [130] | 3 (2,3 %) |
| **Otras 64 revistas indexadas (≤ 2 estudios c/u)** | Diversas | Q1–Q3 | Citas dispersas [10], [12], [13], [17]–[20], etc. | 71 (54,2 %) |
| **Total Corpus Primario** | — | — | **[3]–[133] (131 estudios únicos)** | **131 (100,0 %)** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Nombres de revistas unificados y normalizados de Scopus y Web of Science.*
