class animal():
    def move(self):
        print("I move therefore i am ")
class human(animal):
    def move(self):
        print("human can walk and run ")
class fish(animal):
    def move(self):
        print("fish can swime and drive")

def main():
    h1=human()
    h1.move()
    f1=fish()
    f1.move()

if __name__=="__main__":
    main()