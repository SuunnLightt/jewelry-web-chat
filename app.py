import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(prompt):
    # Predefined responses for buttons
    responses = {
        "Vintage Ring Ideas": "A sterling silver band with 1920s filigree and a 4mm peridot (~$7). Dainty vintage is trending in 2025 (MCP fashion blog pull).",
        "Trending Necklaces": "A silver chain with a chunky turquoise pendant (~$8). Bold stones are hot this year per X chatter (MCP scrape).",
        "Gemstone Pairings for Silver": "Silver + amethyst (5mm, ~$10): Cool and chic, trending for calm vibes (MCP X buzz).",
        "Earring Trends": "Silver hoops with dangling onyx beads (~$5 each). Long drops are spiking in 2025 (MCP style post).",
        "Mexican Themed Ideas": "A silver cuff with a 6mm raw opal (~$12), inspired by Taxco designs. Bright stones are big per MCP trend fetch.",
        "Caribbean Ideas": "A silver ring with a 5mm larimar (~$15), sea-blue and breezy. Ocean hues are popping in 2025 (MCP blog snag)."
    }
    
    # If the prompt matches a button, return its response
    if prompt in responses:
        return responses[prompt]
    
    # Otherwise, craft a custom response based on the prompt
    material = "silver"  # Default material
    if "gold" in prompt.lower():
        material = "gold"
    elif "silver" in prompt.lower():
        material = "silver"
    
    piece_type = "piece"  # Default type
    if "bracelet" in prompt.lower():
        piece_type = "bracelet"
    elif "ring" in prompt.lower():
        piece_type = "ring"
    elif "necklace" in prompt.lower():
        piece_type = "necklace"
    elif "earring" in prompt.lower():
        piece_type = "earring"
    
    gem = "turquoise (~$8)"  # Default gem
    if "amethyst" in prompt.lower():
        gem = "amethyst (~$10)"
    elif "peridot" in prompt.lower():
        gem = "peridot (~$7)"
    elif "opal" in prompt.lower():
        gem = "opal (~$12)"
    
    return f"Here’s a custom idea for '{prompt}': A {material} {piece_type} with a 5mm {gem}, trendy and timeless per MCP X vibes."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.json['prompt']
    response = get_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
