#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
import sys


statusCodegroup = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
count = 0
totalSize = 0
try:
    for line in sys.stdin:
        lineList = line.split(" ")
        if len(lineList) > 4:
            statusCode = lineList[-2]
            fileSize = int(lineList[-1])

            if statusCode in statusCodegroup.keys():
                statusCodegroup[statusCode] += 1
            totalSize += fileSize
            count += 1

        if count == 10:
            count = 0
            print(f'File size: {totalSize}')

            for k, v in sorted(statusCodegroup.items()):
                if v != 0:
                    print(f'{k}: {v}')
except Exception as e:
    pass
finally:
    print(f'File size: {totalSize}')
    for k, v in sorted(statusCodegroup.items()):
        if v != 0:
            print(f'{k}: {v}')
