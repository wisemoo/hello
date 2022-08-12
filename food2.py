import myfood

foodlist = ["짜장면", "짬뽕", "탕수육", "밀면", "돈까스"]

# 리스트중에 먹고 싶은 메뉴가 없으면
# 사용자가 입력을 한다(계속)
while True:
    addfood = input("추가 음식 입력 :")
    print(f"당신이 입력한 내용: {addfood}")
    if addfood == "그만":
        break
    foodlist.append(addfood)

# 위 리스트를 출력
myfood.print_list(foodlist)

myfood.print_rand_list(foodlist)