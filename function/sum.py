def sum(input_value):
    Ace=0
    for i in range (0, int(input_value) +1):
       Ace=Ace+i
    return Ace


prompt_value=input("Give me a number: ")
print(sum(prompt_value))