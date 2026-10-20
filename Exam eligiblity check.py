medical_cause=input("Do you have a medical cause Y/N:").strip().upper()
if medical_cause=="Y":
    print("You are allowed")
else:
    attendence=int(input("Enter the attendence:"))
    if attendence>=75:
        print("Allowed")
    else:
        print("Not allowed")
        