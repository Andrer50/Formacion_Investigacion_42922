"""
Regeneración oficial de Fig. 8 y Fig. 9 (Parte 4 - Ajuste fino de fidelidad visual)
Sincronización exacta con Tabla XIX (PI3, n = 82) y Tabla XX (PI4, N = 131)
Formato IEEE (300 dpi, sin títulos incrustados, separación garantizada en ejes)
"""

import os
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.gettempdir()
import matplotlib.pyplot as plt
import numpy as np

out_dir = 'project/resultados/outputs'
os.makedirs(out_dir, exist_ok=True)

# ==============================================================================
# 1. FIGURA 8: SÍNTESIS SWiM BARRAS DIVERGENTES (PI3, n = 82)
# ==============================================================================
print("Regenerando Fig. 8...")
fig, ax = plt.subplots(figsize=(7.0, 3.4), dpi=300)

categories = [
    'Consenso Global SWiM\n(Conteo consolidado, n = 82)',
    'Tiempo y Latencia\n(Favorable / Mejora +1)',
    'Exactitud en Formatos Rígidos\n(Paridad / Sin diferencia 0)',
    'Carga y Costo en HW Restringido\n(Desfavorable / Empeora -1)'
]
y_pos = np.arange(len(categories))

# Dibujar barras divergentes
ax.barh(0, 71, color='#1a9850', height=0.48, edgecolor='black', linewidth=0.6)
ax.barh(0, -3, color='#d73027', height=0.48, edgecolor='black', linewidth=0.6)
ax.barh(1, 71, color='#1a9850', height=0.48, edgecolor='black', linewidth=0.6)
ax.barh(2, 8, color='#ff7f0e', height=0.48, edgecolor='black', linewidth=0.6)
ax.barh(3, -3, color='#d73027', height=0.48, edgecolor='black', linewidth=0.6)

# Etiquetas de datos
t0_r = ax.text(71 + 1.2, 0, '+71 (86.6 %)\n[Paridad: 8 (9.8 %)]', va='center', ha='left', fontsize=7.2, fontweight='bold', color='#1a9850')
t0_l = ax.text(-3 - 1.2, 0, '-3 (3.7 %)', va='center', ha='right', fontsize=7.2, fontweight='bold', color='#d73027')
t1_r = ax.text(71 + 1.2, 1, '+71 estudios (86.6 %)', va='center', ha='left', fontsize=7.2, fontweight='bold', color='#1a9850')
t2_r = ax.text(8 + 1.2, 2, '8 estudios (9.8 %)', va='center', ha='left', fontsize=7.2, fontweight='bold', color='#d95f02')
t3_l = ax.text(-3 - 1.2, 3, '-3 estudios (3.7 %)', va='center', ha='right', fontsize=7.2, fontweight='bold', color='#d73027')

ax.axvline(0, color='black', linewidth=1.0)
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=7.6, fontweight='bold')
ax.invert_yaxis()
ax.set_xlabel('Dirección del voto: Estudios desfavorables ◄ 0 ► Estudios favorables', fontweight='bold', fontsize=8.0)
ax.set_xlim(-18, 98)
ax.grid(axis='x', linestyle='--', alpha=0.5)

handles = [
    plt.Rectangle((0,0),1,1, color='#1a9850', ec='black', lw=0.6, label='Favorable / Mejora (+1)'),
    plt.Rectangle((0,0),1,1, color='#ff7f0e', ec='black', lw=0.6, label='Paridad / Sin diferencia (0)'),
    plt.Rectangle((0,0),1,1, color='#d73027', ec='black', lw=0.6, label='Desfavorable / Empeora (-1)')
]
leg = ax.legend(handles=handles, loc='lower right', frameon=True, fontsize=7.0, framealpha=0.9)

plt.tight_layout()

# Validación geométrica de colisión
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
leg_bbox = leg.get_window_extent(renderer)
for name, t in [('t0_r', t0_r), ('t1_r', t1_r), ('t2_r', t2_r), ('t3_l', t3_l)]:
    tb = t.get_window_extent(renderer)
    intersect = not (tb.x1 < leg_bbox.x0 or tb.x0 > leg_bbox.x1 or tb.y1 < leg_bbox.y0 or tb.y0 > leg_bbox.y1)
    assert not intersect, f"Error: {name} colisiona con la leyenda"

fig8_png = os.path.join(out_dir, 'fig8_swim_barras_divergentes.png')
fig8_svg = os.path.join(out_dir, 'fig8_swim_barras_divergentes.svg')
plt.savefig(fig8_png, dpi=300, bbox_inches='tight')
plt.savefig(fig8_svg, bbox_inches='tight')
plt.close()
print("  -> Fig 8 generada exitosamente (sincronizada con Tabla XIX).")

# ==============================================================================
# 2. FIGURA 9: HEATMAP DOCUMENTO × PLATAFORMA ERP/CRM (PI4, N = 131)
# ==============================================================================
print("Regenerando Fig. 9...")
fig, ax = plt.subplots(figsize=(8.0, 3.4), dpi=300)

doc_labels = [
    'Balances y tablas financieras',
    'Facturas comerciales y fiscales',
    'Formularios y pólizas administrativas',
    'Recibos de caja y comprobantes POS'
]

platform_labels = [
    'Sistemas ERP\n(SAP / Oracle / Dynamics)',
    'Sistemas CRM / DMS\n(Salesforce / SharePoint)',
    'RPA / APIs REST y\nBD Relacionales'
]

# Matriz 4x3 sincronizada exactamente con Tabla XX (suma 131)
matrix_data = np.array([
    [31, 16, 12],  # Balances y tablas: 59
    [22,  8,  4],  # Facturas comerciales: 34
    [10, 11,  5],  # Formularios/Admin: 26
    [ 6,  4,  2]   # Recibos POS: 12
])

im = ax.imshow(matrix_data, cmap='Blues', aspect='auto')
cbar = ax.figure.colorbar(im, ax=ax, shrink=0.85, pad=0.03)
cbar.ax.set_ylabel('Estudios mapeados (n)', rotation=-90, va='bottom', fontsize=7.5)
cbar.ax.tick_params(labelsize=7.0)

ax.set_xticks(np.arange(len(platform_labels)))
ax.set_yticks(np.arange(len(doc_labels)))
ax.set_xticklabels(platform_labels, fontsize=7.0, fontweight='bold')
ax.set_yticklabels(doc_labels, fontsize=7.8, fontweight='bold')

for i in range(len(doc_labels)):
    for j in range(len(platform_labels)):
        val = matrix_data[i, j]
        color = 'white' if val > 20 else 'black'
        ax.text(j, i, f'{val}', ha='center', va='center', color=color, fontweight='bold', fontsize=9.0)

plt.tight_layout()

# Validación geométrica de colisión en eje X
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
bboxes = [lbl.get_window_extent(renderer) for lbl in ax.get_xticklabels()]
ov01 = bboxes[0].x1 - bboxes[1].x0
ov12 = bboxes[1].x1 - bboxes[2].x0
print(f"  -> Separación eje X Fig 9: 0-1={ov01:.1f}px, 1-2={ov12:.1f}px (ambos negativos = sin colisión)")
assert ov01 < 0 and ov12 < 0, "Error: Las etiquetas del eje X en Fig 9 colisionan"

fig9_png = os.path.join(out_dir, 'fig9_heatmap_documentos_erp.png')
fig9_svg = os.path.join(out_dir, 'fig9_heatmap_documentos_erp.svg')
plt.savefig(fig9_png, dpi=300, bbox_inches='tight')
plt.savefig(fig9_svg, bbox_inches='tight')
plt.close()
print("  -> Fig 9 generada exitosamente (orden sincronizado con Tabla XX).")

