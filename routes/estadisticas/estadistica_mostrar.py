from flask import render_template

# Lista de tipos de estadísticas válidos que se pueden mostrar
TIPOS_VALIDOS = ['masa_muscular', 'peso', 'grasa_corporal']

def mostrar_estadistica(tipo_estadistica):
    # Verifica si el tipo de estadística solicitado está en la lista de tipos válidos
    if tipo_estadistica in TIPOS_VALIDOS:
        # Si es válido, renderiza la plantilla HTML y pasa el tipo de estadística como contexto
        return render_template('estadisticas.html', tipo=tipo_estadistica)
    else:
        # Si no es válido, devuelve un mensaje de error con un código de estado 404
        return "Tipo de estadística no encontrada", 404