import requests
import sys

def get_employee_todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Get employee details
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data['name']
    
    # Get employee's TODO list
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    if todos_response.status_code != 200:
        print(f"Could not retrieve TODO list for employee ID {employee_id}.")
        return
    
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)
    
    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_list_progress(employee_id)
