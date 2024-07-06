import streamlit as st
import requests

'''
# CallTagger frontend
'''

st.markdown('''
CallTagger is an application that you can use to classify your text/transcript
''')


url = 'https://mvp-calltagger-sqsyyuiuaq-ew.a.run.app/predict'

#'https://mvp-calltagger-sqsyyuiuaq-ew.a.run.app/predict?transcript='

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
    st.write('The predicted label is', str(response['predicted_label']))
else:
    st.write('Click to get label')
