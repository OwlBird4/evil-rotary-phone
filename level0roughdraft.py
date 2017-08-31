    Windows_10_desktop = Image("Windows-10-desktop.png",screenWidth,screenHeight,True);
    mario_standing = Image("mario_standing.png",150,150,True);
    mario_in_air = Image("mario_in_air.png",150,150,True);
    if level == 0 :
        # Intro Screen Code
        windows.display()
        mario_standing.display()
    
 
        pygame.display.update()
        #pygame.time.delay(100)
        PressEnterToContinue()
        level = 1
