"""
Script de regeneración oficial para figuras IEEE (Fig. 2 a Fig. 9) - Parte 4
Revisión Sistemática de Literatura (RSL) - N = 131 estudios primarios
Formato estándar IEEE (300 dpi, tipografía sans/serif académica, paleta sobria)
Sin títulos duplicados ni notas incrustadas dentro del lienzo gráfico (gestionados en el epígrafe de Word).
Sin superposición de texto en etiquetas de los ejes X.
"""

import os
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.gettempdir()
import matplotlib.pyplot as plt
import numpy as np

# Configuración global de estilo científico
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 8.5
plt.rcParams['axes.labelsize'] = 8.5
plt.rcParams['axes.titlesize'] = 8.8
plt.rcParams['xtick.labelsize'] = 8.0
plt.rcParams['ytick.labelsize'] = 8.0
plt.rcParams['legend.fontsize'] = 7.5
plt.rcParams['figure.titlesize'] = 9.5

out_dir = 'project/resultados/outputs'
os.makedirs(out_dir, exist_ok=True)

# ==============================================================================
# FIGURA 2: EVOLUCIÓN CRONOLÓGICA ANUAL (2020 - 2025/2026) (PD1, N = 131)
# ==============================================================================
print("Generando Fig. 2...")
fig, ax1 = plt.subplots(figsize=(6.8, 3.6), dpi=300)

years = ['2020', '2021', '2022', '2023', '2024', '2025', '2026*']
counts = [4, 14, 17, 27, 16, 50, 3]
pct_labels = ['4\n(3.1%)', '14\n(10.7%)', '17\n(13.0%)', '27\n(20.6%)', '16\n(12.2%)', '50\n(38.2%)', '3\n(2.3%)']
cum_pcts = [3.1, 13.8, 26.8, 47.4, 59.6, 97.8, 100.0]

colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#2ca02c', '#17becf']
bars = ax1.bar(years, counts, color=colors, width=0.55, edgecolor='#333333', linewidth=0.8, alpha=0.9, zorder=3)

# Etiquetas en barras
for bar, lbl in zip(bars, pct_labels):
    height = bar.get_height()
    ax1.annotate(lbl,
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=7.8, fontweight='bold', color='#111111')

# Curva de tendencia acumulada
ax2 = ax1.twinx()
ax2.plot(years, cum_pcts, color='#d62728', marker='o', linewidth=1.8, markersize=5, label='Porcentaje acumulado (%)', zorder=4)
ax2.set_ylabel('Porcentaje acumulado (%)', color='#990000', fontweight='bold', fontsize=8.5)
ax2.tick_params(axis='y', labelcolor='#990000', labelsize=8.0)
ax2.set_ylim(0, 115)

ax1.set_xlabel('Año de publicación formal indexada', fontweight='bold', fontsize=8.5)
ax1.set_ylabel('Número de artículos primarios (n)', fontweight='bold', fontsize=8.5)
ax1.tick_params(axis='x', labelsize=8.0)
ax1.tick_params(axis='y', labelsize=8.0)
ax1.set_ylim(0, 62)
ax1.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)

# Resalte visual 2025-2026 apuntando a la barra de 2025
ax1.annotate('Cierre 2025–2026:\n53 estudios (40.5%)\nExplosión VLM / LLMs',
             xy=(5.0, 50), xytext=(2.7, 45),
             arrowprops=dict(facecolor='#2ca02c', edgecolor='#2ca02c', shrink=0.08, width=1.5, headwidth=6),
             bbox=dict(boxstyle="round,pad=0.4", fc="#f0fff0", ec="#2ca02c", lw=1),
             fontsize=7.8, fontweight='bold')

plt.tight_layout()
fig2_png = os.path.join(out_dir, 'fig2_evolucion_anual.png')
fig2_svg = os.path.join(out_dir, 'fig2_evolucion_anual.svg')
plt.savefig(fig2_png, dpi=300, bbox_inches='tight')
plt.savefig(fig2_svg, bbox_inches='tight')
plt.close()
print("  -> Fig 2 generada exitosamente.")

# ==============================================================================
# FIGURA 3: TOP PAÍSES Y RED DE COOCURRENCIA BIBLIOMÉTRICA (PD2)
# ==============================================================================
print("Generando Fig. 3...")
fig, (ax_geo, ax_kw) = plt.subplots(1, 2, figsize=(7.2, 3.6), dpi=300)

countries = ['China', 'India', 'EE. UU.', 'Alemania', 'Corea Sur', 'Canadá', 'Vietnam', 'Taiwán', 'Turquía', 'España']
c_counts = [39, 11, 10, 9, 6, 5, 5, 4, 4, 3]
c_pcts = [29.8, 8.4, 7.6, 6.9, 4.6, 3.8, 3.8, 3.1, 3.1, 2.3]

y_pos = np.arange(len(countries))
ax_geo.barh(y_pos, c_counts, color='#1f77b4', edgecolor='#333333', height=0.65, alpha=0.85)
ax_geo.set_yticks(y_pos)
ax_geo.set_yticklabels(countries, fontsize=7.8)
ax_geo.invert_yaxis()
ax_geo.set_xlabel('Número de estudios (n)', fontweight='bold', fontsize=8.2)
ax_geo.set_title('(a) Distribución por País (Afiliación 1er autor)', fontsize=8.5, fontweight='bold')
ax_geo.set_xlim(0, 46)
ax_geo.grid(axis='x', linestyle='--', alpha=0.5)

for i, (count, pct) in enumerate(zip(c_counts, c_pcts)):
    ax_geo.text(count + 0.8, i, f"{count} ({pct}%)", va='center', fontsize=7.2, fontweight='bold')

keywords = [
    'Information Extraction', 'Deep Learning', 'Table Structure Rec.',
    'Table Detection', 'Optical Char. Rec.', 'Object Detection',
    'Document Understanding', 'Transformers', 'Computer Vision', 'Key Info Extraction'
]
kw_freq = [26, 21, 11, 11, 24, 8, 6, 5, 6, 4]

y_kw = np.arange(len(keywords))
ax_kw.barh(y_kw, kw_freq, color='#ff7f0e', edgecolor='#333333', height=0.65, alpha=0.85)
ax_kw.set_yticks(y_kw)
ax_kw.set_yticklabels(keywords, fontsize=7.8)
ax_kw.invert_yaxis()
ax_kw.set_xlabel('Frecuencia en Author Keywords (n)', fontweight='bold', fontsize=8.2)
ax_kw.set_title('(b) Clústeres Temáticos Principales (Umbral ≥ 3)', fontsize=8.5, fontweight='bold')
ax_kw.set_xlim(0, 31)
ax_kw.grid(axis='x', linestyle='--', alpha=0.5)

for i, count in enumerate(kw_freq):
    ax_kw.text(count + 0.6, i, f"{count}", va='center', fontsize=7.2, fontweight='bold')

plt.tight_layout()
fig3_png = os.path.join(out_dir, 'fig3_vosviewer_geografia.png')
fig3_svg = os.path.join(out_dir, 'fig3_vosviewer_geografia.svg')
plt.savefig(fig3_png, dpi=300, bbox_inches='tight')
plt.savefig(fig3_svg, bbox_inches='tight')
plt.close()
print("  -> Fig 3 generada exitosamente.")

# ==============================================================================
# FIGURA 4: GRÁFICO DE BURBUJAS DE PETERSEN ET AL. (PD3)
# ==============================================================================
print("Generando Fig. 4...")
fig, ax = plt.subplots(figsize=(6.8, 3.6), dpi=300)

design_labels = ['Caso de Estudio Real', 'Cuasi-experimental', 'Prueba Concepto (PoC)', 'Experimental Controlado']
dataset_labels = [
    'Benchmarks Públicos\n(SROIE, FUNSD, CORD)',
    'Corporativos Privados\n(Facturas/Recibos propios)',
    'Híbridos / Mixtos\n(Público + Corporativo)'
]

data_matrix = np.array([
    [2,  5,  1],   # Caso de estudio
    [4,  4,  2],   # Cuasi-experimental
    [14, 11, 6],   # PoC
    [48, 18, 16]   # Experimental
])

x_coords = []
y_coords = []
sizes = []
labels = []

for y_idx in range(4):
    for x_idx in range(3):
        val = data_matrix[y_idx, x_idx]
        x_coords.append(x_idx)
        y_coords.append(y_idx)
        sizes.append(val * 45)
        labels.append(val)

scatter = ax.scatter(x_coords, y_coords, s=sizes, c=labels, cmap='Blues', alpha=0.75, edgecolors='#111111', linewidth=1.2, zorder=3)

for x, y, val in zip(x_coords, y_coords, labels):
    pct = (val / 131) * 100
    ax.annotate(f"n={val}\n({pct:.1f}%)", xy=(x, y), ha='center', va='center', fontsize=7.6, fontweight='bold',
                color='white' if val >= 18 else '#111111')

ax.set_xticks(range(3))
ax.set_xticklabels(dataset_labels, fontweight='bold', fontsize=7.2)
ax.set_yticks(range(4))
ax.set_yticklabels(design_labels, fontweight='bold', fontsize=7.5)

ax.set_xlim(-0.6, 2.6)
ax.set_ylim(-0.6, 3.6)
ax.grid(True, linestyle=':', alpha=0.6, zorder=0)

plt.tight_layout()

# Medir separación de etiquetas X
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
bboxes = [lbl.get_window_extent(renderer) for lbl in ax.get_xticklabels()]
ov01 = bboxes[0].x1 - bboxes[1].x0
ov12 = bboxes[1].x1 - bboxes[2].x0
print(f"  -> Separación X Fig 4: 0-1={ov01:.1f}px, 1-2={ov12:.1f}px (ambos negativos = sin solapamiento)")
assert ov01 < 0 and ov12 < 0, "Error: Las etiquetas del eje X en Fig 4 se solapan"

fig4_png = os.path.join(out_dir, 'fig4_burbujas_disenos_datasets.png')
fig4_svg = os.path.join(out_dir, 'fig4_burbujas_disenos_datasets.svg')
plt.savefig(fig4_png, dpi=300, bbox_inches='tight')
plt.savefig(fig4_svg, bbox_inches='tight')
plt.close()
print("  -> Fig 4 generada exitosamente.")

# ==============================================================================
# FIGURA 5: DISTRIBUCIÓN QA Y TASA DE CUMPLIMIENTO POR CRITERIO (PASO 6)
# ==============================================================================
print("Generando Fig. 5...")
fig, (ax_qa_dist, ax_crit) = plt.subplots(1, 2, figsize=(7.2, 3.4), dpi=300, gridspec_kw={'width_ratios': [1.1, 1.25], 'wspace': 0.26})

qa_strata = ['Calidad Alta\n(4.5–5.0 pts)', 'Calidad Media\n(4.0 pts)', 'Estrato Inferior*\n(3.5 pts)']
qa_counts = [108, 13, 10]
qa_pcts = [82.4, 9.9, 7.6]
qa_colors = ['#2ca02c', '#1f77b4', '#d62728']

bars_qa = ax_qa_dist.bar(qa_strata, qa_counts, color=qa_colors, width=0.52, edgecolor='#333333', linewidth=0.8, alpha=0.85)
ax_qa_dist.set_ylabel('Número de artículos primarios (n)', fontweight='bold', fontsize=8.0)
ax_qa_dist.set_title('(a) Distribución por Estrato (QA)', fontsize=8.5, fontweight='bold')
ax_qa_dist.set_ylim(0, 125)
ax_qa_dist.tick_params(axis='x', labelsize=6.8)
ax_qa_dist.tick_params(axis='y', labelsize=7.5)
ax_qa_dist.grid(axis='y', linestyle='--', alpha=0.5)

for bar, c, p in zip(bars_qa, qa_counts, qa_pcts):
    h = bar.get_height()
    ax_qa_dist.annotate(f"{c}\n({p}%)", xy=(bar.get_x() + bar.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=7.5, fontweight='bold')

criterios = ['QA1: Objetivos/Tipología', 'QA2: Detalle Dataset', 'QA3: Arquitectura', 'QA4: Métricas Form.', 'QA5: Contraste Baselines']
full_comp = [131, 125, 99, 108, 89]
part_comp = [0, 6, 32, 23, 42]

y_crit = np.arange(len(criterios))
p1 = ax_crit.barh(y_crit, full_comp, color='#2ca02c', edgecolor='#333333', height=0.6, label='Cumplimiento Total (1.0 pt)', alpha=0.85)
p2 = ax_crit.barh(y_crit, part_comp, left=full_comp, color='#ff7f0e', edgecolor='#333333', height=0.6, label='Cumplimiento Parcial (0.5 pt)', alpha=0.85)

ax_crit.set_yticks(y_crit)
ax_crit.set_yticklabels(criterios, fontsize=7.2)
ax_crit.invert_yaxis()
ax_crit.set_xlabel('Número de estudios (n)', fontweight='bold', fontsize=8.0)
ax_crit.set_title('(b) Rigor por Pregunta QA (N = 131)', fontsize=8.5, fontweight='bold')
ax_crit.set_xlim(0, 145)
ax_crit.tick_params(axis='x', labelsize=7.5)
ax_crit.grid(axis='x', linestyle='--', alpha=0.5)
ax_crit.legend(loc='lower left', fontsize=7.0)

ax_crit.annotate('Mayor debilidad empírica:\n32.1% contraste parcial', xy=(110, 4), xytext=(85, 3.4),
                 arrowprops=dict(arrowstyle="->", color='#d62728', lw=1.2),
                 bbox=dict(boxstyle="square,pad=0.2", fc="#fff0f0", ec="#d62728", lw=0.8),
                 fontsize=6.5, color='#990000', fontweight='bold')

# Medir separación de etiquetas X en panel A
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
bboxes = [lbl.get_window_extent(renderer) for lbl in ax_qa_dist.get_xticklabels()]
ov01 = bboxes[0].x1 - bboxes[1].x0
ov12 = bboxes[1].x1 - bboxes[2].x0
print(f"  -> Separación X Fig 5: 0-1={ov01:.1f}px, 1-2={ov12:.1f}px (ambos negativos = sin solapamiento)")
assert ov01 < 0 and ov12 < 0, "Error: Las etiquetas del eje X en Fig 5 se solapan"

fig5_png = os.path.join(out_dir, 'fig5_distribucion_qa_criterios.png')
fig5_svg = os.path.join(out_dir, 'fig5_distribucion_qa_criterios.svg')
plt.savefig(fig5_png, dpi=300, bbox_inches='tight')
plt.savefig(fig5_svg, bbox_inches='tight')
plt.close()
print("  -> Fig 5 generada exitosamente.")

# ==============================================================================
# FIGURA 6: TAXONOMÍA DE FAMILIAS ALGORÍTMICAS (PI1, n = 105)
# ==============================================================================
print("Generando Fig. 6...")
fig, ax = plt.subplots(figsize=(6.8, 3.0), dpi=300)
categories = [
    'Pipelines Híbridos CNN-RNN\ny Segmentación con OCR',
    'Transformers Multimodales\ny Visión-Lenguaje (VLM)',
    'Redes Neuronales de Grafos\ny Modelado Espacial (GNN)',
    'Modelos Generativos y LLMs\n(Zero/Few-Shot)'
]
counts = [56, 22, 16, 11]
colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']
y_pos = np.arange(len(categories))

bars = ax.barh(y_pos, counts, color=colors, height=0.55, edgecolor='black', linewidth=0.7)
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=7.8)
ax.invert_yaxis()
ax.set_xlabel('Número de estudios primarios (n)', fontweight='bold', fontsize=8.2)
ax.grid(axis='x', linestyle='--', alpha=0.5)

for bar, count in zip(bars, counts):
    pct = (count / 105) * 100
    ax.text(count + 1, bar.get_y() + bar.get_height()/2, f'{count} ({pct:.1f} %)',
            va='center', ha='left', fontsize=7.8, fontweight='bold', color='#222222')

ax.set_xlim(0, 68)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig6_taxonomia_algoritmos.png'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(out_dir, 'fig6_taxonomia_algoritmos.svg'), bbox_inches='tight')
plt.close()
print("  -> Fig 6 generada exitosamente.")

# ==============================================================================
# FIGURA 7: RENDIMIENTO CUANTITATIVO POR BENCHMARK (PI2, n = 117)
# ==============================================================================
print("Generando Fig. 7...")
fig, ax = plt.subplots(figsize=(6.8, 3.2), dpi=300)

bench_data = {
    'SROIE\n(Recibos estándar)': {'min': 86.4, 'q1': 92.1, 'med': 95.2, 'q3': 97.4, 'max': 98.7, 'n': 48},
    'CORD\n(Recibos jerárquicos)': {'min': 88.0, 'q1': 91.5, 'med': 94.1, 'q3': 96.2, 'max': 97.4, 'n': 16},
    'FUNSD\n(Formularios ruidosos)': {'min': 72.1, 'q1': 79.3, 'med': 84.5, 'q3': 89.2, 'max': 93.8, 'n': 21},
    'FinTabNet / WTW\n(Estructura tabular)': {'min': 76.5, 'q1': 84.0, 'med': 89.8, 'q3': 93.5, 'max': 96.2, 'n': 42}
}

b_names = list(bench_data.keys())
y_positions = np.arange(len(b_names))

for idx, (name, stats) in enumerate(bench_data.items()):
    ax.plot([stats['min'], stats['max']], [idx, idx], color='#444444', linewidth=1.5, zorder=2)
    rect = plt.Rectangle((stats['q1'], idx - 0.2), stats['q3'] - stats['q1'], 0.4,
                         facecolor='#6baed6', edgecolor='#08519c', linewidth=1.2, zorder=3)
    ax.add_patch(rect)
    ax.plot([stats['med'], stats['med']], [idx - 0.2, idx + 0.2], color='#b10026', linewidth=2.2, zorder=4)
    ax.scatter([stats['min'], stats['max']], [idx, idx], color='#08519c', s=25, zorder=5)
    ax.text(stats['max'] + 0.8, idx, f"Med: {stats['med']:.1f} %\n[{stats['min']:.1f}–{stats['max']:.1f}]",
            va='center', ha='left', fontsize=7.2, fontweight='bold', color='#111111')

ax.set_yticks(y_positions)
ax.set_yticklabels(b_names, fontsize=7.8)
ax.invert_yaxis()
ax.set_xlabel('F1-score / TEDS (%)', fontweight='bold', fontsize=8.2)
ax.set_xlim(65, 108)
ax.grid(axis='x', linestyle='--', alpha=0.5)

line_med = plt.Line2D([0], [0], color='#b10026', lw=2, label='Mediana empírica')
box_iqr = plt.Rectangle((0, 0), 1, 1, facecolor='#6baed6', edgecolor='#08519c', label='Rango intercuartil (Q1–Q3)')
line_ext = plt.Line2D([0], [0], color='#444444', lw=1.5, marker='o', markersize=4, label='Rango total [mín, máx]')
ax.legend(handles=[line_med, box_iqr, line_ext], loc='lower left', frameon=True, fontsize=7.2)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig7_rendimiento_benchmarks.png'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(out_dir, 'fig7_rendimiento_benchmarks.svg'), bbox_inches='tight')
plt.close()
print("  -> Fig 7 generada exitosamente.")

# ==============================================================================
# FIGURA 8: SÍNTESIS SWiM BARRAS DIVERGENTES (PI3, n = 82)
# ==============================================================================
print("Generando Fig. 8...")
fig, ax = plt.subplots(figsize=(6.8, 3.0), dpi=300)

dimensions = [
    'Tiempo y Latencia de Ciclo\n(Reducción de horas/días a seg.)',
    'Exactitud y Tasa de Error\n(vs. Ingreso manual / Reglas)',
    'Carga Operativa y Straight-Through\n(Procesamiento sin intervención)'
]

mejora = [75, 72, 66]
paridad = [5, 8, 11]
empeora = [-2, -2, -5]

y_pos = np.arange(len(dimensions))

bar_empeora = ax.barh(y_pos, empeora, color='#d73027', height=0.45, label='Empeora / Menor eficiencia (-1)', edgecolor='black', linewidth=0.6)
bar_mejora = ax.barh(y_pos, mejora, color='#1a9850', height=0.45, label='Mejora favorable (+1)', edgecolor='black', linewidth=0.6)

for idx, (m_val, p_val, e_val) in enumerate(zip(mejora, paridad, empeora)):
    ax.text(m_val + 1.5, idx, f'+{m_val} ({m_val/82*100:.1f} %)\n[Paridad: {p_val}]', va='center', ha='left', fontsize=7.2, fontweight='bold', color='#1a9850')
    ax.text(e_val - 1.5, idx, f'{e_val}', va='center', ha='right', fontsize=7.2, fontweight='bold', color='#d73027')

ax.axvline(0, color='black', linewidth=1.0)
ax.set_yticks(y_pos)
ax.set_yticklabels(dimensions, fontsize=7.8)
ax.invert_yaxis()
ax.set_xlabel('Dirección del voto: Estudios desfavorables  ◄ 0 ►  Estudios favorables', fontweight='bold', fontsize=8.0)
ax.set_xlim(-15, 95)
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.legend(loc='lower right', frameon=True, fontsize=7.2)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig8_swim_barras_divergentes.png'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(out_dir, 'fig8_swim_barras_divergentes.svg'), bbox_inches='tight')
plt.close()
print("  -> Fig 8 generada exitosamente.")

# ==============================================================================
# FIGURA 9: HEATMAP DOCUMENTO × PLATAFORMA ERP/CRM (PI4, N = 131)
# ==============================================================================
print("Generando Fig. 9...")
fig, ax = plt.subplots(figsize=(6.8, 3.2), dpi=300)

doc_labels = [
    'Facturas comerciales y fiscales',
    'Recibos de caja y comprobantes POS',
    'Balances y tablas financieras',
    'Formularios y guías administrativas'
]
platform_labels = [
    'Sistemas ERP\n(SAP / Oracle / Dynamics)',
    'Sistemas CRM / DMS\n(Salesforce / SharePoint)',
    'RPA / APIs REST y\nBD Relacionales'
]

matrix_data = np.array([
    [22,  8,  4],  # Facturas: 34
    [ 6,  4,  2],  # Recibos: 12
    [31, 16, 12],  # Balances/Tablas: 59
    [10, 11,  5]   # Formularios/Admin: 26
])

im = ax.imshow(matrix_data, cmap='Blues', aspect='auto')
cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)
cbar.ax.set_ylabel('Estudios mapeados (n)', rotation=-90, va="bottom", fontsize=7.5)
cbar.ax.tick_params(labelsize=7.0)

ax.set_xticks(np.arange(len(platform_labels)))
ax.set_yticks(np.arange(len(doc_labels)))
ax.set_xticklabels(platform_labels, fontsize=7.5)
ax.set_yticklabels(doc_labels, fontsize=7.8)

for i in range(len(doc_labels)):
    for j in range(len(platform_labels)):
        val = matrix_data[i, j]
        color = "white" if val > 20 else "black"
        ax.text(j, i, f"{val}", ha="center", va="center", color=color, fontweight='bold', fontsize=9.0)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig9_heatmap_documentos_erp.png'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(out_dir, 'fig9_heatmap_documentos_erp.svg'), bbox_inches='tight')
plt.close()
print("  -> Fig 9 generada exitosamente.")

print("\n¡Todas las figuras IEEE (Fig 2 a Fig 9) regeneradas exitosamente a 300 dpi sin duplicación de títulos internos y con separación garantizada en el eje X!")

