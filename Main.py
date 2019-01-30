from Config import *

while True:
    goal = font.Font(None, 30).render('score:%d' % go, True, Color(255, 255, 255))
    goal_x,goal_y = goal.get_size()
    life = font.Font(None,30).render('life:%d'%li,True,Color(255,255,255))
    invin = font.Font(None,30).render('invincible:%d'%noene,True,Color(255,255,255))
    surface.fill(Color(0, 0, 0))
#--------------------Run--------------------------
    if cho == 0:
        if times == 0:
            if Bgm_Exist:
                main_music.play(-1)
            times += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    move += 20
                if event.key == K_ESCAPE:
                    bo1_music.play()
                    cho = 2
                    continue
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    move = 0
        po[1] -= move
        a -= 1
        if a < 0:
            Wall[b].re = True #Enable Wall
            a = 15
            b = (b+1)%4
            c -= 1
            if noene > 0:
                noene -= 1
        for i in Wall:
            i.move()
            Help.move()
            if i.po_start1[0] < 0: #Init Wall
                i.re = False
                i.restar()
            draw.line(surface,Color(255,255,255),i.po_start1,i.po_end1,20)
            draw.line(surface, Color(255,255,255), i.po_start2, i.po_end2, 20)

            if po[0] == i.po_end1[0]: #Get Score
                go += 1

            if noene == 0:
                if po[0] in range(i.po_end1[0]-20,i.po_end1[0]+20) and po[1] > i.po_end1[1]:
                    li -= 1
                    noene = 5
                    hit_music.play()
                elif po[0] in range(i.po_end2[0]-20,i.po_end2[0]+20) and po[1] < i.po_end2[1]:
                    li -= 1
                    noene = 5
                    hit_music.play()

        if c < 0:
            Help.re = True #Create a Help
            c = 15
        if po[0] in range(Help.po[0]-20,Help.po[0]+20) and po[1] in range(Help.po[1]-20,Help.po[1]+20): #Get a Help
            get_music.play()
            if Help.ty == 0:
                li += 1
            elif Help.ty == 1:
                noene += 20
            Help.restar()
        draw.rect(surface,Help.co,Rect(Help.po[0],Help.po[1],10,10))
        
        draw.rect(surface,Color(255,255,255),Rect(po[0],po[1],10,10))

        po[1] += 5
        if po[1] >= 400 or po[1] < -10 or li <= 0: #Die
            cho = 1
            times = 0
            continue
        surface.blit(goal,(0,0))
        surface.blit(life,(0,20))
        surface.blit(invin,(0,40))
#-------------------------Begin--------------------------------
    elif cho == 3:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bo2_music.play()
                    move = 0
                    a = 15
                    cho = 0
        a -= 1
        star_y += move
        if a < 0:
            a = 15
            move = -move
        surface.blit(title,((600-title_x)/2,(400-title_y)/2-50))
        surface.blit(tip,((600-tip_x)/2,(400-title_y)/2+80))
        draw.rect(surface,Color(255,255,255),Rect(290,star_y,20,20))
#---------------------Die-------------------------------------
    elif cho == 1:
        if Bgm_Exist:
            main_music.stop()
        if times == 0:
            end_music.play()
            times += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()
        surface.blit(text,((600-text_x)/2,(400-text_y)/2-20))
        surface.blit(goal,((600-goal_x)/2,(400-goal_y)/2))
#---------------------Pause-----------------------------------
    elif cho == 2:
        if Bgm_Exist:
            main_music.pause()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if Bgm_Exist:
                        main_music.unpause()
                    bo2_music.play()
                    cho = 0
        surface.blit(goal,((600-goal_x)/2,(400-goal_y)/2))

    fps.tick(15+go//20)
    display.update()
