class Person:
    # greeting_count = 0
    def __init__(self, name, email, phone): 
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person, self.name))
        self.greeting_count += 1
    def print_contact_info(self, name, email, phone):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))
    def add_friend(self, friend):
        self.friends.append(friend)
    def num_friends(self, friends):
        print(len(self.friends))
    def __str__(self): 
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
    def num_unique_people_greeted(self):
        friends = [{"sonny": False}, {"jordan": False}]
        check = friends[0]["sonny"]
        check1 = friends[1]["jordan"]
        if check == False:
            return True
        if check == False:
            return True
    
# 1.1
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

#1.2
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

#1.3
sonny.greet("Jordan")

#1.4
jordan.greet("Sonny")

#1.5
print(sonny.email, sonny.phone)

#1.6
print(jordan.email, jordan.phone)

#2 Make You Own Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self, car):
        print("{} {} {}".format(self.year, self.make, self.model))

car = Vehicle('Nissan', 'Leaf', 2015)

#2.2 - Add a method
car.print_info("car")

#2.3 - Add a method 2
sonny.print_contact_info("Sonny", "sonny@hotmail.com", "483-485-4948")

#2.4 - Add an instance variable (attribute)
jordan.friends.append("sonny") 
sonny.friends.append("jordan")
print(len(jordan.friends))

#2.5 - Add a add_friend method
jordan.add_friend("sonny")
# print(jordan.friends)

#2.6 - Add a num_friends method
jordan.num_friends("sonny")
sonny.num_friends("jordan")

#2.7  - Count number of greetings
print(sonny.greeting_count)
print(jordan.greeting_count)

#2.8 - __str__
print(sonny)
print(jordan)

# Bonus Challenge
sonny.greet("jordan") 
sonny.num_unique_people_greeted()