# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
            arr.append(item)
    return sorted(arr)


array = [1,6,2,1]
print(flatten_and_sort(array))

#  How does this solution ensure data immutability?
# The function does not affect the evirorment of its input. Instead it creates a new array using the data from the array that already exists
# Is this solution a pure function?
# Yes. The function produces same output given the same input. The function produces no side effects. The function does not rely on external state.
# Is this solution a higher order function?
# No this is not. A higher order functionin is a function that receives a function as an argument or returns the function as an argument.
# Why is functional programming helpful?
# It makes it easier to check some problems in programs written as pure functions.

# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)

  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"

# Make sure to answer the following prompts about your coding experience:
# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Inheritance - both the AnakinsPod and SebulbasPod inherited the Podracer class, Encapsulation - classes inheritely bundle info together which helps with the code readability, Abstraction - hiding unnecessary info like the details about the make of the care or what the functions actually do within the class, Polymorphism - is that this class is implemented within other classes
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# This was the easiest way becasue there is a lot of repetitious code 
# How in particular did Object Oriented Programming assist in the solving of this problem?
# I was able to reuse the same data over and over again without retyping it limiting the space for error.