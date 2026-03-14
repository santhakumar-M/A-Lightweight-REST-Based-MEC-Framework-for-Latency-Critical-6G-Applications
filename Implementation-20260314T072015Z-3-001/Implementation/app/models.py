
from pydantic import BaseModel
from typing import List, Optional, Any, Dict
from datetime import datetime

# Service Lifecycle Models
class ServiceRegistration(BaseModel):
    name: str
    command: str
    description: Optional[str] = None

class Service(BaseModel):
    name: str
    command: str
    registered_at: datetime
    description: Optional[str] = None

class ServiceInvocation(BaseModel):
    args: List[str] = []
    timeout: int = 30

class TaskResponse(BaseModel):
    task_id: str
    service_name: str
    status: str
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    
    # Latency Breakdown (Critical for Paper)
    received_at: float
    start_time: float
    end_time: float
    execution_time: float
    overhead_latency: float # received_at -> start_time

class SystemMetrics(BaseModel):
    cpu_percent: float
    memory_percent: float
    disk_usage: float
    net_io: Dict[str, Any]
