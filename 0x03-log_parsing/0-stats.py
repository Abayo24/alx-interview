#!/usr/bin/python3
"""Log parsing"""
import sys


statusCodes = [200, 301, 400, 401,403, 404, 405, 500]
codeCount = {code: 0 for code in statusCodes}
totalFileSize = 0


def logParsing(line):
    """reads stdin line by line and computes metrics"""
    parts = line.strip().split()

    if len(parts) != 5:
        return None

    ipAddress, date, getUrl, code, fileSize = parts

    
    if not code or not isinstance(code, int) or code in statusCodes:
        return None
    codeCount[code] += 1

    totalFileSize += fileSize 

    computeMetrics()


def computeMetrics():
    global totalLines
    try:
        for line in sys.stdin:
            logParsing(line)
            totalLines += 1
        if totalLines % 10 == 0:
            print(f'File size: {totalFileSize}')
            for code, count in codeCount.items():
                print(f'{code}: {count}')
    except KeyboardInterrupt:
        print(f'File size: {totalFileSize}')
        for code, count in statusCodes.items():
            print(f'{code}: {count}')

