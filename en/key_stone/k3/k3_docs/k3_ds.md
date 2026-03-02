---
sidebar_position: 2
---

# K3 Datasheet (Preliminary Version)

## Proprietary, Confidentiality & Disclaimer

**Copyright © 2026 SpacemiT Inc. All rights reserved.**

Without the written approval of SpacemiT (Hangzhou) Technology Co. Ltd. (hereafter SpacemiT), no individual or entity may excerpt, copy or distribute any part or all of the content of this document in any form.

The copyrights of all materials and contents set forth herein are owned by SpacemiT and/or its subsidiaries, except for those specifically indicated as reference to any other party (if any).

The content of this document may be periodically updated due to product version upgrades or other reasons. Unless otherwise specified, this document is provided solely as a user guide, and THE INFORMATION AND ADVICE PROVIDED IN THIS DOCUMENT DO NOT CONSTITUTE ANY EXPLICIT OR IMPLIED WARRANTIES. TO THE EXTENT NOT PROHIBITED BY LAW, THE COMPANY SHALL NOT BE LIABLE FOR ANY FORM OF DAMAGE CAUSED BY THIS DOCUMENT.

## Preliminary Version Notice

<span style="color: red; font-weight: bold;">This document is designated as a Preliminary Version and is provided for reference and evaluation purposes only.</span>
<span style="color: red; font-weight: bold;">The product described in this document is still under development or in the final validation stage. The specifications, parameters, performance data, and functional descriptions provided herein are preliminary and may be modified, refined, or removed prior to the release of the final version. Please refer to the revision history for the latest updates.</span>
<span style="color: red; font-weight: bold;">This document does not represent a final product specification and shall not be relied upon for production design, mass manufacturing, or commercial deployment.</span>
<span style="color: red; font-weight: bold;">SpacemiT reserves the right, at its sole discretion, to update, revise, suspend, or withdraw this document or the related product at any time without notice or liability.</span>
<span style="color: red; font-weight: bold;">Any planned release schedule, including but not limited to a potential V1.0 release date, is provided for planning reference only and does not constitute a binding commitment or contractual obligation.</span>
<span style="color: red; font-weight: bold;">Nothing in this document shall be interpreted as a commercial offer, product roadmap commitment, or legally binding technical specification.</span>

## Disclaimer of Warranties

Unless otherwise expressly agreed in writing, the information provided in this document is supplied “AS IS”.
SpacemiT makes no warranties of any kind, whether express, implied, statutory, or otherwise, including but not limited to warranties of merchantability, fitness for a particular purpose, non-infringement, or performance.
This document is provided for informational purposes only and does not create any contractual rights or obligations.

## Limitation of Liability

To the maximum extent permitted by applicable law, SpacemiT shall not be liable for any direct, indirect, incidental, special, consequential, exemplary, or punitive damages arising out of or related to:
- the use of this document,
- reliance on the information contained herein,
- or the design, development, manufacture, or use of any product based on this document.

Users assume all risks associated with the use of the information provided herein.

## Revision History

> The revision history below is provided for reference only. Specifications remain subject to change without notice.

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">
  <colgroup>
    <col width="200">
    <col width="200">
    <col width="600">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Version</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Date</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Notes</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;"><b>V0.9.1</b></td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">2026.03.02</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">Pinout subsection Multi-Function Pin Register has been removed as part of ongoing specification refinement.</td>
    </tr>
        <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;"><b>V0.9</b></td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">2026.02.28</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">Initial Preliminary release</td>
    </tr>
  </tbody>
</table>

---

## 1. Overview

### 1.1 Introduction

SpacemiT K3 series chips adopt RISC-V homogeneous integrated computing technology, integrating 8 high-performance computing large cores X100 and 8 ultra-wide parallel computing AI cores A100 developed by SpacemiT, which can provide 130 KDMIPS general computing power and 60 TOPS general AI computing power, and can smoothly run 30 billion parameter models.
The K3 series chips are mainly used in AI consumer hardware, such as AI smart home devices, AI-powered conference and office solutions, AI content creation tools, AI-driven e-commerce and retail systems, and other fields.

### 1.2 General Features

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

- SPI Flash, eMMC 5.1, UFS 2.2, SDIO 3.0, NVMe over PCIe  

**Multimedia and Display**  

- Integrated 3D graphics engine supporting Vulkan, OpenCL, OpenGL ES  
- 4K 120 fps decoding and 4K 60 fps encoding (H.265/H.264/VP9)  
- Dual 3840×2160@60fps display outputs via MIPI-DSI (8-lane, 4.5 Gbps/lane) and DP/eDP  
- 4 × MIPI-CSI interfaces (12 lanes total), supporting up to 12 camera inputs  

**Connectivity and I/O**  

- 8 × PCIe Gen3 lanes (8 Gbps/lane) with RC & EP modes, hot-plug supported  
- 3 × USB 3.0 Host, 1 × USB 3.0 DRD (Type-C), 1 × USB 2.0 Host  
- 4 × GMAC (RGMII, RMII, MII) with TSN protocol support  
- 6 × SPI, 2 × eSPI, 17 × UART, 10 × CAN, 9 × I²C, 30 × PWM  

**Power**  

- TDP: 15–25 W  

**Environmental and Reliability**  

- Operating temperature: –40 °C to +85 °C (industrial grade)

## 1.3 Block Diagram

<img src="static/k3_block_diagram.png" alt="K3 Block Diagram" width="800">

## 2. Specifications

### 2.1 CPU Subsystem

#### 2.1.1 SpacemiT® X100™ RISC-V Core

**Introduction**  
The SpacemiT® X100™ is a high-performance, 4-issue, out-of-order, multi-core, multi-cluster RISC-V RVA23 processor optimized for demanding compute scenarios such as servers, autonomous driving systems, and cloud AI inference platforms.  
Designed for both performance and robustness, the X100 core provides comprehensive virtualization, strong security resilience, and RAS (Reliability, Availability, Serviceability) capabilities. These characteristics make it a powerful and scalable solution for data-centric and mission-critical applications.

**Features**  
- Compliance: Fully compliant with RISC-V RVA23 standards  
- Cache Architecture:  
  - 64KB L1 I-Cache and 64KB L1 D-Cache per core  
  - 4MB L2 Cache per cluster  
  - L1 D-Cache supports MESI coherence protocol  
  - L2 Cache supports MOESI coherence protocol  
- Vector Extension: RVV 1.0, VLEN = 256  
- Hypervisor Extension: RVH 1.0, GEILEN = 8  
- Advanced Interrupt Architecture (AIA):  
  - M-mode MSI: 512  
  - S-mode MSI: 512  
  - VS-mode MSI: 64  
- Interrupt Controllers: Supports ACLINT and APLIC with a total of 512 interrupts  
- Performance Monitoring: RISC-V Performance Monitoring Unit (PMU) support  
- Virtual Memory: Supports SV39 virtual memory management  
- Security Framework:  
  - 16 PMP entries in accordance with the RISC-V security framework  
  - Supports RISC-V Debug, Trace, and RERI frameworks  
- RVA23 Optional Extensions (not included in RVA23 base specification):  
  - Vector Crypto: `zvkng`, `zvksg`  
  - Other Extensions: `zvbc`, `zfh`, `zbc`, `zvfh`, `zfbmin`, `zvfbfmin`, `zvfbfwma`  
  - System and Security: `sdtri`, `svvptc`, `sspm`, `smepmp`, `smstateen`, `smcntrpmf`  

**Block Diagram**  

<img src="static/x100_block_diagram.png" alt="" width="600">

#### 2.1.2 SpacemiT® A100™ AI Core

**Introduction**  
The SpacemiT® A100™ is an AI-first RISC-V AI-CPU that delivers native AI compute capability through the SpacemiT-IME instruction set. Its microarchitecture is specifically optimized for operator-level parallelism, memory bandwidth efficiency, and data locality, enabling highly efficient execution of real-world AI workloads.  
In addition to advanced AI acceleration, the A100 fully supports general-purpose CPU functionalities defined by the RVA23* specification and leverages a standard RISC-V unified programming model to power Small-Local Language Model (SLM) and a broad range of AI-centric applications.

**Features**  
- AI Compute Performance: 60 TOPs (@FP4 sparse)  
- RISC-V Compliance: Fully compliant with RISC-V RVA23* standards  
- Cache Architecture:  
  - 32 KB L1 I-Cache and 32 KB L1 D-Cache per core  
  - 1 MB L2 Cache per cluster  
  - 1.5 MB Scratchpad per cluster  
  - L1 D-Cache supports MESI coherence protocol  
  - L2 Cache supports MOESI coherence protocol  
- Vector Extension: RVV 1.0, VLEN = 1024  
- Advanced Interrupt Architecture (AIA):  
  - M-mode MSI: 512  
  - S-mode MSI: 512  
- Interrupt Controllers: Supports ACLINT and APLIC with a total of 512 interrupts  
- Performance Monitoring: Integrated RISC-V Performance Monitoring Unit (PMU)  
- Virtual Memory: Supports SV39 virtual memory management  
- Security Framework:  
  - 32 PMP entries compliant with the RISC-V security framework  
  - Supports RISC-V Debug and Trace  
- RVA23* Optional Extensions (not included in the RVA23 base specification):  
  - Vector Crypto: `zvkng`, `zvksg`  
  - Other Extensions: `zvbc`, `zfh`, `zbc`, `zvfh`, `zfbmin`, `zvfbfmin`, `zvfbfwma`  
  - System and Security: `sdtri`, `svvptc`, `sspm`, `smepmp`, `smstateen`, `smcntrpmf`  

> **Note**: RVA23* (in A100 AI core) does not include the Hypervisor extension.

**Block Diagram**  

<img src="static/a100_block_diagram.png" alt="" width="400">

#### RT24 RISC-V Core

**Introduction**  
The RT24 serves as the system management core within the K3 SoC. It is based on CVA6, the OpenHW Group’s open-source 64-bit RISC-V CPU, featuring a 6-stage, in-order, single-issue pipeline with RV64GC support and Unix-like operating system compatibility. Designed for high efficiency and reliability, the RT24 core provides essential control, coordination, and low-power management functions across the system.

**Features**  
- Ultra-low standby and active power consumption  
- Implements the RV64IMAFDC (RV64GC) instruction set  
- Supports three RISC-V privilege levels: M, S, and U  
- Provides virtual address translation through ITLB, DTLB, and PTW units  

**Block Diagram**  

<img src="static/rt24_block_diagram.png" alt="" width="600">

#### 2.1.4 Debug

**Introduction**  
The debugging interface serves as the channel for software to interact with the processor. Through this interface, users can access CPU registers and memory contents, as well as other on-chip device information. Additionally, tasks such as downloading programs can be performed via the debugging interface.

**Block Diagram**  
The micro-architecture of the debugging interface is depicted below.
<img src="static/debug_block_diagram.png" alt="" width="600">

As illustrated, the debugging system consists of  

- A debugging software (e.g., GDB)
- A debugging agent service (e.g., OpenOCD)
- A debugger (e.g., JTAG Debug Probe)
- A debugging interface (e.g., DTM)

These components are interconnected as follows:  

- The debugging software generally communicates with the debugging agent service over a network.
- The debugging agent service commonly interfaces with the debugger via USB.  
- The debugger interacts with the CPU through the JTAG interface  

The JTAG memory access method could be either **progbuf** or **sysbus** mode, where  

- The **progbuf** mode is a standard JTAG method that accesses memory through the CPU  
- The **sysbus** mode bypasses the CPU to access on-chip resources via the System Bus Access (SBA) port  

#### 2.1.5 Trace

**Introduction**  
The RISC-V Trace System provides a hardware–software interface for debugging and analyzing the execution trace of a hart, including details of its memory accesses.  
Once a RISC-V hart streams its program execution and memory-access trace through the ingress port defined by the RISC-V Trace Specification, an encoder compresses the data for efficient transmission.  
The trace data can then be stored on-chip, where host-side decoder software reconstructs the full execution flow, allowing developers to accurately observe the hart’s runtime behavior.

**Features**  
The trace components of the X100 and A100 cores on the K3 are fully compliant with the RISC-V N-Trace protocol and its associated interfaces — RISC-V Trace Control Interface and RISC-V Hart-to-Trace Interface.  
Key features include:

- Independent trace encoder connected to each X100/A100 core  
- Integrated ATB bridge for connection to the ATB bus  
- Support for BTM (Branch Trace Mode) compression  
- Optional message types such as ownership messages, and enables improved trace handling in complex OS environments.  
- Precise trace enable/disable control via debug triggers  
- Extended compression capabilities such as virtual address compression to further enhance trace efficiency  

**Block Diagram**
<img src="static/trace_block_diagram.png" alt="" width="600">

### 2.2 Memory & Storage

#### 2.2.1 On-Chip Memory

**Introduction**  
K3 integrates the following on-chip memory resources:
- 128 KB Boot ROM
Stores the first-stage bootloader and supports booting from multiple external media. Also supports program download via USB and UART, and enables eFuse-based secure boot.
- 512 KB SRAM
Shared by the main CPU and the RCPU.

#### 2.2.2 LPDDR4x/5

**Introduction**  
The Dynamic Memory Interface provides a high-performance, low-power connection to external LPDDR4x and LPDDR5 DRAM devices. It supports flexible configurations and dynamic frequency scaling to balance bandwidth and power efficiency across various application scenarios.

**Features**
- Supports LPDDR4x and LPDDR5 memory types:  
  - LPDDR4x data rate up to 4266 MT/s  
  - LPDDR5 data rate up to 6400 MT/s  
- Maximum Supported Memory Capacity: 32 GB  
- Supports two channels, each with a 32-bit data width  
- Each channel supports two ranks  
- Supports dynamic frequency scaling, allowing real-time frequency adjustment based on bandwidth demand to optimize power efficiency  

#### 2.2.3 Quad-SPI

**Introduction**  
The Quad-SPI interface provides communication between the SoC and external serial flash memory devices. It supports data transfer over up to four bidirectional data lines, offering high flexibility and compatibility with a wide range of flash devices.

**Features**  
- Supports XIP mode and Page mode  
- Independent 1/2/4 data width  
- Maximum clock frequency up to 102 MHz, minimum 13.25 MHz  
- Supports SPI Nor Flash and SPI Nand Flash  
- Supports 1.8 V and 3.3 V signal voltages  

#### 2.2.4 eMMC Interface

**Introduction**  
The eMMC interface functions as a host controller for the eMMC bus, enabling data transfer between the external eMMC card and the internal system bus master.

**Features**  
- Compliant with 8-bit eMMC 5.1 specification  
- Compatible with SDHCI register set, with additional vendor-specific registers  
- Supports 1-bit / 8-bit MMC and CE-ATA cards  
- Supports the following data transfer types as defined in the SDHCI specification:  
  - PIO  
  - SDMA  
  - ADMA  
  - ADMA2  
- Supports SPI mode operation for eMMC cards  
- Supports the following speed modes defined in the eMMC 5.1 specification:  
  - Legacy mode: up to 26 MB/s bandwidth, 1.8 V signal voltage  
  - High-Speed SDR: up to 52 MB/s bandwidth, 1.8 V signal voltage  
  - High-Speed DDR: up to 52 MB/s bandwidth, 1.8 V signal voltage  
  - HS200: up to 200 MB/s bandwidth, 1.8 V signal voltage  
  - HS400: up to 400 MB/s bandwidth, 1.8 V signal voltage  
- Supports hardware generation of all command and data transactions, with CRC validation  
- Equipped with a 1024-byte data FIFO buffer (2 × 512-byte data blocks)  

#### 2.2.5 SD/MMC Interface

**Introduction**  
The SD/MMC interface functions as a host controller for the SD/MMC bus, enabling data transfer between the external SD/MMC card and the internal system bus master.

**Features**  
- Compliant with 4-bit SD 3.0 UHS-I specification  
- Compatible with SDHCI register set, with additional vendor-specific registers  
- Supports 1-bit / 4-bit SD storage  
- Supports the following data transfer types as defined in the SDHCI specification:  
  - PIO  
  - SDMA  
  - ADMA  
  - ADMA2  
- Supports the following speed modes as defined in the SD 3.0 specification:  
  - Default Speed: up to 12.5 MB/s bandwidth, 3.3 V signal voltage  
  - High Speed: up to 25 MB/s bandwidth, 3.3 V signal voltage  
  - SDR12: up to 25 MHz clock, 1.8 V signal voltage  
  - SDR25: up to 50 MHz clock, 1.8 V signal voltage  
  - SDR50: up to 100 MHz clock, 1.8 V signal voltage  
  - SDR104: up to 208 MHz clock, 1.8 V signal voltage  
  - DDR50: up to 50 MHz clock, 1.8 V signal voltage  
- Supports hardware generation of all command and data transactions, with CRC validation  
- Supports read-wait control and suspend/resume functions for SD/MMC cards  
- Supports card insertion/removal detection through GPIO mode  
- Equipped with a 1024-byte data FIFO buffer (2 × 512-byte data blocks)  

#### 2.2.6 UFS Interface

**Introduction**  
The UFS (Universal Flash Storage) interface provides a high-performance, low-power mass storage solution for the SoC. It complies with the JEDEC UFS 2.2, MIPI UniPro v1.6, and MIPI M-PHY v3.0 specifications.  

The UFS supports up to 2 lanes over a serial interface, providing 2 transmit (TX) and 2 receive (RX) for full-duplex communication. It supports High-Speed Mode (HS-GEAR3) and Low-Speed Mode (PWM-GEAR1), offering high bandwidth and low latency. It supports standard SCSI command set operations and allows the system to boot directly from UFS storage.

**Features**  
- Compliance with JEDEC UFS 2.2 specification  
- Compliance with MIPI UniPro v1.6 and MIPI M-PHY v3.0 specifications  
- Support for serial interface protocol:  
  - High-Speed Mode (HS-GEAR3) with up to 2 transmit (TX) and 2 receive (RX) lanes  
  - Low-Speed Mode (PWM-GEAR1)  
- Support for standard SCSI command operations  
- Support for system booting from UFS  

### 2.3 Image Subsystem

#### 2.3.1 MIPI Camera IN Interface

**Introduction**  
The MIPI Camera IN interface integrates four MIPI-CSI2 v1.1 controllers, each equipped with four data lanes supporting a maximum transfer rate of 1.5 Gbps per lane.

**Features**  
- Configurable data lanes: 1, 2, or 4  
- Independent D-PHY Resources：  
  - CSI0 and CSI1 each have a dedicated D-PHY interface  
- Shared D-PHY Resource：  
  - CSI2 and CSI3 share one 4-lane D-PHY interface. Each supports up to 4 lanes when used independently, or up to 2 lanes per interface when operating simultaneously  
- Supported input data formats:  
  - Legacy YUV420 8-bit  
  - YUV420 8-bit  
  - RAW8  
  - RAW10  
  - RAW12  
  - Embedded data type  
- Supported data interleaving types:  
  - Data-type interleaving  
  - Virtual-channel interleaving  

**Block Diagram**
<img src="static/mipi_block_diagram.png" alt="" width="800">

#### 2.3.2 GPU

**Introduction**  
This GPU architecture is built around multi-threaded unified shading clusters featuring a high-SIMD-efficiency ALU design. It employs a tile-based deferred rendering (TBDR) pipeline that supports concurrent processing of multiple tiles, enabling high-performance 3D graphics and compute workloads.

**Features**  
- Fully compliant with major graphics and compute APIs:  
  - OpenGL ES 1.1 / 3.2  
  - EGL 1.5  
  - OpenCL 3.0  
  - Vulkan 1.3  
- Tile-Based Deferred Rendering (TBDR) for 3D graphics, with concurrent multi-tile processing  
- Programmable, high-quality image anti-aliasing  
- Fine-grained triangle culling for improved rendering efficiency  
- Support for DRM security  
- Support for GPU virtualization, with up to 8 virtual GPU instances  
- Support for multi-lane isolation technology, providing up to 8 independent lanes  
- Separate IRQs per lane/OS context  
- Optional AI acceleration cooperation when paired with a neural network accelerator  
- Multi-threaded unified shading engine supporting:  
  - Pixel shading  
  - Vertex shading  
  - Compute shader (GPGPU) workloads  
- ALU architecture optimized for high SIMD efficiency  
- Fully virtualized memory addressing with Unified Memory Architecture (UMA)  
- Fine-grained task switching, workload balancing, and power management  
- Advanced DMA-driven operation to minimize host CPU involvement  
- 128 KB system-level cache (SLC)  
- Specialized texture cache unit  
- Compressed texture decoding  
- Lossless geometry compression performed during geometry processing  
- Lossless or visually lossless framebuffer compression for reduced bandwidth usage  
- Dedicated firmware processor for GPU core management:  
  - Single-threaded design  
  - 2 KB instruction cache + 2 KB data cache  
  - Independent power island  
- On-chip performance, power, and statistics registers for system monitoring  

#### 2.3.3 V2D

**Introduction**  
V2D is a 2D hardware acceleration module that supports common 2D image operations such as format conversion, rotation, mirroring, scaling, cropping, solid fill, and alpha blending.

**Features**  

- Scaling:  
  - Upscaling up to 8×  
  - Downscaling down to 1/8×  
- Rotation & Mirroring:  
  - 0°, 90°, 180°, 270° rotation  
  - Mirror and flip operations  
- Blending & Compositing:  
  - Simple layer and background blending  
- Image Cropping  
- Solid Color Fill  
- Color Space Conversion:  
  - RGB to and from BT.601 / BT.709 (narrow and full range)  
- Maximum Resolution: 4096×2160  
- Dithering for smoother color transitions  
- Memory Management Unit (MMU) support  
- Bus Interfaces: APB3, AXI3  
- Supported Input Formats:  
  - RGB888, RGBX888, RGBA8888, ARGB8888 (optional RB swap)  
  - RGB565, RGBA5658, ARGB8565 (optional RB swap)  
  - A8 (8-bit alpha image), Y8 (8-bit grayscale)  
  - YUV420 semi-planar (UV swappable)  
  - AFBC 16×16 RGBA8888 (Layout0 split/non-split)  
  - AFBC 16×16 NV12 (Layout1 split/non-split)  
- Supported Output Formats:  
  - Same as input formats, including RGB, ARGB, A8, Y8, YUV420, and AFBC variation  

### 2.4 Video Subsystem

#### 2.4.1 Introduction  

The Video Processing Unit (VPU) is quad-core video accelerator designed to handle both decoding and encoding of multiple video standards. It includes a host CPU that runs firmware to control the hardware engine, managing tasks such as bitstream parsing, sub-block control, and error resilience.  

The VPU can operate at up to 1 GHz and supports a wide range of video standards, including H.265, H.264, VP8, VP9, MPEG4, MPEG2, and H.263. It allows simultaneous operations such as:  
- Encoding and decoding at 4K@60fps  
- H.264/H.265 encoding at 4K@60fps  
- H.264/H.265 decoding at 4K@60fps  

The video codec core performs the actual decoding and encoding for each standard using dedicated hardware logic. The Macroblock Sequencer serves as the main controller, scheduling the process flows of sub-blocks to reduce the load on the processor and simplify firmware complexity.  

Additionally, several standard-independent blocks share common logic during operation, ensuring high efficiency and streamlined performance across different video standards.

#### 2.4.2 Video Encoder

**Encoding Features**  
- Configurable Arm Frame Buffer Compression (AFBC) 1.0 or 1.2 for input  
- Supports YUV422 and YUV420 AFBC block splitting (16 × 16)  
- Supports stride (not applicable to AFBC input formats)  
- Horizontal and vertical mirroring (not applicable to AFBC input formats)  
- Optional source frame rotation in 90° steps before encoding (not applicable to AFBC input formats)  

> **Note:** If YUV422 is rotated by 90° or 270° without conversion to YUV420, the output will be converted to YUV440  

**Supported Source-Frame Input Formats**  

- 1-plane YUV422, scan-line format, interleaved in YUYV or UYVY order  
  > **Note:** YUV422 input can be converted to YUV420  
- 1-plane RGB (8-bit), byte-address order: RGBA, BGRA, ARGB, ABGR  
- 2-plane YUV420, scan-line format, with chroma interleaved in UV or VU order  
- 3-plane YUV420, scan-line format  
  > **Note:** Supported for testing purposes only; not recommended for optimal performance  
- AFBC YUV422  
- AFBC YUV420  

**Supported Encoding Formats**  
- HEVC（H.265）Main Profile  
- HEVC (H.265) Main 10 Profile
- H.264 Baseline Profile（BP）  
- H.264 Main Profile（MP）  
- H.264 High Profile（HP）  
- VP8  
- VP9 Profile 0
- JPEG, baseline sequential

**HEVC (H.265) Encoding Features**
- Output bitstream compliant with HEVC Main Profile
- Encoding performance: Up to 4K@60 fps
- Maximum frame size: 4096 × 4096 pixels
- Bit depth: 8-bit, supporting I, P, and B frames
- Supports Tiled Mode, up to 4 tiles (horizontal split only)
- Motion Estimation (ME) with search range:
  - Horizontal: ±128 pixels & Vertical: ±64 pixels
  - Precision: Supports down to 1/4-pixel (QPEL) accuracy
- Intra Prediction Modes:
  - Luma: 8×8, 16×16, 32×32
  - Chroma: 4×4, 8×8, 16×16
- Inter Prediction Modes: 8×8, 16×16, 32×32
- Transform Sizes
  - Luma: 8×8, 16×16, 32×32
  - Chroma: 4×4, 8×8, 16×16
- Supports Deblocking Filter
- Quantization modes: fixed QP, or leaky bucket model–based rate control (based on target bitrate and buffer size)
- Supports Long-Term Reference (LTR) frames
- Supports slice insertion at CTU-row granularity

> **Note**: The encoder does not enforce a maximum bit constraint per CTU.

**H.264 Encoding Features**  
- Encoded bitstream compliant with Baseline, Main, and High Profiles  
- Encoding performance: Up to 4K@60 fps
- Maximum frame size: 4096 × 4096 pixels  
- Frame types: Supports I, P, and B frames  
- Entropy coding: CABAC or CAVLC  
  > **Note:** B frames are not supported by CAVLC  
- Motion Estimation (ME) with search range:
  - Horizontal: ±128 pixels & Vertical: ±64 pixels
  - Precision: Supports down to 1/4-pixel (QPEL) accuracy  
- Intra Prediction Modes:  
  - Luma: 4×4, 8×8, 16×16  
  - Chroma: 8×8  
- Inter Prediction Modes: 8×8, 16×16  
- Transform Sizes: 4×4, 8×8 
- Supports Deblocking Filter
- Constrained intra-prediction (selectable)  
- Quantization modes: fixed QP, or leaky bucket model–based rate control (based on target bitrate and buffer size) 
- Long-term reference frame support  
- Selectable intra-frame refresh intervals  
- Slice insertion granularity: 32-pixel high rows

> **Notes:**  
> 1. For further details, refer to ITU-T H.264 Annex B: VC-1 Compressed Video Bitstream Format and Decoding Process  
> 2. Encoder does not prevent output from exceeding the maximum bits per macroblock  

**VP8 Encoding Features**  
- Encoding performance: Up to 4K@60 fps
- Maximum frame size: 2048 × 2048 pixels  
- Frame types: Supports I and P frames  
- Motion Estimation (ME) with search range:
  - Horizontal: ±128 pixels & Vertical: ±64 pixels
  - Precision: Supports down to 1/4-pixel (QPEL) accuracy
- Intra Prediction Modes:
  - Luma: 4×4, 8×8, 16×16  
  - Chroma: 8×8  
- Inter Prediction Modes: 8×8, 16×16
- Supports Deblocking Filter
- Quantization modes: fixed QP, or leaky bucket model–based rate control (based on target bitrate and buffer size)

**VP9 Encoding Features**  
- Encoded bitstream compliant with VP9 Profile 0 at 8-bit depth  
- Encoding performance: Up to 4K@60 fps 
- Maximum frame size: 4096 × 4096 pixels  
- Sample depth: 8-bit  
- Frame types: Supports I and P frames  
- Motion Estimation (ME) with search range:
  - Horizontal: ±128 pixels & Vertical: ±64 pixels
  - Precision: Supports down to 1/4-pixel (QPEL) accuracy 
- Intra Prediction Modes:
  - Luma: 8×8, 16×16, 32×32  
  - Chroma: 4×4, 8×8, 16×16  
- Inter Prediction Modes: 8×8, 16×16, 32×32  
- Transform sizes:  
  - Luma: 8×8, 16×16, 32×32  
  - Chroma: 4×4, 8×8, 16×16  
- Supports Deblocking Filter
- Quantization modes: fixed QP, or leaky bucket model–based rate control (based on target bitrate and buffer size)  

#### 2.4.3 Video Decoder

**Decoding Features**  
- Supports the following output frame formats:  
  - 2-plane YUV420, scan-line format, chroma interleaved in UV or VU order  
  - 3-plane YUV420, scan-line format  
    > **Note:** 3-plane format is for testing purposes only; not recommended for maximum performance in normal applications  
- Ensure correct YUV buffer alignment and stride for optimal performance  
- Supports YUV420 AFBC format, 8-bit color depth  
- Configurable for AFBC 1.0 or AFBC 1.2 output  
- Stride support for scan-line formats only  
- Decoded frame rotation supported in 90-degree increments before output  
  > **Note:** Not applicable for AFBC output formats  
- Supports reporting of average luminance (brightness) and chrominance (color) values for each 32×32 pixel block in every displayed output frame  

**Supported Decoding Formats**  
- HEVC (H.265): Main Profile  
- H.264: Baseline, Main, High Profiles  
- VP8  
- VP9: Profile 0  
- VC-1: Simple Profile (SP), Main Profile (MP), Advanced Profile (AP)  
- MPEG-4: Simple Profile (SP), Advanced Simple Profile (ASP)  
- MPEG-2: Main Profile (MP)  
- H.263: Profile 0  

**HEVC (H.265) Decoding Features**  
- Full compliance with Main Profiles
- Decoding performance: Up to 4K@120 fps  
- Maximum frame size: 4096 × 4096 pixels

**H.264 Decoding Features**
- Fully compliant with Baseline, Main, High, and High 10 progressive profiles
- Decoding performance: Up to 4K@120 fps
- Escape option is always enabled to prevent emulation of a Network Abstraction Layer (NAL) unit start code, regardless of the NAL packet format setting  

> **Note:** For further details, refer to ITU-T H.264 Annex B: VC-1 Compressed Video Bitstream Format and Decoding Process  

**VP8 Decoding Features**  
- Fully compliant with the VP8 specification
- Decoding performance: Up to 4K@120 fps
- Maximum frame size: 2048 × 2048 pixels  

**VP9 Decoding Features**  
- Fully compliant with Profile 0
- Decoding performance: Up to 4K@120 fps
- Maximum frame size: 4096 × 4096 pixels  

**VC-1 Decoding Features**  
- Fully compliant with VC-1 Simple, Main, and Advanced Profiles  
- Decoding performance: Up to 4K@120 fps  
- Maximum frame size: 2048 × 4096 pixels

**MPEG4 Decoding Features**  
- Compliant with MPEG-4 Simple Profile (SP) and Advanced Simple Profile (ASP)
- Supports Global Motion Compensation (GMC) with a limitation of one warp point  
- Decoding performance: Up to 4K@120 fps
- Maximum frame size: 2048 × 2048 pixels

**MPEG2 Decoding Features**  
- Compliant with MPEG-2 Main Profile  
- Decoding performance: Up to 4K@120 fps
- Maximum frame size:  
  - Progressive streams: Width up to 4096 pixels  
  - Interlaced streams: Width up to 2048 pixels and Height up to 4096 pixels

**H.263 Decoding Features**  
- Compliant with H.263 Profile 0  
- Decoding performance: Up to 4K@120 fps
- Maximum frame size: Width and height up to 2048 pixels  

### 2.5 Display Subsystem

#### 2.5.1 Display Controller

**Introduction**  
The Display Controller is a hardware module that transfers display data from the internal memory to the DSI and DP/eDP controllers. It supports high-resolution panels and advanced image processing features.

**Features**  
- Resolution Support:
  - 3840×2160 @ 60fps  
  - 2560×1440 @ 144fps  
- Layer Composition:  
  - Up to 4 full-size layer composers  
  - Maximum 16 layer composers via up-down layer reuse in the RDMA channel  
- Command & Write-Back:  
  - `cmdlist` mechanism to configure hardware registers  
  - Concurrent write-back for raw and AFBC formats  
  - Dithering, cropping, and rotation supported in write-back path  
- Memory Management:  
  - Advanced MMU with nearly no page misses during 90° and 270° rotation  
- Color & Display Enhancements:  
  - Color Keying and solid color generation  
  - Advanced Error Diffusion and pattern-based dithering  
  - Color saturation and contrast enhancement  
  - Display effect adjustment  
- Input Formats:  
  - ABGR2101010, ARGB2101010, BGRA2101010, RGBA2101010  
  - ABGR8888, ARGB8888, BGRA8888, RGBA8888  
  - XBGR8888, XRGB8888, BGRX8888, RGBX8888  
  - BGR888, RGB888, ABGR1555, RGBA5551, BGR565/RGB565  
  - XYUV_444_P1_8, XYUV_444_P1_10, YVYU_422_P1_8, VYUY_422_P1_8  
  - YUV_420_P2_8, YUV_420_P3_8  
   <img src="static/disp_input_addr.png" alt="" width="800">
- Output Formats:  
  - RGB888, RGB565, RGB666  
- Panel & Mode Support:  
  - Video mode and command mode (frame buffer in LCM)  
  - Dynamic DDR frequency adjustment with embedded DFC buffer  
- Source Format Support:  
  - Both AFBC and raw image sources  

#### 2.5.2 MIPI DSI Interface

**Introduction**  
The MIPI Display Serial Interface (MIPI DSI) is a high-speed interface connecting the host processor to display peripherals, fully compliant with MIPI Alliance specifications for mobile and embedded devices.

**Features**  
- Standards Compliance:  
  - MIPI DSI v1.2  
  - MIPI D-PHY v1.2  
  - Display Command Set (DCS) standard  
- Lane & Speed Support:  
  - Up to 8 data lanes  
  - Maximum speed up to 4.5 Gbps per lane  
  - 1 active panel per D-PHY link  
- Resolution Support:  
  - Up to 3840×2160 @ 60fps or 2560×1440 @ 90fps  
- Operational Modes:  
  - Command Mode, Video Mode, and Video Burst Mode
- Signaling Support:  
  - HS-TX (High-Speed Transmit)  
  - LP-TX / LP-RX (Low-Power Transmit / Receive)  
  - LP-CLK / LP-CD (Low-Power Clock / Data)  
- Data & Channel Support:  
  - Support for all pixel formats defined in DSI and DCS  
  - Support for virtual channels in the MIPI link  
  - Burst video mode support with D-PHY up to 4.5 Gbps per lane  

#### 2.5.3 DP/eDP Controller

**Introduction**  
The DP/eDP Controller is a display interface controller that manages data transfer from the SoC to external DisplayPort (DP) or embedded DisplayPort (eDP) panels.

**Features**  
- Compliance with DisplayPort (DP) standard v1.2  
- Compliance with embedded DisplayPort (eDP) standard v1.4  
- Supports resolutions up to 3840×2160 @ 60fps or 2560×1440 @ 144fps  

### 2.6 Audio Subsystem

#### 2.6.1 Introduction

The K3 SoC integrates a comprehensive Audio Subsystem designed to deliver high-quality, low-latency audio performance. It incorporates multiple I²S and DisplayPort audio interfaces to support diverse playback and recording scenarios across multimedia and communication applications.  

The subsystem includes the following primary interfaces:  
- 6 × Full-Duplex I²S Interfaces  
- 4 × Half-Duplex I²S Interfaces (two connected to the DP/eDP controller)  
- 2 × DP/eDP Audio Interfaces

#### 2.6.2 Full-Duplex I²S Interfaces Features

- Support full-duplex operation with simultaneous playback and recording  
- Compliance with the standard I²S audio format  
- Fixed audio parameters:  
  - Sampling rate: 48 kHz  
  - Data depth: 16 bits  
  - Channels: 2 (stereo)  
- Configurable system clock (sysclk) modes: 64fs, 128fs, or 256fs  

#### 2.6.3 Half-Duplex I²S Interfaces Features

- Support playback or recording in half-duplex mode  
- Compliance with standard I²S, left-justified, and right-justified formats  
- Audio parameters:  
  - Sampling rate: 48 kHz  
  - Data depth: 16 bits  
  - Channels: 2 (stereo)  
- Support for TDM (Time-Division Multiplexing) mode:  
  - DSP_A / DSP_B modes  
  - Sampling rate: 48 kHz  
  - Data depth: 16-bit / 32-bit  
  - Up to 4 channels  

#### 2.6.4 DP/eDP Audio Interfaces Features

- Support audio playback over DisplayPort or Embedded DisplayPort links  
- Compliance with I²S, left-justified, and right-justified formats  
- Audio parameters:  
  - Sampling rate: up to 192 kHz  
  - Data depth: 16-bit / 20-bit / 24-bit  
  - Channels: 2 (stereo)  

### 2.7 Connectivity Subsystem

#### 2.7.1 PCIe 3.0 (IOMMU)

**Introduction**  
The K3 SoC integrates five PCIe ports — PCIeA, PCIeB, PCIeC, PCIeD, and PCIeE — each supporting PCIe Gen3 operation at 8 GT/s per lane.  

- Lane configuration:  
  - PCIeA provides eight lanes  
  - PCIeB and PCIeC provide two lanes each  
  - PCIeD and PCIeE provide one lane each  
- Mode support:  
  - PCIeA supports dual-mode operation (Root Complex / Endpoint)  
  - PCIeB, PCIeC, PCIeD, and PCIeE support Root Complex (RC) mode only  
- Virtual channels: PCIeB, PCIeC, PCIeD, and PCIeE support VC0 and VC1  
- IOMMU support: PCIeA, PCIeB, and PCIeE support IOMMU for device virtualization  
- PHY configuration:  
  - A total of six PHYs are integrated, providing eight lanes  
  - PHY0 and PHY1 are dual-lane PHYs  
  - PHY2, PHY3, PHY4, and PHY5 are single-lane PHYs  
  - PHY2, PHY3, and PHY4 are shared between PCIe and USB  

**Features**  
- Supports dual-mode operation, programmable as either Root Complex (RC) or Endpoint (EP)  
- Integrated Internal Address Translation Unit (iATU) with 8 outbound and 8 inbound entries  
- Integrated DMA engine with hardware flow control, including 4 write and 4 read channels  
- Supports ECRC generation and checking  
- Supports Maximum Payload Size up to 256 bytes  
- Supports automatic lane flip and reversal  
- Supports Active State Link Power Management (ASPM) with L0 and L1 power states  
- Supports Latency Tolerance Reporting (LTR)  
- Supports Virtual Channel 0 (VC0) and Virtual Channel 1 (VC1)  
- Supports Precision Time Measurement (PTM)
- Supports ID-Based Ordering (IDO)  
- Supports completion timeout range configuration  
- Supports Separate Reference Clock with Independent Spread (SRIS)  
- Supports up to 64 outbound non-posted requests  
- Supports up to 32 outstanding AXI slave non-posted requests  
- In Endpoint (EP) mode:  
  - Supports Function 0 with 6 size-programmable BARs  
  - Supports MSI capability  
- In Root Complex (RC) mode:  
  - Integrates MSI and MSI-X reception module  

#### 2.7.2 USB

**Introduction**  
The K3 SoC integrates multiple USB interfaces to support high-speed connectivity and flexible device configurations. The USB subsystem includes the following ports:  
- One USB 2.0 Host Port  
- One USB 3.0 DRD (Dual-Role Device) Port with an integrated USB 2.0 DRD interface (USB 3.0 Port A)  
- Three USB 3.0 Host Ports (USB 3.0 Port B/C/D) — their SuperSpeed PHYs are shared with PCIe and can operate in either USB or PCIe mode, but only one function can be selected at a time  

##### USB 2.0 Host Port Features

**Controller**  
- Supports USB 2.0 Host mode only  
- Compliant with the USB 2.0 specification  
- Host controller registers and data structures conform to the Intel xHCI specification  
- Supports High-Speed (480 Mb/s), Full-Speed (12 Mb/s), and Low-Speed (1.5 Mb/s) operation  

**Communication Interface**  
- Utilizes a UTMI+ (30/60 MHz) interface for USB 2.0 PHY  

**Clock Domains**  
- UTMI+ PHY (30/60 MHz)  
- MAC (125 MHz nominal)  
- Bus clock domain  
- RAM clock domain  

**System & Power Management**  
- Integrated DMA controller  
- Supports USB 2.0 suspend mode  

**Endpoints & Memory**  
- Supports up to 32 endpoints in Device mode  
- Flexible endpoint FIFO sizing (not restricted to powers of 2) for contiguous memory allocation  
- Supports descriptor caching and data prefetching to improve performance in high-latency systems  

**Additional Features**  
- Software-controlled USB standard commands (SETUP packets can be forwarded to the application for decoding)  
- Hardware-level error handling for USB bus and packet-level errors  
- Interrupt support  

##### USB 3.0 DRD Port Features (Port A, with USB 2.0 DRD Interface)

**Controller**  
- Supports both Host and Device modes for USB 3.0 and USB 2.0  
- Fully compliant with USB 3.0 and USB 2.0 specifications  
- USB 3.0 Host controller registers and data structures conform to the Intel xHCI specification  
- USB 3.0 Device controller registers and data structures are self-defined and require software configuration  
- Supports one USB 3.0 port and one USB 2.0 port  
- Supports SuperSpeed (5 Gb/s), High-Speed (480 Mb/s), Full-Speed (12 Mb/s), and Low-Speed (1.5 Mb/s; Host-only) operation  

**Communication Interface**  
- Utilizes PIPE3 (125 MHz) interface for USB 3.0 PHY  
- Utilizes UTMI+ (30/60 MHz) interface for USB 2.0 PHY  

**Clock Domains**  
- PIPE3 PHY (125 MHz)  
- UTMI+ PHY (30/60 MHz)  
- MAC (125 MHz nominal)  
- Bus clock domain  
- RAM clock domain  

**System & Power Management**  
- Integrated DMA controller  
- Supports USB 2.0 suspend mode  
- Supports U1/U2/U3 low-power states for USB 3.0  

**Endpoints & Memory**  
- Supports up to 32 endpoints in Device mode  
- Flexible endpoint FIFO sizing  
- Descriptor caching and data prefetching for optimized throughput  

**Additional Feature**  
- Software-controlled standard USB commands  
- Hardware-level error detection and recovery for USB bus and packet-level errors  
- Interrupt support  
- The USB 3.0 SuperSpeed PHY integrates an internal Type-C orientation switch controllable via GPIO input  

##### USB 3.0 Host Port Features (Ports B/C/D)

**Controller**  
- Supports USB 3.0 and USB 2.0 Host modes  
- Fully compliant with USB 3.0 and USB 2.0 specifications  
- USB 3.0 Host controller registers and data structures conform to the Intel xHCI specification  
- Supports one USB 3.0 port and one USB 2.0 port  
- Supports SuperSpeed (5 Gb/s), High-Speed (480 Mb/s), Full-Speed (12 Mb/s), and Low-Speed (1.5 Mb/s) operation  

**Communication Interface**  
- Utilizes PIPE3 (125 MHz) interface for USB 3.0 PHY  
- The SuperSpeed PHY is shared with the corresponding PCIe Port (only one function can be active at a time)  
- Utilizes UTMI+ (30/60 MHz) interface for USB 2.0 PHY  

**Clock Domains**  
- PIPE3 PHY (125 MHz)  
- UTMI+ PHY (30/60 MHz)  
- MAC (125 MHz nominal)  
- Bus clock domain  
- RAM clock domain  

**System & Power Management**  
- Integrated DMA controller  
- Supports USB 2.0 suspend mode  
- Supports U1/U2/U3 low-power states for USB 3.0  

**Endpoints & Memory**  
- Supports up to 32 endpoints in Device mode  
- Flexible endpoint FIFO sizing  
- Descriptor caching and data prefetching for improved performance  

**Additional Features**  
- Software-controlled USB commands  
- Hardware-level error handling for USB bus and packet-level issues  
- Interrupt support  

**Block Diagram**

<img src="static/usb_block_diagram.png" alt="" width="800">

#### 2.7.3 Ethernet GMAC

**Introduction**  
The K3 integrates four Gigabit Media Access Controller (GMAC) interfaces compliant with IEEE 802.3-2015, suitable for AV bridges/nodes, switches, network interface cards (NICs), and data-center bridge applications.

**Features**  
- Supports 10/100/1000 Mbps link speeds  
- Supports MII, RMII, and RGMII interfaces  
- Provides a rich set of packet filtering features, including:  
  - Hash and perfect filtering for MAC addresses  
  - Source and destination IP address filtering  
  - Source and destination TCP/UDP port filtering  
- Compliant with IEEE 1588 v1/v2, supporting sub-microsecond synchronization accuracy  
- Supports one-step time stamping for PTP over UDP  
- Transmit flow control:  
  - IEEE Pause or Priority Flow Control (PFC) frames in full-duplex mode  
  - Backpressure mechanism in half-duplex mode  
  - Receive flow control via IEEE Pause frames  
- Provides comprehensive TCP/IP offload capabilities, including:  
  - Source address and VLAN insertion, replacement, and deletion  
  - Transmit checksum offload with hardware-based checksum calculation and insertion  
  - Receive checksum offload with hardware checksum verification  
  - IP checksum offload with hardware calculation and insertion  
  - TCP/UDP checksum offload with hardware calculation and insertion  
  - Header and payload split storage  
  - TCP/UDP segmentation offload (TSO)  
- Supports Time-Sensitive Networking (TSN) features, including:  
  - Enhancements to Scheduled Traffic (IEEE 802.1Qbv-2015)  
  - Frame Preemption (IEEE 802.1Qbu-2016)  
  - Time-based scheduling  

#### 2.7.4 CAN-FD Interface

**Introduction**  
The K3 integrates up to 10 CAN-FD interfaces. Each CAN-FD controller is a full implementation of the CAN protocol, compliant with both CAN with Flexible Data-Rate (CAN-FD) and CAN 2.0 Part B specifications, enabling high-performance automotive and industrial communication.

**Features**  
- Full compliance with CAN-FD protocol and CAN 2.0 Part B, supporting:  
  - Standard and extended data frames  
  - Data payloads from 0 to 64 bytes  
  - Programmable bit rates  
  - Content-related addressing  
- Compliant with ISO 11898-1 standard  
- Silicon-proven, passing ISO 16845-1:2016 CAN conformance tests  
- Flexible mailboxes: configurable for 0, 8, 16, 32, or 64 bytes; each mailbox can be assigned to transmit or receive standard/extended messages  
- Receive FIFO: up to 6 frames with automatic pointer handling and DMA support  
- Transmission features: abort capability, configurable priority (lowest ID, lowest buffer number, or highest priority)  
- Flexible message buffers: 128 slots (8 bytes each), configurable as transmitter or receiver  
- Programmable clock source: peripheral clock or oscillator  
- RAM usable for general-purpose storage (not required for transmission/reception)  
- Special modes:  
  - Listen-Only Mode (LOM)  
  - Loop-Back mode for self-test  
  - Pretended networking in low-power modes (Doze and Stop)  
- Timing and synchronization:  
  - 16-bit free-running timer with optional external time tick  
  - Global network time synchronization via specific messages  
  - Synchronization indication through SYNCH bit in Error Status 1 register  
- Error handling:  
  - CRC status for transmitted messages  
  - Detection and correction of memory read errors using 5 parity bits per byte (corrects single-bit errors, detects two-bit errors)  
- Advanced receive filtering:  
  - ID filtering supports 128 extended IDs, 256 standard IDs, or 512 partial (8-bit) IDs  
  - Up to 32 elements in ID Filter Table  
  - Supports Identifier Acceptance Filter Hit Indicator (IDHIT)  
- Transceiver Delay Compensation (TDC) for CAN-FD high-speed transmission  
- Low latency for high-priority messages via arbitration  
- Interrupts: maskable and independent per mailbox/FIFO  
- Fully backward compatible with previous CAN-FD versions  

#### 2.7.5 SPI Interface

**Introduction**  
The SPI (Serial Peripheral Interface) is a synchronous serial interface that enables communication with external devices using the Motorola SPI protocol. It can be configured to operate in either Master mode, where the connected device acts as a slave, or Slave mode, where the connected device functions as the master.

**Features**  
- Supports all four CPOL/CPHA combinations defined by the SPI specification.  
- Configurable for operation in either Master or Slave mode.  
- Supports receive-without-transmit operation.  
- Supports serial bit rates ranging from 6.3 Kbps (minimum recommended) to 52 Mbps (maximum allowed).  
- Data size configurable to 8, 16, 18, or 32 bits.  
- Equipped with independent transmit (TXFIFO) and receive (RXFIFO) buffers:  
  - In Non-Packed Data Mode, both FIFOs are 32 entries × 32 bits, supporting a total of 32 samples.  
  - In Packed Data Mode, double-depth FIFOs are used for 8-bit or 16-bit data, providing 64 entries × 16 bits, supporting a total of 64 samples.  
  - Both FIFOs support loading and unloading via Programmed I/O (PIO) or DMA burst transfers.  

#### UART Interface

**Introduction**  
The UART (Universal Asynchronous Receiver/Transmitter) module provides asynchronous serial communication between the system and external devices. It supports flexible configuration, efficient data handling, and diagnostic features, suitable for both low- and high-speed communication scenarios.

**Features**  
- Interfaces: Supports up to 17 independent UART interfaces. It includes 11 AP domain UARTS and 6 RCPU domain UARTS  
- Compatibility: Fully compatible with industry-standard 8250 UART.  
- Asynchronous Communication: Automatic insertion and removal of start, stop, and parity bits in the serial data stream.  
- Interrupt Control: Independent control of transmit, receive, line status, and data set interrupts.  
- Modem Control: CTS and RTS supported on AP domain UART1–UART10 and RCPU domain UART1.  
- Auto Flow Control:  
  - RTS (output): automatically driven by UART receive FIFO.  
  - CTS (input): controlled by external modem transmission signal.  
- Programmable Serial Parameters:  
  - Character length: 7 or 8 bits  
  - Parity: even, odd, or none  
  - Stop bits: 1  
  - Baud rate: up to 3.6 Mbps for 4 high-speed UARTs  
  - False start-bit detection supported  
- FIFO Buffers:  
  - 256-byte transmit FIFO  
  - 256-byte receive FIFO  
- Diagnostics:  
  - Loopback mode for communication link verification  
  - Break, parity, and framing error simulation  
- DMA Support: Independent DMA request channels for transmit and receive operations.  

#### 2.7.7 I²C Bus Interface

**Introduction**  
The Inter-Integrated Circuit (I²C) bus is a true multi-master serial communication bus featuring collision detection and arbitration capabilities.  
The I²C bus interface can operate as either a master or slave device on the I²C bus. Developed by Philips Corporation, this serial interface requires only two signal lines:  
- SDA: Data line for bidirectional input and output  
- SCL: Clock line providing timing reference and bus control  

The I²C bus enables seamless communication between the I²C unit and various external I²C peripherals or microcontrollers. Its simple hardware design provides an efficient and cost-effective method for transferring control and status information between on-chip and off-chip devices.  

The I²C bus interface resides on the peripheral bus and supports:  
- Data transfer via a buffered interface for reliable communication  
- Control and status management through memory-mapped registers  

**Features**  
- Supports up to 10 independent I²C interfaces  
- Compliant with the I²C bus specification Version 2.1, except for:  
  - Hardware general call support  
  - 10-bit slave addressing  
  - CBUS compatibility  
- Supports Multi-Master operation and bus arbitration  
- Supports the following operation modes and speeds:  
  - Standard Mode: up to 100 Kbps  
  - Fast Mode: up to 400 Kbps  
  - High-Speed Slave Mode: up to 3.4 Mbps (High-Speed I²C only)  
  - High-Speed Master Mode: up to 3.3 Mbps (High-Speed I²C only)  

> **Note:**  
> 1. In High-Speed Master Mode, operational frequency is limited by the value of the pull-up resistors on the bus.  
> 2. The SCL frequency *f* is inversely proportional to the pull-up resistor *R* (i.e. *f ∝ 1/R*).  

**Block Diagram**  

The architecture of the I²C bus interface is depicted below.  

<img src="static/i2c_block_diagram.png" alt="" width="600">

#### 2.7.8 IR-RX Interface

**Introduction**  
IRC (IR Controller) can be used to receive infrared signals from external sources.

**Features**  
- Supports up to 4 IRC modules  
- Converts incoming infrared signals into Run-Length-Code (RLC) format  
- Configurable signal width threshold for noise filtering and detection  
- 32-byte FIFO for temporary storage of received data  
- Sample clock up to 102.4M with a 24-bit frequency divider in it which allows user to configure sample clock freely  

#### 2.7.9 eSPI

**Introduction**  
The eSPI Controller is a full implementation of the Enhanced Serial Peripheral Interface (eSPI) version 1.0 protocol, officially introduced by Intel in 2016. It was designed to replace the LPC interface, reducing pin count and power consumption. eSPI is widely used in Embedded Controllers (ECs), Baseboard Management Controllers (BMCs), Super I/O (SIO) devices, Port-80 debug cards, and similar components.  

eSPI is based on the electrical characteristics of the SPI bus while redefining its protocol layer. Compared with LPC, eSPI offers the following advantages:  
- Significantly reduces the number of pins by converting all LPC/SMBus/sideband signals into in-band signals.  
- Supports operating frequencies of 20 MHz, 25 MHz, 33 MHz, 50 MHz, and 66 MHz, providing higher bandwidth.  
- Uses a 1.8 V interface voltage.  

**Basic Features**  
- Fully compliant with the eSPI v1.0 (2016) specification.  
- Supports four channel types: Peripheral (PR), Out-of-Band (OOB), Virtual Wires (VW), and Flash Access.
- Supports I/O modes: 1×, 2×, and 4×.  
- Supports frequency modes of 20/25/33/50/66 MHz.  
- Supports up to one slave device (SLAVE0).  
- Supports automatic CRC insertion and checking; CRC checking can be enabled by setting `CRC_CHECK_EN` (0x68, SLAVE0_CONFIG).  
- Provides two merged interrupt outputs corresponding to controller status/error interrupts and VW interrupts; the CPU identifies the interrupt source by reading the status register.  
- Includes a watchdog and software reset to prevent bus stalls when the slave does not respond during PR-read operations through the AXI3 slave interface.  
- Supports automatic gating of the master interface to reduce power consumption during idle periods.  
- Allows rewriting of internal slave status registers for software debugging.  
- Provides a register-mapped `RESET#` signal to reset the eSPI slave.  

**PR Channel Features**  
- The PR channel provides a mechanism for software to perform read and write operations on slaves that are transparent to the software layer.  
- The AXI slave interface of the eSPI Controller can be translated into PR read/write operations on the eSPI interface, while slave requests on the eSPI bus are converted into AXI master read/write operations, simplifying PR-channel communication.  
- TX and RX data are stored in independent 32-bit × 16 FIFOs.  
- Two 32 MB address spaces are used for PR MEM read/write operations. By configuring `PR_BASE_ADDR_MEM_0` (0x38) and `PR_BASE_ADDR_MEM_1` (0x3C), the full 32-bit memory address space of the slave can be accessed.  
- One 16 KB address space is used for PR I/O read/write operations, allowing direct access to the 16-bit I/O space.  
- Message-type transmissions on the PR channel are initiated and received through operation registers, using an independent 32-byte FIFO.  
- `PR_MAX_SIZE = 64` bytes, requiring that master and slave PR channel transmissions do not cross 64-byte boundaries.  

**VW Channel Features**  

- Supports VW interrupts 0 – 23.  
- Supports up to 16 GPIOs simultaneously, divided into four groups corresponding to four indices. The mapping between GPIO groups and VW channel indices is configurable.  
- The maximum count for a single VW transmission is 16.  
- Interrupt or GPIO operations on the slave can be triggered by configuring registers.  
- Supports automatic updates of interrupt and GPIO states.  
- Supports system events with indices 2 – 7 and generates corresponding interrupts.  
- Each interrupt has an associated status register supporting interrupt masking and polarity configuration.  

**OOB Channel Features**  
- OOB request forwarding is handled by the CPU through interrupts.  
- The maximum size of a single OOB transmission is 128 bytes.  

**Flash Access Channel Features**  
- Flash Access request forwarding is handled by the CPU through interrupts.  
- The maximum size of a single Flash Access transmission is 128 bytes.  

**Block Diagram**  
The architecture of the eSPI controller is depicted below.
<img src="static/espi_block_diagram.png" alt="" width="800">

### 2.8 Security Subsystem

#### 2.8.1 Crypto Engine

**Introduction**  
Supports internationally recognized cryptographic algorithms as well as China’s commercial cryptography algorithms.

**Features**  
- Hash Algorithms: SHA1/224/256, SM3  
- Symmetric Algorithms: AES128/192/256, SM4  
- Asymmetric Algorithms: RSA1024/2048/4096, ECC128/256/512, SM2  

#### 2.8.2 TRNG

**Introduction**  
A random number generator compliant with China’s commercial cryptography standards.

**Features**  
- Built-in 32-bit TRNG  
- Ensures randomness, unpredictability, and non-reproducibility  

#### 2.8.3 eFuse

**Introduction**  
Integrated 4096-bit eFuse, divided into 16 banks of 256 bits each, with 256 bits available for user customization.

**Features**  

- Supports eFuse bank locking  
- Supports automatic hardware parameter loading  
- Supports lifecycle management  
- Supports secure boot configuration  
- Supports storage of root keys and encryption-protected keys  
- Supports 256-bit non-volatile counter (NV Counter)  

#### 2.8.4 IOPMP

**Introduction**  
The IOPMP (I/O Physical Memory Protection) module is designed in coordination with the PMP（Physical Memory Protection） to ensure secure access control across the platform’s peripherals.  
- The PMP validates bus accesses initiated by the RISC-V cores;
- The IOPMP verifies transactions issued by other bus masters or subsystems.  

Configured exclusively by the Secure World, the IOPMP defines access permissions and attributes for transactions initiated by non-CPU masters.  
All transactions are subject to IOPMP entry checks, and access is granted only when the permission verification passes.

**Features**  
- Supports access control for read, write, and execute permissions  
- Bus requests incur a one-cycle delay after permission checking  
- Supports logging of access violation information  
- Supports interrupt generation for access violation events  
- Integrates 9 IOPMPs to provide security control for hardware modules and subsystems

### 2.9 System Peripherals

#### 2.9.1 DMA

**Introduction**  
The Direct Memory Access (DMA) controller is designed to transfer data between memory and peripheral devices without CPU intervention, thereby enhancing system performance and reducing processor overhead.  
Peripheral devices do not directly issue addresses or commands to the memory controller. Instead, each DMA request from a peripheral device triggers a corresponding memory-bus transaction.  
The processor can also access the peripheral bus via the DMA controller, which serves as a DMA bridge, enabling data transfers that bypass the system’s primary DMA path when necessary.  
The DMA controller supports various data transfer types in DMA Flow-Through Mode through 16 configurable DMA channels. The supported data transfer paths are summarized below:

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">

  <colgroup>
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Source / Destination</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Internal Memory</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">External Memory</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Internal Peripheral</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">External Peripheral</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- Row 1: Internal Memory -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold;">Internal Memory</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Flow-Through Mode</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
    </tr>
    <!-- Row 2: External Memory -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold;">External Memory</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Flow-Through Mode</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Flow-Through Mode</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
    </tr>
    <!-- Row 3: Internal Peripheral -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold;">Internal Peripheral</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Flow-Through Mode</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Flow-Through Mode</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
    </tr>
    <!-- Row 4: External Peripheral -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold;">External Peripheral</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Flow-Through Mode</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Flow-Through Mode</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">___</td>
    </tr>
  </tbody>
</table>

**Features**  
- Two independent DMA controller instances, supporting:  
  - One for secure domains  
  - One for non-secure domains  
- Support for the following data transfer types in DMA Flow-Through Mode:  
  - Memory-to-Memory  
  - Peripheral-to-Memory  
  - Memory-to-Peripheral  
- Flow-Through Mode supported for direct data transfers between Flash and DDR memory  
- Priority mechanism enabling simultaneous processing of up to 4 channels with outstanding DMA requests  
- Each of the 16 DMA channels can operate in either descriptor-fetch or non-descriptor-fetch mode  
- Support for the following special descriptor modes:  
  - Descriptor Comparison  
  - Descriptor Branching  
- Retrieval of trailing bytes from peripheral receive buffers  
- Configurable burst sizes: 8, 16, 32, or 64 bytes  
- Programmable peripheral data widths: byte, half-word, or word  
- Support for up to 8191 bytes per descriptor (larger transfers achieved by chaining multiple descriptors)  
- Flow Control Bit support to synchronize DMA requests with peripheral readiness (transfers occur only when the flow control bit is set)  
- 64-bit address bus supporting direct access to physical memory space above 4GB  

**Block Diagram**  
The architecture of the DMA controller is depicted below.
<img src="static/dma_block_diagram.png" alt="" width="500">

#### 2.9.2 HDMA

**Introduction**  
The K3 integrates 8 AXI DMA Controllers (HDMA). The HDMA IP core is a high-speed, high-throughput general-purpose DMA controller, designed to transfer data between system memory and peripherals such as high-speed converters.

**Features**  
- Supports Unaligned Address Transfers  
- Automatic 4K address boundary crossing  
- Zero-latency transfer switch-over architecture for continuous high-speed streaming  
- Supports Cyclic Transfers  
- Supports 2D Transfers  
- Supports Scatter-Gather Transfers  
- Framelock support for synchronized data streams  
- AutoRun mode for autonomous transfer operation  

#### 2.9.3 Timer

**Introduction**  
The K3 SoC integrates nine general-purpose 32-bit timers for system applications. Each timer has its own 32-bit Timer Counter Control Register (TCCRn) and functions as an up-counter.

**Features**  
- Programmable count modes:  
  - Fast count mode: Input clock frequency selectable from 12.8 MHz, 6.4 MHz, 3 MHz, or 1 MHz  
  - Slow count mode: Input clock frequency of 32.768 KHz  

#### 2.9.4 WatchDog

**Introduction**  
The K3 SoC integrates six 24-bit Watchdog Timers (WDTs) designed to monitor system operation and initiate recovery actions in case of software malfunctions or system hangs.

**Features**  
- Programmable count mode:  
  - WDT operates with an input clock frequency of 256 Hz  
  - Each WDT includes a 24-bit counter  

#### 2.9.5 Temperature Sensor

**Introduction**  
The K3 integrates one Temperature Sensor (TSEN) module featuring 7 temperature measurement points. It is designed to monitor thermal conditions across various on-chip locations, providing real-time temperature data that enables the system to perform dynamic thermal management and protection operations.

**Features**  
- Support for system restart temperature threshold configuration  
- Provides 7 independent temperature measurement points as follows:
  - Top sensor
  - VPU sensor
  - GPU sensor
  - Cluster 0 sensor
  - Cluster 1 sensor
  - Cluster 2 sensor
  - Cluster 3 sensor
- 12-bit temperature sampling accuracy for precise thermal monitoring  

#### 2.9.6 PWM

**Introduction**  
The PWM (Pulse Width Modulation) interface provides precise control of analog circuits and peripheral devices using digital signals. It supports programmable waveform generation with adjustable frequency, duty cycle, and phase alignment, making it suitable for applications such as motor control, LED dimming, and audio modulation.

**Features**  
- Channels: K3 includes 20 independent PWM channels, labeled PWM0–PWM19, each with its own configuration registers.  
- Independent Control: Each channel can operate autonomously, generating PWM signals via multi-function pins.  
- Timing Control:  
  - Individual control of leading-edge and trailing-edge timings for each PWM output.  
  - Continuous mode operation or dynamically adjustable waveforms to meet varying application requirements.  
- Frequency & Duty Cycle:  
  - Supports frequencies from 195.3 Hz to 12.8 MHz.  
  - 50% duty cycle supported; other duty-cycle values depend on the selected frequency.  
- Counters & Dividers:  
  - 6-bit clock divider and 10-bit period counter for fine-grained frequency control.  
  - 15-bit pulse counter for precise pulse generation.  
- Power Saving:  
  - Supports a power-saving mode by stopping the internal clock (`PSCLK_PWM`) of a channel while holding its output (`PWM_OUT`) at a constant high or low level, reducing power consumption when the PWM output is not required.  

#### 2.9.7 Mailbox

**Introduction**  
The Mailbox provides an inter-processor communication mechanism that allows on-chip processors to exchange messages efficiently.

**Features**  
- Each instance supports four mailbox channels and two users.  
- Each mailbox channel includes an 8 × 32-bit FIFO.  
- Independent threshold registers are provided to generate new-message and not-empty interrupts.  
- For each mailbox channel, the message direction can be flexibly configured through software.  

**Block Diagram**  
The architecture of the Mailbox is depicted below.
<img src="static/mailbox_block_diagram.png" alt="" width="800">

#### 2.9.8 Spinlock

**Introduction**  
Spinlock is a hardware synchronization mechanism used in multi-core systems. It prevents simultaneous access to shared resources, ensuring data consistency.

**Features**  
- Each instance supports 32 lock units.  
- Two lock states are supported: locked and unlocked.  

#### 2.9.9 GPIO

**Introduction**  
The K3 provides General-Purpose Input/Output (GPIO) ports for generating and capturing application-specific input and output. These ports are accessed through the alternate function muxing, and the GPIO unit manages their control and status.

**Features**  
- A GPIO port configured as an input can also serve as an interrupt source  
- At system reset, by default all GPIO ports are configured as an input until changed by the boot process or user software  
- Each GPIO port has a dedicated control signal  
- Supports separated interrupts over either leading-edge timing or trailing-edge timing or both  
- The GPIO port output can be individually set or cleared  
- The GPIO port input can be individually read  

#### 2.9.10 Time-Out Monitor

**Introduction**  
The Time-Out Monitor (TOM) is an AXI bus event detection module designed to monitor AXI transactions and identify timeout conditions that may occur during data transfers between system components.

**Features**  
- Configurable timeout threshold for flexible detection of stalled transactions  
- Programmable auto-response behavior when a timeout event is detected  
- Debug support: the address and ID of the first timed-out transaction are captured for analysis  
- Configurable AW/ARREADY signal monitoring to ensure bus transaction reliability  

### 2.10 Clock & Reset

#### 2.10.1 Introduction
The K3 integrates multiple on-chip clock sources and reset controls to support a wide range of operational scenarios, providing high flexibility, stability, and power efficiency.  
K3 comes with the following clocks:  
- One 24MHz OSC clock  
- One 32.768kHz RTC clock  
- One 3MHz OSC clock  
- One 1MHz OSC clock  

#### 2.10.2 Features

- Eight integrated PLLs providing multiple frequency options for diverse system requirements  
- Dynamic Voltage and Frequency Scaling (DVFS) support for optimal power–performance balance  
- Glitch-free clock switching and programmable clock dividers to efficiently generate required frequencies while minimizing PLL resource cost  
- Fine-grained clock gating and software-controlled reset mechanisms for improved power saving and flexible system management  

#### 2.10.3 Clock System  

The K3 integrates eight Phase-Locked Loops (PLLs) designed to provide a wide range of stable and configurable frequency sources for different modules and CPU cores. Each PLL supports programmable control through the Main PMU registers and is optimized for low jitter and quick lock time.  

- **PLL1** is designed to generate fixed frequency points for CPU cores and system peripherals.  
- **PLL2** is designed to generate multiple fixed frequencies that complement PLL1, providing a full range of clock sources for peripheral modules.  
- **PLL3** provides clock frequencies for CPU Core 0 frequency scaling and dynamic switching.  
- **PLL4** provides clock frequencies for CPU Core 1 frequency scaling and switching.  
- **PLL5** provides clock frequencies for CPU Core 2 frequency scaling and switching.  
- **PLL6** generates additional fixed frequencies to extend system clock flexibility alongside PLL1.  
- **PLL7** generates supplementary fixed frequencies to support various system and peripheral modules.  
- **PLL8** provides clock frequencies for CPU Core 3 frequency scaling and dynamic switching.  

##### Resource Reset Schemes  

The K3 allows applying different schemes of resource reset as tabled below.

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="300">
    <col width="600">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">No.</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Resource Reset Scheme</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- Row 1 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Power-On-Reset</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">Reset the whole chip during power-on sequence</td>
    </tr>
    <!-- Row 2 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">2</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">WatchDog Reset</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">Reset the whole chip excluding pinmux registers and debug registers</td>
    </tr>
    <!-- Row 3 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">3</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Module Software Reset</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">Reset each module individually through software</td>
    </tr>
    <!-- Row 4 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">4</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">Power Island POR Reset</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">Reset the whole power island during its power-on sequence</td>
    </tr>
  </tbody>
</table>

### 2.11 Boot Mode

#### 2.11.1 Introduction

The K3 platform supports multiple boot methods:  
1. Online Download: Downloads and boots the Bootloader using standard communication protocols.  
2. Local Boot: Loads and boots the Bootloader from various storage media.  

The boot mode is selected by configuring the Boot Strap Pins.

#### 2.11.2 Features

The K3 platform supports two categories of boot modes:

1. Download Mode
   Used for downloading images or for debugging and testing.  
   In this mode, the device communicates with a host system through a wired interface and receives data based on predefined protocols to complete system startup.  

   Download modes include:  
   - USB Fastboot Mode: Connects to the host via the USB 2.0 interface using the Fastboot protocol.  
   - UART Xmodem Mode: Connects to the host via the UART interface using the Xmodem/Xmodem-1K protocol.  

2. Normal Boot Mode
   When a valid image is preloaded, the system can boot directly from a specified storage medium.  
   K3 supports loading the Bootloader from the following storage devices:  
   - SD Card  
   - eMMC  
   - SPI NOR Flash  
   - SPI NAND Flash  
   - UFS  

**Boot Priority**:  
The K3 always first attempts to boot from the SD Card.  
If no SD card is detected or no valid Bootloader image is found, the system automatically falls back to a secondary storage device.  
The secondary boot device can be selected by configuring the Boot Strap Pins.

The K3 uses a combination of four Boot Strap pins to select the boot mode, as shown in the table below:

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">
  <colgroup>
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        Download Select<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_69</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        Download Mode<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_68</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        Boot Select 1<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_66</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        Boot Select 0<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_65</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Boot Mode</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- Row 1 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">USB Fastboot</td>
    </tr>
    <!-- Row 2 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">UART Xmodem</td>
    </tr>
    <!-- Row 3 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">SD Card → eMMC</td>
    </tr>
    <!-- Row 4 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">SD Card → SPI NOR</td>
    </tr>
    <!-- Row 5 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">SD Card → SPI NAND</td>
    </tr>
    <!-- Row 6 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">x</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">SD Card → UFS</td>
    </tr>
  </tbody>
</table>

> **Note**: “x” indicates that the pin state does not affect boot mode selection.

## 3. Package

### 3.1 Introduction

K3 is available in one package as follows:

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Size</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Pitch</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Count</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- Row 1 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold;">FBGA</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">27×27 mm</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">0.650 mm</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1563 (40×40)</td>
    </tr>
  </tbody>
</table>

The related package outline drawing (POD) is depicted in the following section.

### 3.2 Package Outline Drawing (POD)

<img src="static/package1.png" alt="" width="500">

<img src="static/package2.png" alt="" width="800">

## 4. Pinout

### 4.1 Pinout Diagram & Description

The overall pinout diagram of K3 is depicted below.
<img src="static/k3_pinmap.png" alt="" width="900">

Let’s consider the division into the quadrants, in order to conveniently provide the pinout description of K3 in the following subsections.

#### 4.1.1 (A~Y, 1~20)

<img src="static/k3_pinmap_a-y_1-20.png" alt="" width="800">

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_08</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKT_B</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DMI1_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKC_B</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_09</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE5_TX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE4/USB3-D_TX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_A_01</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE3/USB3-C_TX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE2/USB3-B_TX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_TX1P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_TX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_TX1P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">A20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE3/USB3-C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">L20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE2/USB3-B</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKT_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_11</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKC_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_10</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_00</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE5_TX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_02</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE5_REFCLK_N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE4/USB3-D_TX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_A_00</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE4_REFCLK_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE3/USB3-C_TX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE3_REFCLK_N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE2/USB3-B_TX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PLL_DDR1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE2_REFCLK_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_TX1N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_REFCLK_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_TX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_B_USB_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_TX1N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">B20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_REFCLK_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_00</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_02</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">M20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE2/USB3-B</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_15</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS1_T_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_14</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS1_C_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_ZN</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_01</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_03</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE5_REFCLK_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKE0_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE4_REFCLK_N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE3_REFCLK_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PLL_DDR1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE2_REFCLK_N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_REFCLK_N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_B_USB_M</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">C20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_REFCLK_N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_03</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_01</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">N20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_13</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_12</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKE1_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS0_C_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_B_00</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS0_T_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE5_RX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CS1_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_D_USB_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE4/USB3-D_RX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE3/USB3-C_RX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE2/USB3-B_RX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_RX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">D20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_T_B_0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_C_B_0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">P20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_C_A_1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_T_B_1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_T_A_1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_C_B_1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CS1_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE5_RX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_D_USB_M</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE4/USB3-D_RX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE3/USB3-C_RX0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE2/USB3-B_RX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_RX0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">E20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS0_T_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS0_C_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">R20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS1_C_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_12</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQS1_T_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_C_A_0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKE0_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_WCK_T_A_0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CKE1_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE5</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE4/USB3-D</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_B_USB20</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE_USB_COMBO_ADTEST_0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_USB20_HOST</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_C_USB_M</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_RX1N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">F20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD33_D_USB20</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">T20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DMI0_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DMI1_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_11</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_13</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DMI0_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_15</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_04</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_B_01</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CS0_A_CA06</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE5</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE4/USB3-D</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_C_USB20</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_C_USB_P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE1_RX1P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">U20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_10</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">G20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD33_C_USB20</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_09</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_05</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_04</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_07</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_05</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_14</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_B_03</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_A_05</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_B_02</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE3/USB3-C</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PCIE_USB_COMBO_ADTEST_1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">V20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_08</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_D_USB20</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_C_USB20</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">H20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_A_06</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_07</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DQ_B_06</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_A_03</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_B_04</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD2H_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CS0_B_CA06</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VAA18_VDD2H_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_D_USB20</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE3/USB3-C</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE2/USB3-B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">W20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE5</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_RESET_N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE4/USB3-D</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_PWROK</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">J20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_DTO</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_ATO</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_A_02</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_A_04</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD2H_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR1_CA_B_05</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VAA18_VDD2H_DDR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PCIE2/USB3-B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Y20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE5</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE4/USB3-D</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">K19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE3/USB3-C</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
  </tbody>
</table>

#### 4.1.2 (A~Y, 21~40)

<img src="static/k3_pinmap_a-y_21-40.png" alt="" width="800">

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 8px 4px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 8px 4px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_TX0N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_B_USB20</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXCKN_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VDDBH_0V9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCPLL_1P2V</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXCKP_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCIO_0V8</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXCKSB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_21</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_45</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_25</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_50</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_29</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_32</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_57</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_34</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_60</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">A39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_66</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_TX0P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">L40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_72</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">USB20_HOST_M</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_USB20_HOST</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXCKP_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VDDVPH0_0V9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VDDVPH0_0V9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXCKN_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_22</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_26</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_46</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_30</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_51</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_58</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_33</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_38</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_61</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">B40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_67</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">M40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_73</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">USB20_HOST_P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXTRK_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXTRK_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_23</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">DTEST_PAD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_27</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">ATEST_PAD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_31</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_52</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_35</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_62</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_36</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">N40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_74</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">C40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_40</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_RX1P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXVLD_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_28</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_37</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_DS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_39</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_63</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">D40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_41</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_68</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_RX1N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">P40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_75</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATASB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_OSC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_O_CKNT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_OSC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXCKSB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATASB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[2]_24</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PMIC_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PWR_SSP_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PMIC_WDT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_CLK</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PRI_TDO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_CMD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PRI_TRST_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">E40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PWR_SSP_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D5</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">R40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_RX0P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PLL234</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_O_CKPT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXVLD_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_FUSE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PRI_TMS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PWR_SSP_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EXT_32K_IN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">T40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D7</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PRI_TDI</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">F40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PCIE/USB3_RCAL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD33_USB20_HOST</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PLL234</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PCIE0_RX0N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_PMIC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_TXDATA_M0[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_PMIC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_RXDATA_M0[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">EMMC_D0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PRI_TCK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCXO_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">U40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">RESET_IN_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PLL567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">G40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">PWR_SSP_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PLL567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD33_B_USB20</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_ATEST</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_BGR_EAREFCLKN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VDD_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_EW_VCTRL_EXT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D3N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_42</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D3P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_47</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_53</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D2N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_55</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">V40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D2P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_54</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">H40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_69</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCAON_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCAON_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_BGR_EAREFCLKP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VDD_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">XI_PAD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_OSCPLL234567</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_43</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_48</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI3_CLKN</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI3_CLKP</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_56</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">W40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_59</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_64</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">J40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_70</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PCIE0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_USB20_HOST</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCAON_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCPLL_1P2V</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VCC18_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">XO_PAD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_OSCPLL234567</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D1P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_44</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D1N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_49</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D0P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_65</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">Y40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_D0N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">K40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;">GPIO[3]_71</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5;"></td>
    </tr>
  </tbody>
</table>

#### 4.1.3 (AA~AY, 1~20)

<img src="static/k3_pinmap_aa-ay_1-20.png" alt="" width="800">

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_15</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_ATO</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_PWROK</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DTO</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_A_05</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PLL1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_QSPI</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_SD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_13</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_05</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_14</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_02</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_A_04</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_00</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_B_00</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_A_02</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC12_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_QSPI_CAP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DMI1_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_06</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_12</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_07</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_03</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_01</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_B_01</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_A_01</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD08_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD33_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC12_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO5</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS1_C_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_04</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS1_T_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DMI0_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_T_B_0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_14</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_C_B_0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_15</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKE0_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_A_00</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD08_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD33_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_EXTR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO5</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_T_B_1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_T_A_0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_C_B_1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_C_A_0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_12</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_13</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_B_02</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKE0_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_REF_CLK</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">QSPI_CLK</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">QSPI_DAT3</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_09</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS0_C_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_11</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS0_T_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS0_C_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS1_C_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS0_T_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQS1_T_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKE1_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKE1_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DRD_USB</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB_PORTA_ADTEST</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD0_RXN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_A_DRD_USB_P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_TXD0N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX0N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">QSPI_CS0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_08</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_02</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_10</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_01</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DMI0_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_04</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CS0_B_CA06</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CS1_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PLL_DDR0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD0_RXP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB20_A_DRD_USB_M</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_TXD0P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX0P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">QSPI_DAT1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_00</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_03</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_06</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_T_A_1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_05</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_WCK_C_A_1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_B_05</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_ZN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PLL_DDR0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD1_RXP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_RST_N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_TXD1N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_AUXP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX2P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKC_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKT_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_B_07</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_11</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_B_04</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_09</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_B_03</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_RESET_N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_PLL1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD0_TXP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD1_RXN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD1_TXN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_RXD1P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_TXD1P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_RXD0N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DVDD08_EDP1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_AUXN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DVDD08_EDP1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX1N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX2N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX3N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKC_A</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CKT_A</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DMI1_A</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_10</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CS0_A_CA06</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_DQ_A_08</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CA_A_03</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK6</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK7</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DDR0_CS1_B</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_PLL1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD0_TXN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_PLL1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DRD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB30_A_DRD1_TXP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_RXD1N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_UFS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UFS_RXD0P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX1P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP1_TX3P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
  </tbody>
</table>

#### 4.1.4 (AA~AY, 21~40)

<img src="static/k3_pinmap_aa-ay_21-40.png" alt="" width="800">

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Pin Number</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_SD_CAP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO5</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D2N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_CLKN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D2P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_CLKP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AA40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AL40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_SD_CAP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO5</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC18_GPIO1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_CSI2</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_CSI2</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_CLKN</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D1P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI2_CLKP</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D1N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D3N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D3P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D3P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D3N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_CLKN</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D0P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AB40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_CLKP</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AM40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D0N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC1833_GPIO1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_EXTR</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D1P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_AUXN</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D1N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_AUXP</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AC40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AN40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">QSPI_DAT2</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_119</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_114</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_108</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_106</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_20</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_CSI0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_16</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_CSI0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_06</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_CSI1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_05</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD08_CSI1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_79</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_78</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI1_D0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D3N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX3P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AD40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D3P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AP40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX3N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">QSPI_CS1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_120</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_109</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_105</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_99</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_19</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_07</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_04</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_76</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_80</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D2N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX2P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D2P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX2N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AE40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AR40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">QSPI_DAT0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_124</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_121</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_115</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_110</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_CSI1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_100</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_CSI1</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_18</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_CSI2</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_13</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_CSI2</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_08</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_77</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_CLKN</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_81</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_CLKP</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_86</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_90</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D1P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AF40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D1N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX1P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AT40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX1N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MMC1_DAT2</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MMC1_DAT1</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_125</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_116</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_111</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_101</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_09</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_03</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_87</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX0P</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">EDP0_TX0N</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_CSI0_D0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AU40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AG40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_MIPI012</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MMC1_CLK</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MMC1_DAT0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_126</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_117</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_102</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_17</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_02</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_82</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD12_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_88</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_CSI0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_CSI0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_96</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AV40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_98</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D2P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MMC1_CMD</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D2N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_122</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D1N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_118</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AH40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D1P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_112</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_104</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_14</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_12</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_CPUX</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_10</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_01</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DVDD08_EDP0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">DVDD08_EDP0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_83</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_89</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD12_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_91</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_93</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_95</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_97</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AW40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MMC1_DAT3</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_127</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_CLKN</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_123</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_CLKP</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AJ40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_113</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_107</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[5]_103</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_15</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_11</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[1]_00</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_85</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VCC_SYS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_84</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_EDP0</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_92</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVDD18_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">GPIO[4]_94</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D0P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D0N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AY40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">VSS</td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D3P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI0_D3N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">AVSS_DSI</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D2N</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
    <tr><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">AK40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">MIPI_DSI1_D2P</td><td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td></tr>
  </tbody>
</table>

### 4.2 I/O Pin Parameters

#### 4.2.1 For 1.8V I/O Pins

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="150">
    <col width="100">
    <col width="450">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Power Domain</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Symbol</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Min</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Typ</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- 1.8V Input Section -->
    <tr>
      <td rowspan="5" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">1.8V Input</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vih</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level input</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC×0.7V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">1.8V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC+0.2V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level input</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">-0.3V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC×0.3V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpu</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Pull up resistor</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">55kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">79kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">121kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpd</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Pull down resistor</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">51kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">87kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">169kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Iil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Input leakage current (Pad in input mode)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10µA</td>
    </tr>
    <!-- 1.8V Output Section -->
    <tr>
      <td rowspan="10" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">1.8V Output</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Voh</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC−0.2V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vol</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0.2V</td>
    </tr>
    <!-- IOL Rows (Split for clarity within 500px col) -->
    <tr>
      <td rowspan="4" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Iol<br><span style="font-size:11px; color:#666;">DCS[1:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.2V) <strong>DCS=00</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">13mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.2V) <strong>DCS=01</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">25mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.2V) <strong>DCS=10</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">37mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.2V) <strong>DCS=11</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">49mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <!-- IOH Rows (Split for clarity within 500px col) -->
    <tr>
      <td rowspan="4" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Ioh<br><span style="font-size:11px; color:#666;">DCS[1:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.2V) <strong>DCS=00</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">11mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.2V) <strong>DCS=01</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">21mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.2V) <strong>DCS=10</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">32mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.2V) <strong>DCS=11</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">42mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
  </tbody>
</table>

### 4.2.2 For 3.3V I/O Pins

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="150">
    <col width="100">
    <col width="450">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Power Domain</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Symbol</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Min</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Typ</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- 3.3V Input Section -->
    <tr>
      <td rowspan="5" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">3.3V Input</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vih</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level input voltage</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">2V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC+0.3V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level input voltage</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">-0.3V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0.8V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpu</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Pull-up resistor</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">26kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">47kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">72kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpd</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Pull-down resistor</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">27kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">54kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">267kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Iil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Input leakage current</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10µA</td>
    </tr>
    <!-- 3.3V Output Section -->
    <tr>
      <td rowspan="18" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">3.3V Output</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Voh</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output voltage</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">2.4V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vol</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output voltage</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0.4V</td>
    </tr>
    <!-- IOL Rows (8 configurations) -->
    <tr>
      <td rowspan="8" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Iol<br><span style="font-size:11px; color:#666;">DS[2:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=000</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">7mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=001</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=010</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">14mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=011</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">18mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=100</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">21mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=101</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">24mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=110</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">28mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Low level output current (Vpad=0.4V) <strong>DS=111</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">31mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <!-- IOH Rows (8 configurations) -->
    <tr>
      <td rowspan="8" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Ioh<br><span style="font-size:11px; color:#666;">DS[2:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=000</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">7mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=001</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=010</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">13mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=011</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">16mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=100</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">19mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=101</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">23mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=110</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">26mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">High level output current (Vpad=VCC−0.5V) <strong>DS=111</strong></td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">29mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
  </tbody>
</table>

### 4.3 Multiplexed Signal/Pin Functions

The **Function 0** through **7** signals is assigned to the I/O pins of K3.  
Most I/O pins of K3 are multi-function allowing them to be configured for one of several available functions using Multi-Function Pin Registers (MFPRs). Additionally, some functions can be configured to be present on several different pins.  
The assigned signals are organized by their functions (e.g. power supply, clock, etc.) which are arranged in groups according to their interfaces (e.g. JTAG, SPIx, etc.) as per description in the following subsections (sorted alphabetically for user convenience).

> **Note:** Definition of symbols used for signal/pin type:
>
> - **I** = Input  
> - **O** = Output  
> - **I/O** = Input/Output  
> - **OD** = Open-Drain  
> - **RO** = Reference output  

#### 4.3.1 JTAG – Primary

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Signal/Pin</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TCK</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Primary JTAG interface 1 test clock. Used for all transfers on the JTAG test interface.</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDI</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Primary JTAG interface 1 test data input. Used to send data from the JTAG controller to the K3 processor. This pin has an internal pullup resistor.</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDO</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Primary JTAG Interface 1 test data output. Used to return data from the K1 processor to the JTAG controller.</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TMS</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Primary JTAG Interface 1 test mode select. Used to select the test mode required from the JTAG controller. This pin has an internal pullup resistor.</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TRSTn</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Primary JTAG Interface 1 test reset. Used for IEEE 1194.1 test reset.</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_OUT</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">24 MHz VCXO output clock</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_REQ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">OCLK1 request</td>
    </tr>
  </tbody>
</table>

#### 4.3.2 Miscellaneous

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Signal/Pin</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MPLL_TST_CK</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PLL test pin</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MN_CLK_OUT</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Fractional (M/N) divided clock. Main PMU general purpose M/N fractional clock divider clock output. CLK_REQ must be set as Function 0 and pulled high for the 13 MHz clock to be output on GPIO[122] (MN_CLK_OUT).</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Sleep_OUT</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PMIC sleep setting</td>
    </tr>
  </tbody>
</table>

#### 4.3.3 SPIx

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Signal/Pin</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">SPIx_FRM</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Synchronous serial port frame 0/2. The serial frame sync can be configured as an output (master mode operation) or an input (slave mode operation).</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">SPIx_RXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Synchronous serial port receive data 0/2. Serial data latched using the bit clock.</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">SPIx_SCLK</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Synchronous serial port clock 0/2. The serial bit clock can be configured as an output (master mode operation) or an input (slave mode operation).</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">SPIx_TXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Synchronous serial port transmit data 0/2. Serial data driven out synchronously with the bit clock.</td>
    </tr>
  </tbody>
</table>

#### 4.3.4 TWSI

**Dedicated**

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Signal/Pin</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SDA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSI serial data/address signal</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SCL</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSI serial clock line signal</td>
    </tr>
  </tbody>
</table>

**Common**

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Signal/Pin</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">I²Cx_SCL</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O,OD</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSIx clock</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">I²Cx_SDA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O,OD</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSIx data</td>
    </tr>
  </tbody>
</table>

#### 4.3.5 UARTx

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Signal/Pin</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UARTx_CTSn</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx clear-to-send</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UARTx_RTSn</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx request-to-send</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UARTx_RXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx receive data</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UARTx_TXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx transmit data</td>
    </tr>
  </tbody>
</table>

#### 4.3.6 USB

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Signal/Pin</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">Type</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">USBx_N</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB D±</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">USBx_P</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VBUS_ON</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB VBUS present indicator</td>
    </tr>
  </tbody>
</table>

### 4.4 Multi-Function I/O Pin Assignments

The General-Purpose Input/Output (GPIO) module provides flexible pin control and signal multiplexing capabilities. Each GPIO pin can operate as a standard input/output or be configured for one of several alternate functions, allowing efficient connection between the system and on-chip peripherals.

The tables below provide a detailed description of the signal assignments for Function 0 through Function 6, organized according to their respective interface groups.

#### QSPI 1.8V/3.3V

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">QSPI_DAT3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">QSPI_DAT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">QSPI_DAT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">QSPI_DAT0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">QSPI_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">QSPI_CS0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CS0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">QSPI_CS1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CS1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
  </tbody>
</table>

#### SD/MMC1 1.8V/3.3V

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">MMC1_DAT3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[93]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDI</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">MMC1_DAT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[94]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TMS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">MMC1_DAT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[95]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">MMC1_DAT0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[96]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">MMC1_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[97]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">MMC1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[98]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TCK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SDA</td>
    </tr>
  </tbody>
</table>

#### PMIC [1.8V only]

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">RESET_IN_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">RESET_IN_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM10</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EXT_32K_IN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EXT_32K_IN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM11</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R_PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM12</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R_PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM13</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">VCXO_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM14</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PMIC_WDT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PMIC_WDT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM15</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PMIC_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PMIC_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM16</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PWR_SSP_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[120]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PWR_SSP_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[121]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PWR_SSP_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[122]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PWR_SSP_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[123]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PRI_TDI</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDI</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[124]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[17]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM6</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PRI_TMS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TMS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[125]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM7</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_RXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PRI_TCK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TCK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[126]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PRI_TDO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[127]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[16]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM9</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">PRI_TRST_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TRSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
  </tbody>
</table>

#### EMMC5 [1.8V only]

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[32]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[33]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[34]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[35]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[36]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D6</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D6</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_D7</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D7</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_DS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_DS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">EMMC_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
  </tbody>
</table>

#### GPIO1 1.8V/3.3V

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM6</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM7</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_ALERT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM9</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM10</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM13</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM14</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[16]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[16]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[17]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[17]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_CRS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_ID</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[18]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[18]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_COL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_VBUSON</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[19]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[19]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_PPS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DRV</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[20]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[20]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_D_DRV</td>
    </tr>
  </tbody>
</table>

#### GPIO2 1.8V/3.3V

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[21]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[21]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM15</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[28]</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[22]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[22]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM16</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[29]</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[23]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[23]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM17</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[24]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[24]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM18</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[25]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[25]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM19</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[26]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[26]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[27]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[27]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[28]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[28]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[29]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[29]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[30]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[30]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EDP0_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[31]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[31]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EDP1_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[32]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[32]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[33]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[33]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM6</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[34]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[34]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM7</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[35]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[35]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[36]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[36]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM9</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[37]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[37]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[38]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[38]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[39]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[39]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_CRS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[40]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[40]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_COL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR0_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[41]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[41]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_PPS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK32K_OUT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">IR0_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_RXD</td>
    </tr>
  </tbody>
</table>

#### GPIO3 [1.8V only]

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[42]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[42]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[43]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[43]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[44]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[44]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[45]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[45]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[46]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[46]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[47]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[47]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM5</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[48]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[48]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[49]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[49]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM7</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[50]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[50]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_MRLn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM8</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[51]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[51]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATNLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[52]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[52]/Strap[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM10</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[53]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[53]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM11</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[54]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[54]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINTEG</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM12</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[55]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[55]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM13</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[56]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[56]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM14</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[57]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[57]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EDP0_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM15</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[58]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[58]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_PPS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM16</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[59]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[59]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM17</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[60]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[60]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM18</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[61]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[61]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM19</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[62]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[62]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[63]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[63]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[18]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[64]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[64]/Strap[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[19]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[65]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[65]/Strap[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[20]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[66]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[66]/Strap[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[21]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[67]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[67]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[22]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[68]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[68]/Strap[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[69]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[69]/Strap[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_RXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[70]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[70]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_SCLK</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[71]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[71]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR0_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_FRM</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[72]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[72]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[73]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[73]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[74]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[74]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_REQ</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30H-1_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[75]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[75]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_PPS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_ALERT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_OUT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30H-2_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SDA</td>
    </tr>
  </tbody>
</table>

#### GPIO4 1.8V/3.3V

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[76]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[76]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[77]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[77]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[78]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[78]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[79]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[79]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[80]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[80]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[81]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[81]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[82]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[82]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[83]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[83]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[84]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[84]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_B_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[85]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[85]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_C_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[86]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[86]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DIR</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[87]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[87]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_MRLn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PRSNT2n</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[88]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[88]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATNLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_RXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[89]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[89]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[90]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[90]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_RXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[91]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[91]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[23]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINTEG</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[92]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[92]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[24]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[93]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[93]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[25]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_ALERT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[94]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[94]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[26]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[95]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[95]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[27]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_ID</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[96]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[96]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_VBUSON</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[97]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[97]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[98]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[98]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK32K_OUT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_ALERT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
  </tbody>
</table>

#### GPIO5 1.8V/3.3V

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 12px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Name</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Default Pull</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 0</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 1</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 2</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 3</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 4</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 5</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">Function 6</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[99]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[99]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[100]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[100]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK32K_OUT</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[101]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[101]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[102]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[102]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[103]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[103]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[104]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[104]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30H-1_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[105]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[105]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM17</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[106]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[106]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM18</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[107]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[107]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DIR</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM19</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[108]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[108]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">IR0_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[109]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[109]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[110]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[110]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM7</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[111]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[111]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">ucie_deSCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_INT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM8</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[112]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[112]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">ucie_deSDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_D_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[113]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[113]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[30]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[114]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[114]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[31]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[115]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[115]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[32]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[116]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[116]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_ID</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[33]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[117]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[117]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_VBUSON</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[34]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[118]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[118]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[35]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[119]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[119]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_INT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[120]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[120]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[121]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[121]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_MRLn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[122]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[122]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_ATNLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[123]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[123]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PWRLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[124]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[124]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_EINT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[125]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[125]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_EINTEG</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[126]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">UP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[126]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">GPIO_[127]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">DOWN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">ENABLE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[127]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_C_DRV</td>
    </tr>
  </tbody>
</table>

## 5. Electrical Characteristics

### 5.1 Pin AC/DC Operating Conditions

The following table describes the recommended operating conditions.

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Module</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Symbol/Pin</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Min</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Typ</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">CPU</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD08_X100</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.72V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.05V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD08_M1A100</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.72V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PLL</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL234</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL567</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL234</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL567</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PLL-DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL_DDR0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL_DDR1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD1V8_PLL_DDR0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD1V8_PLL_DDR1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">CSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_CSI0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_CSI1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_CSI2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_CSI0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_CSI1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_CSI2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VAA1V8_VDD2H_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD2H_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.01V/1.045V (LP5/LP4x)</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.05V/1.1V (LP5/LP4x)</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.12V/1.155V (LP5/LP4x)</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.47V/0.57V (LP5/LP4x)</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.5V/0.6V (LP5/LP4x)</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.57V/0.63V (LP5/LP4x)</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD12_DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.14V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.2V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.32V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">EDP</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_EDP0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">DVDD08_EDP0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">EDP1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_EDP1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">DVDD08_EDP1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">EMMC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_EMMC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_EMMC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">FUSE</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">FUSE_AVDD18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">GPIO</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_PMIC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V/2.97V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V/3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V/2.97V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V/3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V/2.97V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V/3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V/2.97V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V/3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_QSPI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V/2.97V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V/3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_MMC1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V/2.97V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V/3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">OSC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_OSC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_OSC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeA</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeA</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeC/USB3-B</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeC/USB3-B</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeD/USB3-C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeD/USB3-C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeE/USB3-D</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeE/USB3-D</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIe5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIe5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">UCIE</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCAON_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.84V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCIO_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.84V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCPLL_1P2V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.116V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.2V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.236V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDD_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.84V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDDBH_0V9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.855V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.9V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.945V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDDVPH0_0V9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.855V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.9V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.945V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">UFS</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UFS_VCC_1V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.71V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UFS_VCCQ_1V2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.14V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.2V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.32V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UFS_VDDU_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.76</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">USB2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_B_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_C_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_D_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_USB20_Host</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_B_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_C_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_D_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_USB20_Host</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_B_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.069V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_C_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.069V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_D_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.069V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_DRD_USB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.069V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_USB20_Host</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.069V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">USB3-DRD</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_DRD_USB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.744V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_DRD_USB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.674V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.8V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
  </tbody>
</table>

### 5.2 Absolute Maximum DC Ratings

#### 5.2.1 For Pins

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Module</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Symbol/Pin</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Min</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">CPU</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD08_X100</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.05V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD08_M1A100</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">Digital Power</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_M1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PLL</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL234</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL567</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL234</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL567</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PLL-DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL_DDR0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL_DDR1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD1V8_PLL_DDR0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD1V8_PLL_DDR1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">CSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_CSI0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_CSI1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_CSI2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_CSI0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_CSI1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_CSI2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VAA1V8_VDD2H_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD2H_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.12V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDDQ_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.57V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VDD0V8_DDR</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD12_DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.32V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_DSI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">EDP</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_EDP0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">DVDD08_EDP0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">EDP1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_EDP1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">DVDD08_EDP1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">EMMC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_EMMC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_EMMC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">FUSE</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">FUSE_AVDD18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">GPIO</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_PMIC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_QSPI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_MMC1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V/3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">OSC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_OSC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_OSC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeA</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeA</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeC/USB3-B</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeC/USB3-B</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeD/USB3-C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeD/USB3-C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIeE/USB3-D</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIeE/USB3-D</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">PICE PHY5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIe5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PCIe5</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">UCIE</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCAON_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.84V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCIO_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.84V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCPLL_1P2V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.236V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDD_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.84V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDDBH_0V9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.945V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDDVPH0_0V9</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.945V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">UFS</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UFS_VCC_1V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.96V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UFS_VCCQ_1V2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.32V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UFS_VDDU_0V8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">USB2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_B_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_C_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_D_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_USB20_Host</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_B_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_C_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_D_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_USB20_Host</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_B_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_C_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_D_USB20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_DRD_USB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_USB20_Host</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">3.63V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;">USB3-DRD</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_DRD_USB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">0.88V</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-weight: bold;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_DRD_USB</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-0.3V</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">1.98V</td></tr>
  </tbody>
</table>

#### 5.2.2 For Packages

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Item</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Symbol</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Min</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Operating Temperature (Industrial Standard)</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Ta</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-40°C</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">85°C</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Junction Temperature</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Tj</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">N/A</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">125°C</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">Storage Temperature</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Tstg</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-40°C</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">125°C</td>
    </tr>
  </tbody>
</table>

### 5.3 Thermal Characteristics

Thermal Resistance (Junction-to-Case): 0.23°C/W (with integrated heat spreader)

### 5.4 Pin Maximum Currents

TBD

### 5.5 Power On/Off Sequence

TBD

## 6. Reflow Profile

TBD
