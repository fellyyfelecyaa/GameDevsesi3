def main_py(no_list):
    A = [disk for disk in range (no_list, 0, -1)]
    B = []
    C = []

    def getList_string ():
        return f"{A} {B} {C}\n"
    
    def move_rings (start, goal):
        if not start:
            return
        goal.append(start.pop())
    
    def move_stick (start, goal, auxiliary, n):
        if n == 1:
            move_rings(start, goal)
            return getList_string()

        result = ""
        result += move_stick(start, auxiliary, goal, n - 1)

        move_rings(start, goal)
        result += getList_string()

        result += move_stick(auxiliary, goal, start, n - 1)
        return result

    return_str = getList_string()
    if no_list > 0:
        return_str += move_stick(A, C, B, no_list)

    return return_str

print(main_py(3))