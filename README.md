# Data Cleaning CSV Tool

## Overview
This project is a simple Python program that cleans CSV files.  
It removes duplicate rows and can optionally filter data based on conditions.

---

## Features
- Reads CSV files
- Removes duplicate rows based on a column or entire row
- Optional filtering of rows (example: `age > 20`)
- Saves cleaned data to a new CSV file

---

## Example Dataset (Before Cleaning)

| Name  | Age | City   |
|-------|-----|--------|
| John  | 20  | London |
| Mary  | 22  | Paris |
| John  | 20  | London |
| James | 25  | Berlin |
| Mary  | 22  | Paris |

---

## Cleaning Duplicates

You can remove duplicates by:

- Specifying a column (example: `name`)  
- Leaving the column blank to remove exact duplicate rows

---

## Result (After Cleaning by Name)

| Name  | Age | City   |
|-------|-----|--------|
| John  | 20  | London |
| Mary  | 22  | Paris |
| James | 25  | Berlin |

---

## How to Run

1. Open a terminal in the project folder  
2. Run the program:

```bash
python data_cleaner.py