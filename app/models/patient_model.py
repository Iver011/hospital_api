from app.database import db

class Patient(db.Model):

    __tablename__="patients"


    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    diagnosis=db.Column(db.String(100), nullable=False)
    ci=db.Column(db.Integer, nullable=False)

    def __init__(self, name, last_name,diagnosis, ci):
        self.name=name
        self.last_name=last_name
        self.diagnosis=diagnosis
        self.ci=ci

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Patient.query.all()

    @staticmethod
    def get_by_id(id):
        return Patient.query.get(id)

    def update(self, name=None, last_name=None, diagnosis=None, ci=None):
        if name is not None:
            self.name=name
        if last_name is not None:
            self.last_name=last_name
        if diagnosis is not diagnosis:
            self.diagnosis=diagnosis
        if ci is not None:
            self.ci=ci
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


