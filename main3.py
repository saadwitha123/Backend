from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Banking API running"}

persons = [
    {'account_id': 1, 'name': 'John', 'balance': 400},
    {'account_id': 2, 'name': 'Swathi', 'balance': 600}
]

# 1. Get all persons
def get_all_persons():
    return persons


# 2. Get person by account id
def get_person_by_id(account_id):
    for p in persons:
        if p['account_id'] == account_id:
            return p
    return "Account not found"


# 3. Get person by name (partial match)
def get_person_by_name(name):
    result = []
    for p in persons:
        if name.lower() in p['name'].lower():
            result.append(p)
    return result


# 4. Credit amount
def credit(account_id, amount):
    for p in persons:
        if p['account_id'] == account_id:
            p['balance'] += amount
            return p
    return "Account not found"


# 5. Withdraw amount
def withdraw(account_id, amount):
    for p in persons:
        if p['account_id'] == account_id:
            if p['balance'] < amount:
                return "Insufficient balance"
            p['balance'] -= amount
            return p
    return "Account not found"


# 6. Transfer amount
def transfer(from_acc, to_acc, amount):
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
