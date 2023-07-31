from driww import *
from importlib import import_module
from driww.modules import ALL_MODULES
for module_name in ALL_MODULES:
        imported_module = import_module("driww.modules." + module_name)
bot.run_until_disconnected()

