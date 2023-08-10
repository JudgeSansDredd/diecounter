from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class ImageClassification(Base):
    __tablename__ = "image_classification"

    id: Mapped[int] = mapped_column(primary_key=True)
    die_type: Mapped[int] = mapped_column(Integer)
    die_value: Mapped[int] = mapped_column(Integer)
    image_path: Mapped[str] = mapped_column(String)
