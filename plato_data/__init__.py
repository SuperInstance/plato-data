"""
plato-data — Data loading for PLATO rooms.

Load from CSV, JSONL, PLATO tiles, fleet telemetry, or raw tensors.
Split, batch, and stream to training.

No ML framework dependencies. Pure data plumbing.
"""

from .data_rooms import DataRoom, DataSpec

__version__ = "1.0.0"
