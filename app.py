import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

st.title("Anaesthetic Drug Simulator")

infusion_rate = st.slider("Infusion rate", 0.1, 3.0, 1.2)
k10 = st.slider("Elimination rate", 0.1, 0.5, 0.25)

time = np.linspace(0, 3, 300)

def model(C, t, k10, infusion_rate):
    return infusion_rate - k10*C

solution = odeint(model, 0, time, args=(k10, infusion_rate))

fig, ax = plt.subplots()
ax.plot(time, solution)

ax.set_xlabel("Time (hours)")
ax.set_ylabel("Drug concentration")

st.pyplot(fig)