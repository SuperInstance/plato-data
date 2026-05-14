# plato-data

Data loading for PLATO rooms. No ML framework opinions — just data plumbing.

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

## Zero coupling

Only depends on PyTorch for tensor ops. Works with any training loop.
