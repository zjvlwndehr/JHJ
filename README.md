![header](https://capsule-render.vercel.app/api?text=JHJ%20Script!&fontColor=FFE3EE&type=waving)

먼저 act페이지를 구성했는데요
구글스프레드시트 api를 이용해 구글스프레드 시트와 저희 서버와 연결했습니다
클라이언트로부터 post방식의 요청으로 선생님의 id, 학생의 id, unixtimestamp 파라미터를 받고 
구글 스프레드시트를 업데이트 했습니다.
그 다음 show 페이지를 구성했습니다.
show페이지에 POST방식으로 요청을 하면
선생님의  id를 확인하면, DB에서 요청된 id를 기반으로 사전형식으로 데이터를 반환합니다.