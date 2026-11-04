import docx
import re

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

print("=== CHECKING ALL MENTIONS OF 'MODELO' ===")

# Look for sentences where 'modelo' is used in first person or implies the authors created a model
suspicious_model_uses = []

for i, p in enumerate(doc.paragraphs):
    text = p.text
    if 'modelo' in text.lower():
        # split into sentences
        sentences = re.split(r'[.!?]\s+', text)
        for s in sentences:
            if 'modelo' in s.lower():
                s_lower = s.lower()
                # Check for suspicious active verbs or ownership
                if any(k in s_lower for k in [
                    'proponemos', 'propuesto', 'diseñamos', 'entrenamos', 'evaluamos nuestro',
                    'nuestro modelo', 'mi modelo', 'tu modelo', 'su modelo', 'desarrollamos un modelo',
                    'implementamos un modelo', 'este modelo permite', 'presentamos un modelo',
                    'creamos un modelo', 'construimos un modelo', 'en nuestro modelo', 'del modelo que',
                    'según tu', 'según el modelo que', 'para tu modelo'
                ]):
                    suspicious_model_uses.append((f'P{i}', s.strip()))

print(f"Total suspicious 'modelo' sentences found: {len(suspicious_model_uses)}")
for loc, sent in suspicious_model_uses:
    print(f"[{loc}] {sent}\n")

