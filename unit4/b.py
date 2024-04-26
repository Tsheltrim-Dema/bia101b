#def elevator_direction(commands):
   # count = 0
    #for command in commands:
       # if command == "((((":
            #count += 1
      #  elif command == "))))":
          #  count -= 1
    
   # if count > 0:
      #  return "Going up"
    #elif count < 0:
    #    return "Going down"
   # else:
        #return "Staying on the same floor"
    
# Example input commands
#commands = ["((((", ")))", ")))", "(((("]

# Output the final direction
#print(elevator_direction(commands))

#def final_floor(input_str):
   # floor = 0
   # for char in input_str:
  #      if char == '(':
   #         floor += 1
  #      elif char == ')':
     #       floor -= 1
  #  return floor
#print(final_floor("(((("))
#print(final_floor("((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("))  

input_str = "((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("
floor_index= 0

for i in input_str:
    if i== "(":
        floor_index= floor_index+1
    if i ==")":
        floor_index= floor_index-1
print('the final floor is', floor_index)

# problem 2
# ? 

