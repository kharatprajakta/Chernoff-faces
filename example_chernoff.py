import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from ChernoffFace import chernoff_face
from sklearn.datasets import load_iris

# ==================================================
# Create output directory
# ==================================================
os.makedirs("plots", exist_ok=True)

# ==================================================
# EXAMPLE 1: Manually Created Data
# Feature mapping (by column order):
# 1 → Face width      = Weight
# 2 → Face height     = Height
# 3 → Eye size        = Age
# 4 → Mouth curvature = Score
# ==================================================

data = pd.DataFrame({
    "height": [150,160,170,180,190],
    "weight": [50,60,70,80,90],
    "age": [20,25,30,35,40],
    "score": [60,65,70,75,80]
})

data_faces = data[["weight", "height", "age", "score"]]

titles1 = [f"Obs {i+1}" for i in range(len(data_faces))]

fig1 = chernoff_face(
    data=data_faces.values,
    titles=titles1,
    color_mapper=cm.Pastel2,
    n_columns=3,
    figsize=(10, 6)
)

plt.suptitle(
    "Chernoff Faces – Manual Data\n"
    "Face width=Weight | Face height=Height | Eye size=Age | Mouth=Score",
    fontsize=12
)

fig1.savefig("plots/chernoff_manual.png", dpi=300)
plt.show()

# ==================================================
# EXAMPLE 2: Normally Distributed Data (50 Observations)
# Same facial-feature mapping
# ==================================================

np.random.seed(123)

data1 = pd.DataFrame({
    "height": np.random.normal(170, 8, 50),
    "weight": np.random.normal(65, 10, 50),
    "age": np.random.normal(30, 5, 50),
    "score": np.random.normal(75, 12, 50)
})

data1_faces = data1[["weight", "height", "age", "score"]]

titles2 = [f"Sample {i+1}" for i in range(len(data1_faces))]

fig2 = chernoff_face(
    data=data1_faces.values,
    titles=titles2,
    color_mapper=cm.tab20,
    n_columns=10,
    figsize=(16, 8)
)

plt.suptitle(
    "Chernoff Faces – Simulated Normal Data\n"
    "Face width=Weight | Face height=Height | Eye size=Age | Mouth=Score",
    fontsize=14
)

fig2.savefig("plots/chernoff_simulated.png", dpi=300)
plt.show()

# ==================================================
# EXAMPLE 3: Iris Dataset
# Feature mapping:
# Face width  → Sepal.Width
# Face height → Sepal.Length
# Eye size    → Petal.Length
# Mouth curve → Petal.Width
# ==================================================

iris = load_iris()

iris_df = pd.DataFrame(
    iris.data,
    columns=["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]
)

iris_faces = iris_df[
    ["Sepal.Width", "Sepal.Length", "Petal.Length", "Petal.Width"]
]

titles3 = [iris.target_names[i] for i in iris.target]

fig3 = chernoff_face(
    data=iris_faces.values,
    titles=titles3,
    color_mapper=cm.Set3,
    n_columns=12,
    figsize=(18, 10)
)

plt.suptitle(
    "Chernoff Faces – Iris Dataset\n"
    "Width=Sepal.Width | Height=Sepal.Length | Eyes=Petal.Length | Mouth=Petal.Width",
    fontsize=16
)

fig3.savefig("plots/chernoff_iris.png", dpi=300)
plt.show()
