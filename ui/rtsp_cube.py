import pygame
from pygame.math import Vector3
import cv2
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

class RTSPCube:
    def __init__(self, width, height, rtsp_urls):
        self.width = width
        self.height = height
        self.rtsp_urls = rtsp_urls
        self.cube_size = min(width, height) // 4
        self.rotation = [0, 0, 0]
        self.position = Vector3(width // 2, height // 2, 0)
        self.speed = Vector3(2, 2, 0)

        # Initialize OpenGL
        pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (width / height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        # Initialize RTSP streams
        self.streams = [cv2.VideoCapture(url) for url in rtsp_urls]
        self.textures = [glGenTextures(1) for _ in rtsp_urls]

    def update(self, fft_data):
        # Update rotation based on audio data
        if len(fft_data) > 0:
            self.rotation[0] += max(fft_data) * 5
            self.rotation[1] += max(fft_data) * 3
            self.rotation[2] += max(fft_data) * 2

        # Update position (bouncing effect)
        self.position += self.speed
        if self.position.x <= self.cube_size or self.position.x >= self.width - self.cube_size:
            self.speed.x *= -1
        if self.position.y <= self.cube_size or self.position.y >= self.height - self.cube_size:
            self.speed.y *= -1

    def draw(self, screen):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        # Apply rotation and position
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)
        glTranslatef(self.position.x - self.width // 2, self.position.y - self.height // 2, 0)

        # Draw cube with RTSP streams as textures
        for i, stream in enumerate(self.streams):
            ret, frame = stream.read()
            if ret:
                # Convert frame to OpenGL texture
                frame = cv2.flip(frame, 0)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                glBindTexture(GL_TEXTURE_2D, self.textures[i])
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, frame.shape[1], frame.shape[0], 0, GL_RGB, GL_UNSIGNED_BYTE, frame)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

                # Draw cube face
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, self.textures[i])
                glBegin(GL_QUADS)
                glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
                glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)
                glEnd()
                glDisable(GL_TEXTURE_2D)

            glRotatef(90, 0, 1, 0)  # Rotate to next face

        pygame.display.flip()

    def cleanup(self):
        for stream in self.streams:
            stream.release()
