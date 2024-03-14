from flask import Flask, request, jsonify
from simple_python.src import remove_null, reverse_substrings

app = Flask(__name__)

@app.route('/clean_string', methods=['POST'])
def clean_string():
    """This route handles POST requests to clean a string.
    
    It expects a JSON object with a key 'string' containing the input string.
    It then removes 'NULL' values and reverses substrings in the input string.
    
    Returns:
    JSON: A JSON object with the cleaned string.
    """
    data = request.json
    if 'string' not in data:
        return jsonify({'error': 'String not found in request data'}), 400
    
    input_string = data['string']
    
    # Perform cleaning operations
    cleaned_string = remove_null(input_string)
    cleaned_string = reverse_substrings(cleaned_string)

    return jsonify({'cleaned_string': cleaned_string}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=12345)

