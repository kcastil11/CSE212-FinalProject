class Fast_food_restaurant:
    def __init__(self,max_size, stock):
        self.stock = stock
        self.max_size = max_size

        self.line = []

    def add_to_line(self, name):
        """
        Purpose: Add a person to the end of the line
        with the name given as an argument. Have a 
        conditional that will compare the queue size
        to the max size and return a phrase saying
        you cant add more people since the max size has
        been reached.
        """
        if self.get_line_size() == self.max_size:
            print("Line is too big! Wait for more people to leave.")
            return

        self.line.append(name)


    def remove_first_in_line(self):
        """
        Purpose: Remove the first person in the line.
        If someone is removed from the line we know that
        the meal is given away. Since everyone
        is only allowed 1, deduct from the stock here.
        """
        self.line.pop(0)
        self.subtract_from_stock()


    def subtract_from_stock(self):
        """
        Purpose: Subtract amount from food stock.
        """
        self.stock -= 1


    def get_line_size(self):
        """
        Purpose: Returns the size of the line
        """
        return len(self.line)


    def out_of_food(self):
        """
        Purpose: Return a boolean to see if the restaurant
        is out of food.
        """
        return self.stock == 0


    def __str__(self):
        """
        Purpose: Loop through self.line and grab the names of all
        who are in the line. Return everyone in the line.
        """
        front = "[ "
        end = "]"
        names = ""
        for name in self.line:
            names += name + " "
        return front + names + end


stock = 8
line = Fast_food_restaurant(10, stock)

# ============== Test 1 ============== #
print("============== Test 1 ==============")
print()
line.add_to_line("Maya") 
line.add_to_line("Andres")
line.add_to_line("Lucca")
line.add_to_line("Lola")
line.add_to_line("Karl")
line.add_to_line("Alfredo")
print(line) # Output: Maya Andres Lucca Lola Karl Alfredo
print()

# ============== Test 2 ============== #
print("============== Test 2 ==============")
print()
line.remove_first_in_line()
line.remove_first_in_line()
print(line) # Output: Lucca Lola Karl Alfredo

line.add_to_line("Eduardo")
line.add_to_line("Vero")
line.add_to_line("Ezra")
line.add_to_line("Alberto")
line.add_to_line("Lina")
line.add_to_line("Luis")
print(line)  # Output: Lucca Lola Kalr Alfredo Eduardo Vero Ezra Alberto Lina Luis
print()

# ============== Test 3 ============== #
print("============== Test 3 ==============")
print()
line.add_to_line("Nancy") # Output: Line is too big! Wait for more people to leave.
line.add_to_line("Lucia") # Output: Line is too big! Wait for more people to leave.
print(line)  # Output: Lucca Lola Karl Alfredo Eduardo Vero Ezra Alberto Lina Luis

for person in range(line.get_line_size()):
    """
    We will then remove everyone from the line and give them
    the order of food. 

    Output: Have a great day guys!!
    """
    if line.out_of_food():
        print("Have a great day guys!!")

    line.remove_first_in_line()

print(line) # Ouptut: [ ]


    

