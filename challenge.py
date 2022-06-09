# the problem
# given a score sheet represented by a list of ints between -100 nad +100
# write a function that return the score for the runner up. the 2nd highest score in the array, just RETURN the number
# 

# function recieves an array and gets a list 
# do not use sorting functions

from distutils.command.build_scripts import first_line_re


def find_second(scores : list):
  scores.sort()
  scores.reverse()
  # print('List start: ')
  first = scores[0]
  for num in scores:
    if num != first:
      return num
    # print(num, end="")
    # print(',', end="")
  # return scores[-2]
  
  
def solution2(scores: list):
  first -101
  second = -101
  for num in scores:
    if num > first:
      second = first
      first = num
    elif num > second and num != first:
      second = num
  return second


ls1 = [5,2,4,3,1]
ls2=[-2,-5,0,5,20]
ls3=[1,2,3,4,5,5]

# print(find_second(ls1))
# print(find_second(ls2))
# print(find_second(ls3))


# from logging import addLevelName
print(solution2(ls1))
print(solution2(ls2))
print(solution2(ls3))

# score_sheet=[1,5,25,26,19,89,90]


# max=max(score_sheet[0].score_sheet[1])
# snd_max = min (score_sheet[0].score_sheet[1])
# n = len(score_sheet)
# for i in range(2,n):
#   if score_sheet[i]>max:
#     snd_max=max
#     max=score_sheet[i]
#   elif score_sheet[i]>snd_max and max != score_sheet[i]:
#     max != score_sheet[i]
#     snd_max = score_sheet[i]

# print('the 2nd highestn is :')





