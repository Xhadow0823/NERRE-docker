import os
from flask import send_file
from typing import List

def get_history_result_list() -> List[str]:
    if not os.path.isdir("./results"):
        os.mkdir("./results")
    return os.listdir("./results")
    
def get_history_result(filename):
    base_dir = "./results"
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        return send_file(filepath, )

def clear_all_results() -> bool:
    try:
        os.remove("results/*")
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__" :
    history = get_history_result_list()
    print(history)
