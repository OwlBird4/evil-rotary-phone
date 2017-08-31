while gameOver == False :
    pygame.display.update()


    if level == 0 :
        # Intro Screen Code
        windows.display()
        marioair.display()
    
 
        pygame.display.update()
        #pygame.time.delay(100)
        PressEnterToContinue()
        level = 1
