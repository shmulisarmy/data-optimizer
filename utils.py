def make_sure_scema_is_correct(scema, json_data):
    for s in scema:
        assert s in json_data[0]


    for s in json_data[0]:
        assert s in scema