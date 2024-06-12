from flask import Blueprint, jsonify, request
from app.models.patient_model import Patient
from app.views.patient_view import render_patient_detail, render_patient_list
from app.utils.decorators import roles_required,jwt_required


patient_bp=Blueprint("patient",__name__)

@patient_bp.route("/patients", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_patients():
    patients=Patient.get_all()
    return jsonify(render_patient_list(patients))

@patient_bp.route("/patients/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["user","admin"])
def get_patient(id):
    patient=Patient.get_by_id(id)
    if patient:
        return jsonify(render_patient_detail(patient))
    return jsonify({"error":"Paciente no encontrado"}),404

@patient_bp.route("/patients", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_patient():
    data=request.json
    name=data.get("name")
    last_name=data.get("last_name")
    diagnosis=data.get("diagnosis")
    ci=data.get("ci")

    if not name or not last_name or not diagnosis or not ci:
        return jsonify({"error":"Faltan datos requeridos"}),400
    
    patient=Patient(name=name,last_name=last_name,diagnosis=diagnosis,ci=ci)
    patient.save()
    return jsonify(render_patient_detail(patient)),201


@patient_bp.route("/patients/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_patient(id):
    patient=Patient.get_by_id(id)
    if not patient:
        return jsonify({"error": "Paciente no encontrado"}),404
    
    data=request.json
    name=data.get("name")
    last_name=data.get("last_name")
    diagnosis=data.get("diagnosis")
    ci=data.get("ci")

    patient.update(name=name,last_name=last_name,diagnosis=diagnosis,ci=ci)
    return jsonify(render_patient_detail(patient))

@patient_bp.route("/patients/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_patient(id):
    patient=Patient.get_by_id(id)
    if not patient:
        return jsonify({"error":"Paciente no encontrado"}),404
    patient.delete()
    return "",204




    

