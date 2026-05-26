from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

plane_x = -9
plane_y = -2

speed = 0.03

def draw_runway():
    glColor3f(0.25, 0.25, 0.25)
    glBegin(GL_QUADS)
    glVertex2f(-10, -3)
    glVertex2f(10, -3)
    glVertex2f(10, -1)
    glVertex2f(-10, -1)
    glEnd()

    glColor3f(1, 1, 1)
    for i in range(-9, 10, 2):
        glBegin(GL_LINES)
        glVertex2f(i, -2)
        glVertex2f(i + 1, -2)
        glEnd()

def draw_plane(x, y):
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x + 2.5, y)
    glVertex2f(x + 3.2, y + 0.25)
    glVertex2f(x + 2.5, y + 0.5)
    glVertex2f(x, y + 0.5)
    glEnd()

    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + 1.2, y + 0.25)
    glVertex2f(x + 0.3, y - 0.7)
    glVertex2f(x + 2.2, y + 0.25)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + 0.3, y + 0.5)
    glVertex2f(x - 0.3, y + 1.0)
    glVertex2f(x + 0.8, y + 0.5)
    glEnd()


def special_keys(key, x, y):
    global speed
    if key == GLUT_KEY_RIGHT:
        speed += 0.01
    elif key == GLUT_KEY_LEFT:
        speed -= 0.01
        if speed < 0:
            speed = 0
    print("Speed:", round(speed, 2))


def display():
    global plane_x, plane_y, speed
    glClear(GL_COLOR_BUFFER_BIT)
    draw_runway()
    plane_x += speed
    if plane_x > -2:
        plane_y += speed / 4

    if plane_x > 12:
        plane_x = -9
        plane_y = -2
    draw_plane(plane_x, plane_y)
    glutSwapBuffers()

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def init():
    glClearColor(0.4, 0.7, 1.0, 1)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-10, 10, -5, 5)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(900, 600)
glutCreateWindow(b"Plane Takeoff Animation")
init()
glutDisplayFunc(display)
glutSpecialFunc(special_keys)
glutTimerFunc(0, timer, 0)
glutMainLoop()