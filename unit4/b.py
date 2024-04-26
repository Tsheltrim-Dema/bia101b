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

#input_str = "((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("
floor_index= 0

for i in input_str:
    if i== "(":
        floor_index= floor_index+1
    if i ==")":
        floor_index= floor_index-1      
print('the final floor is', floor_index)

# problem 2
# ? 

def is_valid_brackets(input_str):
    stack = []
    brackets = {'(': ')', ')': '('}
    for char in input_str:
        if char in brackets:
            if stack and brackets[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    return not stack

# Example usage
input_str = "()(()"
print(is_valid_brackets(input_str))

def is_valid_brackets(input_str):
    stack = []
    for char in input_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return not stack

print(is_valid_brackets("()"))  
print(is_valid_brackets("(())"))  
print(is_valid_brackets("(()))")) 
print(is_valid_brackets("((()))")) 
print(is_valid_brackets(")("))