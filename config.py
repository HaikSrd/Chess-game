import ctypes
user32 = ctypes.windll.user32
screen_size = user32.GetSystemMetrics(0) , user32.GetSystemMetrics(1)

x_border = (screen_size[0] - screen_size[1])/2
y_border = 0

white_color = (222,184,135)
dark_color = (139,69,19)
light_possible_next_color = (145, 120, 86)
dark_possible_next_color = (97, 49, 16)

