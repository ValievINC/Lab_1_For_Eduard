def generate_x_list(k):
    x_list = []
    x_0 = []
    for i in range(N):
        x_0.append(1)
    x_list.append(x_0)

    counts = 2**k
    multiplier = 1
    value = [1, -1]
    while k > 0:
        multiplier *= 2
        counts = counts // 2
        x_list.extend([value * counts])
        new_value = [[1] * multiplier, [-1] * multiplier]
        value = [element for sublist in new_value for element in sublist]
        k -= 1
    return x_list


def generate_multiplications(x_list):
    x_temp = []
    x_mult = []
    for i in range(1, len(x_list)-1):
        for j in range(i+1, len(x_list)):
            for el1, el2 in zip(x_list[i], x_list[j]):
                x_temp.append(el1 * el2)
            x_mult.append(x_temp[:])
            x_temp.clear()
    return x_mult


def generate_big_x_values_list(x_min, x_max, k):
    big_x_list = []
    counts = 2 ** k
    multiplier = 1
    value = [x_max[0], x_min[0]]
    i = 0
    while k > 0:
        i += 1
        multiplier *= 2
        counts = counts // 2
        big_x_list.extend([value * counts])
        if i <= k:
            new_value = [[x_max[i]] * multiplier, [x_min[i]] * multiplier]
            value = [element for sublist in new_value for element in sublist]
        else:
            break
        k -= 1
    return big_x_list


k = int(input())
x_min = []
x_max = []
for i in range(k):
    values = list(map(int, input().split()))
    x_min.append(values[0])
    x_max.append(values[1])

N = 2**k    # Количество опытов, необходимое для построения математической модели

y = list(map(int, input().split()))

x_list = generate_x_list(k)
x_mult = generate_multiplications(x_list)
x_fulllist = x_list + x_mult

b = []
temp = []
for i in range(len(x_fulllist)):
    for el1, el2 in zip(x_fulllist[i], y):
        temp.append(el1 * el2)
    result = sum(temp)/N
    b.append(result)
    temp.clear()

ratios = [str(b[0])]
for i in range(1, len(b)):
    if b[i] != 0:
        ratios.append(str(b[i]) + f'x{i}')

print('y =', ''.join(ratios))

x_delta_max = []
x_delta_min = []
for i in range(len(x_max)):
    x_delta_max.append((x_max[i] + x_min[i]) / 2)
    x_delta_min.append((x_max[i] - x_min[i]) / 2)

number_of_opit = int(input())

total = 0
for i in range(len(x_fulllist)):
    total += b[i] * x_fulllist[i][number_of_opit - 1]

print(total)

big_x_list = generate_big_x_values_list(x_min, x_max, k)

total_2 = b[0]
for i in range(len(x_max)):
    total_2 += b[i+1] * ((big_x_list[i][number_of_opit - 1] - x_delta_max[i]) / x_delta_min[i])

print(total_2)