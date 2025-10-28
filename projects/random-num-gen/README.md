# Random Number Generator 🎲  
A small Python tool in the **py-libs** collection by [bugOpsX](https://github.com/bugOpsX) that lets you generate random numbers easily.  
Ideal for learning, experiments, quick utilities, and extending into more advanced randomness & sampling tasks.

---

## 🚀 Features  
- Generate one or many random numbers within a specified range (integer and/or float).  
- Optionally set a seed for reproducibility (very handy for testing, demos).  
- Simple, lightweight, no heavy dependencies (pure Python standard library).  
- Easily extendable: e.g., adding distributions, sampling without replacement, more complex workflows.

---

## 🧰 Getting Started  
### Prerequisites  
- Python 3.7+ (or whichever version you used)  
- Standard library only (no external packages needed)  

### Installation  
Clone the repo (if you haven’t already):  
```bash
git clone https://github.com/bugOpsX/py-libs.git  
cd py-libs/projects/random-num-gen  
```
You can run the main script or import the module into your own code.

### Usage
Here’s a quick example of how you might run/generate numbers:
```
from random_num_gen import generate_random_numbers

# generate 5 random integers between 1 and 100
nums = generate_random_numbers(count=5, min_val=1, max_val=100, integer=True, seed=42)
print(nums)

# generate 10 random floats between 0.0 and 1.0
floats = generate_random_numbers(count=10, min_val=0.0, max_val=1.0, integer=False)
print(floats)
```
### 📖 How it Works

- Utilises Python’s built-in random module to generate pseudorandom numbers.
- If a seed is provided, the sequence becomes reproducible (great for tests / demos).
- If integer mode: uses randint(a, b) (or equivalent logic)
- If float mode: uses uniform(a, b) (or equivalent)
- Enough flexibility so you can build further: distributions, custom generators, sampling, etc.


