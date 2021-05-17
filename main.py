# def greet():
#     return " Hello Jordan"

# print(greet())

# ====================================

"""
function with parameters 
"""
# def greet(name):
#   return f"Hello {name}, Good morning"

# print(greet("Felix"))
# print(greet("Jordan"))
# print(greet("John"))
# print(greet("Sam"))

# help(greet)
# help(print)

# def x(agent):
#    '''
#    variable referencing hitman agent number
#    agent: the agent number
#    '''
#    return f'Hello {agent}, this yr mission'
  
# print(x(47))
# help(x)

"""
Arbitrary parameters
"""

# def fruits(*names):
#   '''
#   Accepts unkmown number of fruit names and prints each of them
#   *names: list of fruits
#   '''

#   # names ar tuples
#   for fruit in names:
#     print(fruit)
#     print(type(names))

# fruits("Orange", "Apples", "Grapes")

"""
Keyword parameters
"""

# def greet(name, msg):
#   """
#   This function greets a person with a given message
#   name: person to the greet
#   msg: message to greet perosn with
#   """

#   return f"Hello {name}, {msg}"
# print(greet("Jordan","Good morining"))
# print(greet("Good morining","Steph"))
# print(greet(name = "Jordan",msg = "Good morining"))
# print(greet(msg = "Good morining",name = "Steph"))

"""
Arbitrary Keyword parameters
"""

# def athlete(**player):
  # print(type(player))
  # print(player)
  # for key in player:
  #   print(player[key])

# athlete(fname = "Lebron", lname = "James")
# athlete(fname = "Lebron", lname = "James", sport = "Basketball")

"""
Default parameter values
"""

# def greet(name = "Jordan"):
#   return f"Hello, {name}"

# print(greet("Jay"))
# print(greet())

"""
pass statement
"""

# def greet():
#   pass

"""
Recursion
"""

# def factorial_recursive(n):
#   """
#   Multiply a given number by every number less than it down to 1 in a factorial way e.g if n is 5 then calculate 5*4*3*2*1 = 120
#   n: is the highest starting number
#   """
#   if n == 1:
#     return True
#   else:
#     return n * factorial_recursive(n-1)

# print(factorial_recursive(5))
# print(factorial_recursive(30))

# docs.python.org/3/library/functions.html