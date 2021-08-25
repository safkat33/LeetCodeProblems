import sys
# for line in sys.stdin:
#     print(int(line)**2, end="")

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print(f'Processing Message from sys.stdin {line}')
    print(int(line) ** 2, end="")
print("Done")


# In case of using fileinput
import fileinput

for line in fileinput.input():
    print(int(line)**2)



import sys
for line in sys.stdin:
    print(line)
    line = line.rstrip()
    print(line)


# for line in sys.stdin:
#     line = line.rstrip()