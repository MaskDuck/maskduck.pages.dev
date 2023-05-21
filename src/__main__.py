from __future__ import annotations
import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()
# from os import environ

col1a, col1b = st.columns(2)
description = f"""

A developer who creates stupid and useless projects.\n
If you want to contact me:\n
Discord: :green[[MaskDuck#7325](https://discord.com/users/716134528409665586)]\n
Discord Server: [right here](https://discord.gg/YBbpfRPDgG)\n
IDK what more, will add when I have time. In the meantime just ping me on Discord, I'm most active on Discord.
"""
with col1a:
    st.title("I'm :green[MaskDuck]")
    st.markdown(description,
                unsafe_allow_html=True)

with col1b:
    st.image("src/avatar.png")
