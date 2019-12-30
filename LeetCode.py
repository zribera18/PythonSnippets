input_twosum = [2, 7, 11, 15]

input_addtwoNumbers1 = [2, 7]
input_addtwoNumbers2 = [2, 7]

input_medianArray1 = [1,2]
input_medianArray2 = [3,4]


def twoSum(input, sum):
    for x in range(0, len(input)):
        for y in range(0, len(input)):
            if input_twosum[x] + input_twosum[y] == sum:
                return (x,y)
    return None

def addTwoNumbers(first, second):
    first_number = ""
    second_number = ""
    for i in range(0, len(first)):
        first_number += str(first[len(first) - 1 - i])
    for i in range(0, len(second)):
        second_number += str(second[len(second) - 1 - i])
    return int(first_number) + int(second_number)

def medianArray(input1, input2)



if __name__ == '__main__':
    print str(twoSum(input_twosum, 9))
    print str(twoSum(input_twosum, 17))

    print str(addTwoNumbers(input_addtwoNumbers1, input_addtwoNumbers2))

