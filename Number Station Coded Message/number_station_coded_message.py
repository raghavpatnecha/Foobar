def answer(l, t):

    input_list = l
    target = t

    summed_num = 0
    result = []

    for i, elm in enumerate(input_list):

        for j in range(i, len(input_list)):

            summed_num += input_list[j]

            if summed_num == target:

                result.append([i, j])

        summed_num = 0

    if len(result) == 0:
        return [-1, -1]
    else:
        return result[0]
