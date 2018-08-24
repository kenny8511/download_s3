import csv
import subprocess

CSV_FILE_PATH = "path/to/csv"
BUCKET_NAME = "your_bucket_name"
SAVE_DIR = "path/to/save_dir"
PROFILE = "default"

with open(CSV_FILE_PATH,  newline='') as f:
    dataReader = csv.reader(f)
    for row in dataReader:
        try:
            res = subprocess.run("aws s3 cp s3://" + BUCKET_NAME + "/" + row[0] + " " + SAVE_DIR + " --profile " + PROFILE, shell=True)
        except Exception as e:
            print("Error：" + row[0])
            print(str(e))