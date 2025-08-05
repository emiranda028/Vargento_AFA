# utils.py
import pandas as pd

def cargar_dataset(ruta="data/jugadas_var.csv"):
    return pd.read_csv(ruta)
