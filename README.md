# JBG050-DC2-Grp21

## Environment Setup
>***NOTE:*** This codebase utilizes python 3.10 - i.e, ensure your environment has a pre existing installation of python 3.10


> Package manager of choice - `conda`. Feel free to use any package manager you like.


- If your device supports **CUDA** computation (has an NVIDIA GPU), use `requirements_GPU.txt` to install dependencies

    ```
    pip install -r requirements_GPU.txt
    ```

- If your device does not support **CUDA** computation, use `requirements_non_GPU.txt` to install dependencies

    ```
    pip install -r requirements_non_GPU.txt
    ```

---

## Data Aggregation

File [data_aggregation.py](src/exploration/data_aggregation.py) sorts through all data files under `data/crimes_outcomes_stopnsearch` and constructs singular CSV / Parquet files for each of the following categories:
  1. Crimes
  2. Crime Outcomes
  3. Stop and Search actions.

Stores curated files under `data/curatad_data`