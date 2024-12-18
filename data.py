from models import *
db_init()
clients = [
    Client(first_name="Иван4", last_name="Иванов", address="ул. Ленина, 10", phone="+79001112233"),
    Client(first_name="Мария4", last_name="Петрова", address="ул. Пушкина, 5", phone="+790033335566"),
    Client(first_name="Саша4", last_name="Курочкин", address="ул. Новачева, 12", phone="+79002225561"),
    Client(first_name="Михаил4", last_name="Боярский", address="ул. Луганская, 45", phone="+7934344445564"),
    Client(first_name="Василий4", last_name="Остров", address="ул. Сальная, 6", phone="+790053535568")
]

post_offices = [
    PostOffice(address="ул. Ленина, 10", working_hours="09:00-18:00", contact_phone="+79001112233"),
    PostOffice(address="ул. Пушкина, 5", working_hours="09:00-18:00", contact_phone="+79004445566"),
    PostOffice(address="ул. Новачева, 12", working_hours="09:00-21:00", contact_phone="+79004445561"),
    PostOffice(address="ул. Сальная, 6", working_hours="09:00-18:00", contact_phone="+79004445565"),
    PostOffice(address="ул. Новачева, 48", working_hours="09:00-21:00", contact_phone="+79004559561")
]
PostOffice1=post_offices[0]
PostOffice2=post_offices[1]
PostOffice3=post_offices[2]
PostOffice4=post_offices[3]

with Session(engine) as session:
    session.add(PostOffice1)
    session.add(PostOffice2)
    session.add(PostOffice3)
    session.add(PostOffice4)
    session.commit()
    session.refresh(PostOffice1)
    session.refresh(PostOffice2)
    session.refresh(PostOffice3)
    session.refresh(PostOffice4)

employees = [
    Employee(first_name="Алексей", last_name="Смирнов", position="Почтальон", post_office_id=PostOffice1.id),
    Employee(first_name="Ольга", last_name="Сидорова", position="Оператор", post_office_id=PostOffice1.id),
    Employee(first_name="Иван", last_name="Сидоров", position="Менеджер", post_office_id=PostOffice1.id),
    Employee(first_name="Олег", last_name="Курочкин", position="Почтальон", post_office_id=PostOffice2.id),
    Employee(first_name="Василий", last_name="Свирин", position="Оператор", post_office_id=PostOffice2.id),
    Employee(first_name="Дмитрий", last_name="Шкаликов", position="Менеджер", post_office_id=PostOffice2.id),
    Employee(first_name="Олег", last_name="Чернов", position="Почтальонр", post_office_id=PostOffice3.id),
    Employee(first_name="Сергей", last_name="Кузьмин", position="Оператор", post_office_id=PostOffice3.id),
    Employee(first_name="Ирина", last_name="Альева", position="Менеджер", post_office_id=PostOffice3.id),
    Employee(first_name="Наталья", last_name="Фридманова", position="Менеджер", post_office_id=PostOffice3.id)
]

# employees = [
#     Employee(first_name="Алексей", last_name="Смирнов", position="Почтальон", post_office_id=1),
#     Employee(first_name="Ольга", last_name="Сидорова", position="Оператор", post_office_i=1),
#     Employee(first_name="Иван", last_name="Сидоров", position="Менеджер", post_office_id=1),
#     Employee(first_name="Олег", last_name="Курочкин", position="Почтальон", post_office_id=2),
#     Employee(first_name="Василий", last_name="Свирин", position="Оператор", post_office_id=2),
#     Employee(first_name="Дмитрий", last_name="Шкаликов", position="Менеджер", post_office_id=2),
#     Employee(first_name="Олег", last_name="Чернов", position="Почтальонр", post_office_id=3),
#     Employee(first_name="Сергей", last_name="Кузьмин", position="Оператор", post_office_id=3),
#     Employee(first_name="Ирина", last_name="Альева", position="Менеджер", post_office_id=3),
#     Employee(first_name="Наталья", last_name="Фридманова", position="Менеджер", post_office_id=3)
# ]


correspondences = [
    Correspondence(employee_id=1, service_id=1, weight=0.1, send_date="2024-01-01", receive_date="2024-01-05", sender_id=1, receiver_id=2, post_id=1),
    Correspondence(employee_id=2, service_id=1, weight=0.2, send_date="2024-01-02", receive_date="2024-01-06", sender_id=2, receiver_id=3, post_id=1),
    Correspondence(employee_id=2, service_id=2, weight=1.2, send_date="2024-01-02", receive_date="2024-01-06", sender_id=1, receiver_id=3, post_id=2),
    Correspondence(employee_id=2, service_id=2, weight=3.4, send_date="2024-01-05", receive_date="2024-01-07", sender_id=2, receiver_id=3, post_id=3),
    Correspondence(employee_id=2, service_id=2, weight=2.0, send_date="2024-02-02", receive_date="2024-02-05", sender_id=4, receiver_id=5, post_id=4)
]

postal_services = [
    PostalService(name="Отправка письма", description="Услуга по отправке письма", cost=50.0),
    PostalService(name="Отправка посылки", description="Услуга по отправке посылки", cost=200.0)
]


def fill_database():
    with Session(engine) as session:
        session.add_all(clients)
        session.add_all(post_offices)
        post_offices[0].manager_id = 1
        post_offices[1].manager_id = 2
        session.add_all(employees)
        session.add_all(correspondences)
        session.add_all(postal_services)
        session.commit()


def print_table_data():
    with Session(engine) as session:
        #Клиенты
        clients = session.exec(select(Client)).all()
        print("Клиенты:")
        for client in clients:
            print(client)
        
        #Почтовые отделения
        post_offices = session.exec(select(PostOffice)).all()
        print("\nПочтовые отделения:")
        for post_office in post_offices:
            print(post_office)
        
        #Сотрудники
        employees = session.exec(select(Employee)).all()
        print("\nСотрудники:")
        for employee in employees:
            print(employee)
        
        #Корреспонденция
        correspondences = session.exec(select(Correspondence)).all()
        print("\nКорреспонденция:")
        for correspondence in correspondences:
            print(correspondence)
        
        #Почтовые услуги
        postal_services = session.exec(select(PostalService)).all()
        print("\nПочтовые услуги:")
        for postal_service in postal_services:
            print(postal_service)

