def render_patient_list(patients):
    return[
        {
            "id":patient.id,
            "name":patient.name,
            "last_name":patient.last_name,
            "diagnosis":patient.diagnosis,
            "ci":patient.ci,
        }
        for patient in patients
    ]


def render_patient_detail(patient):
    return{
        "id":patient.id,
        "name":patient.name,
        "last_name":patient.last_name,
        "diagnosis":patient.diagnosis,
        "ci":patient.ci
    }