from data import *
from shemess import *

def create_PostOffices(session: Session, post_office: PostOfficeCreate):
    db_post_office = PostOffice.model_validate(post_office)
    session.add(db_post_office)
    session.commit()
    session.refresh(db_post_office)
    return db_post_office

def get_PostOffices(session: Session):
    return session.exec(select(PostOffice)).all()

def get_PostOffice(session: Session, post_office_id: int):
     return session.get(PostOffice, post_office_id)

def put_PostOffice(session: Session, post_office_id: int, adress: str, working_hours: str, contact_phone: str, manager_id: int):
     db_update = session.get(PostOffice, post_office_id)
     db_update.address = adress
     db_update.working_hours = working_hours
     db_update.contact_phone = contact_phone
     db_update.manager_id = manager_id
     session.add(db_update)
     session.commit()
     session.refresh(db_update)
    
def del_PostOffice(session: Session, post_office_id: int):
    db_delete = session.get(PostOffice, post_office_id)
    session.delete(db_delete)
    session.commit()

def create_Clients(session: Session, client: ClientCreate):
    db_client = Client.model_validate(client)
    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client

def get_Clients(session: Session):
    return session.exec(select(Client)).all()

def get_Client(session: Session, client_id: int):
     return session.get(Client, client_id)

def put_Client(session: Session, client_id: int, first_name: str, last_name: str, adress: str, phone: str):
     db_update = session.get(Client, client_id)
     db_update.first_name= first_name
     db_update.last_name = last_name
     db_update.address = adress
     db_update.phone = phone
     session.add(db_update)
     session.commit()
     session.refresh(db_update)
    
def del_Client(session: Session, client_id: int):
    db_delete = session.get(Client, client_id)
    session.delete(db_delete)
    session.commit()

def create_Employees(session: Session, employee: EmployeeCreate):
    db_employee = Employee.model_validate(employee)
    session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return db_employee

def get_Employees(session: Session):
    return session.exec(select(Employee)).all()

def get_Employee(session: Session, empluyee_id: int):
     return session.get(Employee, empluyee_id)

def put_Employee(session: Session, employee_id: int, first_name: str, last_name: str, position: str, post_office_id: int):
     db_update = session.get(Employee, employee_id)
     db_update.first_name = first_name
     db_update.last_name = last_name
     db_update.position = position
     db_update.post_office_id = post_office_id
     session.add(db_update)
     session.commit()
     session.refresh(db_update)
    
def del_Employee(session: Session, employee_id: int):
    db_delete = session.get(Employee, employee_id)
    session.delete(db_delete)
    session.commit()

def create_Correspondences(session: Session, correspondence: CorrespondenceCreate):
    db_correspondence = Correspondence.model_validate(correspondence)
    session.add(db_correspondence)
    session.commit()
    session.refresh(db_correspondence)
    return db_correspondence

def get_Correspondences(session: Session):
    return session.exec(select(Correspondence)).all()

def get_Correspondence(session: Session, correspondence_id: int):
     return session.get(Correspondence, correspondence_id)

def create_PostalServices(session: Session, postal_service: PostalServiceCreate):
    db_postal_service = PostalService.model_validate(postal_service)
    session.add(db_postal_service)
    session.commit()
    session.refresh(db_postal_service)
    return db_postal_service

def get_PostalService(session: Session):
    return session.exec(select(PostalService)).all()

def get_PostalServices(session: Session, postal_service_id: int):
     return session.get(PostalService, postal_service_id)

#заполнение бд данными из functions_data
#fill_database()


#print_table_data()

def get_request_1(session: Session):
        avgprice = session.exec(select(func.avg(PostalService.cost))).first()
        return {"Средняя цена за услуги" : avgprice}

def get_request_2(session: Session):
        workers_p1 = session.exec(select(Employee).where(Employee.post_office_id==1)).all()
        res = []
        for w in workers_p1:
            res.append({"Имя" : w.first_name, "Фамилия" : w.last_name, "Должность:" : w.position, "id" : w.id})
        return {"Сотрудники первого почтового отделения" : res}

def get_request_3(session: Session):
        senders_lenin = session.exec(select(Client.first_name,Client.last_name).join(Correspondence, onclause=Correspondence.sender_id==Client.id).join(PostOffice).where(PostOffice.address=="ул. Ленина, 10")).all()
        res = []
        for s in senders_lenin:
            res.append({"Имя: " : s[0], "Фамилия" : s[1]})
        return {"Все люди, которые отправляли посылки с ул. Ленина, 10" : res}
    

    
