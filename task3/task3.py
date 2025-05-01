import json

name_file_values = input("Введите файл со значениями: ")
file_values = open(name_file_values)
data = json.load(file_values)
file_values.close()

values = {}
for item in data["values"]:
    number = item["id"]
    result = item["value"]
    values[number] =result

name_file_tests = input("Введите файл с тестами ")
file_tests = open(name_file_tests)
tests = json.load(file_tests)
file_tests.close()

def podstanovka_value(test):
    id = test["id"]
    if id in values:
        test["value"] = values[id]

    if "values" in test:
        for vnutrenniy_test in test["values"]:
            podstanovka_value(vnutrenniy_test)

for test in tests["tests"]:
    podstanovka_value(test)

name_file_output = input("Введите файл для результатов: ")
file_output = open(name_file_output, "w")
json.dump(tests, file_output, indent=2)
file_output.close()

print("Записано в: ", name_file_output)