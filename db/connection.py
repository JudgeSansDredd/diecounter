from sqlalchemy import create_engine

from .models import Base


class Connection:
    def __init__(self):
        self.engine = create_engine("sqlite:///db/db.sqlite", echo=True)
        self.create_models()

    def create_models(self):
        Base.metadata.create_all(self.engine)
