def filter_long_names(students, min_length=5):
    result = []
    for name in students:
        if len(name) >= min_length:
            result.append(name)
    return result
print(filter_long_names(["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"]))
print(filter_long_names(["Ali", "Muhammad", "Jo"], 4))