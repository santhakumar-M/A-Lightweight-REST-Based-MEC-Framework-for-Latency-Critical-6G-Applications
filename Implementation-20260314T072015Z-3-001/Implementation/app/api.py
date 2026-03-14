
from fastapi import APIRouter, HTTPException, Path
from typing import List
from .models import ServiceRegistration, Service, ServiceInvocation, TaskResponse, SystemMetrics
from .core import MetricsCollector, TaskExecutor, MECManager

router = APIRouter()

# --- System Metrics ---
@router.get("/metrics", response_model=SystemMetrics)
async def get_metrics():
    """Get current system metrics (CPU, Memory, Disk, Net)."""
    try:
        data = MetricsCollector.get_system_metrics()
        return SystemMetrics(**data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- MEC Service Management ---
@router.post("/services", response_model=Service)
async def register_service(registration: ServiceRegistration):
    """Register a new MEC service."""
    return MECManager.register_service(registration)

@router.get("/services", response_model=List[Service])
async def list_services():
    """List all registered services."""
    return MECManager.list_services()

@router.post("/services/{name}/invoke", response_model=TaskResponse)
async def invoke_service(
    invocation: ServiceInvocation,
    name: str = Path(..., description="The name of the service to invoke")
):
    """
    Invoke a registered service.
    This calculates precise latencies: Overhead vs Execution.
    """
    service = MECManager.get_service(name)
    if not service:
        raise HTTPException(status_code=404, detail=f"Service '{name}' not found")
        
    return TaskExecutor.execute_service(service, invocation.args, invocation.timeout)
