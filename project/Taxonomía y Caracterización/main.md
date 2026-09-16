# III. Taxonomía y Caracterización

Tal como se anuncia en la introducción, esta sección presenta la caracterización general de las propuestas de Inteligencia Artificial identificadas para la automatización del registro y la validación documental en sistemas empresariales, clasificándolas según dos ejes: sus **enfoques algorítmicos** y sus **inputs de datos**. Este esquema es el que permitirá, en la Sección II (extracción de datos) y en la Sección IV (Análisis de Brechas), determinar qué arquitecturas —basadas en secuencias, en grafos o en modelos multimodales masivos— resultan más adecuadas para cada tipología documental [1], [5].

**A. Enfoques algorítmicos**

Siguiendo la evolución descrita en la literatura, los enfoques se ordenan en un continuo de madurez técnica [1], [2]:

- **Basados en reglas y plantillas (OCR tradicional)**: dependen de layouts estáticos predefinidos; son la causa principal de los cuellos de botella, costos y errores operativos señalados en la introducción [2].
- **Basados en secuencias**: representan el documento como una cadena de tokens con embeddings posicionales; paradigma dominante desde 2021 [1].
- **Basados en grafos**: modelan el documento como nodos y aristas espaciales entre palabras o segmentos; predominantes antes de 2021, útiles ante layouts muy irregulares [1].
- **Multimodales / generativos (LLM)**: fusionan texto, layout e imagen en un solo modelo, con salidas de texto libre; categoría emergente que habilita KIE sin plantillas rígidas [1].

**B. Inputs de datos**

En paralelo, cada propuesta se caracteriza según las modalidades de entrada que combina —texto, posición/layout y visual, más características hechas a mano en los enfoques más antiguos [1]— y según el tipo de documento visualmente rico (VRD) sobre el que se valida: facturas, recibos, formularios o contratos [2], [3]. Esta segunda variable es la que evidencia si el estudio se probó sobre benchmarks públicos controlados (p. ej. FUNSD, CORD, SROIE) o sobre datos de un flujo empresarial real (ERP/CRM), distinción central para responder la subpregunta SP-P del presente estudio.

La Tabla I resume ambos ejes y sirve como formulario de codificación para el cribado a texto completo de los estudios primarios.

**TABLA I. Caracterización de los estudios primarios**

| Eje | Categorías | Evidencia a extraer |
|---|---|---|
| Enfoque algorítmico | Reglas/plantillas · Secuencial · Grafo · Multimodal/generativo | Arquitectura o modelo empleado y año de publicación |
| Inputs de datos | Textual · Layout · Visual · Hand-crafted | Modalidades fusionadas y mecanismo de integración |
| Tipología documental | Facturas · Recibos · Formularios · Contratos | Tipo de documento y sistema empresarial (ERP/CRM) asociado |
| Base de validación | Benchmark público · Dataset privado/empresarial | Dataset usado y métrica reportada (F1, precisión, recall) |
