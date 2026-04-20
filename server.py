from flask import Flask, request, jsonify
from ppllocr import OCR
import base64
import re
import argparse

app = Flask(__name__)
ocr = OCR()

pattern = re.compile(r'^data:image/\w+;base64,')

@app.route('/ocr', methods=['POST'])
def ocr_base64():
    try:
        data = request.get_json()
        img_base64 = data.get('image')
        
        if not img_base64:
            return jsonify({"code": -1, "msg": "missing image field"}), 400

        img_base64 = pattern.sub('', img_base64)
        img_bytes = base64.b64decode(img_base64)
        result = ocr.classification(img_bytes)

        return jsonify({
            "code": 0,
            "data": result,
            "msg": "success"
        })

    except Exception as e:
        return jsonify({"code": -1, "msg": str(e)}), 400

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080, help='Server port')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=False)
