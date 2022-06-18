# -*- coding: UTF-8 --
import keyboard as kb
import random as r
import sys

nums = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
"""numbers in the game"""
score = 0
"""score"""
Game2048BSFile = "./Game2048BestScore.txt"
"""location of Game2048BestScore.txt"""
with open(Game2048BSFile, "w", encoding="UTF-8") as BSw:
    pass
with open(Game2048BSFile, "r", encoding="UTF-8") as BSr:
    if BSr.read() == "":
        with open(Game2048BSFile, "w", encoding="UTF-8") as BSw:
            BSw.write("0")


def new_num():
    """
    add a number
    """
    while True:
        rand_list = r.randint(0, 3)
        """list that the number belongs to"""
        rand_index = r.randint(0, 3)
        """position of the number"""
        if nums[rand_list][rand_index] == 0:
            rand_num = r.randint(0, 9)
            """number that decides to create 4 or 2"""
            if rand_num == 0:
                nums[rand_list][rand_index] = 4
            else:
                nums[rand_list][rand_index] = 2
            break


def left():
    """
    move left
    """
    global score, nums
    for i in range(4):
        # move zeros
        for j in range(nums[i].count(0)):
            nums[i].remove(0)
            nums[i].append(0)
        # get two numbers into one
        for j in range(3):
            if nums[i][j] == nums[i][j + 1]:
                nums[i][j] *= 2
                score += nums[i][j]
                nums[i].pop(j + 1)
                nums[i].append(0)


def reverse():
    """
    reverse nums
    """
    global nums
    nums = [
        [nums[0][3], nums[0][2], nums[0][1], nums[0][0]],
        [nums[1][3], nums[1][2], nums[1][1], nums[1][0]],
        [nums[2][3], nums[2][2], nums[2][1], nums[2][0]],
        [nums[3][3], nums[3][2], nums[3][1], nums[3][0]]
    ]


def slash_reverse():
    """
    reverse nums by \\slash\\ direction
    """
    global nums
    nums = [
        [nums[0][0], nums[1][0], nums[2][0], nums[3][0]],
        [nums[0][1], nums[1][1], nums[2][1], nums[3][1]],
        [nums[0][2], nums[1][2], nums[2][2], nums[3][2]],
        [nums[0][3], nums[1][3], nums[2][3], nums[3][3]]
    ]


def pr_r():
    """
    print result
    """
    global nums, score
    print("\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------\n\n        ", end="")
    for i in nums:
        for j in i:
            if j == 0:
                print(".\t", end="")
            else:
                print(f"{j}\t", end="")
        print("\n\n\n        ", end="")
    print(f"score: {score}\n\n\n        ", end="")
    with open(Game2048BSFile, "r", encoding="UTF-8") as BSr:
        BSr.seek(0)
        best_score = int(BSr.read())
    if score > best_score:
        with open(Game2048BSFile, "w", encoding="UTF-8") as BSw:
            BSw.write(str(score))
        best_score = score
    print(f"best: {best_score}\n\n------------------------------------------------------------\n")


def move(key):
    """
    move
    :param key: callback of pressed key
    """
    nums1 = nums
    """a list to know if player really moved"""
    fail = True
    """failed?"""
    if "left down" in str(key) or "a down" in str(key):
        reverse()
        reverse()
        left()
    elif "right down" in str(key) or "d down" in str(key):
        reverse()
        left()
        reverse()
    elif "up down" in str(key) or "w down" in str(key):
        slash_reverse()
        left()
        slash_reverse()
    elif "down down" in str(key) or "s down" in str(key):
        slash_reverse()
        reverse()
        left()
        reverse()
        slash_reverse()
    else:
        pass
    if nums1 != nums:
        # failed?
        for i in nums:
            for j in i:
                fail = fail and j != 0
        if fail:
            print("Game over")
            sys.exit()
        new_num()
        pr_r()


# create numbers at the beginning of game
while sum(nums[0]) + sum(nums[1]) + sum(nums[2]) + sum(nums[3]) < 6:
    new_num()
pr_r()
kb.on_press(move)
kb.wait()
