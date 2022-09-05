# 성격 유형 룩업 테이블 : my_score[lookup.index("R")]는 나의 R 성격 점수
lookup = list("RTCFJMAN")


# (성격 유형, 선택지)에 따라 (점수를 반영할 성격 유형, 실제 반영 점수) 반환
def add_score(question, choice):
    first, second = question
    if 1 <= choice <= 4:
        return lookup.index(first), 4 - choice
    return lookup.index(second), choice - 4


def solution(survey, choices):
    my_score = [0] * 8
    answer = ''

    # 나의 성격 유형 리스트에 설문에 따른 점수 반영하기
    for question, choice in zip(survey, choices):
        item, score = add_score(question, choice)
        my_score[item] += score

    # 검사 결과 도출하기
    for i in range(0, 8, 2):
        one, theother = my_score[i], my_score[i + 1]
        if one < theother:
            answer += lookup[i + 1]
        else:
            answer += lookup[i]
    return answer