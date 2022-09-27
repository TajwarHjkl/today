import json

from . import settings_manupulation
from . import paths

# get settings data
settings = settings_manupulation.settings

# todo
todo = []


def add(id=None, name=None, duration=None, category=None):
    '''
    add a new task
    '''

    global todo  
    
    # use default values if arguments are not provided
    if(not(name)):
        name = settings['default']['name']

    if(not(duration)):
        duration = settings['default']['duration']

    # create task
    task = {
        "name": name,
        "duration": int(duration),
        }

    # if task ID is provided, insert new task there
    if(type(id)==int):
        todo .insert(id, task)

    # else, append
    else:
        todo .append(task)

    # write task data
    write()

    return(True)

def remove(id=None):
    '''
    remove task
    '''

    global tasks

    # if ID is provided then remove that task
    if(type(id)==int):
        todo .pop(id)

    # else, remove the last task
    else:
        todo .pop()

    # write task data
    write()

    return(True)

def write():
    '''
    write task dat
    '''

    with open(paths.todo_path, 'w') as data:
        json.dump(todo, data)

    return(True)

def read():
    '''
    read task data
    '''

    global todo  
    try:
        with open(paths.todo_path, 'r') as data:
            todo = json.load(data)
    except FileNotFoundError:
        print('Todo file does not exist. Creating a new one.')
        write()

    return(True)

read()