# Return True is the text (string) is composed ONLY of digits (0, 1, 2...9)
# Example :
#      isInteger("145")     ->  True
#      isInteger("145A")    ->  False
def isInteger(text): #"4567899"
    for i in text:
        if i not in('0', '1', '2', '3', '4', '5', '6', '7', '8','9'):
            return False
    return True

    # complete this body !

    # Return True is the number (integer) is in the range [min, max]
    # Example :
    #      isNumberInRange(145, 0,200)     ->  True
    #      isNumberInRange(145, 0,100)     ->  False


def isValueInRange(value, min, max):
    if min <= value <= max:
        return True
    else:
        return False
    # complete this body !


valueText = input("Enter the value : ")
minText = input("Enter  the min : ")
maxText = input("Enter  the max : ")

if isInteger(valueText) and isInteger(minText) and isInteger(minText):
    value = int(valueText)
    min = int(minText)
    max = int(maxText)

    if isValueInRange(value, min, max):
        print("Correct value")
    else:
        print("Error : value " + valueText +
              " is not in range " + minText + ", " + maxText)

else:
    print("Error : value, min, max should be numbers")
