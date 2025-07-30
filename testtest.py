# Temporary script to debug W&B artifact download for trainval_data.csv
import wandb
import pandas as pd
import os

run = wandb.init(project="nyc_airbnb", job_type="debug")
artifact = run.use_artifact("trainval_data.csv:latest")
artifact_dir = artifact.download()

# List the actual file name downloaded
print("Downloaded artifact to:", artifact_dir)
print("Files in directory:", os.listdir(artifact_dir))

# Dynamically find the file (since it's renamed)
filename = os.listdir(artifact_dir)[0]
csv_path = os.path.join(artifact_dir, filename)

df = pd.read_csv(csv_path)
print(df.head())

run.finish()