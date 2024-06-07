import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from PIL import Image


img=Image.open("Cluster-Legacy-Inner-Orange.jpg")
st.image(img,use_column_width=True)


st.write("""
    # DNA Nucleotide Count Web App
    This app counts the nucleotide composition of queried DNA

    
""")

st.header("Enter DNA Sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence=st.text_area("Sequence Input",sequence_input,height=250)
sequence=sequence.splitlines()
sequence=sequence[1:]
sequence=''.join(sequence)

st.write("""
         ***
         """)

st.header( "Input (DNA Query)")
sequence

st.header("Output (DNA Nucleotide  count)")

st.subheader("1. Print Dictionary")
def DNA_nucleotide_count(seq):
    d=dict([
       ( 'A',seq.count('A')),
       ( 'T',seq.count('T')),
       ( 'G',seq.count('G')),
       ( 'C',seq.count('C')),
    ])

    return d

X=DNA_nucleotide_count(sequence)

X_label=list(X)
X_values=list(X.values())

X
st.subheader("2. Print Text")
st.write(f"There are {X['A']} adenine(A)")
st.write(f"There are {X['T']} thymine(T)")
st.write(f"There are {X['G']} guanine(G)")
st.write(f"There are {X['A']} cytosine(C)")

st.subheader("1. Display Dataframe")

df=pd.DataFrame.from_dict(X,orient='index')
df=df.rename({0:"count"},axis="columns")
df.reset_index(inplace=True)
df=df.rename({'index':"nucleotide"},axis="columns")

st.write(df)

st.subheader("4. Display Bar Chart")

p=alt.Chart(df).mark_bar().encode(x='nucleotide',y='count')
p=p.properties(width=alt.Step(80))

st.write(p)
