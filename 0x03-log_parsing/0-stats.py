#!/usr/bin/python3
"""Log parsing"""
import sys


statusCodes = [200, 301, 400, 401, 403, 404, 405, 500]
codeCount = {code: 0 for code in statusCodes}
totalFileSize = 0
totalLines = 0


def logParsing(line):
    """reads stdin line by line and computes metrics"""
    global totalFileSize
    global codeCount
    global totalLines

    parts = line.strip().split()

    if len(parts) != 6:
        return

    ipAddress, dash, date, getUrl, statusCode, fileSize = parts

    if dash != '-' or not getUrl.startsWith('"GET /projects/260 HTTP/1.1"'):
        return

    try:
        statusCode = int(statusCode)
        fileSize = int(fileSize)

        if statusCode in codeCount:
            codeCount[statusCode] += 1

        totalFileSize += fileSize
        totalLines += 1

    except ValueError:
        pass


def printMetrics():
    """prints out the metrics"""
    global totalFileSize
    global codeCount

    print(f'File size: {totalFileSize}')
    for code in sorted(codeCount.keys()):
        if codeCount[code] > 0:
            print(f'{code}: {codeCount[code]}')


def main():
    """reads from stdin and computes metrics"""
    global totalLines

    try:
        for line in sys.stdin:
            logParsing(line)
        if totalLines % 10 == 0:
            printMetrics()
    except KeyboardInterrupt:
        printMetrics()
        sys.exit(0)


if __name__ == "__main__":
    main()
