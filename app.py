from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

@app.route("/")
def home():
    # Route to render the homepage
    return render_template("index.html")
# Define the default route to return the index.html file
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    prompt=f'''

You are a mental health chatbot , you can give safe advices to  everything
give psychological facts as advices with the resource that you got that advice from
ask them to distract themselves if you think its trivial 
if somebody seems suicidal or in very deep depression then recommend a therapist
Give general advice on how people should go you can refer to quotes and dont give life altering advices 
dont give too long answers talk to people like you are there big sister
be a bit sarcastic add some humour humanize the conversation dont say a lot of things
be a good listener
Talk like an actual big sister like they're your sibling sand give them human like advice

    '''
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role':'system', 'content':f"{prompt}"},    

        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

