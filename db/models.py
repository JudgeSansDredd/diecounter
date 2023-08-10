from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Parent
class DieType(Base):
    __tablename__ = "die_types"

    # Some fields
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[int] = mapped_column(Integer)

    # Parent -> Children
    image_classifications: Mapped[list["ImageClassification"]] = relationship(
        back_populates="die_type"
    )


# Child
class ImageClassification(Base):
    __tablename__ = "image_classification"

    # Some fields
    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign key (this is child object)
    die_type_id: Mapped[int] = mapped_column(ForeignKey("die_types.id"))

    # Child -> Parent
    die_type: Mapped["DieType"] = relationship(back_populates="image_classifications")
