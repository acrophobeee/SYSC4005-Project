from simpy.resources import container

import data
import random as rd


class inspector1(object):
    def __init__(self, env, pb, workstation_1, workstation_2, workstation_3):
        self.pb = pb
        self.env = env
        self.action = env.process(self.run())
        self.workstation_1 = workstation_1
        self.workstation_2 = workstation_2
        self.workstation_3 = workstation_3

    def run(self):
        while True:
            service_time = data.wslist("servinsp1.dat")
            print(service_time)
            self.pb.service_times["inspector_1"].append(service_time)
            yield self.env.timeout(service_time)

            block_time = self.env.now
            if self.workstation_1.component_container.level <= self.workstation_2.component_container_1.level or \
                    self.workstation_1.component_container.level <= self.workstation_3.component_container_1.level:
                yield self.workstation_1.component_container.put(1)
                print('Added component 1 to workstation 1')
            elif self.workstation_2.component_container_1.level <= self.workstation_3.component_container_1.level:
                yield self.workstation_2.component_container_1.put(1)
                print('Added component 1 to workstation 2')
            else:
                yield self.workstation_3.component_container_1.put(1)
                print('Added component 1 to workstation 3')
            self.pb.block_times[1].append(self.env.now - block_time)


class inspector2(object):
    def __init__(self, env, pb,  workstation_2, workstation_3):
        self.pb = pb
        self.env = env
        self.workstation_2 = workstation_2
        self.workstation_3 = workstation_3
        self.action = env.process(self.run())

    def run(self):
        if rd.randint(0, 2) == 1:
            service_time = data.wslist("servinsp22.dat")
            self.pb.service_times["inspector_22"].append(service_time)
            yield self.env.timeout(service_time)
            block_time = self.env.now
            yield self.workstation_2.component_container_2.put(1)
            self.pb.block_times[2].append(self.env.now - block_time)

        else:
            service_time = data.wslist("servinsp23.dat")
            self.pb.service_times["inspector_23"].append(service_time)
            yield self.env.timeout(service_time)
            block_time = self.env.now
            yield self.workstation_3.component_container_3.put(1)
            self.pb.block_times[3].append(self.env.now - block_time)


class workstation1(object):
    def __init__(self, env, pb):
        self.env = env
        self.pb = pb
        self.action = env.process(self.run())
        self.component_container = container.Container(self.env, 2)

    def run(self):
        while True:
            # Waits until there are components available to use
            idle_start = self.env.now
            print("step1")
            yield self.component_container.get(1)
            print("step2")
            self.pb.idle_times[1].append(self.env.now - idle_start)
            service_time = data.wslist("ws1.dat")  # <--Generate duration here
            self.pb.service_times["workstation_1"].append(service_time)
            yield self.env.timeout(service_time)
            self.pb.products[1] + 1
            print("step3")
            print('Product 1 assembled')


class workstation2(object):
    def __init__(self, env, pb):
        self.pb = pb
        self.env = env
        self.action = env.process(self.run())
        self.component_container_1 = container.Container(self.env, 2)
        self.component_container_2 = container.Container(self.env, 2)

    def run(self):
        while True:
            # Waits until there are components available to use
            idle_start = self.env.now
            yield self.component_container_1.get(1) & self.component_container_2.get(1)
            self.pb.idle_times[2].append(self.env.now - idle_start)
            service_time = data.wslist("ws2.dat")  # <--Generate duration here
            self.pb.service_times["workstation_2"].append(service_time)
            yield self.env.timeout(service_time)
            self.pb.products[2] + 1
            print('Product 2 assembled')


class workstation3(object):
    def __init__(self, env, pb):
        self.pb = pb
        self.env = env
        self.action = env.process(self.run())
        self.component_container_1 = container.Container(self.env, 2)
        self.component_container_3 = container.Container(self.env, 2)

    def run(self):
        while True:
            # Waits until there are components available to use
            idle_start = self.env.now
            yield self.component_container_1.get(1) & self.component_container_3.get(1)
            self.pb.idle_times[2].append(self.env.now - idle_start)
            service_time = data.wslist("ws3.dat")  # <--Generate duration here
            self.pb.service_times["workstation_3"].append(service_time)
            yield self.env.timeout(service_time)
            self.pb.products[3] + 1
            print('Product 3 assembled')
