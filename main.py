from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
#from your_bot_module import bot, dp, settings  # Импортируем необходимые компоненты бота
import logging

from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Server started')
    yield
    print('Выключение')

# @asynccontextmanager
# async def lifespan(app: FastAPI):
    # # Код, выполняющийся при запуске приложения
    # webhook_url = settings.get_webhook_url()  # Получаем URL вебхука
    # await bot.set_webhook(
    #     url=webhook_url,
    #     allowed_updates=dp.resolve_used_update_types(),
    #     drop_pending_updates=True
    # )
    # logging.info(f"Webhook set to {webhook_url}")
    # yield  # Приложение работает
    # # Код, выполняющийся при завершении работы приложения
    # await bot.delete_webhook()
    # logging.info("Webhook removed")


app_vk = FastAPI(title='Haltura', lifespan=lifespan)

app_vk.include_router(router)


# Маршрут для обработки вебхуков
# @app_vk.post("/webhook")
# async def webhook(request: Request) -> None:
#     logging.info("Received webhook request")
#     update = await request.json()  # Получаем данные из запроса
#     # Обрабатываем обновление через диспетчер (dp) и передаем в бот
#     await dp.feed_update(bot, update)
#     logging.info("Update processed")




