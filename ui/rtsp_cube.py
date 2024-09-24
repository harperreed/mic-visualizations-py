import pygame
from pygame.math import Vector3
import cv2
import numpy as np

class RTSPCube:
    def __init__(self, width, height, rtsp_urls, speed):
        self.width = width
        self.height = height
        self.cube_size = min(width, height) // 4
        self.rotation = [0, 0, 0]
        
        # Set initial position to bottom right
        self.position = Vector3(width - self.cube_size, height - self.cube_size, 0)
        
        # Set speed as a 2D vector
        self.speed = Vector3(-abs(speed[0]), -abs(speed[1]), 0)  # Negative to move up-left initially

        # Initialize RTSP streams
        self.streams = []
        self.textures = []
        for url in rtsp_urls:
            stream = cv2.VideoCapture(url)
            if stream.isOpened():
                self.streams.append(stream)
                ret, frame = stream.read()
                if ret:
                    self.textures.append(pygame.image.frombuffer(
                        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).tobytes(), 
                        frame.shape[1::-1], "RGB"))
                else:
                    self.textures.append(None)
            else:
                print(f"Failed to open RTSP stream: {url}")

        # Fallback colors for sides without streams
        self.colors = [
            (255, 0, 0),    # Red
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (255, 255, 0),  # Yellow
            (255, 0, 255),  # Magenta
            (0, 255, 255),  # Cyan
        ]

    def update(self, fft_data):
        # Update rotation based on audio data
        if len(fft_data) > 0:
            self.rotation[0] += max(fft_data) * 5
            self.rotation[1] += max(fft_data) * 3
            self.rotation[2] += max(fft_data) * 2

        # Update position (bouncing effect)
        self.position += self.speed
        
        # Check boundaries and reverse direction if needed
        if self.position.x <= 0 or self.position.x >= self.width - self.cube_size * 2:
            self.speed.x *= -1
        if self.position.y <= 0 or self.position.y >= self.height - self.cube_size * 2:
            self.speed.y *= -1

        # Update RTSP frames
        for i, stream in enumerate(self.streams):
            ret, frame = stream.read()
            if ret:
                self.textures[i] = pygame.image.frombuffer(
                    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).tobytes(), 
                    frame.shape[1::-1], "RGB")

    def draw(self, screen):
        cube_surface = pygame.Surface((self.cube_size * 2, self.cube_size * 2), pygame.SRCALPHA)
        cube_surface.fill((0, 0, 0, 0))

        # Define cube vertices
        vertices = [
            (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
        ]

        # Define cube faces
        faces = [
            (0, 1, 2, 3), (1, 5, 6, 2), (5, 4, 7, 6),
            (4, 0, 3, 7), (3, 2, 6, 7), (4, 5, 1, 0)
        ]

        # Rotate vertices
        rotated = []
        for x, y, z in vertices:
            # Rotate around x-axis
            y = y * np.cos(np.radians(self.rotation[0])) - z * np.sin(np.radians(self.rotation[0]))
            z = y * np.sin(np.radians(self.rotation[0])) + z * np.cos(np.radians(self.rotation[0]))
            # Rotate around y-axis
            x = x * np.cos(np.radians(self.rotation[1])) + z * np.sin(np.radians(self.rotation[1]))
            z = -x * np.sin(np.radians(self.rotation[1])) + z * np.cos(np.radians(self.rotation[1]))
            # Rotate around z-axis
            x = x * np.cos(np.radians(self.rotation[2])) - y * np.sin(np.radians(self.rotation[2]))
            y = x * np.sin(np.radians(self.rotation[2])) + y * np.cos(np.radians(self.rotation[2]))
            rotated.append((x, y, z))

        # Sort faces by z-order (painter's algorithm)
        face_list = []
        for i, face in enumerate(faces):
            z = sum(rotated[v][2] for v in face)
            face_list.append((z, i))
        face_list.sort(reverse=True)

        # Draw faces
        for _, i in face_list:
            points = [((rotated[v][0] * self.cube_size + self.cube_size), 
                       (rotated[v][1] * self.cube_size + self.cube_size)) for v in faces[i]]
            
            if i < len(self.textures) and self.textures[i]:
                # Draw textured face
                scaled_texture = pygame.transform.scale(self.textures[i], (self.cube_size * 2, self.cube_size * 2))
                pygame.draw.polygon(cube_surface, (255, 255, 255), points)
                cube_surface.blit(scaled_texture, (0, 0), special_flags=pygame.BLEND_MULT)
            else:
                # Draw colored face
                pygame.draw.polygon(cube_surface, self.colors[i], points)

        # Blit cube onto main screen
        screen.blit(cube_surface, (self.position.x - self.cube_size, self.position.y - self.cube_size))

    def cleanup(self):
        for stream in self.streams:
            stream.release()