from flask import Flask, request, render_template, send_from_directory
from netmiko import ConnectHandler
import threading
import os
from datetime import datetime

app = Flask(__name__)
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

results = {}

def run_commands_on_device(ip, vendor, cmd_type, commands):
    device = {
        'device_type': vendor,
        'host': ip,
        'username': 'admin',     # Replace with your actual username
        'password': 'admin123',  # Replace with your actual password
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
        output = f"Connection to {ip} failed: {str(e)}"

    # Save output to a file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{ip}_{timestamp}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w") as f:
        f.write(output)

    results[ip] = filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    ip_list = request.form['ips'].splitlines()
    vendor = request.form['vendor']
    cmd_type = request.form['cmd_type']
    commands = request.form['commands'].splitlines()

    threads = []
    global results
    results = {}

    for ip in ip_list:
        ip = ip.strip()
        if ip:
            t = threading.Thread(target=run_commands_on_device, args=(ip, vendor, cmd_type, commands))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    # Generate output HTML
    html_output = "<h2>Command Execution Results</h2><ul>"
    for ip, file_name in results.items():
        html_output += f"<li>{ip} - <a href='/output/{file_name}' target='_blank'>Download Output</a></li>"
    html_output += "</ul><br><a href='/'>Back to Home</a>"

    return html_output

@app.route('/output/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
