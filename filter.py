from queue import *


# treating the dictionary like the person is the ID and the experiences is the data
def Matching(wants: list[str], Diction):
    count = 0
    q = []
    pq = PriorityQueue()

    for name in Diction:
        q.append([len(wants), name])

    for want in range(len(wants)):
        for key in Diction:
            for item in Diction[key]:
                if wants[want] in item:
                    q[count][0] -= 1
            count += 1
        count = 0
    for value in q:
        pq.put((value[0], value[1]))
    return pq

def printing(pq):

    num = 0

    if pq.qsize() > 6:
        while num < 6:
            person = (pq.get()[1])
            print(str(person))
            num += 1

    else:
        while not pq.empty():
            person = (pq.get()[1])
            print(str(person))