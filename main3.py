from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app = FastAPI()

persons = [
    {"account_id": 1, "name": "John", "balance": 400},
    {"account_id": 2, "name": "Swathi", "balance": 600}
]

@app.get('/persons')
def get_all_persons():
    return persons


@app.get('/person/{account_id}')
def get_person_by_id(account_id:int):
    for p in persons:
        if p['account_id'] == account_id:
            return p
    return "Account not found"


@app.get('/person/name/{name}')
def get_person_by_name(name:str):
    result = []
    for p in persons:
        if name.lower() in p['name'].lower():
            result.append(p)
    return result


@app.post('/credit')
async def credit_amount(request: Request):
    data = await request.json()
    for p in persons:
        if p['account_id'] == data['account_id']:
            p['balance'] += data['amount']
            return p
    return "Account not found"


@app.post('/withdraw')
async def withdraw_amount(request: Request):
    data = await request.json()
    for p in persons:
        if p['account_id'] == data['account_id']:
            # if p['balance'] < amount:
            #     return "Insufficient balance"
            p['balance'] -= data['amount']
            return p
    return "Account not found"


@app.post('/transfer')
def transfer(from_acc:int, to_acc:int, amount:int):
    sender = None
    receiver = None

    for p in persons:
        if p['account_id'] == from_acc:
            sender = p
        if p['account_id'] == to_acc:
            receiver = p

    if not sender or not receiver:
        return "Invalid account"

    if sender['balance'] < amount:
        return "Insufficient balance"

    sender['balance'] -= amount
    receiver['balance'] += amount

    return "Transfer successful"
