from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import NewsSchema, Request, Response, RequestNews
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_news_service(request: RequestNews, db: Session = Depends(get_db)):
    crud.create_book(db, news=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)


@router.get("/")
async def get_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _news = crud.get_news(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_news)



@router.get("/{news_id}")
async def read_item(news_id: int, db: Session = Depends(get_db)):
    _news = crud.get_news_by_id(db, news_id=news_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_news)


# @router.get("/news/{id}")
# async def read_item(id: int):
#     return {"news_id": id}

@router.patch("/update")
async def update_news(request: RequestNews, db: Session = Depends(get_db)):
    _news = crud.update_news(db, news_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_news)


@router.delete("/delete")
async def delete_news(request: RequestNews,  db: Session = Depends(get_db)):
    crud.remove_news(db, news_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)