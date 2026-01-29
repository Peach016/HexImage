from rich.console import Console; from rich.style import Style
while True:
    try:
        for i in open(input(">>> "), "r").readlines():
            print()
            for a in i.split():
                try: Console().print("  " * int(a.split(",")[0]), style=Style(bgcolor=f"#{a.split(',')[1]}"), end="")
                except: Console().print("  ", style=Style(bgcolor=f"#{a}"), end="")
        print("\n")
    except FileNotFoundError: print("This file not found!")