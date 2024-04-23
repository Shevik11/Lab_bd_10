# generic_dao.py
from sqlalchemy.orm import sessionmaker

class GenericDAO:
    def __init__(self, session, model_class):
        self.session = session
        self.model_class = model_class

    def get(self, id):
        return self.session.query(self.model_class).get(id)

    def create(self, **values):
        obj = self.model_class(**values)
        self.session.add(obj)
        self.session.commit()
        return obj

    def update(self, obj, **values):
        for key, value in values.items():
            setattr(obj, key, value)
        self.session.commit()

    def delete(self, obj):
        self.session.delete(obj)
        self.session.commit()
