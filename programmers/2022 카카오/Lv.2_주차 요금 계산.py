from collections import defaultdict


def conver_minutes(enter_time, out_time):
    # print(enter_time, out_time)
    enter_time = int(enter_time[:2]) * 60 + int(enter_time[3:])
    out_time = int(out_time[:2]) * 60 + int(out_time[3:])
    return out_time - enter_time


def solution(fees, records):
    TIME, FEE, PER_TIME, PER_FEE = fees
    print(f'시간{TIME}, 요금:{FEE}, 단위시간: {PER_TIME}, 단위요금: {PER_FEE}')

    def calculate(enter_time, out_time="23:59"):
        nonlocal car_number
        fee = 0
        minutes = conver_minutes(enter_time, out_time)
        if minutes <= TIME:
            fee = FEE
        else:
            fee = int(FEE + ((minutes - TIME) // PER_TIME + bool(minutes % PER_TIME)) * PER_FEE)
        print(car_number, enter_time, out_time, '시간', minutes, '요금:', fee)
        return fee

    answer = [0] * 10000
    prefix_time = [0] * 10000
    parking = defaultdict(dict)  # {차량번호: { cnt: 주차장 사용 횟수, log: [[입차1, 출차1], [입차2, 출차2]]}}

    for record in records:
        time, car_number, state = record.split()
        car_number = int(car_number)
        print(parking[1], parking)
        # 입차 => last_enter_log에 저장
        if state == "IN":
            cnt = parking[car_number].setdefault("cnt", -1)
            cnt = parking[car_number].setdefault("log", [])
            parking[car_number]["cnt"] = cnt + 1
            parking[car_number]["log"].append([time, "23:59"])

        # 출차 => last_enter_log 조회 => 정산 => answer에 반영 => last_enter_log에서 해당 번호 삭제
        else:
            idx = parking[car_number]["cnt"]
            parking[car_number]["log"][idx][-1] = time
    print(parking)

    for car_number, enter_time in parking.items():
        answer[car_number] += calculate(enter_time)

    answer = list(map(lambda x: x + 1, list(filter(lambda x: True if -1 != x else False, answer))))

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))