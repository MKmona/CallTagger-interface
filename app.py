import streamlit as st
import requests
from PIL import Image


'''
# CallTagger Application
'''

st.markdown('''
CallTagger is an application that you can use to classify your text/transcript
''')

image = Image.open('../CallTagger-interface/images/callCenter_girl.png')

# Images (and most elements in general) are always aligned to the left, to align the image to the center we can use:
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image, caption='Welcome to our Call Center Service')

# st.image(image, caption='Welcome to our Call Center Service')

url = 'https://mvp-calltagger-sqsyyuiuaq-ew.a.run.app/predict'


user_transcript = st.text_area('**Please enter a text to be analyzed and categorized**👇', max_chars=3000)
# st.write("You entered: ", user_transcript)

params = {'transcript': user_transcript}

button = st.button('Predicted Label')
if button:
    response = requests.get(url=url,
                        params=params).json()
    print(response)
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('Click to get new prediction')
    # st.write('Further clicks are not visible but are executed')

    # display the prediction to the user in **bold** and the label in blue
    # st.write('**The predicted label is: **', str(response['predicted_label']))
    st.write(f'**The predicted label is: :blue[{str(response["predicted_label"])}]**')
else:
    st.write('Click to get label')
