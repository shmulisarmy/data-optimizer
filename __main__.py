from data import users, scema
from time import sleep
from utils import make_sure_scema_is_correct
from json import dumps
from deepdiff import DeepDiff
from main_tools import expand_data, optomize_data









make_sure_scema_is_correct(scema, users)


optomized_data = optomize_data(users, scema)
data_back_to_normal = expand_data(optomized_data, scema)

assert DeepDiff(data_back_to_normal, users) == {}

saved_data_bytes = len(dumps(data_back_to_normal).encode("utf-8")) - len(dumps(optomized_data).encode("utf-8"))
print(f"data saved: {saved_data_bytes} bytes")