import click #to create a cli
import json # to save and load tasks from a file
import os # to check if the file exists

TODO_FILE="todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE,"r") as file:
        return json.load(file)
def save_tasks(tasks):
    with open(TODO_FILE,"w") as file:
        json.dump(tasks,file,indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass
@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks=load_tasks()
    tasks.append({"task":task,"Done":False})
    save_tasks(tasks)
    click.echo(f"Task added successfully:{task}")
    
@click.command()
def list():
    """List all the tasks"""
    tasks=load_tasks()
    if not tasks:
        click.echo("No tasks found")
        return
    for index,task in enumerate(tasks,start=1):
        status="✅" if task["Done"] else "❌"
        click.echo(f"{index}.{task['task']} [{status}]")
@click.command()
@click.argument("task_number",type=int)
def done(task_number):
    """Add new task to the list"""
    tasks=load_tasks()
    if 1<=task_number <=len(tasks):
        tasks[task_number -1 ]["Done"]=True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed!")
    else:
        click.echo("Invalid task number.")

@click.command()
@click.argument("task_number" ,type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks=load_tasks()
    if 1<=task_number <=len(tasks):
        removed_task=tasks.pop(task_number -1)
        save_tasks(tasks)  # Save updated task list
        click.echo(f"Deleted task: {removed_task['task']}")
    else:
        click.echo("Invalid task number.")
        
cli.add_command(remove)

cli.add_command(done)
cli.add_command(add)
cli.add_command(list)
if __name__ == "__main__":
    cli()