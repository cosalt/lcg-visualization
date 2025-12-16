# Linear Congruential Generator (LCG) Visualization

Ever wondered how random number generators actually work? This project visualizes one of the oldest and simplest methods: the Linear Congruential Generator.

## try it online!

**[Launch Web App](https://lcg-visualization.streamlit.app)**

Interactive web version with adjustable parameters - no installation needed!

## wat dis?

A Linear Congruential Generator is a classic algorithm for creating sequences of pseudo-random numbers. It's not truly random (nothing in computers really is), but it's fast and good enough for many applications. The formula is surprisingly simple:

**X<sub>n+1</sub> = (a × X<sub>n</sub> + c) mod m**

where:
- **m** is the modulus (the "box" size - 16 in this demo)
- **a** is the multiplier (5)
- **c** is the increment (3)
- **seed** is where we start (1)

this visualization uses small numbers so you can actually see what's happening. real-world implementations use much larger values.

## What You'll See

the animation shows two views side-by-side:

### left: The Math in Action (1D View)
Watch each step of the formula unfold:
1. **Blue** - Start with the current number
2. **Orange** - Multiply it by 5
3. **Green** - Add 3
4. **Purple** - Take modulo 16 (the "wrap around" that keeps numbers in range)

### right: The Pattern (2D View)
This plots each number against its successor. The red squares show the sequence pattern - this is similar to what's called a "spectral test" in random number generation. Good random generators should fill this space uniformly without obvious patterns.

## run how

### web version (recommended)
the easiest way is to use the interactive web app - see deployment instructions in [DEPLOYMENT.md](DEPLOYMENT.md).

### desktop version
Make sure you have the required libraries:

```bash
pip install matplotlib numpy
```

then run!!:

```bash
python "Linear Congruential Generator (LCG).py"
```

the animation will loop continuously, showing you how each number in the sequence is generated.

### streamlit web appp (local)
to run the interactive web version locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## mess around with it

want to see how different parameters affect the pattern? Try changing these values at the top of the file:

```python
m = 16   # modulus
a = 5    # multiplier
c = 3    # increment
seed = 1 # starting number
```

some combinations will give you better "random" patterns than others. that's the art and science of choosing good LCG parameters!

## why this matters and why i did it

LCGs are everywhere - from video games to Monte Carlo simulations. While modern cryptography uses more sophisticated methods, understanding LCGs gives you insight into:
- how computers generate randomness
- why some "random" sequences have patterns
- the basics of pseudo-random number generation

+ it's cool, to watch math in motion

## Technical Bits

- Built with Python 3
- Uses matplotlib for visualization and animation
- Animation runs at 1 second per step (4 steps per number)
- Automatically detects and handles cycle completion

---

Made with curiosity and matplotlib :P Feel free to experiment!
😛
