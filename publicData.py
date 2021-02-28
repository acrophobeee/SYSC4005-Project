
class publicData(object):

    def __init__(self):
        self.service_times = {
            "inspector_1": [],
            "inspector_22": [],
            "inspector_23": [],
            "workstation_1": [],
            "workstation_2": [],
            "workstation_3": [],
        }
        self.idle_times = {
            1: [],
            2: [],
            3: [],
        }
        self.block_times = {
            1: [],
            2: [],
            3: []
        }
        self.products = {
            1: 0,
            2: 0,
            3: 0,
        }
