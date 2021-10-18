import json

def csvToJSON(path_to_read, path_to_write):
    data_str = ""

    with open(path_to_read, "r", encoding="utf-8") as data_file:
        data_str = data_file.read()

    data_list = data_str.split('\n')

    data_json = []

    keys_json = []

    for i, data in enumerate(data_list):
        data_elements = data.split(", ")

        if i == 0:
            keys_json = data_elements
            continue

        data_dict = {}

        for i in range(len(keys_json)):
            data_dict[keys_json[i]] = data_elements[i]


        data_json.append(data_dict)

    with open(path_to_write, "w", encoding="utf-8") as data_file:
        json.dump(data_json, data_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    csvToJSON("./example_data.txt", "./example_data.json")