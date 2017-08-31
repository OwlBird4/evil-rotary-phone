while gameOver == False :
    pygame.display.update()


    if level == 0 :
        # Intro Screen Code
        windows.display()
    
 
        pygame.display.update()
        #pygame.time.delay(100)
        PressEnterToContinue()
        level = 1
