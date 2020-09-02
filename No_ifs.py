# Write a function that accepts two parameters (a and b) 
# and says whether a is smaller than, bigger than, or equal to b.

# Here is an example code:

#  var noIfs = function (a,b) {
#   if(a > b) return a + " is greater than " + b
#   else if(a < b) return a + " is smaller than " + b
#   else if(a == b) return a + " is equal to " + b
#  }

# There's only one problem...

# You can't use if statements, and you can't use shorthands like (a < b)?true:false;
# in fact the word "if" and the character "?" are not allowed in the code.

# MY SOLUTION: 

def no_ifs(a, b):
    
    messages = [' is smaller than ', ' is equal to ', ' is greater than ']
    
    index = ((a > b) - (a < b)) + 1
    
    return str(a) + messages[index] + str(b)