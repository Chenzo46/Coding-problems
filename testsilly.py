import math 

states = ["off", "red", "green", "blue"]

def ledStates(errorCode: int) -> tuple:
    ledState1 = math.floor(errorCode / 4)
    ledState2 = errorCode % 4
    return states[ledState1], states[ledState2]
    

def calcErrorCode(statesInput):
    errorCode = 0
    for index, stateString in enumerate(statesInput):
        if stateString == "BROKEN":
            errorCode += 2**(len(statesInput) - index - 1)
        elif not stateString == "WORKING":
            raise("BAD input dummy")

    return errorCode
def main():
    cases = int(input())

    for case in range(cases):
        states = list()
        statesInput = input().split(" ")   
        errorCode = calcErrorCode(statesInput)
        ledState1, ledState2 = ledStates(errorCode)
        print(ledState1, ledState2)

if __name__ == '__main__':
    main()