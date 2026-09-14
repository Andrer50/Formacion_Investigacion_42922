# Metodología: formulación del marco PICO y estrategia de búsqueda

## 1. Delimitación del estudio

El presente avance corresponde a la formulación metodológica de una revisión sistemática de la literatura sobre el uso de la Inteligencia Artificial (IA) y el Procesamiento Inteligente de Documentos (IDP) en la automatización del registro y la validación de documentos empresariales.

El estudio se delimita a **sistemas de información empresariales y flujos internos de registro documental estrictamente privados**. En consecuencia, no se consideran como población principal los sistemas gubernamentales, los servicios públicos ni los flujos documentales dirigidos directamente a usuarios externos.

La pregunta maestra de la revisión se formula de la siguiente manera:

> **¿Cuál es el impacto de la Inteligencia Artificial (IA) en la automatización de procesos y la reducción de la carga operativa frente al ingreso manual de datos en el área de registro y validación documental de sistemas empresariales?**

## 2. Marco PICO

El marco PICO permite organizar la pregunta general en cuatro componentes y mantener la trazabilidad entre el problema de investigación, las subpreguntas, los términos de búsqueda y la síntesis de resultados.

| Componente | Definición para esta revisión |
| --- | --- |
| **P: Población / Contexto** | Sistemas de información empresariales y flujos de trabajo de registro documental estrictamente privados. |
| **I: Intervención** | Integración de arquitecturas de Inteligencia Artificial y Procesamiento Inteligente de Documentos (IDP / IA-OCR), incluida la extracción de información. |
| **C: Comparación** | Ingreso manual de datos o procesamiento tradicional sin integración de IA. |
| **O: Outcome / Resultado** | Nivel de automatización, reducción de la carga operativa y eficiencia, considerando también precisión y velocidad. |

## 3. Subpreguntas de investigación

Cada subpregunta corresponde a un componente específico del marco PICO. Esta relación permite identificar qué evidencia debe extraerse de cada estudio y cómo se organizarán los resultados de la revisión.

| Código | Componente | Subpregunta |
| --- | --- | --- |
| **SP-P** | **Población / Contexto** | **¿Qué desafíos operativos enfrentan actualmente los sistemas de información empresariales en sus flujos internos de registro y validación documental?** |
| **SP-I** | **Intervención** | **¿Cómo influye la integración de arquitecturas de Inteligencia Artificial y Procesamiento Inteligente de Documentos en los flujos de extracción de datos semiestructurados?** |
| **SP-C** | **Comparación** | **¿Cómo se compara el desempeño de la automatización documental mediante IA frente al ingreso manual de datos tradicional en términos de precisión y velocidad?** |
| **SP-O** | **Resultados** | **¿Qué efecto tienen estas tecnologías en la reducción de la carga operativa y la optimización de la eficiencia para los trabajadores internos de la empresa?** |

### 3.1. Trazabilidad entre PICO y resultados

La presentación de los resultados se organizará según los códigos de las subpreguntas. Cada estudio incluido deberá indicar a cuál o cuáles de ellas aporta evidencia.

| Componente | Evidencia que se debe extraer | Organización de resultados |
| --- | --- | --- |
| **P** | Tipo de empresa, sistema de información, documento y flujo interno analizado; además de los desafíos operativos identificados. | Respuesta a **SP-P**. |
| **I** | Técnica de IA o IDP utilizada, arquitectura, etapa de extracción y tipo de dato semiestructurado procesado. | Respuesta a **SP-I**. |
| **C** | Método manual o tradicional empleado como referencia y condiciones de comparación. | Respuesta a **SP-C**. |
| **O** | Métricas de automatización, precisión, velocidad, carga operativa y eficiencia. | Respuesta a **SP-O**. |

## 4. Términos de búsqueda

Para consultar bases de datos indexadas como Scopus y Web of Science, los términos derivados del marco PICO se expresan en inglés. Dentro de cada bloque, los sinónimos se combinan mediante el operador booleano `OR`.

| Bloque | Componente PICO | Términos en inglés |
| --- | --- | --- |
| **P** | Contexto | `"enterprise information systems"` OR `"document management"` OR `"business workflows"` |
| **I** | Tecnología | `"artificial intelligence"` OR `"intelligent document processing"` OR `"optical character recognition"` OR `"information extraction"` |
| **C** | Comparación | `"manual data entry"` OR `"manual processing"` OR `"traditional processing"` |
| **O** | Resultados | `"automation"` OR `"workload reduction"` OR `"efficiency"` OR `"operational load"` |

## 5. Ecuación de búsqueda principal

Los cuatro bloques se unen con el operador `AND`, mientras que los términos equivalentes de cada componente se unen con `OR`. La ecuación contiene más de tres operadores booleanos y puede adaptarse a la sintaxis específica de cada base de datos.

```text
("enterprise information systems" OR "document management" OR "business workflows") AND ("artificial intelligence" OR "intelligent document processing" OR "optical character recognition" OR "information extraction") AND ("manual data entry" OR "manual processing" OR "traditional processing") AND ("automation" OR "workload reduction" OR "efficiency" OR "operational load")
```

### 5.1. Adaptación a bases de datos

Para Scopus, la ecuación puede ejecutarse dentro de los campos de título, resumen y palabras clave mediante `TITLE-ABS-KEY(...)`. Para Web of Science, puede utilizarse el campo de tema mediante `TS=(...)`.

**Scopus**

```text
TITLE-ABS-KEY(("enterprise information systems" OR "document management" OR "business workflows") AND ("artificial intelligence" OR "intelligent document processing" OR "optical character recognition" OR "information extraction") AND ("manual data entry" OR "manual processing" OR "traditional processing") AND ("automation" OR "workload reduction" OR "efficiency" OR "operational load"))
```

**Web of Science**

```text
TS=(("enterprise information systems" OR "document management" OR "business workflows") AND ("artificial intelligence" OR "intelligent document processing" OR "optical character recognition" OR "information extraction") AND ("manual data entry" OR "manual processing" OR "traditional processing") AND ("automation" OR "workload reduction" OR "efficiency" OR "operational load"))
```

## 6. Registro de búsqueda y reproducibilidad

Cada ejecución de la ecuación deberá registrarse para garantizar que la búsqueda pueda ser revisada y replicada. Como mínimo, se documentarán la base consultada, la fecha, la ecuación exacta y la cantidad de resultados obtenidos.

| Base de datos | Fecha de ejecución | Ecuación aplicada | Resultados brutos | Resultados tras filtros | Archivo o evidencia |
| --- | --- | --- | ---: | ---: | --- |
| Scopus | Pendiente | Ecuación principal adaptada a `TITLE-ABS-KEY` | Pendiente | Pendiente | Captura y exportación `.ris` / `.bib` |
| Web of Science | Pendiente | Ecuación principal adaptada a `TS` | Pendiente | Pendiente | Captura y exportación `.ris` / `.bib` |

Los valores marcados como **Pendiente** se completarán después de ejecutar la búsqueda en cada base. En la etapa de selección, los estudios se clasificarán según la subpregunta PICO a la que aporten evidencia.
