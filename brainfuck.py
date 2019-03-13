import sys

def runfile(filename):
    f = open(filename, "r")
    evaluate(f.read())
    f.close()

def evaluate(code):
    map = buildmap(code)
    cells, codeptr, ptr, = [0], 0, 0

    while codeptr < len(code):
        cmd = code[codeptr]

        if cmd == ">":
            ptr += 1
            if ptr == len(cells): cells.append(0)

        if cmd == "<":
            ptr = 0 if ptr <= 0 else ptr - 1

        if cmd == "+":
            cells[ptr] += 1

        if cmd == "-":
            cells[ptr] -= 1

        if cmd == ".":
            sys.stdout.write(chr(cells[ptr]))

        if cmd == ",":
            cells[ptr] = ord(sys.stdin.read(1))

        if cmd == "[":
            if cells[ptr] == 0: codeptr = map[codeptr]

        if cmd == "]":
            if cells[ptr] != 0: codeptr = map[codeptr]

        codeptr += 1

def buildmap(code):
    temp, map = [], {}

    for pos, cmd in enumerate(code):
        if cmd == "[": temp.append(pos)
        if cmd == "]":
            start = temp.pop()
            map[start] = pos
            map[pos] = start

    return map

def main():
    if(len(sys.argv) == 1):
        print("Enter Brainfu**, confirm with enter")
        evaluate(sys.stdin.readline())
    if(len(sys.argv) == 2):
        runfile(sys.argv[1])

main()
