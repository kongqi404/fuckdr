from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import socket
import base64
from pydantic import BaseModel
import uvicorn


class Addr(BaseModel):
    Addr: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)


@app.get("/check")
async def read_root(_: int):
    return r'{"code": "0", "data": {"version": "1.2"}}'


@app.post("/query")
async def query(Addr: Addr):
    ip = socket.gethostbyname(socket.gethostname())
    key = "6cfd5dd4dea0e831"
    data = AES.new(key.encode("utf-8"), AES.MODE_ECB).encrypt(
        pad(ip.encode("utf-8"), 16)
    )
    data = base64.b64encode(data).decode("utf-8")
    return {"code": "0", "data": data}


@app.options("/query")
async def query_op():
    return None


def main():
    uvicorn.run("fuckdr.fkdr:app", port=10440, log_level="info")
