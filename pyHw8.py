class Car:
	condition = "New"
	"""docstring for car"""
	def __init__(self,model,color,mpg):
    	self.model = model
    	self.color = color
    	self.mpg = mpg

	def getter(self):
        return self.model, self.color, self.mpg

	def setter(self,model,color,mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

	def milesDriven(self,tank):
    	miles = self.mpg * tank
    	return miles


myCar = Car()
myCar.model = 'BMW'
myCar.color = 'Black'
myCar.mpg = 50

class mySportsCar(Car):
    """docstring for mySportsCar."""
    def __init__(self,model,color,mpg):
        super().__init__(model,color,mpg)

porche = mySportsCar()
porche.model = "Porche"
porche.color = "Black"
porche.mpg = 50

print(milesDriven(porche,18))
print(myCar.model, myCar.color,myCar.mpg)
