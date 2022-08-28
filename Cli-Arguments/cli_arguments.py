import typer
from typing import Optional
def main(a: str = typer.Argument(...),b: Optional[int] = typer.Argument(None)):
    typer.echo(f"The <a> required argument: {a}")
    typer.echo(f"The <b> optional argument: {b}")

if __name__ == "__main__":
    typer.run(main)    