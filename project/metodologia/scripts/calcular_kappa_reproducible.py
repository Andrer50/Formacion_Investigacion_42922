"""
Script Reproducible: Calculo Determinista del Coeficiente Kappa de Cohen (intra-evaluador)
Proyecto: Formacion para la Investigacion - RSL Inteligencia Artificial / IDP
Muestra de auditoria: 20.6 % del corpus final (n = 27 estudios primarios)
"""

import sys
import io
import numpy as np
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def calcular_kappa_cohen(matriz, etiquetas, nombre_fase):
    """
    Calcula de forma exacta:
    - Po: Proporcion de acuerdo observado (diagonal / total)
    - Pe: Proporcion de acuerdo esperado por azar (sumatoria marginales fila * columna / total^2)
    - Kappa: (Po - Pe) / (1 - Pe)
    """
    mat = np.array(matriz, dtype=float)
    n = np.sum(mat)
    
    # 1. Acuerdo observado (Po)
    acuerdos = np.trace(mat)
    po = acuerdos / n
    
    # 2. Acuerdo esperado por azar (Pe)
    marginal_filas = np.sum(mat, axis=1)
    marginal_columnas = np.sum(mat, axis=0)
    pe = np.sum(marginal_filas * marginal_columnas) / (n * n)
    
    # 3. Kappa de Cohen
    kappa = (po - pe) / (1.0 - pe)
    
    # 4. Clasificacion segun Landis & Koch (1977)
    if kappa >= 0.81:
        interpretacion = "Casi perfecto (Almost perfect)"
    elif kappa >= 0.61:
        interpretacion = "Sustancial (Substantial)"
    elif kappa >= 0.41:
        interpretacion = "Moderado (Moderate)"
    elif kappa >= 0.21:
        interpretacion = "Regular (Fair)"
    else:
        interpretacion = "Leve / Pobre"
        
    print("=" * 70)
    print(f"FASE: {nombre_fase}")
    print("=" * 70)
    
    df_mat = pd.DataFrame(matriz, index=[f"Test: {e}" for e in etiquetas], columns=[f"Retest: {e}" for e in etiquetas])
    print("\nMatriz de Contingencia (n = 27):")
    print(df_mat)
    
    print(f"\nResultados Estadisticos:")
    print(f"- Total de muestra (n):           {int(n)} estudios (20.6 % del corpus)")
    print(f"- Acuerdos exactos:              {int(acuerdos)} de {int(n)}")
    print(f"- Proporcion observada (Po):      {po:.3f} ({po * 100:.1f} %)")
    print(f"- Proporcion azar esperada (Pe):  {pe:.3f} ({pe * 100:.1f} %)")
    print(f"- COEFICIENTE KAPPA (k):          {kappa:.2f}")
    print(f"- Interpretacion (Landis & Koch): {interpretacion}\n")
    
    return po, pe, kappa

if __name__ == '__main__':
    print("\nREPORTE DE FIABILIDAD METODOLOGICA TEST-RETEST (KAPPA DE COHEN)")
    print("Protocolo: 3 semanas de separacion temporal a ciegas | n = 27 estudios\n")
    
    # 1. Fase de Cribado (Titulo y Resumen) - Binaria: Incluir / Excluir
    mat_cribado = [
        [19, 1],  # Test: Incluir
        [1, 6]    # Test: Excluir
    ]
    calcular_kappa_cohen(mat_cribado, ["Incluir", "Excluir"], "1. Cribado Tematico por Titulo y Resumen")
    
    # 2. Fase de Elegibilidad (Texto Completo) - Binaria: Incluir / Excluir
    mat_elegibilidad = [
        [22, 1],  # Test: Incluir
        [0, 4]    # Test: Excluir
    ]
    calcular_kappa_cohen(mat_elegibilidad, ["Incluir", "Excluir"], "2. Elegibilidad a Texto Completo (Kitchenham / AMSTAR 2)")
    
    # 3. Taxonomia de Familias Algoritmicas (PI1) - Multiclase (4 familias)
    # Total n = 27: 25 acuerdos, 2 discrepancias (resueltas con asesor)
    etiquetas_pi1 = ["Transformers/Multimodal", "Hibridos CNN/OCR", "Vision-Language (VLM)", "Grafos (GNN)"]
    mat_pi1 = [
        [12, 1, 0, 0],
        [0, 6, 0, 0],
        [1, 0, 4, 0],
        [0, 0, 0, 3]
    ]
    calcular_kappa_cohen(mat_pi1, etiquetas_pi1, "3. Asignacion Taxonomica de Arquitecturas IA (PI1)")
    
    # 4. Sintesis Comparativa SWiM (PI3) - Multiclase (3 direcciones de efecto)
    # Total n = 27: 25 acuerdos, 2 discrepancias
    etiquetas_pi3 = ["Mejora (+1)", "Paridad (0)", "Empeora (-1)"]
    mat_pi3 = [
        [20, 1, 0],
        [1, 3, 0],
        [0, 0, 2]
    ]
    calcular_kappa_cohen(mat_pi3, etiquetas_pi3, "4. Direccion del Efecto SWiM vs. Metodos Tradicionales (PI3)")
