# K3 Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/chip/K3/K3_brief_en.pdf)**

## Overview

**K3 is a high-performance RISC-V AI CPU capable of running 30B large models.**

SpacemiT K3 series chips adopt RISC-V homogeneous integrated computing technology, integrating 8 high-performance computing X100 cores and 8 ultra-wide parallel AI computing A100 cores developed by SpacemiT, which provide 130 KDMIPS of general computing power and 60 TOPS of general AI computing power, and can smoothly run 30-billion-parameter models.
The K3 series chips are mainly used in AI consumer hardware, such as AI smart home devices, AI-powered conference and office solutions, AI content creation tools, AI-driven e-commerce and retail systems, and other fields. 

- **Exceptional CPU Performance**
  8 high-performance X100 cores, up to 2.4 GHz, delivering 130 K DMIPS
  RVA23 profile compliant, with single-core SPECint2006 > 9.0/GHz (comparable to Arm Cortex-A76)

- **General-Purpose AI Performance**
  Up to 60 TOPS AI performance, supporting BF16, FP16, FP8, INT8, and INT4
  Runs local 30B models smoothly, reaching ~84% of 235B model capability

- **Latest RISC-V Architecture for Massive Parallelism**
  A100 supports up to 1024-bit RVV 1.0 vector processing
  Dedicated TCM and DMA acceleration

- **Rich I/O Expansion**
  Multiple high-speed interfaces for diverse workloads
  Supports 8-lane PCIe, 4x USB 3.0 ports, and 4x GMAC

- **Full Hardware Virtualization**
  Supports RV Hypervisor 1.0, AIA, and RV IOMMU extensions
  Enables virtualization across CPU, memory, interrupts, and I/O

- **Enhanced Security**
  Supports M/S/U privilege levels with hardware protection against Spectre/Meltdown-class attacks
  Supports SM2/3/4 cryptographic standards

- **Industrial-Grade Standards**
  Stable operation from –40°C to 85°C for demanding environments

## Features

- **High-Performance RISC-V Processor**
  - 8× X100™ 64-bit RISC-V AI processor cores
  - X100™ is a quad-issue, out-of-order high-performance core
  - 8 MB shared L2 cache per 8-core cluster
- **60TOPS General-Purpose AI Compute**
  - 8-core A100™ delivers up to 60 TOPS AI performance
  - Model throughput > 10 Tokens/s @ 30B
  - Supports FP16, BF16, FP8, INT8, and INT4 data formats
  - Supports all AI algorithms and model deployment
- **RISC-V Hardware Virtualization**
  - RVH 1.0 extension for CPU and memory virtualization
  - RV AIA extension for interrupt virtualization
  - RV IOMMU extension for device virtualization
- **RISC-V Security Architecture**
  - Supports RISC-V PMP & ePMP, combined with IOPMP for high-level security protection
  - Secure boot, secure storage & signature verification
  - Hardware acceleration for AES / SHA / RSA / SM2 / SM3 / SM4
  - Full product lifecycle security management support
- **Memory**
  - 64-bit LPDDR5 - 6400Mbps
  - 64-bit LPDDR4x - 4266Mbps
  - Up to 32 GB capacity, with bandwidth up to 51 GB/s
- **Storage**
  - SPI flash
  - eMMC 5.1
  - UFS 2.2
  - SDIO 3.0 SD card
  - SSD support: NVMe over PCIe
- **Real-Time RISC-V Processor**
  - Dual-core RT24™ 64-bit RISC-V real-time processor
  - Six-stage in-order pipeline per core
- **Multimedia and Display**
  - Integrated 3D graphics engine supporting Vulkan, OpenCL, and OpenGLES
  - 4K 120fps decoding for H.265, H.264, VP9, and other formats
  - 4K 60fps encoding for H.265, H.264, and other formats
  - Dual 3840×2160@60fps display outputs
  - MIPI-DSI 8-lane display output, 4.5Gbps/lane, supporting:
    - 3840*2160@60fps
    - 2560*1440@90fps
    - 1920*1080@60fps, etc.
  - Dual DP/eDP display outputs, supporting
    - 3840*2160@60fps
    - 2560*1440@144fps, etc.
  - 4× MIPI-CSI, 12 lanes: 4 + 4 + (2 + 2)
  - Supports up to 12 camera inputs
- **Interfaces**
  - 8× PCIe lanes (8Gbps per lane), across 5 PCIe controllers
    - PCIe x8 supports both RC and EP modes
    - Hot-plug supported
  - 3× USB 3.0 Host (combo with PCIe, includes USB 2.0)
  - 1× USB 3.0 DRD (Type-C, includes USB 2.0 OTG)
  - 1× USB 2.0 Host
  - 4× GMAC (RGMII & RMII & MII)
    - TSN protocol support
  - 6× SPI, 2× eSPI, 17× UART, 10× CAN-FD, 9× I2C, 30× PWM
- **Power**
  - TDP: 15W–25W

## Block Diagram

![](./static/k3_block_diagram.png)
