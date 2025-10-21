from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.panel import Panel

console = Console()

def welcome_message():
    console.print("[bold magenta]Welcome to [cyan]Py-Libs![/cyan][/bold magenta]", style="bold green")

def highlight_text(text, color="yellow", style="bold"):
    console.print(f"[{style} {color}]{text}[/{style} {color}]")

def display_table(data, columns):
    """
    data: List of tuples or lists
    columns: List of column names
    """
    table = Table(show_header=True, header_style="bold blue")
    for col in columns:
        table.add_column(col)
    
    for row in data:
        table.add_row(*[str(i) for i in row])
    
    console.print(table)

def show_progress(task_name="Processing", total=100):
    console.print(f"[bold green]{task_name}:[/bold green]")
    for _ in track(range(total), description="Working..."):
        pass  # Replace with your actual task

def fun_panel(message="Hello!"):
    panel = Panel(message, title="Fun Panel", subtitle="Made with Rich", style="bold magenta")
    console.print(panel)
