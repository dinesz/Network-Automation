from flask import Flask, request, render_template, send_from_directory
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import os

app = Flask(__name__)
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

MAX_THREADS = 100

def run_commands_on_device(ip, vendor, cmd_type, commands):
    device = {
        'device_type': vendor,
        'host': ip,
        'username': 'admin',     # 🔁 Customize for your environment
        'password': 'admin123',  # 🔁 Customize for your environment
    }

    try:
        connection = ConnectHandler(**device)
        output = ""

        if cmd_type == "show":
            for cmd in commands:
                output += f"\n> {cmd}\n{connection.send_command(cmd)}\n"
        elif cmd_type == "config":
            output = connection.send_config_set(commands)

        connection.disconnect()
    except Exception as e:
        output = f"[ERROR] {ip}: {str(e)}"

    # Save output to file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{ip.replace('.', '_')}_{timestamp}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w") as f:
        f.write(output)

    return ip, filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    ip_list = [ip.strip() for ip in request.form['ips'].splitlines() if ip.strip()]
    vendor = request.form['vendor']
    cmd_type = request.form['cmd_type']
    commands = [cmd.strip() for cmd in request.form['commands'].splitlines() if cmd.strip()]

    results = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {
            executor.submit(run_commands_on_device, ip, vendor, cmd_type, commands): ip
            for ip in ip_list
        }

        for future in as_completed(futures):
            try:
                ip, filename = future.result()
                results.append((ip, filename))
            except Exception as e:
                results.append((futures[future], f"[ERROR] Thread failed: {str(e)}"))

    html_output = "<h2>Automation Results</h2><ul>"
    for ip, filename in results:
        if filename.endswith(".txt"):
            html_output += f"<li>{ip}: <a href='/output/{filename}' target='_blank'>View Output</a></li>"
        else:
            html_output += f"<li>{ip}: {filename}</li>"
    html_output += "</ul><br><a href='/'>⬅ Back</a>"

    return html_output

@app.route('/output/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
