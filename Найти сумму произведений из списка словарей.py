import json

INPUT_FILENAME = 'input.json'


def task(filename) -> float:
    answer = 0
    with open(filename) as file:
        for line in json.load(file):
            answer += line["score"] * line["weight"]
    return answer


print(f"{task(INPUT_FILENAME):.3f}")
