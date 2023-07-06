import openai
from flask import Flask, request, jsonify

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Create Flask web application
app = Flask(__name__)

# Define a route for the question-answering endpoint
@app.route('/ask', methods=['POST'])
def ask_question():
    # Get the question from the request
    question = request.json['question']

    

   


# Generate the answer using GPT-3.5 or GPT-4
    response = openai.Completion.create(
        engine=
   
'text-davinci-003',  # Specify GPT version (GPT-3.5 or GPT-4)
        prompt=question,
        max_tokens=
        prompt=question,
       

        prompt=question,

       
100,
        n=
       
1,
        stop=
       
None,
        temperature=
       
0.7
    )

    
    )

   

    )

# Extract the generated answer from the API response
    answer = response.choices[
    answer = response.choices

   
0].text.strip()

    

   


# Return the answer as a JSON response
    
   
return jsonify({'answer': answer})

# Run the Flask application
if __name__ == '__main__':
    app.run()

    app.run