from PyQt6.QtWidgets import QApplication, QMessageBox
import sys

try:
    from OpenGL import GL
except ImportError:
    app = QApplication(sys.argv)
    QMessageBox.critical(None, "OpenGL check",
            "PyOpenGL must be installed to run this example.")
    sys.exit(1)

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class MainWindow(QtWidgets.QOpenGLWidget):
    vertex = [
        [ 0.0, 0.0, 0.0 ],
        [ 1.0, 0.0, 0.0 ],
        [ 1.0, 1.0, 0.0 ],
        [ 0.0, 1.0, 0.0 ],
        [ 0.0, 0.0, 1.0 ],
        [ 1.0, 0.0, 1.0 ],
        [ 1.0, 1.0, 1.0 ],
        [ 0.0, 1.0, 1.0 ]]

    edge = [
        [ 0, 1 ],
        [ 1, 2 ],
        [ 2, 3 ],
        [ 3, 0 ],
        [ 4, 5 ],
        [ 5, 6 ],
        [ 6, 7 ],
        [ 7, 4 ],
        [ 0, 4 ],
        [ 1, 5 ],
        [ 2, 6 ],
        [ 3, 7 ]]

    
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(300, 300)

    def paintGL(self):
        print("Inside paintGL()")
        glClearColor(0.0, 0.0, 1.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(3.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glBegin(GL_LINES)

        for i in range(0, 12):
            glVertex(self.vertex[self.edge[i][0]])
            glVertex(self.vertex[self.edge[i][1]])
        glEnd()

        glFlush()        

    def resizeGL(self, w, h):
        print("Inside resizeGL()")
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(30.0, w/h, 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def initializeGL(self):
        print("Inside initializeGL()")
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glClearColor(0.0, 0.0, 0.0, 1.0)        

        glClearDepth(1.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 1.0, 1.0, 30.0)

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow(None)    
    w.show()
    sys.exit(qApp.exec())
