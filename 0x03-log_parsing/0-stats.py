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
        return None

    ipAddress, dash, date, getUrl, code, fileSize = parts

    if dash != '-' or not getUrl.startsWith('"GET /projects/260 HTTP/1.1"'):
        return None

    try:
        if not code or not isinstance(code, int) or code in statusCodes:
            return None
        codeCount[code] += 1

        totalFileSize += fileSize

    except ValueError:
        pass


def printMetrics():
    """prints out the metrics"""
    global totalFileSize
    global codeCount

    print(f'File size: {totalFileSize}')
    for code in sorted(codeCount.keys()):
        print(f'{code}: {codeCount[code]}')


def main():
    """reads from stdin and computes metrics"""
    global totalLines
    try:
        for line in sys.stdin:
            logParsing(line)
            totalLines += 1
        if totalLines % 10 == 0:
            printMetrics()
    except KeyboardInterrupt:
        printMetrics()
        sys.exit(0)


if __name__ == "__main__":
    main()
