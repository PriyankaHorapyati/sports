import os
appointments={}
class Appointment:
    def __init__(self,apointment_id,athlete_id,date_time,notes,feedback_data):
        self.apointment_id=apointment_id
        self.athlete_id=athlete_id
        self.date_time=date_time
        self.notes=notes
        self.feedback_data=feedback_data
        
class Appointment_System :
    
    def create_appointment():
        athlete_id=input("Enter athlete_id")
        if athlete_id not in appointments:
            apointment_id=input("enter apointment_id")
            date_time=input("enter date_time".split())
            notes=input("enter what type of appointment")
            appointments[athlete_id] = {'apointment_id':apointment_id,'date_time':date_time,'notes':notes}
            with open("appointments.txt","a") as file:
                file.write(f"athlete_id:{athlete_id}\nAppointment id:{apointment_id}\ndate_time:{date_time}\ntype of appotinment:{notes}\n")
            print("Appointment created successfully!")
        else:
            print("athlete_id already exist")
    
    
    def get_appointment():
        athlete_id = input("Enter athlete_id: ")
        if athlete_id in appointments:
            print(f"Appointment details for {athlete_id}:")
            print(f"apointment_id:{appointments[athlete_id]['apointment_id']}")
            print(f"date_time: {appointments[athlete_id]['date_time']}")
            print(f"notes: {appointments[athlete_id]['notes']}")
        else:
            print("Appointment not found.")
    
    
    def update_appointment():
        athlete_id = input("Enter athlete_id: ")
        
        if athlete_id in appointments:
            appointment_id = input("Enter new appointment_id: ")
            date_time = input("Enter new appointment date_time: ")
            notes = input("Enter new notes: ")
            
            appointments[athlete_id]['apointment_id'] = appointment_id
            appointments[athlete_id]['date_time'] = date_time
            appointments[athlete_id]['notes'] = notes
            
            
            with open("appointments.txt", "w") as file:
                for id, appointment in appointments.items():
                    file.write(f"Appointment id:{appointment['apointment_id']}\n")
                    file.write(f"athlete_id:{id}\n")
                    file.write(f"date_time:{appointment['date_time']}\n")
                    file.write(f"type of appointment:{appointment['notes']}\n")
                    file.write("\n")
                    
            print("Appointment updated successfully!")
        else:
            print("Appointment not found.")

    
    def delete_appointment():
        athlete_id = input("Enter athlete_id: ")
        if athlete_id in appointments:
            del appointments[athlete_id]
            with open("appointments.txt", "w") as file:
                for id, appointment in appointments.items():
                    file.write(f"Appointment id:{appointment['apointment_id']}\n")
                    file.write(f"athlete_id:{id}\n")
                    file.write(f"date_time:{appointment['date_time']}\n")
                    file.write(f"type of appointment:{appointment['notes']}\n")
                    file.write("\n")
                    print("Appointment deleted successfully!")
        else:
            print("Appointment not found.")

        '''athlete_id = input("Enter athlete_id: ")
        if athlete_id in appointments:
            del appointments[athlete_id]
            a= open("appointments.txt", "w")
            a.write(str(appointments))       
            print("Appointment deleted successfully!")
        else:
            print("Appointment not found.")'''
    
    
    def schedule_sport_psychology_sessions():
        print("New session ")
        athlete_id=input('enter athlete_id')
        apointment_id=input("enter apointment_id")
        date_time=input("enter date_time".split())
        notes=input("enter what type of appointment")
        appointments[athlete_id] = {'apointment_id':apointment_id,'date_time':date_time,'notes':notes}
        with open("appointments.txt","a") as file:
            file.write(f"\nnew session for athlete_id:{athlete_id}\nnew_Appointment id:{apointment_id}\ndate_time:{date_time}\ntype of appotinment:{notes}\n")
        
        
        
        
            
    def display_menu():
        print("\nSports Psychology Appointment System")
        print("1. Create Appointment")
        print("2. get Appointment")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5.manage_session_feedback")
        print("6.schedule_sport_psychology_sessions")
        print("7. Exit")

# Main loop
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            create_appointment()
        elif choice == '2':
            get_appointment()
        elif choice == '3':
            update_appointment()
        elif choice == '4':
            delete_appointment()
        elif choice == '5':
            manage_session_feedback()
            
        elif choice == '6':
            schedule_sport_psychology_sessions()    
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
                
            
            

