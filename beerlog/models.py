from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import BaseModel, validator
from statistics import mean
from datetime import datetime
from pydantic import field_validator


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @field_validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} o valor deve ser entre 1 e 10")
        return v

    @field_validator("rate", mode="before")
    def calculo_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


try:
    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)
except RuntimeError:
    print("Zika demais")
