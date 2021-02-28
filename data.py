# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def wslist(fileLocation):
    dataset = open(fileLocation).read().splitlines()
    return randomGenerator(dataset)


def randomGenerator(datalist):
    toget = 0
    for x in range(0, len(datalist)-1):
        toget += float(datalist[x])
    mean = toget / len(datalist)-1
    return random.random() * mean
