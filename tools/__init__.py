import agate
import fabric.api
import re

def recode_headings(csv_in, csv_out):
  """Strip accented characters in the column names of a CSV file"""
  with open(csv_in) as csv, open(csv_out, "w") as recoded:
    lines = csv.readlines()
    for i, line in enumerate(lines):
      if i == 0: # fix the first line
        line = line.decode("utf-8", "ignore").encode("utf-8")
      recoded.write(line)

"""
data = {
    "immigration": (
      (1, "index"),
      (18, "total"),
      (19, "non-immigrants"),
      (20, "immigrants"),
      (21, "immigrants-before-1971"),
      (22, "immigrants-1971-1980"),
      (23, "immigrants-1981-1990"),
      (24, "immigrants-1991-2000"),
      (25, "immigrants-2001-2011")
    )
}

nhs = "nhs-planning-districts-indexed.csv"

for item in data.items():
    cut = tools.cut_csv(nhs, item)
    renamed = tools.rename_csv(cut, item)
"""

def cut_csv(csv, item):
    key, name_index = item
    tmp = "{}-tmp.csv".format(key)
    cols = ",".join(str(index) for index, name in name_index)
    cmd = "csvcut -c {} {} > {}".format(cols, csv, tmp)
    fabric.api.local(cmd)
    return tmp

def rename_csv(tmp, item):
    key, name_index = item
    columns_renamed = agate.Table.from_csv(tmp, [name for index, name in name_index])
    columns_renamed.to_csv("{}.csv".format(key))

