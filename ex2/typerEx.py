import json
import typer
import os
from typing import List

app = typer.Typer()
FILE_PATH = "data.json"
@app.command()
def add(json_str: str):
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        typer.echo("Invalid JSON")
        raise typer.Exit(code=1)
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                file_data = json.load(f)
            except json.JSONDecodeError:
                file_data = [] 
    else:
        file_data = []
    file_data.append(data)
    with open(FILE_PATH, "w") as f:
        json.dump(file_data, f, indent=2)
    typer.echo("JSON saved successfully")

@app.command()
def get_last_10():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                file_data = json.load(f)
            except json.JSONDecodeError:
                file_data = []  
    else:
        file_data = []
    last_10 = file_data[-10:]
    if last_10:
        typer.echo("Last 10 arguments:")
        for item in last_10:
            typer.echo(json.dumps(item, indent=2))
    else:
        typer.echo("No data available.")
if __name__ == "__main__":
    app()    














