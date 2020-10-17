import pygame as p #파이게임생성

p.init()  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (900,400)    #가로,세로
sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("게임판")    #게임창제목 display:해상도설정
playing = True
#비행기생성
plane =p.image.load("비행기.png")
#배경
bg =p.image.load("별자리 배경.png")
bg_x=0
bg_y=0
bg1 = bg.copy()
bg1_x=900
bg1_y=0

while playing: #while True - 계속 반복하기

    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료

    sc.fill(white)  #배경화면색 설정
    
    sc.blit(bg,(bg_x,bg_y))

    sc.blit(bg1,(bg1_x,bg1_y))
    #배경이 움직이는코드,(속도)
    bg_x -= 2 #bg_x = bg_x - 1
    
    bg1_x -= 2
    #배경이 윈쪽벽에 닿게 되면
    if bg_x <= -900:
         bg_x = 900

    if bg1_x <= -900:
        bg1_x = 900
         
    
    sc.blit(plane,(0,150))
    p.display.flip()    #화면업데이트
