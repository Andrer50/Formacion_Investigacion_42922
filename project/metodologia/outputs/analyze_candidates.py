import pandas as pd
import json
import re

# Load screened master
df = pd.read_csv('project/metodologia/outputs/corpus_screened_master.csv')

print(f"Total screened master: {len(df)}")

# Filter out obvious non-business / medical / handwritten ancient documents
exclude_terms = ['covid', 'medical', 'clinical', 'patient', 'hospital', 'ancient', 'historical manuscript', 'music', 'biomedical', 'e-government', 'smart city']
pattern_exclude = '|'.join(exclude_terms)

valid = df[~df['title'].str.contains(pattern_exclude, case=False, na=False) & 
           ~df['abstract'].str.contains(pattern_exclude, case=False, na=False)].copy()

print(f"Valid after domain exclusion: {len(valid)}")

# Let's find candidate papers with high relevance to invoices, receipts, financial/business docs, IDP, KIE, ERP
def score_relevance(row):
    score = 0
    t = (str(row['title']) + " " + str(row['abstract']) + " " + str(row['author_keywords'])).lower()
    
    # Core domain terms
    if any(k in t for k in ['invoice', 'receipt', 'purchase order', 'bill of lading', 'financial document', 'vat invoice', 'business document', 'business workflow', 'erp', 'accounting']):
        score += 4
    if any(k in t for k in ['layoutlm', 'multimodal', 'key information extraction', 'kie', 'intelligent document processing', 'idp', 'table structure recognition', 'document ai', 'form understanding', 'graph neural network', 'spatial dependency']):
        score += 3
    if any(k in t for k in ['f1-score', 'f1 score', 'precision', 'recall', 'accuracy', 'latency', 'runtime', 'benchmark']):
        score += 2
    if any(k in t for k in ['baseline', 'traditional', 'rule-based', 'manual', 'comparison', 'outperform', 'error reduction']):
        score += 2
    if str(row['doi']).startswith('10.'):
        score += 1
    return score

valid['relevance_score'] = valid.apply(score_relevance, axis=1)
valid = valid.sort_values(by=['relevance_score', 'year'], ascending=[False, False]).reset_index(drop=True)

print("Top 15 candidates:")
for i, r in valid.head(15).iterrows():
    print(f"{i+1}. Score {r['relevance_score']} | [{r['source_db']}] {r['authors']} ({r['year']}) - {r['title'][:70]}")
    print(f"   DOI: {r['doi']}")
