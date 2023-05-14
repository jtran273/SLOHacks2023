from classes import *
from UserInputRegistration import *
from filter import *
def main():
    cgval = 'y'

    care_receiver = create_care_receiver_from_input()
    print(f"Created Care Receiver: {care_receiver}")
    wanted_services = get_care_receiver_input()
    print(f"Selected services: {wanted_services}")

    dict = {}
    while cgval != 'n':
        caregiver = create_caregiver_from_input()
        print(f"Created Care Giver: {caregiver}")
        provided_services = get_caregiver_input()
        print(f"Provided services: {provided_services}")
        dict[str(caregiver)] = provided_services
        cgval = input("Input more? (y/n) ")

    printing(Matching(wanted_services, dict))


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

if __name__ == '__main__':
    main()
