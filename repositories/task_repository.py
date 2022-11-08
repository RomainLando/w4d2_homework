from db.run_sql import run_sql
import repositories.user_repository as user_repository
from models.task import Task
  
def select_all():  
    tasks = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['id'])
        task = Task(row['description'], row['assignee'], row['duration'], user, row['completed'], row['id'] )
        tasks.append(task)
    return tasks 

def save(task):
    sql = """
    INSERT INTO tasks
    (description, assignee, duration, completed, user_id)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING *
    """
    values = [task.description, task.assignee, task.duration, task.completed, task.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task

def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user= user_repository.select(result['user_id'])
        task = Task(result['description'], result['assignee'], result['duration'], user, result['completed'])
    return task

def delete(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(task):
    sql = """
    UPDATE tasks SET (description, assignee, duration, completed, user_id)
    = (%s, %s, %s, %s, %s) WHERE id = %s
    """
    values = [task.description, task.assignee, task.duration, task.completed, task.user.id, task.id]
    run_sql(sql, values)