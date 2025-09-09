# My Users Data
 
def add_person():
    name = ""
    age = 0     
    email = ""
    phone = 0

    while True:
            try:
                name = input("Enter Name: ").strip().lower()
                # Validate that the name contains only letters and is not empty
                if all(part.isalpha() for part in name.split()) and len(name.split()) >= 1:
                    break
                else:
                    print("Invalid: Please enter a valid name (letters only).")
            except Exception:
                print("Invalid: Please enter a valid name (letters only).")

# VALIDATE AGE INPUT
    while True:
            try:
                age = int(input("Enter Age: "))
                break
            except ValueError:
                print("Invalid: Please enter a valid age.")

# VALIDATE EMAIL INPUT
    while True:
            try:
                email = str(input("Enter Email: ")).strip().lower()
                # Basic validation for email format
                if "@" in email and "." in email:
                    break   
                else:
                    print("Invalid: Please enter a valid email address.")
            except Exception:
                    print("Invalid: Please enter a valid email address.")   

# VALIDATE PHONE NUMBER INPUT
    while True:
            try:
                phone = int(input("Phone Number: ")) 
                break
            except ValueError:
                print("Invalid: Please enter a valid phone number.")

    person = { "name": name, "age": age, "email": email, "phone": phone
    }
    return person 

def display_contacts(people):
     for i, person in enumerate (people):
          print (i + 1,".", person['name'], '|', person['age'], '|', person['email'], '|', person['phone'])
# DELETE DATA
def delete_contact(people):
    display_contacts(people)

    while  True:        
            number = input("Enter number to delete:")
            try:
                number = int(number)
                if number <= 0 or number > len(people):
                    print ("Invalid, number is out of range ")
                    break
            except:
                print("Invalid number.")
            people.pop(number - 1)
            print("User sucessfully deleted")

# SEARCH USER DATA
def search(people):
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    for person in people:
        first_name = person ['name'].split()[0]
        last_name = person ['name'].split()[-1]
        if  first_name == search_name:
            print("Contact information found:")
            print("Name:", person['name'])
            print("Age:", person['age'])
            print("Email:", person['email'])
            print("Phone:", person['phone'])
            found = True
            break
    if not found:                                  
        print("Contac information not found")

# MAIN PROGRAM
print("Hello, welcome to the Contact Management System")    

people = []

# COMMAND LOOP
while True:
    print("Contact size:", len(people))
    command = input("You can 'Search', 'Add', 'Delete', and 'Q' for quit :").strip().lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added successfully.")
    elif command == "search":
        search(people)
        print("Search completed.")
    elif command == "delete":
        delete_contact(people)
        # people.append(person)
        print("Data successfully deleted.")
        print("Would you like to delete another contact?")
    elif command == "q":
         break
    else:
        print("Wrong input, please try again.")

    # people = []
    # print(people)
    
    continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_prompt != "yes":                                                    
        print("Exiting the Contact Management System. Goodbye!")
        break