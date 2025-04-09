import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Vn
def calculate_vn(h, b, d, a, a_d, fck, rf, rv, rh, fyt, fyv, fyh):
    V_1 = 381.7 + 2.294 * h - 3.331 * d - 2.393 * b - 0.0360 * a
    V_2 = 0.000098 * h**2 + 0.000364 * a**2 + 0.007280 * h * b - 0.000637 * h * a - 0.002486 * b * a
    V_3 = -2.91 * fck - 0.1872 * fyh + 0.1424 * fyt
    V_4 = -0.04547 * fck**2 - 0.00262 * fck * fyt - 0.002001 * fck * fyh
    V_5 = -15984 * rf - 6618 * rv - 18508 * rh
    V_6 = -98.1 * h * rf + 129.8 * d * rf + 62.32 * b * rf + 315.9 * b * rh + 24.27 * a * rv - 21.45 * a * rh
    V_7 = 176.9 * fck * rf + 0.000416 * a * fyh
    V_8 = -0.0346 * fck * h + 0.0601 * fck * d + 0.03379 * fck * b - 0.008572 * fck * a

    Vn = V_1 + V_2 + V_3 + V_4 + V_5 + V_6 + V_7 + V_8
    return Vn

# Streamlit app interface
st.set_page_config(
    page_title="Shear Capacity of RC Deep Beams (Vn) Calculator",
    page_icon="https://github.com/MHR-u/Deep_Beam/blob/main/Deep%20Beam.png?raw=true",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f6;
        }
        .title-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .title-text {
            font-size: 2.2rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .image-container img {
            width: 100%;
            max-width: 1200px;
            height: auto;
            margin-top: 10px;
            border-radius: 10px;
        }
        .note-box {
            background-color: #d4edda;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 3px rgba(0, 0, 0, 0.1);
        }
        hr {
            border: none;
            height: 1px;
            background-color: #ddd;
            margin-top: 20px;
            margin-bottom: 20px;
        }

    </style>
""", unsafe_allow_html=True)

# Stylish header with title and image
st.markdown(f"""
    <div class="title-container">
        <div class="title-text">Shear Capacity of RC Deep Beams (Vn)</div>
        <div class="image-container">
            <img src="https://github.com/MHR-u/Deep_Beam/blob/main/Deep%20Beam.png?raw=true" alt="Image">
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Stylish Note Section
st.markdown("""
<div class="note-box">
    <strong>Note:</strong>
    <ol>
        <li>The shear capacity of RC deep beams (Vn) is determined based on the parameters provided below.</li>
        <li>The accuracy of the output increases as the input values remain within the specified MIN-MAX ranges.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Definitions
st.write(""" 
### Definitions:
- **h**: Beam height in (mm).
- **b**: Section width in (mm).
- **d**: Effective depth in (mm).
- **a**: Shear span in (mm).
- **a/d**: Shear span-to-effective depth ratio (dimensionless).
- **fck**: Concrete compressive strength in (MPa).
- **rf**: Flectural reinforcement ratio.
- **rv**: Vertical reinforcement ratio.
- **rh**: Horizontal reinforcement ratio.
- **fyt**: Yield stress of flexural reinforcement in (MPa).
- **fyv**: Yield stress of vertical reinforcement in (MPa).
- **fyh**: Yield stress of horizontal reinforcement in (MPa).
""")

# Inputs with tooltips
st.write("### Enter the following parameters:")
h = st.number_input("h (mm) [Min=160 - Max=2100]:", value=0.0, help="Section height in (mm).")
b = st.number_input("b (mm) [Min=51 - Max=600]:", value=0.0, help="Section width in (mm).")
d = st.number_input("d (mm) [Min=140 - Max=2000]:", value=0.0, help="Effective depth in (mm).")
a = st.number_input("a (mm) [Min=80 - Max=2500]:", value=0.0, help="Shear span in (mm).")
a_d = st.number_input("a/d (mm) [Min=0.27 - Max=2.5]:", value=0.0, help="Shear span in (mm).")
fck = st.number_input("fck (MPa) [Min=11.3 - Max=120.1]:", value=0.0, help="Concrete compressive strength in (MPa).")
rf = st.number_input("rf [Min=0.0026 - Max=0.1133]:", value=0.0, help="Flexural reinforcement ratio.")
rv = st.number_input("rv [Min=0.00 - Max=0.0286]:", value=0.0, help="Vertical reinforcement ratio.")
rh = st.number_input("rh [Min=0.00 - Max=0.0317]:", value=0.0, help="Horizontal reinforcement ratio.")
fyt = st.number_input("fyt (MPa) [Min=267 - Max=1330]:", value=0.0, help="Yield stress of flexural reinforcement in (MPa).")
fyv = st.number_input("fyv (MPa) [Min=0.00 - Max=1051]:", value=0.0, help="Yield stress of vertical reinforcement in (MPa).")
fyh = st.number_input("fyh (MPa) [Min=0.00 - Max=855]:", value=0.0, help="Yield stress of horizontal reinforcement in (MPa).")

# Allow the user to choose which variable to plot against Vn
plot_variable = st.selectbox("Select a variable to plot against Vn:", ["h", "b", "d", "a", "a_d", "fck", "rf", "rv", "rh", "fyt", "fyv", "fyh"])

# Convert Vn to N or kN
convert_units = st.radio("Convert Vn to:", ('kN', 'N'))

# Calculate Vn when button is pressed
if st.button("Calculate Vn"):
    if h > 0 and b > 0 and d > 0 and a > 0 and a_d > 0 and fck > 0:
        Vn = calculate_vn(h, b, d, a, a_d, fck, rf, rv, rh, fyt, fyv, fyh)

        # Convert to N or kN
        if convert_units == 'N':
            Vn *= 1000  # Convert to N

        st.subheader(f"Calculated Vn: {Vn:.2f} {convert_units}")

        # Plotting Vn against the selected variable
        if plot_variable == "h":
            variable_values = np.linspace(100, 1000, 100)
            vn_values = [calculate_vn(h_val, b, d, a, a_d, fck, rf, rv, rh, fyt, fyv, fyh) for h_val in variable_values]
        elif plot_variable == "b":
            variable_values = np.linspace(100, 500, 100)
            vn_values = [calculate_vn(h, b_val, d, a, a_d, fck, rf, rv, rh, fyt, fyv, fyh) for b_val in variable_values]
        elif plot_variable == "d":
            variable_values = np.linspace(100, 500, 100)
            vn_values = [calculate_vn(h, b, d_val, a, a_d, fck, rf, rv, rh, fyt, fyv, fyh) for d_val in variable_values]
        elif plot_variable == "a":
            variable_values = np.linspace(100, 500, 100)
            vn_values = [calculate_vn(h, b, d, a_val, a_d, fck, rf, rv, rh, fyt, fyv, fyh) for a_val in variable_values]
        elif plot_variable == "a_d":
            variable_values = np.linspace(2.0, 4.0, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d_val, fck, rf, rv, rh, fyt, fyv, fyh) for a_d_val in variable_values]
        elif plot_variable == "fck":
            variable_values = np.linspace(10, 100, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d, fck_val, rf, rv, rh, fyt, fyv, fyh) for fck_val in variable_values]
        elif plot_variable == "rf":
            variable_values = np.linspace(0.001, 0.1, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d, fck, rf_val, rv, rh, fyt, fyv, fyh) for rf_val in variable_values]
        elif plot_variable == "rv":
            variable_values = np.linspace(0.001, 0.03, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d, fck, rf, rv_val, rh, fyt, fyv, fyh) for rv_val in variable_values]
        elif plot_variable == "rh":
            variable_values = np.linspace(0.001, 0.03, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d, fck, rf, rv, rh_val, fyt, fyv, fyh) for rh_val in variable_values]
        elif plot_variable == "fyt":
            variable_values = np.linspace(100, 600, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d, fck, rf, rv, rh, fyt_val, fyv, fyh) for fyt_val in variable_values]
        elif plot_variable == "fyv":
            variable_values = np.linspace(100, 600, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d, fck, rf, rv, rh, fyt, fyv_val, fyh) for fyv_val in variable_values]
        elif plot_variable == "fyh":
            variable_values = np.linspace(100, 600, 100)
            vn_values = [calculate_vn(h, b, d, a, a_d, fck, rf, rv, rh, fyt, fyv, fyh_val) for fyh_val in variable_values]

        if convert_units == 'N':
            vn_values = [vn * 1000 for vn in vn_values]

        # Filter out negative Vn values
        variable_values_filtered = []
        vn_values_filtered = []
        for v, vn in zip(variable_values, vn_values):
            if vn > 0:
                variable_values_filtered.append(v)
                vn_values_filtered.append(vn)

        # Plot
        fig, ax = plt.subplots()
        ax.plot(variable_values_filtered, vn_values_filtered, label=f"Vn vs. {plot_variable}", color='green')
        ax.set_xlabel(plot_variable)
        ax.set_ylabel(f"Vn ({convert_units})")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.error("Please input valid values for all parameters.")

# Footer
st.write("""
### Researchers:
**Maher K. Abbas<sup>1</sup>**, and **Iman Kattoof Harith<sup>1</sup>**

<sup>1</sup>Civil Engineering Department, College of Engineering, Al-Qasim Green University, Babylon, 51013, Iraq. 
""", unsafe_allow_html=True)
