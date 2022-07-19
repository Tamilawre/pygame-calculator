import pygame
from sys import exit

pygame.init()
# set the calculator display size
screen = pygame.display.set_mode((450, 350))
pygame.display.set_caption("calculator")
# define the area of the white space
surface = pygame.Surface((450, 100))
cursor = pygame.Surface((3, 50))
cursor_surface = pygame.Surface((3, 50))
color = "black"
# this determines the color of the input area
white = (255, 255, 255)
background_color = (20, 20, 20)
surface.fill(white)
clock = pygame.time.Clock()
timer = 0
cursor_x = 5

# this part belongs to the buttons
buttons = []
x = 10
y = 110
n = 0


# this class takes in the coordinates,width,height and the text you want to display on the button


class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.border = 3
        self.button = pygame.Surface((self.width, self.height))
        self.button_hitbox = self.button.get_rect(topleft=(self.x + 3, self.y + 3))
        self.outline = pygame.Surface((self.width + self.border, self.height + self.border))
        self.value = 0
        self.button_color = (20, 20, 20)
        self.outline_color = (100, 100, 100)
        self.click_number = 0
        self.touched = False
        self.is_pressed = False
        self.activated = False
        self.deactivated = False

    def draw(self):
        text_font = pygame.font.Font(None, 50)
        text = text_font.render(str(self.text), True, self.outline_color)
        text_rect = text.get_rect(center=(self.x + self.width / 2 + 2, self.y + self.height / 2 + 2))
        self.button.fill(self.button_color)
        self.outline.fill(self.outline_color)
        screen.blit(self.outline, (self.x, self.y))
        screen.blit(self.button, self.button_hitbox)
        screen.blit(text, text_rect)

    def clicked(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_hitbox.collidepoint(event.pos):
                return True
            else:
                return False

# position the 0-9 key buttons


for i in range(10):
    if n == 5:
        y += 73
        x = 10
        n = 0
    button = Button(x, y, 60, 60, i)
    button.value = i
    buttons.append(button)
    x += 73
    n += 1
special_values = []
del_button = Button(375, 110, 60, 115, "del")
equal_button = Button(375, 237, 60, 95, "=")
plus_button = Button(10, 256, 60, 60, "+")
minus_button = Button(83, 256, 60, 60, "-")
divide_button = Button(156, 256, 60, 60, "/")
multiply_button = Button(229, 256, 60, 60, "*")
dot = Button(302, 256, 60, 60, ".")
index = 0
pressed = False
number = 0
number_x = 5
number_y = 10
# stores the list of all the buttons that have been pressed
history = []
history2 = ""
history3 = ""
value1 = 0
value2 = 0
value = ""
# the position where our result will be displayed on the screen
output_x = 10
output_y = 60
while True:
    mouse_pos = pygame.mouse.get_pos()
    clock.tick(60)
    timer += 1
    speed_of_blink = 5
    for i in range(len(history)):
        number_font = pygame.font.Font(None, 50)
        number_text = number_font.render(str(history3), True, "black")
        surface.blit(number_text, (number_x, number_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # change the button's color and return it's value if it is clicked
        for btn in buttons:
            if btn.clicked():
                print(btn.value)
                history.append(btn.value)
                history3 += str(btn.value)
                surface.fill("white")
                for i in range(len(history)):
                    number_font = pygame.font.Font(None, 50)
                    number_text = number_font.render(str(history3), True, "black")
                    surface.blit(number_text, (number_x, number_y))
                # surface.fill("white")
                # number_x -= 20
                cursor_x += 19
                btn.outline_color = (20, 20, 20)
                btn.button_color = (100, 100, 100)
                
            else:
                btn.outline_color = (100, 100, 100)
                btn.button_color = (20, 20, 20)
        del_button.value = "delete"
        # delete buttons blink
        if del_button.clicked():
            surface.fill("white")
            print(del_button.value)
            history3= history3[:-1]
            cursor_x -= 19

            history.pop()
            del_button.button_color = (100, 100, 100)
            del_button.outline_color = (20, 20, 20)
        else:
            del_button.button_color = (20, 20, 20)
            del_button.outline_color = (100, 100, 100)

        # equal buttons blink
        # print out the result of our arithmetic
        equal_button.value = "="
        if equal_button.clicked():
            print(equal_button.value)
            print(history)
            history3 = ""
            surface.fill("white")
            cursor_x = 5
            for item in history:
                history2 += str(item)
            # print(history2)
            for item in history2:
            # to perform arithmetic on input containing multiple operators we can set value1 to the result of the operation between value1 and value2 the we repeat the process forward
            # for item in history:
                if item == "+":
                    # we get the index then we slice upwards excluding the operator
                    value1 = history2[:history2.index("+")]
                    # print(value1)
                    value2 = history2[history2.index("+")+1:]
                    # print(value2)
                    result = int(value1)+int(value2)
                    print(result)
                    # print(history.index("+"))
                    # show the result of the calculation
                    output_font = pygame.font.Font(None, 50)
                    output = output_font.render(str(result), True, "black")
                    surface.blit(output, (output_x, output_y))
                    history =[]
                    history2 = ""
                if item == "-":
                    # we get the index then we slice upwards excluding the operator
                    value1 = history2[:history2.index("-")]
                    # print(value1)
                    value2 = history2[history2.index("-")+1:]
                    # print(value2)
                    result = int(value1)-int(value2)
                    print(result)
                    # show the result of the calculation
                    output_font = pygame.font.Font(None, 50)
                    output = output_font.render(str(result), True, "black")
                    surface.blit(output, (output_x, output_y))
                    # print(history.index("-"))
                    history = []
                    history2 =""
                if item == "*":
                    # we get the index then we slice upwards excluding the operator
                    value1 = history2[:history2.index("*")]
                    # print(value1)
                    value2 = history2[history2.index("*")+1:]
                    # print(value2)
                    result = int(value1)*int(value2)
                    print(result)
                    # show the result of the calculation
                    output_font = pygame.font.Font(None, 50)
                    output = output_font.render(str(result), True, "black")
                    surface.blit(output, (output_x, output_y))
                    # print(history.index("*"))
                    history = []
                    history2 = ""
                if item == "/":
                    # we get the index then we slice upwards excluding the operator
                    value1 = history2[:history2.index("/")]
                    # print(value1)
                    value2 = history2[history2.index("/")+1:]
                    # print(value2)
                    result = int(value1)/int(value2)
                    print(result)
                    # print(history.index("/"))
                    # show the result of the calculation
                    output_font = pygame.font.Font(None, 50)
                    output = output_font.render(str(result), True, "black")
                    surface.blit(output, (output_x, output_y))
                    history = []
                    history2 = ""
           
            equal_button.button_color = (100, 100, 100)
            equal_button.outline_color = (20, 20, 20)
        else:
            equal_button.button_color = (20, 20, 20)
            equal_button.outline_color = (100, 100, 100)

        plus_button.value = "+"
        if plus_button.clicked():
            print(plus_button.value)
            history3 += str(plus_button.value)
            history.append(plus_button.value)
            plus_button.button_color = (100, 100, 100)
            plus_button.outline_color = (20, 20, 20)
        else:
            plus_button.button_color = (20, 20, 20)
            plus_button.outline_color = (100, 100, 100)

        minus_button.value = "-"
        if minus_button.clicked():
            print(minus_button.value)
            history3 += str(minus_button.value)
            history.append(minus_button.value)
            minus_button.button_color = (100, 100, 100)
            minus_button.outline_color = (20, 20, 20)
        else:
            minus_button.button_color = (20, 20, 20)
            minus_button.outline_color = (100, 100, 100)

        divide_button.value = "/"
        if divide_button.clicked():
            print(divide_button.value)
            history3 += str(divide_button.value)
            history.append(divide_button.value)
            divide_button.button_color = (100, 100, 100)
            divide_button.outline_color = (20, 20, 20)
        else:
            divide_button.button_color = (20, 20, 20)
            divide_button.outline_color = (100, 100, 100)

        multiply_button.value = "*"
        if multiply_button.clicked():
            print(multiply_button.value)
            history3 += str(multiply_button.value)
            history.append(multiply_button.value)
            multiply_button.button_color = (100, 100, 100)
            multiply_button.outline_color = (20, 20, 20)
        else:
            multiply_button.button_color = (20, 20, 20)
            multiply_button.outline_color = (100, 100, 100)

        dot.value = "."
        if dot.clicked():
            print(dot.value)
            history3 += str(dot.value)
            dot.button_color = (100, 100, 100)
            dot.outline_color = (20, 20, 20)
        else:
            dot.button_color = (20, 20, 20)
            dot.outline_color = (100, 100, 100)
       
    if timer == 10:
        color = "white"
    if timer == 10 + speed_of_blink:
        color = "black"
        timer = 0
    cursor.fill(color)
    screen.fill(background_color)
    screen.blit(surface, (0, 0))
    # surface.blit(cursor, (cursor_x, 0))
    for butn in buttons:
        butn.draw()
   
    # cursor.fill("white")
   
    
    # important buttons
    del_button.draw()
    equal_button.draw()
    plus_button.draw()
    minus_button.draw()
    divide_button.draw()
    multiply_button.draw()
    dot.draw()
    pygame.display.update()
