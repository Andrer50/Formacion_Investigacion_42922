import docx
import struct
import os

def get_png_dimensions(fpath):
    with open(fpath, 'rb') as f:
        head = f.read(24)
        w, h = struct.unpack('>II', head[16:24])
        return w, h

REPLACEMENTS = {
    'Fig. 8': 'project/resultados/outputs/fig8_swim_barras_divergentes.png',
    'Fig. 9': 'project/resultados/outputs/fig9_heatmap_documentos_erp.png'
}

def update_doc_figures(docpath):
    print(f"=== UPDATING ONLY FIG. 8 AND FIG. 9 IN: {docpath} ===")
    doc = docx.Document(docpath)
    
    updated_count = 0
    for i, p in enumerate(doc.paragraphs):
        blips = p._element.xpath('.//a:blip/@r:embed')
        if not blips:
            continue
            
        next_text = doc.paragraphs[i+1].text.strip() if i+1 < len(doc.paragraphs) else ''
        for fig_key, img_path in REPLACEMENTS.items():
            if next_text.startswith(fig_key):
                rId = blips[0]
                new_w, new_h = get_png_dimensions(img_path)
                with open(img_path, 'rb') as f:
                    new_bytes = f.read()
                    
                # 1. Update image blob
                rel = doc.part.rels[rId]
                rel.target_part._blob = new_bytes
                
                # 2. Update XML extent cx/cy
                for tag in ['.//wp:extent', './/a:xfrm/a:ext']:
                    for ext in p._element.xpath(tag):
                        cx = int(ext.get('cx'))
                        new_cy = int(cx * (new_h / new_w))
                        ext.set('cy', str(new_cy))
                        
                updated_count += 1
                print(f"  [P{i:3d}] Updated {fig_key} (rId: {rId}) -> new size: {new_w}x{new_h}, ratio: {new_h/new_w:.4f}")
                
    doc.save(docpath)
    print(f"Successfully saved {docpath} with {updated_count} figures updated.\n")

if __name__ == '__main__':
    update_doc_figures('project/shared/RSL_Sergio_Rupay.docx')
    update_doc_figures('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    print("FIG. 8 AND FIG. 9 UPDATED CLEANLY WITHOUT TOUCHING ANY OTHER FIGURES OR TEXT!")

