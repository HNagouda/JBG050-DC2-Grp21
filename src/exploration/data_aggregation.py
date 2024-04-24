import os
from tqdm import tqdm
import pandas as pd

#* ====================================================================
#* === Path configurations ===
#* ====================================================================

BASE_DIR = os.path.abspath(os.getcwd())
DATA_DIR = os.path.join(BASE_DIR, 'data')
crimes_outcomes_stopnsearch_dir = os.path.join(DATA_DIR, 'crimes_outcomes_stopnsearch')
curated_data_dir = os.path.join(DATA_DIR, 'curated_data')

if not os.path.exists(curated_data_dir):
    os.makedirs(curated_data_dir)

#* ====================================================================
#* === Data Aggregation and Curation ===
#* ====================================================================

stop_and_search_files, outcome_files, crime_files = [], [], []

# Collect all relevant CSV filenames
print("\nCurating all relevant CSV filenames...")
for root, dirs, files in tqdm(os.walk(crimes_outcomes_stopnsearch_dir)):
    for file in files:
        if file.endswith("stop-and-search.csv"):
            stop_and_search_files.append(os.path.join(root, file))
        elif file.endswith("outcomes.csv"):
            outcome_files.append(os.path.join(root, file))
        elif file.endswith("street.csv"):
            crime_files.append(os.path.join(root, file))
        else:
            print(f"Unknown file category: {file}")

# Print Statistics
print(f"\nNumber of Stop and Search files: {len(stop_and_search_files)}")
print(f"Number of Outcome files: {len(outcome_files)}")
print(f"Number of Crime files: {len(crime_files)}")

# Combine all files into one DataFrame
print("\nCombining files into single DataFrame(s) based on category...")

print("\nCombining Stop and Search files...")
stop_and_search_df = pd.concat((pd.read_csv(file) for file in tqdm(stop_and_search_files)), ignore_index=True)
stop_and_search_df.to_csv(os.path.join(curated_data_dir, 'stop_and_search.csv'), index=False)
stop_and_search_df.to_parquet(os.path.join(curated_data_dir, 'stop_and_search.parquet'), index=False)
print('Stop and Search DataFrame saved as CSV and Parquet files')
print("\nStop and Search DataFrame Info:")
print(stop_and_search_df.info())

del stop_and_search_df

print("\nCombining Outcome files...")
outcome_df = pd.concat((pd.read_csv(file) for file in tqdm(outcome_files)), ignore_index=True)
outcome_df.to_csv(os.path.join(curated_data_dir, 'outcome.csv'), index=False)
outcome_df.to_parquet(os.path.join(curated_data_dir, 'outcome.parquet'), index=False)
print('Outcome DataFrame saved as CSV and Parquet files')
print("\nOutcome DataFrame Info:")
print(outcome_df.info())

del outcome_df

print("\nCombining Crime files...")
crime_df = pd.concat((pd.read_csv(file) for file in tqdm(crime_files)), ignore_index=True)
crime_df.to_csv(os.path.join(curated_data_dir, 'crime.csv'), index=False)
crime_df.to_parquet(os.path.join(curated_data_dir, 'crime.parquet'), index=False)
print('Crime DataFrame saved as CSV and Parquet files')
print("\nCrime DataFrame Info:")
print(crime_df.info())

del crime_df
