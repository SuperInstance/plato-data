# README Audit — plato-data

**Date:** 2026-05-17 | **Reviewer:** Forgemaster ⚒️

## Scores

| Criterion | Score | Notes |
|-----------|:-----:|-------|
| WHAT it is | ✅ | "Data loading for PLATO rooms" — clear |
| WHY you'd use it | ⚠️ | "No ML framework opinions — just data plumbing" is good, but doesn't explain what PLATO rooms are or why you'd need data loading for them |
| HOW to install | ❌ | No `pip install` or `Cargo.toml` anywhere. Assumes you know how. |
| HOW to use (code) | ✅ | Good usage examples showing CSV, fleet telemetry, dataloaders |
| Links / context | ❌ | No links to plato-types, plato-training, or SuperInstance org |

**Total: 3/5**

## Issues

1. **No install command.** This is a Python package — needs `pip install plato-data`.
2. **Weak "Why".** The tagline "just data plumbing" is catchy but the reader doesn't know what PLATO rooms are. One sentence of context would fix this.
3. **No links.** plato-data sits between plato-types and plato-training. Should link both.

## Action Taken

- ✅ README rewritten with install, why, and links sections added
