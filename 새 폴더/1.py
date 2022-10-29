# def isExist(id, registered_list):
#     if id in registered_list:
#         return True
#     return False
#
#
# def recommand_N(N):
#     if not N:
#         N = '0'
#     n = int(N) + 1
#     return str(n)
#
#
# def solution(registered_list, new_id):
#     answer = ''
#
#     while isExist(new_id, registered_list):
#         print(new_id)
#         for i in range(len(new_id)):
#             if new_id[i].isdecimal():
#                 S = new_id[:i]
#                 N = recommand_N(new_id[i:])
#                 new_id = S + N
#                 # print('while', new_id)
#                 break
#         else:
#             new_id = new_id + recommand_N('')
#     answer = new_id
#     return answer
#

def isExist(id, registered_list):
    if id in registered_list:
        return True
    return False


def recommand_N(N):
    if not N:
        N = '0'
    return int(N) + 1


def split_number(id):
    S = id
    N = ''
    start = 0
    for i in range(len(id)):
        if id[i].isdecimal():
            S = new_id[:i]
            N = new_id[i:]
            start = i
            break
    return S, N



def solution(registered_list, new_id):
    answer = ''

    S = new_id
    N = ''
    start = len(new_id)

    for i in range(len(new_id)):
        if new_id[i].isdecimal():
            S = new_id[:i]
            N = new_id[i:]
            start = i
            break

    def remain_number(id):
        number = id[start:]
        if not number:
            number = '0'
        return int(number)

    used_numbers = []
    for id in list(filter(lambda x: True if S in x else False, registered_list)):
        used_numbers.append(remain_number(id))

    print(S, N, start, used_numbers)

    N = 0 if not N else int(N)

    while isExist(N, used_numbers):
        N = recommand_N(N)

    if N == 0:
        N = ''

    answer = S + str(N)

    # registered_list = list(map(remain_number(), (filter(lambda x: True if S in x else False, registered_list))))
    # print(registered_list)
    # registered_list = list(map(remain_number, (filter(lambda x: True if S in x else False, registered_list))))
    # while isExist(new_id, registered_list):
    #     for i in range(len(new_id)):
    #         if new_id[i].isdecimal():
    #             S = new_id[:i]
    #             N = recommand_N(new_id[i:])
    #             new_id = S + N
    #             break
    #     else:
    #         new_id = new_id + recommand_N('')

    return answer



#
registered_list = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
new_id = "cow"
print('ansswer', solution(registered_list, new_id))
# registered_list = ["apple1", "orange", "banana3"]
# new_id =  "apple"
# print('ansswer', solution(registered_list, new_id))
# ["apple1", "orange", "banana3"],

#
# def isExist(id, registered_list):
#     if id in registered_list:
#         return True
#     return False
#
#
# def recommand_N(N):
#     if not N:
#         N = '0'
#     n = int(N) + 1
#     return str(n)
#
#
# def split_number(id):
#     S = id
#     N = ''
#     for i in range(len(id)):
#         if id[i].isdecimal():
#             S = new_id[:i]
#             N = new_id[i:]
#             break
#     return S, N
#
#
# def remain_number(id):
#     S, N = split_number(id)
#     if not N:
#         N = '0'
#     return int(N)
#
#
# def solution(registered_list, new_id):
#     answer = ''
#
#     # S, N = split_number(new_id)
#
#     # registered_list = list(map(remain_number, (filter(lambda x, True if S in x else False, registered_list))))
#     # print(registered_list)
#     # while isExist(new_id, registered_list):
#     #     for i in range(len(new_id)):
#     #         if new_id[i].isdecimal():
#     #             S = new_id[:i]
#     #             N = recommand_N(new_id[i:])
#     #             new_id = S + N
#     #             break
#     #     else:
#     #         new_id = new_id + recommand_N('')
#
#     answer = new_id
#     return answer