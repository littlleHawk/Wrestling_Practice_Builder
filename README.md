# Wrestling Practice Builder

A Python-based tool for coaches and athletes that generates structured wrestling practice plans from a configurable Jupyter Notebook dashboard. The practice body is built by programmatically assembling individual moves into timed repetition sets, making it easy to produce consistent, reproducible training sessions.

---

## Features

- Interactive dashboard built in a Jupyter Notebook (`.ipynb`) for easy input
- Accepts user-defined parameters to customize the practice (duration, focus areas, skill level, etc.)
- Generates a full practice plan from a library of individual wrestling moves
- Repeatable and editable — tweak inputs and regenerate instantly
- Move library stored in CSV format for easy additions and modifications

---

## Project Structure

```
Wrestling_Practice_Builder/
├── builder_dash.ipynb       # Main interactive dashboard (start here)
├── Practice_Builder.py      # Core practice generation logic
├── utilities.py             # Helper functions used by the builder
├── widgets_utilites.py      # Jupyter widget utilities for the dashboard
├── test_moves.csv           # Sample move library (CSV)
└── notes.txt                # Developer notes
```

---

## Requirements

- Python 3.x
- Jupyter Notebook or JupyterLab
- The following Python packages:
  - `ipywidgets`
  - `pandas`
  - `notebook` (or `jupyterlab`)

Install dependencies with:

```bash
pip install jupyter ipywidgets pandas
```

---

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/littlleHawk/Wrestling_Practice_Builder.git
   cd Wrestling_Practice_Builder
   ```

2. **Launch the Jupyter dashboard:**

   ```bash
   jupyter notebook builder_dash.ipynb
   ```

3. **Configure your practice** using the interactive widgets in the notebook (duration, move categories, rep counts, etc.).

4. **Generate the practice plan** — the output will be a structured practice schedule built from moves in the CSV library.

---

## Customizing the Move Library

Moves are stored in `test_moves.csv`. You can add, remove, or modify moves by editing this file directly. Each row represents a move with its associated metadata (e.g., name, category, difficulty).


## License

This project does not currently include a license file. Please contact the repository owner before using or distributing this code.
