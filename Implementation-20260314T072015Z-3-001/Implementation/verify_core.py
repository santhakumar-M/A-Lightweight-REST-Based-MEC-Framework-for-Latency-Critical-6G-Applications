
import sys
import os
import time

# Add current directory to path so we can import app
sys.path.append(os.getcwd())

from app.core import MetricsCollector, TaskExecutor, MECManager
from app.models import ServiceRegistration

def test_metrics():
    print("Testing MetricsCollector...")
    metrics = MetricsCollector.get_system_metrics()
    print(f"Metrics: {metrics}")
    assert "cpu_percent" in metrics
    assert "memory_percent" in metrics
    print("MetricsCollector Test Passed!")

def test_service_flow():
    print("\nTesting MEC Service Flow (Register -> Invoke)...")
    
    # 1. Register Service
    service_name = "test-echo"
    # Use python to print version as a cross-platform safe command
    registration = ServiceRegistration(
        name=service_name,
        command="python",
        description="Returns python version"
    )
    
    service = MECManager.register_service(registration)
    print(f"Service Registered: {service.name} -> {service.command}")
    assert service.name == service_name
    
    # 2. Invoke Service
    print(f"Invoking {service_name}...")
    response = TaskExecutor.execute_service(service, ["--version"])
    
    print(f"Invoke Response: status={response.status}")
    print(f"Execution Time: {response.execution_time:.4f}s")
    print(f"Overhead: {response.overhead_latency:.6f}s")
    
    assert response.status == "success"
    assert "Python" in response.stdout
    assert response.overhead_latency > 0
    assert response.execution_time > 0
    
    print("MEC Service Flow Test Passed!")

if __name__ == "__main__":
    try:
        test_metrics()
        test_service_flow()
        print("\nAll core tests passed.")
    except Exception as e:
        print(f"\nTests Failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
