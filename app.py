from flask import Flask, render_template_string

app = Flask(__name__)

commands = [
    # Anonymous Browsing
    {"category": "Anonymous Browsing", "title": "Tor Browser", "command": "torbrowser-launcher", "description": "Launch the Tor Browser."},
    {"category": "Anonymous Browsing", "title": "ProxyChains Firefox", "command": "proxychains firefox duckduckgo.com", "description": "Firefox via proxychains."},

    # Network Privacy
    {"category": "Network Privacy", "title": "MAC randomize", "command": "macchanger -r eth0", "description": "Random MAC address."},
    {"category": "Network Privacy", "title": "MAC show", "command": "macchanger -s eth0", "description": "Show MAC address."},

    # File Protection
    {"category": "File Protection", "title": "GPG Encrypt", "command": "gpg -c filename.txt", "description": "Encrypt file with password."},
    {"category": "File Protection", "title": "ZIP Encrypt Folder", "command": "zip -re archive.zip folder/", "description": "Password-protect folder."},
    {"category": "File Protection", "title": "Shred File", "command": "shred -u filename.txt", "description": "Securely delete file."},

    # System Anonymity
    {"category": "System Anonymity", "title": "Anonsurf Start", "command": "anonsurf start", "description": "Route all traffic via Tor."},
    {"category": "System Anonymity", "title": "Anonsurf Stop", "command": "anonsurf stop", "description": "Restore default network."},

    # Network Monitoring
    {"category": "Network Monitoring", "title": "Wireshark", "command": "wireshark", "description": "Packet capture and inspection."},
    {"category": "Network Monitoring", "title": "iftop", "command": "iftop", "description": "Live bandwidth usage."},

    # Disk Privacy
    {"category": "Disk Privacy", "title": "LUKS Encrypt", "command": "cryptsetup luksFormat /dev/sdX", "description": "Encrypt a partition."},

    # Email Privacy
    {"category": "Email Privacy", "title": "GPG Email", "command": "gpg --encrypt --armor -r user@example.com message.txt", "description": "Encrypt email with GPG."},

    # Secure Communication
    {"category": "Secure Communication", "title": "Signal App", "command": "flatpak run org.signal.Signal", "description": "Encrypted messaging."}
]

template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Kali Linux Privacy Commands</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; font-size: 0.9rem; }
        code { background-color: #eee; padding: 2px 4px; border-radius: 3px; }
        .card { height: 100%; }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 10px;
        }
        h5 { font-size: 1rem; margin-bottom: 0.5rem; }
        .card-text { margin-bottom: 0.4rem; }
    </style>
</head>
<body>
<div class="container my-3">
    <h2 class="text-center mb-3">🔐 Kali Linux Privacy Commands</h2>
    <div class="grid-container">
        {% for cmd in commands %}
        <div class="card shadow-sm p-2">
            <h5>{{ cmd.title }}</h5>
            <p class="card-text">{{ cmd.description }}</p>
            <code>{{ cmd.command }}</code>
            <button class="btn btn-sm btn-outline-secondary mt-2"
                    onclick="navigator.clipboard.writeText('{{ cmd.command }}')">Copy</button>
        </div>
        {% endfor %}
    </div>
</div>
</body>
</html>
'''

@app.route("/")
def index():
    return render_template_string(template, commands=commands)

if __name__ == "__main__":
    app.run(debug=True)
