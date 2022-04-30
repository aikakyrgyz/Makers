####################################################
from polymorphism import Car, Ship, Airplane
person1 = Car('Honda')
person2 = Ship('Titanic')
person3 = Car('Toyota')
person4 = Ship('Victoria')
person5 = Airplane('Qatar')
for person in (person1, person2, person3, person4, person5):
    person.go('Alaska')
####################################################
from polymorphism import Cat, Dog, Duck
an1 = Cat('Tom', 6)
an2 = Dog('Rex', 19)
an3 = Duck('Qyucaki', 2)
an4 = Cat('Mitya', 5)
an5 = Dog('Kolokolchik', 7)

def func(animal):
    animal.info()
    animal.make_sound()

func(an1)
func(an2)
func(an3)
func(an4)
func(an5)
######################################################


