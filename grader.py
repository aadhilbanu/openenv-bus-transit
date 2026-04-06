from tasks.easy import grade as easy_grade
from tasks.medium import grade as medium_grade
from tasks.hard import grade as hard_grade

def evaluate(task, **kwargs):
    if task == "easy":
        return easy_grade(kwargs["state"], kwargs["reward"])
    elif task == "medium":
        return medium_grade(kwargs["time"])
    elif task == "hard":
        return hard_grade(kwargs["time"], kwargs["seats"])
