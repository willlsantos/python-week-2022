from sqlmodel import Session, create_engine

from beerlog import models
from beerlog.config import settings

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
