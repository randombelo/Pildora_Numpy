# NumPy Orders Analytics API

Píldora formativa del bootcamp Full Stack sobre **NumPy**, la librería base del análisis de datos en Python.

## Descripción

NumPy aporta el `ndarray`, un array N-dimensional de tipo homogéneo en memoria contigua, con operaciones **vectorizadas** (sin bucles `for` en Python) y **broadcasting**.

Este proyecto lo aplica en un caso full stack: una API con **FastAPI** que analiza los pedidos de una tienda online (estadísticas, detección de outliers con z-score e histograma). El "frontend" es la documentación interactiva de FastAPI en `/docs`.

Conceptos que se muestran: `ndarray`, vectorización, broadcasting, boolean indexing, agregaciones (`mean`, `median`, `std`, `percentile`), `histogram`, generador aleatorio con semilla y conversión de tipos NumPy a JSON.

## Requisitos

- Python 3.10 o superior

## Cómo ejecutar

```bash
git clone <URL-DEL-REPO>
cd numpy-orders-analytics

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload
```

Abre http://127.0.0.1:8000/docs para probar los endpoints.

Benchmark lista vs NumPy: `python demo.py`

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/stats` | Count, media, mediana, desviación típica, mínimo, máximo y percentil 95 |
| GET | `/outliers?threshold=3` | Pedidos atípicos según z-score |
| GET | `/histogram?bins=10` | Conteos e intervalos para graficar |
| POST | `/analyze` | Mismas estadísticas sobre una lista enviada por el usuario |

Ejemplo de cuerpo para `/analyze`: `{"values": [10, 12, 11, 13, 12, 11, 10, 13, 12, 500]}`

## Consideraciones

- Un array tiene un solo `dtype`; para datos tabulares mixtos, usar pandas.
- Los tipos NumPy (`np.int64`, `np.float32`) no son nativos de JSON: se convierten con `int()`, `float()` o `.tolist()`.
- El z-score es simple y didáctico, pero la media y la desviación se distorsionan con los propios outliers. En producción conviene valorar IQR o mediana y MAD.

## Recursos adicionales

- Documentación oficial de NumPy: https://numpy.org/doc/
- Quickstart: https://numpy.org/doc/stable/user/quickstart.html
- Artículo "Array programming with NumPy" (Nature, 2020)
- FastAPI: https://fastapi.tiangolo.com/
