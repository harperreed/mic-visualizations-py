# 🎵 Audio Visualizations 🎨

Welcome to the **Audio Visualizations** repository! Here, you can explore a collection of engaging visual representations of audio data created using Python and Pygame. Each visualization dynamically responds to the frequency data from audio inputs, crafting a unique visual experience.

## 📜 Summary of Project

This project aims to seamlessly integrate sound and sight by crafting stunning graphics that react to audio signals. Leveraging **Fast Fourier Transform (FFT)** data, each script generates distinctive visual patterns that fluctuate according to the audio's frequencies and intensities. The repository includes a variety of visual styles, such as:

- Circular patterns
- Fractal trees
- Waveforms
- Spectrum representations
- And many more!

## ⚙️ How to Use

To get started with this project, follow the instructions below:

1. **Clone the repository**
   ```bash
   git clone https://github.com/harperreed/mic-visualizations-py.git
   cd mic-visualizations-py
   ```

2. **Install the required dependencies**
   You can install the necessary dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run a Visualization Script**
   Pick a visualization script from the `visualizations` folder. For example:
   ```bash
   python visualizations/circular.py
   ```

4. **Input Audio Data**
   Ensure that your audio input is correctly configured, as the visualizations bounce off audio feed data.

5. **Enjoy!** 🎉

## 💻 Tech Info

- **Programming Language:** Python
- **Graphics Library:** Pygame
- **Data Processing:** NumPy (for numerical and FFT manipulation)

### Visualizations Included:

- `circular.py`: Generates circular visuals based on frequency data.
- `circular_spectrum.py`: Displays the spectrum of audio data in a circular format.
- `fractal_tree.py`: Creates fractal trees that react to the audio intensity.
- `frequency_dots.py`: Displays random dots that change size and color based on audio frequencies.
- `particle_system.py`: Visualizes a vibrant particle system influenced by audio input.
- `rings.py`: Draws concentric circles in response to audio data.
- `ripple.py`: Creates visual ripple effects synchronized with audio playback.
- `spectrum.py`: Visualizes audio data as a bar graph.
- `spiral.py`: Generates an evolving spiral pattern that adjusts with audio changes.
- `star_field.py`: Simulates a field of stars, enhancing visuals based on audio inputs.

Explore each script and unleash your creativity! Should you have any questions or suggestions, please do not hesitate to open an issue or reach out. Happy coding! 🚀✨

## Running Tests

To run the tests locally, follow these steps:

1. Ensure you have all the required dependencies installed:
   ```
   pip install -r requirements.txt
   ```

2. Navigate to the project root directory.

3. Run the tests using the following command:
   ```
   python -m unittest discover tests
   ```

This will discover and run all the tests in the `tests/` directory.

If you want to run a specific test file, you can use:
```
python -m unittest tests/test_file_name.py
```

Replace `test_file_name.py` with the name of the test file you want to run.
