from classes import *

def create_care_receiver_from_input() -> CareReceiver:
    name = input("Enter care receiver's name: ")
    age = int(input("Enter care receiver's age: "))
    gender = input("Enter care receiver's gender: ")
    address = input("Enter care receiver's address: ")
    phone_number = input("Enter care receiver's phone number: ")
    email = input("Enter care receiver's email: ")
    return CareReceiver(name, age, gender, address, phone_number, email)


def create_caregiver_from_input() -> CareGiver:
    name = input("Enter caregiver's name: ")
    age = int(input("Enter caregiver's age: "))
    gender = input("Enter caregiver's gender: ")
    address = input("Enter caregiver's address: ")
    phone_number = input("Enter caregiver's phone number: ")
    email = input("Enter caregiver's email: ")

    return CareGiver(name, age, gender, address, phone_number, email)

def get_caregiver_input():
    experiences = [
        "Cooking",
        "Cleaning",
        "Bathing",
        "Medication administration",
        "Transportation",
        "Companionship",
        "Mobility assistance",
        "Physical therapy",
        "Emotional support",
        "Dementia care",
        "Personal hygiene",
        "Wound care",
        "Palliative care",
        "Incontinence care",
        "Respiratory care",
        "Hospice care",
        "Feeding assistance",
        "Light housekeeping",
        "Errands",
        "Grooming"
    ]
    selected_experiences = []
    while True:
        print("Enter an experience from the list below or press 'q' to quit:")
        print(experiences)
        experience = input()

        if experience == 'q':
            break

        if experience in experiences:
            selected_experiences.append(experience)
            experiences.remove(experience)
            print("Experience added!")

        else:
            print("Invalid experience. Please try again.")

    return selected_experiences


def get_care_receiver_input():
    experiences = [
        "Cooking",
        "Cleaning",
        "Bathing",
        "Medication administration",
        "Transportation",
        "Companionship",
        "Mobility assistance",
        "Physical therapy",
        "Emotional support",
        "Dementia care",
        "Personal hygiene",
        "Wound care",
        "Palliative care",
        "Incontinence care",
        "Respiratory care",
        "Hospice care",
        "Feeding assistance",
        "Light housekeeping",
        "Errands",
        "Grooming"
    ]
    selected_service = []
    while True:
        print("Enter an service you need from the list below or press 'q' to quit:")
        print(experiences)
        experience = input()

        if experience == 'q':
            break

        if experience in experiences:
            selected_service.append(experience)
            experiences.remove(experience)
            print("Wanted Service added!")

        else:
            print("Invalid service. Please try again.")

    return selected_service