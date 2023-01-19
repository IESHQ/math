
x = 10 
def globallyChange(): 
    global x            # Access the global var 
    x = "didn't work" 
globallyChange()        # Call the function 
print(x) 
