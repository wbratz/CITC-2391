array = ["xyxxxyxyy", "xxxxxyyyx", "xxyxxyyyx"]

for str in array:
    for i in range(len(str)):
        for j in range(len(str)):
            if(i == j):
                continue

            

def flip(chr):
    if chr == 'x':
        return 'y'
    if chr == 'y':
        return 'x'