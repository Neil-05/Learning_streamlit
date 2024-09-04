import streamlit as st

st.title('Neil')
st.header('Waiting for the message')
st.subheader('Will she?')
st.text('I guess so :)')

st.markdown('# I like games')
st.markdown('## I like games')
st.markdown('###### I like games')

st.success('Data is submitted')
st.info('information')
st.warning('THis is a warning')
st.error('THis is for error')

exp=ZeroDivisionError('Division is not possible by 0 ')
st.exception(exp)

st.help(ZeroDivisionError)

st.write("range (1,10)")
st.write(range (1,10))

st.write("1+2+3")
st.write(1+2+3)

st.code('x=10\n'
         'arange(x,20,1)\n'
         '\tprint(x)')

st.checkbox('Hello')

if(st.checkbox("Handsome")):
    st.success("Thanks for your compliment")
if(st.checkbox("Work of a god")):
    st.warning("Huh, I already knew")

radiob=st.radio('Select : ',('Green Flag','Red Flag'))
if(radiob=='Green Flag'):
    st.write('Congratulation!! she will never be yours.')
elif(radiob=='Red Flag'):
    st.write('Tujhe hi degi bhai wohhh')

st.subheader('SelectBox : ')
selectbox=st.selectbox("KKRH : ",['Data Analytics','Machine Learning','Natural Language Processing','Web Scarping','Image Processing','Computer Vision'])
st.write('You have selected : ',selectbox)

st.subheader('MultiSelectBox : ')
multisel=st.multiselect("Kya karna chahte ho  : ",['Data Analytics','Machine Learning','Natural Language Processing','Web Scarping','Image Processing','Computer Vision'])
st.write('You have selected : ', len(multisel), multisel)

st.subheader("Button ")
st.button('Click me ')
if(st.button('Click on me :)')):
    st.write("ahahahahaah, save me ")

st.text('Slider')
slide=st.slider("Input your age : ",1,90,step=1)
if(slide<18):
    st.error('You cannot enter the site as for your saftey issues.')
elif(slide>18 and slide<=22):
    st.warning('Enter on your own risk. \nWelcome!')
else:
    st.success('A Warm welcome to you.')

st.text('Enter your Username: ')
name= st.text_input('UserName : ')
if(name):
    st.write("Hi",name)

st.text("Enter your password")
st.text_input("Password: ",type='password')

textArea=st.text_area("Write about yourself  ")
st.write(textArea)

st.subheader("Enter your age: ")
st.number_input('Age : ',18,90,step=1)

st.subheader("Enter Date ")
st.date_input('Date : ')

st.subheader("Enter your time : ")
st.time_input('Time : ',step=60)
