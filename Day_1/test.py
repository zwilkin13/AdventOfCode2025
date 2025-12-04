def load_file_path(input_file):
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, input_file)

file_path = load_file_path('text_input.txt')

with open(file_path, 'r') as input:
    password = 0
    dial_pos = 50
    for line in input:
        dir = line[0]
        num = line[1:]
        if dir == 'L':
            dial_pos -= int(num)
        else:
            dial_pos += int(num)

        while dial_pos < 0:
            dial_pos += 100

        while dial_pos > 99:
            dial_pos -= 100

        if dial_pos == 0:
            password += 1

    print(password)


# Part Two
with open(file_path, 'r') as input:
    password = 0
    dial_pos = 50
    for line in input:
        dir = line[0]
        num = line[1:]
        start_pos = dial_pos
        if dir == 'L':
            dial_pos -= int(num)
        else:
            dial_pos += int(num)

        prev_hundreds = start_pos // 100
        cur_hundreds = dial_pos // 100

        password += abs(cur_hundreds - prev_hundreds)

        if dir == 'L':
            # if we end on 0 moving to the left, we will have missed adding 1 to the password
            # in the abs() part, so we need to account for that by adding 1 to the result
            if dial_pos % 100 == 0:
                password += 1

            # if we started at 0 and moved to the left we need to account for the fact that 
            # we counted the passing over the 0 value in the previous loop
            if start_pos % 100 == 0:
                password -= 1

    print(password)