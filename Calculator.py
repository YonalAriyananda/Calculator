def UserInput():
    UInput = input('Please enter reuired function: ')
    return UInput

functionlist = ['+','-','/','*']


def SelectFunction(UInput):
    numbers = []
    

    for i in UInput:
        

        if i in functionlist:
            if i == '+':
                func = 'Add'
            elif i == '-':
                func = 'Sub'
            elif i == '*':
                func = 'Mul'
            elif i == '/':
                func = 'Div'
    if func == 'Add':
     y = UInput.split("+")
    if func == 'Sub':
      y = UInput.split('-')
    if func == 'Mul':

     y = UInput.split('*')
    if func == 'Div':
     y = UInput.split('/')

    return y,func

def Add(numbers):
    sum = int(numbers[0])+int(numbers[1])
    return sum

def Sub(numbers):
    equals = int(numbers[0])-int(numbers[1])
    return equals

def Mul(numbers):
    product = int(numbers[0])*int(numbers[1])
    return product

def Div(numbers):
    equals = int(numbers[0])/int(numbers[1])
    return equals

def Equal():
    x = UserInput()
    num,func = SelectFunction(x)
    
    
    
    if func == 'Add':
        final = Add(num)
    if func == 'Sub':
        final = Sub(num)

    if func == 'Mul':
        final = Mul(num)

    if func == 'Div':
        final = Div(num)

    return final

print(Equal())




