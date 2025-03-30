trainingData = [1,2,3,4,5,6]
expectedOutput = [23,26,29,32,35,38]

weight = 0.1
bias = 0
trainingRate = 0.01
amountToTrain = 350

def predictor(inputData):
    return weight * inputData + bias

for i in range(amountToTrain):
    cost = sum([(expOut - predictor(trainData))**2 for expOut,trainData in zip(expectedOutput,trainingData)])

    weight -= trainingRate * sum([(-2 * trainData)*(expOut - (predictor(trainData))) for expOut,trainData in zip(expectedOutput,trainingData)])

    bias -= trainingRate * sum([-2*(expOut-(predictor(trainData))) for expOut,trainData in zip(expectedOutput,trainingData)])

print(f"cost: {cost:.2f} weight: {weight:.2f} bias: {bias:.2f}") 

testData = [7,8,9,10]
testExpData = [41,44,47,50]

for g in range(len(testData)):
    print("Test output = " , predictor(testData[g]), "\n Cost = " , testExpData[g] - (predictor(testData[g])))