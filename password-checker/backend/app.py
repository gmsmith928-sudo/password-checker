from flask import Flask, request, jsonify
import re
import math

app = Flask(__name__)

def score_password(pw: str) -> dict:
    length = len(pw)
    score = 0
    reasons = []
    if length >= 12: score += 40
    elif length >= 8:
        score += 20
        reasons.append("Consider using 12+ characters.")
    else:
        reasons.append("Password too short.")

    classes = sum([
        bool(re.search(r'[a-z]', pw)),
        bool(re.search(r'[A-Z]', pw)),
        bool(re.search(r'\d', pw)),
        bool(re.search(r'[^A-Za-z0-9]', pw))
    ])
    score += classes * 15
    if classes < 3:
        reasons.append("Use mixed character types.")

    low = pw.lower()
    common = ['password', '1234', 'qwerty', 'admin']
    if any(c in low for c in common):
        reasons.append("Avoid common patterns.")
        score -= 20

    score = max(0, min(100, score))
    entropy = estimate_entropy(pw)
    return {"score": score, "entropy_bits": entropy, "reasons": reasons}

def estimate_entropy(pw: str) -> float:
    pool = 0
    if re.search(r'[a-z]', pw): pool += 26
    if re.search(r'[A-Z]', pw): pool += 26
    if re.search(r'\d', pw): pool += 10
    if re.search(r'[^A-Za-z0-9]', pw): pool += 32
    if pool == 0: return 0.0
    return round(len(pw) * math.log2(pool), 2)

@app.route('/api/check', methods=['POST'])
def check_password():
    data = request.get_json() or {}
    pw = data.get("password", "")
    if not pw: return jsonify({"error":"password required"}), 400
    if len(pw) > 1000: return jsonify({"error":"too long"}), 400
    return jsonify({"ok": True, "result": score_password(pw)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
