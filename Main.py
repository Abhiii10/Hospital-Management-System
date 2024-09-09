# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('Abhishek','999','T2 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('Dikshant','Madai','Neurologist.'), Doctor('Rama','Krishna','General Surgery'), Doctor('Hari','Krishna','Orthopedics')]
    patients = [Patient('Kiara','Admani', 18, '9855412523','H1 565'), Patient('Sita','Kumari', 43,'9865412523','J5 7AG'), Patient('Lionel','Messi', 35, '9864026723','H1 GHA')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)

        elif op == '2':
            
            while True:
                op = input('Do you want to discharge a patient(yes/no):').lower()

                if op == 'yes' :
                   admin.discharge(patients,discharged_patients)

                elif op == 'no':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            # 6 - Quit
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
