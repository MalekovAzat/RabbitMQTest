# RabbitMQ Test consumers producers

The current directory contain source code for base test of consumers and producers for RabbitMQ.

## Producer

The producer creates new message and requests to deliver them to server.
The producer is represented by _producer.Sync.py_.
There are several command line arguments for use:

1. -h, --help show this help message and exit
2. -n NAME, --name NAME The name which will be shown in the final table.
3. -t TIME, --time TIME Time while the action is performing.
4. -m MODE, --mode MODE Set 'save' or 'nosave' for saving to persistance
5. -q QUEUE, --queue QUEUE
   The name of the queue which will be created and
   connected to chanel
6. -si SERVERIP, --serverIp SERVERIP
   The host of the RabbitMQ server
7. -u USER, --user USER The name for log in RabbitMQ server
8. -p PASSWORD, --password PASSWORD
   The password for log in RabbitMQ server

### Example of usage:

`python3 producerSync.py -n p1 -t 100 -m nosave -q queue1 -si 192.168.1.202 -u user1 -p 0000`

## Consumer

The consumer waits for messages and process it. The producer is represented by _consumerSync.py_.There are several command line arguments for use:

1. -h, --help show this help message and exit
2. -n NAME, --name NAME The name which will be shown in the final table.
3. -t TIME, --time TIME Time while the action is performing.
4. -m MODE, --mode MODE Set 'noconfirm' or 'confirmMannually' for set autoconfirming
5. -q QUEUE, --queue QUEUE
   The name of the queue which will be created and
   connected to chanel
6. -si SERVERIP, --serverIp SERVERIP
   The host of the RabbitMQ server
7. -u USER, --user USER The name for log in RabbitMQ server
8. -p PASSWORD, --password PASSWORD
   The password for log in RabbitMQ server

### Example of usage:

`python3 consumerSync.py -n c1 -t 100 -m confirmMannually -q queue1 -si 192.168.1.202 -u user1 -p 0000`

## Multi testing provided by _taskExecutor.py_

There is extra script that helps to start several consumers and producers.

_taskExecutor.py_ has several requred arguments:

1. rf RESULTFILE, --resultFile RESULTFILE
   The name of the result csv file. Example: File.csv

2. -tf TESTFILE, --testFile TESTFILE
   The name of json file with tests. Example: Test.json

and one no requred argument:

1. -tl TESTSLIST [TESTSLIST ...], --testsList TESTSLIST [TESTSLIST ...]
   The list of test name that will be performed

Example of usage:

`python3 taskExecutor.py -rf results.csv -tf TestConfig.json -tl Test3`

Test list which is provided after **-tl** flag shuld be described in the _TestConfig.json_ file. Otherwice script perform all test provided by _TestConfig.json_.

Example of _TestConfig.json_:

```javascript
{
    "Test1": {
        "producers": [
            "python3 producerSync.py -n p1 -t 100 -m nosave -q queue1 -si 192.168.1.202 -u user1 -p 0000",
            "python3 producerSync.py -n p1 -t 100 -m nosave -q queue1 -si 192.168.1.202 -u user1 -p 0000",
            "python3 producerSync.py -n p1 -t 100 -m nosave -q queue1 -si 192.168.1.202 -u user1 -p 0000",
            "python3 producerSync.py -n p1 -t 100 -m nosave -q queue1 -si 192.168.1.202 -u user1 -p 0000",
            "python3 producerSync.py -n p1 -t 100 -m nosave -q queue1 -si 192.168.1.202 -u user1 -p 0000"
        ],
        "consumers": [
            "python3 consumerSync.py -n c1 -t 100 -m confirmMannually -q queue1 -si 192.168.1.202 -u user1 -p 0000",
            "python3 consumerSync.py -n c1 -t 100 -m confirmMannually -q queue1 -si 192.168.1.202 -u user1 -p 0000",
            "python3 consumerSync.py -n c1 -t 100 -m confirmMannually -q queue1 -si 192.168.1.202 -u user1 -p 0000",
            "python3 consumerSync.py -n c1 -t 100 -m confirmMannually -q queue1 -si 192.168.1.202 -u user1 -p 0000"
        ]
    },
    "Test1": {
        "producers": [
            "python3 producerSync.py -n p1 -t 100 -m nosave -q queue1 -si 192.168.1.202 -u user1 -p 0000"
        ],
        "consumers": [
            "python3 consumerSync.py -n c1 -t 100 -m noconfirm -q queue1 -si 192.168.1.202 -u user1 -p 0000"
        ]
    }
}
```

Provided example generates csv file _results.csv_ which wiil contain results of performed test:

```
Test Name,c1,c1,c1,c1,p1,p1,p1,p1,p1
Test1,29.63,29.87,29.93,30.04,1102.57,1126.76,1337.11,1348.14,1605.85
```

It can be format with
`cat results.csv | column -t -s, | less -S`

```
Test Name  c1       c1       c1       c1       p1       p1       p1
Test1      29.63    29.87    29.93    30.04    1102.57  1126.76  13
```
