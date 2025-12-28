sidebar_position: 1

# K1 SDK Overview

The SpacemiT K1 platform provides multiple Software Development Kits (SDKs) designed for embedded systems, IoT devices, and robotics applications.  
Each SDK includes a Board Support Package (BSP), toolchains, sample projects, and documentation, allowing developers to select the most suitable package for their product requirements.

## Buildroot SDK

The Buildroot SDK delivers a complete Linux BSP for the SpacemiT Stone-series SoCs, including:

- OpenSBI
- U-Boot / UEFI
- Linux Kernel
- Configurable root filesystem (middleware + samples)

It is optimized for embedded scenarios that require fast, customized system builds. Developers can extend drivers and user applications with ease.

Please refer to [Buildroot User Guide](#) for details.

## OpenWrt SDK

The OpenWrt SDK is built on **OpenWrt 23.05** (with bl-v2.0.y tracking master) and integrates the full BSP for Stone-series SoCs:

- OpenSBI  
- U-Boot / UEFI  
- Linux Kernel  
- A feature-complete root filesystem optimized for networking  

It is primarily intended for soft routers, NAS systems, and network-centric embedded devices.

Please refer to [OpenWrt User Guide](#) for details.

## Bianbu SDK

**Bianbu OS** is a RISC-V optimized operating system built from Ubuntu community sources.  
It offers excellent compatibility, extensibility, and a stable environment for product development across:

- General computing  
- Smart terminals  
- Vertical-industry applications  

Please refer to [Bianbu SDK User Guide](#) for details.

## OpenHarmony SDK (K1 OH5.0)

**K1 OH5.0** is the world’s first native **RISC-V + OpenHarmony 5.0** solution.  
It runs on the K1 RISC-V AI CPU and includes:

- OpenHarmony 5.0.0.71  
- Integrated AI and LLM capabilities  
- Distributed application framework  
- Fully validated system integration  
- Complete production toolchains and documentation  

Please refer to [K1 OH5.0 User Guide](#) for details.

## ROS2 SDK (AI Robot Platform)

The **AI Robot SDK** targets next-generation intelligent robotics and is built on:

- K1 AI-enabled RISC-V SoC  
- Bianbu OS  
- ROS2 execution framework  

The solution includes:

- Integrated **MediaEngine**  
- **RVV-Opt** vector-optimized libraries  
- RDK robotics development kits  
- Pre-loaded AI models and operator toolchains  

Developers can quickly deploy applications for:

- Service robots  
- Quadruped robots  
- UAVs  
- Robotic arms  
- Autonomous mobile platforms  

Please refer to [ROS2 SDK User Guide](#) for details.

