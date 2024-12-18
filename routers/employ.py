from fastapi import APIRouter, Depends, HTTPException
from equests import create_Employees, get_Employees, get_Employee, put_Employee, del_Employee
from shemess import EmployeeCreate, EmployeeRead
from models import Session, List, get_session

router = APIRouter()

@router.post("/", response_model=EmployeeCreate)
async def create_employees_ep(employee: EmployeeCreate, session: Session = Depends(get_session)):
    return create_Employees(session, employee)

@router.get("/",response_model=List[EmployeeRead])
async def get_employees_ep(session: Session = Depends(get_session)):
    return get_Employees(session)

@router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee_ep(employee_id: int, session: Session = Depends(get_session)):
    employee = get_Employee(session, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}",response_model=EmployeeRead)
async def put_employee_ep(employee_id: int, address: str, working_hours: str, contact_phone: str, manager_id: int ,session: Session = Depends(get_session)):
    employee = put_Employee(session, employee_id, address, working_hours, contact_phone, manager_id)
    return employee

@router.delete("/{employee_id}", response_model=EmployeeRead)
async def del_employee_ep(employee_id: int, session: Session = Depends(get_session)):
    return del_Employee(session, employee_id)
