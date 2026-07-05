from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()
APP_NAME = "PATTERN STUDIO"
APP_VERSION = "1.0"
SAVE_DIR = Path("pattern_outputs")
SAVE_DIR.mkdir(exist_ok=True)

@dataclass
class PatternResult:
    name: str
    lines: list[str]
    symbol: str
    height: int
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    @property
    def total_symbols(self) -> int:
        return sum(line.count(self.symbol) for line in self.lines)

    @property
    def max_width(self) -> int:
        return max((len(line) for line in self.lines), default=0)

def clear_screen() -> None:
    console.clear()

def pause(prompt: str = "\nTekan Enter untuk lanjut...") -> None:
    try:
        input(prompt)
    except (EOFError, KeyboardInterrupt):
        pass

def ask_text(prompt: str, default: str | None = None) -> str:
    try:
        if default is None:
            value = input(f"{prompt}: ").strip()
        else:
            value = input(f"{prompt} ({default}): ").strip()
        return value
    except (EOFError, KeyboardInterrupt):
        return ""

def ask_int(prompt: str, default: int = 5, minimum: int = 1, maximum: int = 30) -> int:
    while True:
        try:
            raw = input(f"{prompt} ({default}): ").strip()
            if raw == "":
                return default
            num = int(raw)
            if minimum <= num <= maximum:
                return num
            console.print(f"[red]Masukkan angka {minimum} sampai {maximum}.[/red]")
        except ValueError:
            console.print("[red]Input harus angka.[/red]")
        except (EOFError, KeyboardInterrupt):
            return default

def banner() -> None:
    clear_screen()
    now = datetime.now()

    info = Table.grid(padding=(0, 2))
    info.add_column(justify="left", no_wrap=True)
    info.add_column(justify="left")

    info.add_row("👤 User", ": Edward")
    info.add_row("🐍 Python", ": 3.13")
    info.add_row("📅 Date", f": {now.strftime('%d %b %Y')}")
    info.add_row("⏰ Time", f": {now.strftime('%H:%M:%S')}")
    info.add_row("💾 Version", f": {APP_VERSION}")

    console.print(
        Panel(
            info,
            title=f"[bold]{APP_NAME}[/bold]",
            border_style="white",
            padding=(1, 2),
        )
    )

def loading() -> None:
    console.print("[dim]Membuat pola[/dim]", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print()

# ===== PATTERN GENERATORS =====
def triangle_left(height: int, symbol: str) -> list[str]:
    return [symbol * i for i in range(1, height + 1)]

def triangle_right(height: int, symbol: str) -> list[str]:
    return [" " * (height - i) + symbol * i for i in range(1, height + 1)]

def triangle_reverse(height: int, symbol: str) -> list[str]:
    return [symbol * i for i in range(height, 0, -1)]

def pyramid(height: int, symbol: str) -> list[str]:
    return [" " * (height - i - 1) + symbol * (2 * i + 1) for i in range(height)]

def diamond(height: int, symbol: str) -> list[str]:
    top = pyramid(height, symbol)
    bottom = pyramid(height - 1, symbol)[::-1] if height > 1 else []
    return top + bottom

def hollow_pyramid(height: int, symbol: str) -> list[str]:
    lines: list[str] = []
    for i in range(height):
        if i == 0:
            lines.append(" " * (height - 1) + symbol)
        elif i == height - 1:
            lines.append(symbol * (2 * height - 1))
        else:
            inner = " " * (2 * i - 1)
            lines.append(" " * (height - i - 1) + symbol + inner + symbol)
    return lines

def x_pattern(height: int, symbol: str) -> list[str]:
    lines = []
    for i in range(height):
        row = []
        for j in range(height):
            row.append(symbol if j == i or j == (height - 1 - i) else " ")
        lines.append("".join(row))
    return lines

def christmas_tree(height: int, symbol: str) -> list[str]:
    leaves = pyramid(height, symbol)
    trunk_pad = " " * (height - 1)
    trunk = [trunk_pad + "|||" for _ in range(2)]
    star = " " * (height - 1) + "★"
    return [star] + leaves + trunk

def hourglass(height: int, symbol: str) -> list[str]:
    if height < 2:
        return [symbol]
    top = [" " * i + symbol * (2 * (height - i) - 1) for i in range(height)]
    bottom = top[-2::-1]
    return top + bottom

def checkerboard(height: int, symbol: str) -> list[str]:
    lines = []
    for i in range(height):
        row = []
        for j in range(height):
            row.append(symbol if (i + j) % 2 == 0 else " ")
        lines.append("".join(row))
    return lines

def frame_box(height: int, symbol: str) -> list[str]:
    width = max(2, height * 2)
    top_bottom = symbol * width
    if height == 1:
        return [symbol]
    if height == 2:
        return [top_bottom, top_bottom]
    middle = [symbol + " " * (width - 2) + symbol for _ in range(height - 2)]
    return [top_bottom] + middle + [top_bottom]

def stair_left(height: int, symbol: str) -> list[str]:
    return [symbol * i for i in range(1, height + 1)]

def stair_right(height: int, symbol: str) -> list[str]:
    return [" " * (height - i) + symbol * i for i in range(1, height + 1)]

def plus_pattern(height: int, symbol: str) -> list[str]:
    size = height if height % 2 == 1 else height + 1
    mid = size // 2
    lines = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(symbol if i == mid or j == mid else " ")
        lines.append("".join(row))
    return lines

def border_triangle(height: int, symbol: str) -> list[str]:
    lines = []
    for i in range(1, height + 1):
        if i == 1:
            lines.append(symbol)
        elif i == height:
            lines.append(symbol * i)
        else:
            lines.append(symbol + " " * (i - 2) + symbol)
    return lines

def hollow_diamond(height: int, symbol: str) -> list[str]:
    lines = []
    for i in range(height):
        if i == 0:
            lines.append(" " * (height - 1) + symbol)
        else:
            inner = " " * (2 * i - 1)
            lines.append(" " * (height - i - 1) + symbol + inner + symbol)
    for i in range(height - 2, -1, -1):
        if i == 0:
            lines.append(" " * (height - 1) + symbol)
        else:
            inner = " " * (2 * i - 1)
            lines.append(" " * (height - i - 1) + symbol + inner + symbol)
    return lines

BASE_PATTERNS: list[tuple[str, Callable[[int, str], list[str]], str]] = [
    ("Triangle Left", triangle_left, "classic rising triangle"),
    ("Triangle Right", triangle_right, "right-aligned triangle"),
    ("Triangle Reverse", triangle_reverse, "descending triangle"),
    ("Pyramid", pyramid, "centered pyramid"),
    ("Diamond", diamond, "clean diamond"),
    ("Hollow Pyramid", hollow_pyramid, "outlined pyramid"),
    ("X Pattern", x_pattern, "cross shape"),
    ("Christmas Tree", christmas_tree, "tree style"),
    ("Hourglass", hourglass, "sand timer style"),
    ("Checkerboard", checkerboard, "grid pattern"),
    ("Frame Box", frame_box, "simple border"),
    ("Stair Left", stair_left, "steps to the left"),
    ("Stair Right", stair_right, "steps to the right"),
    ("Plus Pattern", plus_pattern, "plus symbol"),
    ("Border Triangle", border_triangle, "triangle outline"),
]

PATTERNS: dict[str, tuple[str, Callable[[int, str], list[str]], str]] = {}
for idx in range(50):
    base_name, func, desc = BASE_PATTERNS[idx % len(BASE_PATTERNS)]
    variant = idx // len(BASE_PATTERNS) + 1
    key = str(idx + 1)
    label = f"{base_name} {variant}" if variant > 1 else base_name
    PATTERNS[key] = (label, func, desc)

def show_menu() -> None:
    table = Table(box=None, show_header=False, pad_edge=False, expand=True)

    for _ in range(5):
        table.add_column(justify="left", ratio=1)

    items = list(PATTERNS.items())

    for i in range(0, len(items), 5):
        row = []
        chunk = items[i:i + 5]

        for key, (name, func, _) in chunk:
            cell = Text()
            cell.append(f"{key}\n", style="cyan")
            cell.append(f"{name}\n", style="bold white")
            cell.append(preview_art(func, indent=2), style="dim")
            row.append(cell)

        while len(row) < 5:
            row.append("")

        table.add_row(*row)

        if i + 5 < len(items):
            table.add_row("", "", "", "", "")

    table.add_row(
        "[cyan]R[/cyan]\n[bold white]Random[/bold white]",
        "",
        "",
        "",
        "[cyan]0[/cyan]\n[bold white]Exit[/bold white]",
    )

    console.print(
        Panel(
            table,
            title="MENU",
            border_style="white",
            padding=(1, 2),
        )
    )
def preview_art(pattern_func: Callable[[int, str], list[str]], indent: int = 4) -> str:
    spaces = " " * indent
    lines = pattern_func(7, "*")
    return "\n".join(spaces + line for line in lines)

def render_pattern(result: PatternResult) -> None:
    text = "\n".join(result.lines)
    console.print(
        Panel(
            text,
            title=result.name,
            subtitle=f"Height {result.height} | Symbol {result.symbol}",
            border_style="white",
            padding=(1, 2),
        )
    )

def show_preview(pattern_name: str, pattern_func: Callable[[int, str], list[str]]) -> None:
    preview_lines = pattern_func(7, "*")
    console.print(
        Panel(
            "\n".join(preview_lines),
            title=f"Contoh {pattern_name} (tinggi 7)",
            border_style="dim",
            padding=(1, 2),
        )
    )

def save_result(result: PatternResult) -> Path:
    filename = SAVE_DIR / f"{result.name.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with filename.open("w", encoding="utf-8") as f:
        f.write(f"{APP_NAME}\n")
        f.write(f"Pattern : {result.name}\n")
        f.write(f"Height  : {result.height}\n")
        f.write(f"Symbol  : {result.symbol}\n")
        f.write(f"Time    : {result.created_at}\n\n")
        f.write("\n".join(result.lines))
    return filename

def main() -> None:
    try:
        while True:
            banner()
            show_menu()
            while True:
                choice = ask_text("Choice", None).strip().upper()

                if choice == "":
                    continue

                if choice == "0":
                    console.print("\n[dim]Program selesai.[/dim]")
                    return

                if choice == "R":
                    choice = random.choice(list(PATTERNS.keys()))
                    console.print(f"[green]Random selected:[/green] {PATTERNS[choice][0]}")

                if choice not in PATTERNS:
                    console.print("[red]Pilihan tidak valid.[/red]")
                    continue

                pattern_name, pattern_func, _ = PATTERNS[choice]
                break

            height = ask_int("Height", default=5, minimum=1, maximum=30)
            symbol = ask_text("Symbol", "*").strip() or "*"

            loading()
            lines = pattern_func(height, symbol)
            result = PatternResult(pattern_name, lines, symbol, height)

            banner()
            render_pattern(result)

            console.print(
                f"\n[white]Total symbol:[/white] {result.total_symbols}   "
                f"[white]Width:[/white] {result.max_width}"
            )

            save_choice = ask_text("Save output? (y/t)", "y").lower().strip()
            if save_choice == "y":
                file_path = save_result(result)
                console.print(f"[green]Saved:[/green] {file_path}")

            pause("\nTekan Enter untuk kembali ke menu...")

    except KeyboardInterrupt:
        console.print("\n[red]Dihentikan.[/red]")

if __name__ == "__main__":
    main()
