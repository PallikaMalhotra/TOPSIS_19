import pandas as pd
import numpy as np
import os
import time

def run_topsis(input_file, weights_str, impacts_str, output_dir):
    df = pd.read_csv(input_file, encoding="latin1")

    if df.shape[1] < 3:
        raise ValueError("Input file must have at least 3 columns")

    data = df.iloc[:, 1:].apply(pd.to_numeric)

    weights = np.array(list(map(float, weights_str.split(","))))
    impacts = impacts_str.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise ValueError("Weights and impacts count mismatch")

    # Normalize
    norm = data / np.sqrt((data ** 2).sum())
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    scores = d_worst / (d_best + d_worst)

    df["Topsis Score"] = scores
    df["Rank"] = scores.rank(ascending=False).astype(int)

    os.makedirs(output_dir, exist_ok=True)
    output_file = f"topsis_result_{int(time.time())}.csv"
    output_path = os.path.join(output_dir, output_file)

    df.to_csv(output_path, index=False)

    return output_path
