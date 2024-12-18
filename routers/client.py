from fastapi import APIRouter, Depends, HTTPException
from equests import create_Clients, get_Clients, get_Client, put_Client, del_Client
from shemess import ClientCreate, ClientRead
from models import Session, List, get_session

router = APIRouter()

@router.post("/", response_model=ClientCreate)
async def create_client_ep(client: ClientCreate, session: Session = Depends(get_session)):
    return create_Clients(session, client)

@router.get("/",response_model=List[ClientRead])
async def get_clients_ep(session: Session = Depends(get_session)):
    return get_Clients(session)

@router.get("/{client_id}", response_model=ClientRead)
async def get_client_ep(client_id: int, session: Session = Depends(get_session)):
    client = get_Client(session, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}",response_model=ClientRead)
async def put_client_ep(client_id: int, address: str, working_hours: str, contact_phone: str, manager_id: int ,session: Session = Depends(get_session)):
    client = put_Client(session, client_id, address, working_hours, contact_phone, manager_id)
    return client

@router.delete("/{client_id}", response_model=ClientRead)
async def del_client_ep(client_id: int, session: Session = Depends(get_session)):
    return del_Client(session, client_id)

