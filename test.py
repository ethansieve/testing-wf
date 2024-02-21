import sys


# throw error if argv is empty
if len(sys.argv) < 3:
    raise ValueError("Please provide a file to read")

print("Reading file: ", sys.argv[2])
