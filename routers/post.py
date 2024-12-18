from fastapi import APIRouter, Depends, HTTPException
from equests import *
from shemess import PostOfficeCreate, PostOfficeRead
from models import Session, List, get_session

router = APIRouter()

@router.post("/", response_model=PostOfficeRead)
async def create_post_office_ep(post_office: PostOfficeCreate, session: Session = Depends(get_session)):
    return create_PostOffices(session, post_office)

@router.get("/",response_model=List[PostOfficeRead])
async def get_post_offices_ep(session: Session = Depends(get_session)):
    return get_PostOffices(session)

@router.get("/{post_office_id}", response_model=PostOfficeRead)
async def get_post_office_ep(post_office_id: int, session: Session = Depends(get_session)):
    post_office = get_PostOffice(session, post_office_id)
    if post_office is None:
        raise HTTPException(status_code=404, detail="Post Office not found")
    return post_office

@router.put("/{post_office_id}",response_model=PostOfficeRead)
async def put_post_office_ep(post_office_id: int, address: str, working_hours: str, contact_phone: str, manager_id: int ,session: Session = Depends(get_session)):
    post_office = put_PostOffice(session, post_office_id, address, working_hours, contact_phone, manager_id)
    return post_office

@router.delete("/{post_office_id}", response_model=PostOfficeRead)
async def del_post_office_ep(post_office_id: int, session: Session = Depends(get_session)):
    return del_PostOffice(session, post_office_id)
