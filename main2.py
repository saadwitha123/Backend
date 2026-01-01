from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app = FastAPI()

contacts = [
    {
        'id' : 1,
        'name' : 'John',
        'phone' : 7329164520
    },
    {
        'id' : 2,
        'name' : 'swathi',
        'phone' : 9376104562
    }
]

@app.post('/add/task')
async def add_task(request: Request):
    data = await request.json()
    contacts.append(data)
    return contacts


@app.get('/tasks')
def get_all_tasks():
    return contacts


@app.get('/task')
def get_task(task_id):
    for t in contacts:
        if t['id'] == int(task_id):
            return t
    return "Not Found"


@app.put('/task')
async def update_task(request:Request):
    data = await request.json()
    for t in contacts:
        if t['id'] == data['id']:
           t.update(data) 
           return contacts
    return "No such task"

@app.delete('/task/{task_id}')
def delete_task(task_id):
    for t in contacts:
        if t['id'] == int(task_id):
            contacts.remove(t)
            return contacts
        return "No such tasks"