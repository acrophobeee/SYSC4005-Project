# This is a sample Python script.

import simpy as simpy
import model
from publicData import publicData

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_env = simpy.Environment()
    pb = publicData()
    # initialize model
    workstation_1 = model.workstation1(main_env, pb)
    workstation_2 = model.workstation2(main_env, pb)
    workstation_3 = model.workstation3(main_env, pb)
    inspector_1 = model.inspector1(main_env, pb, workstation_1, workstation_2, workstation_3)
    inspector_2 = model.inspector2(main_env, pb, workstation_2, workstation_3)
    main_env.run(until=10)