from models import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from dataclasses import dataclass

@dataclass
class Sensor(db.Model):
    __tablename__ = 'sensor_table'
    id:Mapped[int]=mapped_column(primary_key=True)
    temperature:Mapped[float]=mapped_column(nullable=False)
    humidity:Mapped[float]=mapped_column(nullable=False)
    air_quality:Mapped[float]=mapped_column(nullable=False)
    date_hour:Mapped[str]=mapped_column(String(100),nullable=False)