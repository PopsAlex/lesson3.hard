data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

_index = 0


def calculate_structure_sum(data):

    index_ = 0
    if isinstance(data, list):
        for i in data:
            index_ += calculate_structure_sum(i)
    if isinstance(data, dict):
        for key, value in data.items():
            index_ += calculate_structure_sum(key)
            index_ += calculate_structure_sum(value)
    if isinstance(data, tuple):
        for i in data:
            index_ += calculate_structure_sum(i)
    if isinstance(data, int):
        return data
    if isinstance(data, str):
        return len(data)
    if isinstance(data, float):
        return data
    if isinstance(data, set):
        for i in data:
            index_ += calculate_structure_sum(i)
    return index_


result = calculate_structure_sum(data_structure)
print(result)