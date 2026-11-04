import os

def update_docx_builders():
    files = [
        'project/metodologia/scripts/build_combined_ieee_article.py',
        'project/resultados/scripts/build_resultados_completo_docx.py'
    ]

    target_old = '''add_p(
    "Agrupa casos minoritarios donde la introducción de arquitecturas de IA generó efectos contraproducentes frente a flujos convencionales (Tabla XIX). El sobrecosto operativo se originó en la necesidad "
    "de re-inspección humana obligatoria ante alucinaciones de LLMs en montos monetarios críticos [121] o en la sobrecarga de latencia inducida por modelos masivos al ejecutarse en infraestructura local sin aceleración GPU [37], [56]. "
    "",
    bold_prefix="2.3. Escenarios de Sobrecosto y Carga Operativa Desfavorable (Empeora -1): "
)

add_p(
    "El debate fundamental en torno a la relación costo-beneficio y eficiencia operativa de la IA frente a sistemas convencionales se polariza en tres vertientes contrastadas:",
    bold_prefix="3) Contrastes y Debates de Eficiencia: "
)
add_p(
    "Investigaciones aplicadas defienden que la automatización neuronal reduce drásticamente las horas-hombre y amortiza los costos de software en centros de servicios compartidos corporativos [4], [11], [16], [67], [80] (Chen L.-C. et al. [4]; Xiao et al. [11]; Saeed et al. [16]; Nguyen M.-T. et al. [67]; Yang Z. et al. [80]).",
    bold_prefix="a) Ahorro masivo y amortización en grandes volúmenes: "
)'''

    replacement_new = '''add_p(
    "Registra los estudios en los que la implementación de modelos pesados de IA resultó contraproducente frente a flujos convencionales debido a cuellos de botella de hardware en servidores sin GPU o a la sobrecarga de auditoría humana requerida para corregir alucinaciones numéricas en montos contables y códigos fiscales (Tabla XIX) [37], [56], [121].",
    bold_prefix="2.3. Escenarios de Sobrecosto y Penalización por Alucinación (Desfavorable -1): "
)

add_p(
    "La síntesis SWiM pone de relieve una tensión operativa entre tres posturas documentadas en el corpus:",
    bold_prefix="3) Contrastes y Debates de Eficiencia: "
)
add_p(
    "La mayoría de la evidencia sostiene que en entornos con alta rotación de proveedores y formatos heterogéneos, los modelos multimodales eliminan el cuello de botella del mantenimiento manual de plantillas, reduciendo drásticamente el tiempo de ciclo operativo [4], [6], [44], [55], [103], [127].",
    bold_prefix="a) Superioridad de la automatización cognitiva en flujos multiformato: "
)'''

    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        if target_old in content:
            content = content.replace(target_old, replacement_new)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Successfully replaced PI3 block in {path}")
        else:
            print(f"[ERROR] Target block not found in {path}")

def update_markdown_builder():
    path = 'project/resultados/scripts/build_full_resultados_markdown.py'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    p_start = content.find('**2.3. Escenarios de Sobrecosto')
    p_end = content.find('**Suficiencia y ventaja económica', p_start)

    if p_start != -1 and p_end != -1:
        # Check preceding 2 characters before **Suficiencia
        prefix_p2 = content[p_end-4:p_end]
        print(f"Prefix before Suficiencia: {repr(prefix_p2)}")
        
        old_part = content[p_start:p_end]
        new_part = '''**2.3. Escenarios de Sobrecosto y Penalización por Alucinación (Desfavorable -1):**  
Registra los estudios en los que la implementación de modelos pesados de IA resultó contraproducente frente a flujos convencionales debido a cuellos de botella de hardware en servidores sin GPU o a la sobrecarga de auditoría humana requerida para corregir alucinaciones numéricas en montos contables y códigos fiscales (Tabla XIX) [37], [56], [121].

#### Bloque 3 — Contrastes y Debates de Eficiencia
**3) Contrastes y Debates de Eficiencia:** La síntesis SWiM pone de relieve una tensión operativa entre tres posturas documentadas en el corpus:

a) **Superioridad de la automatización cognitiva en flujos multiformato:** La mayoría de la evidencia sostiene que en entornos con alta rotación de proveedores y formatos heterogéneos, los modelos multimodales eliminan el cuello de botella del mantenimiento manual de plantillas, reduciendo drásticamente el tiempo de ciclo operativo [4], [6], [44], [55], [103], [127].

b) '''
        # If prefix was "2. ", we want to replace from p_start to p_end including "2. "
        p_replace_end = p_end
        if content[p_end-3:p_end] == "2. ":
            p_replace_start_b = p_end - 3
        else:
            p_replace_start_b = p_end

        content = content[:p_start] + new_part + content[p_end:]
        
        # Also change 3. **Sobrecosto to c) **Sobrecosto
        content = content.replace('\n3. **Sobrecosto de infraestructura', '\nc) **Sobrecosto de infraestructura')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Successfully replaced PI3 block in {path}")
    else:
        print(f"[ERROR] Could not find markdown boundaries: p_start={p_start}, p_end={p_end}")

if __name__ == '__main__':
    update_docx_builders()
    update_markdown_builder()

