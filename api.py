from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse 

app = FastAPI()


#Query parameter
@app.get('/submit')
def save_data(name, age):
    return JSONResponse({
        'message': f"Hello {name}, your age (age)"
    })








# @app.get('/json')
# def get_details():
#     data = {
#         'name' :'Jhon',
#         'age' : 20
#     }
#     return JSONResponse(data)



# @app.get('/html')
# def get_details():
#     html = '''
#            <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>My First Web Page</title>
# </head>
# <body>
#     <h1>Hello, World!</h1>
#     <p>This is my first paragraph of text on this page.</p>
# </body>
# </html>
# '''
#     return HTMLResponse(html)



# @app.get('/redirect')
# def get_details():
#     url = "https://www.hotstar.com/in/home/json"
#     return RedirectResponse(url, status_code = 302)