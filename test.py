from functions import kill
import time
def josephus(people, skip, screen, n):
    people_list = list(range(1, people + 1))
    index = skip - 1
    while len(people_list) > 1:
        print("Person %d is killed" % people_list.pop(index))
        kill(screen, index, n)
        time.sleep(3)
        index = (index + skip - 1) % len(people_list)
    print("The last survivor is Person %d" % people_list[0])
 