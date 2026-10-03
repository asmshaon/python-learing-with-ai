# Learning Python with AI

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Chapters done](https://img.shields.io/badge/chapters%20done-47%20%2F%2097-2ea44f)
![Status](https://img.shields.io/badge/status-in%20progress-orange)

My hands-on study log for the full Python curriculum, from the first `print()`
to machine learning, data structures and databases. I use an AI pair
(Claude) as a tutor: it helps me read up on each topic, design practice
problems and review my solutions. **I write and run the code myself.**

> **Why share it?** Learning in public keeps me consistent. Every chapter is a
> small, runnable file, so you can see exactly what I practised and how I
> solved it.

---

## Progress at a glance

| #   | Section                      | Folder                                                         | Done        | Status         |
| --- | ---------------------------- | -------------------------------------------------------------- | ----------- | -------------- |
| 01  | Python Basics                | [`01_basics/`](chapters/01_basics/)                            | 33 / 33     | ✅ Complete    |
| 02  | Object-Oriented Programming  | [`02_oop/`](chapters/02_oop/)                                  | 10 / 10     | ✅ Complete    |
| 03  | File Handling                | [`03_file_handling/`](chapters/03_file_handling/)              | 4 / 4       | ✅ Complete    |
| 04  | Popular Libraries            | [`04_libraries/`](chapters/04_libraries/)                      | 0 / 5       | 🚧 In progress |
| 05  | Machine Learning             | [`05_machine_learning/`](chapters/05_machine_learning/)        | 0 / 23      | ⏳ Planned     |
| 06  | Data Structures & Algorithms | `06_dsa/`                                                      | 0 / 20      | ⏳ Planned     |
| 07  | Databases                    | `07_databases/`                                                | 0 / 2       | ⏳ Planned     |
|     | **Total**                    |                                                                | **47 / 97** |                |

---

## How each chapter works

Every chapter is **one self-contained Python file** with the same layout:

1. **Notes**: the module docstring summarises the concept, key syntax and
   common gotchas. It works as a cheat sheet I can come back to.
2. **Three problems** (`problem_1()`, `problem_2()`, `problem_3()`), each with
   a worked solution that **returns** its result so it can be tested.
3. **A `__main__` block** that runs all three and prints the answers.

A short excerpt from
[`14_dictionaries.py`](chapters/01_basics/14_dictionaries.py):

```python
"""
Chapter 14: Python Dictionaries
...
- person.get("email", "-")   returns the fallback "-" instead of raising
- b = a does NOT copy. Use a.copy() for a shallow copy,
  copy.deepcopy(a) for a full copy.
"""

# Problem 1: Safe reads and writes
#   (Test with {"name": "Ana", "age": 30}
#    -> expected ({'name': 'Ana', 'age': 31, 'city': 'Dhaka'}, 'unknown'))
def problem_1(): ...
```

---

## Run it yourself

The chapters for sections 01–03 use **only the standard library**:

```bash
git clone https://github.com/asmshaon/python-learing-with-ai.git
cd python-learing-with-ai

python3 chapters/01_basics/01_syntax.py          # run one chapter

# run every chapter as a quick smoke test
find chapters -name '*.py' -not -name '_template.py' -not -path '*/rough-khata/*' \
  -exec python3 {} \;
```

Sections 04 (libraries), 05 (ML) and 07 (databases) need third-party packages:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

To start a new chapter, copy [`chapters/_template.py`](chapters/_template.py).

---

## Repository layout

```text
chapters/
├── _template.py            # starting point for every chapter
├── 01_basics/              # 01_syntax.py … 33_virtualenv.py
├── 02_oop/                 # classes, inheritance, polymorphism, encapsulation …
├── 03_file_handling/       # open / read / write / delete files
├── 04_libraries/           # NumPy, pandas, SciPy, Django, Matplotlib
│   ├── data/               # sample CSVs used by the pandas practice
│   ├── *_practice.ipynb    # Jupyter notebooks for exploratory practice
│   └── *_scratch.py        # quick experiments
├── 05_machine_learning/
└── rough-khata/            # rough notebook ("khata"): asyncio and other experiments
```

---

## Detailed progress

<details>
<summary><b>01 · Python Basics</b> (33 / 33) ✅</summary>

| #   | Chapter           | Status |
| --- | ----------------- | ------ |
| 01  | Syntax            | ✅     |
| 02  | Output            | ✅     |
| 03  | Comments          | ✅     |
| 04  | Variables         | ✅     |
| 05  | Data Types        | ✅     |
| 06  | Numbers           | ✅     |
| 07  | Casting           | ✅     |
| 08  | Strings           | ✅     |
| 09  | Booleans          | ✅     |
| 10  | Operators         | ✅     |
| 11  | Lists             | ✅     |
| 12  | Tuples            | ✅     |
| 13  | Sets              | ✅     |
| 14  | Dictionaries      | ✅     |
| 15  | If...Else         | ✅     |
| 16  | Match             | ✅     |
| 17  | While Loops       | ✅     |
| 18  | For Loops         | ✅     |
| 19  | Functions         | ✅     |
| 20  | Range             | ✅     |
| 21  | Arrays            | ✅     |
| 22  | Iterators         | ✅     |
| 23  | Modules           | ✅     |
| 24  | Dates             | ✅     |
| 25  | Math              | ✅     |
| 26  | JSON              | ✅     |
| 27  | RegEx             | ✅     |
| 28  | PIP               | ✅     |
| 29  | Try...Except      | ✅     |
| 30  | String Formatting | ✅     |
| 31  | None              | ✅     |
| 32  | User Input        | ✅     |
| 33  | VirtualEnv        | ✅     |

</details>

<details>
<summary><b>02 · Object-Oriented Programming</b> (10 / 10) ✅</summary>

| #   | Chapter          | Status |
| --- | ---------------- | ------ |
| 01  | Python OOP       | ✅     |
| 02  | Classes/Objects  | ✅     |
| 03  | `__init__` Method | ✅    |
| 04  | self Parameter   | ✅     |
| 05  | Class Properties | ✅     |
| 06  | Class Methods    | ✅     |
| 07  | Inheritance      | ✅     |
| 08  | Polymorphism     | ✅     |
| 09  | Encapsulation    | ✅     |
| 10  | Inner Classes    | ✅     |

</details>

<details>
<summary><b>03 · File Handling</b> (4 / 4) ✅</summary>

| #   | Chapter            | Status |
| --- | ------------------ | ------ |
| 01  | File Handling      | ✅     |
| 02  | Read Files         | ✅     |
| 03  | Write/Create Files | ✅     |
| 04  | Delete Files       | ✅     |

</details>

<details open>
<summary><b>04 · Popular Libraries</b> (0 / 5) 🚧</summary>

| #   | Chapter        | Status                                     |
| --- | -------------- | ------------------------------------------ |
| 01  | NumPy          | 🚧 practising in `numpy_practice.ipynb`    |
| 02  | pandas         | 🚧 practising in `pandas_practice.ipynb`   |
| 03  | SciPy          | 🚧 practising in `scipy_practice.ipynb`    |
| 04  | Django         | 📝 scaffolded                              |
| 05  | Matplotlib     | ⏳ planned                                 |

</details>

<details>
<summary><b>05 · Machine Learning</b> (0 / 23) ⏳</summary>

Getting Started · Mean, Median, Mode · Standard Deviation · Percentile ·
Data Distribution · Normal Data Distribution · Scatter Plot · Linear Regression ·
Polynomial Regression · Multiple Regression · Scale · Train/Test · Decision Tree ·
Confusion Matrix · Hierarchical Clustering · Logistic Regression · Grid Search ·
Categorical Data · K-means · Bootstrap Aggregation · Cross Validation ·
AUC-ROC Curve · K-Nearest Neighbors

</details>

<details>
<summary><b>06 · Data Structures & Algorithms</b> (0 / 20) ⏳</summary>

Python DSA · Lists and Arrays · Stacks · Queues · Linked Lists · Hash Tables ·
Trees · Binary Trees · Binary Search Trees · AVL Trees · Graphs · Linear Search ·
Binary Search · Bubble Sort · Selection Sort · Insertion Sort · Quick Sort ·
Counting Sort · Radix Sort · Merge Sort

</details>

<details>
<summary><b>07 · Databases</b> (0 / 2) ⏳</summary>

Python MySQL · Python MongoDB

</details>

Legend: ✅ done · 🚧 in progress · 📝 scaffolded · ⏳ planned

---

## Connect

I'm **Abu Saleh Muhammad Shaon**. If you're also learning Python, or have tips
for the next sections, feel free to open an issue or reach out on LinkedIn.
⭐ Star the repo if you'd like to follow along.
