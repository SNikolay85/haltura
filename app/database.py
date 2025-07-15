from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import MetaData, String, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.sql import func
from typing_extensions import Annotated
from config import REAL_DB, PG_USER, PG_PASSWORD, PG_HOST, PG_PORT


PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{REAL_DB}"
engine = create_async_engine(PG_DSN, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)

my_metadata = MetaData()

str100 = Annotated[str, 100]
created_on = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now())]
updated_on = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())]


class Base(DeclarativeBase):
    metadata = my_metadata
    type_annotation_map = {
        str100: String(100),
    }

    create_on: Mapped[created_on]
    update_on: Mapped[updated_on]

    repr_cols_num = 2
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f'{col}={getattr(self, col)}')
        return f'<{self.__class__.__name__} {", ".join(cols)}>'


async def delete_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)


async def create_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
