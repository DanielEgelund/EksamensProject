import hashlib

def new_employee():
    user_initialer = input("Indtast initaler (4 tegn): ")
    user_navn = input("Indtast fulde navn: ")
    user_email = input("Indtast email: ")
    user_password = input("Indtast password: ")
    user_profilnr = input("Indtast profil nr. ")

    def Hasher(password):
        hashed_password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        return hashed_password


    textfile_read = open("medarbejdere.txt", "r")

    already_in_file = False


    for line in textfile_read.readlines():

        if user_initialer in line:
            print("Brugeren findes allerede")
            already_in_file = True
            new_employee()
        elif user_email in line:
            print("Brugeren findes allerede")
            already_in_file = True
            new_employee()


    if already_in_file == False:
        textfile_write = open("medarbejdere.txt", "a")
        
        textfile_write.writelines(f"{user_initialer}:{user_navn}:{user_email}:{Hasher(user_password)}:{user_profilnr}\n")
        print("\nProfil oprettet!")
        velkommen()

def udskrift():
    file_reader = open("medarbejdere.txt", "r")
    lines = file_reader.readlines()
    for line in lines:
        words = line.split(":")
        print( "Initialer: " + words[0] + " | Navn: " + words[1] + " | Email: " + words[2] +  " | Brugerprofil: " + words[4] + "\n")
    
    print("__________________________________________________________________________________")
    velkommen()



def velkommen():
    print("\nVelkommen til Medarbejdersystem 1.0\n")
    user_choice = input('For at oprette en ny medarbejder tast: "NEW" \n\nFor at printe eksisterende medarbejdere tast "PRINT" \n\nFor at afslutte programmet tast "QUIT"\n\n')

    if user_choice.lower() == "new":
        new_employee()
    elif user_choice.lower() == "print":
        udskrift()
    elif user_choice.lower() == "quit":
        exit()


velkommen()