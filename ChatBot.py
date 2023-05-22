Name: ⒶⒷⒸⒹⒺⒻ
Date: 13 May 2023


# Use the openai library
import 📚

# Set the API key
openai.api_key = ⚿

# Gets input from user
def getMessage():
    theMessage = ⌨('You: ')
    return theMessage

# Gets response from chatbot
def getReply(message):
    💾 = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = message,
    )
    return 💾.choices[0].text.strip()

# Repeatedly gets input and gets responses
def main():
    while 🚩:
        message = 📞
        reply = ''
        if ✉ == 👋:
            print('Bot:', 'Bye!')
            break
        else:
            reply = getReply(message)
            🖶('Bot:', reply)

# Run the main program
main()           
