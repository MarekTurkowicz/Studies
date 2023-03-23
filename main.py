import os
import logo
logo.pprint()
def write_empty(file_name):
    with open(file_name + ".max", "w") as output_file:
        output_file.write("\n")
print("asdawdasdawd")
print("element of the new branch")
while (True):
    file_name = input("Podaj nazwę pliku: ")
    try:
        with open(file_name, "r") as file:
            file_contents = file.readlines()

            if not file_contents:
                write_empty(file_name)

            else:
                people = []
                for line in file_contents:
                    # print(line)
                    data = line.strip().split()
                    if len(data) == 4:
                        people.append(data)

                if not people:
                    write_empty(file_name)
                else:
                    max_efficiency_people = []
                    max_efficiency = 0
                    for person in people:
                        if len(person[0]) > 3 and person[1].endswith("ski"):
                            efficiency = float(person[3])
                            if efficiency > max_efficiency:
                                max_efficiency_people = [(person, efficiency)]
                                max_efficiency = efficiency
                            elif efficiency == max_efficiency:
                                max_efficiency_people.append((person, efficiency))

                    if max_efficiency_people:
                        output_file_name = file_name + ".max"
                        with open(output_file_name, "w") as output_file:
                            for person, efficiency in max_efficiency_people:
                                anonymized_surname = person[1][0] + "*" * (len(person[1]) - 4) + person[1][-3:]
                                output_file.write(f"{person[0]} {anonymized_surname} {person[2]}\n")
                    else:
                        write_empty(file_name)
        break

    except FileNotFoundError:
        print(f"Plik '{file_name}' nie istnieje.")
        os.system('cls')
    except IOError:
        print(f"Wystąpił błąd wejścia-wyjścia podczas pracy z plikiem '{file_name}'.")
        os.system('cls')
