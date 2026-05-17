# plato-data

**Data loading for PLATO rooms — CSV, JSONL, fleet telemetry, and tile streams into PyTorch DataLoaders.**

[![License](https://img.shields.io/badge/license-MIT-blue)]()

## Why?

PLATO rooms process tiles (training artifacts with provenance). plato-data converts any data source — CSV logs, JSONL embeddings, fleet telemetry time series, or raw tensors — into DataLoaders ready for training. No ML framework opinions, no coupling to specific model architectures. Just data plumbing that works with any training loop.

## Install

```bash
pip install plato-data
```

## Loaders

| Source | Method | Use Case |
|--------|--------|----------|
| CSV | `DataRoom.from_csv()` | Structured tabular data |
| JSONL | `DataRoom.from_jsonl()` | Log files, embeddings |
| PLATO tiles | `DataRoom.from_plato()` | Tile streams as training data |
| Fleet telemetry | `DataRoom.from_fleet_telemetry()` | Time-series sensor data |
| Tensors | `DataRoom.from_tensors()` | Direct construction |

## Usage

```python
from plato_data import DataRoom

# From CSV
room = DataRoom.from_csv("sensors.csv", label_col="status")

# Split and get DataLoaders
train_dl, val_dl = room.dataloader(batch_size=32)

# From fleet logs with sliding windows
room = DataRoom.from_fleet_telemetry("logs/", metric_cols=["cpu", "mem", "disk"])
```

## Related

- **[plato-types](https://github.com/SuperInstance/plato-types)** — Tile lifecycle, Lamport clocks (foundation)
- **[plato-training](https://github.com/SuperInstance/plato-training)** — Micro model training (primary consumer)
- **[tensor-spline](https://github.com/SuperInstance/tensor-spline)** — Compressed layers for training
- **[ASSEMBLY-GUIDE](https://github.com/SuperInstance/plato-training/blob/master/ASSEMBLY-GUIDE.md)** — Full ecosystem assembly guide

## Zero coupling

Only depends on PyTorch for tensor ops. Works with any training loop.
