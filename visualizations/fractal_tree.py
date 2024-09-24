import pygame
import math

def draw_branch(screen, start, end, depth, thickness, color):
    pygame.draw.line(screen, color, start, end, thickness)
    if depth > 0:
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)
        
        new_length = length * 0.7
        left_angle = angle + math.pi / 4
        right_angle = angle - math.pi / 4
        
        left_end = (end[0] + new_length * math.cos(left_angle),
                    end[1] + new_length * math.sin(left_angle))
        right_end = (end[0] + new_length * math.cos(right_angle),
                     end[1] + new_length * math.sin(right_angle))
        
        draw_branch(screen, end, left_end, depth-1, thickness-1, color)
        draw_branch(screen, end, right_end, depth-1, thickness-1, color)

def draw(screen, fft_data, width, height):
    screen.fill((0, 0, 0))
    
    # Use FFT data to determine tree parameters
    avg_intensity = sum(fft_data) / len(fft_data)
    max_depth = int(5 + avg_intensity * 5)
    start_length = height * 0.4 * (1 + avg_intensity)
    
    start = (width // 2, height)
    end = (width // 2, height - start_length)
    
    # Use different frequency bands for RGB color components
    r = int(255 * sum(fft_data[:len(fft_data)//3]) / (len(fft_data)//3))
    g = int(255 * sum(fft_data[len(fft_data)//3:2*len(fft_data)//3]) / (len(fft_data)//3))
    b = int(255 * sum(fft_data[2*len(fft_data)//3:]) / (len(fft_data)//3))
    color = (r, g, b)
    
    draw_branch(screen, start, end, max_depth, 10, color)