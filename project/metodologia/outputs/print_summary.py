import pandas as pd
df = pd.read_csv('project/metodologia/outputs/corpus_included_final.csv')
for i, r in df.iterrows():
    print(f"{r['id']} | {r['year']} | {r['classification']} | {r['authors'][:25]} | {r['title'][:60]} | {r['source_db']}")
