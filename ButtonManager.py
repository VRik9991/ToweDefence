def click_checker(buttons, get_mouse_x_and_y):
    for button in buttons:
        if button.hit_box[0][0] <= get_mouse_x_and_y[0] <= button.hit_box[0][1] and button.hit_box[1][0] <= get_mouse_x_and_y[1] <= button.hit_box[1][1]:
            button.click()