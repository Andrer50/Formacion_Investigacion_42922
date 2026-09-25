import pandas as pd
import numpy as np
import re
import os

scopus_file = r'project/metodologia/inputs/scopus_export_it2.csv'
wos_file = r'project/metodologia/inputs/wos_export_it2.xls'

# Read files
df_scopus = pd.read_csv(scopus_file, encoding='utf-8')
df_wos = pd.read_excel(wos_file)

# Standardize columns
# Scopus: Title, Abstract, Authors, Year, DOI, Affiliations, Source title, Document Type, EID
scopus_std = pd.DataFrame({
    'source_db': 'Scopus',
    'id': df_scopus['EID'].astype(str) if 'EID' in df_scopus else [f"2-s2.0-{i}" for i in range(len(df_scopus))],
    'authors': df_scopus['Authors'].fillna('') if 'Authors' in df_scopus else '',
    'title': df_scopus['Title'].fillna('') if 'Title' in df_scopus else '',
    'year': df_scopus['Year'].fillna(0).astype(int) if 'Year' in df_scopus else 0,
    'source_title': df_scopus['Source title'].fillna('') if 'Source title' in df_scopus else '',
    'doi': df_scopus['DOI'].fillna('').astype(str).str.strip().str.lower() if 'DOI' in df_scopus else '',
    'abstract': df_scopus['Abstract'].fillna('') if 'Abstract' in df_scopus else '',
    'author_keywords': df_scopus['Author Keywords'].fillna('') if 'Author Keywords' in df_scopus else '',
    'index_keywords': df_scopus['Index Keywords'].fillna('') if 'Index Keywords' in df_scopus else '',
    'affiliations': df_scopus['Affiliations'].fillna('') if 'Affiliations' in df_scopus else '',
    'doc_type': df_scopus['Document Type'].fillna('') if 'Document Type' in df_scopus else ''
})

# WoS: Article Title, Abstract, Authors, Publication Year, DOI, Affiliations, Source Title, Document Type, UT (Unique WOS ID)
wos_std = pd.DataFrame({
    'source_db': 'Web of Science',
    'id': df_wos['UT (Unique WOS ID)'].astype(str) if 'UT (Unique WOS ID)' in df_wos else [f"WOS:{i}" for i in range(len(df_wos))],
    'authors': df_wos['Authors'].fillna('') if 'Authors' in df_wos else '',
    'title': df_wos['Article Title'].fillna('') if 'Article Title' in df_wos else '',
    'year': df_wos['Publication Year'].fillna(0).astype(int) if 'Publication Year' in df_wos else 0,
    'source_title': df_wos['Source Title'].fillna('') if 'Source Title' in df_wos else '',
    'doi': df_wos['DOI'].fillna('').astype(str).str.strip().str.lower() if 'DOI' in df_wos else '',
    'abstract': df_wos['Abstract'].fillna('') if 'Abstract' in df_wos else '',
    'author_keywords': df_wos['Author Keywords'].fillna('') if 'Author Keywords' in df_wos else '',
    'index_keywords': df_wos['Keywords Plus'].fillna('') if 'Keywords Plus' in df_wos else '',
    'affiliations': df_wos['Affiliations'].fillna('') if 'Affiliations' in df_wos else '',
    'doc_type': df_wos['Document Type'].fillna('') if 'Document Type' in df_wos else ''
})

# Clean DOIs: remove https://doi.org/, http://dx.doi.org/, spaces
def clean_doi(d):
    if not d or d == 'nan':
        return ''
    d = re.sub(r'^https?://(dx\.)?doi\.org/', '', d).strip().lower()
    return d

scopus_std['clean_doi'] = scopus_std['doi'].apply(clean_doi)
wos_std['clean_doi'] = wos_std['doi'].apply(clean_doi)

def clean_title(t):
    if not t:
        return ''
    t = t.lower()
    t = re.sub(r'[^a-z0-9]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

scopus_std['clean_title'] = scopus_std['title'].apply(clean_title)
wos_std['clean_title'] = wos_std['title'].apply(clean_title)

print(f"Scopus raw count: {len(scopus_std)}")
print(f"WoS raw count: {len(wos_std)}")
total_raw = len(scopus_std) + len(wos_std)
print(f"Total raw records: {total_raw}")

# Deduplication
# 1. Combine
combined = pd.concat([scopus_std, wos_std], ignore_index=True)

# Find duplicates
# Match by clean_doi (if not empty) or clean_title (if title length > 15)
duplicates = []
unique_records = []
seen_dois = {}
seen_titles = {}

for idx, row in combined.iterrows():
    doi = row['clean_doi']
    title = row['clean_title']
    
    is_dup = False
    dup_reason = ''
    matched_to = ''
    
    if doi and doi in seen_dois:
        is_dup = True
        dup_reason = f"Duplicate DOI: {doi}"
        matched_to = seen_dois[doi]
    elif len(title) > 20 and title in seen_titles:
        is_dup = True
        dup_reason = f"Duplicate Title: {title[:40]}..."
        matched_to = seen_titles[title]
        
    if is_dup:
        duplicates.append({
            'idx': idx,
            'source_db': row['source_db'],
            'title': row['title'],
            'doi': row['doi'],
            'matched_to_db': matched_to['source_db'],
            'matched_to_title': matched_to['title'],
            'reason': dup_reason
        })
    else:
        if doi:
            seen_dois[doi] = row
        if len(title) > 20:
            seen_titles[title] = row
        unique_records.append(row)

df_unique = pd.DataFrame(unique_records)
df_dups = pd.DataFrame(duplicates)

print(f"Duplicates removed: {len(df_dups)}")
print(f"Unique records for Screening: {len(df_unique)}")

# Screening against PI1-PI4 and EX
# Terms regex
pi1_pattern = r'\b(transformer|layoutlm|layoutlmv\d|bert|roberta|deep learning|neural network|cnn|rnn|lstm|graph|gnn|gcn|yolo|ocr|large language model|llm|gpt|vision transformer|vit|multimodal|donut|tesseract|crnn|rule-based|template|kie|key information extraction|document ai|idp|deep neural|spatial|visual features|word embedding|bimodal|multimodal)\b'
pi2_pattern = r'\b(f1|f-score|f-measure|accuracy|precision|recall|exactness|map|iou|bleu|rouge|cer|wer|processing time|execution time|latency|throughput|speed|response time|seconds|fps|performance|evaluated|outperforms|benchmark|character error rate|word error rate)\b'
pi3_pattern = r'\b(manual|human|traditional|baseline|compared to|comparison|versus|vs\.|conventional|rule-based|state-of-the-art|sota|previous method|existing method|workload reduction|error reduction|cost reduction|labor|saving|benchmark comparison)\b'
pi4_pattern = r'\b(invoice|receipt|bill|voucher|form|purchase order|contract|financial document|administrative document|business document|tax|statement|check|cheque|shipping|erp|crm|sap|business process|workflow|enterprise|accounting|supply chain|funsd|cord|sroie|rvl-cdip|docbank|docvqa|semi-structured|visually rich document|vrd)\b'

ex4_medical = r'\b(electronic health records|clinical notes|ehr|radiology|patient|hospital|medical record|dna|biomedical|pathology|x-ray|computed tomography|clinical trial|cardiovascular|ophthalmology)\b'
ex4_plates = r'\b(license plate|vehicle plate|car plate|traffic monitoring|license-plate)\b'
ex4_ancient = r'\b(ancient manuscript|medieval|historical archive|paleography|historical handwriting)\b'

def screen_record(row):
    text = f"{row['title']} {row['abstract']} {row['author_keywords']} {row['index_keywords']}".lower()
    
    # Check EX4 (out of scope)
    # Only exclude if strongly medical/plates/ancient AND lacks business/invoice terms
    is_medical = bool(re.search(ex4_medical, text))
    is_plates = bool(re.search(ex4_plates, text))
    is_ancient = bool(re.search(ex4_ancient, text))
    has_business = bool(re.search(r'\b(invoice|receipt|business|financial|accounting|erp|purchase order|form|office|tax)\b', text))
    
    if (is_medical or is_plates or is_ancient) and not has_business:
        return {
            'PI1': False, 'PI2': False, 'PI3': False, 'PI4': False,
            'total_pi': 0,
            'status': 'Excluded',
            'exclusion_code': 'EX4',
            'exclusion_reason': 'Out of scope domain (medical/traffic/ancient without enterprise focus)',
            'classification': 'Excluido (EX4)'
        }
    
    # Evaluate PIs
    c_pi1 = bool(re.search(pi1_pattern, text))
    c_pi2 = bool(re.search(pi2_pattern, text))
    c_pi3 = bool(re.search(pi3_pattern, text))
    c_pi4 = bool(re.search(pi4_pattern, text))
    
    tot = sum([c_pi1, c_pi2, c_pi3, c_pi4])
    
    if tot == 0:
        return {
            'PI1': False, 'PI2': False, 'PI3': False, 'PI4': False,
            'total_pi': 0,
            'status': 'Excluded',
            'exclusion_code': 'EX-n',
            'exclusion_reason': 'Does not answer any research question (PI1-PI4)',
            'classification': 'Excluido (EX-n)'
        }
    
    classification = 'Estudio de caracterización'
    if tot == 4:
        classification = 'Estudio nuclear (4/4)'
    elif tot == 3:
        classification = 'Estudio de soporte temático (3/4)'
    elif tot == 2:
        classification = 'Estudio de soporte temático (2/4)'
    elif tot == 1:
        classification = 'Estudio de caracterización (1/4)'
        
    return {
        'PI1': c_pi1, 'PI2': c_pi2, 'PI3': c_pi3, 'PI4': c_pi4,
        'total_pi': tot,
        'status': 'Included',
        'exclusion_code': '',
        'exclusion_reason': '',
        'classification': classification
    }

screening_results = df_unique.apply(screen_record, axis=1, result_type='expand')
df_screened = pd.concat([df_unique.reset_index(drop=True), screening_results.reset_index(drop=True)], axis=1)

print("\n--- SCREENING SUMMARY ---")
print(df_screened['status'].value_counts())
print("\n--- CLASSIFICATION BREAKDOWN ---")
print(df_screened['classification'].value_counts())
print("\n--- EXCLUSION REASONS ---")
print(df_screened[df_screened['status'] == 'Excluded']['exclusion_code'].value_counts())

# Save outputs
os.makedirs('project/metodologia/outputs', exist_ok=True)
df_screened.to_csv('project/metodologia/outputs/corpus_screened_master.csv', index=False, encoding='utf-8')
df_dups.to_csv('project/metodologia/outputs/corpus_duplicates_removed.csv', index=False, encoding='utf-8')

# Included only
df_included = df_screened[df_screened['status'] == 'Included'].copy()
df_included['study_id'] = [f"[S{i+1:02d}]" for i in range(len(df_included))]
df_included.to_csv('project/metodologia/outputs/corpus_included_final.csv', index=False, encoding='utf-8')

print(f"\nFinal Included Studies: {len(df_included)}")
print(f"Nucleares (4/4): {len(df_included[df_included['total_pi'] == 4])}")
print(f"Soporte (3/4): {len(df_included[df_included['total_pi'] == 3])}")
print(f"Soporte (2/4): {len(df_included[df_included['total_pi'] == 2])}")
print(f"Caracterización (1/4): {len(df_included[df_included['total_pi'] == 1])}")
