from time import perf_counter

#run script
def main(year, day, exampleOutput, funcs):
    exampleResult = {}
    exampleTime = {}
    inputResult = {}
    inputTime = {}
    print('')
    #load day data
    exampleData = loadFile(f'{str(year)}\Example\{str(day)}.txt')
    inputData = loadFile(f'{str(year)}\Input\{str(day)}.txt')

    for step, func in {"A": funcs['a'],"B": funcs['b']}.items():
        print(f'Day {day} - {step}')

        if not exampleOutput[step] or not exampleData:
            exampleResult[step] = None
            exampleOutput[step] = None
            exampleTime[step] = 0
        else:
            startTime = perf_counter()
            exampleResult[step] = func(exampleData[:])
            stopTime = perf_counter()
            exampleTime[step] = stopTime - startTime

        print(f'Example: {exampleResult[step]} [{exampleOutput[step]}] in {exampleTime[step]:.5f}s')
        if exampleResult[step] == exampleOutput[step]:
            startTime = perf_counter()
            inputResult[step] = func(inputData[:])
            stopTime = perf_counter()
            inputTime[step] = stopTime - startTime
            print(f'Input: {inputResult[step]} in {inputTime[step]:.5f}s')
            
        print('')

def loadFile(filename):
    try:
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
    except FileNotFoundError:
        lines = []
    return lines

if __name__ == '__main__':
    print('Hello')