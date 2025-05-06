from flask import render_template


TIPOS_VALIDOS = ['masa_muscular', 'peso', 'grasa_corporal']

def mostrar_estadistica(tipo_estadistica):
    if tipo_estadistica in TIPOS_VALIDOS:
        # Puedes pasar el tipo al template para personalizarlo
        return render_template('estadisticas.html', tipo=tipo_estadistica)
    else:
        return "Tipo de estadística no encontrada", 404