Add-Type -AssemblyName System.Drawing

function Analyze-Bands($imgName) {
    $path = Join-Path 'project\resultados\outputs' $imgName
    $fullPath = (Resolve-Path $path).Path
    $bmp = [System.Drawing.Bitmap]::FromFile($fullPath)
    Write-Host "=== $imgName ($($bmp.Width) x $($bmp.Height)) ==="
    
    # Check every 5 rows from y=0 to 200
    for ($y = 0; $y -le 200; $y += 5) {
        $nonWhite = 0
        for ($x = 0; $x -lt $bmp.Width; $x += 2) {
            $c = $bmp.GetPixel($x, $y)
            if ($c.R -lt 250 -or $c.G -lt 250 -or $c.B -lt 250) {
                $nonWhite++
            }
        }
        if ($nonWhite -gt 0) {
            Write-Host "  Top y=$y : nonWhite=$nonWhite"
        }
    }
    
    # Check from H-150 to H
    for ($y = $bmp.Height - 150; $y -lt $bmp.Height; $y += 5) {
        $nonWhite = 0
        for ($x = 0; $x -lt $bmp.Width; $x += 2) {
            $c = $bmp.GetPixel($x, $y)
            if ($c.R -lt 250 -or $c.G -lt 250 -or $c.B -lt 250) {
                $nonWhite++
            }
        }
        if ($nonWhite -gt 0) {
            Write-Host "  Bottom y=$y : nonWhite=$nonWhite"
        }
    }
    $bmp.Dispose()
}

Analyze-Bands 'fig2_evolucion_anual.png'
Analyze-Bands 'fig3_vosviewer_geografia.png'
Analyze-Bands 'fig4_burbujas_disenos_datasets.png'
Analyze-Bands 'fig5_distribucion_qa_criterios.png'

