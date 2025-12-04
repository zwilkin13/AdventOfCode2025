def load_file_path(input_file):
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, input_file)

def crack_that_fn_safe_man(input_file):
    with open(input_file, 'r') as turns:
        zero_count = 0
        dial = 50
        for turn in turns:
            if turn[0] == 'R':  dial += int(turn[1:])   # Right Turn
            else:               dial -= int(turn[1:])   # Left Turn
            while not (0 <= dial <= 99):
                dial = 100 - abs(dial) if dial < 0 else dial - 100
            if dial == 0:       zero_count += 1

    print(f"Cracked that mf! - {zero_count}")
...

file_path = load_file_path('text_input.txt')
crack_that_fn_safe_man(file_path)