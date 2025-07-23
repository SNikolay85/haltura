from app.api.dao import UserDAO
import asyncio

print(asyncio.run(UserDAO.find_user_by_id(int(5003388090))))

print('tyt')