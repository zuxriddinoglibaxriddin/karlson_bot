from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot('5714804443:AAHtG-8eiFEn97u4_3NnQ2Rlmu7IRMIhO8Q')
dp = Dispatcher(bot, storage=storage)

