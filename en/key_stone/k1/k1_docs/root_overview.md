sidebar_position: 1

# K1 Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/chip/K1/K1_brief_en.pdf)**

## Overview

K1 Series: 8-Core 64-bit RISC-V AI CPU

The K1 series leverages homogenous fusion computing technology, integrating eight high-performance X60™ computing cores developed by SpacemiT. It delivers 50 KDMIPS of general computing power and 2 TOPS of AI computing power, enabling seamless operation of local large models such as 0.5B and 1B parameters.

The K1 series chips are primarily designed for applications in AI edge computing, AI-integrated hardware, intelligent robotics, industrial main control systems, cloud computing and open-source Harmony OS among others.

- **Outstanding CPU performance**
8-core RISC-V AI CPU, delivering 50 KDMIPS of CPU computing power, with single-core CPU performance SPECint®2006 > 4.0/GHz

- **Homogeneous AI integration, superior LLM performance**
Delivers 2 TOPS AI power via parallel AI-CPU cores, integrating swiftly with major AI ecosystems. Large model performance > 10 Tokens/S @ 1B local model

- **Latest RISC-V architecture, robust parallel computing power**
Support of RVA22 Profile and 256-bit RVV 1.0 standard RISC-V CPU, offering double the parallel processing power of Neon, with vector performance exceeding ARM NEON by over 150%

- **Top-tier energy efficiency**
The streamlined RISC-V architecture and advanced micro-architecture design reduce power consumption to 80% of comparable chips under the same workload.

- **Rich I/O capabilities**
Integrated with multiple PCIe, USB, GMAC and SPI interfaces, offering comprehensive peripheral connectivity options.

- **Industrial standards compliance**
The CPU delivers stable and reliable computing power from -40°C to 85°C, complying  the demanding requirements of industrial applications.

## Key Features

- **Processor**
  - Latest RVA22 profile architecture
  - 8-core X60™ 64-bit AI processor
  - 8-stage dual-issue in-order pipeline
  - Support of 256-bit RVV1.0 standard
  - CPU integrated with 2.0 TOPS AI performance
  - Shared 1MB L2 cache across 8 cores

- **RISC-V integrated AI technology**
  - AI-CPU with 2.0 TOPS AI performance
  - Capable of > 10 Tokens/S @1B for LLMs
  - Support of all AI algorithms and models, including all LLMs
  - Follow of CPU programming paradigms, enabling zero-cost AI deployment

- **RISC-V security architecture** 
  - Support of RISC-V PMP & ePMP security extensions
  - Support of secure boot, storage and signature verification
  - Support of algorithms AES, SHA, RSA
  - Support of product lifecycle security management

- **RCPU**
  - RISC-V real-time CPU with 300MHz clock speed
  - Support of heterogeneous dual system

- **Memory**
  - 32-bit LPDDR4/LPDDR4X, up to 2400MT/s
  - Support of up to 16GB, with bandwidth up to 10.6GB/s

- **Storage**
  - Support of SPI flash
  - Support of eMMC 5.1
  - Support of SDIO 3.0 SD cards
  - Support of SSD: NVMe over PCIe

- **Multimedia & Display**
  - Support of 3D graphics engine: OpenCL 3.0, OpenGLES 1.1/3.2, Vulkan 1.3
  - Support of 4K H.265/H.264/VP9/VP8 codec formats
  - Support of dual displays with independent output, up to 1920×1440@60fps 
    - Output via MIPI-DSI or HDMI
  - Support of triple camera input, with a single camera up to 16MP 
    - MIPI-CSI 8 Lanes (4+2+2 or 4+4)

- **Interfaces**
  - 5× PCIe 2.1 (x2 + x2 + x1 configuration, 5Gbps per lane)
  - 1× USB 3.0 (combo with PCIe 2.1 x1)
  - 2× USB 2.0 (OTG + Host)
  - 2× GMAC (RGMII & 1000M)
  - 4× SPI, 7× I2C, 12× UART, 2× CAN-FD, 30× PWM

- **GPIO**
  - 24× GPIO 3.3V
  - 104× GPIO 1.8V

- **Operating system**
  - Bianbu OS
  - Mainstream Linux OS distributions
  - RTOS

- **Package**
  - Two packages available (pin-to-pin):
    - FCCSP, 17×17mm, 0.65mm pin pitch
    - FCBGA, 19×19mm, 0.65mm pin pitch

- **Power consumption** 
  - TDP 3～5W

## Block Diagram

![](./static/k1_blockdiagram.png)
