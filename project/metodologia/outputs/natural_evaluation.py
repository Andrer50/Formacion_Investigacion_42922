import sys
import io
import pandas as pd
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cargar el corpus exportado de Scopus y WoS
df_master = pd.read_csv('project/metodologia/outputs/corpus_screened_master.csv')

# Excluir dominios ajenos (médico, manuscritos antiguos, etc.)
exclude_terms = ['covid', 'medical', 'clinical', 'patient', 'hospital', 'ancient', 'historical manuscript', 'music', 'biomedical', 'e-government', 'smart city']
pattern_exclude = '|'.join(exclude_terms)

valid = df_master[
    (df_master['year'] >= 2020) & (df_master['year'] <= 2025) &
    ~df_master['title'].str.contains(pattern_exclude, case=False, na=False) & 
    ~df_master['abstract'].str.contains(pattern_exclude, case=False, na=False)
].copy()

print(f"Total registros únicos válidos en el dominio empresarial (2020-2025): {len(valid)}\n")

# Criterios naturales estrictos:
# PI1: Propuesta o uso de arquitectura de IA / Deep Learning / Transformers / IDP / Multimodal
def check_pi1(text):
    keywords = [
        'neural network', 'deep learning', 'transformer', 'layoutlm', 'multimodal', 
        'graph neural', 'gnn', 'convolutional', 'cnn', 'donut', 'nougat', 
        'large language model', 'llm', 'vision-language', 'vdu', 'kie', 'intelligent document processing'
    ]
    return 1 if any(k in text for k in keywords) else 0

# PI2: Métricas cuantitativas explícitas reportadas
def check_pi2(text):
    keywords = [
        'f1-score', 'f1 score', 'f1 of', 'f1 reaches', 'precision of', 'recall of', 
        'accuracy of', 'accuracy rate', 'error rate', 'latency', 'execution time', 'reduction in time',
        'percent', '%', 'benchmark', 'evaluated on'
    ]
    return 1 if any(k in text for k in keywords) else 0

# PI3: Comparación directa y explícita frente a métodos tradicionales / reglas / digitación manual
def check_pi3(text):
    # Debe haber una mención explícita a la comparación con métodos tradicionales, reglas o manual
    keywords = [
        'compared with traditional', 'compared to traditional', 'outperforms traditional',
        'versus traditional', 'vs traditional', 'traditional rule-based', 'traditional ocr',
        'manual processing', 'manual data entry', 'manual labor', 'manual effort',
        'rule-based baseline', 'traditional baseline', 'conventional method', 'conventional ocr',
        'existing rule-based', 'handcrafted rules', 'template matching'
    ]
    return 1 if any(k in text for k in keywords) else 0

# PI4: Aplicación a documentos empresariales específicos (facturas, recibos, órdenes, ERP)
def check_pi4(text):
    keywords = [
        'invoice', 'invoices', 'receipt', 'receipts', 'purchase order', 'bill of lading', 
        'vat invoice', 'financial document', 'commercial invoice', 'business expense', 
        'erp', 'accounting system', 'enterprise workflow', 'corporate document'
    ]
    return 1 if any(k in text for k in keywords) else 0

results = []
for idx, r in valid.iterrows():
    full_text = (str(r['title']) + " " + str(r['abstract']) + " " + str(r['author_keywords'])).lower()
    p1 = check_pi1(full_text)
    p2 = check_pi2(full_text)
    p3 = check_pi3(full_text)
    p4 = check_pi4(full_text)
    total = p1 + p2 + p3 + p4
    
    results.append({
        'authors': r['authors'],
        'year': r['year'],
        'title': r['title'],
        'source_db': r['source_db'],
        'doi': r['doi'],
        'PI1': p1,
        'PI2': p2,
        'PI3': p3,
        'PI4': p4,
        'total_pi': total
    })

df_eval = pd.DataFrame(results)

print("DISTRIBUCIÓN NATURAL DE CHECKS (Evaluación Semántica Estricta):")
print(df_eval['total_pi'].value_counts().sort_index(ascending=False))

print("\n-------------------------------------------------------------")
print("ARTÍCULOS QUE CUMPLEN NATURALMENTE CON 4/4 (Estudios Nucleares):")
nucleares_naturales = df_eval[df_eval['total_pi'] == 4]
print(f"Total identificados naturalmente: {len(nucleares_naturales)}\n")

for i, r in nucleares_naturales.iterrows():
    print(f"• [{r['source_db']}] {r['authors']} ({r['year']})")
    print(f"  Título: {r['title']}")
    print(f"  DOI: {r['doi']}")
    print()
