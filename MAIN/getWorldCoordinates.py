def getRealWorld(x_pixel, y_pixel):
    # TESTING EQUATION
    #x = 0.4471x - 423.25
    #y = 5.4878 + 355

    # RIT CALIBRATION EQUATION


    XGRADIENT = 0.447
    XINTERCEPT = -417.64




    YGRADIENT = -0.452
    YINTERCEPT = 842.05

    # x_pixel = int(input("please enter the x coordinates in pixels"))
    # y_pixel = int(input("please enter the y coordinates in pixels"))
    

    x_world = x_pixel * XGRADIENT + XINTERCEPT
    y_world = y_pixel * YGRADIENT + YINTERCEPT
    # print(f"x-coordinates: {x_world} y-coordinates: {y_world}")
    return x_world, y_world

# while (True):
#     getRealWorld



