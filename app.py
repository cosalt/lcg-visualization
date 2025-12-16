import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="LCG Visualization", page_icon="🔢", layout="wide")

# Title and explanation
st.title("🔢 Linear Congruential Generator Visualization")

st.markdown("""
### What is an LCG?

A **Linear Congruential Generator** is one of the oldest and simplest pseudo-random number generators. 
It produces a sequence of numbers using a simple mathematical formula:

$$X_{n+1} = (a \\times X_n + c) \\mod m$$

Where:
- **m** = modulus (defines the range, 0 to m-1)
- **a** = multiplier
- **c** = increment  
- **seed** = starting value ($X_0$)

Despite its simplicity, LCGs are used in many applications including simulations, games, and statistical sampling. 
The quality of randomness depends heavily on choosing good parameters.
""")

st.divider()

# Sidebar controls
st.sidebar.header("🎛️ LCG Parameters")
st.sidebar.markdown("Adjust these values to see how they affect the generator:")

m = st.sidebar.slider("Modulus (m)", min_value=8, max_value=64, value=16, step=4,
                      help="The 'box size' - all numbers will be between 0 and m-1")
a = st.sidebar.slider("Multiplier (a)", min_value=1, max_value=15, value=5,
                      help="Multiplier in the formula")
c = st.sidebar.slider("Increment (c)", min_value=0, max_value=15, value=3,
                      help="Constant added in each step")
seed = st.sidebar.slider("Seed", min_value=0, max_value=m-1, value=1,
                         help="Starting value of the sequence")

st.sidebar.divider()

# Animation controls
st.sidebar.header("⚙️ Visualization Settings")
show_animation = st.sidebar.checkbox("Show Step-by-Step Animation", value=True,
                                     help="Animate each calculation step")
animation_speed = st.sidebar.slider("Animation Speed", min_value=0.1, max_value=2.0, 
                                   value=0.5, step=0.1,
                                   help="Seconds per step")

st.sidebar.divider()
st.sidebar.markdown("### 💡 Tips")
st.sidebar.markdown("""
- Try different **modulus** values to see larger/smaller sequences
- **Good LCG parameters** create patterns that fill the 2D plot uniformly
- **Poor parameters** create obvious patterns or short cycles
- Classic example: `m=16, a=5, c=3` (shown by default)
""")

# Generate sequence
def generate_sequence(m, a, c, seed, max_len=None):
    if max_len is None:
        max_len = m + 1
    sequence = []
    x = seed
    seen = set()
    
    for _ in range(max_len):
        if x in seen and len(sequence) > 1:  # Detected cycle
            break
        seen.add(x)
        sequence.append(x)
        x = (a * x + c) % m
    
    return sequence

sequence = generate_sequence(m, a, c, seed)

# Display sequence info
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Sequence Length", len(sequence))
with col2:
    st.metric("Period", len(sequence) - 1 if len(sequence) > 1 else 0)
with col3:
    coverage = (len(set(sequence)) / m) * 100
    st.metric("Coverage", f"{coverage:.1f}%")

st.caption(f"Sequence: {' → '.join(map(str, sequence[:min(20, len(sequence))]))}" + 
          (" → ..." if len(sequence) > 20 else ""))

st.divider()

# Create two columns for the visualization
if show_animation:
    st.subheader("🎬 Step-by-Step Calculation")
    
    # Create placeholder for animation
    viz_col1, viz_col2 = st.columns(2)
    
    with viz_col1:
        st.markdown("#### Equation Steps (1D View)")
        math_placeholder = st.empty()
    
    with viz_col2:
        st.markdown("#### Resulting Sequence (2D View)")
        pattern_placeholder = st.empty()
    
    # Animation
    x_data, y_data = [], []
    
    for idx in range(len(sequence) - 1):
        current_val = sequence[idx]
        next_val = sequence[idx + 1]
        
        # Step 1: Show current value
        fig1, ax1 = plt.subplots(figsize=(6, 2))
        ax1.set_xlim(0, max(m*a + c, 20))
        ax1.set_ylim(-0.5, 0.5)
        ax1.get_yaxis().set_visible(False)
        ax1.axhline(0, color='gray', linestyle='--', alpha=0.3)
        ax1.barh(0, current_val, height=0.3, color='blue', alpha=0.7)
        ax1.set_title(f"Step 1: Start with $X_n = {current_val}$", fontsize=10)
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['left'].set_visible(False)
        plt.tight_layout()
        math_placeholder.pyplot(fig1)
        plt.close(fig1)
        time.sleep(animation_speed)
        
        # Step 2: Multiply
        val = current_val * a
        fig2, ax2 = plt.subplots(figsize=(6, 2))
        ax2.set_xlim(0, max(m*a + c, 20))
        ax2.set_ylim(-0.5, 0.5)
        ax2.get_yaxis().set_visible(False)
        ax2.axhline(0, color='gray', linestyle='--', alpha=0.3)
        ax2.barh(0, val, height=0.3, color='orange', alpha=0.7)
        ax2.set_title(f"Step 2: Multiply by {a} → $({a} \\times {current_val}) = {val}$", fontsize=10)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        plt.tight_layout()
        math_placeholder.pyplot(fig2)
        plt.close(fig2)
        time.sleep(animation_speed)
        
        # Step 3: Add increment
        val = (current_val * a) + c
        fig3, ax3 = plt.subplots(figsize=(6, 2))
        ax3.set_xlim(0, max(m*a + c, 20))
        ax3.set_ylim(-0.5, 0.5)
        ax3.get_yaxis().set_visible(False)
        ax3.axhline(0, color='gray', linestyle='--', alpha=0.3)
        ax3.barh(0, val, height=0.3, color='green', alpha=0.7)
        ax3.set_title(f"Step 3: Add {c} → ${current_val*a} + {c} = {val}$", fontsize=10)
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)
        ax3.spines['left'].set_visible(False)
        plt.tight_layout()
        math_placeholder.pyplot(fig3)
        plt.close(fig3)
        time.sleep(animation_speed)
        
        # Step 4: Modulo
        val_before = (current_val * a) + c
        fig4, ax4 = plt.subplots(figsize=(6, 2))
        ax4.set_xlim(0, max(m*a + c, 20))
        ax4.set_ylim(-0.5, 0.5)
        ax4.get_yaxis().set_visible(False)
        ax4.axhline(0, color='gray', linestyle='--', alpha=0.3)
        ax4.barh(0, next_val, height=0.3, color='purple', alpha=0.7)
        ax4.set_title(f"Step 4: Modulo {m} → ${val_before} \\mod {m} = {next_val}$", fontsize=10)
        ax4.spines['top'].set_visible(False)
        ax4.spines['right'].set_visible(False)
        ax4.spines['left'].set_visible(False)
        plt.tight_layout()
        math_placeholder.pyplot(fig4)
        plt.close(fig4)
        
        # Update 2D plot
        x_data.append(current_val)
        y_data.append(next_val)
        
        fig5, ax5 = plt.subplots(figsize=(6, 6))
        ax5.set_xlim(-1, m)
        ax5.set_ylim(-1, m)
        ax5.set_xlabel("$X_n$", fontsize=11)
        ax5.set_ylabel("$X_{n+1}$", fontsize=11)
        ax5.grid(True, linestyle=':', alpha=0.4)
        ax5.plot(x_data, y_data, 'rs-', markersize=8, linewidth=1, alpha=0.6)
        ax5.set_aspect('equal')
        ax5.set_title(f"Pattern Evolution (Step {idx+1}/{len(sequence)-1})", fontsize=10)
        plt.tight_layout()
        pattern_placeholder.pyplot(fig5)
        plt.close(fig5)
        
        time.sleep(animation_speed * 0.5)

else:
    # Static visualization (both plots side by side)
    st.subheader("📊 Complete Sequence Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Final State")
        # Show final calculation
        if len(sequence) > 1:
            last_idx = len(sequence) - 2
            current_val = sequence[last_idx]
            next_val = sequence[last_idx + 1]
            val_before = (current_val * a) + c
            
            fig_final, ax_final = plt.subplots(figsize=(6, 2))
            ax_final.set_xlim(0, max(m*a + c, 20))
            ax_final.set_ylim(-0.5, 0.5)
            ax_final.get_yaxis().set_visible(False)
            ax_final.axhline(0, color='gray', linestyle='--', alpha=0.3)
            ax_final.barh(0, next_val, height=0.3, color='purple', alpha=0.7)
            ax_final.set_title(f"Last Calculation: ${val_before} \\mod {m} = {next_val}$", fontsize=10)
            ax_final.spines['top'].set_visible(False)
            ax_final.spines['right'].set_visible(False)
            ax_final.spines['left'].set_visible(False)
            plt.tight_layout()
            st.pyplot(fig_final)
            plt.close(fig_final)
    
    with col2:
        st.markdown("#### 2D Pattern (Spectral View)")
        # Generate complete 2D plot
        x_data = sequence[:-1]
        y_data = sequence[1:]
        
        fig_pattern, ax_pattern = plt.subplots(figsize=(6, 6))
        ax_pattern.set_xlim(-1, m)
        ax_pattern.set_ylim(-1, m)
        ax_pattern.set_xlabel("$X_n$", fontsize=11)
        ax_pattern.set_ylabel("$X_{n+1}$", fontsize=11)
        ax_pattern.grid(True, linestyle=':', alpha=0.4)
        ax_pattern.plot(x_data, y_data, 'rs-', markersize=8, linewidth=1, alpha=0.6)
        ax_pattern.set_aspect('equal')
        ax_pattern.set_title("Complete Sequence Pattern", fontsize=11)
        plt.tight_layout()
        st.pyplot(fig_pattern)
        plt.close(fig_pattern)

st.divider()

# Additional insights
st.subheader("📈 Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Sequence Quality")
    unique_values = len(set(sequence))
    max_possible = m
    
    if unique_values == max_possible:
        st.success(f"✓ Full period! Generates all {m} possible values.")
    elif unique_values > max_possible * 0.7:
        st.info(f"Good coverage: {unique_values}/{max_possible} unique values")
    else:
        st.warning(f"Limited coverage: {unique_values}/{max_possible} unique values")
    
    # Check for obvious patterns
    if len(sequence) < m // 2:
        st.warning("⚠️ Short cycle detected - poor parameter choice")

with col2:
    st.markdown("#### Parameter Quality")
    
    # Hull-Dobell Theorem checks (for full period)
    checks = []
    
    # c and m must be coprime
    from math import gcd
    if gcd(c, m) == 1:
        checks.append("✓ c and m are coprime")
    else:
        checks.append("✗ c and m are not coprime")
    
    # a-1 divisible by all prime factors of m
    # Simplified check for power of 2
    if m & (m-1) == 0:  # m is power of 2
        if (a - 1) % 4 == 0:
            checks.append("✓ a-1 is divisible by 4")
        else:
            checks.append("✗ a-1 is not divisible by 4")
    
    for check in checks:
        if "✓" in check:
            st.success(check)
        else:
            st.error(check)

st.divider()

# Footer
st.markdown("""
---
### 🧮 About LCGs

LCGs were first proposed by Lehmer in 1949 and have been extensively studied. While simple and fast, 
they have known limitations:
- Predictable patterns in higher dimensions
- Not cryptographically secure
- Quality heavily depends on parameter selection

For modern applications requiring high-quality randomness, consider using cryptographically secure 
pseudo-random number generators (CSPRNGs) instead.

**Made with Streamlit** | [View on GitHub](https://github.com/cosalt/lcg-visualization)
""")
