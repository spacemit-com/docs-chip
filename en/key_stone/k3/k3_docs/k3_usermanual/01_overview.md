---
sidebar_position: 2
---

# 1. Overview

## 1.1 Introduction

SpacemiT K3 series chips adopt RISC-V homogeneous integrated computing technology, integrating 8 high-performance computing large cores X100 and 8 ultra-wide parallel computing AI cores A100 developed by SpacemiT, which can provide 130 KDMIPS general computing power and 60 TOPS general AI computing power, and can smoothly run 30 billion parameter models.
The K3 series chips are mainly used in AI consumer hardware, such as AI smart home devices, AI-powered conference and office solutions, AI content creation tools, AI-driven e-commerce and retail systems, and other fields.

## 1.2 General Features

**Processor Subsystem**  

- 8 × X100™ 64-bit RISC-V cores (quad-issue, out-of-order)  
- Total CPU performance: 130 KDMIPS  
- SpecINT2006 > 9.0 per GHz; max frequency 2.4 GHz  
- Shared 8 MB L2 cache across 8 cores  

**AI Computing Subsystem**  

- 8 × A100™ AI cores providing 60 TOPS of compute power  
- Supports inference for models up to 30B parameters (>10 tokens/s @ 30B)  
- Compliant with RVV 1.0, RVA23, and Vector Crypto standards  
- Compatible with general CPU programming paradigm (no conversion overhead)  

**Memory Subsystem**  

- 64-bit LPDDR5 (6400 Mbps) / LPDDR4x (4266 Mbps)  
- Up to 32 GB capacity, 51 GB/s peak bandwidth  

**Real-Time Subsystem**  

- Dual-core RT24™ 64-bit RISC-V processor  
- Six-stage in-order pipeline per core  

**Virtualization and Security**  

- Supports RVH 1.0, AIA, and IOMMU extensions for CPU, memory, and I/O virtualization  
- Hardware-level protection against speculative attacks (Spectre, Meltdown)  
- Supports RISC-V PMP, ePMP, and IOPMP security frameworks  
- Secure boot, secure storage, and signature verification  
- Cryptographic algorithms: AES, SHA, RSA, SM2, SM3, SM4  
- Product lifecycle security management  

**Storage Interfaces**  

- SPI flash, eMMC 5.1, UFS 2.2, SDIO 3.0, NVMe over PCIe  

**Multimedia and Display**  

- Integrated 3D graphics engine supporting Vulkan, OpenCL, OpenGL ES  
- 4K@180 fps decoding and 4K@90 fps encoding (H.265/H.264/VP9)  
- Dual 3840×2160@60fps display outputs via MIPI-DSI (8-lane, 4.5 Gbps/lane) or DP/eDP  
  > Note: DPU0 supports MIPI-DSI or DP/eDP; DPU1 supports DP/eDP only.
- 4 × MIPI-CSI interfaces (12 lanes total), supporting up to 12 camera inputs  

**Connectivity and I/O**  

- 8 × PCIe Gen3 lanes (8 Gbps/lane) with RC & EP modes, hot-plug supported  
- 3 × USB 3.0 Host, 1 × USB 3.0 DRD (Type-C), 1 × USB 2.0 Host  
- 4 × GMAC (RGMII, RMII, MII) with TSN protocol support  
- 6 × SPI, 2 × eSPI, 17 × UART, 10 × CAN-FD, 9 × I²C, 30 × PWM  

**Power**  

- TDP: 15–25 W  

**Environmental and Reliability**  

- Operating temperature: –40 °C to +85 °C (industrial grade)

## 1.3 Block Diagram

<img src="./static/k3_block_diagram.png" alt="K3 Block Diagram" width="800">