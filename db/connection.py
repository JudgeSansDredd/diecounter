from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db.models import ImageClassification

from .models import Base


class Connection:
    def __init__(self):
        self.engine = create_engine("sqlite:///db/db.sqlite", echo=False)

    def init_db(self):
        Base.metadata.create_all(self.engine)

    def add_image_classification(self, die_type, die_value, image_path):
        kwargs = {
            "die_type": die_type,
            "die_value": die_value,
            "image_path": image_path,
        }
        with Session(self.engine) as session:
            image_classification = ImageClassification(**kwargs)
            session.add(image_classification)
            session.commit()

    def get_image_classification(self, image_path):
        with Session(self.engine) as session:
            stmt = select(ImageClassification).where(
                ImageClassification.image_path.__eq__(image_path)
            )
            return session.scalar(stmt)
