# Notas de integridad del corpus (resolver antes de entregar)
1. `generate_corpus_110.py` asigna PI1–PI4 de 106 estudios por posición/módulo, y las descripciones son genéricas. No se usaron.
2. Las descripciones de los 4 nucleares están escritas a mano (p. ej. "LayoutLM adaptado", F1 94,8 %, 78 %) sin respaldo; Wei et al. usa RoBERTa+GCN.
3. Kappa 0,86/0,91 y QA 4,12 solo existen como texto en los scripts de metodología.
4. PRISMA (745 excluidos en cribado) no coincide con `corpus_screened_master.csv` (859 Included / 16 Excluded).
5. ~23 estudios posiblemente fuera de dominio (EEG "ERP", vacunación, etc.): ver `outputs/alerta_pertinencia.csv`.
6. Corpus elegido por puntaje de palabras clave y luego por año → 2025 = 68 estudios; la distribución anual no mide el campo.
7. Países solo de WoS (55 estudios). 8. Codificación automática por resumen; S001, S003, S004 sin resumen.
9. El borrador (grafos "predominantes antes de 2021", multimodal "emergente") no se sostiene con n = 12 en 2020–2022.
10. Muestra del 20 % (n=22): 12 estudios (55 %) son de otro dominio según lectura manual. Un filtro estricto (≥ 2 términos documentales) coincidió 22/22 y deja 75 de 110 en dominio; de los 866 únicos 2020-2025 del cribado, 520 lo cumplen → se puede reconstruir un corpus ≥ 80 estudios en dominio (decisión del equipo; actualizar PRISMA).
11. κ manual vs automática (estudios en dominio, n=10): enfoque 0,85 (aceptable); tipología 0,38 y base de validación 0,17 (< 0,60: requieren codificación manual completa). La codificación manual de la muestra la hizo Claude; deben verificarla y, idealmente, que dos humanos codifiquen (columnas A_ y B_) y correr 03_muestra_kappa.py calcular.
12. GRADE-CERQual (Tabla IX) es una calificación propuesta; deben consensuarla.
