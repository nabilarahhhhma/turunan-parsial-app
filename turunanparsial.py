import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("🧮 Aplikasi Turunan Parsial")

# Input fungsi
x, y = sp.symbols('x y')
fungsi_str = st.text_input("Masukkan fungsi f(x, y):", "x**2 * y + y**3")

try:
    f = sp.sympify(fungsi_str)
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    st.latex(f"f(x, y) = {sp.latex(f)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

    # Input titik evaluasi
    x0 = st.number_input("Nilai x₀:", value=1.0)
    y0 = st.number_input("Nilai y₀:", value=2.0)

    # Evaluasi fungsi dan turunannya
    f_val = f.subs({x: x0, y: y0})
    fx_val = fx.subs({x: x0, y: y0})
    fy_val = fy.subs({x: x0, y: y0})

    st.write("Nilai fungsi di titik (x₀, y₀):", f_val)
    st.write("Gradien di titik (x₀, y₀):", f"({fx_val}, {fy_val})")

    st.subheader("📊 Grafik Permukaan & Bidang Singgung")

    # Plotting
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Rentang nilai
    X_vals = np.linspace(x0 - 2, x0 + 2, 50)
    Y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(X_vals, Y_vals)

    f_lambd = sp.lambdify((x, y), f, 'numpy')
    Z = f_lambd(X, Y)

    # Fungsi bidang singgung z = f(x0, y0) + fx*(x - x0) + fy*(y - y0)
    Z_tangent = float(f_val) + float(fx_val)*(X - x0) + float(fy_val)*(Y - y0)

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, label="Permukaan")
    ax.plot_surface(X, Y, Z_tangent, color='red', alpha=0.5, label="Bidang Singgung")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title("Permukaan Fungsi dan Bidang Singgung")

    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
