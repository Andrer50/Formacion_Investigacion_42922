import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Create figure with ample vertical space
fig, ax = plt.subplots(figsize=(12, 16), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Colors
color_banner = '#f59e0b'
color_phase_bg = '#dbeafe'
color_box_border = '#1e293b'
color_box_fill = '#ffffff'
color_arrow = '#0f172a'

# Title Header
header = patches.FancyBboxPatch((8, 93.5), 84, 4.5, boxstyle="round,pad=0.4", ec="#d97706", fc=color_banner, lw=1.5)
ax.add_patch(header)
ax.text(50, 95.7, "PRISMA 2020 Flow Diagram: Systematic Literature Review", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1e293b')

# Left Phase Banners
phases = [
    ("IDENTIFICATION", 75, 16),
    ("SCREENING", 55, 18),
    ("ELIGIBILITY", 32, 18),
    ("INCLUDED", 2, 26)
]

for name, y_pos, height in phases:
    p_box = patches.FancyBboxPatch((2, y_pos), 5, height, boxstyle="round,pad=0.2", ec="#93c5fd", fc=color_phase_bg, lw=1)
    ax.add_patch(p_box)
    ax.text(4.5, y_pos + height/2, name, ha='center', va='center', rotation=90, fontsize=9.5, fontweight='bold', color='#1e40af')

def draw_box(x, y, w, h, title, lines, align='left', bg=color_box_fill, title_color='#0f172a'):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0.3", ec=color_box_border, fc=bg, lw=1.2)
    ax.add_patch(box)
    
    # Title
    ax.text(x + 1.5 if align=='left' else x + w/2, y + h - 2.0, title, ha=align, va='top', fontsize=9.5, fontweight='bold', color=title_color)
    
    # Content lines
    curr_y = y + h - 4.5
    for line in lines:
        ax.text(x + 1.5 if align=='left' else x + w/2, curr_y, line, ha=align, va='top', fontsize=8.5, color='#334155')
        curr_y -= 2.4

# 1. Identification Phase
draw_box(12, 75, 36, 16, "Records identified from databases:", [
    "• Scopus database (n = 3,270)",
    "• Web of Science Core Coll. (n = 431)",
    "Total raw records identified (n = 3,701)"
])

draw_box(56, 75, 36, 16, "Records removed before screening:", [
    "• Platform automation limits (n = 3,124)",
    "  (Document Type != Article, 2020–2026)",
    "• Duplicate records removed (n = 239)",
    "  (matched by DOI and normalized title)"
])

# Arrow 1: ID -> Dup/Removed
ax.annotate('', xy=(56, 83), xytext=(48, 83), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

# Arrow 2: ID -> Screening
ax.annotate('', xy=(30, 69), xytext=(30, 75), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

# 2. Screening Phase
draw_box(12, 59, 36, 10, "Records screened by title/abstract:", [
    "Unique records assessed (n = 338)"
], align='left')

draw_box(56, 57, 36, 14, "Records excluded in screening (n = 41):", [
    "• EX4 Out of business domain (n = 35)",
    "  (clinical EHR, ancient manuscripts)",
    "• EX-n No relation to PIs (n = 6)"
])

# Arrow 3: Screened -> Excluded
ax.annotate('', xy=(56, 64), xytext=(48, 64), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

# Arrow 4: Screened -> Sought
ax.annotate('', xy=(30, 49), xytext=(30, 59), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

# 3. Retrieval & Eligibility
draw_box(12, 42, 36, 7, "Reports sought for retrieval:", [
    "Full-text pre-selected (n = 297)"
])

draw_box(56, 42, 36, 7, "Reports not retrieved:", [
    "• Reports not retrievable (n = 0)"
])

# Arrow 5: Sought -> Not retrieved
ax.annotate('', xy=(56, 45.5), xytext=(48, 45.5), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

# Arrow 6: Sought -> Eligibility
ax.annotate('', xy=(30, 36), xytext=(30, 42), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

draw_box(12, 22, 36, 14, "Reports assessed for eligibility:", [
    "Full-text articles evaluated (n = 297)",
    "• Quality Assessment QA >= 3.0",
    "• Inter-reviewer agreement (κ = 0.92)"
])

draw_box(56, 20, 36, 18, "Reports excluded at full-text (n = 166):", [
    "• Excluded by AMSTAR 2 item 7 (n = 20):",
    "  - EX3 Secondary surveys/reviews (n = 8)",
    "  - EX-n No quantitative metrics (n = 7)",
    "  - EX2 Not accessible full-text (n = 5)",
    "• EX-n General OCR without biz docs (n = 146)"
])

# Arrow 7: Assessed -> Excluded
ax.annotate('', xy=(56, 29), xytext=(48, 29), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

# Arrow 8: Assessed -> Included
ax.annotate('', xy=(30, 19), xytext=(30, 22), arrowprops=dict(arrowstyle="->", lw=1.5, color=color_arrow))

# 4. Included Phase
draw_box(12, 2, 80, 17, "Primary Studies Included in Systematic Literature Review (N = 131):", [
    "• Flagship Nuclear Studies (4/4 PIs answered): n = 4 (3.1%) [S001, S002, S003, S004]",
    "• Advanced Thematic Support Studies (4/4 & 3/4 PIs): n = 108 (82.4%)",
    "• Algorithmic & Performance Support Studies (2/4 PIs): n = 17 (13.0%)",
    "• Contextual Characterization Studies (1/4 PIs): n = 2 (1.5%)",
    "• 100% Peer-reviewed Journal Articles (0% Conference papers, 0% EEG noise)"
], bg='#f0fdf4', title_color='#065f46')

# Save PNG and SVG with absolute paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_png = os.path.join(base_dir, 'outputs', 'diagrama_flujo_prisma_2020.png')
out_svg = os.path.join(base_dir, 'outputs', 'diagrama_flujo_prisma_2020.svg')
evid_png = os.path.join(base_dir, 'evidencias', 'diagrama_flujo_prisma_2020.png')

os.makedirs(os.path.dirname(out_png), exist_ok=True)
os.makedirs(os.path.dirname(evid_png), exist_ok=True)

plt.savefig(out_png, bbox_inches='tight', dpi=300)
plt.savefig(out_svg, bbox_inches='tight')
plt.savefig(evid_png, bbox_inches='tight', dpi=300)
plt.close()

print("PRISMA diagram generated successfully with clean absolute paths for N=131!")
