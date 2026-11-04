Add-Type -AssemblyName System.Drawing

$configs = @(
    @{ Name = 'fig2_evolucion_anual.png'; Top = 135; Bottom = 1015 },
    @{ Name = 'fig3_vosviewer_geografia.png'; Top = 130; Bottom = 1075 },
    @{ Name = 'fig4_burbujas_disenos_datasets.png'; Top = 145; Bottom = 1070 },
    @{ Name = 'fig5_distribucion_qa_criterios.png'; Top = 130; Bottom = 1055 }
)

foreach ($cfg in $configs) {
    $path = Join-Path 'project\resultados\outputs' $cfg.Name
    $fullPath = (Resolve-Path $path).Path
    $backupPath = $fullPath -replace '\.png$', '_backup_before_clean.png'
    
    # Create backup if not exists
    if (-not (Test-Path $backupPath)) {
        Copy-Item -Path $fullPath -Destination $backupPath
    }
    
    $bmp = [System.Drawing.Bitmap]::FromFile($backupPath)
    $w = $bmp.Width
    $h = $cfg.Bottom - $cfg.Top
    
    $rect = [System.Drawing.Rectangle]::new(0, $cfg.Top, $w, $h)
    $cropped = $bmp.Clone($rect, $bmp.PixelFormat)
    $bmp.Dispose()
    
    # Save back to original file
    $cropped.Save($fullPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $cropped.Dispose()
    
    Write-Host "Cleaned and cropped: $($cfg.Name) -> New dimensions: $w x $h (Removed internal Fig header & Footer)"
}

