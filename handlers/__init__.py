'Собирает все роутеры во-едино'

# Импортируем все обработчики
from handlers import (
    start,
    keyboard
)

routers = (
    start.router,
    keyboard.router
)

__all__ = ("routers",)
