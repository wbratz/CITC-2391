"""
Programmer: William Bratz
Assignment: Module 10 - Lab
Date Completed: 10/27/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

class SimpleCounter:
       #initilizer
     def __init__(self,firstnum):
            self._count = firstnum
       #increment method
     def increment(self):
           self._count += 1
       #clear method
     def clear(self):
            self._count = 0
       #get value of count
     def get_value(self):
            return self._count
       #decrement value
     def decrement(self):
            pass

#advanced counter inherits from simple counter
class AdvancedCounter(SimpleCounter):
       #initilizer
    def __init__(self, firstnum):
        super().__init__(firstnum)
       #override increment
    def increment(self):
            self._count += 2
       #override decrement
    def decrement(self):
        self._count -= 1
    
def main():

       user_input = int(input("Enter an initial number: " ))

       simple_count = SimpleCounter(user_input)
       adv_counter = AdvancedCounter(user_input)

       print()
       print("After incrementing..")
       simple_count.increment()
       adv_counter.increment()

       print(simple_count.get_value())
       print(adv_counter.get_value())

       print()
       print("After decrementing...")
       simple_count.decrement()
       adv_counter.decrement()

       print(simple_count.get_value())
       print(adv_counter.get_value())       

       print()
       print("After clearing...")
       simple_count.clear()
       adv_counter.clear()
       print(simple_count.get_value())
       print(adv_counter.get_value())

main()


