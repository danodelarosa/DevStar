if ($env:VIRTUAL_ENV) {
    Write-Host "Estás dentro de un entorno virtual de Python en la ruta: $env:VIRTUAL_ENV"
} else {
    Write-Host "No estás dentro de un entorno virtual de Python."
}
