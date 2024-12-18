import uvicorn
from fastapi import FastAPI
from models import db_init, reset
from data import fill_database, print_table_data
from routers import post as PostRoute, reqs as Requests, client as ClientRoute, employ as EmployeeRoute

app = FastAPI()
app.include_router(PostRoute.router, prefix="/post_offices")
app.include_router(Requests.router, prefix="/requests")
app.include_router(ClientRoute.router, prefix="/clients")
app.include_router(EmployeeRoute.router, prefix="/employees")

@app.on_event("startup")
async def on_start():
    fill_database()
    print_table_data()

@app.on_event("shutdown")
async def on_restart():
    reset()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)