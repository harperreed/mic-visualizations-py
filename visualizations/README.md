# 🎨 Audio Visualizations 🎶

Welcome to the **Audio Visualizations** repository! Here, you will find an exciting collection of Python scripts that generate captivating visual representations of audio data using the Pygame library. Each visualization is designed to respond dynamically to the audio's frequency domain data (FFT), creating an immersive experience for viewers.

## 📜 Summary of Project

This project aims to bridge sound and sight by creating stunning graphics based on audio signals. By utilizing **Fast Fourier Transform (FFT)** data, each script generates unique visual patterns that fluctuate with the audio's frequencies and amplitudes. Whether you're looking for mesmerizing circular designs, fractal trees, or star fields, this repository has something for everyone!

### Features:
- Interactive visualizations responding to audio input
- Multiple visualization styles, including:
  - Circular patterns
  - Fractal trees
  - Particle systems
  - Ripple effects
  - Spectrum bars
  - Spiral graphics
  - Star fields
- Built using Python and Pygame

## ⚙️ How to Use

To run this project, you'll need to have Python installed on your system along with the Pygame library. Follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/harperreed/audio-visualizations.git
   cd audio-visualizations
   ```

2. **Install Dependencies:**
   Make sure you have Pygame installed. If not, you can install it via pip:
   ```bash
   pip install pygame numpy
   ```
   
3. **Run a Visualization Script:**
   Choose any of the visualization scripts in the `visualizations` directory and execute it. For example:
   ```bash
   python visualizations/circular.py
   ```

4. **Input Audio:**
   Make sure to configure the audio input source correctly, as the visualizations are designed to react to audio data.

5. **Enjoy!** 🎉

## 💻 Tech Info

- **Language:** Python
- **Library:** Pygame for graphics
- **Data Handling:** Numpy (for FFT data manipulation)
- **Visualizations Included:** 

  - `circular.py`: Draws lines radiating from the center based on frequency data.
  - `circular_spectrum.py`: Creates a circular spectrum effect.
  - `fractal_tree.py`: Generates a fractal tree representation, changing with audio intensity.
  - `frequency_dots.py`: Displays random dots that vary in size and color based on frequency data.
  - `particle_system.py`: Visualizes particles influenced by audio intensity.
  - `rings.py`: Draws concentric rings that react to frequency bands.
  - `ripple.py`: Creates ripple effects on the screen based on audio input.
  - `spectrum.py`: Bar graph style visualization of the audio spectrum.
  - `spiral.py`: Displays an evolving spiral pattern.
  - `star_field.py`: Simulates a star field, with stars moving toward the viewer based on audio data.
  
---

Feel free to explore each script and modify them as per your creativity! If you have any questions or suggestions, please open an issue or reach out. Happy coding! 🖥️✨
