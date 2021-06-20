"""A computer choices a random integer from 1 to 100.
An user have to give correct answer.
When the answer is a bigger than the integer, print "UP".
When the answer is a smaller than the interger, print "DOWN".
When the answer is the integer,
print "정답" and let the user knows counts which the user entered."""

import random

if __name__ == "__main__":

    print("컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다.")
    print("이 숫자를 맞춰주세요.")

    solution = random.randint(1, 100)

    PRED = 0
    COUNT = 0
    while solution != PRED:
        PRED = int(input("1~100 숫자 입력: "))
        COUNT += 1
        if PRED < solution:
            print("DOWN")
        elif PRED > solution:
            print("UP")

    print(f"정답입니다! {COUNT}회 만에 맞췄어요.")
