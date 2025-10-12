from color_console import welcome_message, highlight_text, display_table, show_progress, fun_panel

welcome_message()

highlight_text("This is a warning!", color="red")
highlight_text("This is an info message", color="cyan", style="italic")

data = [
    ("Alice", 25, "Python"),
    ("Bob", 30, "Java"),
    ("Charlie", 22, "JavaScript")
]
columns = ["Name", "Age", "Language"]
display_table(data, columns)

show_progress("Loading Data", total=50)

fun_panel("You have successfully completed the demo!")
