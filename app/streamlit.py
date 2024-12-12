# streamlit_app.py
import streamlit as st
from Individual import Individual
from GP import GP
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from PIL import Image
import os
import glob
import re
import pandas as pd
import seaborn as sns


def create_gif(directory):
    frames = []
    imgs = sorted(glob.glob(f"{directory}/*.png"))
    imgs.sort(key=lambda f: int(re.sub("\D", "", f)))
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    if frames:
        frames[0].save(
            f"{directory}/created_gif_new.gif",
            format="GIF",
            append_images=frames[1:],
            save_all=True,
            duration=200,
            loop=0,
        )


# Page configuration
st.set_page_config(page_title="Genetic Algorithm Image Recreation", layout="wide")

# UI title and description
st.title("Genetic Algorithm Image Recreation")


def display_image(image, caption):
    buf = BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    encoded = base64.b64encode(byte_im).decode()
    st.image(f"data:image/png;base64,{encoded}", caption=caption)


# Sidebar for user inputs
st.sidebar.header("Settings")
population_size = st.sidebar.slider(
    "Population Size", min_value=10, max_value=500, value=100, step=10
)
epochs = st.sidebar.slider(
    "Number of Generations", min_value=100, max_value=10000, value=1000, step=100
)

# Main section
st.header("Original Image")
if st.button("Show Original Image"):
    original_image = Image.open("dog.png")
    st.image(original_image, caption="Original Image", width=300)

st.header("Run Genetic Algorithm")
if st.button("Run Algorithm"):
    gp = GP("dog.png")  # Use your target image path
    fittest = gp.run_gp(population_size, epochs)
    display_image(fittest.image, "Fittest Individual")

    st.success("Images saved for GIF creation!")

    # Create GIF
    create_gif("gif")
    st.image("gif/created_gif_new.gif", caption="Recreation GIF")

st.header("Visualize Crossover and Mutation")
if st.button("Show Crossover and Mutation"):
    ind1 = Individual(200, 200)
    ind2 = Individual(200, 200)
    gp = GP("dog.png")  # Use your target image path
    child = gp.crossover(ind1, ind2)
    if child:
        st.image(
            [ind1.image, ind2.image, child.image],
            caption=["Parent 1", "Parent 2", "Child"],
            width=200,
        )
    else:
        st.warning("Crossover did not produce a fitter child.")

    st.image(ind1.image, caption="Pre-Mutation", width=200)
    gp.mutate(ind1)
    st.image(ind1.image, caption="Post-Mutation", width=200)

st.header("Fitness Graph")
if st.button("Show Fitness Graph"):
    df = pd.read_csv("figures/data_cross.csv")
    sns.lineplot(data=df, x="epoch", y="fitness_estimate")
    plt.xlabel("Generation")
    plt.ylabel("Fittest Individual")
    plt.title("Fittest Individual (Delta_E) vs. Generation")
    plt.axhline(15, ls="--")
    plt.ylim(0, 100)
    st.pyplot(plt)

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #666;
    }
    </style>
    <div class="footer">
        Powered by Genetic Algorithm | Developed by Your Team
    </div>
    """,
    unsafe_allow_html=True,
)
