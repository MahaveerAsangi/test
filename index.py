from fastapi import FastAPI,Request
from crud import read_books
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

tags_metadata = [
    {
        "name": "Books",
        "description": "This endpoint is used to fetch all the books information from books.csv",
    },
]
app = FastAPI(openapi_tags=tags_metadata)
templates = Jinja2Templates(directory="template")


@app.get("/get_books", response_class=HTMLResponse, tags=["Books"])
async def fetch_books(client_request: Request):
    response = read_books()
    # print(response)
    return templates.TemplateResponse("data.html", {"request": client_request, "data": response})


@app.get('/get_mahaveer')
def get_mahaveer():
    response = {'id':1, 'name':'mahaveer', 'address':'LU'}
    return response

if __name__:"__main__":
    uvicorn.run(app)
