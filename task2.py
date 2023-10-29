def find_common_participants(s1, s2, sep=","):
    list_ = list(set(s1.split(sep=sep)).intersection(s2.split(sep=sep)))
    list_.sort()
    return list_


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))