# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
#a loop to find the instances of X-DSPAM-Confidence
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line.rstrip())
#a set of variables to pull the floats out of X-DSPAM-Confidence
    col = line.find(":")
    fl = line[col+2:]
    print(fl)

#a recursive function to sum the numbers from fl
def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers(numbers[1:])

sum_numbers(fl.float())

print("Done")
