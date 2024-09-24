from data import users, scema
from utils import make_sure_scema_is_correct
from main_tools import expand_data, optomize_data
from deepdiff import DeepDiff




def test_schema_correctness():
    make_sure_scema_is_correct(scema, users)


def test_to_make_sure_returned_data_is_correct():
    optomized_data = optomize_data(users, scema)
    data_back_to_normal = expand_data(optomized_data, scema)

    assert DeepDiff(data_back_to_normal, users) == {}

