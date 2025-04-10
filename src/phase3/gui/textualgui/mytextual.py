# Un mini tableau de bord terminal avec Textual
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container, Horizontal
from textual.reactive import reactive
from rich.text import Text
import random

class StatBox(Static):
    def __init__(self, title: str, value: str, style: str = "bold white on dark_green"):
        super().__init__()
        self.title = title
        self.value = value
        self.box_style = style

    def compose(self) -> ComposeResult:
        yield Static(Text(self.title, style="bold cyan"))
        yield Static(Text(self.value, style=self.box_style), classes="value")

    def update_value(self, new_value: str):
        self.query_one(".value", Static).update(Text(new_value, style=self.box_style))

class DashboardApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    Container {
        width: 80%;
        border: panel white;
        padding: 2;
    }
    .value {
        margin-top: 1;
        padding: 1 2;
        border: round white;
    }
    """

    counter = reactive(0)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Horizontal(
                StatBox("CPU Usage", "45%"),
                StatBox("RAM Usage", "3.2 GB"),
                StatBox("Disk I/O", "128 MB/s"),
            ),
            Button("Actualiser", id="refresh", variant="success")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "refresh":
            for box in self.query(StatBox):
                if "CPU" in box.title:
                    box.update_value(f"{random.randint(10, 95)}%")
                elif "RAM" in box.title:
                    box.update_value(f"{round(random.uniform(2.0, 6.0), 1)} GB")
                elif "Disk" in box.title:
                    box.update_value(f"{random.randint(80, 200)} MB/s")

if __name__ == "__main__":
    DashboardApp().run()