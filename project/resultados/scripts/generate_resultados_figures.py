"""
Generador de figuras estadísticas oficiales para la Sección Resultados (ATI3)
Revisión Sistemática de Literatura (RSL) - N = 131 estudios primarios
Formato estándar IEEE (300 dpi, tipografía sans/serif académica, paleta sobria)
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración global de estilo científico
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9
plt.rcParams['axes.labelsize'] = 9.5
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8.5
plt.rcParams['ytick.labelsize'] = 8.5
plt.rcParams['legend.fontsize'] = 8.5
plt.rcParams['figure.titlesize'] = 11

out_dir = 'project/resultados/outputs'
os.makedirs(out_dir, exist_ok=True)

# ==============================================================================
# FIGURA 2: EVOLUCIÓN CRONOLÓGICA ANUAL (2020 - 2025/2026) (PD1)
# ==============================================================================
fig, ax1 = plt.subplots(figsize=(6.8, 3.8), dpi=300)

years = ['2020', '2021', '2022', '2023', '2024', '2025', '2026*']
counts = [4, 14, 17, 26, 16, 51, 3]
pcts = [3.1, 10.7, 13.0, 19.8, 12.2, 38.9, 2.3]

colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#2ca02c', '#17becf']
bars = ax1.bar(years, counts, color=colors, width=0.55, edgecolor='#333333', linewidth=0.8, alpha=0.9, zorder=3)

# Etiquetas en barras
for bar, c, p in zip(bars, counts, pcts):
    height = bar.get_height()
    ax1.annotate(f'{c}\n({p}%)',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=8, fontweight='bold', color='#111111')

# Curva de tendencia acumulada
ax2 = ax1.twinx()
cum_pcts = np.cumsum(pcts)
ax2.plot(years, cum_pcts, color='#d62728', marker='o', linewidth=1.8, markersize=5, label='Porcentaje acumulado (%)', zorder=4)
ax2.set_ylabel('Porcentaje acumulado (%)', color='#990000', fontweight='semibold')
ax2.tick_params(axis='y', labelcolor='#990000')
ax2.set_ylim(0, 115)

ax1.set_xlabel('Año de publicación formal indexada', fontweight='semibold')
ax1.set_ylabel('Número de artículos primarios (n)', fontweight='semibold')
ax1.set_ylim(0, 62)
ax1.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)

# Resalte visual 2025-2026
ax1.annotate('Cierre 2025–2026:\n54 estudios (41.2%)\nExplosión VLM / LLMs',
             xy=(5.5, 51), xytext=(3.2, 48),
             arrowprops=dict(facecolor='#2ca02c', edgecolor='#2ca02c', shrink=0.08, width=1.5, headwidth=6),
             bbox=dict(boxstyle="round,pad=0.4", fc="#f0fff0", ec="#2ca02c", lw=1),
             fontsize=8, fontweight='semibold')

plt.title('Fig. 2. Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales\n(2020–2025/2026, N = 131)', pad=12, fontweight='bold')
fig.text(0.5, 0.01, '* Nota: 2026 corresponde a 3 artículos indexados como Early Access a finales de 2025 (refs [3], [65], [66]).\nFuente: elaboración propia a partir del corpus primario [3]–[133].', ha='center', fontsize=7.5, style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 0.98])
fig2_png = os.path.join(out_dir, 'fig2_evolucion_anual.png')
fig2_svg = os.path.join(out_dir, 'fig2_evolucion_anual.svg')
plt.savefig(fig2_png, dpi=300)
plt.savefig(fig2_svg)
plt.close()
print("Generada:", fig2_png)

# ==============================================================================
# FIGURA 3: TOP PAÍSES Y RED DE COOCURRENCIA BIBLIOMÉTRICA (PD2)
# ==============================================================================
fig, (ax_geo, ax_kw) = plt.subplots(1, 2, figsize=(7.2, 3.8), dpi=300)

# Panel A: Países
countries = ['China', 'India', 'EE. UU.', 'Alemania', 'Corea Sur', 'Canadá', 'Vietnam', 'Taiwán', 'Turquía', 'España']
c_counts = [39, 11, 10, 9, 6, 5, 5, 4, 4, 3]
c_pcts = [29.8, 8.4, 7.6, 6.9, 4.6, 3.8, 3.8, 3.1, 3.1, 2.3]

y_pos = np.arange(len(countries))
ax_geo.barh(y_pos, c_counts, color='#1f77b4', edgecolor='#333333', height=0.65, alpha=0.85)
ax_geo.set_yticks(y_pos)
ax_geo.set_yticklabels(countries)
ax_geo.invert_yaxis()
ax_geo.set_xlabel('Número de estudios (n)', fontweight='semibold')
ax_geo.set_title('(a) Distribución por País (Afiliación 1er autor)', fontsize=9, fontweight='bold')
ax_geo.set_xlim(0, 46)
ax_geo.grid(axis='x', linestyle='--', alpha=0.5)

for i, (count, pct) in enumerate(zip(c_counts, c_pcts)):
    ax_geo.text(count + 0.8, i, f"{count} ({pct}%)", va='center', fontsize=7.5, fontweight='bold')

# Panel B: Red conceptual de palabras clave (Visualización de clusters VOSviewer)
keywords = [
    'Information Extraction', 'Deep Learning', 'Table Structure Rec.',
    'Table Detection', 'Optical Char. Rec.', 'Object Detection',
    'Document Understanding', 'Transformers', 'Computer Vision', 'Key Info Extraction'
]
kw_freq = [26, 21, 11, 11, 24, 8, 6, 5, 6, 4]

y_kw = np.arange(len(keywords))
ax_kw.barh(y_kw, kw_freq, color='#ff7f0e', edgecolor='#333333', height=0.65, alpha=0.85)
ax_kw.set_yticks(y_kw)
ax_kw.set_yticklabels(keywords)
ax_kw.invert_yaxis()
ax_kw.set_xlabel('Frecuencia en Author Keywords (n)', fontweight='semibold')
ax_kw.set_title('(b) Clústeres Temáticos Principales (Umbral ≥ 3)', fontsize=9, fontweight='bold')
ax_kw.set_xlim(0, 31)
ax_kw.grid(axis='x', linestyle='--', alpha=0.5)

for i, count in enumerate(kw_freq):
    ax_kw.text(count + 0.6, i, f"{count}", va='center', fontsize=7.5, fontweight='bold')

fig.suptitle('Fig. 3. Concentración geográfica y mapa de términos temáticos clave (PD2, N = 131)', fontsize=10, fontweight='bold', y=0.98)
fig.text(0.5, 0.01, 'Fuente: elaboración propia a partir del corpus primario [3]–[133] mediante análisis en VOSviewer y normalización Scopus/WoS.', ha='center', fontsize=7.5, style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
fig3_png = os.path.join(out_dir, 'fig3_vosviewer_geografia.png')
fig3_svg = os.path.join(out_dir, 'fig3_vosviewer_geografia.svg')
plt.savefig(fig3_png, dpi=300)
plt.savefig(fig3_svg)
plt.close()
print("Generada:", fig3_png)

# ==============================================================================
# FIGURA 4: GRÁFICO DE BURBUJAS DE PETERSEN ET AL. (PD3)
# ==============================================================================
fig, ax = plt.subplots(figsize=(6.8, 4.0), dpi=300)

design_labels = ['Caso de Estudio Real', 'Cuasi-experimental', 'Prueba Concepto (PoC)', 'Experimental Controlado']
dataset_labels = ['Benchmarks Públicos\n(SROIE, FUNSD, CORD)', 'Corporativos Privados\n(Facturas/Recibos propios)', 'Híbridos / Mixtos\n(Público + Corporativo)']

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
    ax.annotate(f"n={val}\n({pct:.1f}%)", xy=(x, y), ha='center', va='center', fontsize=7.8, fontweight='bold',
                color='white' if val >= 18 else '#111111')

ax.set_xticks(range(3))
ax.set_xticklabels(dataset_labels, fontweight='semibold')
ax.set_yticks(range(4))
ax.set_yticklabels(design_labels, fontweight='semibold')

ax.set_xlim(-0.6, 2.6)
ax.set_ylim(-0.6, 3.6)
ax.grid(True, linestyle=':', alpha=0.6, zorder=0)

plt.title('Fig. 4. Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]):\nDiseño Metodológico vs. Tipología de Dataset (PD3, N = 131)', pad=12, fontweight='bold')
fig.text(0.5, 0.01, 'Nota: El área de cada burbuja es proporcional al volumen de estudios (n). Concordancia inter-evaluador κ = 0.85.\nFuente: elaboración propia a partir del corpus primario [3]–[133].', ha='center', fontsize=7.5, style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 0.98])
fig4_png = os.path.join(out_dir, 'fig4_burbujas_disenos_datasets.png')
fig4_svg = os.path.join(out_dir, 'fig4_burbujas_disenos_datasets.svg')
plt.savefig(fig4_png, dpi=300)
plt.savefig(fig4_svg)
plt.close()
print("Generada:", fig4_png)

# ==============================================================================
# FIGURA 5: DISTRIBUCIÓN QA Y TASA DE CUMPLIMIENTO POR CRITERIO (PASO 6)
# ==============================================================================
fig, (ax_qa_dist, ax_crit) = plt.subplots(1, 2, figsize=(7.2, 3.8), dpi=300)

# Panel A: Estratificación QA
qa_strata = ['Calidad Alta\n(4.5–5.0 pts)', 'Calidad Media\n(4.0 pts)', 'Estrato Inferior*\n(3.5 pts)']
qa_counts = [108, 13, 10]
qa_pcts = [82.4, 9.9, 7.6]
qa_colors = ['#2ca02c', '#1f77b4', '#d62728']

bars_qa = ax_qa_dist.bar(qa_strata, qa_counts, color=qa_colors, width=0.55, edgecolor='#333333', linewidth=0.8, alpha=0.85)
ax_qa_dist.set_ylabel('Número de artículos primarios (n)', fontweight='semibold')
ax_qa_dist.set_title('(a) Distribución por Estrato de Calidad (QA)', fontsize=9, fontweight='bold')
ax_qa_dist.set_ylim(0, 125)
ax_qa_dist.grid(axis='y', linestyle='--', alpha=0.5)

for bar, c, p in zip(bars_qa, qa_counts, qa_pcts):
    h = bar.get_height()
    ax_qa_dist.annotate(f"{c}\n({p}%)", xy=(bar.get_x() + bar.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8, fontweight='bold')

# Panel B: Tasa de cumplimiento por criterio (QA1 a QA5)
criterios = ['QA1: Objetivos/Tipología', 'QA2: Detalle Dataset', 'QA3: Arquitectura', 'QA4: Métricas Form.', 'QA5: Contraste Baselines']
full_comp = [131, 125, 99, 108, 89]     # 1.0 pts
part_comp = [0, 6, 32, 23, 42]         # 0.5 pts

y_crit = np.arange(len(criterios))
p1 = ax_crit.barh(y_crit, full_comp, color='#2ca02c', edgecolor='#333333', height=0.6, label='Cumplimiento Total (1.0 pt)', alpha=0.85)
p2 = ax_crit.barh(y_crit, part_comp, left=full_comp, color='#ff7f0e', edgecolor='#333333', height=0.6, label='Cumplimiento Parcial (0.5 pt)', alpha=0.85)

ax_crit.set_yticks(y_crit)
ax_crit.set_yticklabels(criterios, fontsize=8)
ax_crit.invert_yaxis()
ax_crit.set_xlabel('Número de estudios (n)', fontweight='semibold')
ax_crit.set_title('(b) Rigor por Pregunta QA (Evaluación N = 131)', fontsize=9, fontweight='bold')
ax_crit.set_xlim(0, 145)
ax_crit.grid(axis='x', linestyle='--', alpha=0.5)
ax_crit.legend(loc='lower left', fontsize=7.5)

# Anotación en QA5 y QA3
ax_crit.annotate('Mayor debilidad empírica:\n32.1% contraste parcial', xy=(110, 4), xytext=(85, 3.4),
                 arrowprops=dict(arrowstyle="->", color='#d62728', lw=1.2),
                 bbox=dict(boxstyle="square,pad=0.2", fc="#fff0f0", ec="#d62728", lw=0.8),
                 fontsize=7, color='#990000', fontweight='bold')

fig.suptitle('Fig. 5. Evaluación de Calidad Metodológica (Kitchenham) y Vulnerabilidad por Criterio (N = 131)', fontsize=10, fontweight='bold', y=0.98)
fig.text(0.5, 0.01, '* Nota: El estrato de 3.5 pts se excluye temporalmente en el análisis de sensibilidad (Paso 8). Media global = 4.61 / 5.0.\nFuente: elaboración propia a partir del corpus primario [3]–[133].', ha='center', fontsize=7.5, style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
fig5_png = os.path.join(out_dir, 'fig5_distribucion_qa_criterios.png')
fig5_svg = os.path.join(out_dir, 'fig5_distribucion_qa_criterios.svg')
plt.savefig(fig5_png, dpi=300)
plt.savefig(fig5_svg)
plt.close()
print("Generada:", fig5_png)

print("\n¡Todas las 4 figuras IEEE generadas exitosamente en 300 dpi y formato vectorial SVG!")
