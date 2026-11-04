import docx
doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')
t = doc.paragraphs[137].text
print("repr(t[:20]):", repr(t[:20]))
print("chars:", [ord(c) for c in t[:15]])
print("target chars:", [ord(c) for c in "1) Apertura:"])
print("matches:", t.startswith("1) Apertura:"))

