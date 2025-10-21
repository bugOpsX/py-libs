"""
Feature: Colorful Console Output using Rich
Description:
Adds colorful, stylish console messages with highlights, tables, and progress bars.
"""

from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep

console = Console()

def welcome_message():
    """Display a fun, colorful welcome message."""
    console.print("[bold magenta]✨ Welcome to Py-Libs! ✨[/bold magenta]")
    console.print("[green]Bringing life and color to your console![/green]\n")

def highlight_examples():
    """Showcase text highlighting and styling."""
    console.print("[bold blue]Info:[/bold blue] This is an informational message.")
    console.print("[bold yellow]Warning:[/bold yellow] Be cautious here.")
    console.print("[bold red]Error:[/bold red] Something went wrong!\n")

def show_table():
    """Display a colorful table."""
    table = Table(title="Py-Libs Contributors", style="bold cyan")
    table.add_column("Name", style="green", justify="center")
    table.add_column("Role", style="yellow", justify="center")
    table.add_column("Status", style="magenta", justify="center")

    table.add_row("Apurva", "Developer", "🔥 Active")
    table.add_row("You!", "Contributor", "⚡ Pending")
    console.print(table)
    console.print()

def show_progress():
    """Display a progress bar."""
    console.print("[cyan]Simulating progress...[/cyan]")
    for _ in track(range(10), description="[magenta]Processing...[/magenta]"):
        sleep(0.2)
    console.print("[bold green]✅ Done![/bold green]\n")

def demo():
    """Run all features together."""
    welcome_message()
    highlight_examples()
    show_table()
    show_progress()

if __name__ == "__main__":
    demo()