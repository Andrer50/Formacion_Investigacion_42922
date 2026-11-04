Add-Type -AssemblyName System.Drawing

$imgNames = @('fig2_evolucion_anual.png', 'fig3_vosviewer_geografia.png', 'fig4_burbujas_disenos_datasets.png', 'fig5_distribucion_qa_criterios.png')

foreach ($name in $imgNames) {
    $path = Join-Path 'project\resultados\outputs' $name
    $fullPath = (Resolve-Path $path).Path
    $bmp = [System.Drawing.Bitmap]::FromFile($fullPath)
    Write-Host "$name : $($bmp.Width) x $($bmp.Height)"
    $bmp.Dispose()
}

