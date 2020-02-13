import random
import sys


def getBestTask(candidates, tasks):
    bestTimeTask = sys.maxsize
    bestTask = 0
    for c in candidates:
        time = tasks[c]
        if time < bestTimeTask:
            bestTimeTask = time
            bestTask = c
    return bestTask


def greedyWatingTime(tasks):
    candidates = set()
    n = len(tasks)
    for i in range(n):
        candidates.add(i)
    sol = []
    while candidates:
        bestTask = getBestTask(candidates, tasks)
        candidates.remove(bestTask)
        sol.append(bestTask)
    return sol


n = 10
tasks = []
for i in range(n):
    tasks.append(int(random.uniform(44, 140)))
sol = greedyWatingTime(tasks)
print(tasks)
print(sol)