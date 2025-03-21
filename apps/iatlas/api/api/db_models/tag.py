from api import db
from . import Base
from api.enums import tag_type_enum


class Tag(Base):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    color = db.Column(db.String, nullable=True)
    long_display = db.Column(db.String, nullable=True)
    short_display = db.Column(db.String, nullable=True)
    tag_type = db.Column(tag_type_enum, nullable=False)
    order = db.Column(db.Integer, nullable=True)

    data_sets = db.relationship(
        "Dataset", lazy="noload", uselist=True, secondary="datasets_to_tags"
    )

    publications = db.relationship(
        "Publication", lazy="noload", uselist=True, secondary="tags_to_publications"
    )

    related_tags = db.relationship(
        "Tag",
        foreign_keys="TagToTag.tag_id",
        lazy="noload",
        secondary="tags_to_tags",
        back_populates="tags",
        uselist=True,
    )

    samples = db.relationship(
        "Sample", lazy="noload", uselist=True, secondary="samples_to_tags"
    )

    tags = db.relationship(
        "Tag",
        foreign_keys="TagToTag.related_tag_id",
        lazy="noload",
        secondary="tags_to_tags",
        back_populates="related_tags",
        uselist=True,
    )

    def __repr__(self):
        return "<Tag %r>" % self.name
