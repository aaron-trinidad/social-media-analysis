# Social Media Analysis (Synthetic Data)

## Overview

This is a small educational project demonstrating **data loading, cleaning, exploratory data analysis (EDA), visualization, and a simple machine learning example** on a synthetic Twitter-like dataset.  
The dataset is generated with Python and includes features such as `followers`, `likes`, `retweets`, `category`, `sentiment`, `posted_hour`, and a target variable `viral`.

The purpose of this project is **to illustrate common techniques in data analysis** and provide a simple example workflow.

---

## Project Structure

```
social-media-analysis/
├─ data/                   # Generated dataset CSV
├─ notebooks/              # Jupyter notebook(s) for analysis
│   └─ social_media_analysis.ipynb
├─ src/                    # Python scripts
│   └─ generate_dataset.py
└─ README.md
```

---

## Getting Started

1. **Generate the dataset** (optional, if not already present) This can be done via the script or directly from a notebook cell:

```bash
python src/generate_dataset.py
```

2. **Open the notebook** to explore and analyze the data:

```bash
jupyter notebook notebooks/social_media_analysis.ipynb
```

3. **Follow the notebook steps** to:
   - Load the dataset
   - Perform exploratory data analysis
   - Handle missing values and outliers
   - Visualize distributions and relationships

---

## Dependencies

- Python 3.8+
- All dependencies are listed in `requirements.txt`

Install dependencies via pip if needed:

```bash
pip install -r requirements.txt
```

---

## Notes

- This is a **synthetic dataset**, generated for demonstration purposes.

---

## Author

Aaron Trinidad
