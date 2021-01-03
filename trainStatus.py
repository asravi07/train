class Train :
    def __init__(self,name,seats,fare) :
        self.name = name
        self.seats = seats
        self.fare = fare
    def getstatus(self) :
        print("                                                ")
        print(f"###############{self.name}##############")
        print("                                                ")
        if n<seats :
            print(f"The avilable seats in {self.name} : {self.seats}")
        else:
            print(f"Seats not available.\nAvailable Seats : {self.seats}")
    def fareinfo(self) :
        print(f"Total fare : {self.fare*n}")

#Input by Counter Man
name = input("Enter the name of Train                : ")
seats = int(input("Enter the seat available in Train      : "))
fare = int(input("Enter the fair per person              : "))
n = int(input("Enter the no. of person                : "))
a = Train(name,seats,fare)

#Output given to Costumers
print("*************************************")
print("***********INDIAN RAILWAYS***********")
print("*************************************")
a.getstatus()
a.fareinfo()