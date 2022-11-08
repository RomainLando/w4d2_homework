import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository 
import repositories.user_repository as user_repository


# task_repository.delete_all()
# user_repository.delete_all()


# task1= Task('Laundry', 'Steve', 120, False)
# task_repository.save(task1)

# task1= Task('Portfolio', 'Megan', 90, False)
# task_repository.save(task1)


# task_repository.save(task1)

# user1= User('Romain', "Landolfini")
# user2= User('Alexia', "Smith")
# task1= Task('Portfolio', 'Romain', 90, user1, False)
# task2= Task('Shopping', 'Alexia', 50, user2, False)

# user_repository.save(user1)
# user_repository.save(user2)

# task_repository.save(task1)
# task_repository.save(task2)
user = user_repository.select(5)

print(user_repository.tasks(user))
#     print(user.__dict__)

# print(task_repository.select(11))
# task_repository.update(task1)
# task_repository.delete(10)
