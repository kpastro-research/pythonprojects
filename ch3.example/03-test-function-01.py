# Example function to process time
def process_value(value):
    if ":" in value:
        min, second_centi = value.split(":")
        if "." in second_centi:
            second, centi = second_centi.split(".")
        else:
            second = second_centi
            centi = "0"
    else:
        min = 0
        if "." in value:
            second, centi = value.split(".")
        else:
            second = value
            centi = "0"
    return min, second, centi



def process_line(lineInFile):
    valuesInLine = lineInFile.split(',')
    swimmerTimings = list()
    for values in valuesInLine:
        min, second, centi = process_value(values)

        swimmerTimings.append((min,second, centi))
    return swimmerTimings


lineInFile1="1:27.95,1:21.07,1:30.96,1:23.22,1:27.95,1:28.30"
print(process_line(lineInFile1))
lineInFile2="39.07,37.66,36.13,39.42"
print(process_line(lineInFile2))