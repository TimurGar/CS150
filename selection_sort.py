from tempfile import tempdir


x = [60, 80, 40, 90, 97, 50, 95, 85]

def index_of_smallest_starting_at(x, d):
    best_index = d
    for i in range(d, len(x)):
        if x[i] < x[best_index]:
            best_index = i
    return best_index

def selection_sort(x):
    for i in range(0, len(x)):
        sm_ind = index_of_smallest_starting_at(x, i)
        temp = x[i]
        x[i] = x[sm_ind]
        x[sm_ind] = temp
    return x

print("begging x:", x)
print("final x:", selection_sort(x))
