import agate
import re

def recode_headings(csv_in, csv_out):
  """Strip accented characters in the column names of a CSV file"""
  with open(csv_in) as csv, open(csv_out, "w") as recoded:
    lines = csv.readlines()
    for i, line in enumerate(lines):
      if i == 0: # fix the first line
        line = line.decode("utf-8", "ignore").encode("utf-8")
      recoded.write(line)


