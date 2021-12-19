import dialogflow
import os
from google.api_core.exceptions import InvalidArgument

# key access for google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'private_key4.json'
session_client = dialogflow.SessionsClient()
session = session_client.session_path('test-t9ek', 'Ruslan')

while True:
    message = input('>>')
    text_input = dialogflow.types.TextInput(text=message, language_code='ru')
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        if response.query_result.fulfillment_text:
            print(response.query_result.fulfillment_text,
                  '('+response.query_result.intent.display_name +')')
        else:
            print('Im not inderstand you dude')




    except InvalidArgument:
        raise

