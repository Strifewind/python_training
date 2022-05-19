# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average 
# of those values and produce an output as shown below. Do not use the sum() function or a variable named 
# sum in your solution. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when
# you are testing below enter mbox-short.txt as the file name.

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
