def compute_running_total(input_list):
    running_total = []
    total = 0

    for num in input_list:
        total += num
        running_total.append(total)

    return running_total