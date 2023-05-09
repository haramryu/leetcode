# ChatGPT 스터디 발표
### 주제 1. Certi. Pro. 공부를 ChatGPT로 해보자
#### 착안

서버 코드도 사람보다 잘 짠다는 소문이 있던데, 그럼 Algorithm 문제는 얼마나 잘 풀까?  
학습 데이터도 많아서 잘 풀겠지??

leetcode 고  

<kbd><img width="727" alt="image" src="https://github.com/haramryu/leetcode/assets/22101375/299fef91-411f-41d9-8bf1-6ad5c3108ddb"></kbd>


문제 복사해서 붙여넣고,  
C++로 풀어달라고 해보자  

<kbd><img width="754" alt="image" src="https://github.com/haramryu/leetcode/assets/22101375/c148dcb1-cfbb-4e9f-8752-b81b327588c0"></kbd>


복사해서 붙여넣으면?  
짠 Accept. 

<kbd><img width="1502" alt="image" src="https://github.com/haramryu/leetcode/assets/22101375/7addb845-f915-4af2-b45e-86d326e12cfc"></kbd>

통과 못하는 경우도 있다고 합니다.(by 규병님)  
제가 돌려본 건 다 통과 했음.

#### 실행
그럼 leetcode 복사해다가 붙여 넣는 과정을 자동화 하기 위해서 서버를 하나 띄워보자.  
그리고 서버도 ChatGPT한테 짜라고 하지 뭐.  

<kbd><img width="761" alt="image" src="https://github.com/haramryu/leetcode/assets/22101375/d9eb126f-92a6-4913-8a92-551b9d0b5a95"></kbd>

2시간만에 서버 뚝딱함  

#### 결과
http://27.96.135.223:8000

### 주제2. 도리를 지키면서 ChatGPT로 돈을 버는 가장 현실적인 방법(제 생각입니다.)
#### Hallucination
ChatGPT는 거짓말을 한다.  
없는 걸 있는 것처럼, 안되는 걸 되는 것처럼.  
ChatGPT도 하고 Bing AI도 하고 Bard도 하고 다 한다고 한다.  

#### AutoGPT 소개
- ChatGPT는 질문 하나하면 응답 한번 하고 끝
- 목표를 정해주면, 생각해서 계획하고 행동을 반복
- 장기 기억 할 내용을 DB에 저장하기도 함
- 할 수 있는 것
  - 웹사이트 하나 만들어 봐라 --> node js 다운 받고 코딩 해줌
  - 신발을 팔건데 시장 분석 해줘 --> 경쟁사 사이트 들어가서 장단점 분석 및 요약 리포트 txt파일로 작성
- 그러나 아직 장난감 수준이라고 함(by 코딩애플)
- 그런데 GitHub star가 이렇게 증가하고,
<kbd>![image](https://github.com/haramryu/leetcode/assets/22101375/8f8b2387-9eb0-4e10-afe3-f6407640cde9)</kbd>
- 도네이션으로 월 3만달러를 벌고 있다고 합니다.


#### AutoGPT 코드 분석...
- System
- Thoughts
- Reasoning
- Plan
- Criticism
- Next Action
