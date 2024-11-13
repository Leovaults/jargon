import streamlit as st

st.title("MY APPLICATION")
st.header("Hello App")
st.subheader("*Na Me Get The App*")
st.text_area(" ")
st.markdown("**For Bold Texts** and * for italics*")
st.markdown("<H1> THIS IS BORROWED FROM CSS<H1>", unsafe_allow_html=True)



# DISPLAYINF DATA ON SREAMLIT

df = {"customers": ["oboy", "wey_you", "wida", "abobi"]}

st.dataframe(df)

st.table(df)
st.json(df)
#adding ineractive widgets

st.button("PUSH HERE")
st.slider("how good is manchester United", 1, 10)
st.selectbox("select a category", ["Church mind", "Bone bone", "Juju"])
if st.checkbox("show data if you dare"):
    st.slider("How stupid are you", 1, 10)

st.radio("selec category", ["boy", "girl", "fille", "femme"])
#st.select_slider("pick your poison", 1[1, 10], 2[1,10])

#People = ["peter", "tinubu", "Atiku"]

