import numpy as np


def summary(data: np.ndarray) -> dict:
    """Estadísticas básicas. Se convierte a tipos nativos de Python para poder serializar a JSON."""
    return {
        "count": int(data.size),
        "mean": float(data.mean()),
        "median": float(np.median(data)),
        "std": float(data.std()),
        "min": float(data.min()),
        "max": float(data.max()),
        "p95": float(np.percentile(data, 95)),
    }


def find_outliers(data: np.ndarray, threshold: float = 3.0) -> np.ndarray:
    """Devuelve los valores cuyo z-score absoluto supera el umbral."""
    std = data.std()
    if std == 0:
        return data[:0]  # array vacío: no hay dispersión
    z = (data - data.mean()) / std  # broadcasting
    return data[np.abs(z) > threshold]  # boolean indexing
