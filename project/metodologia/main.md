# Metodología de la Revisión Sistemática de Literatura (RSL)

## 0. Encuadre metodológico y estándares de investigación

La presente Revisión Sistemática de Literatura (RSL) se diseña y ejecuta bajo las directrices metodológicas de **Kitchenham & Charters (2007)** para la ingeniería de software y sistemas de información, y se reporta siguiendo los estándares internacionales de la declaración **PRISMA 2020** (_Preferred Reporting Items for Systematic Reviews and Meta-Analyses_).

El protocolo de investigación (preguntas, criterios de elegibilidad, ecuaciones de búsqueda y estrategia de extracción) ha sido formalizado _a priori_ para garantizar la objetividad, la reproducibilidad y la mitigación de sesgos en la selección del corpus documental.

---

## 1. Paso 1 — El tema de partida y delimitación del estudio

El estudio aborda el uso de la **Inteligencia Artificial (IA)** y el **Procesamiento Inteligente de Documentos (IDP / Intelligent Document Processing)** en la automatización del registro y la validación de documentos empresariales.

- **Delimitación positiva:** Sistemas de información empresariales (ERP, CRM, gestores documentales) y flujos internos de registro y validación documental corporativos estrictamente privados.
- **Delimitación negativa:** Se excluyen los sistemas de administración pública/gubernamental, los servicios de atención ciudadana y los flujos documentales masivos de cara al usuario final externo, debido a que obedecen a marcos regulatorios, volumetrías y dinámicas operativas distintas.

---

## 2. Paso 2 — Delimitación de los componentes PICOC

Para descomponer el problema y asegurar una cobertura exhaustiva y auditable, se emplea el marco extendido **PICOC** (Población, Intervención, Comparación, Outcome/Resultado y Contexto):

| Componente                   | Definición para este estudio                                                                                                                | Justificación                                                                                                                            |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **P — Población / Problema** | Sistemas de información empresariales (ERP, CRM, DMS) y flujos internos de registro y validación documental.                                | Representa el entorno operativo y tecnológico donde se generan cuellos de botella por el ingreso manual y la heterogeneidad de formatos. |
| **I — Intervención**         | Arquitecturas de Inteligencia Artificial para IDP (IA-OCR, KIE, modelos basados en secuencias, grafos o LLM multimodales).                  | Constituye la tecnología y enfoque algorítmico cuyo impacto y eficacia se analizan en la literatura.                                     |
| **C — Comparación**          | Ingreso manual de datos o procesamiento tradicional basado en reglas y plantillas rígidas.                                                  | Establece la línea base convencional frente a la cual se contrasta la ganancia en precisión, tiempo y costos.                            |
| **O — Resultado / Outcome**  | Grado de automatización, reducción de la carga operativa, precisión en la extracción (F1-score, exactitud) y velocidad/tiempo de respuesta. | Variables cuantitativas y métricas de rendimiento clave para evaluar la viabilidad y el retorno operativo.                               |
| **C — Contexto**             | Entornos corporativos privados y ventana temporal 2020–2025.                                                                                | Delimita el dominio de aplicación y el período de maduración de los modelos de aprendizaje profundo y multimodales.                      |

---

## 3. Paso 3 — La pregunta maestra

Articulando los cinco componentes del marco PICOC en una única formulación integral, la pregunta principal de la investigación se define como:

> **¿Cuál es el impacto de las arquitecturas de Inteligencia Artificial y Procesamiento Inteligente de Documentos (IDP), frente al ingreso manual y enfoques basados en reglas, sobre la precisión, la velocidad y la reducción de la carga operativa en el registro y validación documental dentro de sistemas empresariales, entre 2020 y 2025?**

---

## 4. Paso 4 — Descomposición en preguntas de investigación (PI)

A partir del andamiaje PICOC, la pregunta maestra se descompone en **cuatro Preguntas de Investigación (PI)** temáticas que orientan la extracción y síntesis de evidencia técnica:

| Código  | Pregunta de investigación                                                                                                                                                        | Componente PICOC que la origina |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------------------: |
| **PI1** | ¿Qué arquitecturas y enfoques algorítmicos de IA/IDP (secuencias, grafos, modelos generativos multimodales) se han implementado en el procesamiento de documentos empresariales? |              **I**              |
| **PI2** | ¿Qué niveles de precisión (F1-score, exactitud) y velocidad/tiempo de resolución alcanzan estas arquitecturas en tareas de extracción de datos semiestructurados?                |            **I + O**            |
| **PI3** | ¿Qué diferencias de desempeño, escalabilidad y costo operativo se reportan entre las soluciones basadas en IA y los métodos tradicionales o manuales?                            |           **I vs. C**           |
| **PI4** | ¿En qué tipologías documentales (facturas, recibos, formularios, contratos) y arquitecturas de sistemas empresariales (ERP/CRM) se han validado estas propuestas?                |        **P / Contexto**         |

---

## 5. Paso 5 — Preguntas descriptivas o bibliométricas (PD)

Para caracterizar cuantitativamente el cuerpo de literatura científica recuperado, se formulan **tres Preguntas Descriptivas (PD)** independientes del análisis temático PICO:

| Código  | Pregunta descriptiva / bibliométrica                                                                                                                   | Propósito en la RSL                                                                                 |
| :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **PD1** | ¿Cómo ha evolucionado el volumen de producción científica anual sobre IA aplicada a documentos empresariales entre 2020 y 2025?                        | Identificar tendencias de publicación y puntos de inflexión temporal en el área.                    |
| **PD2** | ¿Qué autores, revistas/conferencias indexadas y países concentran la mayor productividad e impacto académico?                                          | Mapear los núcleos de investigación y los canales de difusión de mayor relevancia.                  |
| **PD3** | ¿Qué tipos de diseño metodológico (estudios de caso, experimentos controlados, benchmarks) y datasets (públicos vs. privados) predominan en el corpus? | Evaluar el nivel de madurez empírica y la transferibilidad de las soluciones al entorno industrial. |

---

## 6. Paso 6 — Términos de búsqueda y ecuación lógica

A partir de los componentes PICOC, se derivaron los términos clave y sinónimos en inglés, combinándolos con el operador booleano `OR` dentro de cada bloque, aplicando comodines (`*`) para capturar variaciones morfológicas y uniendo los bloques con el operador `AND`.

### 6.1. Matriz de descriptores y palabras clave (actualizada)

| Bloque PICOC | Concepto base                                         | Descriptores en inglés (con sinónimos, variantes y comodines)                                                                                                                                                                               |
| :----------: | :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|    **P**     | Sistemas empresariales y documentos                   | `"business document*"` OR `"financial document*"` OR `"administrative document*"` OR `"invoice*"` OR `"receipt*"` OR `"document management"` OR `"business workflow*"` OR `"ERP"` OR `"enterprise system*"`                                 |
|    **I**     | Inteligencia Artificial y Procesamiento de Documentos | `"intelligent document processing"` OR `"IDP"` OR `"document AI"` OR `"document understanding"` OR `"key information extraction"` OR `"KIE"` OR `"LayoutLM*"` OR `"optical character recognition"` OR `"OCR"` OR `"information extraction"` |
|  **O / C**   | Automatización, validación y desempeño                | `"automat*"` OR `"validat*"` OR `"extract*"` OR `"recognition"` OR `"accuracy"` OR `"efficiency"` OR `"workload"`                                                                                                                           |

### 6.2. Ecuación booleana principal calibrada

```text
("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*")
AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction")
AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload")
```

### 6.3. Adaptación sintáctica por base de datos

- **Scopus:**
  ```text
  TITLE-ABS-KEY(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))
  ```
- **Web of Science (WoS):**
  ```text
  TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction" OR "NLP" OR "deep learning" OR "machine learning") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))
  ```

### 6.4. Registro de ecuaciones ejecutadas por iteración (Trazabilidad detallada)

Para preservar el registro exacto de cada consulta realizada sin saturar las tablas sinópticas, se codifican a continuación las cadenas booleanas ejecutadas para cada base de datos:

#### **[EQ-IT1-SCOPUS] Iteración 1 — Scopus (Exploratoria / Restrictiva)**

```text
TITLE-ABS-KEY(("enterprise information systems" OR "document management" OR "business workflows" OR "ERP" OR "invoice processing" OR "receipt processing") AND ("intelligent document processing" OR "IDP" OR "optical character recognition" OR "OCR" OR "information extraction" OR "key information extraction" OR "document AI" OR "LayoutLM") AND ("manual data entry" OR "manual processing" OR "traditional processing" OR "rule-based" OR "automation" OR "workload reduction" OR "efficiency" OR "accuracy"))
```

#### **[EQ-IT2-SCOPUS] Iteración 2 — Scopus (Calibrada Definitiva)**

```text
TITLE-ABS-KEY(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))
```

#### **[EQ-IT1-WOS] Iteración 1 — Web of Science (Exploratoria / Restrictiva)**

```text
TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))
```

#### **[EQ-IT2-WOS] Iteración 2 — Web of Science (Calibrada Definitiva)**

```text
TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction" OR "NLP" OR "deep learning" OR "machine learning") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))
```

### 6.5. Tabla comparativa de iteraciones y calibración de la búsqueda

La siguiente tabla resume la evolución metodológica del proceso de consulta, referenciando las ecuaciones codificadas en la sección 6.4:

| Base de datos | N.° Iteración | Ecuación referenciada | Resultados brutos ($n$) | Diagnóstico metodológico | Decisión | Evidencia archivada |
| :---: | :---: | :---: | :---: | :--- | :---: | :--- |
| **Scopus** | **Iteración 1** | `[EQ-IT1-SCOPUS]` | **142** | **Sobre-restringida:** Frases literales cerradas y comparación manual rígida que limitaron la recuperación. | **Descartada** | `project/metodologia/evidencias/scopus_iteracion1_142.png` |
| **Scopus** | **Iteración 2** | `[EQ-IT2-SCOPUS]` | **865** | **Óptima:** Uso de comodines (`*`), descriptores _KIE/Doc AI_ y ampliación morfológica ($800 \le n \le 1200$). | **Aprobada** | `project/metodologia/evidencias/scopus_iteracion2_865.png` |
| **Web of Science** | **Iteración 1** | `[EQ-IT1-WOS]` | **123** | **Sobre-restringida:** El campo `TS` de WoS con sintaxis estricta resultó excesivamente restrictivo frente a Scopus. | **Descartada** | `project/metodologia/evidencias/wos_iteracion_1_123.png` |
| **Web of Science** | **Iteración 2** | `[EQ-IT2-WOS]` | **755** | **Óptima:** Ampliación del bloque de Intervención con sinónimos generales (_NLP, deep learning, machine learning_). | **Aprobada** | `project/metodologia/evidencias/wos_iteracion_2_755.png` |

---
## 7. Paso 7 — Criterios de inclusión y exclusión codificados

Los criterios de elegibilidad se codifican de forma unívoca para permitir la trazabilidad individual de cada decisión de cribado y se vinculan a sus evidencias correspondientes:

> **Regla operativa de filtrado:** Primero se declaran los criterios de inclusión; durante el cribado, se aplican primero las exclusiones gruesas (año, idioma, tipo de documento) y posteriormente se verifica la inclusión temática a texto completo.

| Código | Tipo | Criterio de elegibilidad | Evidencia / Verificación asociada |
| :---: | :---: | :--- | :--- |
| **IN1** | Inclusión | Estudios publicados en la ventana temporal comprendida entre **2020 y 2025**. | `project/metodologia/evidencias/IN1_Scopus_limite_años.png`<br>`project/metodologia/evidencias/IN1_WebOS_limite_años.png` |
| **IN2** | Inclusión | Artículos de revista revisados por pares (_journal articles_) o ponencias en congresos internacionales indexados (_conference proceedings_). | `project/metodologia/evidencias/IN2_Scopus_tipo_documentos.png`<br>`project/metodologia/evidencias/IN2_WebOS_tipo_documentos.png` |
| **IN3** | Inclusión | Estudios indexados en las bases de datos principales **Scopus** o **Web of Science Core Collection**. | `project/metodologia/evidencias/IN3_Scopus_evidencia.png`<br>`project/metodologia/evidencias/IN3_WebOS_evidencia.png` |
| **IN4** | Inclusión | Artículos que propongan, evalúen o comparen modelos de IA/IDP aplicados al registro, extracción o validación de documentos en entornos empresariales. | Matriz de Mapeo (Paso 10) y dataset final:<br>`project/metodologia/outputs/corpus_included_final.csv` |
| **EX1** | Exclusión | Documentos publicados en idiomas distintos al **inglés** o **español**. | Filtros nativos aplicados en Scopus y WoS (`IN1_Scopus_limite_años.png`) |
| **EX2** | Exclusión | Publicaciones no disponibles a texto completo a través de los accesos institucionales. | Verificación en Fase 3 de Elegibilidad ($n = 5$) |
| **EX3** | Exclusión | Literatura gris, preprints sin arbitraje, notas editoriales o revisiones puramente teóricas sin validación empírica en documentos empresariales. | Descarte nativo y exclusión en Elegibilidad ($n = 8$) |
| **EX4** | Exclusión | Estudios enfocados exclusivamente en trámites del sector público/gubernamental o registros médicos/clínicos no equiparables a flujos empresariales. | Registros excluidos en cribado de título/resumen ($n = 680$) |
| **EX-n** | Exclusión | Documentos que, tras la evaluación temática, no aportan evidencia empírica a ninguna de las cuatro preguntas de investigación (**PI1–PI4**). | Registros excluidos en cribado ($n = 65$) y elegibilidad ($n = 7$) |

---

## 8. Paso 8 — Bitácora de reducción del corpus (evidencia de búsqueda)

Para garantizar la **reproducibilidad temporal**, las búsquedas en ambas bases se ejecutaron en la misma fecha calendario (**21/09/2026**).

### 8.1. Registro maestro por base indexada

| Base de datos | Fecha de ejecución | Ecuación adaptada | Resultados brutos ($n$) | Tras filtros nativos ($n$) | Archivo exportado de evidencia |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Scopus** | 21/09/2026 | `[EQ-IT2-SCOPUS]` en `TITLE-ABS-KEY` | **865** | **458** | `project/metodologia/outputs/scopus_export_Sep 21-2026_3cc76042-0bc1-42ac-864b-2c1c706c1fcc.csv`<br>`project/metodologia/evidencias/IN3_Scopus_evidencia.png` |
| **Web of Science** | 21/09/2026 | `[EQ-IT2-WOS]` en `TS` | **755** | **502** | `project/metodologia/outputs/webos_export_Sep 21-2026.xls`<br>`project/metodologia/evidencias/IN3_WebOS_evidencia.png` |
| **Total consolidado** | **21/09/2026** | — | **1620** | **960** | Archivos archivados en `outputs/` y `evidencias/` |

### 8.2. Bitácora de filtros nativos paso a paso (Scopus)

| Base | Filtro nativo aplicado | Valor del filtro | $n$ restante | Evidencia asociada |
| :--- | :--- | :--- | :---: | :--- |
| **Scopus** | *(Búsqueda inicial bruta — Iteración 2)* | Ecuación calibrada sin filtros | **865** | `project/metodologia/evidencias/scopus_iteracion2_865.png` |
| Scopus | 1. Rango temporal (`IN1`) | 2020–2025 | **492** | `project/metodologia/evidencias/IN1_Scopus_limite_años.png` |
| Scopus | 2. Tipo de documento (`IN2` / `EX3`) | Article (109), Conference Paper (349) | **458** | `project/metodologia/evidencias/IN2_Scopus_tipo_documentos.png` |
| Scopus | 3. Idioma y Colección (`IN3` / `EX1`) | English, Spanish / Scopus Elsevier | **458** | `project/metodologia/evidencias/IN3_Scopus_evidencia.png` |
| Scopus | **Total Scopus exportado** | Filtros acumulados | **458** | `project/metodologia/outputs/scopus_export_Sep 21-2026_3cc76042-0bc1-42ac-864b-2c1c706c1fcc.csv` |

### 8.3. Bitácora de filtros nativos paso a paso (Web of Science)

| Base | Filtro nativo aplicado | Valor del filtro | $n$ restante | Evidencia asociada |
| :--- | :--- | :--- | :---: | :--- |
| **WoS** | *(Búsqueda inicial bruta — Iteración 2)* | Ecuación calibrada sin filtros | **755** | `project/metodologia/evidencias/wos_iteracion_2_755.png` |
| WoS | 1. Rango temporal (`IN1`) | 2020–2025 | **502** | `project/metodologia/evidencias/IN1_WebOS_limite_años.png` |
| WoS | 2. Tipo de documento (`IN2` / `EX3`) | Article (502) | **502** | `project/metodologia/evidencias/IN2_WebOS_tipo_documentos.png` |
| WoS | 3. Indexación (`IN3`) | Web of Science Core Collection | **502** | `project/metodologia/evidencias/IN3_WebOS_evidencia.png` |
| WoS | **Total WoS exportado** | Filtros acumulados | **502** | `project/metodologia/outputs/webos_export_Sep 21-2026.xls` |

---

## 9. Paso 9 — Las cuatro fases del flujo PRISMA 2020

El proceso de selección ejecutado sobre los registros exportados de Scopus y Web of Science arroja las siguientes cifras exactas y matemáticamente consistentes:

```mermaid
flowchart TD
    subgraph F1["Fase 1: Identificación"]
        A1["Registros identificados en bases de datos<br>(Scopus: n = 458, WoS: n = 502)"] --> A2["Total de registros exportados tras filtros nativos<br>(n = 960)"]
        A2 --> A3["Eliminación de duplicados (cotejo por DOI y título normalizado)<br>(n = 85 eliminados)"]
        A3 --> A4["Registros únicos ingresados al cribado<br>(n = 875)"]
    end

    subgraph F2["Fase 2: Cribado (Screening)"]
        A4 --> B1["Cribado por título, resumen y pertinencia temática (IN4 vs EX1-EX4)"]
        B1 --> B2["Registros excluidos por título y resumen (n = 745)<br>• EX4 Fuera de dominio empresarial: n = 680<br>• EX-n Sin aporte a preguntas PI: n = 65"]
        B1 --> B3["Estudios que superan el cribado y pasan a elegibilidad<br>(n = 130)"]
    end

    subgraph F3["Fase 3: Elegibilidad"]
        B3 --> C1["Evaluación a texto completo y control de calidad metodológica (QA Kitchenham)"]
        C1 --> C2["Exclusiones justificadas a texto completo (n = 20)<br>• EX3 Revisiones teóricas sin prueba empírica: n = 8<br>• EX-n Sin métricas reproducibles: n = 7<br>• EX2 Sin acceso a texto completo: n = 5"]
        C1 --> C3["Estudios que superan el umbral de calidad (QA ≥ 3.0)"]
    end

    subgraph F4["Fase 4: Inclusión"]
        C3 --> D1["Corpus final de estudios primarios incluidos en la síntesis<br>(N = 110 estudios primarios)<br>• Estudios Nucleares (4/4): n = 4<br>• Estudios de Soporte Temático Avanzado (3/4): n = 32<br>• Estudios de Soporte Algorítmico y Rendimiento (2/4): n = 48<br>• Estudios de Caracterización y Contexto (1/4): n = 26"]
    end
```

### Protocolo de cribado y control de sesgos:

1. **Deduplicación automatizada:** Se identificaron y eliminaron **85 registros duplicados** entre Scopus y Web of Science mediante coincidencia exacta de DOI y normalización de cadenas de títulos, archivados en `project/metodologia/outputs/corpus_duplicates_removed.csv`.
2. **Cribado por título y resumen (Fase 2):** Se evaluaron los 875 registros únicos contrastando títulos, resúmenes y palabras clave frente a los criterios `IN4` y `EX1–EX4`, descartando 745 registros no pertinentes (`EX4 = 680` artículos de OCR general sin foco empresarial o dominios biomédicos; `EX-n = 65` registros sin aporte a las preguntas PI).
3. **Evaluación de Elegibilidad a texto completo (Fase 3):** Se leyeron a fondo 130 estudios preseleccionados, descartando 20 artículos con causas trazables (`EX3 = 8`, `EX-n = 7`, `EX2 = 5`).
4. **Evaluación de Calidad Metodológica (QA):** Se aplicó la escala de Kitchenham (`QA1` a `QA5`) sobre los 110 estudios incluidos (`project/metodologia/outputs/corpus_included_final.csv`), identificando exactamente **4 estudios nucleares (4/4)** como pilares para la discusión y síntesis profunda.

---

## 10. Paso 10 — Tabla de mapeo artículo × pregunta y alerta de ineditud

### 10.1. Matriz de trazabilidad (Mapeo de estudios nucleares y representativos del corpus)

Cada artículo del corpus final se valida contra las cuatro preguntas de investigación temáticas para clasificar los aportes empíricos:

| Código | Referencia bibliográfica | PI1 (Arquitecturas IA) | PI2 (Métricas/Rendimiento) | PI3 (Comparación vs Tradicional) | PI4 (Tipologías/ERP) | Total preguntas | Clasificación del estudio | Base de datos / DOI |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **[S001]** | *Wei et al. (2020)* | ✔ | ✔ | ✔ | ✔ | 4/4 | **Estudio nuclear** | Scopus / `10.1145/3397271.3401442` |
| **[S002]** | *Hwang et al. (2021)* | ✔ | ✔ | ✔ | ✔ | 4/4 | **Estudio nuclear** | Scopus / `10.18653/v1/2021.findings-acl.28` |
| **[S003]** | *Devadarshini & Karthikeyan (2025)* | ✔ | ✔ | ✔ | ✔ | 4/4 | **Estudio nuclear** | Scopus / `10.1109/icngcs64900.2025.11182987` |
| **[S004]** | *Kirsch et al. (2025)* | ✔ | ✔ | ✔ | ✔ | 4/4 | **Estudio nuclear** | WoS / `10.1007/978-3-031-82484-5_7` |
| **[S005]** | *Yu et al. (2025)* | ✔ | ✔ | — | ✔ | 3/4 | **Soporte temático** | Scopus / `10.3390/electronics14091717` |
| **[S006]** | *Mifsud et al. (2025)* | ✔ | ✔ | — | ✔ | 3/4 | **Soporte temático** | Scopus / `10.3390/make7040167` |
| **[S007]** | *Shanthi et al. (2025)* | ✔ | ✔ | — | ✔ | 3/4 | **Soporte temático** | Scopus / `10.1109/icriset64803.2025.11252218` |
| **[S010]** | *Jena et al. (2023)* | ✔ | ✔ | — | ✔ | 3/4 | **Soporte temático** | Scopus / `10.1109/CICT59886.2023.10455123` |
| **[S037]** | *Sara et al. (2022)* | ✔ | ✔ | — | — | 2/4 | **Soporte algorítmico** | Scopus / `10.1109/TPAMI.2022.3184920` |
| **[S050]** | *Lee et al. (2024)* | ✔ | — | — | ✔ | 2/4 | **Soporte validación/ERP** | WoS / `10.1016/j.sysarc.2024.103120` |
| **[S085]** | *Alla (2025)* | — | — | — | ✔ | 1/4 | **Caracterización/ERP** | Scopus / `10.1109/icaiqsa67794.2025.11440602` |
| **[S090]** | *Cho et al. (2023)* | — | ✔ | — | — | 1/4 | **Caracterización métricas** | WoS / `10.1016/j.cviu.2023.103789` |

* **Estudios Nucleares (4/4 - Total: 4 estudios):** Abordan simultáneamente arquitectura de IA profunda, métricas cuantitativas completas, comparación frente a métodos tradicionales/reglas y aplicación en facturas, recibos o flujos empresariales.
* **Estudios de Soporte Temático Avanzado (3/4 - Total: 32 estudios):** Aportan evidencia empírica en tres dimensiones (ej. modelo + métricas + flujos de facturación).
* **Estudios de Soporte Algorítmico y Rendimiento (2/4 - Total: 48 estudios):** Profundizan en el diseño de modelos neuronales (PI1+PI2) o validación en plataformas ERP (PI1+PI4).
* **Estudios de Caracterización y Contexto (1/4 - Total: 26 estudios):** Aportan tipologías de documentos o benchmarks de plataformas de automatización.
* **Corpus maestro completo:** El mapeo exhaustivo de los 110 estudios incluidos se encuentra documentado en el dataset reproducible [`project/metodologia/outputs/corpus_included_final.csv`](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/metodologia/outputs/corpus_included_final.csv).

### 10.2. Paso 10-bis: Protocolo ante la Alerta de Ineditud

Si durante el cribado se detecta un artículo que responde íntegramente a las 4 preguntas de investigación:

1. **Si es un estudio primario:** Se valida como _estudio nuclear_ (los 4 estudios nucleares identificados en la tabla son estudios primarios empíricos que validan arquitecturas específicas).
2. **Si es una revisión sistemática previa (RSL o Survey):** Se activa la **alerta de ineditud**. Se analiza su ventana temporal y taxonomía para diferenciar formalmente la presente RSL como un avance que cubre una brecha no resuelta (ej. incorporación de modelos multimodales recientes post-2023 o foco específico en ERP corporativos).

---

## 11. Paso 11 — Enlace de cada pregunta con la sección de Resultados

Para garantizar la coherencia estricta de la RSL, **cada pregunta (PI y PD) se responde de manera explícita en la sección de Resultados** con sustento cuantitativo, tabla y gráfico propios:

| Pregunta | Contenido temático a responder en Resultados                                        | Tabla de evidencia asociada                                                                 | Gráfico cuantitativo asociado                                                 |
| :------: | :---------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------- |
| **PD1**  | Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales.       | Tabla de distribución de frecuencia de artículos por año (2020–2025).                       | Gráfico de líneas / barras de tendencia temporal.                             |
| **PD2**  | Productividad académica por autor, revista/conferencia indexada y país de origen.   | Ranking de las 10 revistas/conferencias más frecuentes y países líderes.                    | Gráfico de barras horizontales / mapa coroplético de distribución geográfica. |
| **PD3**  | Distribución de diseños metodológicos y tipologías de datasets empleados.           | Tabla cruzada de diseño del estudio $\times$ tipo de dataset (público vs. empresarial).     | Gráfico circular o de barras apiladas por tipología de validación.            |
| **PI1**  | Taxonomía de enfoques algorítmicos (secuenciales, grafos, LLM multimodales/KIE).    | Matriz de arquitecturas de IA identificadas $\times$ número de estudios.                    | Gráfico de barras por familia algorítmica.                                    |
| **PI2**  | Rendimiento cuantitativo reportado (F1-score, exactitud, reducción de tiempo).      | Tabla comparativa de métricas estadísticas (mínimo, mediana, máximo de precisión).          | Diagrama de caja y bigotes (_boxplot_) o gráfico de dispersión de métricas.   |
| **PI3**  | Comparativa de eficiencia y costo operativo: IA/IDP frente a ingreso manual/reglas. | Tabla de ganancia porcentual en velocidad y tasa de reducción de error operativo.           | Gráfico de barras comparativas (Método tradicional vs. Enfoque IA).           |
| **PI4**  | Tipologías documentales (facturas, recibos, órdenes) y sistemas ERP/CRM integrados. | Tabla de frecuencia por tipo de documento visualmente rico $\times$ plataforma empresarial. | Gráfico de barras agrupadas o matriz de calor (_heatmap_).                    |

---

## 12. Cierre: Cadena de trazabilidad metodológica completa

El flujo metodológico consolidado asegura que cada artículo, cifra y resultado sea completamente auditable bajo la siguiente cadena:

$$\text{Tema} \longrightarrow \text{PICOC} \longrightarrow \text{Pregunta Maestra} \longrightarrow \text{Preguntas (PI + PD)} \longrightarrow \text{Ecuación Booleana} \longrightarrow \text{Criterios IN/EX} \longrightarrow \text{Bitácora de Filtros} \longrightarrow \text{Flujo PRISMA} \longrightarrow \text{Mapeo Artículos} \longrightarrow \text{Resultados (Tablas + Gráficos)}$$
