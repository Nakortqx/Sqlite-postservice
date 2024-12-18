from sqlmodel import Field, Session, SQLModel, create_engine, Relationship, select
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.engine import URL
from typing import List, Optional
from datetime import datetime, time

# engine = create_engine("postgresql://postgres:password@localhost:5432/meth3?client_encoding=UTF8")

engine = create_engine("sqlite:///database.db?check_same_thread=False")


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    address: str
    phone: str 


class PostOffice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    address: str
    working_hours: str
    contact_phone: str
    #manager_id: Optional[int] = Field(default=None,foreign_key="employee.id")
    manager_id: Optional[int] = Field(default=None,sa_column=Column(ForeignKey('employee.id',use_alter=True,name='applications_employee_id_fkey')))

class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    position: str
    #post_office_id: Optional[int] = Field(default=None, foreign_key="postoffice.id")
    post_office_id: Optional[int] = Field(default=None,sa_column=Column(ForeignKey('postoffice.id',use_alter=True,name='applications_postoffice_id_fkey')))
    correspondences: List["Correspondence"] = Relationship(back_populates="employee")

class Correspondence(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    post_id: Optional[int] = Field(default=None, foreign_key="postoffice.id")
    employee_id: Optional[int] = Field(default=None, foreign_key="employee.id")
    service_id: str = Field(default=None, foreign_key="postalservice.id")
    weight: float
    #send_date: Optional[datetime] = Field(default=None, alias="Дата_отправки")
    send_date: str = Field(default=None)
    #receive_date: Optional[datetime] = Field(default=None, alias="Дата_получения")
    receive_date: str = Field(default=None)
    sender_id: Optional[int] = Field(default=None, foreign_key="client.id")
    receiver_id: Optional[int] = Field(default=None, foreign_key="client.id")
    employee: Optional[Employee] = Relationship(back_populates="correspondences")
    #sender: Optional[Client] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Correspondence.sender_id]"})
    #receiver: Optional[Client] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Correspondence.receiver_id]"})

class PostalService(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    cost: float

def db_init():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def reset():
    SQLModel.metadata.drop_all(engine)