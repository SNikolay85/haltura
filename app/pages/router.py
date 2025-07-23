from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from app.api.dao import ApplicationDAO, ServiceDAO, MasterDAO, UserDAO


router_pages = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router_pages.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request, "title": "Элегантная парикмахерская"})


@router_pages.get("/form/", response_class=HTMLResponse)
async def read_root(request: Request, first_name, services=Depends(ServiceDAO.find_all_lst), masters=Depends(MasterDAO.find_all_lst)):
    return templates.TemplateResponse("form.html",
                                      {"request": request,
                                       "title": "Форма записи",
                                       "first_name": first_name,
                                       "services": services,
                                       "masters": masters})
