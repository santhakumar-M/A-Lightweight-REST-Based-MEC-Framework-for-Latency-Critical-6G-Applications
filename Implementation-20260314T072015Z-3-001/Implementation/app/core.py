
import subprocess
import psutil
import time
import uuid
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
from .models import TaskResponse, Service, ServiceRegistration

logger = logging.getLogger(__name__)

# --- MEC Manager (The "Missing Middle Box" - Lightweight Registry) ---
class MECManager:
    _registry: Dict[str, Service] = {}

    @classmethod
    def register_service(cls, registration: ServiceRegistration) -> Service:
        service = Service(
            name=registration.name,
            command=registration.command,
            description=registration.description,
            registered_at=datetime.now()
        )
        cls._registry[registration.name] = service
        logger.info(f"Registered service: {service.name} -> {service.command}")
        return service

    @classmethod
    def get_service(cls, name: str) -> Optional[Service]:
        return cls._registry.get(name)

    @classmethod
    def list_services(cls) -> List[Service]:
        return list(cls._registry.values())

# --- Metrics & Execution ---
class MetricsCollector:
    @staticmethod
    def get_system_metrics() -> Dict[str, Any]:
        return {
            "cpu_percent": psutil.cpu_percent(interval=None),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('/').percent,
            "net_io": psutil.net_io_counters()._asdict()
        }

class TaskExecutor:
    @staticmethod
    def execute_service(service: Service, args: List[str], timeout: int = 30) -> TaskResponse:
        # Timestamp 1: Request fully processed by logic (approx received time)
        received_at = time.time()
        
        task_id = str(uuid.uuid4())
        cmd = [service.command] + args
        
        logger.info(f"Invoking service {service.name} (Task {task_id}): {' '.join(cmd)}")
        
        # Timestamp 2: About to fork/exec
        start_time = time.time()
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False
            )
            # Timestamp 3: Process finished
            end_time = time.time()
            
            status = "success" if result.returncode == 0 else "failed"
            stdout = result.stdout
            stderr = result.stderr

        except subprocess.TimeoutExpired:
            end_time = time.time()
            status = "timeout"
            stdout = ""
            stderr = "Task timed out"
        except Exception as e:
            end_time = time.time()
            status = "error"
            stdout = ""
            stderr = str(e)

        # precise logic: execution duration vs control plane overhead
        execution_duration = end_time - start_time
        overhead = start_time - received_at

        return TaskResponse(
            task_id=task_id,
            service_name=service.name,
            status=status,
            stdout=stdout,
            stderr=stderr,
            received_at=received_at,
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_duration,
            overhead_latency=overhead
        )
