from typing import List
from fastapi import FastAPI, Response, status
from beerlog.core import get_beers_from_database
from beerlog.serializers import BeerOut
from beerlog.serializers import BeerIn
from beerlog.models import Beer
from beerlog.database import get_session

api = FastAPI(title="Beerlog")

@api.get("/beers/", response_model=List[BeerOut])
def list_beers():
    beers = get_beers_from_database()
    return beers

@api.post("/beers", response_model=BeerOut)
async def add_beer(beer_in: BeerIn, response: Response):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)

    response.status_code = status.HTTP_201_CREATED
    return beer