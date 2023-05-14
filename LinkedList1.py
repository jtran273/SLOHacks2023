from classes import *
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newdata):
        new_node = Node(newdata)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node


# Create 20 linked lists
list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()
list4 = LinkedList()
list5 = LinkedList()
list6 = LinkedList()
list7 = LinkedList()
list8 = LinkedList()
list9 = LinkedList()
list10 = LinkedList()
list11 = LinkedList()
list12 = LinkedList()
list13 = LinkedList()
list14 = LinkedList()
list15 = LinkedList()
list16 = LinkedList()
list17 = LinkedList()
list18 = LinkedList()
list19 = LinkedList()
list20 = LinkedList()


# Define the potential experiences


# Get user input for the caregiver's experiences
def update_linked_lists(care_giver: CareGiver):

    caregiver_experiences = []
    for i, experience in enumerate(experiences):
        answer = input(f"Do you have experience in {experience}? (yes or no): ")
        if answer.lower() == "yes":
            caregiver_experiences.append(experience)
        if i == len(experiences) - 1:
            print("Thank you. Your experiences have been recorded.")

    # Add the caregiver to the linked lists of matching experiences
    for experience in caregiver_experiences:
        if experience == "Cooking":
            list1.insert(care_giver)
        elif experience == "Cleaning":
            list2.insert(care_giver)
        elif experience == "Bathing":
            list3.insert(care_giver)
        elif experience == "Medication administration":
            list4.insert(care_giver)
        elif experience == "Transportation":
            list5.insert(care_giver)
        elif experience == "Companionship":
            list6.insert(care_giver)
        elif experience == "Mobility assistance":
            list7.insert(care_giver)
        elif experience == "Physical therapy":
            list8.insert(care_giver)
        elif experience == "Emotional support":
            list9.insert(care_giver)
        elif experience == "Dementia care":
            list10.insert(care_giver)
        elif experience == "Personal hygiene":
            list11.insert(care_giver)
        elif experience == "Wound care":
            list12.insert(care_giver)
        elif experience == "Palliative care":
            list13.insert(care_giver)
        elif experience == "Incontinence care":
            list14.insert(care_giver)
        elif experience == "Respiratory care":
            list15.insert(care_giver)
        elif experience == "Hospice care":
            list16.insert(care_giver)
        elif experience == "Feeding assistance":
            list17.insert(care_giver)
        elif experience == "Light housekeeping":
            list18.insert(care_giver)
        elif experience == "Errands":
            list19.insert(care_giver)
        elif experience == "Grooming":
            list20.insert(care_giver)


def experience_input(caregiver):
    n = 0
    while n <= 20:
        create_LList = LinkedList()
        n += 1
    input_value = input("Which experience do you have," *experiences)



care_giver = CareTaker("John Smith", 35, "Male", "123 Main St.", "555-555-5555", "john.smith@email.com", "Monday-Friday, 9am-5pm")
update_linked_lists(care_giver)

