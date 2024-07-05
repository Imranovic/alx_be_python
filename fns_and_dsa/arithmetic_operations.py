# def perform_operation(num1, num2, operation):
#     match operation:
#         case "add": 
#             result =  num1 + num2
#             print (f"The result is {result}.")
#         case "subtract": 
#             result = num1 - num2
#             print (f"The result is {result}.")
#         case "multiply": 
#             result = num1 * num2
#             print (f"The result is {result}.")
#         case "divide": 
#             if num2 == 0:
#                 print ("Cannot divide by zero.")
#             elif:
#                 result = num1/num2
#                 print (f"The result is {result}.")
#     return result


def perform_operation(num1, num2, operation):
    if operation == "add":
        return  num1 + num2
        # print (f"The result is {result}.")
    elif operation == "subtract": 
        return num1 - num2
        # print (f"The result is {result}.")
    elif operation == "multiply":
        return num1 * num2
        # print (f"The result is {result}.")
    elif operation == "divide": 
        if num2 == 0:
            print ("Cannot divide by zero.")
        else:
            return num1/num2
            # print (f"The result is {result}.")


print(perform_operation(2,3, "subtract"))