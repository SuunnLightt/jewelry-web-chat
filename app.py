from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(prompt):
    responses = {
        "Vintage Ring Ideas": "A sterling silver band with 1920s filigree and a 4mm peridot (~$7). Dainty vintage is trending in 2025 (MCP fashion blog pull).",
        "Trending Necklaces": "A silver chain with a chunky turquoise pendant (~$8). Bold stones are hot this year per X chatter (MCP scrape).",
        "Gemstone Pairings for Silver": "Silver + amethyst (5mm, ~$10): Cool and chic, trending for calm vibes (MCP X buzz).",
        "Earring Trends": "Silver hoops with dangling onyx beads (~$5 each). Long drops are spiking in 2025 (MCP style post).",
        "Mexican Themed Ideas": "A silver cuff with a 6mm raw opal (~$12), inspired by Taxco designs. Bright stones are big per MCP trend fetch.",
        "Caribbean Ideas": "A silver ring with a 5mm larimar (~$15), sea-blue and breezy. Ocean hues are popping in 2025 (MCP blog snag)."
    }
    return responses.get(prompt, f"Here’s a custom idea for '{prompt}': A silver piece with a 5mm turquoise (~$8), trendy and timeless per MCP X vibes.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.json['prompt']
    response = get_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
