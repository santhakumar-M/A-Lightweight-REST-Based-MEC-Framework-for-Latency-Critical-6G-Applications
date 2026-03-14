
import requests
import time
import json
import sys

# Configuration
BASE_URL = "http://localhost:8000/api/v1"

def log(step, message):
    print(f"[{step}] {message}")

def check_health():
    """Check if the MEC Server is running."""
    try:
        response = requests.get("http://localhost:8000/")
        if response.status_code == 200:
            log("HEALTH", "Server is active!")
            return True
    except requests.exceptions.ConnectionError:
        log("ERROR", "Connection refused. Is main.py running?")
        return False
    return False

def register_service(name, command, description):
    """Register a new service with the MEC Manager."""
    url = f"{BASE_URL}/services"
    payload = {
        "name": name,
        "command": command,
        "description": description
    }
    
    log("REGISTER", f"Registering service '{name}' -> '{command}'...")
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        log("SUCCESS", f"Service Registered: {json.dumps(data, indent=2)}")
        return True
    else:
        log("ERROR", f"Registration Failed: {response.text}")
        return False

def list_services():
    """Fetch all available services."""
    url = f"{BASE_URL}/services"
    response = requests.get(url)
    services = response.json()
    log("DISCOVERY", f"Available Services: {[s['name'] for s in services]}")

def invoke_service(name, args):
    """Invoke a service and measure client-side latency."""
    url = f"{BASE_URL}/services/{name}/invoke"
    payload = {
        "args": args,
        "timeout": 10
    }
    
    log("INVOKE", f"Calling '{name}' with args {args}...")
    
    # Measure Client-Side Latency (End-to-End)
    start_time = time.time()
    response = requests.post(url, json=payload)
    end_time = time.time()
    
    client_latency = end_time - start_time
    
    if response.status_code == 200:
        data = response.json()
        overhead = data.get('overhead_latency', 0)
        execution = data.get('execution_time', 0)
        
        print("\n--- Execution Result ---")
        print(f"Status:      {data['status']}")
        print(f"Stdout:      {data['stdout'].strip()}")
        print(f"Latency Analysis:")
        print(f"  1. Client E2E:       {client_latency:.6f} sec")
        print(f"  2. Service Exec:     {execution:.6f} sec")
        print(f"  3. MEC Overhead:     {overhead:.6f} sec")
        print("------------------------\n")
    else:
        log("ERROR", f"Invocation Failed: {response.text}")

def main():
    if not check_health():
        sys.exit(1)

    # 1. Register a Service (Control Plane)
    # We'll use 'python --version' as a simple service
    if register_service("version-service", "python", "Checks python version"):
        
        # 2. Discovery
        list_services()
        
        # 3. Invoke (Data Plane)
        invoke_service("version-service", ["--version"])
        
        # 4. Invoke another logical service
        # Let's verify 'whoami' (works on most *nix/windows via subprocess if shell=False/executable exists)
        # On windows 'whoami' is an executable.
        register_service("identity-service", "whoami", "Returns current user")
        invoke_service("identity-service", [])

if __name__ == "__main__":
    main()
