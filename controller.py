from sqlalchemy.orm import Session
from model import News
from schemas import NewsSchema


def get_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(News).offset(skip).limit(limit).all()


def get_news_by_id(db: Session, news_id: int):
    return db.query(News).filter(News.id == news_id).first()


def create_news(db: Session, news: NewsSchema):
    _news = News(title=news.title, description=news.description)
    db.add(_news)
    db.commit()
    db.refresh(_news)
    return _news


def remove_news(db: Session, news_id: int):
    _news = get_news_by_id(db=db, news_id=news_id)
    db.delete(_news)
    db.commit()


def update_news(db: Session, news_id: int, title: str, description: str):
    _news = get_news_by_id(db=db, news_id=news_id)

    _news.title = title
    _news.description = description

    db.commit()
    db.refresh(_news)
    return _news