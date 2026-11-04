Add-Type -AssemblyName System.Drawing

$imgNames = @('fig2_evolucion_anual.png', 'fig3_vosviewer_geografia.png', 'fig4_burbujas_disenos_datasets.png', 'fig5_distribucion_qa_criterios.png')

foreach ($name in $imgNames) {
    $path = Join-Path 'project\resultados\outputs' $name
    $fullPath = (Resolve-Path $path).Path
    $bmp = [System.Drawing.Bitmap]::FromFile($fullPath)
    
    # Check rows for non-white pixels in top 200 rows and bottom 150 rows
    $w = $bmp.Width
    $h = $bmp.Height
    
    # Top scan
    $firstNonWhite = -1
    $lastTitleRow = -1
    for ($y = 0; $y -lt [Math]::Min(300, $h); $y++) {
        $hasColor = $false
        for ($x = 0; $x -lt $w; $x += 4) {
            $c = $bmp.GetPixel($x, $y)
            if ($c.R -lt 250 -or $c.G -lt 250 -or $c.B -lt 250) {
                $hasColor = $true
                break
            }
        }
        if ($hasColor -and $firstNonWhite -eq -1) {
            $firstNonWhite = $y
        }
        if (-not $hasColor -and $firstNonWhite -ne -1 -and $lastTitleRow -eq -1) {
            $lastTitleRow = $y
        }
    }
    
    # Bottom scan
    $bottomFirstNonWhite = -1
    for ($y = $h - 1; $y -ge [Math]::Max(0, $h - 250); $y--) {
        $hasColor = $false
        for ($x = 0; $x -lt $w; $x += 4) {
            $c = $bmp.GetPixel($x, $y)
            if ($c.R -lt 250 -or $c.G -lt 250 -or $c.B -lt 250) {
                $hasColor = $true
                break
            }
        }
        if ($hasColor) {
            $bottomFirstNonWhite = $y
            break
        }
    }
    
    Write-Host "$name (H=$h): First non-white row=$firstNonWhite, End of title gap=$lastTitleRow, Bottom non-white=$bottomFirstNonWhite"
    $bmp.Dispose()
}

