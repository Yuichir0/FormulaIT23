def find_common_participants(first_group, second_group, delimeter=","):
    common_participants = list(set(first_group.split(delimeter)).intersection(set(second_group.split(delimeter))))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)
