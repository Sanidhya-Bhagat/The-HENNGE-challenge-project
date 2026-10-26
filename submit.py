import hmac, hashlib, struct, time, base64, urllib.request, json

def generate_totp(secret):
    key = secret.encode('utf-8')
    t = int(time.time()) // 30
    msg = struct.pack('>Q', t)
    h = hmac.new(key, msg, hashlib.sha512).digest()
    offset = h[-1] & 0x0F
    code = struct.unpack('>I', h[offset:offset+4])[0] & 0x7FFFFFFF
    return str(code % 10**10).zfill(10)

def submit(email, gist_url):
    secret = email + 'HENNGECHALLENGE004'
    totp = generate_totp(secret)
    credentials = base64.b64encode(f'{email}:{totp}'.encode()).decode()
    payload = json.dumps({
        'github_url': gist_url,
        'contact_email': email,
        'solution_language': 'python'
    }).encode()
    req = urllib.request.Request(
        'https://api.challenge.hennge.com/challenges/backend-recursion/004',
        data=payload,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Basic {credentials}'
        },
        method='POST'
    )
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode())

submit('sanidhyabhagat@gmail.com', 'https://gist.github.com/Sanidhya-Bhagat/0358edb82cfc6069f7d9ad9c067cc4f9')