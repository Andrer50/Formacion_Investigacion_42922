import docx
import re

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

print("=== CHECKING FOR 1ST PERSON SINGULAR AND 2ND PERSON ===")

# Words that indicate 1st person singular or 2nd person conversational text
triggers = [
    r'\byo\b', r'\bme\b', r'\bmi\b', r'\bmis\b', r'\bmío\b', r'\bmía\b',
    r'\btú\b', r'\btu\b', r'\btus\b', r'\bte\b', r'\bti\b',
    r'\busted\b', r'\bustedes\b',
    r'\bdiapositiva\b', r'\bppt\b', r'\bpresentaci[oó]n\b',
    r'\bsemana\b', r'\bclase\b', r'\bsesi[oó]n\b', r'\bchat\b',
    r'\bprompt\b', r'según tu', r'tu modelo', r'mi modelo'
]

compiled = re.compile('|'.join(triggers), re.IGNORECASE)

found_issues = []

for i, p in enumerate(doc.paragraphs):
    text = p.text
    matches = list(compiled.finditer(text))
    for m in matches:
        word = m.group(0).lower()
        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 30)
        snippet = text[start:end].replace('\n', ' ')
        
        # Filter out valid academic occurrences
        # e.g., 'me' inside other words? We used \bme\b. But 'me' in spanish: 'se me'? Or 'me' as pronoun?
        # e.g. 'mi' in spanish: 'mi' (note of music or pronoun).
        # e.g. 'prompt engineering'
        # e.g. 'representación' (regex has \bpresentaci[oó]n\b so it won't match representación)
        found_issues.append((i, word, snippet, p.text))

print(f"Total potential occurrences found: {len(found_issues)}")
for i, word, snippet, full_p in found_issues:
    print(f"P{i} [Trigger: {word}]: ...{snippet}...")

