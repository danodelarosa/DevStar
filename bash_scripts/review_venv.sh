#!/bin/bash

# Comprueba si la variable de entorno VIRTUAL_ENV está definida
if [ -n "$VIRTUAL_ENV" ]; then
    echo "El entorno virtual está activo en: $VIRTUAL_ENV"
else
    # Comprueba si el archivo "activate" existe en el directorio actual
    if [ -f "activate" ]; then
        echo "El entorno virtual está activo en el directorio actual."
    else
        echo "No se ha activado un entorno virtual."
    fi
fi
