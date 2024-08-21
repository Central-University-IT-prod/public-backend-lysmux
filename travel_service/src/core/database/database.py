from sqlalchemy import URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


def get_session_maker(database_url: URL) -> async_sessionmaker:
    engine = create_async_engine(url=database_url, pool_pre_ping=True)
    session_maker = async_sessionmaker(bind=engine)

    return session_maker
