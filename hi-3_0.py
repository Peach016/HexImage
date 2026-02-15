from rich.console import Console
from rich.style import Style
console = Console()

def separation(text: str, width: int):
    a, lst = 0, list(text)
    for i in range(1, len(text)):
        if i % width == 0:
            if a == 0: lst.insert(i, " ")
            if a > 0: lst.insert(i + a, " ")
            a += 1
    return ''.join(lst)

with open(input(">>> "), "rb") as fil:
    fil = bytes.hex(fil.read())
    width = int(fil[:4], 16)
    height = int(fil[4:8], 16)
    pixels = separation(fil[8:], 6).split()
    counter = 0
    if height > 1:
        for pixel in pixels:
            if counter % width == 0 and counter != 0:
                print("\n", end="")
                
            console.print("  ", style=Style(bgcolor=f"#{pixel}"), end="")
            counter += 1
print("\n")