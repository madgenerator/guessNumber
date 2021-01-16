#1~20 사이의 숫자를 입력 받는다
#정답 숫자를 미리 만들어 둠 (random 함수 사용)
#입력이 정답보다 크면 "정답은 더 작습니다" 출력
#입력이 정답보다 작으면 "정답은 더 큽니다" 출력
#입력과 정답이 같으면 "정답입니다!!" 출력하고 프로그램 종료
#정답을 맞출때 까지 무한 반복
#5번 시도하고 못맞추면 종료

import random
answer = random.randint(1,20) #1~20 사이의 정수
print(answer)

trycount=0

while(True):
  tryNumber = int(input("정답을 맞춰보세요: "))

  if(tryNumber>answer):
    print("정답이 작습니다")
  elif(tryNumber<answer):
    print("정답이 큽니다")
  else:
    print('정답입니다!!')
    break

  trycount=trycount+1
  if(trycount>=5):
    print("기회를 모두 사용!! 땡!!")
    break
