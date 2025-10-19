# 🎨 Rich Console Enhancer

## 🧩 Module Name
`color_console.py`

## 📘 Description
This module enhances console output using the [Rich](https://github.com/Textualize/rich) library.  
It adds colorful text, styled messages, tables, progress bars, and panels — making console logs more readable and engaging.

This contribution aims to improve the user experience and developer feedback in the terminal for the project.

---

## ✨ Features
- 🎨 Colorful and styled console messages  
- 🧱 Easy-to-read data tables  
- ⏳ Visual progress bars  
- 💬 Fun, interactive panels  
- 👋 A vibrant welcome message for your project  

---

## 🛠 Dependencies
Make sure you have the **Rich** library installed:

```bash
pip install rich
```

---

## 🧰 How to Use

### 1. Import the module
Place the `color_console.py` file inside your project directory (e.g., inside a `utils` or `libs` folder).

```python
from color_console import (
    welcome_message,
    highlight_text,
    display_table,
    show_progress,
    fun_panel
)
```

### 2. Example Usage

```python
# Display a colorful welcome message
welcome_message()

# Highlight text with custom colors and styles
highlight_text("Error: Invalid input!", color="red")
highlight_text("Process completed successfully!", color="green", style="bold")

# Create and show a data table
data = [
    ("Alice", 25, "Python"),
    ("Bob", 30, "Java"),
    ("Charlie", 22, "JavaScript")
]
columns = ["Name", "Age", "Language"]
display_table(data, columns)

# Show a progress bar
show_progress("Loading Data", total=50)

# Display a fun panel
fun_panel("Feature added successfully!")
```

---

## ⚙️ Functions Overview

| Function | Description |
|-----------|--------------|
| `welcome_message()` | Prints a colorful welcome banner |
| `highlight_text(text, color, style)` | Prints styled, highlighted text |
| `display_table(data, columns)` | Displays data in a formatted table |
| `show_progress(task_name, total)` | Shows a progress bar for any loop or task |
| `fun_panel(message)` | Displays a fun, styled panel message |

---

## 🧑‍💻 Contribution Context
This module was contributed to add **stylish and expressive console output** to improve developer interaction and readability.  
It’s lightweight, easy to integrate, and can be expanded to include emojis, gradients, or dynamic log styling.

---

## 🪪 License
This contribution is provided under the **MIT License** unless the main project specifies otherwise.

---

**Contributed by:** 
Ashutosh Agarwal [https://github.com/Ashutosh-agarwal2004]  

💡 *“Because even terminals deserve a little color.”*
