from flask import render_template, request, redirect, url_for, session
from backend.Modelos.database import db
from backend.Modelos.Info_diaria import Info_diaria  # Asegúrate de tener este modelo importado

def delete_info_diaria(id_info_diaria):
    if 'is_admin' not in session:
        return redirect(url_for('login'))

    info = Info_diaria.query.get(id_info_diaria)
    
    if info:
        db.session.delete(info)
        db.session.commit()

    return redirect(url_for('info_diaria'))
