#make a pet and take care of it
# should be in one class
#Make a tiemr to have it lose a timer over time
#Have a class food, class activities,maybe a fat rating
#queue can have it act as a brain
class Dog():#If i want to move changed values in food to Dog use getter and setters
	def __init__(self,health,stam,happiness):
		self.health = health;
		self.stam = stam;
		self.happiness = happiness;
	def name(self):
		name = input("What is your dog's name: ")
	def breed(self):
		breed = input("What is your dog's breed: ")	
	def check(self):
		return self.health,self.stam,self.happiness	
class food(Dog): #main class is food
	def __init__(self,treat,stamina,happy,health,stam,happiness): #Getting everything from Dog and adding additional functionalities(food has values from Dog but not vice versa)
		Dog.health = health
		Dog.stam = stam 
		Dog.happiness = happiness
		self.treat = treat
		self.stamina = stamina
		self.happy = happy
	def get_stats(self):
		return self.treat, self.stamina, self.happy,Dog.health,Dog.stam,Dog.happiness	
	def calculate_stats(self):
		Dog.health = Dog.health + self.treat
		Dog.stam = Dog.stam + self.stamina
		Dog.happiness = Dog.happiness + self.happy
		return Dog.health,Dog.stam,Dog.happiness
	def set_stats(self):
		self.health = Dog.health
		self.stam = Dog.stam
		self.happiness = Dog.happiness
		return self.health,self.stam,self.happiness
class solidfood(food): 
	def __init__(self):
		self.treat = 15
		self.stamina = 10
		self.happy = 5
class treat(food):
	def __init__(self):
		self.treat = 10
		self.stamina = 5
		self.happy = 15
class water(food):
	def __init__(self):
		self.treat = 5
		self.stamina = 15
		self.happy = 10
	'''
class activities(Dog): #main class is activities
	def check(self):
		self.health = self.health - self.hunger
		self.stam = self.stam - self.stamina
		self.happiness = self.happiness - self.happy
		print(self.health, self.stam, self.happiness)
		return self.health,self.stam,self.happiness
class walk(activities):
	hunger = 10
	stamina = 5
	happy = -5
class bath(activities):
	hunger = 0
	stamina = 5
	happy = 10
class fetch(activities):
	hunger = 15
	stamina = 15
	happy = -10
	'''



dog = Dog(100,100,100)
food = food(5,5,5,100,100,100)
solidfood = solidfood()
treat = treat()
water = water()

dog.name()
dog.breed()
print(dog.check())
print(food.get_stats())
print(food.calculate_stats())
print(solidfood.get_stats())
print(solidfood.calculate_stats())
print(food.check())
print(food.set_stats())
#print(Dog.check())