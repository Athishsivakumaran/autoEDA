# AutoEDA – Your Friendly EDA Assistant

AutoEDA is a simple Python tool that automatically explores your dataset and gives you a clean, easy-to-read report. If you're tired of writing the same code every time you start a new data science project, this library is for you.

---

##  What It Does

- Loads your CSV or DataFrame
- Tells you about:
  - Number of rows and columns
  - Duplicates and missing values
  - Column types (numerical, categorical, datetime)
  - Summary stats
  - Correlations between features
- Generates helpful plots like:
  - Histograms
  - Correlation heatmaps
  - Missing value matrix/bar
- Creates an EDA report (HTML or Markdown)

---

##  How to Use

### 1. Install it

```bash
pip install autoeda-lib
```

Or clone it:

```bash
git clone https://github.com/your-username/autoeda.git
cd autoeda
pip install -r requirements.txt
```

### 2. Run it

```python
from autoeda import AutoEDA

eda = AutoEDA("your_dataset.csv")  # or pass a DataFrame
eda.run()
```

You’ll get a full report in your current folder.

---

## Why Use This?

Because you want to:

- Save time on every new dataset
- Quickly spot data quality issues
- Make a good first impression in interviews and projects
- Understand your data before modeling

This tool shows your skills in the **first and most important step** of any ML pipeline.

---

## What's Next

- Smarter data type detection
- Time series support
- Cleaner suggestions for outliers and skewed data

---

## License

MIT License © 2025 Your Name

---

##  Feedback?

Open an issue, make a PR, or just say hi! Happy analyzing 