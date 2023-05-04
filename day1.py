# 문자열뒤집기
def solution(my_string):
    return my_string[::-1]

##################################################################################################################################

# 두수의나눗셈
import math
def solution(num1, num2):
    return math.floor((num1/num2)*1000)
#나머지를 //로했더니 정답이안나와서 floor를사용했다.
#    return (num1//num2)*1000
# 데이터는 [3,2] [7,3] [1,16] 정답은 1500, 2333 , 62 인데 결과값이 1000, 2000, 0 이나온다 

##################################################################################################################################

# 배열자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
# 이건 처음에 len()쓰고 list()쓰고 별걸다써서 잘랐다가 for문도사용했었다. 
# 무튼그렇게 잘랐는데 생각보다간단하게잘린문제

##################################################################################################################################

# 배열의 원소 길이
def solution(strlist):
    answer = []
    for str in strlist:
        answer.append(len(str))
    return answer
# 이건 map을공부하기전에 작성해서 map을 공부하고나서는 간단하게풀었다.이해를 했다는거에 의의를 둔? 그리고 응용했구나?라는뿌듯함
def solution(strlist):
    answer = list(map(len, strlist))
    return answer

##################################################################################################################################

# 숫자 비교하기
def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
#이부분도 한줄쓰기를 연습하고
def solution(num1, num2):
    return 1 if num1==num2 else -1
#수정함

##################################################################################################################################

# 배열 두배 만들기
def solution(numbers):
    max = []
    for multi in numbers:
        max.append(multi*2)
    return max
# 한줄쓰기연습후 수정
def solution(numbers):
    return [num*2 for num in numbers]