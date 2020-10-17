import pygame as p #파이게임생성
import random as r

p.init()  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (900,400)    #가로,세로
sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("게임판")    #게임창제목 display:해상도설정
playing = True


#비행기생성
plane =p.image.load("비행기.png")
p_rect = plane.get_rect(left = 0 , top = 100)
p_y = 0


#배경
bg =p.image.load("별자리 배경.png")
bg_x=0
bg_y=0
bg1 = bg.copy()
bg1_x=900
bg1_y=0

#적군
en = p.image.load("벽돌2.png")
e_rect = en.get_rect(left = 850 , top = 100)

an = p.image.load("쿵쿵이.png")
a_rect = en.get_rect(left = 850 , top = 300)

move = False
move2 = True





while playing: #while True - 계속 반복하기

    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료
            quit()  #shell 창 종료
            
        if event.type == p.KEYDOWN: #키보드를 눌렀을때
            if event.key == p.K_UP:
                p_y = -7
            if event.key == p.K_DOWN:
                p_y = 7
                
                
        if event.type == p.KEYUP: #키보드를 떼었을때
            if event.key == p.K_UP:
                p_y = 0
            if event.key == p.K_DOWN:
                p_y = 0

              
    p_rect.top += p_y # p_rect.top = p_rect.top + p_y
            
    sc.fill(white)  #배경화면색 설정
    sc.blit(bg,(bg_x,bg_y))
    sc.blit(bg1,(bg1_x,bg1_y))
    #배경이 움직이는코드,(속도)
    
    bg_x -= 5 #bg_x = bg_x - 1
    
    bg1_x -= 5
    #배경이 윈쪽벽에 닿게 되면
    if bg_x <= -900:
         bg_x = 900

    if bg1_x <= -900:
        bg1_x = 900
         
    
    sc.blit(plane,p_rect)
    #위쪽아래쪽막는코드
    if p_rect.top <= 0: #위쪽벽에닿으면
        p_rect.top = 0
    if p_rect.top >= 300: #위쪽벽에닿으면
        p_rect.top = 300



    sc.blit(en,e_rect)
    #적군움직이기
    e_rect.left -= 5   #e_rect.left = e_rect.left - 10
    if e_rect.left <= 0:    #적이 윈쪽벽에 닿으면
        e_rect.left = 850
        e_rect.top = r.randint(0,350)

    sc.blit(an,a_rect)
    #적군움직이기
    if move2: 
        a_rect.left -= 20   #a_rect.left = a_rect.left - 10
    if move: 
        a_rect.left += 3   #a_rect.left = a_rect.left - 10

    if a_rect.left <= 0:    #적이 윈쪽벽에 닿으면
        move2 = False
        move = True
    if a_rect.left >= 900:    #적이 오른쪽벽에 닿으면     
        move2 = True
        move = False
        a_rect.top = r.randint(0,350)
        
    
    if p_rect.colliderect(e_rect):
        playing = False
    if p_rect.colliderect(a_rect):
        playing = False
        

    p.display.flip()    #화면업데이트
