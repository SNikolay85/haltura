import enum

from sqlalchemy import Time, Enum, ForeignKey, Date, UniqueConstraint, BigInteger
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base
from typing_extensions import Annotated


intpk = Annotated[int, mapped_column(primary_key=True)]
# user_fk = Annotated[int, mapped_column(ForeignKey('user.telegram_id', ondelete="CASCADE"))]
master_fk = Annotated[int, mapped_column(ForeignKey('master.master_id', ondelete="CASCADE"))]
service_fk = Annotated[int, mapped_column(ForeignKey('service.service_id', ondelete="CASCADE"))]
str100 = Annotated[str, 100]


class User(Base):
    __tablename__ = 'user'

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str100] = mapped_column(nullable=False)  # Имя пользователя
    username: Mapped[str100] = mapped_column(nullable=True)  # Telegram username
    __table_args__ = (UniqueConstraint('telegram_id', 'first_name', 'username', name='user_uc'),)

    # Связь с заявками (один пользователь может иметь несколько заявок)
    applications: Mapped[list['Application']] = relationship(back_populates="user")

    repr_cols_num = 3
    repr_cols = tuple()


class Master(Base):
    __tablename__ = 'master'

    master_id: Mapped[intpk]
    master_name: Mapped[str100] = mapped_column(nullable=False)   # Имя мастера
    __table_args__ = (UniqueConstraint('master_id', 'master_name', name='master_uc'),)

    # Связь с заявками (один мастер может иметь несколько заявок)
    applications: Mapped[list['Application']] = relationship(back_populates="master")


class Service(Base):
    __tablename__ = 'service'

    service_id: Mapped[intpk]
    service_name: Mapped[str100] = mapped_column(nullable=False)  # Название услуги
    __table_args__ = (UniqueConstraint('service_id', 'service_name', name='service_uc'),)

    # Связь с заявками (одна услуга может быть частью нескольких заявок)
    applications: Mapped[list['Application']] = relationship(back_populates="service")


class Application(Base):
    __tablename__ = 'application'

    class GenderEnum(enum.Enum):
        male = "Мужской"
        female = "Женский"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.telegram_id', ondelete="CASCADE"))  # Внешний ключ на пользователя
    # user_id: Mapped[user_fk]
    master_id: Mapped[master_fk]
    service_id: Mapped[service_fk]
    appointment_date: Mapped[Date] = mapped_column(Date, nullable=False)  # Дата заявки
    appointment_time: Mapped[Time] = mapped_column(Time, nullable=False)  # Время заявки
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum), nullable=False)
    client_name: Mapped[str100] = mapped_column(nullable=False)  # Имя пользователя

    user: Mapped['User'] = relationship(back_populates="applications")
    master: Mapped['Master'] = relationship(back_populates="applications")
    service: Mapped['Service'] = relationship(back_populates="applications")

    repr_cols_num = 8
    repr_cols = tuple()
