from rich.console import Console; from rich.style import Style
while True:
    try:
        for i in open(input(">>> "), "r").readlines():
            print()
            for a in i.split():
                Console().print("  ", style=Style(bgcolor=f'#{a.replace("\ufeff", "")}'), end="")
        print("\n")
    except FileNotFoundError: print("This file not found!")