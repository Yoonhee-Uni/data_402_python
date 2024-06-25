print("\nQ1a\n")
# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:
class Country:
    def __init__(self, country, continent, climate, language):
        self.country = country
        self.continent = continent
        self.climate = climate
        self.language = language

    def print(self):
        print("Country :", self.country, "Continent :", self.continent, "Climate :", self.climate, "Language :", self.language )


print("\nQ1b\n")
# Q1b: Create a subclass of a city which inherits from the country class

# A1b:
class City(Country):
    def __init__(self, country, continent, climate, language, city):
        super().__init__(country, continent, climate, language)
        self.city = city
    def print(self):
        super().print()d
        print("City :", self.city)


# country1= Country("Korea", "Asia", "Continental", "Korean")
# country2= Country("Ukraine", "Europe", "Continental", "Ukrainian")
# city1 = City("Korea", "Asia", "Continental", "Korean", "Seoul")
city2 = City("Ukraine", "Europe", "Continental", "Ukrainian","Kyiv")

# country1.print()
# country2.print()

# city1.print()
city2.print()
# # -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers
# and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False

# A2a:

result = []

for i in list_of_numbers:
    prime_task = Number(i)
    x = prime_task.is_prime()
    if x :
        result.append(i)
print(result)






print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
result = []

for number in list_of_numbers:
    x = Number(number)
    find_divisible = x.divisible_by_n(12)
    if find_divisible :
        result.append(number)


print(result)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
       print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:
boss_one = GoodBoss("Yoonhee", "good", "smart", "good")
boss_one.encourage()

# -------------------------------------------------------------------------------------- #





