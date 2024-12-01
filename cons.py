class New:
    #default contructor 
    def __init__(self):
        pass

    #parametrized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


n=New("Sanket",76)

print(n.name,n.marks)  