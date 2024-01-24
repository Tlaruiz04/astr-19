#create the class cat 
class Cat:
    #initial function when calling cat
    def __init__(self, name = "No name", l_arms = 0, l_legs = 4, n_eyes = 2, tail =True, furry = True):
        self.name = name
        self.l_arms = l_arms
        self.l_legs = l_legs 
        self.n_eyes = n_eyes
        self.tail = tail
        self.furry = furry
    def cat_specs(self):
        print(f"This cat is named {self.name}")
        print(f"This cat has {self.l_legs} legs. ")
        print(f"This cat has {self.l_arms} arms.")
        print(f"This cat has {self.n_eyes} eyes.")
        print(f"Does this cat have a tail? {self.tail}")
        print(f"Does this cat have fur? {self.furry}")
def main():
    my_cat = Cat("Dally")
    my_cat.cat_specs()
if __name__ == "__main__":
    main()
