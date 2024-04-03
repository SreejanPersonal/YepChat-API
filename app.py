from flask import Flask, request, jsonify
import mistral_8x7b_yepchat

app = Flask(__name__)

@app.route('/')
def initial():
    # Developer information
    developer_info = {
        'developer': 'Devs Do Code',
        'contact': {
            'Telegram': 'https://t.me/devsdocode',
            'YouTube Channel': 'https://www.youtube.com/@DevsDoCode',
            'Discord Server': 'https://discord.gg/ehwfVtsAts',
            'Instagram': {
                'Personal': 'https://www.instagram.com/sree.shades_/',
                'Channel': 'https://www.instagram.com/devsdocode_/'
            }
        }
    }

    endpoint = {
    'route': "/chat",
    'params': {
        "query": "[SEARCH QUERY]"
    },
    'optional_params': {
        "max_tokens": "[]",
        "model": "[]",
        "temperature": "[]",
        "assistant": "[]",
        "system": "[]"
    },
    'url_demo' : '/chat?query=example&&max_tokens=100&&model=gpt-3.5&&temperature=0.7&&assistant=assistant_name&&system=system_prompt'
}
    return jsonify([{"endpoint" : endpoint}, {'developer_info': developer_info}])

@app.route('/chat', methods=['GET'])
def chat():
    
    query = request.args.get('query')  # Assuming the query is sent in JSON format
    max_tokens = int(request.args.get('max_tokens', 300))
    temperature = float(request.args.get('temperature', 0.7))  # Optional parameter with default value

    # Developer information
    developer_info = {
        'developer': 'Devs Do Code',
        'contact': {
            'Telegram': 'https://t.me/devsdocode',
            'YouTube Channel': 'https://www.youtube.com/@DevsDoCode',
            'Discord Server': 'https://discord.gg/ehwfVtsAts',
            'Instagram': {
                'Personal': 'https://www.instagram.com/sree.shades_/',
                'Channel': 'https://www.instagram.com/devsdocode_/'
            }
        }
    }

    if query:    
        response = mistral_8x7b_yepchat.Mistral_Inference(max_tokens=max_tokens, temperature=temperature).chat(query)
        return jsonify([{'response': response}, {'developer_info': developer_info}])

    else:
        error_message = {
        'developer_contact': {
            'telegram': 'https://t.me/DevsDoCode',
            'instagram': 'https://www.instagram.com/sree.shades_/',
            'discord': 'https://discord.gg/ehwfVtsAts',
            'linkedin': 'https://www.linkedin.com/in/developer-sreejan/',
            'twitter': 'https://twitter.com/Anand_Sreejan'
        },
        'error': 'Oops! Something went wrong. Please contact the developer Devs Do Code.'
    }
        return jsonify(error_message), 400



