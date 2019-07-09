#make a pet and take care of it
# should be in one class
#Make a tiemr to have it lose a timer over time
#Have a class food, class activities,maybe a fat rating
#queue can have it act as a brain
class Dog():
	health = 100;
	stam = 100;
	happiness = 100;
	def name(self):
		name = input("What is your dog's name: ")
	def breed(self):
		breed = input("What is your dog's breed: ")	
class food(Dog): #main class is food
	def check(self):
		self.health = self.health + self.treat
		self.stam = self.stam + self.stamina
		self.happiness = self.happiness + self.happy
		print(self.health, self.stam, self.happiness)
		return self.health,self.stam,self.happiness
class solidfood(food):
	treat = 15
	stamina = 10
	happy = 5
class treat(food):
	treat = 10
	stamina = 5
	happy = 15
class water(food):
	treat = 5
	stamina = 15
	happy = 10
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



dog = Dog()
food = food()
solidfood = solidfood()
treat = treat()
walk = walk()


dog.name()
dog.breed()
solidfood.check()
treat.check()
walk.check()

