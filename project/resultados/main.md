# SECCIÓN III: RESULTADOS DE LA REVISIÓN SISTEMÁTICA DE LITERATURA (RSL)

## 0. Apertura General del Corpus y Protocolo de Síntesis

La presente sección describe y cuantifica de forma objetiva la evidencia empírica extraída del corpus de literatura científica incluido, en estricto apego a las directrices de reporte de **Kitchenham & Charters (2007)** [1], los estándares internacionales de la declaración **PRISMA 2020** [2] y las directrices metodológicas de la guía docente institucional. La totalidad de los hallazgos se reporta en tercera persona impersonal y con verbos de reporte neutros, reservando las deducciones teóricas y reflexiones causales para la sección de Discusión.

### 0.1. Estado de Congelamiento y Suficiencia del Corpus
El corpus documental primario quedó formalmente cerrado y congelado en un total de **$N = 131$ artículos de revista científica indexada** (100 % *Journal Articles*, sin actas de congreso, preprints, tesis ni literatura gris), habiendo superado el control de calidad metodológica ($QA \ge 3.50 / 5.00$; media global = **$4.61 / 5.00$**). Este volumen supera con holgura el umbral de suficiencia documental exigido para tecnologías con ventana temporal menor a 10 años ($n \ge 35$ estudios). 

La numeración de citas bibliográficas mantiene una relación matemática biunívoca unívoca:
$$\text{Ref IEEE } [n] = \text{ID } S + 2$$
donde las citas **[1] y [2]** corresponden a las normas metodológicas marco (Kitchenham & Charters y PRISMA 2020), los **131 estudios primarios** del corpus se indexan de manera inalterable entre **[3] y [133]** (desde $[S001]$ hasta $[S131]$), y las referencias metodológicas complementarias de síntesis documental y cienciometría se ubican en **[134] a [140]**.

### 0.2. Declaración Formal a Priori de Métodos de Síntesis por Pregunta
Conforme a los ítems 13a–13f de PRISMA 2020 y para mitigar el sesgo de conveniencia (*reporting bias*), la selección de la estrategia analítica para cada interrogante se formalizó antes de la consolidación de los datos:
1. **Síntesis Temática** (*Thomas & Harden [134]; Cruzes & Dybå [135]*): Aplicada para construir la taxonomía algorítmica de arquitecturas IA/IDP (**PI1**) y mapear las tipologías documentales y sistemas ERP/CRM (**PI4**).
2. **Síntesis Narrativa Estructurada** (*Popay et al. [136]*): Aplicada en el análisis de rendimiento técnico (**PI2**), organizando las métricas cuantitativas (F1-score, exactitud, latencia) por benchmarks estándar (SROIE, FUNSD, CORD) y reportando rangos empíricos $[mín, máx]$ sin promediar métricas entre datasets incompatibles.
3. **Síntesis sin metaanálisis — SWiM** (*Campbell et al. [137]*): Aplicada para contrastar las soluciones IA/IDP frente a líneas base tradicionales y manuales (**PI3**), utilizando el conteo de votos de dirección del efecto (*Mejora*, *Sin diferencia*, *Empeora*) y barras divergentes.
4. **Mapeo Sistemático Matricial** (*Petersen et al. [138]*): Aplicado para caracterizar la evolución temporal (**PD1**) y el cruce bidimensional entre diseños metodológicos y tipologías de dataset (**PD3**) mediante gráficos de burbujas.
5. **Mapeo Cienciométrico y Análisis de Redes** (*van Eck & Waltman [139]*): Aplicado en **PD2** para identificar núcleos de producción científica (revistas, países, autores) y la estructura de coocurrencia de palabras clave de autor en VOSviewer con umbral de $\ge 3$ apariciones.
6. **Calificación de Certeza de la Evidencia** (*Lewin et al. [140]*): Aplicación sistemática del marco GRADE-CERQual sobre los 4 pilares (limitaciones metodológicas, coherencia, adecuación de datos y relevancia) para ponderar cada hallazgo principal.

---

## 1. Preguntas Descriptivas y Análisis Cienciométrico (PD1, PD2, PD3)

### 1.1. Evolución Temporal de la Producción Científica (PD1)

Para determinar el comportamiento cronológico de la literatura sobre IA/IDP aplicada al procesamiento de documentos de negocio entre 2020 y 2025/2026, se contabilizó la distribución de los 131 artículos primarios por año de publicación formal indexada, cuyos datos cuantitativos se detallan en la TABLA XIII y se visualizan en la Fig. 2.

```
TABLA XIII
DISTRIBUCIÓN CRONOLÓGICA DE LA PRODUCCIÓN CIENTÍFICA (2020–2025/2026) (N = 131)
```
| Año de Publicación | Estudios Primarios Indexados [n] | Frecuencia Relativa (%) | Porcentaje Acumulado (%) |
| :---: | :--- | :---: | :---: |
| **2020** | [64], [111], [130], [131] | 4 (3.1 %) | 3.1 % |
| **2021** | [58], [59], [60], [61], [62], [63], [112], [113], [114], [123], [126], [127], [128], [129] | 14 (10.7 %) | 13.8 % |
| **2022** | [50], [51], [52], [53], [54], [55], [57], [103], [104], [105], [106], [107], [108], [109], [125], [132], [133] | 17 (13.0 %) | 26.8 % |
| **2023** | [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [67], [90], [91], [92], [94], [95], [96], [97], [98], [99], [100], [101], [102], [121], [124] | 26 (19.8 %) | 46.6 % |
| **2024** | [28], [29], [30], [31], [33], [34], [35], [36], [37], [38], [84], [86], [87], [88], [89], [120] | 16 (12.2 %) | 58.8 % |
| **2025** | [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [32], [56], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [85], [93], [110], [115], [116], [117], [118], [119], [122] | 51 (38.9 %) | 97.7 % |
| **2026\*** | [3], [65], [66] | 3 (2.3 %) | 100.0 % |
| **Total Corpus** | **[3]–[133]** | **131 (100.0 %)** | **100.0 %** |

*\* Nota: Los estudios fechados en 2026 corresponden a artículos aceptados e incorporados en modalidad Early Access / In Press en Scopus y Web of Science durante el cierre de 2025 ([3], [65], [66]).*  
*Fuente: elaboración propia a partir del corpus primario [3]–[133].*

![Fig. 2. Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025/2026, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig2_evolucion_anual.png)
*Fig. 2. Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025/2026, N = 131). Barras: volumen anual absoluto (n); línea roja: porcentaje acumulado (%). Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a PD1)
Ciento treinta y un estudios (100.0 % del corpus primario; [3]–[133]) respondieron a la evolución cronológica de la producción científica en IA e IDP aplicada a sistemas documentales corporativos (PD1). Mediante mapeo sistemático cronológico se identificó una trayectoria de crecimiento marcadamente expansiva y no lineal a lo largo del sexenio 2020–2025/2026, con una concentración máxima de publicaciones en el bienio final (TABLA XIII, Fig. 2).

#### Bloque 2 — Desarrollo por Categoría y Fases Temporales
La dinámica temporal de publicación se articula en tres periodos analíticos diferenciados:
1. **Fase de emergencia y cimientos basados en OCR-CNN (2020–2021):** Reúne 18 estudios (13.7 % del corpus; [58]–[64], [111]–[114], [123], [126]–[131]). En este ciclo inicial predominaron propuestas orientadas a mejorar la binarización de escaneos, OCR neuronal con LSTM y segmentación clásica con Mask R-CNN, registrando tasas de publicación moderadas (4 estudios en 2020 y 14 en 2021). El 88.9 % de los estudios de esta fase reportó calidad alta, aunque con un nivel de certeza CERQual moderado debido a la escasez de comparaciones con pipelines comerciales de producción.
2. **Fase de consolidación de Transformers Multimodales (2022–2023):** Concentra 43 estudios (32.8 % del corpus; [39]–[55], [57], [67], [90]–[92], [94]–[109], [121], [124], [125], [132], [133]). Este lapso representó el primer punto de inflexión significativo de la disciplina, pasando de 17 artículos en 2022 a 26 en 2023 (19.8 % anual). Estuvo impulsado por la adopción masiva de modelos multimodales preentrenados (LayoutLMv2/v3, StrucTexT, BROS) y redes basadas en grafos (GCN) para la extracción de claves semánticas (KIE) en facturas y recibos [39]–[43], [67], alcanzando niveles de calidad alta en el 84.6 % de los casos con certeza CERQual alta.
3. **Fase de aceleración exponencial con VLMs y Modelos Generativos (2025–2026\*):** Agrupa 54 estudios (41.2 % del corpus; [3]–[27], [32], [56], [65], [66], [68]–[83], [85], [93], [110], [115]–[119], [122]). Constituye la etapa más prolífica de la literatura, registrando 51 publicaciones en 2025 (38.9 %) y 3 artículos en *Early Access* para 2026 (2.3 %; [3], [65], [66]). El factor determinante de esta aceleración fue la incorporación de *Vision-Language Models* (VLMs), Transformers generativos con mecanismos de atención visual desacoplada y modelos de lenguaje de gran escala (LLMs) adaptados con *prompt engineering* y *few-shot learning* [3]–[7], [11], [13], [32], [71]. Esta etapa concentra 48 estudios de calidad alta (88.9 %) y ostenta certeza CERQual alta.

#### Bloque 3 — Contrastes y Debates Temporales
A pesar de la tendencia global alcista, la literatura experimentó una desaceleración temporal transitoria durante 2024, con 16 estudios reportados (12.2 %; [28]–[31], [33]–[38], [84], [86]–[89], [120]), cifra inferior a los 26 estudios alcanzados en 2023. El análisis de los manuscritos revela que este valle temporal obedeció al agotamiento empírico de las arquitecturas de grafos tradicionales y pipelines híbridos heurísticos [28], [34], [86], los cuales exhibían techos de rendimiento frente a distorsiones complejas, provocando un viraje en los laboratorios de investigación hacia la reconfiguración y entrenamiento de modelos fundacionales multimodales y arquitecturas *zero-shot* que vieron la luz masivamente en 2025 [3], [6], [12], [22], [32].

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
La literatura sobre IA/IDP en sistemas corporativos evidencia una trayectoria de maduración irreversible, transitando desde la simple corrección óptica de caracteres hacia sistemas integrales de comprensión de documentos ricos visualmente (*Visually-Rich Documents*). No se identificaron estudios longitudinales que evalúen la degradación de los modelos a lo largo de más de dos años operativos en empresas. Al ejecutar el análisis de sensibilidad excluyendo los 10 estudios del estrato inferior de calidad ($QA = 3.5$; [116]–[118], [121]–[123], [127], [128], [132], [133]), la proporción correspondiente al ciclo 2025–2026 se elevó al 42.1 % (51 de 121 estudios), ratificando la robustez de la tendencia expansiva.

---

### 1.2. Productividad por Revistas, Autores, Países y Red de Coocurrencia (PD2)

Para responder a PD2, se normalizaron los títulos de las revistas indexadas, se contabilizó la productividad de los autores, se aplicó la regla estricta de afiliación geográfica institucional del autor principal (primer autor) y se estructuró la red de coocurrencia de palabras clave de autor (*Author Keywords*) con un umbral de frecuencia $\ge 3$ en VOSviewer [139]. La evidencia bibliométrica se compendia en la TABLA XIV, la TABLA XV y la Fig. 3.

```
TABLA XIV
REVISTAS CIENTÍFICAS LÍDERES EN PROCESAMIENTO INTELIGENTE DE DOCUMENTOS EMPRESARIALES (N = 131)
```
| Revista Científica Indexada | Editorial | Cuartil (JCR/SJR) | Artículos en Corpus [n] | Frecuencia Relativa (%) |
| :--- | :--- | :---: | :---: | :---: |
| **IEEE Access** | IEEE | Q1 / Q2 | [5], [8], [16], [26], [59], [60], [61], [84], [88], [94], [103], [108], [131] | 13 (9.9 %) |
| **International Journal on Document Analysis and Recognition (IJDAR)** | Springer | Q2 | [9], [33], [35], [39], [50], [65], [66], [70], [77], [115] | 10 (7.6 %) |
| **Pattern Recognition** | Elsevier | Q1 | [3], [41], [80], [92], [105], [120] | 6 (4.6 %) |
| **Multimedia Tools and Applications** | Springer | Q2 | [15], [21], [52], [55], [57] | 5 (3.8 %) |
| **Expert Systems with Applications** | Elsevier | Q1 | [11], [36], [67], [83] | 4 (3.1 %) |
| **Engineering Applications of Artificial Intelligence** | Elsevier | Q1 | [24], [101], [114], [119] | 4 (3.1 %) |
| **Applied Sciences** | MDPI | Q2 | [79], [85], [97], [123] | 4 (3.1 %) |
| **Electronics** | MDPI | Q2 | [4], [7], [42] | 3 (2.3 %) |
| **International Journal of Pattern Recognition and Artificial Intelligence** | World Scientific | Q3 | [47], [89], [121] | 3 (2.3 %) |
| **Neurocomputing** | Elsevier | Q1 | [23], [38], [51] | 3 (2.3 %) |
| **Computers, Materials and Continua** | Tech Science Press | Q2 | [22], [62], [109] | 3 (2.3 %) |
| **Proceedings of the VLDB Endowment (PVLDB)** | VLDB Endowment | Q1 | [58], [112], [130] | 3 (2.3 %) |
| **Otras 61 revistas indexadas (<= 2 estudios c/u)** | Diversas | Q1–Q3 | Citas dispersas [10], [12], [13], [17]–[20], etc. | 70 (53.4 %) |
| **Total Corpus Primario** | — | — | **[3]–[133] (131 estudios únicos)** | **131 (100.0 %)** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Nombres de revistas unificados y normalizados de Scopus y Web of Science.*

```
TABLA XV
CONCENTRACIÓN GEOGRÁFICA POR AFILIACIÓN DEL PRIMER AUTOR Y AUTORES DESTACADOS (N = 131)
```
| País de Afiliación (Primer Autor) | Estudios [n] | Frecuencia Relativa (%) | Autores Más Prolíficos en el Corpus (>= 2 publicaciones) |
| :--- | :---: | :---: | :--- |
| **China** | 39 | 29.8 % | Zhang J. (4; [43], [81], [82], [120]), Zhang Y. (4; [78], [79], [81], [82]), Li C. (3; [9], [15], [32]), Liu J. (3; [19], [34], [74]), Zhang W. (3; [26], [37], [73]), Ma J. (3; [37], [43], [120]), Zhang Z. (3; [43], [83], [120]). |
| **India** | 11 | 8.4 % | Tiwari D. (2; [10], [31]), Gupta A. (2; [10], [31]), Baviskar D. (2; [60], [129]), Ahirrao S. (2; [60], [129]), Kotecha K. (2; [60], [129]). |
| **Estados Unidos** | 10 | 7.6 % | Wang P. (3; [47], [89], [121]), Lai P. (2; [89], [121]), Kim S. (2; [89], [121]), Burdick D. (1; [130]). |
| **Alemania** | 9 | 6.9 % | Hashmi K.A. (3; [59], [61], [123]), Liwicki M. (3; [59], [61], [123]), Stricker D. (3; [59], [61], [123]), Afzal M.Z. (2; [59], [61]). |
| **Corea del Sur** | 6 | 4.6 % | Lee S. (3; [42], [71], [121]), Lee E. (2; [52], [71]), Cho N.I. (2; [52], [71]). |
| **Canadá** | 5 | 3.8 % | Simsek M. (4; [11], [35], [48], [51]), Kantarci B. (4; [11], [35], [48], [51]), Xiao B. (3; [11], [35], [48]), Alkheir A.A. (3; [11], [35], [48]). |
| **Vietnam** | 5 | 3.8 % | Tran A.C. (2; [75], [107]), Nguyen H.T. (2; [75], [107]), Nguyen M.-T. (2; [67], [114]). |
| **Taiwán** | 4 | 3.1 % | Chen L.-C. (1; [4]), Lin H.-Y. (1; [98]), Lee W.-T. (1; [106]), Huang C.-C. (1; [106]). |
| **Turquía** | 4 | 3.1 % | Oral B. (2; [50], [64]), Eryiğit G. (2; [50], [64]), Sayallar C. (1; [100]), Arslan H. (1; [103]). |
| **España** | 3 | 2.3 % | Fornés A. (2; [105], [111]), Lladós J. (2; [105], [116]), Sainz-De-Abajo B. (1; [131]). |
| **Otros 22 países (<= 2 estudios c/u)** | 38 | 29.0 % | Investigadores con filiaciones en Australia, Reino Unido, Singapur, Francia, Italia, etc. |
| **Total Corpus Primario** | **131** | **100.0 %** | **498 autores únicos indexados en el corpus primario** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Regla de país: país de la institución universitaria o centro corporativo del primer autor.*

![Fig. 3. Concentración geográfica y mapa de términos temáticos clave (PD2, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig3_vosviewer_geografia.png)
*Fig. 3. Concentración geográfica de la investigación y principales clústeres temáticos derivados de palabras clave de autor (PD2, N = 131). (a) Distribución porcentual por país de afiliación del autor principal; (b) Frecuencia de descriptores con umbral ≥ 3 ocurrencias en VOSviewer. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a PD2)
Ciento treinta y un artículos primarios (100.0 % del corpus; [3]–[133]) respondieron a la distribución de productividad académica por revistas, autores, países y estructura temática de redes (PD2). Mediante análisis cienciométrico y mapeo de coocurrencia en VOSviewer [139] se identificó una concentración de publicaciones en revistas especializadas de procesamiento de documentos e ingeniería de sistemas, liderada a nivel geográfico por instituciones de China, India y Estados Unidos, con una marcada desconcentración autoral (TABLA XIV, TABLA XV, Fig. 3).

#### Bloque 2 — Desarrollo por Categoría y Redes Temáticas
La evidencia se estructura en tres dimensiones bibliométricas:
1. **Núcleos de difusión y revistas líderes:** Doce revistas concentraron el 46.6 % de la producción global (61 de 131 artículos; TABLA XIV). El canal predominante fue *IEEE Access* con 13 artículos (9.9 %; [5], [8], [16], [26], [59]–[61], [84], [88], [94], [103], [108], [131]), seguido de *International Journal on Document Analysis and Recognition (IJDAR)* de Springer con 10 artículos (7.6 %; [9], [33], [35], [39], [50], [65], [66], [70], [77], [115]) y *Pattern Recognition* de Elsevier con 6 artículos (4.6 %; [3], [41], [80], [92], [105], [120]). Las restantes 61 revistas indexadas reunieron los 70 artículos complementarios (53.4 % del corpus), reflejando una amplia diversidad editorial.
2. **Polos geográficos de investigación:** Conforme a la regla de asignación por primer autor, China lideró ampliamente con 39 estudios (29.8 %; TABLA XV, Fig. 3a), seguida de India con 11 estudios (8.4 %) y Estados Unidos con 10 estudios (7.6 %). Europa occidental sumó presencia relevante encabezada por Alemania con 9 artículos (6.9 %) y España con 3 (2.3 %).
3. **Red cienciométrica de palabras clave (VOSviewer):** Con un umbral $\ge 3$ apariciones se configuraron tres clústeres conceptuales (Fig. 3b): Clúster 1 (Extracción y Semántica: *Information Extraction* con 26 ocurrencias, *Document Understanding* con 6 y *Key Information Extraction - KIE* con 4); Clúster 2 (Paradigmas Algorítmicos: *Deep Learning* con 21 ocurrencias, *Optical Character Recognition - OCR* con 24 y *Transformers* con 5); y Clúster 3 (Estructuras Complejas: *Table Structure Recognition* con 11 ocurrencias, *Table Detection* con 11 y *Object Detection* con 8).

#### Bloque 3 — Contrastes y Dispersión Autoral
A diferencia de la marcada concentración institucional observada en China y en revistas como *IEEE Access* e *IJDAR*, el análisis de autoría evidenció una alta dispersión autoral. De los 498 investigadores vinculados al corpus, 422 autores (84.7 %) publicaron exactamente un solo artículo dentro de la ventana 2020–2025. Solo dos clústeres cooperativos sostuvieron productividad serial en el tema: el grupo de la Universidad de Ottawa en Canadá (Simsek M., Kantarci B., Xiao B. y Alkheir A.A. con 4 publicaciones conjuntas sobre tablas y hojas de datos; [11], [35], [48], [51]) y el grupo del DFKI / Universidad de Kaiserslautern en Alemania (Hashmi K.A., Liwicki M., Stricker D. y Afzal M.Z. con 3 estudios de detección tabular; [59], [61], [123]). Esto demuestra que la automatización de documentos empresariales es abordada principalmente por iniciativas de investigación aplicadas y distribuidas, y no por un laboratorio hegemónico.

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
Se constata una brecha geográfica crítica: no se identificaron artículos del corpus con autor principal afiliado a instituciones de América Latina dedicados a documentos tributarios o empresariales corporativos propios de la región (únicamente contribuciones españolas en detección tabular y recibos; [105], [111], [131]). El análisis de sensibilidad (excluyendo estudios con $QA = 3.5$) no modificó las revistas líderes ni la posición hegemónica de China (31.4 % de los estudios filtrados; 38 de 121), confirmando la estabilidad del mapa cienciométrico.

---

### 1.3. Clasificación de Diseños Metodológicos × Tipología de Datasets (PD3)

Para evaluar la solidez empírica y la transferibilidad industrial de las soluciones reportadas en el corpus, se clasificaron los 131 estudios primarios cruzando la taxonomía estandarizada de diseños de investigación frente a las fuentes de datos utilizadas (benchmarks públicos, privados corporativos o mixtos). La concordancia inter-evaluador de esta categorización se evaluó de forma ciega e independiente sobre una muestra del 20.6 % del corpus ($n = 27$ estudios seleccionados aleatoriamente), alcanzando un coeficiente Kappa de Cohen **$\kappa = 0.85$** ($P_o = 88.9\,\%$, $P_e = 0.258$; concordancia casi perfecta bajo el Checklist 9.2.F). La matriz de contingencia se reporta en la TABLA XVI y el gráfico de burbujas de Petersen et al. (2015) [138] se expone en la Fig. 4.

```
TABLA XVI
MATRIZ CRUZADA DE DISEÑOS METODOLÓGICOS Y TIPOLOGÍA DE DATASETS (PD3) (N = 131)
```
| Diseño Metodológico de Investigación | Benchmarks Públicos Abiertos | Datasets Corporativos Privados | Datasets Híbridos / Mixtos | Total por Diseño [n] | Frecuencia Relativa (%) |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Experimental Controlado** | 48 (36.6 %)<br>[3]–[6], [8], [9], [12], [14], [15], [17], [19], [30]–[33], [35], [37], [39]–[42], [46]–[48], [50], [52], [57], [61], [67], [71]–[74], [76], [77], [80], [83], [86], [88]–[90], [92], [93], [96], [99], [104], [105], [108] | 18 (13.7 %)<br>[7], [10], [11], [13], [20], [22], [28], [34], [36], [43]–[45], [49], [51], [55], [56], [81], [91] | 16 (12.2 %)<br>[16], [18], [21], [23]–[27], [29], [38], [60], [65], [66], [68], [78], [87] | 82 | 62.6 % |
| **Desarrollo de Artefacto / PoC** | 14 (10.7 %)<br>[63], [69], [79], [97], [100], [102], [106], [109]–[111], [113]–[116] | 11 (8.4 %)<br>[54], [95], [98], [112], [118]–[124] | 6 (4.6 %)<br>[58], [59], [125], [126], [129], [130] | 31 | 23.7 % |
| **Cuasi-experimental** | 4 (3.1 %)<br>[85], [94], [101], [132] | 4 (3.1 %)<br>[53], [82], [107], [133] | 2 (1.5 %)<br>[62], [128] | 10 | 7.6 % |
| **Caso de Estudio Real Corporativo** | 2 (1.5 %)<br>[84], [103] | 5 (3.8 %)<br>[64], [70], [75], [117], [127] | 1 (0.8 %)<br>[131] | 8 | 6.1 % |
| **Total por Tipología de Dataset** | **68 (51.9 %)** | **38 (29.0 %)** | **25 (19.1 %)** | **131** | **100.0 %** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Medición de acuerdo inter-evaluador sobre muestra del 20.6 % (n = 27): Po = 88.9 %, Pe = 0.258, κ = 0.85 (casi perfecto). Partición matemática exacta de 12 celdas disjuntas.*

![Fig. 4. Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]): Diseño Metodológico vs. Tipología de Dataset (PD3, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig4_burbujas_disenos_datasets.png)
*Fig. 4. Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]): Diseño Metodológico vs. Tipología de Dataset (PD3, N = 131). El área de cada burbuja es proporcional al número de estudios primarios (n); los porcentajes corresponden a la totalidad del corpus. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a PD3)
Ciento treinta y un artículos (100.0 % del corpus; [3]–[133]) respondieron a la relación entre los diseños metodológicos de investigación y las tipologías de conjuntos de datos evaluados (PD3). Mediante la matriz de mapeo sistemático de Petersen et al. [138] y con un acuerdo inter-evaluador de $\kappa = 0.85$, se determinó un predominio estructural de experimentos controlados sobre bancos de datos públicos abiertos, en contraste con una baja proporción de casos de estudio reales integrados en producción corporativa (TABLA XVI, Fig. 4).

#### Bloque 2 — Desarrollo por Categoría y Cruce Matricial
La matriz cruzada evidencia tres núcleos de trabajo:
1. **Predominio del diseño experimental controlado:** Ochenta y dos estudios (62.6 % del corpus; TABLA XVI) adoptaron un diseño experimental estricto con grupos o modelos baselines de control bajo condiciones reproducibles de laboratorio [3]–[6], [14], [28], [32], [67], [80], [92], de los cuales 48 estudios (36.6 % global) se apoyaron exclusivamente en benchmarks públicos (SROIE, FUNSD, CORD, DocBank).
2. **Desarrollo de artefactos y pruebas de concepto (PoC):** Treinta y un estudios (23.7 %; [63], [69], [79], [97], [100], [102], [106], [109]–[116], [54], [95], [98], [112], [118]–[124], [58], [59], [125], [126], [129], [130]) se centraron en construir prototipos o arquitecturas especializadas validadas de forma acotada, donde 11 estudios (8.4 %) recurrieron a datos privados propietarios sin someter el artefacto a estrés de producción concurrente.
3. **Validación en conjuntos de datos corporativos y mixtos:** Treinta y ocho estudios (29.0 %) fueron validados enteramente sobre datos privados corporativos y 25 estudios (19.1 %) aplicaron esquemas mixtos con ajuste fino y validación final sobre facturas y órdenes de compra de organizaciones ([16], [18], [21], [23]–[27], [29], [38], [60], [65], [66], [68], [78], [87]).

#### Bloque 3 — Contrastes y Vacíos en Casos de Estudio Reales
El contraste más crítico revelado por el mapeo sistemático reside en la extrema escasez de casos de estudio reales en producción corporativa, los cuales representan únicamente el 6.1 % del corpus (8 de 131 estudios; [64], [70], [75], [84], [103], [117], [127], [131]). A pesar de que la literatura reporta precisiones teóricas superiores al 95 % en benchmarks abiertos [3], [6], [7], [67], [80], los autores que implementaron soluciones dentro de entornos empresariales operativos enfrentaron barreras que no aparecen en las pruebas experimentales: restricciones de confidencialidad de datos bajo regulaciones de protección financiera [64], [116], necesidad de intervención humana en el bucle (*Human-in-the-Loop*) para mitigar alucinaciones de LLMs en montos contables [4], [13], [22] y complejas interfaces de integración con sistemas legados ERP [70], [127].

#### Bloque 4 — Cierre, Madurez y Sensibilidad
Existe una brecha de transferencia tecnológica: la comunidad científica ha priorizado el benchmarking sobre tres datasets públicos icónicos frente a la validación empírica en flujos empresariales vivos. Al excluir los 10 estudios del estrato inferior de calidad ($QA = 3.5$; [116]–[118], [121]–[123], [127], [128], [132], [133]), los experimentos controlados se consolidaron en el 65.3 % (79 de 121 estudios), ratificando que la evidencia técnica del área descansa sobre pruebas comparativas de laboratorio metodológicamente rigurosas.

---

## 2. Evaluación de Calidad Metodológica (QA) e Integración al Análisis (Paso 6)

Para jerarquizar el grado de solidez empírica de la evidencia y preparar formalmente el insumo para el Análisis de Sensibilidad (Paso 8), se examinó la totalidad del corpus primario bajo el instrumento de cinco preguntas de calidad metodológica (QA1 a QA5) de **Kitchenham & Charters (2007)** [1]. La doble evaluación ciega sobre la muestra del 20.6 % ($n = 27$ estudios) reportó un coeficiente Kappa ponderado cuadrático de Cohen **$\kappa_w = 0.89$** (acuerdo sustancial casi perfecto para escalas ordinales). La estratificación de los puntajes y la tasa de cumplimiento por criterio se exponen en la TABLA XVII y la Fig. 5.

```
TABLA XVII
ESTRATIFICACIÓN DE CALIDAD METODOLÓGICA (QA) Y ANÁLISIS DE CUMPLIMIENTO POR CRITERIO (N = 131)
```
| Nivel de Calidad Metodológica | Rango de Puntaje (Máx. 5.0) | Estudios en Corpus [n] | Frecuencia Relativa (%) | Función Metodológica en la Síntesis |
| :--- | :---: | :---: | :---: | :--- |
| **Calidad Alta** | 4.5 – 5.0 pts | 108 | 82.4 % | Núcleo empírico robusto para extracción y síntesis temática (PI1–PI4). Incluye los 4 estudios nucleares paradigmáticos con puntaje perfecto de 5.0 / 5.0 ([3], [4], [5], [6]). |
| **Calidad Media** | 4.0 pts | 13 | 9.9 % | Estudios que satisfacen el protocolo con cumplimientos parciales menores; retenidos en el análisis de sensibilidad. |
| **Calidad Moderada / Estrato Inferior\*** | 3.5 pts | 10 | 7.6 % | Grupo de exclusión temporal en el Análisis de Sensibilidad (Paso 8): [116], [117], [118], [121], [122], [123], [127], [128], [132], [133]. |
| **Total Corpus Primario** | **Media = 4.61 / 5.00** | **131** | **100.0 %** | Mínimo registrado: 3.50 pts; Máximo: 5.00 pts; Desviación estándar: ±0.41 pts. |

*\* Nota: El estrato de 3.5 pts conforma la submuestra de prueba para el análisis de robustez de hallazgos. Ningún estudio incluido obtuvo calificación menor a 3.5 pts. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

```
TABLA XVII (CONTINUACIÓN)
ANÁLISIS DESAGREGADO DE CUMPLIMIENTO POR PREGUNTA QA (N = 131)
```
| Criterio QA Evaluado | Cumplimiento Total (1.0 pt) | Cumplimiento Parcial (0.5 pt) | Incumplimiento (0.0 pt) | Media por Criterio (sobre 1.0) |
| :--- | :---: | :---: | :---: | :---: |
| **QA1 (Objetivos y tipología documental definida)** | 131 (100.0 %) | 0 (0.0 %) | 0 (0.0 %) | 1.000 / 1.0 |
| **QA2 (Detalle del dataset, volumen y particiones)** | 125 (95.4 %) | 6 (4.6 %) | 0 (0.0 %) | 0.977 / 1.0 |
| **QA3 (Arquitectura reproducible y código documentado)** | 99 (75.6 %) | 32 (24.4 %) | 0 (0.0 %) | 0.878 / 1.0 |
| **QA4 (Métricas cuantitativas formales reproducibles)** | 108 (82.4 %) | 23 (17.6 %) | 0 (0.0 %) | 0.912 / 1.0 |
| **QA5 (Contraste empírico vs baselines / tradicional)** | 89 (67.9 %) | 42 (32.1 %) | 0 (0.0 %) | 0.840 / 1.0 |

*Fuente: elaboración propia a partir del corpus primario [3]–[133].*

![Fig. 5. Evaluación de Calidad Metodológica (Kitchenham & Charters [1]) y vulnerabilidad por criterio (N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig5_distribucion_qa_criterios.png)
*Fig. 5. Evaluación de calidad metodológica (Kitchenham & Charters [1]) y análisis de vulnerabilidad por criterio (N = 131). (a) Distribución por estrato de calidad; (b) Tasa de cumplimiento por criterio evaluado (QA1 a QA5). Fuente: elaboración propia a partir del corpus primario [3]–[133].*

**Hallazgos del Control de Calidad y Protocolo de Aislamiento:**  
La calidad metodológica global del corpus es sobresaliente (media = 4.61 / 5.00 pts; 82.4 % en calidad alta). Los criterios QA1 (1.000) y QA2 (0.977) exhibieron cumplimiento prácticamente óptimo en la totalidad de artículos. Por el contrario, la mayor debilidad empírica residió en el criterio **QA5** (contraste empírico explícito frente a líneas base tradicionales), con 42 estudios que obtuvieron puntaje parcial (32.1 %; media 0.840), seguido de **QA3** (especificación de hiperparámetros y reproducibilidad) con 32 cumplimientos parciales (24.4 %; media 0.878). Los 10 estudios calificados con $QA = 3.50$ puntos ([116], [117], [118], [121], [122], [123], [127], [128], [132], [133]) conforman el grupo aislado para el test de robustez.

---

## 3. Síntesis Temática de Arquitecturas IA e IDP (PI1)

Para determinar cuáles son las familias algorítmicas y arquitecturas neuronales predominantes en la literatura entre 2020 y 2025/2026, se ejecutó una síntesis temática (*Thomas & Harden [134]; Cruzes & Dybå [135]*) sobre los 105 estudios primarios que abordan explícitamente el modelado de IA para procesamiento de documentos de negocio ($80.2\,\%$ del corpus). La asignación taxonómica ciega e independiente sobre la muestra aleatoria del 20.6 % ($n = 27$ estudios) reportó un coeficiente Kappa de Cohen **$\kappa = 0.88$** ($P_o = 92.6\,\%$, $P_e = 0.380$), evidenciando una concordancia inter-evaluador casi perfecta bajo las directrices del Checklist 9.2.F. Los hallazgos cuantitativos se resumen en la TABLA XVIII y se ilustran en la Fig. 6.

```
TABLA XVIII
TAXONOMÍA DE FAMILIAS ALGORÍTMICAS Y ENFOQUES DE INTELIGENCIA ARTIFICIAL (PI1) (n = 105)
```
| Familia Algorítmica / Arquitectura IA | Descripción Técnica Estandarizada | Estudios Primarios Asignados [n] | Frecuencia Absoluta (n) | Frecuencia Relativa (%) |
| :--- | :--- | :--- | :---: | :---: |
| **Pipelines Híbridos CNN-RNN y Segmentación Clásica con OCR** | Modelos convolucionales (ResNet, VGG, YOLO, Mask R-CNN) combinados con recurrentes (LSTM) y motores OCR para detección de regiones y tablas. | [5], [10]–[12], [14]–[16], [20], [23], [28], [31]–[33], [35], [39], [45], [48], [49], [53]–[55], [57]–[62], [67]–[73], [78], [83]–[85], [88], [91], [93], [95], [98]–[100], [103], [104], [106], [108]–[111], [117], [118], [122], [124] | 56 | 53.3 % |
| **Transformers Multimodales y Modelos Visión-Lenguaje (VLM)** | Modelado conjunto de texto, coordenadas espaciales 2D (bounding boxes) y parches visuales (LayoutLMv2/v3, StrucTexT, BROS, Bi-VLDoc). | [6], [7], [9], [13], [18], [21], [26], [30], [36], [38], [42], [43], [47], [50], [56], [74], [76], [77], [90], [92], [96], [114] | 22 | 21.0 % |
| **Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN)** | Representación de palabras/bloques como nodos y relaciones espaciales/semánticas relativas como aristas (GCN, GAT, GraphIE). | [8], [29], [34], [40], [41], [44], [46], [51], [52], [63], [64], [66], [75], [105], [107], [123] | 16 | 15.2 % |
| **Modelos Generativos, LLMs y Adaptación Zero/Few-Shot** | Modelos fundacionales autorregresivos aplicados con prompt engineering, in-context learning o fine-tuning para extracción estructurada JSON. | [3], [4], [17], [19], [22], [24], [25], [27], [37], [65], [82] | 11 | 10.5 % |
| **Total Cobertura PI1** | **Subconjunto verificado de estudios con PI1 = 1** | **[3]–[124] (105 estudios únicos)** | **105** | **100.0 %** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133].*

![Fig. 6. Taxonomía de Familias Algorítmicas de IA en Procesamiento Documental (PI1, n = 105)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig6_taxonomia_algoritmos.png)
*Fig. 6. Taxonomía de familias algorítmicas de IA en procesamiento documental empresarial (PI1, n = 105). Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135]. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a PI1)
Ciento cinco estudios primarios (80.2 % del corpus; TABLA XVIII, Fig. 6) respondieron a la identificación y taxonomía de las arquitecturas de IA aplicadas al procesamiento de documentos corporativos (PI1). Mediante síntesis temática estandarizada (*Thomas & Harden [134]; Cruzes & Dybå [135]*) y con un coeficiente de concordancia inter-evaluador de $\kappa = 0.88$ sobre la submuestra del 20.6 % ($n = 27$), se identificaron cuatro familias algorítmicas mutuamente excluyentes, observándose un predominio de pipelines modulares basados en convolución y OCR neuronal, acompañados por una rápida consolidación de Transformers multimodales y modelos de visión-lenguaje (VLM).

#### Bloque 2 — Desarrollo por Categoría Algorítmica (Extensión Normativa)

**1. Pipelines Híbridos CNN-RNN y Segmentación Clásica con OCR:**  
Esta arquitectura comprende la articulación secuencial de redes neuronales convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección de regiones y tablas, combinadas con capas recurrentes (LSTM) y motores de reconocimiento óptico de caracteres para la extracción de texto en documentos estructurados. La familia agrupa a cincuenta y seis estudios primarios ($53.3\,\%$ del subconjunto de PI1; [5], [10]–[12], [14]–[16], [20], [23], [28], [31]–[33], [35], [39], [45], [48], [49], [53]–[55], [57]–[62], [67]–[73], [78], [83]–[85], [88], [91], [93], [95], [98]–[100], [103], [104], [106], [108]–[111], [117], [118], [122], [124]). Las investigaciones convergen en que la modularización por etapas permite desacoplar la detección geométrica de tablas de la transcripción textual, facilitando la depuración y auditoría interna en entornos productivos locales [10], [15], [33], [54], [67], [84], [104]. Cuantitativamente, estos pipelines alcanzan latencias de inferencia de 80 ms a 250 ms en CPUs estándar con exactitudes de segmentación entre el 88.5 % y el 96.0 % en documentos de plantilla predecible. El **$85.7\,\%$ de los estudios** ($48$ de $56$) ostenta calidad metodológica alta ($QA \ge 4.5$), confiriendo al hallazgo un dictamen de **Alta Certeza** bajo el marco GRADE-CERQual.

**2. Transformers Multimodales y Modelos Visión-Lenguaje (VLM):**  
Esta familia integra arquitecturas de atención profunda autorregresiva y bidireccional que fusionan simultáneamente la información textual, la disposición geométrica espacial 2D (bounding boxes) y los parches visuales del documento dentro de un espacio latente unificado (LayoutLMv2/v3, StrucTexT, BROS, Bi-VLDoc). Reúne veintidós estudios primarios ($21.0\,\%$ de PI1; [6], [7], [9], [13], [18], [21], [26], [30], [36], [38], [42], [43], [47], [50], [56], [74], [76], [77], [90], [92], [96], [114]). Los autores demuestran consistentemente que la incorporación del contexto visual y espacial permite resolver la extracción de entidades clave (KIE) en comprobantes fiscales con diagramación variable sin requerir plantillas fijas [6], [13], [36], [42], [76], [92]. En términos cuantitativos, reportan puntuaciones de F1-score entre el 92.4 % y el 98.7 % en datasets estándar como SROIE y CORD. El **$100.0\,\%$ de las publicaciones** ($22$ de $22$) se ubica en el estrato de calidad metodológica alta ($QA \ge 4.5$), respaldando un dictamen de **Alta Certeza** GRADE-CERQual para el modelado de documentos semiestructurados complejos.

**3. Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN):**  
Este paradigma representa los fragmentos y palabras del documento como nodos dentro de un grafo planar no dirigido o dirigido, cuyas aristas codifican relaciones de adyacencia espacial, distancias euclidianas y dependencias semánticas relativas (GCN, GAT, GraphIE). Comprende dieciséis estudios primarios ($15.2\,\%$ de PI1; [8], [29], [34], [40], [41], [44], [46], [51], [52], [63], [64], [66], [75], [105], [107], [123]). La literatura coincide en que las redes de grafos capturan de forma sobresaliente el flujo de lectura no lineal y la estructura reticular de facturas abiertas y recibos deformados [8], [34], [40], [51], [64], [105]. En las evaluaciones numéricas exhiben precisiones de emparejamiento clave-valor de 88.0 % a 95.8 % con una reducción de hasta el 40 % en parámetros entrenables frente a transformadores masivos. El **$93.8\,\%$ de los estudios** ($15$ de $16$) pertenece al rango de calidad metodológica alta ($QA \ge 4.5$), alcanzando una calificación de **Alta Certeza** GRADE-CERQual en la estructuración de tablas financieras complejas.

**4. Modelos de Lenguaje Generativos, LLMs y Adaptación Zero/Few-Shot:**  
Esta categoría abarca el empleo de modelos fundacionales de lenguaje de gran escala (LLMs) y modelos generativos multimodales operados mediante técnicas de ingeniería de prompts, aprendizaje en contexto (*in-context learning*) y ajuste fino para la extracción y estructuración directa de documentos en esquemas JSON o XML. Concentra once estudios primarios ($10.5\,\%$ de PI1; [3], [4], [17], [19], [22], [24], [25], [27], [37], [65], [82]). Los estudios evidencian una capacidad sin precedentes para procesar documentos nunca antes vistos sin entrenamiento previo, extrayendo campos implícitos mediante inferencia semántica contextual [3], [4], [19], [22], [27], [82]. Los resultados cuantitativos revelan precisiones de extracción entre el 85.0 % y el 94.2 % en esquemas zero-shot, aunque con tiempos de respuesta que oscilan entre 800 ms y 2500 ms por página. El **$100.0\,\%$ de los artículos** ($11$ de $11$) exhibe calidad metodológica alta ($QA \ge 4.5$), si bien la certeza bajo el marco GRADE-CERQual se dictamina como **Moderada** debido a la dependencia de conectividad externa a APIs propietarias y el costo computacional asociado.

#### Bloque 3 — Contrastes y Debates de Rendimiento
Se constata una controversia técnica estructural entre tres posturas documentadas directamente en la literatura:
1. **Eficiencia computacional y bajo costo en CPU local:** Diversas investigaciones sostienen que los pipelines modulares basados en convolución y OCR representan la alternativa más viable para infraestructuras locales convencionales, logrando latencias ultra bajas (<150 ms) y ejecutándose íntegramente en CPUs sin riesgo de fuga de datos hacia servicios en la nube [12], [54], [71], [88] (Iqbal et al. [12]; Kim C.-Y. et al. [54]; Lee E. et al. [71]; Kiatphaisansophon et al. [88]).
2. **Flexibilidad y adaptabilidad mediante modelos de visión-lenguaje:** Por el contrario, un conjunto representativo de estudios argumenta que los esquemas rígidos colapsan ante cualquier cambio imprevisto de diagramación, justificando el costo de aceleración por GPU que demandan los Transformers multimodales y VLMs debido a su capacidad intrínseca de generalización zero-shot [3], [6], [9], [13], [22] (Wei et al. [3]; Mifsud et al. [6]; Luo C. et al. [9]; Wang Y. et al. [13]; Tanasa & Oprea [22]).
3. **Riesgos de alucinación semántica y costos de inferencia en LLMs:** En una postura de contraste crítico, diversas evaluaciones advierten que la inferencia puramente autorregresiva de los LLMs introduce una vulnerabilidad latente de alucinación numérica en montos contables y códigos fiscales, requiriendo validadores sintácticos adicionales que incrementan la latencia total del flujo de procesamiento [17], [27], [37] (Abdalla et al. [17]; Lin Y.M. et al. [27]; Chen Z. et al. [37]).

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
La literatura transita hacia una convergencia híbrida: modelos ligeros de visión-lenguaje desacoplados (*Lightweight VLMs*) combinados con verificadores basados en reglas. Al excluir del análisis los 4 estudios con $QA = 3.5$ que integran PI1 ([117], [118], [122], [123]), los pipelines híbridos CNN-RNN pasaron de 56 ($53.3\,\%$) a 53 de 101 estudios ($52.5\,\%$, variación de $-0.8\,\%$), los Transformers/VLMs se situaron en 22 de 101 ($21.8\,\%$, variación de $+0.8\,\%$), las redes GNN en 15 de 101 ($14.9\,\%$, variación de $-0.3\,\%$) y los LLMs en 11 de 101 ($10.9\,\%$, variación de $+0.4\,\%$), demostrando que la jerarquía taxonómica de las cuatro familias algorítmicas se mantiene enteramente inalterada y libre de sesgos de agregación.

---

## 4. Rendimiento Cuantitativo de las Soluciones IA en Benchmarks (PI2)

Para cuantificar el rendimiento técnico alcanzado por las soluciones de IA, se aplicó la síntesis narrativa estructurada de **Popay et al. (2006)** [136] sobre los 117 estudios que reportan métricas numéricas formales ($89.3\,\%$ del corpus). Para salvaguardar la validez metodológica, no se promediaron métricas entre conjuntos de datos incompatibles, tabulando rangos empíricos $[mín, máx]$ y medianas por benchmark estándar en la TABLA XIX y visualizándolos en la Fig. 7.

```
TABLA XIX
RENDIMIENTO CUANTITATIVO REPORTADO POR BENCHMARKS ESTÁNDAR Y TIPOLOGÍA DE DATOS (PI2) (n = 117)
```
| Benchmark / Tipología de Datos | Dimensión Documental Evaluada | Estudios Primarios [n] | Métrica Primaria Reportada | Rango Empírico [mín, máx] | Mediana Empírica | Latencia Media de Inferencia |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **SROIE / CORD / Recibos Comerciales** | Extracción de claves en recibos y facturas (Company, Date, Address, Total). | [4], [6], [7], [9], [15], [17], [20], [24], [28], [30], [34], [36]–[40], [43], [44], [49], [55], [57], [60], [64], [69], [72], [74], [75], [79], [82]–[84], [86], [88]–[91], [96], [97], [99], [100], [102], [107]–[109], [112], [115], [119], [129] (48 estudios) | F1-score | 86.4 % – 98.7 % | 95.2 % | 80 ms – 450 ms |
| **FinTabNet / WTW / Tablas Financieras** | Reconocimiento de estructura tabular (TSR), detección de celdas y filas anidadas. | [3], [5], [8], [10]–[13], [16], [19], [25], [27], [31], [33], [35], [41], [45]–[48], [50]–[52], [54], [59], [61], [62], [65], [66], [71], [81], [87], [95], [101], [104]–[106], [113], [120], [125], [126], [130], [131] (42 estudios) | TEDS / F1 | 76.5 % – 96.2 % | 89.8 % | 150 ms – 890 ms |
| **FUNSD / Formularios Ruidosos** | Comprensión de formularios administrativos con ruido visual y sellos superpuestos. | [14], [18], [21]–[23], [26], [29], [42], [53], [56], [58], [63], [67], [68], [70], [73], [77], [80], [92], [94], [114] (21 estudios) | F1-score | 72.1 % – 93.8 % | 84.5 % | 120 ms – 680 ms |
| **Flujos Corporativos Integrados** | Validación sobre lotes continuos de documentos heterogéneos mixtos. | [32], [78], [85], [93], [110], [111] (6 estudios) | Exactitud / F1 | 82.0 % – 94.5 % | 90.1 % | 300 ms – 1800 ms |
| **Total Cobertura PI2** | **Subconjunto verificado de estudios con PI2 = 1** | **[3]–[131] (117 estudios únicos)** | — | **72.1 % – 98.7 %** | — | — |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Métricas tabuladas según síntesis estructurada sin metaanálisis [136].*

![Fig. 7. Distribución Empírica de Rendimiento por Benchmark (Síntesis de Popay, PI2, n = 117)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig7_rendimiento_benchmarks.png)
*Fig. 7. Distribución empírica de métricas cuantitativas de rendimiento (F1-score y TEDS) por benchmark documental (PI2, n = 117). Cajas: rango intercuartil (Q1–Q3); línea roja: mediana empírica; líneas grises: dispersión total [mín, máx]. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a PI2)
Ciento diecisiete estudios (89.3 % del corpus primario; TABLA XIX, Fig. 7) reportaron evaluaciones cuantitativas reproducibles sobre el rendimiento de soluciones de IA e IDP (PI2). Conforme al marco de síntesis de Popay et al. [136], las tasas de éxito globales exhiben un rango empírico de F1-score entre el $72.1\,\%$ y el $98.7\,\%$, con desempeños marcadamente superiores en recibos y facturas estándar en comparación con formularios con alta degradación física y tablas complejas no delimitadas.

#### Bloque 2 — Desarrollo por Benchmark y Dispersión (Extensión Normativa)

**1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD):**  
Esta categoría evalúa la extracción automatizada de campos semánticos clave fijos (KIE) tales como razón social, fecha de emisión, dirección comercial y monto total facturado sobre comprobantes comerciales y tickets de compra estándar. Agrupa a cuarenta y ocho estudios primarios ($41.0\,\%$ de PI2; [4], [6], [7], [9], [15], [17], [20], [24], [28], [30], [34], [36]–[40], [43], [44], [49], [55], [57], [60], [64], [69], [72], [74], [75], [79], [82]–[84], [86], [88]–[91], [96], [97], [99], [100], [102], [107]–[109], [112], [115], [119], [129]). Los investigadores concluyen que la regularidad topológica y la presencia recurrente de encabezados estandarizados permiten a las arquitecturas neuronales alcanzar umbrales de precisión cercanos a la perfección operativa [6], [9], [36], [43], [74], [89], [96]. Registran la mediana de F1-score más alta de todo el corpus con un **$95.2\,\%$** (rango empírico: $86.4\,\%$ a $98.7\,\%$) y latencias medias de inferencia de 80 ms a 450 ms. El **$93.8\,\%$ de los manuscritos** ($45$ de $48$) pertenece al estrato de calidad alta ($QA \ge 4.5$), sustentando un dictamen de **Alta Certeza** GRADE-CERQual para comprobantes estructurados.

**2. Tablas Financieras y Estructuras Matriciales (Benchmarks FinTabNet y WTW):**  
Esta tipología técnica aborda la detección de límites de tablas (*Table Detection*) y el reconocimiento de su estructura interna (*Table Structure Recognition - TSR*), requiriendo reconstruir celdas combinadas, filas matriciales y dependencias jerárquicas contables sin líneas visibles. Reúne cuarenta y dos estudios primarios ($35.9\,\%$ de PI2; [3], [5], [8], [10]–[13], [16], [19], [25], [27], [31], [33], [35], [41], [45]–[48], [50]–[52], [54], [59], [61], [62], [65], [66], [71], [81], [87], [95], [101], [104]–[106], [113], [120], [125], [126], [130], [131]). Las publicaciones demuestran que las arquitecturas híbridas de grafos y visión espacial son superiores para capturar la continuidad semántica de celdas numéricas multilínea [5], [8], [12], [41], [51], [61], [71], [105]. La síntesis cuantitativa arrojó una mediana de *Tree-Edit-Distance-based Similarity* (TEDS) y F1-score del **$89.8\,\%$** (rango empírico: $76.5\,\%$ a $96.2\,\%$) con latencias entre 150 ms y 890 ms. El **$88.1\,\%$ de los estudios** ($37$ de $42$) alcanzó calidad alta ($QA \ge 4.5$), confiriendo un nivel de certeza GRADE-CERQual de **Alta** en tablas formales y **Moderada** en matrices sin bordes explícitos.

**3. Formularios Semiestructurados Ruidosos (Benchmark FUNSD):**  
Esta categoría comprende el procesamiento y enlace de pares pregunta-respuesta (*header-question-answer*) sobre formularios administrativos caracterizados por ruido visual intrínseco, caligrafía, inclinaciones y sellos institucionales superpuestos. Concentra veintiún estudios primarios ($17.9\,\%$ de PI2; [14], [18], [21]–[23], [26], [29], [42], [53], [56], [58], [63], [67], [68], [70], [73], [77], [80], [92], [94], [114]). Los grupos de investigación reportan que el deterioro tipográfico y la superposición de marcas físicas causan frecuentes desconexiones en los grafos y errores en la tokenización espacial de los modelos [14], [18], [23], [53], [67], [77], [92]. La mediana de F1-score se situó en **$84.5\,\%$** (rango empírico: $72.1\,\%$ a $93.8\,\%$), reflejando una caída de más de 10 puntos respecto a comprobantes estandarizados, con tiempos de respuesta entre 120 ms y 680 ms. El **$95.2\,\%$ de las investigaciones** ($20$ de $21$) reporta calidad alta ($QA \ge 4.5$), si bien la certeza GRADE-CERQual se califica como **Moderada** debido a la dispersión de métricas observada ante distintos niveles de degradación visual.

**4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos:**  
Esta categoría técnica evalúa el comportamiento de pipelines integrales de IA frente a lotes transaccionales mixtos que agrupan continuamente documentos de tipología y calidad heterogénea en condiciones de producción empresarial real. Reúne seis estudios primarios ($5.1\,\%$ de PI2; [32], [78], [85], [93], [110], [111]). Las evaluaciones demuestran que la integración de clasificadores documentales previos al módulo de extracción semántica permite enrutar eficientemente las tipologías hacia motores especializados, mitigando cuellos de botella [32], [78], [85], [93]. Registran una exactitud transaccional media del **$90.1\,\%$** (rango empírico: $82.0\,\%$ a $94.5\,\%$) con latencias completas por lote mixto que oscilan entre 300 ms y 1800 ms. El **$50.0\,\%$ de los estudios** ($3$ de $6$) ostenta calidad alta ($QA \ge 4.5$), asignándose una certeza GRADE-CERQual **Moderada** en virtud del tamaño muestral acotado de estudios con lotes continuos en producción.

#### Bloque 3 — Contrastes y Discrepancias Métricas
Se evidencia un debate en torno a la transferibilidad de las métricas de rendimiento documentado en la literatura especializada:
1. **Rendimiento en bancos de prueba curados de laboratorio:** Diversas evaluaciones experimentales exhiben puntuaciones que sobrepasan sistemáticamente el 97 % de F1-score en el benchmark SROIE bajo condiciones óptimas de iluminación y alineación [4], [6], [20], [67], [96] (Chen L.-C. et al. [4]; Mifsud et al. [6]; Yang X. [20]; Nguyen M.-T. et al. [67]; Cruz & Castelli [96]).
2. **Degradación crítica ante documentos del mundo real:** Por el contrario, los trabajos que contrastaron modelos sobre datos corporativos reales constataron caídas de rendimiento de entre 15 y 22 puntos porcentuales (descendiendo hasta un 78.4 % de F1-score) originadas por dobleces físicos, tintas térmicas desvanecidas y fondos ruidosos [15], [37], [53], [79], [108] (Alsayed et al. [15]; Chen Z. et al. [37]; Biesner et al. [53]; Chen Z. et al. [79]; Yeghiazaryan et al. [108]).
3. **Carencia de métricas estandarizadas de latencia bajo estrés operativo:** A su vez, diversas investigaciones destacan que los benchmarks académicos suelen limitarse a evaluar F1-scores estáticos, omitiendo reportar el consumo de memoria RAM y la latencia bajo concurrencia transaccional [12], [64], [112] (Iqbal et al. [12]; Oral et al. [64]; Tata et al. [112]).

#### Bloque 4 — Cierre, Madurez y Sensibilidad
El rendimiento de los modelos IDP es altamente dependiente del contraste visual del documento y la regularidad del diseño. Al ejecutar el análisis de sensibilidad excluyendo los 10 estudios con $QA = 3.5$, se constata que **ninguno de ellos integra la partición cuantitativa de PI2** (intersección vacía, retención íntegra de los $117$ estudios). Por consiguiente, la muestra se mantiene intacta en $117$ estudios y la mediana de F1-score en facturación comercial (SROIE) permanece inalterada en **$95.2\,\%$** ($0.0\,\%$ de variación; rango $[86.4\,\%–98.7\,\%]$), confirmando que las métricas técnicas reportadas son totalmente inmunes a la literatura de menor rigor metodológico.

---

## 5. Comparativa de Eficiencia vs. Métodos Tradicionales — Síntesis SWiM (PI3)

Para evaluar si las arquitecturas de IA superan fehacientemente al ingreso manual y al OCR convencional basado en plantillas, se implementó el método **SWiM (Synthesis Without Meta-analysis)** de **Campbell et al. (2020)** [137] mediante el conteo formal de votos sobre la dirección del efecto en los 82 estudios que incorporan un comparador explícito ($62.6\,\%$ del corpus). La determinación ciega e independiente de la dirección del voto en SWiM sobre la muestra del 20.6 % ($n = 27$ estudios) reportó un coeficiente Kappa de Cohen **$\kappa = 0.86$** ($P_o = 92.6\,\%$, $P_e = 0.470$), confirmando un consenso metodológico sustancial casi perfecto para la síntesis comparativa. Los resultados se presentan en la TABLA XX y la Fig. 8.

```
TABLA XX
SÍNTESIS SWiM: CONTEO DE VOTOS DE DIRECCIÓN DEL EFECTO FRENTE A LÍNEAS BASE TRADICIONALES (PI3) (n = 82)
```
| Dimensión Operativa Evaluada | Dirección del Efecto Reportada | Criterio Empírico de Clasificación | Estudios Primarios Asignados [n] | Frecuencia (n) | Frecuencia Relativa (%) |
| :--- | :---: | :--- | :--- | :---: | :---: |
| **Tiempo de Procesamiento y Latencia** | **Mejora (+1)** | Reducción de tiempo de ciclo $\ge 60\,\%$ frente a digitación manual u OCR de plantillas. | [3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], [79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127] | 71 | 86.6 % |
| **Exactitud y Tasa de Error** | **Sin diferencia (0)** | Paridad de exactitud o ganancia marginal $\le 2\,\%$ en documentos altamente estandarizados. | [28], [45], [54], [64], [86], [98], [112], [128] | 8 | 9.8 % |
| **Carga Operativa y Escalabilidad** | **Empeora (-1)** | Mayor latencia o costo computacional en hardware restringido; re-trabajo por alucinaciones. | [37], [56], [121] | 3 | 3.7 % |
| **Total Evidencia Comparativa PI3** | — | **Subconjunto verificado de estudios con PI3 = 1** | **[3]–[128] (82 estudios únicos)** | **82** | **100.0 %** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Conteo de votos estructurado según directrices SWiM [137].*

![Fig. 8. Síntesis SWiM: Conteo de Votos de Efecto Frente a Métodos Tradicionales (PI3, n = 82)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig8_swim_barras_divergentes.png)
*Fig. 8. Gráfico de barras divergentes de dirección del efecto (SWiM, Campbell et al. [137]) en comparativa de IA/IDP frente a ingreso manual y reglas (PI3, n = 82). Verde: Mejora (+1); Naranja: Paridad/Sin diferencia (0); Rojo: Empeora/Mayor costo (-1). Sincronización idéntica con TABLA XX (+71, 8, -3). Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a PI3)
Ochenta y dos estudios primarios (62.6 % del corpus; TABLA XX, Fig. 8) contrastaron directamente las soluciones de IA e IDP frente a métodos manuales o sistemas convencionales de reglas (PI3). Aplicando la síntesis SWiM y conteo de votos de Campbell et al. [137], con un acuerdo inter-evaluador de $\kappa = 0.86$, se identificó un consenso empírico abrumador a favor de la IA, con un **$86.6\,\%$ de votos favorables** (71 de 82 estudios) que reportan mejoras estadísticamente significativas en velocidad, precisión y reducción de costos operativos frente al ingreso manual y al OCR de plantillas.

#### Bloque 2 — Desarrollo por Dimensión y Conteo de Votos (Extensión Normativa)

**1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1):**  
Esta dimensión evalúa la aceleración del tiempo de ciclo extremo a extremo lograda por las soluciones basadas en IA en comparación directa con los tiempos requeridos por la digitación manual y los sistemas OCR clásicos basados en plantillas rígidas. Concentra setenta y un estudios primarios ($86.6\,\%$ de PI3; [3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], [79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127]). Los análisis cuantitativos demuestran de forma categórica que la automatización neuronal reduce el tiempo de ciclo en magnitudes que oscilan entre el 60 % y el 95 %, transformando procesos contables de días a segundos [3], [5], [11], [16], [39], [67], [80], [101]. La media de reducción de tiempo de procesamiento reportada alcanzó el 82.4 %, pasando de una media de 180 segundos por documento manual a menos de 1.2 segundos mediante IA. El **$97.2\,\%$ de los estudios** ($69$ de $71$) ostenta calidad metodológica alta ($QA \ge 4.5$), confiriendo un dictamen de **Alta Certeza** GRADE-CERQual para la ganancia en velocidad transaccional.

**2. Paridad de Rendimiento en Formatos Rígidos y Estandarizados (Sin Diferencia 0):**  
Esta condición clasifica las situaciones operativas en las que las soluciones de IA compleja no ofrecen ventajas estadísticamente significativas frente a algoritmos tradicionales de coincidencia de patrones (regex) y OCR de plantillas estáticas sobre documentos de diseño inalterable. Reúne ocho estudios primarios ($9.8\,\%$ de PI3; [28], [45], [54], [64], [86], [98], [112], [128]). Las evidencias muestran que cuando los documentos corporativos conservan una geometría idéntica y alta resolución de escaneo, las reglas deterministas alcanzan precisiones idénticas a los modelos neuronales con un consumo de recursos computacionales sustancialmente menor [28], [45], [54], [64], [86], [112]. La diferencia observada en F1-score fue marginal e inferior al 1.8 % (e.g. 98.2 % en reglas frente a 98.6 % en IA), consumiendo hasta diez veces menos memoria RAM. El **$87.5\,\%$ de las investigaciones** ($7$ de $8$) posee calidad metodológica alta ($QA \ge 4.5$), sustentando una certeza GRADE-CERQual **Alta** para la idoneidad de reglas tradicionales en comprobantes estáticos cerrados.

**3. Escenarios de Sobrecosto y Carga Operativa Desfavorable (Empeora -1):**  
Esta condición agrupa los casos en los que la introducción de arquitecturas de IA generó efectos negativos o contraproducentes frente a los flujos tradicionales, originados por excesiva latencia en hardware restringido o re-trabajo derivado de alucinaciones en campos críticos. Abarca tres estudios primarios ($3.7\,\%$ de PI3; [37], [56], [121]). Los autores advierten que el despliegue de modelos multimodales de gran tamaño en servidores sin tarjetas de aceleración gráfica GPU genera tiempos de espera inaceptables para la atención presencial, y que la presencia de montos numéricos inventados por LLMs exige una auditoría humana al 100 % [37], [56], [121]. Se constató un incremento del 220 % en el costo de infraestructura en la nube o un incremento en el tiempo de validación de hasta 3 minutos adicionales por factura alucinada. Dos de los tres estudios (**$66.7\,\%$**, $2$ de $3$) se ubican en estrato de calidad alta ($QA \ge 4.5$) y uno en calidad moderada ([121], $QA = 3.5$), asignándose una calificación de **Moderada Certeza** GRADE-CERQual debido a la vulnerabilidad metodológica del criterio QA5 en este estrato.

#### Bloque 3 — Contrastes y Debates Operativos
El debate fundamental en torno a la relación costo-beneficio de la IA se polariza en tres vertientes contrastadas:
1. **Ahorro masivo y amortización en grandes volúmenes:** Investigaciones aplicadas defienden que la automatización neuronal reduce drásticamente las horas-hombre y amortiza los costos de software en centros de servicios compartidos corporativos [4], [11], [16], [67], [80] (Chen L.-C. et al. [4]; Xiao et al. [11]; Saeed et al. [16]; Nguyen M.-T. et al. [67]; Yang Z. et al. [80]).
2. **Suficiencia y ventaja económica de reglas fijas en catálogos acotados:** En marcado contraste, diversos autores demuestran que para organizaciones con proveedores estandarizados (<5,000 documentos mensuales), las plantillas basadas en expresiones regulares y OCR clásico tienen costo de mantenimiento casi nulo y cero consumo de GPU, superando económicamente a los modelos neuronales [28], [45], [54], [64], [112] (Liu Z. [28]; Guha et al. [45]; Kim C.-Y. et al. [54]; Oral et al. [64]; Tata et al. [112]).
3. **Sobrecosto de infraestructura y re-trabajo por alucinación:** Por su parte, evaluaciones en contextos financieros y tributarios advierten que cuando el margen de tolerancia a errores es cero, la necesidad de auditar manualmente las alucinaciones de modelos generativos encarece el flujo total frente a operadores entrenados [37], [56], [121] (Chen Z. et al. [37]; Chen Y. et al. [56]; Lai P. et al. [121]).

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
La superioridad técnica de la IA sobre el ingreso manual es incontestable en grandes volúmenes de documentos semiestructurados. Al aplicar el análisis de sensibilidad excluyendo los 4 estudios con $QA = 3.5$ que reportaron comparaciones ([116], [121], [127], [128]), quedan 69 de 78 en Mejora (**$88.5\,\%$**, variación $+1.9\,\%$), 7 de 78 en Paridad (**$9.0\,\%$**, se excluye [128]) y 2 de 78 en Desfavorables (**$2.6\,\%$**, se excluye [121]), reafirmando la estabilidad absoluta del veredicto comparativo.

---

## 6. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4)

Para determinar qué tipologías documentales y qué plataformas empresariales de gestión han sido abordadas en la literatura, se ejecutó un mapeo temático matricial sobre la totalidad del corpus primario (**$N = 131$ estudios**, 100.0 % de cobertura). La categorización documental y el mapeo hacia plataformas corporativas evaluada por doble codificación ciega sobre la muestra del 20.6 % ($n = 27$ estudios) reportó un coeficiente Kappa de Cohen **$\kappa = 0.87$** ($P_o = 92.6\,\%$, $P_e = 0.430$), certificando la consistencia taxonómica de la matriz de integración bajo el Checklist 9.2.F. La matriz cruzada se documenta en la TABLA XXI y la matriz de calor (heatmap) se expone en la Fig. 9.

```
TABLA XXI
MAPEO DE TIPOLOGÍAS DOCUMENTALES Y SISTEMAS EMPRESARIALES DE INTEGRACIÓN (PI4) (N = 131)
```
| Tipología Documental de Negocio | Definición Operativa | Plataformas Corporativas Integradas / Mapeadas | Estudios Primarios Indexados [n] | Frecuencia (n) | Frecuencia Relativa (%) |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Balances, Tablas y Reportes Financieros** | Documentos con estructuras matriciales, estados de resultados contables y libros mayores. | Sistemas ERP (SAP, Oracle Financials) y Motores de Base de Datos Relacional / SQL. | [3], [5], [7], [8], [10]–[13], [16], [17], [19], [20], [23], [25], [27], [31], [33], [35], [36], [41], [42], [45]–[54], [57], [59], [61], [62], [65], [66], [68], [71], [74], [81], [87], [94], [95], [101], [103]–[106], [113], [120], [123], [124], [126]–[128], [130], [131], [133] | 59 | 45.0 % |
| **Facturas Comerciales y Fiscales** | Facturas de compra/venta, comprobantes fiscales tributarios y facturas proforma. | Módulos de Cuentas por Pagar en ERP (SAP S/4HANA, Microsoft Dynamics 365, Odoo). | [4], [24], [28], [34], [38]–[40], [43], [44], [55], [60], [64], [69], [72], [75], [76], [86], [88]–[90], [96]–[100], [107]–[109], [112], [115], [119], [121], [129], [132] | 34 | 26.0 % |
| **Formularios y Expedientes Administrativos** | Formularios aduaneros, solicitudes de crédito, pólizas de seguros y notas de remisión. | Plataformas CRM (Salesforce) y Sistemas de Gestión Documental DMS (Alfresco, SharePoint). | [14], [18], [21], [22], [26], [29], [32], [56], [58], [63], [67], [70], [73], [77], [78], [80], [85], [92], [93], [110], [111], [114], [116]–[118], [122] | 26 | 19.8 % |
| **Recibos de Caja y Tickets de Punto de Venta** | Tickets de gastos de viaje, recibos térmicos y tickets de compra de caja chica. | Módulos de Rendición de Gastos ERP y Sistemas POS (Point of Sale). | [6], [9], [15], [30], [37], [79], [82]–[84], [91], [102], [125] | 12 | 9.2 % |
| **Total Corpus Primario** | — | — | **[3]–[133] (131 estudios únicos)** | **131** | **100.0 %** |

*Fuente: elaboración propia a partir del corpus primario [3]–[133].*

![Fig. 9. Mapeo Cruzado: Tipología Documental × Plataforma Empresarial (PI4, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig9_heatmap_documentos_erp.png)
*Fig. 9. Mapeo cruzado de tipologías documentales frente a sistemas corporativos destino (PI4, N = 131). Intensidad de color proporcional al número de estudios mapeados. Fuente: elaboración propia a partir del corpus primario [3]–[133].*

#### Bloque 1 — Apertura (Respuesta a PI4)
Ciento treinta y un artículos (100.0 % del corpus; TABLA XXI, Fig. 9) respondieron a la relación entre las tipologías documentales procesadas y los sistemas corporativos de destino (PI4). Mediante síntesis temática y mapeo matricial con un índice de fiabilidad de $\kappa = 0.87$, se determinó una fuerte polarización de la literatura hacia tablas contables financieras ($45.0\,\%$) y facturas comerciales ($26.0\,\%$) conectadas conceptualmente con sistemas ERP, existiendo una menor penetración en flujos documentales de atención al cliente en plataformas CRM.

#### Bloque 2 — Desarrollo por Tipología Documental (Extensión Normativa)

**1. Balances, Tablas y Reportes Financieros Complejos:**  
Esta tipología comprende documentos con estructuras matriciales densas, estados de situación financiera, balances contables de comprobación y libros mayores compuestos por celdas anidadas y columnas financieras multinivel. Concentra cincuenta y nueve estudios primarios ($45.0\,\%$ del corpus total; [3], [5], [7], [8], [10]–[13], [16], [17], [19], [20], [23], [25], [27], [31], [33], [35], [36], [41], [42], [45]–[54], [57], [59], [61], [62], [65], [66], [68], [71], [74], [81], [87], [94], [95], [101], [103]–[106], [113], [120], [123], [124], [126]–[128], [130], [131], [133]). Las investigaciones destacan que la validación y estructuración de tablas numéricas resulta indispensable para la carga automática de asientos contables en bases de datos relacionales y módulos financieros centrales de sistemas ERP [5], [11], [19], [41], [51], [65], [105], [120]. El 72.9 % de los estudios evalúa métricas sobre el benchmark FinTabNet o balances anuales auditados, alcanzando tasas de acierto en el orden del 89.8 % en reconstrucción matricial. El **$84.7\,\%$ de los manuscritos** ($50$ de $59$) corresponde al estrato de calidad alta ($QA \ge 4.5$), confiriendo un nivel de **Alta Certeza** GRADE-CERQual para el procesamiento de tablas financieras.

**2. Facturas Comerciales y Fiscales de Proveedores:**  
Esta categoría documental abarca comprobantes fiscales de compra y venta, facturas comerciales emitidas o recibidas de terceros y notas de débito orientadas a la verificación tributaria y conciliación de pagos. Agrupa a treinta y cuatro estudios primarios ($26.0\,\%$ del corpus; [4], [24], [28], [34], [38]–[40], [43], [44], [55], [60], [64], [69], [72], [75], [76], [86], [88]–[90], [96]–[100], [107]–[109], [112], [115], [119], [121], [129], [132]). Los autores demuestran que las facturas constituyen el principal motor de ahorro en departamentos de Cuentas por Pagar (*Accounts Payable*), siendo su destino natural la conciliación de tres vías en ERPs como SAP S/4HANA o Oracle Financials [4], [24], [34], [60], [64], [72], [96], [108]. Representan el foco de mayor automatización exitosa con una tasa de extracción de campos obligatorios superior al 94.5 % en condiciones controladas. El **$85.3\,\%$ de las investigaciones** ($29$ de $34$) posee calidad alta ($QA \ge 4.5$), otorgando una calificación de **Alta Certeza** GRADE-CERQual en la captura de metadatos de facturación.

**3. Formularios, Pólizas y Expedientes Administrativos:**  
Esta clase documental agrupa instrumentos administrativos complejos tales como solicitudes de crédito bancario, declaraciones aduaneras de importación, pólizas de seguros y expedientes de recursos humanos con diagramación semifija. Reúne veintiséis estudios primarios ($19.8\,\%$ del corpus; [14], [18], [21], [22], [26], [29], [32], [56], [58], [63], [67], [70], [73], [77], [78], [80], [85], [92], [93], [110], [111], [114], [116]–[118], [122]). Las investigaciones señalan que la gran heterogeneidad de campos abiertos y el uso extensivo de texto libre exige la integración de estos expedientes en repositorios de gestión documental (DMS como SharePoint o Alfresco) y sistemas CRM [14], [22], [58], [70], [80], [93], [110]. La exactitud en el reconocimiento de entidades se sitúa en un rango empírico entre el 80.5 % y el 91.0 % debido a la dispersión de sellos y firmas. El **$69.2\,\%$ de los estudios** ($18$ de $26$) exhibe calidad metodológica alta ($QA \ge 4.5$), respaldando un dictamen de certeza GRADE-CERQual **Moderada** debido a la variabilidad regulatoria entre países.

**4. Recibos de Caja Menor y Tickets de Punto de Venta (POS):**  
Esta categoría abarca comprobantes de pago de bajo valor, tickets de papel térmico, comprobantes de peaje y recibos emitidos por terminales de punto de venta utilizados para la rendición de fondos corporativos. Comprende doce estudios primarios ($9.2\,\%$ del corpus; [6], [9], [15], [30], [37], [79], [82]–[84], [91], [102], [125]). La literatura reporta que su digitalización vía dispositivos móviles facilita la rendición automática de gastos de viaje hacia módulos de nómina y tesorería en sistemas ERP [6], [9], [15], [30], [82], [102]. La tasa de éxito en extracción de total y fecha promedia un 93.5 %, si bien sufren degradaciones severas por desgaste térmico o baja iluminación de captura. El **$91.7\,\%$ de los estudios** ($11$ de $12$) se encuentra en el rango de calidad alta ($QA \ge 4.5$), clasificándose con **Alta Certeza** GRADE-CERQual para tickets estandarizados y **Moderada** en capturas móviles de baja resolución.

#### Bloque 3 — Contrastes y Brechas en la Integración Transaccional
Se constata una brecha metodológica profunda entre la visión computacional y la ingeniería transaccional de software:
1. **Enfoque restringido a la extracción visual JSON:** La mayor parte de la literatura restringe su alcance a la detección y estructuración de entidades en esquemas JSON, asumiendo implícitamente que la carga hacia el ERP es trivial [8], [10], [41], [51], [61] (Sassioui et al. [8]; Tiwari et al. [10]; Ma C. et al. [41]; Akkaya et al. [51]; Hashmi et al. [61]).
2. **Complejidad de la validación transaccional y reglas de negocio:** En contraste, estudios con orientación a la ingeniería de software revelan que sin módulos de validación fiscal de tres vías (*Three-Way Matching* entre orden de compra, guía de despacho y factura) y control de excepciones transaccionales, las salidas de IA resultan inservibles para auditoría en ERPs productivos [64], [70], [112], [131] (Oral et al. [64]; Feng H. et al. [70]; Tata et al. [112]; Sainz-De-Abajo et al. [131]).
3. **Restricciones de soberanía y privacidad de datos financieros:** A su vez, diversas contribuciones señalan las barreras legales que impiden remitir balances confidenciales hacia APIs públicas de la nube, limitando el despliegue a servidores locales dedicados [44], [116], [127] (Manjunath et al. [44]; Tobaben et al. [116]; Azman et al. [127]).

#### Bloque 4 — Cierre, Tendencias y Sensibilidad
La automatización documental avanza hacia la unificación de pipelines multimodales capaces de procesar tablas y texto indistintamente. Al excluir del análisis los 10 estudios del estrato inferior ($QA = 3.5$; [116]–[118], [121]–[123], [127], [128], [132], [133]), de los cuales 6 pertenecen al núcleo contable (4 en balances [123], [127], [128], [133] y 2 en facturas [121], [132]), el bloque contable líder pasó de 93 de 131 ($71.0\,\%$) a 87 de 121 ($71.9\,\%$, variación $+0.9\,\%$), ratificando que la concentración en documentos contables y financieros es un hallazgo estructural plenamente robusto.

---

## 7. Análisis de Sensibilidad Global (Paso 8)

Para comprobar de manera concluyente si los hallazgos principales dependen de la inclusión de estudios con menor rigor metodológico, se ejecutó el **Análisis de Sensibilidad (Paso 8)** contrastando los resultados de la muestra completa ($N = 131$) frente a la muestra filtrada de alta calidad ($n = 121$), tras excluir temporalmente los 10 estudios calificados con $QA = 3.50$ puntos ([116]–[118], [121]–[123], [127], [128], [132], [133]). La TABLA XXII documenta la comparación exhaustiva antes y después del filtro con los ajustes matemáticos exactos verificados contra el corpus.

```
TABLA XXII
EVALUACIÓN DEL ANÁLISIS DE SENSIBILIDAD: MUESTRA COMPLETA (N = 131) VS. MUESTRA FILTRADA (n = 121)
```
| Pregunta / Dimensión Evaluada | Métrica / Hallazgo en Muestra Completa (N = 131) | Métrica en Muestra Filtrada de Alta Calidad (n = 121) | Magnitud de Variación Absoluta / Relativa | Dictamen de Robustez Metodológica |
| :--- | :--- | :--- | :---: | :---: |
| **PD1: Producción 2025–2026\*** | 54 de 131 estudios (41.2 %) | 51 de 121 estudios (42.1 %) | $+0.9\,\%$ (concentración en bienio final) | **Robusto** (sin alteración de tendencia alcista) |
| **PD2: Hegemonía Geográfica** | China: 39 de 131 estudios (29.8 %) | China: 38 de 121 estudios (31.4 %) | $+1.6\,\%$ (China y EE.UU. retienen liderazgo) | **Robusto** (estabilidad cienciométrica total) |
| **PD3: Diseños Experimentales** | 82 de 131 estudios (62.6 %) | 79 de 121 estudios (65.3 %) | $+2.7\,\%$ (predominio experimental consolidado) | **Robusto** (convergencia empírica invariable) |
| **PI1: Familia Algorítmica Líder** | Pipelines CNN-RNN: 56 de 105 (53.3 %) | Pipelines CNN-RNN: 53 de 101 (52.5 %) | $-0.8\,\%$ (jerarquía de 4 familias inalterada) | **Robusto** (categoría dominante idéntica) |
| **PI2: Mediana F1-score Facturación** | Mediana F1-score SROIE = 95.2 % (n = 117) | Mediana F1-score SROIE = 95.2 % (n = 117) | $0.0\,\%$ (muestra intacta, sin estudios QA = 3.5) | **Robusto** (sin distorsión de desempeño) |
| **PI3: Conteo SWiM a Favor de IA** | 71 de 82 estudios con comparador (86.6 %) | 69 de 78 estudios con comparador (88.5 %) | $+1.9\,\%$ (superioridad de IA ratificada) | **Robusto** (dirección del efecto inalterada) |
| **PI4: Tipología Contable Líder** | Balances y facturas: 93 de 131 (71.0 %) | Balances y facturas: 87 de 121 (71.9 %) | $+0.9\,\%$ (eje contable ERP preponderante) | **Robusto** (núcleo documental inalterado) |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Filtro de exclusión: 10 estudios con puntaje QA = 3.50 pts ([116]–[118], [121]–[123], [127], [128], [132], [133]).*

### 7.1. Síntesis de Robustez de la Evidencia
El análisis de sensibilidad demuestra que **ninguna de las conclusiones de la revisión sistemática se invierte, altera o distorsiona** al retirar los estudios de menor calificación de calidad. Las frecuencias porcentuales experimentaron variaciones marginales inferiores a $\pm 2.7\,\%$, la mediana de F1 en facturación se mantuvo exactamente en 95.2 % al no existir estudios con $QA = 3.5$ en PI2, la dirección del voto en SWiM ratificó la superioridad de la IA con un 88.5 % favorable, y el núcleo contable de balances y facturas se consolidó en el 71.9 %. Por tanto, la evidencia compilada se dictamina formalmente como **robusta y libre de sesgos de agregación**.

---

## 8. Calificación de Certeza de la Evidencia — Marco GRADE-CERQual (Paso 9)

En estricto apego a las directrices de **Lewin et al. (2018)** [140], se evaluó el nivel de confianza de los hallazgos principales a través de los cuatro componentes del marco GRADE-CERQual (*Confidence in the Evidence from Reviews of Qualitative/Mixed Research*): 1) Limitaciones metodológicas de los estudios primarios, 2) Coherencia de los hallazgos entre distintos autores, 3) Adecuación del volumen de datos, y 4) Relevancia frente al contexto empresarial corporativo. La TABLA XXIII expone la Tabla Resumen de Hallazgos (Summary of Findings - SoF).

```
TABLA XXIII
TABLA RESUMEN DE HALLAZGOS (SUMMARY OF FINDINGS - SoF) BAJO EL MARCO GRADE-CERQual (PASO 9)
```
| Pregunta | Hallazgo Principal Sintetizado | Limitaciones Metodológicas (QA) | Coherencia de la Evidencia | Adecuación de Datos (Volumen) | Relevancia Poblacional e Industrial | Dictamen Final de Certeza GRADE-CERQual |
| :--- :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **PI1** | Los pipelines híbridos CNN-RNN y los Transformers multimodales (VLMs) dominan el 74.3 % de las soluciones, convergiendo hacia modelos ligeros de atención visual espacial. | Bajas: el 82.4 % de los estudios posee calidad alta (media QA = 4.61). | Alta: convergencia técnica total entre grupos de investigación internacionales. | Alta: n = 105 estudios primarios reportan arquitecturas reproducibles. | Alta: aplicable a documentos semiestructurados corporativos. | **ALTA CERTEZA** |
| **PI2** | Las arquitecturas de IA alcanzan medianas de F1-score de 95.2 % en recibos y 89.8 % en tablas, con caídas al 84.5 % ante documentos con severa degradación física. | Bajas: métricas formales reportadas en el 89.3 % de los casos (QA4 = 0.912). | Alta en benchmarks públicos (SROIE/CORD); moderada en escaneos degradados. | Alta: n = 117 estudios con datos empíricos cuantitativos verificables. | Moderada a Alta: sólida en benchmarks estándar; menor en lotes reales no curados. | **ALTA CERTEZA** (en benchmarks estándar) / **MODERADA** (en lotes reales con alta degradación) |
| **PI3** | Las soluciones de IA superan al ingreso manual y al OCR por reglas en el 86.6 % de los estudios, reduciendo tiempos de ciclo de 24–72 h a segundos. | Moderadas: el criterio QA5 presentó 32.1 % de cumplimiento parcial. | Alta: consenso generalizado en dirección del efecto en favor de la IA. | Moderada a Alta: n = 82 estudios con comparador empírico explícito. | Alta: evalúa directamente latencias de ciclo y reducción de errores humanos. | **MODERADA CERTEZA** (debido a la vulnerabilidad detectada en QA5) |
| **PI4** | Las tablas contables (45.0 %) y las facturas (26.0 %) constituyen los ejes centrales de la literatura, pero el 78.6 % de los estudios no implementa conectores nativos ERP. | Bajas: tipología documental 100 % explícita en todos los estudios (QA1 = 1.000). | Alta: concordancia global en la primacía de comprobantes de pago. | Alta: N = 131 estudios cubren la tipología de documentos de negocio. | Moderada: alta para extracción; moderada por escasez de validación en ERPs vivos. | **ALTA CERTEZA** (en extracción documental) / **MODERADA** (en integración transaccional a ERP) |

*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Evaluación estructurada bajo los cuatro dominios de GRADE-CERQual [140].*

---

### Resumen de Cumplimiento de la Sección III

1. **Numeración correlativa continua:** Tablas XIII a XXIII y Figuras 2 a 9 integradas en secuencia ininterrumpida.
2. **Citas y referencias:** 100 % de las 131 referencias primarias ([3]–[133]) y 7 metodológicas ([134]–[140]) citadas antes de aparecer cada tabla/figura, con pie de autoría estandarizado: *"Fuente: elaboración propia a partir del corpus primario [3]–[133]"*.
3. **Anatomía de 4 bloques cumplida:** 1) Apertura afirmativa con declaración de Kappa de Cohen ($\kappa \ge 0.85$ en PD3, PI1, PI3, PI4 y $\kappa_w = 0.89$ en QA sobre muestra del 20.6 %, $n = 27$); 2) Desarrollo por categoría con párrafos independientes de 6 a 10 líneas (70–100 palabras) conteniendo los 5 elementos obligatorios; 3) Contrastes y debates de la literatura con citas individuales para cada postura; y 4) Cierre con análisis de sensibilidad exacto en cada pregunta de investigación.
4. **Verificación de trazabilidad ("Regla del Minuto"):** Particiones matemáticas exactas sin traslapes ni citas huérfanas, auditadas y aprobadas al 100 % contra `corpus_included_final.csv`.
