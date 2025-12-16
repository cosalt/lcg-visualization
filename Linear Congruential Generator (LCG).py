import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Linear Congruential Generator (LCG) Visualization
# we use small numbers to make the visual clear
m = 16   # modulus (The "Box" size)
a = 5    # multiplier
c = 3    # increment
seed = 1 # starting number

# generate the sequence first to know what to plot
sequence = []
x = seed
for _ in range(m + 1): # generate enough to show a cycle
    sequence.append(x)
    x = (a * x + c) % m

# 2 - visualization
fig, (ax_math, ax_viz) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle(f'Linear Congruential Generator: $X_{{n+1}} = ({a}X_n + {c}) //mod {m}$', fontsize=16)

# left plot: the equation/number line view
ax_math.set_title("Equation Steps (1D View)")
ax_math.set_xlim(0, m*a + c) # wide enough to show the multiplication before modulo
ax_math.set_ylim(-1, 1)
ax_math.get_yaxis().set_visible(False)
ax_math.axhline(0, color='gray', linestyle='--')

# right plot: the resulting sequence (2D view / spectral test style)
ax_viz.set_title("Resulting Sequence (2D View)")
ax_viz.set_xlim(0, m)
ax_viz.set_ylim(0, m)
ax_viz.set_xlabel("$X_n$")
ax_viz.set_ylabel("$X_{n+1}$")
ax_viz.grid(True, linestyle=':', alpha=0.6)

# visual elements
# math side
bar_current = ax_math.barh(0, 0, height=0.2, color='blue', label='Current Value')
text_step = ax_math.text(0, 0.5, '', fontsize=12)

# viz side
points, = ax_viz.plot([], [], 'rs', markersize=10, label='Generated Squares') # 'rs' = red squares
line, = ax_viz.plot([], [], 'k-', alpha=0.3) # connecting line

# data storage for animation
x_data, y_data = [], []

def init():
    x_data.clear()
    y_data.clear()
    bar_current[0].set_width(0)
    text_step.set_text('')
    points.set_data([], [])
    line.set_data([], [])
    return bar_current, text_step, points, line

def animate(i):
    # determine which number in the sequence we are processing
    idx = i // 4 # 4 animation steps per number generation
    step = i % 4
    
    if idx >= len(sequence) - 1:
        return bar_current, text_step, points, line

    current_val = sequence[idx]
    
    # step 0: show current X_n
    if step == 0:
        bar_current[0].set_width(current_val)
        bar_current[0].set_color('blue')
        text_step.set_text(f"Step 1: Start with $X_n = {current_val}$")
        
    # step 1: multiply (a * X_n)
    elif step == 1:
        val = current_val * a
        bar_current[0].set_width(val)
        bar_current[0].set_color('orange')
        text_step.set_text(f"Step 2: Multiply by {a}\n$({a} \\times {current_val}) = {val}$")

    # step 2: add increment (+ c)
    elif step == 2:
        val = (current_val * a) + c
        bar_current[0].set_width(val)
        bar_current[0].set_color('green')
        text_step.set_text(f"Step 3: Add {c}\n${current_val*a} + {c} = {val}$")

    # step 3: modulo ( % m ) -> the "wrap around"
    elif step == 3:
        val_before = (current_val * a) + c
        next_val = val_before % m
        
        # update math bar to show the "cut"
        bar_current[0].set_width(next_val)
        bar_current[0].set_color('purple')
        text_step.set_text(f"Step 4: Modulo {m}\n${val_before} \\mod {m} = {next_val}$")
        
        # update the 2D plot (the "square" visual)
        x_data.append(current_val)
        y_data.append(next_val)
        points.set_data(x_data, y_data)
        line.set_data(x_data, y_data)

    return bar_current, text_step, points, line

# create animation
# frames = (numbers to generate) * (4 steps per number)
ani = animation.FuncAnimation(fig, animate, frames=(len(sequence)-1)*4, init_func=init, blit=False, interval=1000, repeat=True)

plt.show()