#!/usr/bin/python

def get_data(filename):
    f = open(filename, "r")
    line = f.readline()
    case_count = int(line)
    case_list = []
    for i in xrange(case_count):
        button_list = []
        line = f.readline()
        pieces = line.split()
        button_count = int(pieces.pop(0))
        case_list.append((button_count, button_list))
        for j in xrange(button_count):
            button_list.append((pieces.pop(0),int(pieces.pop(0))))

    f.close()
    return case_list
    
def process_case(case):
    button_count, button_list = case
    step_count = 0
    cur_pos = {'O':0, 'B':0}
    for i in xrange(button_count):
        button = button_list.pop(0)
        other_index = 0
        while other_index < len(button_list) and button[0] == button_list[other_index][0]:
            other_index += 1
            
        button_pressed = False
        other_button = button_list[other_index] if other_index < len(button_list) else None
        # print "button, other button", button, other_button
        while not button_pressed:
            next_pos = move(cur_pos[button[0]], button[1])
            if next_pos is None:
                button_pressed = True
            else:
                cur_pos[button[0]] = next_pos
            
            if other_index < len(button_list):
                other_next_pos = move(cur_pos[button_list[other_index][0]], button_list[other_index][1])
                if other_next_pos is not None:
                    cur_pos[button_list[other_index][0]] = other_next_pos

            step_count += 1
        
    return step_count - 1
        
# return next pos
def move(cur_pos, target_pos):
    next_pos = None
    if cur_pos > target_pos:
        next_pos = cur_pos - 1
    elif cur_pos < target_pos:
        next_pos = cur_pos + 1
        
    return next_pos
    