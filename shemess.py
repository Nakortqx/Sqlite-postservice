from typing import Optional
from pydantic import BaseModel

class PostOfficeCreate(BaseModel):
    address: str
    working_hours: str
    contact_phone: str
    manager_id: Optional[int]

class PostOfficeRead(PostOfficeCreate):
    id: int

class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    address: str 
    phone: str

class ClientRead(ClientCreate):
    id: int

class EmployeeCreate(BaseModel):
    first_name: str 
    last_name: str 
    position: str 
    post_office_id: Optional[int]
    correspondences: list

class EmployeeRead(EmployeeCreate):
    id: int

class CorrespondenceCreate(BaseModel):
    post_id: Optional[int]
    employee_id: Optional[int]
    service_id: str
    weight: float
    send_date: str
    receive_date: str 
    sender_id: Optional[int]
    receiver_id: Optional[int]

class CorrespondenceRead(CorrespondenceCreate):
    id: int

class PostalServiceCreate(BaseModel):
    name: str
    description: str
    cost: float

class PostalServiceRead(PostalServiceCreate):
    id: int
