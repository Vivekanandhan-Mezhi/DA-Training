# Task Management System
# Scenario: You are developing a task management system for a project. 
# Each task has a unique ID, a status (e.g., "to-do", "in-progress", "done"), and a list of 
# assigned team members. You need to update the task status and reassign team members based on 
# new information.

# Question: Write a function that takes a dictionary representing tasks 
# (task IDs as keys and a dictionary with status and team members as values), a task ID, a new status,
#  and a list of new team members. Return the updated tasks dictionary and the status of the operation.
def insert_into_list(list_to_be_updated, new_list):
    length_of_update_list = len(list_to_be_updated)
    length_of_new_list = len(new_list)
    index_counter = 0
    for position in range(length_of_update_list, length_of_update_list+length_of_new_list):
            list_to_be_updated.insert(position, new_list[index_counter])
            index_counter += 1
    return list_to_be_updated

def record_update(list_to_be_updated, new_list):
    length_of_update_list = len(list_to_be_updated)
    if length_of_update_list > 0:
        list_to_be_updated = insert_into_list(list_to_be_updated, new_list)
    else:  
        list_to_be_updated.clear()  
        list_to_be_updated = insert_into_list(list_to_be_updated, new_list) 
    return list_to_be_updated

def task_management(task_list, task_id, status, new_members):
    task_id_list = list(task_list.keys())
    if task_id not in task_id_list:
        task_list[task_id] = {status : new_members}        
    else:    
        for taskid, tasks in task_list.items():
            if taskid == task_id:
                tasks_keys = list(tasks.keys())[0]
                tasks_values = list(tasks.values())[0]
                if status == tasks_keys:
                    if tasks_keys != "done":
                        tasks_values = record_update(tasks_values, new_members)
                    else:
                        tasks_values.clear()
                else:
                    tasks_keys = status
                    tasks_values = record_update(tasks_values, new_members)
                task_list[task_id] = {tasks_keys : tasks_values}
                break    
    return task_list

list_of_tasks = {"T001": {"in-progress": ["M002", "M005"]},
                 "T002": {"done": ["M001, M004", "M003"]},
                 "T003": {"to-do": []}}

list_new_members = ["M006", "M001"]

print(task_management(list_of_tasks, "T002", "in-progress", list_new_members))