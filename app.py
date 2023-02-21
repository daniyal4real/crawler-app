from fastapi import FastAPI
import model
from routes import router
from config import engine
from inform import *
import crud 


model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/news", tags=["news"])
# start()



# async def get_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     _news = crud.get_news(db, skip, limit)
#     return Response(status="Ok", code="200", message="Success fetch all data", result=_news)


