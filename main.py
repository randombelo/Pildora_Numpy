import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

from analytics import find_outliers, summary

app = FastAPI(title="Orders Analytics API")

# Datos simulados y reproducibles. En un proyecto real vendrían de una base de datos.
rng = np.random.default_rng(42)
ORDERS = rng.gamma(shape=2.0, scale=40.0, size=1000).round(2)
ORDERS[:3] = [900, 1200, 1500]  # pedidos sospechosos


@app.get("/stats")
def get_stats():
    return summary(ORDERS)


@app.get("/outliers")
def get_outliers(threshold: float = 3.0):
    outliers = find_outliers(ORDERS, threshold)
    return {
        "threshold": threshold,
        "count": int(outliers.size),
        "values": outliers.tolist(),
    }


@app.get("/histogram")
def get_histogram(bins: int = 10):
    counts, edges = np.histogram(ORDERS, bins=bins)
    return {"counts": counts.tolist(), "edges": edges.round(2).tolist()}


class Payload(BaseModel):
    values: list[float] = Field(min_length=1)


@app.post("/analyze")
def analyze(payload: Payload):
    data = np.array(payload.values)
    return {
        "summary": summary(data),
        "outliers": find_outliers(data, 2.0).tolist(),
    }
