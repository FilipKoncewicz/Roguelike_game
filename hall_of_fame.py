def hall_of_fame_dict(filename):
    data_set = {}
    data = []
    keys = []
    values = []
    with open(filename) as file:
        for line in file:
          data.append(line.strip().split(','))
        for pair in data:
           keys.append(pair[0])
           values.append(int(pair[1]))
        data_set = dict(zip(keys, values))
    return data_set


def display_dict(filename):
  data_set = hall_of_fame_dict(filename)
  data_set = sort_dict(data_set)
  for index, (key, value) in enumerate(data_set.items()):
    print(f"{index + 1}: {key} - {value}\n")


def sort_dict(data_set):
  data_set = dict(sorted(data_set.items(), key = lambda x: x[1], reverse = True))
  return data_set


def save_to_hall_of_fame(filename, name, score):
  data_set = hall_of_fame_dict(filename)
  with open(filename, 'w') as file:
    for key, value in data_set.items():
      file.write(f"{key}, {value}\n")
    file.write(f"{name}, {score}\n")