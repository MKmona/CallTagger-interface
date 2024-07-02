import streamlit as st
import requests

'''
# CallTagger frontend
'''

st.markdown('''
CallTagger is an application that you can use to classify your text/transcript
''')


url = 'https://mvp-y3djeduupq-ew.a.run.app'

# First Method
# Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# st.text_input(
#         "Placeholder for the other text input widget",
#         "",
#         key="placeholder",
#     )

# # input user's transcript
# text_input = st.text_input(
#         "Enter a transcript 👇",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
    #     placeholder=st.session_state.placeholder,
    # )
# st.write("You entered: ", text_input)


# if st.button('Predict Label'):
#     response = requests.get(url=url).json()
#     print(response)
#     # print is visible in the server output, not in the page
#     print('button clicked!')
#     st.write('Click to get new prediction')
#     # st.write('Further clicks are not visible but are executed')
#     # display the prediction to the user
#     st.write('The predicted label is', (response['target label']))
# else:
#     st.write('Click to get label')


# Method 2

user_transcript = st.text_area('Enter a text to be analyzed 👇', max_chars=3000)
# st.write("You entered: ", user_transcript)

params = {'transcript': user_transcript}

button = st.button('Target Label')
if button:
    response = requests.get(url=url,
                        params=params).json()
    print(response)
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('Click to get new prediction')
    # st.write('Further clicks are not visible but are executed')
    # display the prediction to the user
    st.write('The predicted label is', (response['target label']))
else:
    st.write('Click to get label')
