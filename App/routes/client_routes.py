from fastapi import APIRouter
from models.client import Client

router = APIRouter()

clients = []

@router.get("/clients")
def get_clients():
    return clients

@router.post("/clients")
def add_client(client: Client):
    clients.append(client)
    return client