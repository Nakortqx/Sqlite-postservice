from fastapi import APIRouter, Depends
from equests import get_request_1, get_request_2, get_request_3
from models import Session, get_session

router = APIRouter()

@router.get("/",response_model=None)
async def show_requests(session: Session = Depends(get_session)):
    return get_request_1(session), get_request_2(session), get_request_3(session)
