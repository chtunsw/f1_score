from pathlib import Path
from datetime import datetime

self_path = Path(__file__).absolute()
file_path = self_path.parent / "test_v2.psv"

with open(str(file_path)) as f:
    lines = f.readlines()

# get data
data_lines = lines[2:]

# init dict
records = {
    "true_positives": 0,
    "true_negatives": 0,
    "false_positives": 0,
    "false_negatives": 0
}

for line in data_lines:
    date_str, y, y_hat = line.split("|")
    date = datetime.strptime(date_str, "%Y-%m-%d")
    y, y_hat = int(y), int(y_hat)
    # only count Tuesday
    if date.weekday() == 1:
        if y_hat == 1 and y == 1:
            records["true_positives"] += 1
        elif y_hat == 0 and y == 0:
            records["true_negatives"] += 1
        elif y_hat == 1 and y == 0:
            records["false_positives"] += 1
        elif y_hat == 0 and y == 1:
            records["false_negatives"] += 1

precision = records["true_positives"] / (records["true_positives"] + records["false_positives"])
recall = records["true_positives"] / (records["true_positives"] + records["false_negatives"])
f1_score = 2 * precision * recall / (precision + recall)
print(records)
print(f1_score)

