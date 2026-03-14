# A Lightweight REST-Based Multi-Access Edge Computing Framework for 6G Networks

## Abstract / Overview
Multi-access Edge Computing (MEC) is a foundational technology for enabling ultra-low-latency services in sixth-generation (6G) networks, including applications such as extended reality, autonomous systems, and real-time industrial automation. However, many existing MEC platforms rely on heavyweight virtualization infrastructures and complex orchestration frameworks, which introduce control-plane overhead, increased service instantiation time, and higher resource consumption.

This project presents a **lightweight REST-based MEC framework** designed to reduce architectural complexity and improve performance for latency-critical 6G applications. The framework adopts a minimalist design philosophy by eliminating dependency on large orchestration stacks and exposing edge services through optimized RESTful interfaces. 

An experimental prototype was implemented and evaluated against representative heavyweight MEC deployments. The results demonstrate significant improvements in **end-to-end response latency, service instantiation time, and resource utilization**, showing that lightweight MEC architectures can provide an efficient solution for latency-sensitive 6G edge computing environments.

---

## Key Features
Based on the proposed framework described in the research paper, the system provides the following capabilities:

- **Lightweight REST API Layer** for exposing MEC services through optimized HTTP endpoints  
- **Centralized Lightweight MEC Manager** for service lifecycle management  
- **In-memory Service Registry** to store and manage service metadata efficiently  
- **Direct Service Execution Model** using lightweight processes or minimal containers  
- **Reduced Control-Plane Complexity** by eliminating large orchestration frameworks  
- **Performance Monitoring Module** to track latency, resource usage, and service performance  
- **Optimized Service Lifecycle Operations** including service registration, discovery, invocation, and monitoring  

---

## System Architecture

The proposed framework is designed with a **minimalist architecture** to reduce system overhead and improve response time. The architecture consists of four main components:

### 1. REST API Layer
The REST API layer provides external access to MEC services through lightweight HTTP endpoints. It supports operations such as:

- Service registration  
- Service discovery  
- Service invocation  
- Service health monitoring  

This layer typically runs on a lightweight web server to minimize request processing overhead.

---

### 2. Lightweight MEC Manager
The MEC Manager acts as the **central control component** of the framework. Its responsibilities include:

- Managing service metadata  
- Handling lifecycle operations such as start, stop, and restart  
- Maintaining an in-memory registry of available services  

Unlike traditional MEC systems, this manager operates without dependency on full orchestration engines.

---

### 3. Service Execution Environment
Edge applications are deployed in a simplified execution environment where services run as:

- Lightweight processes  
- Minimal containers without orchestration frameworks

This approach reduces cold-start delays and minimizes system resource overhead.

---

### 4. Monitoring and Measurement Module
A built-in monitoring component continuously tracks system performance using metrics such as:

- Service instantiation time  
- End-to-end response latency  
- CPU utilization  
- Memory consumption  

These metrics enable quantitative evaluation of the framework’s efficiency.

---

## Methodology

The project follows a structured experimental methodology to evaluate the effectiveness of the lightweight MEC framework.

### REST-Based Approach
The framework adopts a **REST-first architecture**, where all MEC services are exposed and managed through RESTful APIs. This approach simplifies communication between components and reduces intermediate layers in the service execution pipeline.

### 6G Integration Context
The framework is designed specifically for **latency-critical 6G applications**, where rapid service execution and minimal system overhead are essential. By removing complex orchestration layers and minimizing control-plane interactions, the system improves response times and resource efficiency at the network edge.

### Experimental Workflow
The methodology includes the following steps:

1. **Prototype Development**
   - Implementation of REST APIs for service lifecycle management
   - Integration of a lightweight service execution model

2. **Baseline System Setup**
   - Configuration of a representative heavyweight MEC stack for comparison

3. **Performance Metrics Definition**
   - End-to-end response latency  
   - Service instantiation time  
   - CPU utilization  
   - Memory consumption  

4. **Experimental Scenarios**
   - Single service invocation  
   - Concurrent service requests  
   - Cold-start deployment scenarios  
   - Resource-constrained environments  

5. **Comparative Performance Analysis**
   - Evaluation of the lightweight framework against the baseline MEC system.

---

## Prerequisites / Tools

The prototype implementation described in the paper utilizes the following tools and technologies:

- **Python-based Web Frameworks**
  - FastAPI
  - Flask

- **Go-based HTTP Server** (for lightweight REST endpoints)

- **Linux Environment**
  - Ubuntu 22.04

- **Hardware Configuration**
  - 8-core CPU
  - 16 GB RAM

- **Baseline MEC Deployment**
  - Kubernetes-based MEC stack for comparison

---

## Performance Highlights

Experimental evaluation demonstrates notable improvements compared to a Kubernetes-based MEC deployment:

- **43.1% reduction in end-to-end latency**
- **71.1% improvement in service instantiation time**
- **28% reduction in CPU utilization**
- **35% reduction in memory consumption**

These results highlight the efficiency of the lightweight framework for latency-sensitive edge computing applications.

---

## Conclusion

This project demonstrates that simplifying MEC architecture through a **REST-based lightweight framework** can significantly improve performance in 6G edge computing environments. By reducing control-plane complexity and minimizing orchestration overhead, the proposed system achieves faster service deployment, lower latency, and improved resource efficiency.

The framework provides a practical alternative for **latency-critical applications** where performance and efficiency are more important than large-scale orchestration capabilities.

---

## Future Work

Future research directions include:

- Implementing lightweight horizontal scaling mechanisms  
- Supporting distributed coordination across multiple edge nodes  
- Integrating AI-based task scheduling for intelligent resource allocation  
- Improving compatibility with ETSI MEC APIs  
- Evaluating performance in real-world 6G testbed environments  
- Incorporating lightweight security mechanisms for service protection  

---

## Authors

- **Chandru V** – Saveetha Engineering College  
- **Santhakumar M** – Saveetha Engineering College  
- **Sakthivel B** – Saveetha Engineering College  

---

## Keywords

Multi-access Edge Computing, 6G Networks, REST Architecture, Edge Computing, Ultra-Low Latency, Lightweight Framework, Service Orchestration, Latency-Critical Applications.
