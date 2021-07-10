from subprocess import Popen, PIPE
import argparse
import json

import csv

def deserializeJson(fileName):
    with open(fileName) as f:
        return json.load(f)

def performTest(testDescription):
    procs = []
    for producer in testDescription['producers']:
        procs.append(Popen(producer.split(' '), stdout=PIPE))
    for consumer in testDescription['consumers']:
        procs.append(Popen(consumer.split(' '), stdout=PIPE))

    for p in procs:
        p.wait()

    results = []
    for p in procs:
        results.append(p.communicate()[0].decode('ascii').rstrip())

    return results

def saveToCsvFile(fileName, testName, results):
    with open(fileName, 'a') as f:
        results.sort()
        title = ['Test Name']
        data = [testName]

        for result in results:
            responce = result.split(':')
            title.append(responce[0])
            data.append(responce[1])
        
        writter = csv.writer(f)
        for row in [title, data]:
            writter.writerow(row)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-rf', '--resultFile', help = "The name of the result csv file. Example: File.csv", type=str, required=True)
    parser.add_argument('-tf', '--testFile', help = "The name of json file with tests. Example: Test.json", type=str, required=True)
    parser.add_argument('-tl', '--testsList', help = 'The list of test name that will be performed', nargs='+', required=False)

    args = parser.parse_args()

    testsFromJson = deserializeJson(args.testFile)
    testsList = testsFromJson.keys() if (args.testsList is None) else args.testsList
    
    for key in testsList:
        results = performTest(testsFromJson[key])
        saveToCsvFile(args.resultFile, key, results)

if __name__ == '__main__':
    main()