n = input()
n = int(n)
for _ in range(n):
    user_name = input()
    len_name = len(user_name)
    name_chr_ord = [ord(x) for x in user_name]
    chr_num = num_num = 0
    flag = True
    for idx, chr_ord in enumerate(name_chr_ord):
        if ord("0") <= chr_ord <= ord("9"):
            num_num += 1
        elif ord("a") <= chr_ord <= ord("z"):
            chr_num += 1
        elif ord("A") <= chr_ord <= ord("Z"):
            chr_num += 1
        # rule 1
        if idx == 0 and chr_num == 0:
            print("Wrong")
            flag = False
            break
        # rule 2
        if chr_num + num_num != idx + 1:
            print("Wrong")
            flag = False
            break
    if flag == False:
        continue
    # rule 3
    if chr_num == 0 or num_num == 0:
        print("Wrong")
        continue
    print("Accept")
