from fastapi import FastAPI

from .routers import currencies, historical,convert

app = FastAPI()

app.include_router(currencies.router)
app.include_router(historical.router)
app.include_router(convert.router)

@app.get("/")
def root():
    return {"message":"Success"}