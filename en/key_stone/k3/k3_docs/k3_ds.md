---
sidebar_position: 2
---

# K3 Datasheet

## PDF Version

Click to download [K3 Datasheet (PDF)](https://cdn-resource.spacemit.com/file/chip/K3/k3_datasheet_en.pdf)

## Proprietary, Confidentiality & Disclaimer

**Copyright © 2026 SpacemiT Inc. All rights reserved.**

Without the written approval of SpacemiT (Hangzhou) Technology Co. Ltd. (hereafter SpacemiT), no individual or entity may excerpt, copy or distribute any part or all of the content of this document in any form.

The copyrights of all materials and contents set forth herein are owned by SpacemiT and/or its subsidiaries, except for those specifically indicated as reference to any other party (if any).

The content of this document may be periodically updated due to product version upgrades or other reasons. Unless otherwise specified, this document is provided solely as a user guide, and THE INFORMATION AND ADVICE PROVIDED IN THIS DOCUMENT DO NOT CONSTITUTE ANY EXPLICIT OR IMPLIED WARRANTIES. TO THE EXTENT NOT PROHIBITED BY LAW, THE COMPANY SHALL NOT BE LIABLE FOR ANY FORM OF DAMAGE CAUSED BY THIS DOCUMENT.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| **V1.0** | 2026.04.30 |First Release |

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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 14px;">

  <colgroup>
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Source / Destination</th>
      <th style="text-align: center;">Internal Memory</th>
      <th style="text-align: center;">External Memory</th>
      <th style="text-align: center;">Internal Peripheral</th>
      <th style="text-align: center;">External Peripheral</th>
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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 14px;">

  <colgroup>
    <col width="100">
    <col width="300">
    <col width="600">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">No.</th>
      <th style="text-align: center;">Resource Reset Scheme</th>
      <th style="text-align: left;">Description</th>
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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 14px;">
  <colgroup>
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">
        Download Select<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_69</span>
      </th>
      <th style="text-align: center;">
        Download Mode<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_68</span>
      </th>
      <th style="text-align: center;">
        Boot Select 1<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_66</span>
      </th>
      <th style="text-align: center;">
        Boot Select 0<br><span style="font-weight: normal; font-size: 1em; color: #555;">GPIO_65</span>
      </th>
      <th style="text-align: center;">Boot Mode</th>
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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 14px;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Type</th>
      <th style="text-align: center;">Size</th>
      <th style="text-align: center;">Pin Pitch</th>
      <th style="text-align: center;">Pin Count</th>
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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="text-align: center;">A2</td><td style="text-align: left;">VSS</td><td style="text-align: center;">K20</td><td style="text-align: left;">AVDD08_PCIE1</td></tr>
    <tr><td style="text-align: center;">A3</td><td style="text-align: left;">DDR1_DQ_B_08</td><td style="text-align: center;">L1</td><td style="text-align: left;">DDR1_CKT_B</td></tr>
    <tr><td style="text-align: center;">A4</td><td style="text-align: left;">DDR1_DMI1_B</td><td style="text-align: center;">L2</td><td style="text-align: left;">DDR1_CKC_B</td></tr>
    <tr><td style="text-align: center;">A5</td><td style="text-align: left;">DDR1_DQ_B_09</td><td style="text-align: center;">L3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A6</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L4</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A7</td><td style="text-align: left;">PCIE5_TX0N</td><td style="text-align: center;">L5</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A8</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A9</td><td style="text-align: left;">PCIE4/USB3-D_TX0N</td><td style="text-align: center;">L7</td><td style="text-align: left;">DDR1_CA_A_01</td></tr>
    <tr><td style="text-align: center;">A10</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A11</td><td style="text-align: left;">PCIE3/USB3-C_TX0N</td><td style="text-align: center;">L9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A12</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L10</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A13</td><td style="text-align: left;">PCIE2/USB3-B_TX0N</td><td style="text-align: center;">L11</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A14</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A15</td><td style="text-align: left;">PCIE1_TX1P</td><td style="text-align: center;">L13</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">A16</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L14</td><td style="text-align: left;">AVSS_PCIEUSB</td></tr>
    <tr><td style="text-align: center;">A17</td><td style="text-align: left;">PCIE1_TX0N</td><td style="text-align: center;">L15</td><td style="text-align: left;">AVSS_PCIEUSB</td></tr>
    <tr><td style="text-align: center;">A18</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L16</td><td style="text-align: left;">AVSS_PCIEUSB</td></tr>
    <tr><td style="text-align: center;">A19</td><td style="text-align: left;">PCIE0_TX1P</td><td style="text-align: center;">L17</td><td style="text-align: left;">AVSS_PCIEUSB</td></tr>
    <tr><td style="text-align: center;">A20</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">L18</td><td style="text-align: left;">AVSS_PCIEUSB</td></tr>
    <tr><td style="text-align: center;">B1</td><td style="text-align: left;">VSS</td><td style="text-align: center;">L19</td><td style="text-align: left;">AVDD08_PCIE3/USB3-C</td></tr>
    <tr><td style="text-align: center;">B2</td><td style="text-align: left;">VSS</td><td style="text-align: center;">L20</td><td style="text-align: left;">AVDD08_PCIE2/USB3-B</td></tr>
    <tr><td style="text-align: center;">B3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">M1</td><td style="text-align: left;">DDR1_CKT_A</td></tr>
    <tr><td style="text-align: center;">B4</td><td style="text-align: left;">DDR1_DQ_B_11</td><td style="text-align: center;">M2</td><td style="text-align: left;">DDR1_CKC_A</td></tr>
    <tr><td style="text-align: center;">B5</td><td style="text-align: left;">DDR1_DQ_B_10</td><td style="text-align: center;">M3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B6</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">M4</td><td style="text-align: left;">DDR1_DQ_A_00</td></tr>
    <tr><td style="text-align: center;">B7</td><td style="text-align: left;">PCIE5_TX0P</td><td style="text-align: center;">M5</td><td style="text-align: left;">DDR1_DQ_A_02</td></tr>
    <tr><td style="text-align: center;">B8</td><td style="text-align: left;">PCIE5_REFCLK_N</td><td style="text-align: center;">M6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B9</td><td style="text-align: left;">PCIE4/USB3-D_TX0P</td><td style="text-align: center;">M7</td><td style="text-align: left;">DDR1_CA_A_00</td></tr>
    <tr><td style="text-align: center;">B10</td><td style="text-align: left;">PCIE4_REFCLK_P</td><td style="text-align: center;">M8</td><td style="text-align: left;">VDDQ_DDR</td></tr>
    <tr><td style="text-align: center;">B11</td><td style="text-align: left;">PCIE3/USB3-C_TX0P</td><td style="text-align: center;">M9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B12</td><td style="text-align: left;">PCIE3_REFCLK_N</td><td style="text-align: center;">M10</td><td style="text-align: left;">VDD0V8_DDR</td></tr>
    <tr><td style="text-align: center;">B13</td><td style="text-align: left;">PCIE2/USB3-B_TX0P</td><td style="text-align: center;">M11</td><td style="text-align: left;">AVDD18_PLL_DDR1</td></tr>
    <tr><td style="text-align: center;">B14</td><td style="text-align: left;">PCIE2_REFCLK_P</td><td style="text-align: center;">M12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B15</td><td style="text-align: left;">PCIE1_TX1N</td><td style="text-align: center;">M13</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B16</td><td style="text-align: left;">PCIE1_REFCLK_P</td><td style="text-align: center;">M14</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B17</td><td style="text-align: left;">PCIE1_TX0P</td><td style="text-align: center;">M15</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B18</td><td style="text-align: left;">USB20_B_USB_P</td><td style="text-align: center;">M16</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B19</td><td style="text-align: left;">PCIE0_TX1N</td><td style="text-align: center;">M17</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">B20</td><td style="text-align: left;">PCIE0_REFCLK_P</td><td style="text-align: center;">M18</td><td style="text-align: left;">AVSS_PCIEUSB</td></tr>
    <tr><td style="text-align: center;">C1</td><td style="text-align: left;">DDR1_DQ_B_00</td><td style="text-align: center;">M19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C2</td><td style="text-align: left;">DDR1_DQ_B_02</td><td style="text-align: center;">M20</td><td style="text-align: left;">AVDD08_PCIE2/USB3-B</td></tr>
    <tr><td style="text-align: center;">C3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">N1</td><td style="text-align: left;">DDR1_DQ_A_15</td></tr>
    <tr><td style="text-align: center;">C4</td><td style="text-align: left;">DDR1_DQS1_T_B</td><td style="text-align: center;">N2</td><td style="text-align: left;">DDR1_DQ_A_14</td></tr>
    <tr><td style="text-align: center;">C5</td><td style="text-align: left;">DDR1_DQS1_C_B</td><td style="text-align: center;">N3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C6</td><td style="text-align: left;">DDR1_ZN</td><td style="text-align: center;">N4</td><td style="text-align: left;">DDR1_DQ_A_01</td></tr>
    <tr><td style="text-align: center;">C7</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">N5</td><td style="text-align: left;">DDR1_DQ_A_03</td></tr>
    <tr><td style="text-align: center;">C8</td><td style="text-align: left;">PCIE5_REFCLK_P</td><td style="text-align: center;">N6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C9</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">N7</td><td style="text-align: left;">DDR1_CKE0_A</td></tr>
    <tr><td style="text-align: center;">C10</td><td style="text-align: left;">PCIE4_REFCLK_N</td><td style="text-align: center;">N8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C11</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">N9</td><td style="text-align: left;">VDD0V8_DDR</td></tr>
    <tr><td style="text-align: center;">C12</td><td style="text-align: left;">PCIE3_REFCLK_P</td><td style="text-align: center;">N10</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C13</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">N11</td><td style="text-align: left;">AVDD08_PLL_DDR1</td></tr>
    <tr><td style="text-align: center;">C14</td><td style="text-align: left;">PCIE2_REFCLK_N</td><td style="text-align: center;">N12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C15</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">N13</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">C16</td><td style="text-align: left;">PCIE1_REFCLK_N</td><td style="text-align: center;">N14</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C17</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">N15</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">C18</td><td style="text-align: left;">USB20_B_USB_M</td><td style="text-align: center;">N16</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">C19</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">N17</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">C20</td><td style="text-align: left;">PCIE0_REFCLK_N</td><td style="text-align: center;">N18</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D1</td><td style="text-align: left;">DDR1_DQ_B_03</td><td style="text-align: center;">N19</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">D2</td><td style="text-align: left;">DDR1_DQ_B_01</td><td style="text-align: center;">N20</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">P1</td><td style="text-align: left;">DDR1_DQ_A_13</td></tr>
    <tr><td style="text-align: center;">D4</td><td style="text-align: left;">VSS</td><td style="text-align: center;">P2</td><td style="text-align: left;">DDR1_DQ_A_12</td></tr>
    <tr><td style="text-align: center;">D5</td><td style="text-align: left;">VSS</td><td style="text-align: center;">P3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D6</td><td style="text-align: left;">DDR1_CKE1_B</td><td style="text-align: center;">P4</td><td style="text-align: left;">DDR1_DQS0_C_A</td></tr>
    <tr><td style="text-align: center;">D7</td><td style="text-align: left;">DDR1_CA_B_00</td><td style="text-align: center;">P5</td><td style="text-align: left;">DDR1_DQS0_T_A</td></tr>
    <tr><td style="text-align: center;">D8</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">P6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D9</td><td style="text-align: left;">PCIE5_RX0P</td><td style="text-align: center;">P7</td><td style="text-align: left;">DDR1_CS1_A</td></tr>
    <tr><td style="text-align: center;">D10</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">P8</td><td style="text-align: left;">VDDQ_DDR</td></tr>
    <tr><td style="text-align: center;">D11</td><td style="text-align: left;">USB20_D_USB_P</td><td style="text-align: center;">P9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D12</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">P10</td><td style="text-align: left;">VDD0V8_DDR</td></tr>
    <tr><td style="text-align: center;">D13</td><td style="text-align: left;">PCIE4/USB3-D_RX0N</td><td style="text-align: center;">P11</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D14</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">P12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D15</td><td style="text-align: left;">PCIE3/USB3-C_RX0N</td><td style="text-align: center;">P13</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D16</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">P14</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">D17</td><td style="text-align: left;">PCIE2/USB3-B_RX0P</td><td style="text-align: center;">P15</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D18</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">P16</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">D19</td><td style="text-align: left;">PCIE1_RX0P</td><td style="text-align: center;">P17</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">D20</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">P18</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">E1</td><td style="text-align: left;">DDR1_WCK_T_B_0</td><td style="text-align: center;">P19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E2</td><td style="text-align: left;">DDR1_WCK_C_B_0</td><td style="text-align: center;">P20</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">E3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">R1</td><td style="text-align: left;">DDR1_WCK_C_A_1</td></tr>
    <tr><td style="text-align: center;">E4</td><td style="text-align: left;">DDR1_WCK_T_B_1</td><td style="text-align: center;">R2</td><td style="text-align: left;">DDR1_WCK_T_A_1</td></tr>
    <tr><td style="text-align: center;">E5</td><td style="text-align: left;">DDR1_WCK_C_B_1</td><td style="text-align: center;">R3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">R4</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E7</td><td style="text-align: left;">DDR1_CS1_B</td><td style="text-align: center;">R5</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">R6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E9</td><td style="text-align: left;">PCIE5_RX0N</td><td style="text-align: center;">R7</td><td style="text-align: left;">VDDQ_DDR</td></tr>
    <tr><td style="text-align: center;">E10</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">R8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E11</td><td style="text-align: left;">USB20_D_USB_M</td><td style="text-align: center;">R9</td><td style="text-align: left;">VDD0V8_DDR</td></tr>
    <tr><td style="text-align: center;">E12</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">R10</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E13</td><td style="text-align: left;">PCIE4/USB3-D_RX0P</td><td style="text-align: center;">R11</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E14</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">R12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E15</td><td style="text-align: left;">PCIE3/USB3-C_RX0P</td><td style="text-align: center;">R13</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">E16</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">R14</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E17</td><td style="text-align: left;">PCIE2/USB3-B_RX0N</td><td style="text-align: center;">R15</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">E18</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">R16</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">E19</td><td style="text-align: left;">PCIE1_RX0N</td><td style="text-align: center;">R17</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">E20</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">R18</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F1</td><td style="text-align: left;">DDR1_DQS0_T_B</td><td style="text-align: center;">R19</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">F2</td><td style="text-align: left;">DDR1_DQS0_C_B</td><td style="text-align: center;">R20</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">T1</td><td style="text-align: left;">DDR1_DQS1_C_A</td></tr>
    <tr><td style="text-align: center;">F4</td><td style="text-align: left;">DDR1_DQ_B_12</td><td style="text-align: center;">T2</td><td style="text-align: left;">DDR1_DQS1_T_A</td></tr>
    <tr><td style="text-align: center;">F5</td><td style="text-align: left;">VSS</td><td style="text-align: center;">T3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">T4</td><td style="text-align: left;">DDR1_WCK_C_A_0</td></tr>
    <tr><td style="text-align: center;">F7</td><td style="text-align: left;">DDR1_CKE0_B</td><td style="text-align: center;">T5</td><td style="text-align: left;">DDR1_WCK_T_A_0</td></tr>
    <tr><td style="text-align: center;">F8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">T6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">T7</td><td style="text-align: left;">DDR1_CKE1_A</td></tr>
    <tr><td style="text-align: center;">F10</td><td style="text-align: left;">AVDD18_PCIE5</td><td style="text-align: center;">T8</td><td style="text-align: left;">VDDQ_DDR</td></tr>
    <tr><td style="text-align: center;">F11</td><td style="text-align: left;">AVDD18_PCIE4/USB3-D</td><td style="text-align: center;">T9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F12</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">T10</td><td style="text-align: left;">VDD0V8_DDR</td></tr>
    <tr><td style="text-align: center;">F13</td><td style="text-align: left;">AVDD18_B_USB20</td><td style="text-align: center;">T11</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F14</td><td style="text-align: left;">PCIE_USB_COMBO_ADTEST_0</td><td style="text-align: center;">T12</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">F15</td><td style="text-align: left;">AVDD18_USB20_HOST</td><td style="text-align: center;">T13</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F16</td><td style="text-align: left;">USB20_C_USB_M</td><td style="text-align: center;">T14</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">F17</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">T15</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F18</td><td style="text-align: left;">PCIE1_RX1N</td><td style="text-align: center;">T16</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">F19</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">T19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">F20</td><td style="text-align: left;">AVDD33_D_USB20</td><td style="text-align: center;">T20</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">G1</td><td style="text-align: left;">DDR1_DMI0_B</td><td style="text-align: center;">U1</td><td style="text-align: left;">DDR1_DMI1_A</td></tr>
    <tr><td style="text-align: center;">G2</td><td style="text-align: left;">VSS</td><td style="text-align: center;">U2</td><td style="text-align: left;">DDR1_DQ_A_11</td></tr>
    <tr><td style="text-align: center;">G3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">U3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G4</td><td style="text-align: left;">DDR1_DQ_B_13</td><td style="text-align: center;">U4</td><td style="text-align: left;">DDR1_DMI0_A</td></tr>
    <tr><td style="text-align: center;">G5</td><td style="text-align: left;">DDR1_DQ_B_15</td><td style="text-align: center;">U5</td><td style="text-align: left;">DDR1_DQ_A_04</td></tr>
    <tr><td style="text-align: center;">G6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">U6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G7</td><td style="text-align: left;">DDR1_CA_B_01</td><td style="text-align: center;">U7</td><td style="text-align: left;">DDR1_CS0_A_CA06</td></tr>
    <tr><td style="text-align: center;">G8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">U8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">U9</td><td style="text-align: left;">VDD0V8_DDR</td></tr>
    <tr><td style="text-align: center;">G10</td><td style="text-align: left;">AVDD18_PCIE5</td><td style="text-align: center;">U10</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G11</td><td style="text-align: left;">AVDD18_PCIE4/USB3-D</td><td style="text-align: center;">U11</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G12</td><td style="text-align: left;">AVDD18_C_USB20</td><td style="text-align: center;">U12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G13</td><td style="text-align: left;">AVDD18_PCIE1</td><td style="text-align: center;">U13</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">G14</td><td style="text-align: left;">AVDD18_PCIE1</td><td style="text-align: center;">U14</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G15</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">U15</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">G16</td><td style="text-align: left;">USB20_C_USB_P</td><td style="text-align: center;">U16</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G17</td><td style="text-align: left;">AVDD18_PCIE0</td><td style="text-align: center;">U19</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">G18</td><td style="text-align: left;">PCIE1_RX1P</td><td style="text-align: center;">U20</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">G19</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">V1</td><td style="text-align: left;">DDR1_DQ_A_10</td></tr>
    <tr><td style="text-align: center;">G20</td><td style="text-align: left;">AVDD33_C_USB20</td><td style="text-align: center;">V2</td><td style="text-align: left;">DDR1_DQ_A_09</td></tr>
    <tr><td style="text-align: center;">H1</td><td style="text-align: left;">DDR1_DQ_B_05</td><td style="text-align: center;">V3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H2</td><td style="text-align: left;">DDR1_DQ_B_04</td><td style="text-align: center;">V4</td><td style="text-align: left;">DDR1_DQ_A_07</td></tr>
    <tr><td style="text-align: center;">H3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">V5</td><td style="text-align: left;">DDR1_DQ_A_05</td></tr>
    <tr><td style="text-align: center;">H4</td><td style="text-align: left;">DDR1_DQ_B_14</td><td style="text-align: center;">V6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H5</td><td style="text-align: left;">DDR1_CA_B_03</td><td style="text-align: center;">V7</td><td style="text-align: left;">DDR1_CA_A_05</td></tr>
    <tr><td style="text-align: center;">H6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">V8</td><td style="text-align: left;">VDDQ_DDR</td></tr>
    <tr><td style="text-align: center;">H7</td><td style="text-align: left;">DDR1_CA_B_02</td><td style="text-align: center;">V9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">V10</td><td style="text-align: left;">VDD0V8_DDR</td></tr>
    <tr><td style="text-align: center;">H9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">V11</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H10</td><td style="text-align: left;">VSS</td><td style="text-align: center;">V12</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">H11</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">V13</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H12</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">V14</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">H13</td><td style="text-align: left;">AVDD18_PCIE3/USB3-C</td><td style="text-align: center;">V15</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H14</td><td style="text-align: left;">AVDD18_PCIE1</td><td style="text-align: center;">V16</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">H15</td><td style="text-align: left;">PCIE_USB_COMBO_ADTEST_1</td><td style="text-align: center;">V19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H16</td><td style="text-align: left;">AVDD18_PCIE0</td><td style="text-align: center;">V20</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">H17</td><td style="text-align: left;">AVDD18_PCIE0</td><td style="text-align: center;">W1</td><td style="text-align: left;">DDR1_DQ_A_08</td></tr>
    <tr><td style="text-align: center;">H18</td><td style="text-align: left;">AVDD08_D_USB20</td><td style="text-align: center;">W2</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H19</td><td style="text-align: left;">AVDD08_C_USB20</td><td style="text-align: center;">W3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">H20</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">W4</td><td style="text-align: left;">DDR1_DQ_A_06</td></tr>
    <tr><td style="text-align: center;">J1</td><td style="text-align: left;">DDR1_DQ_B_07</td><td style="text-align: center;">W5</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J2</td><td style="text-align: left;">DDR1_DQ_B_06</td><td style="text-align: center;">W6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">W7</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J4</td><td style="text-align: left;">DDR1_CA_A_03</td><td style="text-align: center;">W8</td><td style="text-align: left;">VDDQ_DDR</td></tr>
    <tr><td style="text-align: center;">J5</td><td style="text-align: left;">DDR1_CA_B_04</td><td style="text-align: center;">W9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">W10</td><td style="text-align: left;">VDD2H_DDR</td></tr>
    <tr><td style="text-align: center;">J7</td><td style="text-align: left;">DDR1_CS0_B_CA06</td><td style="text-align: center;">W11</td><td style="text-align: left;">VAA18_VDD2H_DDR</td></tr>
    <tr><td style="text-align: center;">J8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">W12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">W13</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">J10</td><td style="text-align: left;">VSS</td><td style="text-align: center;">W14</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">W15</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">J12</td><td style="text-align: left;">AVDD18_D_USB20</td><td style="text-align: center;">W16</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J13</td><td style="text-align: left;">AVDD18_PCIE3/USB3-C</td><td style="text-align: center;">W17</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J14</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">W18</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">J15</td><td style="text-align: left;">AVDD18_PCIE2/USB3-B</td><td style="text-align: center;">W19</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">J16</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">W20</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J17</td><td style="text-align: left;">AVDD08_PCIE5</td><td style="text-align: center;">Y1</td><td style="text-align: left;">DDR1_RESET_N</td></tr>
    <tr><td style="text-align: center;">J18</td><td style="text-align: left;">AVDD08_PCIE4/USB3-D</td><td style="text-align: center;">Y2</td><td style="text-align: left;">DDR1_PWROK</td></tr>
    <tr><td style="text-align: center;">J19</td><td style="text-align: left;">AVDD08_PCIE1</td><td style="text-align: center;">Y3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">J20</td><td style="text-align: left;">AVDD08_PCIE1</td><td style="text-align: center;">Y4</td><td style="text-align: left;">DDR1_DTO</td></tr>
    <tr><td style="text-align: center;">K1</td><td style="text-align: left;">VSS</td><td style="text-align: center;">Y5</td><td style="text-align: left;">DDR1_ATO</td></tr>
    <tr><td style="text-align: center;">K2</td><td style="text-align: left;">VSS</td><td style="text-align: center;">Y6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">K3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">Y7</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">K4</td><td style="text-align: left;">DDR1_CA_A_02</td><td style="text-align: center;">Y8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">K5</td><td style="text-align: left;">DDR1_CA_A_04</td><td style="text-align: center;">Y9</td><td style="text-align: left;">VDDQ_DDR</td></tr>
    <tr><td style="text-align: center;">K6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">Y10</td><td style="text-align: left;">VDD2H_DDR</td></tr>
    <tr><td style="text-align: center;">K7</td><td style="text-align: left;">DDR1_CA_B_05</td><td style="text-align: center;">Y11</td><td style="text-align: left;">VAA18_VDD2H_DDR</td></tr>
    <tr><td style="text-align: center;">K8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">Y12</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">K9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">Y13</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">K10</td><td style="text-align: left;">VSS</td><td style="text-align: center;">Y14</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">K11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">Y15</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">K12</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">Y16</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">K13</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">Y17</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">K14</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">Y18</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">K15</td><td style="text-align: left;">AVDD18_PCIE2/USB3-B</td><td style="text-align: center;">Y19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">K16</td><td style="text-align: left;">AVSS_PCIEUSB</td><td style="text-align: center;">Y20</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">K17</td><td style="text-align: left;">AVDD08_PCIE5</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
    <tr><td style="text-align: center;">K18</td><td style="text-align: left;">AVDD08_PCIE4/USB3-D</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
    <tr><td style="text-align: center;">K19</td><td style="text-align: left;">AVDD08_PCIE3/USB3-C</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
  </tbody>
</table>

#### 4.1.2 (A~Y, 21~40)

<img src="static/k3_pinmap_a-y_21-40.png" alt="" width="800">

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: center;">A21</td>
      <td style="text-align: left;">PCIE0_TX0N</td>
      <td style="text-align: center;">L21</td>
      <td style="text-align: left;">AVDD08_PCIE0</td>
    </tr>
    <tr>
      <td style="text-align: center;">A22</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">L22</td>
      <td style="text-align: left;">AVDD08_B_USB20</td>
    </tr>
    <tr>
      <td style="text-align: center;">A23</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[2]</td>
      <td style="text-align: center;">L23</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="text-align: center;">A24</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">L24</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="text-align: center;">A25</td>
      <td style="text-align: left;">UCIE_EW_TXCKN_M0</td>
      <td style="text-align: center;">L25</td>
      <td style="text-align: left;">UCIE_VDDBH_0V9</td>
    </tr>
    <tr>
      <td style="text-align: center;">A26</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[8]</td>
      <td style="text-align: center;">L26</td>
      <td style="text-align: left;">UCIE_VCCPLL_1P2V</td>
    </tr>
    <tr>
      <td style="text-align: center;">A27</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">L27</td>
      <td style="text-align: left;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="text-align: center;">A28</td>
      <td style="text-align: left;">UCIE_EW_RXCKP_M0</td>
      <td style="text-align: center;">L28</td>
      <td style="text-align: left;">UCIE_VCCIO_0V8</td>
    </tr>
    <tr>
      <td style="text-align: center;">A29</td>
      <td style="text-align: left;">UCIE_EW_RXCKSB_M0</td>
      <td style="text-align: center;">L29</td>
      <td style="text-align: left;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="text-align: center;">A30</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">L30</td>
      <td style="text-align: left;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="text-align: center;">A31</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[7]</td>
      <td style="text-align: center;">L31</td>
      <td style="text-align: left;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="text-align: center;">A32</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[2]</td>
      <td style="text-align: center;">L32</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">A33</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">L33</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">A34</td>
      <td style="text-align: left;">GPIO[2]_21</td>
      <td style="text-align: center;">L34</td>
      <td style="text-align: left;">GPIO[3]_45</td>
    </tr>
    <tr>
      <td style="text-align: center;">A35</td>
      <td style="text-align: left;">GPIO[2]_25</td>
      <td style="text-align: center;">L35</td>
      <td style="text-align: left;">GPIO[3]_50</td>
    </tr>
    <tr>
      <td style="text-align: center;">A36</td>
      <td style="text-align: left;">GPIO[2]_29</td>
      <td style="text-align: center;">L36</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">A37</td>
      <td style="text-align: left;">GPIO[2]_32</td>
      <td style="text-align: center;">L37</td>
      <td style="text-align: left;">GPIO[3]_57</td>
    </tr>
    <tr>
      <td style="text-align: center;">A38</td>
      <td style="text-align: left;">GPIO[2]_34</td>
      <td style="text-align: center;">L38</td>
      <td style="text-align: left;">GPIO[3]_60</td>
    </tr>
    <tr>
      <td style="text-align: center;">A39</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">L39</td>
      <td style="text-align: left;">GPIO[3]_66</td>
    </tr>
    <tr>
      <td style="text-align: center;">B21</td>
      <td style="text-align: left;">PCIE0_TX0P</td>
      <td style="text-align: center;">L40</td>
      <td style="text-align: left;">GPIO[3]_72</td>
    </tr>
    <tr>
      <td style="text-align: center;">B22</td>
      <td style="text-align: left;">USB20_HOST_M</td>
      <td style="text-align: center;">M21</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="text-align: center;">B23</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[5]</td>
      <td style="text-align: center;">M22</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="text-align: center;">B24</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[3]</td>
      <td style="text-align: center;">M23</td>
      <td style="text-align: left;">AVSS_USB20_HOST</td>
    </tr>
    <tr>
      <td style="text-align: center;">B25</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">M24</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="text-align: center;">B26</td>
      <td style="text-align: left;">UCIE_EW_TXCKP_M0</td>
      <td style="text-align: center;">M25</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">B27</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[14]</td>
      <td style="text-align: center;">M26</td>
      <td style="text-align: left;">UCIE_VDDVPH0_0V9</td>
    </tr>
    <tr>
      <td style="text-align: center;">B28</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">M27</td>
      <td style="text-align: left;">UCIE_VDDVPH0_0V9</td>
    </tr>
    <tr>
      <td style="text-align: center;">B29</td>
      <td style="text-align: left;">UCIE_EW_RXCKN_M0</td>
      <td style="text-align: center;">M28</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">B30</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[15]</td>
      <td style="text-align: center;">M29</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">B31</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">M30</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">B32</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[5]</td>
      <td style="text-align: center;">M31</td>
      <td style="text-align: left;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="text-align: center;">B33</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">M32</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">B34</td>
      <td style="text-align: left;">GPIO[2]_22</td>
      <td style="text-align: center;">M33</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">B35</td>
      <td style="text-align: left;">GPIO[2]_26</td>
      <td style="text-align: center;">M34</td>
      <td style="text-align: left;">GPIO[3]_46</td>
    </tr>
    <tr>
      <td style="text-align: center;">B36</td>
      <td style="text-align: left;">GPIO[2]_30</td>
      <td style="text-align: center;">M35</td>
      <td style="text-align: left;">GPIO[3]_51</td>
    </tr>
    <tr>
      <td style="text-align: center;">B37</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">M36</td>
      <td style="text-align: left;">GPIO[3]_58</td>
    </tr>
    <tr>
      <td style="text-align: center;">B38</td>
      <td style="text-align: left;">GPIO[2]_33</td>
      <td style="text-align: center;">M37</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">B39</td>
      <td style="text-align: left;">GPIO[2]_38</td>
      <td style="text-align: center;">M38</td>
      <td style="text-align: left;">GPIO[3]_61</td>
    </tr>
    <tr>
      <td style="text-align: center;">B40</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">M39</td>
      <td style="text-align: left;">GPIO[3]_67</td>
    </tr>
    <tr>
      <td style="text-align: center;">C21</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">M40</td>
      <td style="text-align: left;">GPIO[3]_73</td>
    </tr>
    <tr>
      <td style="text-align: center;">C22</td>
      <td style="text-align: left;">USB20_HOST_P</td>
      <td style="text-align: center;">N21</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C23</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">N22</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C24</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[4]</td>
      <td style="text-align: center;">N23</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C25</td>
      <td style="text-align: left;">UCIE_EW_TXTRK_M0</td>
      <td style="text-align: center;">N24</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C26</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">N25</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C27</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[11]</td>
      <td style="text-align: center;">N26</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C28</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[11]</td>
      <td style="text-align: center;">N27</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C29</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">N28</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C30</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[12]</td>
      <td style="text-align: center;">N29</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C31</td>
      <td style="text-align: left;">UCIE_EW_RXTRK_M0</td>
      <td style="text-align: center;">N30</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C32</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">N31</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C33</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">N32</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C34</td>
      <td style="text-align: left;">GPIO[2]_23</td>
      <td style="text-align: center;">N33</td>
      <td style="text-align: left;">DTEST_PAD</td>
    </tr>
    <tr>
      <td style="text-align: center;">C35</td>
      <td style="text-align: left;">GPIO[2]_27</td>
      <td style="text-align: center;">N34</td>
      <td style="text-align: left;">ATEST_PAD</td>
    </tr>
    <tr>
      <td style="text-align: center;">C36</td>
      <td style="text-align: left;">GPIO[2]_31</td>
      <td style="text-align: center;">N35</td>
      <td style="text-align: left;">GPIO[3]_52</td>
    </tr>
    <tr>
      <td style="text-align: center;">C37</td>
      <td style="text-align: left;">GPIO[2]_35</td>
      <td style="text-align: center;">N38</td>
      <td style="text-align: left;">GPIO[3]_62</td>
    </tr>
    <tr>
      <td style="text-align: center;">C38</td>
      <td style="text-align: left;">GPIO[2]_36</td>
      <td style="text-align: center;">N39</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">C39</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">N40</td>
      <td style="text-align: left;">GPIO[3]_74</td>
    </tr>
    <tr>
      <td style="text-align: center;">C40</td>
      <td style="text-align: left;">GPIO[2]_40</td>
      <td style="text-align: center;">P21</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D21</td>
      <td style="text-align: left;">PCIE0_RX1P</td>
      <td style="text-align: center;">P22</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D22</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">P23</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D23</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[0]</td>
      <td style="text-align: center;">P24</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D24</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">P25</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D25</td>
      <td style="text-align: left;">UCIE_EW_TXVLD_M0</td>
      <td style="text-align: center;">P26</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D26</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[12]</td>
      <td style="text-align: center;">P27</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D27</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">P28</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D28</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[10]</td>
      <td style="text-align: center;">P29</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D29</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[14]</td>
      <td style="text-align: center;">P30</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D30</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">P31</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D31</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[6]</td>
      <td style="text-align: center;">P32</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D32</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[1]</td>
      <td style="text-align: center;">P33</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D33</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">P34</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D34</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">P35</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D35</td>
      <td style="text-align: left;">GPIO[2]_28</td>
      <td style="text-align: center;">P36</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D38</td>
      <td style="text-align: left;">GPIO[2]_37</td>
      <td style="text-align: center;">P37</td>
      <td style="text-align: left;">EMMC_DS</td>
    </tr>
    <tr>
      <td style="text-align: center;">D39</td>
      <td style="text-align: left;">GPIO[2]_39</td>
      <td style="text-align: center;">P38</td>
      <td style="text-align: left;">GPIO[3]_63</td>
    </tr>
    <tr>
      <td style="text-align: center;">D40</td>
      <td style="text-align: left;">GPIO[2]_41</td>
      <td style="text-align: center;">P39</td>
      <td style="text-align: left;">GPIO[3]_68</td>
    </tr>
    <tr>
      <td style="text-align: center;">E21</td>
      <td style="text-align: left;">PCIE0_RX1N</td>
      <td style="text-align: center;">P40</td>
      <td style="text-align: left;">GPIO[3]_75</td>
    </tr>
    <tr>
      <td style="text-align: center;">E22</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">R21</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E23</td>
      <td style="text-align: left;">UCIE_EW_TXDATASB_M0</td>
      <td style="text-align: center;">R22</td>
      <td style="text-align: left;">AVDD08_OSC</td>
    </tr>
    <tr>
      <td style="text-align: center;">E24</td>
      <td style="text-align: left;">UCIE_EW_O_CKNT</td>
      <td style="text-align: center;">R23</td>
      <td style="text-align: left;">AVDD18_OSC</td>
    </tr>
    <tr>
      <td style="text-align: center;">E25</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">R24</td>
      <td style="text-align: left;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="text-align: center;">E26</td>
      <td style="text-align: left;">UCIE_EW_TXCKSB_M0</td>
      <td style="text-align: center;">R25</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E27</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[13]</td>
      <td style="text-align: center;">R26</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E28</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">R27</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E29</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[8]</td>
      <td style="text-align: center;">R28</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E30</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[9]</td>
      <td style="text-align: center;">R29</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E31</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">R30</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E32</td>
      <td style="text-align: left;">UCIE_EW_RXDATASB_M0</td>
      <td style="text-align: center;">R31</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E33</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">R32</td>
      <td style="text-align: left;">VCC18_GPIO2</td>
    </tr>
    <tr>
      <td style="text-align: center;">E34</td>
      <td style="text-align: left;">GPIO[2]_24</td>
      <td style="text-align: center;">R33</td>
      <td style="text-align: left;">VCC18_GPIO2</td>
    </tr>
    <tr>
      <td style="text-align: center;">E35</td>
      <td style="text-align: left;">PMIC_INT_N</td>
      <td style="text-align: center;">R34</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E36</td>
      <td style="text-align: left;">PWR_SSP_SCLK</td>
      <td style="text-align: center;">R35</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E37</td>
      <td style="text-align: left;">PMIC_WDT_N</td>
      <td style="text-align: center;">R36</td>
      <td style="text-align: left;">EMMC_CLK</td>
    </tr>
    <tr>
      <td style="text-align: center;">E38</td>
      <td style="text-align: left;">PRI_TDO</td>
      <td style="text-align: center;">R37</td>
      <td style="text-align: left;">EMMC_CMD</td>
    </tr>
    <tr>
      <td style="text-align: center;">E39</td>
      <td style="text-align: left;">PRI_TRST_N</td>
      <td style="text-align: center;">R38</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">E40</td>
      <td style="text-align: left;">PWR_SSP_TXD</td>
      <td style="text-align: center;">R39</td>
      <td style="text-align: left;">EMMC_D5</td>
    </tr>
    <tr>
      <td style="text-align: center;">F21</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">R40</td>
      <td style="text-align: left;">EMMC_D3</td>
    </tr>
    <tr>
      <td style="text-align: center;">F22</td>
      <td style="text-align: left;">PCIE0_RX0P</td>
      <td style="text-align: center;">T21</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F23</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">T22</td>
      <td style="text-align: left;">AVDD08_PLL234</td>
    </tr>
    <tr>
      <td style="text-align: center;">F24</td>
      <td style="text-align: left;">UCIE_EW_O_CKPT</td>
      <td style="text-align: center;">T23</td>
      <td style="text-align: left;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="text-align: center;">F25</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[7]</td>
      <td style="text-align: center;">T24</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F26</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">T25</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F27</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[9]</td>
      <td style="text-align: center;">T26</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F28</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[15]</td>
      <td style="text-align: center;">T30</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F29</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">T31</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F30</td>
      <td style="text-align: left;">UCIE_EW_RXVLD_M0</td>
      <td style="text-align: center;">T32</td>
      <td style="text-align: left;">VCC1833_GPIO2</td>
    </tr>
    <tr>
      <td style="text-align: center;">F31</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[3]</td>
      <td style="text-align: center;">T33</td>
      <td style="text-align: left;">VCC1833_GPIO2</td>
    </tr>
    <tr>
      <td style="text-align: center;">F32</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">T34</td>
      <td style="text-align: left;">AVDD18_FUSE</td>
    </tr>
    <tr>
      <td style="text-align: center;">F33</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">T35</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F34</td>
      <td style="text-align: left;">PRI_TMS</td>
      <td style="text-align: center;">T36</td>
      <td style="text-align: left;">EMMC_D4</td>
    </tr>
    <tr>
      <td style="text-align: center;">F35</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">T37</td>
      <td style="text-align: left;">EMMC_D1</td>
    </tr>
    <tr>
      <td style="text-align: center;">F36</td>
      <td style="text-align: left;">PWR_SSP_RXD</td>
      <td style="text-align: center;">T38</td>
      <td style="text-align: left;">EMMC_D6</td>
    </tr>
    <tr>
      <td style="text-align: center;">F37</td>
      <td style="text-align: left;">EXT_32K_IN</td>
      <td style="text-align: center;">T39</td>
      <td style="text-align: left;">EMMC_D2</td>
    </tr>
    <tr>
      <td style="text-align: center;">F38</td>
      <td style="text-align: left;">PWR_SCL</td>
      <td style="text-align: center;">T40</td>
      <td style="text-align: left;">EMMC_D7</td>
    </tr>
    <tr>
      <td style="text-align: center;">F39</td>
      <td style="text-align: left;">PRI_TDI</td>
      <td style="text-align: center;">U21</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">F40</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">U22</td>
      <td style="text-align: left;">PCIE/USB3_RCAL</td>
    </tr>
    <tr>
      <td style="text-align: center;">G21</td>
      <td style="text-align: left;">AVDD33_USB20_HOST</td>
      <td style="text-align: center;">U23</td>
      <td style="text-align: left;">AVDD18_PLL234</td>
    </tr>
    <tr>
      <td style="text-align: center;">G22</td>
      <td style="text-align: left;">PCIE0_RX0N</td>
      <td style="text-align: center;">U24</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G23</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">U25</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G24</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">U26</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G25</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[6]</td>
      <td style="text-align: center;">U30</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G26</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[1]</td>
      <td style="text-align: center;">U31</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G27</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">U32</td>
      <td style="text-align: left;">VCC18_PMIC</td>
    </tr>
    <tr>
      <td style="text-align: center;">G28</td>
      <td style="text-align: left;">UCIE_EW_TXDATA_M0[10]</td>
      <td style="text-align: center;">U33</td>
      <td style="text-align: left;">VCC18_PMIC</td>
    </tr>
    <tr>
      <td style="text-align: center;">G29</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[13]</td>
      <td style="text-align: center;">U34</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G30</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">U35</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G31</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[4]</td>
      <td style="text-align: center;">U36</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G32</td>
      <td style="text-align: left;">UCIE_EW_RXDATA_M0[0]</td>
      <td style="text-align: center;">U37</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G33</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">U38</td>
      <td style="text-align: left;">EMMC_D0</td>
    </tr>
    <tr>
      <td style="text-align: center;">G34</td>
      <td style="text-align: left;">PRI_TCK</td>
      <td style="text-align: center;">U39</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G35</td>
      <td style="text-align: left;">VCXO_EN</td>
      <td style="text-align: center;">U40</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G38</td>
      <td style="text-align: left;">PWR_SDA</td>
      <td style="text-align: center;">V21</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">G39</td>
      <td style="text-align: left;">RESET_IN_N</td>
      <td style="text-align: center;">V22</td>
      <td style="text-align: left;">AVDD18_PLL567</td>
    </tr>
    <tr>
      <td style="text-align: center;">G40</td>
      <td style="text-align: left;">PWR_SSP_FRM</td>
      <td style="text-align: center;">V23</td>
      <td style="text-align: left;">AVDD08_PLL567</td>
    </tr>
    <tr>
      <td style="text-align: center;">H21</td>
      <td style="text-align: left;">AVDD33_B_USB20</td>
      <td style="text-align: center;">V24</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H22</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">V25</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H23</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">V26</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H24</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">V27</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H25</td>
      <td style="text-align: left;">UCIE_EW_ATEST</td>
      <td style="text-align: center;">V28</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H26</td>
      <td style="text-align: left;">UCIE_BGR_EAREFCLKN</td>
      <td style="text-align: center;">V29</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H27</td>
      <td style="text-align: left;">UCIE_VDD_0V8</td>
      <td style="text-align: center;">V30</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H28</td>
      <td style="text-align: left;">UCIE_EW_VCTRL_EXT</td>
      <td style="text-align: center;">V31</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H29</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">V32</td>
      <td style="text-align: left;">VCC18_GPIO3</td>
    </tr>
    <tr>
      <td style="text-align: center;">H30</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">V33</td>
      <td style="text-align: left;">VCC18_GPIO3</td>
    </tr>
    <tr>
      <td style="text-align: center;">H31</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">V34</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H32</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">V35</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H33</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">V36</td>
      <td style="text-align: left;">MIPI_CSI2_D3N</td>
    </tr>
    <tr>
      <td style="text-align: center;">H34</td>
      <td style="text-align: left;">GPIO[3]_42</td>
      <td style="text-align: center;">V37</td>
      <td style="text-align: left;">MIPI_CSI2_D3P</td>
    </tr>
    <tr>
      <td style="text-align: center;">H35</td>
      <td style="text-align: left;">GPIO[3]_47</td>
      <td style="text-align: center;">V38</td>
      <td style="text-align: left;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="text-align: center;">H36</td>
      <td style="text-align: left;">GPIO[3]_53</td>
      <td style="text-align: center;">V39</td>
      <td style="text-align: left;">MIPI_CSI2_D2N</td>
    </tr>
    <tr>
      <td style="text-align: center;">H37</td>
      <td style="text-align: left;">GPIO[3]_55</td>
      <td style="text-align: center;">V40</td>
      <td style="text-align: left;">MIPI_CSI2_D2P</td>
    </tr>
    <tr>
      <td style="text-align: center;">H38</td>
      <td style="text-align: left;">GPIO[3]_54</td>
      <td style="text-align: center;">W21</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H39</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">W22</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">H40</td>
      <td style="text-align: left;">GPIO[3]_69</td>
      <td style="text-align: center;">W23</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J21</td>
      <td style="text-align: left;">AVDD08_PCIE0</td>
      <td style="text-align: center;">W24</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J22</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">W25</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J23</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">W26</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J24</td>
      <td style="text-align: left;">UCIE_VCCAON_0V8</td>
      <td style="text-align: center;">W27</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J25</td>
      <td style="text-align: left;">UCIE_VCCAON_0V8</td>
      <td style="text-align: center;">W28</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J26</td>
      <td style="text-align: left;">UCIE_BGR_EAREFCLKP</td>
      <td style="text-align: center;">W29</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J27</td>
      <td style="text-align: left;">UCIE_VDD_0V8</td>
      <td style="text-align: center;">W30</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J28</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">W31</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J29</td>
      <td style="text-align: left;">UCIE_VCCIO_0V8</td>
      <td style="text-align: center;">W32</td>
      <td style="text-align: left;">AVDD08_EMMC</td>
    </tr>
    <tr>
      <td style="text-align: center;">J30</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">W33</td>
      <td style="text-align: left;">AVDD08_EMMC</td>
    </tr>
    <tr>
      <td style="text-align: center;">J31</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">W34</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J32</td>
      <td style="text-align: left;">XI_PAD</td>
      <td style="text-align: center;">W35</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J33</td>
      <td style="text-align: left;">AVSS_OSCPLL234567</td>
      <td style="text-align: center;">W36</td>
      <td style="text-align: left;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="text-align: center;">J34</td>
      <td style="text-align: left;">GPIO[3]_43</td>
      <td style="text-align: center;">W37</td>
      <td style="text-align: left;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="text-align: center;">J35</td>
      <td style="text-align: left;">GPIO[3]_48</td>
      <td style="text-align: center;">W38</td>
      <td style="text-align: left;">MIPI_CSI3_CLKN</td>
    </tr>
    <tr>
      <td style="text-align: center;">J36</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">W39</td>
      <td style="text-align: left;">MIPI_CSI3_CLKP</td>
    </tr>
    <tr>
      <td style="text-align: center;">J37</td>
      <td style="text-align: left;">GPIO[3]_56</td>
      <td style="text-align: center;">W40</td>
      <td style="text-align: left;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="text-align: center;">J38</td>
      <td style="text-align: left;">GPIO[3]_59</td>
      <td style="text-align: center;">Y21</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J39</td>
      <td style="text-align: left;">GPIO[3]_64</td>
      <td style="text-align: center;">Y22</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">J40</td>
      <td style="text-align: left;">GPIO[3]_70</td>
      <td style="text-align: center;">Y23</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K21</td>
      <td style="text-align: left;">AVDD08_PCIE0</td>
      <td style="text-align: center;">Y24</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K22</td>
      <td style="text-align: left;">AVDD08_USB20_HOST</td>
      <td style="text-align: center;">Y25</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K23</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">Y26</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K24</td>
      <td style="text-align: left;">AVSS_PCIEUSB</td>
      <td style="text-align: center;">Y27</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K25</td>
      <td style="text-align: left;">UCIE_VCCAON_0V8</td>
      <td style="text-align: center;">Y28</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K26</td>
      <td style="text-align: left;">UCIE_VCCPLL_1P2V</td>
      <td style="text-align: center;">Y29</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K27</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">Y30</td>
      <td style="text-align: left;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K28</td>
      <td style="text-align: left;">UCIE_VCCIO_0V8</td>
      <td style="text-align: center;">Y31</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K29</td>
      <td style="text-align: left;">UCIE_VCCIO_0V8</td>
      <td style="text-align: center;">Y32</td>
      <td style="text-align: left;">VCC18_EMMC</td>
    </tr>
    <tr>
      <td style="text-align: center;">K30</td>
      <td style="text-align: left;">UCIE_VCCIO_0V8</td>
      <td style="text-align: center;">Y33</td>
      <td style="text-align: left;">VCC18_EMMC</td>
    </tr>
    <tr>
      <td style="text-align: center;">K31</td>
      <td style="text-align: left;">VSS_UCIE</td>
      <td style="text-align: center;">Y34</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K32</td>
      <td style="text-align: left;">XO_PAD</td>
      <td style="text-align: center;">Y35</td>
      <td style="text-align: left;">VSS</td>
    </tr>
    <tr>
      <td style="text-align: center;">K33</td>
      <td style="text-align: left;">AVSS_OSCPLL234567</td>
      <td style="text-align: center;">Y36</td>
      <td style="text-align: left;">MIPI_CSI2_D1P</td>
    </tr>
    <tr>
      <td style="text-align: center;">K34</td>
      <td style="text-align: left;">GPIO[3]_44</td>
      <td style="text-align: center;">Y37</td>
      <td style="text-align: left;">MIPI_CSI2_D1N</td>
    </tr>
    <tr>
      <td style="text-align: center;">K35</td>
      <td style="text-align: left;">GPIO[3]_49</td>
      <td style="text-align: center;">Y38</td>
      <td style="text-align: left;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="text-align: center;">K38</td>
      <td style="text-align: left;">VSS</td>
      <td style="text-align: center;">Y39</td>
      <td style="text-align: left;">MIPI_CSI2_D0P</td>
    </tr>
    <tr>
      <td style="text-align: center;">K39</td>
      <td style="text-align: left;">GPIO[3]_65</td>
      <td style="text-align: center;">Y40</td>
      <td style="text-align: left;">MIPI_CSI2_D0N</td>
    </tr>
    <tr>
      <td style="text-align: center;">K40</td>
      <td style="text-align: left;">GPIO[3]_71</td>
      <td style="text-align: center;"></td>
      <td style="text-align: left;"></td>
    </tr>
  </tbody>
</table>

#### 4.1.3 (AA~AY, 1~20)

<img src="static/k3_pinmap_aa-ay_1-20.png" alt="" width="800">

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="text-align: center;">AA1</td><td style="text-align: left;">DDR0_DQ_B_15</td><td style="text-align: center;">AL1</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA2</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL2</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA4</td><td style="text-align: left;">DDR0_ATO</td><td style="text-align: center;">AL4</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA5</td><td style="text-align: left;">DDR0_PWROK</td><td style="text-align: center;">AL5</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA6</td><td style="text-align: left;">DDR0_DTO</td><td style="text-align: center;">AL6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA7</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL7</td><td style="text-align: left;">DDR0_CA_A_05</td></tr>
    <tr><td style="text-align: center;">AA8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">AL8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA10</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AL10</td><td style="text-align: left;">AVSS_PLL1</td></tr>
    <tr><td style="text-align: center;">AA11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL11</td><td style="text-align: left;">AVDD18_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AA12</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA13</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL13</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA14</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL14</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AA15</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL15</td><td style="text-align: left;">AVDD18_EDP1</td></tr>
    <tr><td style="text-align: center;">AA16</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL16</td><td style="text-align: left;">AVDD18_EDP1</td></tr>
    <tr><td style="text-align: center;">AA17</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL17</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AA18</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL18</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">AA19</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL19</td><td style="text-align: left;">VCC1833_QSPI</td></tr>
    <tr><td style="text-align: center;">AA20</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL20</td><td style="text-align: left;">VCC1833_SD</td></tr>
    <tr><td style="text-align: center;">AB1</td><td style="text-align: left;">DDR0_DQ_B_13</td><td style="text-align: center;">AM1</td><td style="text-align: left;">DDR0_DQ_A_05</td></tr>
    <tr><td style="text-align: center;">AB2</td><td style="text-align: left;">DDR0_DQ_B_14</td><td style="text-align: center;">AM2</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB4</td><td style="text-align: left;">DDR0_DQ_B_02</td><td style="text-align: center;">AM4</td><td style="text-align: left;">DDR0_CA_A_04</td></tr>
    <tr><td style="text-align: center;">AB5</td><td style="text-align: left;">DDR0_DQ_B_00</td><td style="text-align: center;">AM5</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB7</td><td style="text-align: left;">DDR0_CA_B_00</td><td style="text-align: center;">AM7</td><td style="text-align: left;">DDR0_CA_A_02</td></tr>
    <tr><td style="text-align: center;">AB8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">AM8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB9</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AM9</td><td style="text-align: left;">AVDD08_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AB10</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM10</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM11</td><td style="text-align: left;">AVDD18_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AB12</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB13</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM13</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AB14</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM14</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AB15</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM15</td><td style="text-align: left;">VCC12_UFS</td></tr>
    <tr><td style="text-align: center;">AB16</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM16</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AB17</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM17</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AB18</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM18</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AB19</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB20</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM20</td><td style="text-align: left;">VCC18_QSPI_CAP</td></tr>
    <tr><td style="text-align: center;">AC1</td><td style="text-align: left;">DDR0_DMI1_B</td><td style="text-align: center;">AN1</td><td style="text-align: left;">DDR0_DQ_A_06</td></tr>
    <tr><td style="text-align: center;">AC2</td><td style="text-align: left;">DDR0_DQ_B_12</td><td style="text-align: center;">AN2</td><td style="text-align: left;">DDR0_DQ_A_07</td></tr>
    <tr><td style="text-align: center;">AC3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC4</td><td style="text-align: left;">DDR0_DQ_B_03</td><td style="text-align: center;">AN4</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC5</td><td style="text-align: left;">DDR0_DQ_B_01</td><td style="text-align: center;">AN5</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC7</td><td style="text-align: left;">DDR0_CA_B_01</td><td style="text-align: center;">AN7</td><td style="text-align: left;">DDR0_CA_A_01</td></tr>
    <tr><td style="text-align: center;">AC8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">AN8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN9</td><td style="text-align: left;">AVDD08_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AC10</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AN10</td><td style="text-align: left;">VDD08_UFS</td></tr>
    <tr><td style="text-align: center;">AC11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN11</td><td style="text-align: left;">AVDD18_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AC12</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN12</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC13</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AN13</td><td style="text-align: left;">AVDD33_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AC14</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN14</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AC15</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AN15</td><td style="text-align: left;">VCC12_UFS</td></tr>
    <tr><td style="text-align: center;">AC16</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN16</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AC17</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AN17</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AC18</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN18</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AC19</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AN19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC20</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN20</td><td style="text-align: left;">VCC1833_GPIO5</td></tr>
    <tr><td style="text-align: center;">AD1</td><td style="text-align: left;">DDR0_DQS1_C_B</td><td style="text-align: center;">AP1</td><td style="text-align: left;">DDR0_DQ_A_04</td></tr>
    <tr><td style="text-align: center;">AD2</td><td style="text-align: left;">DDR0_DQS1_T_B</td><td style="text-align: center;">AP2</td><td style="text-align: left;">DDR0_DMI0_A</td></tr>
    <tr><td style="text-align: center;">AD3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD4</td><td style="text-align: left;">DDR0_WCK_T_B_0</td><td style="text-align: center;">AP4</td><td style="text-align: left;">DDR0_DQ_A_14</td></tr>
    <tr><td style="text-align: center;">AD5</td><td style="text-align: left;">DDR0_WCK_C_B_0</td><td style="text-align: center;">AP5</td><td style="text-align: left;">DDR0_DQ_A_15</td></tr>
    <tr><td style="text-align: center;">AD6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD7</td><td style="text-align: left;">DDR0_CKE0_B</td><td style="text-align: center;">AP7</td><td style="text-align: left;">DDR0_CA_A_00</td></tr>
    <tr><td style="text-align: center;">AD8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">AP8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD9</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AP9</td><td style="text-align: left;">AVDD08_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AD10</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP10</td><td style="text-align: left;">VDD08_UFS</td></tr>
    <tr><td style="text-align: center;">AD11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP11</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD12</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP12</td><td style="text-align: left;">AVDD18_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AD13</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP13</td><td style="text-align: left;">AVDD33_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AD14</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AP14</td><td style="text-align: left;">AVDD18_UFS</td></tr>
    <tr><td style="text-align: center;">AD15</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP15</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AD16</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AP16</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AD17</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP17</td><td style="text-align: left;">EDP1_EXTR</td></tr>
    <tr><td style="text-align: center;">AD18</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AP18</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AD19</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD20</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AP20</td><td style="text-align: left;">VCC1833_GPIO5</td></tr>
    <tr><td style="text-align: center;">AE1</td><td style="text-align: left;">DDR0_WCK_T_B_1</td><td style="text-align: center;">AR1</td><td style="text-align: left;">DDR0_WCK_T_A_0</td></tr>
    <tr><td style="text-align: center;">AE2</td><td style="text-align: left;">DDR0_WCK_C_B_1</td><td style="text-align: center;">AR2</td><td style="text-align: left;">DDR0_WCK_C_A_0</td></tr>
    <tr><td style="text-align: center;">AE3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE4</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR4</td><td style="text-align: left;">DDR0_DQ_A_12</td></tr>
    <tr><td style="text-align: center;">AE5</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR5</td><td style="text-align: left;">DDR0_DQ_A_13</td></tr>
    <tr><td style="text-align: center;">AE6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE7</td><td style="text-align: left;">DDR0_CA_B_02</td><td style="text-align: center;">AR7</td><td style="text-align: left;">DDR0_CKE0_A</td></tr>
    <tr><td style="text-align: center;">AE8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">AR8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR9</td><td style="text-align: left;">AVDD08_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AE10</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AR10</td><td style="text-align: left;">AVDD08_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AE11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR11</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AE12</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR12</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AE13</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AR13</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AE14</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR14</td><td style="text-align: left;">AVDD18_UFS</td></tr>
    <tr><td style="text-align: center;">AE15</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AR15</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AE16</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR16</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AE17</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AR17</td><td style="text-align: left;">UFS_REF_CLK</td></tr>
    <tr><td style="text-align: center;">AE18</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR18</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AE19</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AR19</td><td style="text-align: left;">QSPI_CLK</td></tr>
    <tr><td style="text-align: center;">AE20</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR20</td><td style="text-align: left;">QSPI_DAT3</td></tr>
    <tr><td style="text-align: center;">AF1</td><td style="text-align: left;">DDR0_DQ_B_09</td><td style="text-align: center;">AT1</td><td style="text-align: left;">DDR0_DQS0_C_A</td></tr>
    <tr><td style="text-align: center;">AF2</td><td style="text-align: left;">DDR0_DQ_B_11</td><td style="text-align: center;">AT2</td><td style="text-align: left;">DDR0_DQS0_T_A</td></tr>
    <tr><td style="text-align: center;">AF3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AF4</td><td style="text-align: left;">DDR0_DQS0_C_B</td><td style="text-align: center;">AT4</td><td style="text-align: left;">DDR0_DQS1_C_A</td></tr>
    <tr><td style="text-align: center;">AF5</td><td style="text-align: left;">DDR0_DQS0_T_B</td><td style="text-align: center;">AT5</td><td style="text-align: left;">DDR0_DQS1_T_A</td></tr>
    <tr><td style="text-align: center;">AF6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AF7</td><td style="text-align: left;">DDR0_CKE1_B</td><td style="text-align: center;">AT7</td><td style="text-align: left;">DDR0_CKE1_A</td></tr>
    <tr><td style="text-align: center;">AF8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">AT8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AF9</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AT9</td><td style="text-align: left;">AVDD08_DRD_USB</td></tr>
    <tr><td style="text-align: center;">AF10</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT10</td><td style="text-align: left;">USB_PORTA_ADTEST</td></tr>
    <tr><td style="text-align: center;">AF11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT11</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AF12</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT12</td><td style="text-align: left;">USB30_A_DRD0_RXN</td></tr>
    <tr><td style="text-align: center;">AF13</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT13</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AF14</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AT14</td><td style="text-align: left;">USB20_A_DRD_USB_P</td></tr>
    <tr><td style="text-align: center;">AF15</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT15</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AF16</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AT16</td><td style="text-align: left;">UFS_TXD0N</td></tr>
    <tr><td style="text-align: center;">AF17</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT17</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AF18</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AT18</td><td style="text-align: left;">EDP1_TX0N</td></tr>
    <tr><td style="text-align: center;">AF19</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AF20</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AT20</td><td style="text-align: left;">QSPI_CS0</td></tr>
    <tr><td style="text-align: center;">AG1</td><td style="text-align: left;">DDR0_DQ_B_08</td><td style="text-align: center;">AU1</td><td style="text-align: left;">DDR0_DQ_A_02</td></tr>
    <tr><td style="text-align: center;">AG2</td><td style="text-align: left;">DDR0_DQ_B_10</td><td style="text-align: center;">AU2</td><td style="text-align: left;">DDR0_DQ_A_01</td></tr>
    <tr><td style="text-align: center;">AG3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG4</td><td style="text-align: left;">DDR0_DMI0_B</td><td style="text-align: center;">AU4</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG5</td><td style="text-align: left;">DDR0_DQ_B_04</td><td style="text-align: center;">AU5</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG7</td><td style="text-align: left;">DDR0_CS0_B_CA06</td><td style="text-align: center;">AU7</td><td style="text-align: left;">DDR0_CS1_A</td></tr>
    <tr><td style="text-align: center;">AG8</td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: center;">AU8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG10</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AU10</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AG11</td><td style="text-align: left;">AVDD08_PLL_DDR0</td><td style="text-align: center;">AU11</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AG12</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU12</td><td style="text-align: left;">USB30_A_DRD0_RXP</td></tr>
    <tr><td style="text-align: center;">AG13</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AU13</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AG14</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU14</td><td style="text-align: left;">USB20_A_DRD_USB_M</td></tr>
    <tr><td style="text-align: center;">AG15</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AU15</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AG16</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU16</td><td style="text-align: left;">UFS_TXD0P</td></tr>
    <tr><td style="text-align: center;">AG17</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AU17</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AG18</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU18</td><td style="text-align: left;">EDP1_TX0P</td></tr>
    <tr><td style="text-align: center;">AG19</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AU19</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG20</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU20</td><td style="text-align: left;">QSPI_DAT1</td></tr>
    <tr><td style="text-align: center;">AH1</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV1</td><td style="text-align: left;">DDR0_DQ_A_00</td></tr>
    <tr><td style="text-align: center;">AH2</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV2</td><td style="text-align: left;">DDR0_DQ_A_03</td></tr>
    <tr><td style="text-align: center;">AH3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH4</td><td style="text-align: left;">DDR0_DQ_B_06</td><td style="text-align: center;">AV4</td><td style="text-align: left;">DDR0_WCK_T_A_1</td></tr>
    <tr><td style="text-align: center;">AH5</td><td style="text-align: left;">DDR0_DQ_B_05</td><td style="text-align: center;">AV5</td><td style="text-align: left;">DDR0_WCK_C_A_1</td></tr>
    <tr><td style="text-align: center;">AH6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH7</td><td style="text-align: left;">DDR0_CA_B_05</td><td style="text-align: center;">AV7</td><td style="text-align: left;">DDR0_ZN</td></tr>
    <tr><td style="text-align: center;">AH8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH9</td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: center;">AV9</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH10</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV10</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AH11</td><td style="text-align: left;">AVDD18_PLL_DDR0</td><td style="text-align: center;">AV11</td><td style="text-align: left;">USB30_A_DRD1_RXP</td></tr>
    <tr><td style="text-align: center;">AH12</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AV12</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AH13</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV13</td><td style="text-align: left;">UFS_RST_N</td></tr>
    <tr><td style="text-align: center;">AH14</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AV14</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AH15</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV15</td><td style="text-align: left;">UFS_TXD1N</td></tr>
    <tr><td style="text-align: center;">AH16</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AV16</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AH17</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV17</td><td style="text-align: left;">EDP1_AUXP</td></tr>
    <tr><td style="text-align: center;">AH18</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AV18</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AH19</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV19</td><td style="text-align: left;">EDP1_TX2P</td></tr>
    <tr><td style="text-align: center;">AH20</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AV20</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ1</td><td style="text-align: left;">DDR0_CKC_B</td><td style="text-align: center;">AW1</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ2</td><td style="text-align: left;">DDR0_CKT_B</td><td style="text-align: center;">AW2</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW3</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ4</td><td style="text-align: left;">DDR0_DQ_B_07</td><td style="text-align: center;">AW4</td><td style="text-align: left;">DDR0_DQ_A_11</td></tr>
    <tr><td style="text-align: center;">AJ5</td><td style="text-align: left;">DDR0_CA_B_04</td><td style="text-align: center;">AW5</td><td style="text-align: left;">DDR0_DQ_A_09</td></tr>
    <tr><td style="text-align: center;">AJ6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ7</td><td style="text-align: left;">DDR0_CA_B_03</td><td style="text-align: center;">AW7</td><td style="text-align: left;">DDR0_RESET_N</td></tr>
    <tr><td style="text-align: center;">AJ8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ9</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW9</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AJ10</td><td style="text-align: left;">AVDD08_PLL1</td><td style="text-align: center;">AW10</td><td style="text-align: left;">USB30_A_DRD0_TXP</td></tr>
    <tr><td style="text-align: center;">AJ11</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AW11</td><td style="text-align: left;">USB30_A_DRD1_RXN</td></tr>
    <tr><td style="text-align: center;">AJ12</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW12</td><td style="text-align: left;">USB30_A_DRD1_TXN</td></tr>
    <tr><td style="text-align: center;">AJ13</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AW13</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AJ14</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW14</td><td style="text-align: left;">UFS_RXD1P</td></tr>
    <tr><td style="text-align: center;">AJ15</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AW15</td><td style="text-align: left;">UFS_TXD1P</td></tr>
    <tr><td style="text-align: center;">AJ16</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW16</td><td style="text-align: left;">UFS_RXD0N</td></tr>
    <tr><td style="text-align: center;">AJ17</td><td style="text-align: left;">DVDD08_EDP1</td><td style="text-align: center;">AW17</td><td style="text-align: left;">EDP1_AUXN</td></tr>
    <tr><td style="text-align: center;">AJ18</td><td style="text-align: left;">DVDD08_EDP1</td><td style="text-align: center;">AW18</td><td style="text-align: left;">EDP1_TX1N</td></tr>
    <tr><td style="text-align: center;">AJ19</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AW19</td><td style="text-align: left;">EDP1_TX2N</td></tr>
    <tr><td style="text-align: center;">AJ20</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW20</td><td style="text-align: left;">EDP1_TX3N</td></tr>
    <tr><td style="text-align: center;">AK1</td><td style="text-align: left;">DDR0_CKC_A</td><td style="text-align: center;">AY2</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK2</td><td style="text-align: left;">DDR0_CKT_A</td><td style="text-align: center;">AY3</td><td style="text-align: left;">DDR0_DMI1_A</td></tr>
    <tr><td style="text-align: center;">AK3</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY4</td><td style="text-align: left;">DDR0_DQ_A_10</td></tr>
    <tr><td style="text-align: center;">AK4</td><td style="text-align: left;">DDR0_CS0_A_CA06</td><td style="text-align: center;">AY5</td><td style="text-align: left;">DDR0_DQ_A_08</td></tr>
    <tr><td style="text-align: center;">AK5</td><td style="text-align: left;">DDR0_CA_A_03</td><td style="text-align: center;">AY6</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK6</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY7</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK7</td><td style="text-align: left;">DDR0_CS1_B</td><td style="text-align: center;">AY8</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK8</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY9</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AK9</td><td style="text-align: left;">AVDD18_PLL1</td><td style="text-align: center;">AY10</td><td style="text-align: left;">USB30_A_DRD0_TXN</td></tr>
    <tr><td style="text-align: center;">AK10</td><td style="text-align: left;">AVSS_PLL1</td><td style="text-align: center;">AY11</td><td style="text-align: left;">AVSS_DRD</td></tr>
    <tr><td style="text-align: center;">AK11</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY12</td><td style="text-align: left;">USB30_A_DRD1_TXP</td></tr>
    <tr><td style="text-align: center;">AK12</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AY13</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AK13</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY14</td><td style="text-align: left;">UFS_RXD1N</td></tr>
    <tr><td style="text-align: center;">AK14</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY15</td><td style="text-align: left;">AVSS_UFS</td></tr>
    <tr><td style="text-align: center;">AK15</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY16</td><td style="text-align: left;">UFS_RXD0P</td></tr>
    <tr><td style="text-align: center;">AK16</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AY17</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AK17</td><td style="text-align: left;">AVSS_EDP1</td><td style="text-align: center;">AY18</td><td style="text-align: left;">EDP1_TX1P</td></tr>
    <tr><td style="text-align: center;">AK18</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AY19</td><td style="text-align: left;">AVSS_EDP1</td></tr>
    <tr><td style="text-align: center;">AK19</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY20</td><td style="text-align: left;">EDP1_TX3P</td></tr>
    <tr><td style="text-align: center;">AK20</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
  </tbody>
</table>

#### 4.1.4 (AA~AY, 21~40)

<img src="static/k3_pinmap_aa-ay_21-40.png" alt="" width="800">

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="150">
    <col width="350">
    <col width="150">
    <col width="350">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
      <th style="text-align: center;">Pin Number</th>
      <th style="text-align: left;">Pin Name</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="text-align: center;">AA21</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL21</td><td style="text-align: left;">VCC18_SD_CAP</td></tr>
    <tr><td style="text-align: center;">AA22</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL22</td><td style="text-align: left;">VCC18_GPIO5</td></tr>
    <tr><td style="text-align: center;">AA23</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL23</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA24</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL24</td><td style="text-align: left;">VCC18_GPIO1</td></tr>
    <tr><td style="text-align: center;">AA25</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL25</td><td style="text-align: left;">VCC18_GPIO4</td></tr>
    <tr><td style="text-align: center;">AA26</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL26</td><td style="text-align: left;">VCC18_GPIO4</td></tr>
    <tr><td style="text-align: center;">AA27</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL27</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA28</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL28</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">AA29</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AL29</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA30</td><td style="text-align: left;">AVDD08_DSI</td><td style="text-align: center;">AL30</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">AA31</td><td style="text-align: left;">AVDD08_DSI</td><td style="text-align: center;">AL31</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA32</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL32</td><td style="text-align: left;">AVDD18_EDP0</td></tr>
    <tr><td style="text-align: center;">AA33</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL33</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA34</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL34</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA35</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AL35</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AA36</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AL36</td><td style="text-align: left;">AVSS_DSI</td></tr>
    <tr><td style="text-align: center;">AA37</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AL37</td><td style="text-align: left;">AVSS_DSI</td></tr>
    <tr><td style="text-align: center;">AA38</td><td style="text-align: left;">MIPI_CSI1_D2N</td><td style="text-align: center;">AL38</td><td style="text-align: left;">MIPI_DSI1_CLKN</td></tr>
    <tr><td style="text-align: center;">AA39</td><td style="text-align: left;">MIPI_CSI1_D2P</td><td style="text-align: center;">AL39</td><td style="text-align: left;">MIPI_DSI1_CLKP</td></tr>
    <tr><td style="text-align: center;">AA40</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AL40</td><td style="text-align: left;">AVSS_DSI</td></tr>
    <tr><td style="text-align: center;">AB21</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM21</td><td style="text-align: left;">VCC18_SD_CAP</td></tr>
    <tr><td style="text-align: center;">AB22</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM22</td><td style="text-align: left;">VCC18_GPIO5</td></tr>
    <tr><td style="text-align: center;">AB23</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM23</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB24</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM24</td><td style="text-align: left;">VCC18_GPIO1</td></tr>
    <tr><td style="text-align: center;">AB25</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM25</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB26</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM26</td><td style="text-align: left;">VCC1833_GPIO4</td></tr>
    <tr><td style="text-align: center;">AB27</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM27</td><td style="text-align: left;">VCC1833_GPIO1</td></tr>
    <tr><td style="text-align: center;">AB28</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AM28</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB29</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM29</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB30</td><td style="text-align: left;">AVDD08_CSI2</td><td style="text-align: center;">AM30</td><td style="text-align: left;">VCC_SYS</td></tr>
    <tr><td style="text-align: center;">AB31</td><td style="text-align: left;">AVDD08_CSI2</td><td style="text-align: center;">AM31</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB32</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AM32</td><td style="text-align: left;">AVDD18_EDP0</td></tr>
    <tr><td style="text-align: center;">AB33</td><td style="text-align: left;">MIPI_CSI2_CLKN</td><td style="text-align: center;">AM33</td><td style="text-align: left;">MIPI_DSI1_D1P</td></tr>
    <tr><td style="text-align: center;">AB34</td><td style="text-align: left;">MIPI_CSI2_CLKP</td><td style="text-align: center;">AM34</td><td style="text-align: left;">MIPI_DSI1_D1N</td></tr>
    <tr><td style="text-align: center;">AB35</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AM35</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AB36</td><td style="text-align: left;">MIPI_CSI1_D3N</td><td style="text-align: center;">AM36</td><td style="text-align: left;">MIPI_DSI1_D3P</td></tr>
    <tr><td style="text-align: center;">AB37</td><td style="text-align: left;">MIPI_CSI1_D3P</td><td style="text-align: center;">AM37</td><td style="text-align: left;">MIPI_DSI1_D3N</td></tr>
    <tr><td style="text-align: center;">AB38</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AM38</td><td style="text-align: left;">AVSS_DSI</td></tr>
    <tr><td style="text-align: center;">AB39</td><td style="text-align: left;">MIPI_CSI1_CLKN</td><td style="text-align: center;">AM39</td><td style="text-align: left;">MIPI_DSI1_D0P</td></tr>
    <tr><td style="text-align: center;">AB40</td><td style="text-align: left;">MIPI_CSI1_CLKP</td><td style="text-align: center;">AM40</td><td style="text-align: left;">MIPI_DSI1_D0N</td></tr>
    <tr><td style="text-align: center;">AC21</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AN21</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC22</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN22</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC23</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AN23</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC24</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN24</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC25</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AN25</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC26</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN26</td><td style="text-align: left;">VCC1833_GPIO4</td></tr>
    <tr><td style="text-align: center;">AC27</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AN27</td><td style="text-align: left;">VCC1833_GPIO1</td></tr>
    <tr><td style="text-align: center;">AC28</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN28</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC29</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AN29</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC30</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AN30</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC31</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN31</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC32</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN32</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC33</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN33</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC34</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN34</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC35</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN35</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AC36</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN36</td><td style="text-align: left;">EDP0_EXTR</td></tr>
    <tr><td style="text-align: center;">AC37</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN37</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AC38</td><td style="text-align: left;">MIPI_CSI1_D1P</td><td style="text-align: center;">AN38</td><td style="text-align: left;">EDP0_AUXN</td></tr>
    <tr><td style="text-align: center;">AC39</td><td style="text-align: left;">MIPI_CSI1_D1N</td><td style="text-align: center;">AN39</td><td style="text-align: left;">EDP0_AUXP</td></tr>
    <tr><td style="text-align: center;">AC40</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AN40</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AD21</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP21</td><td style="text-align: left;">QSPI_DAT2</td></tr>
    <tr><td style="text-align: center;">AD22</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AP22</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD23</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP23</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD24</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AP24</td><td style="text-align: left;">GPIO[5]_119</td></tr>
    <tr><td style="text-align: center;">AD25</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP25</td><td style="text-align: left;">GPIO[5]_114</td></tr>
    <tr><td style="text-align: center;">AD26</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AP26</td><td style="text-align: left;">GPIO[5]_108</td></tr>
    <tr><td style="text-align: center;">AD27</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP27</td><td style="text-align: left;">GPIO[5]_106</td></tr>
    <tr><td style="text-align: center;">AD28</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AP28</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD29</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AP29</td><td style="text-align: left;">GPIO[1]_20</td></tr>
    <tr><td style="text-align: center;">AD30</td><td style="text-align: left;">AVDD08_CSI0</td><td style="text-align: center;">AP30</td><td style="text-align: left;">GPIO[1]_16</td></tr>
    <tr><td style="text-align: center;">AD31</td><td style="text-align: left;">AVDD08_CSI0</td><td style="text-align: center;">AP31</td><td style="text-align: left;">GPIO[1]_06</td></tr>
    <tr><td style="text-align: center;">AD32</td><td style="text-align: left;">AVDD08_CSI1</td><td style="text-align: center;">AP32</td><td style="text-align: left;">GPIO[1]_05</td></tr>
    <tr><td style="text-align: center;">AD33</td><td style="text-align: left;">AVDD08_CSI1</td><td style="text-align: center;">AP33</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD34</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AP34</td><td style="text-align: left;">GPIO[4]_79</td></tr>
    <tr><td style="text-align: center;">AD35</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AP35</td><td style="text-align: left;">GPIO[4]_78</td></tr>
    <tr><td style="text-align: center;">AD36</td><td style="text-align: left;">MIPI_CSI1_D0P</td><td style="text-align: center;">AP36</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AD37</td><td style="text-align: left;">MIPI_CSI1_D0N</td><td style="text-align: center;">AP37</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AD38</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AP38</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AD39</td><td style="text-align: left;">MIPI_CSI0_D3N</td><td style="text-align: center;">AP39</td><td style="text-align: left;">EDP0_TX3P</td></tr>
    <tr><td style="text-align: center;">AD40</td><td style="text-align: left;">MIPI_CSI0_D3P</td><td style="text-align: center;">AP40</td><td style="text-align: left;">EDP0_TX3N</td></tr>
    <tr><td style="text-align: center;">AE21</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AR21</td><td style="text-align: left;">QSPI_CS1</td></tr>
    <tr><td style="text-align: center;">AE22</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR22</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE23</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AR23</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE24</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR24</td><td style="text-align: left;">GPIO[5]_120</td></tr>
    <tr><td style="text-align: center;">AE25</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AR25</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE26</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR26</td><td style="text-align: left;">GPIO[5]_109</td></tr>
    <tr><td style="text-align: center;">AE27</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AR27</td><td style="text-align: left;">GPIO[5]_105</td></tr>
    <tr><td style="text-align: center;">AE28</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR28</td><td style="text-align: left;">GPIO[5]_99</td></tr>
    <tr><td style="text-align: center;">AE29</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AR29</td><td style="text-align: left;">GPIO[1]_19</td></tr>
    <tr><td style="text-align: center;">AE30</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AR30</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE31</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR31</td><td style="text-align: left;">GPIO[1]_07</td></tr>
    <tr><td style="text-align: center;">AE32</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR32</td><td style="text-align: left;">GPIO[1]_04</td></tr>
    <tr><td style="text-align: center;">AE33</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR33</td><td style="text-align: left;">GPIO[4]_76</td></tr>
    <tr><td style="text-align: center;">AE34</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR34</td><td style="text-align: left;">GPIO[4]_80</td></tr>
    <tr><td style="text-align: center;">AE35</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR35</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE36</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR36</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AE37</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR37</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AE38</td><td style="text-align: left;">MIPI_CSI0_D2N</td><td style="text-align: center;">AR38</td><td style="text-align: left;">EDP0_TX2P</td></tr>
    <tr><td style="text-align: center;">AE39</td><td style="text-align: left;">MIPI_CSI0_D2P</td><td style="text-align: center;">AR39</td><td style="text-align: left;">EDP0_TX2N</td></tr>
    <tr><td style="text-align: center;">AE40</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AR40</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AF21</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT21</td><td style="text-align: left;">QSPI_DAT0</td></tr>
    <tr><td style="text-align: center;">AF22</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AT22</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AF23</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT23</td><td style="text-align: left;">GPIO[5]_124</td></tr>
    <tr><td style="text-align: center;">AF26</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AT24</td><td style="text-align: left;">GPIO[5]_121</td></tr>
    <tr><td style="text-align: center;">AF27</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT25</td><td style="text-align: left;">GPIO[5]_115</td></tr>
    <tr><td style="text-align: center;">AF28</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AT26</td><td style="text-align: left;">GPIO[5]_110</td></tr>
    <tr><td style="text-align: center;">AF29</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT27</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AF30</td><td style="text-align: left;">AVDD18_CSI1</td><td style="text-align: center;">AT28</td><td style="text-align: left;">GPIO[5]_100</td></tr>
    <tr><td style="text-align: center;">AF31</td><td style="text-align: left;">AVDD18_CSI1</td><td style="text-align: center;">AT29</td><td style="text-align: left;">GPIO[1]_18</td></tr>
    <tr><td style="text-align: center;">AF32</td><td style="text-align: left;">AVDD18_CSI2</td><td style="text-align: center;">AT30</td><td style="text-align: left;">GPIO[1]_13</td></tr>
    <tr><td style="text-align: center;">AF33</td><td style="text-align: left;">AVDD18_CSI2</td><td style="text-align: center;">AT31</td><td style="text-align: left;">GPIO[1]_08</td></tr>
    <tr><td style="text-align: center;">AF34</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AT32</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AF35</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AT33</td><td style="text-align: left;">GPIO[4]_77</td></tr>
    <tr><td style="text-align: center;">AF36</td><td style="text-align: left;">MIPI_CSI0_CLKN</td><td style="text-align: center;">AT34</td><td style="text-align: left;">GPIO[4]_81</td></tr>
    <tr><td style="text-align: center;">AF37</td><td style="text-align: left;">MIPI_CSI0_CLKP</td><td style="text-align: center;">AT35</td><td style="text-align: left;">GPIO[4]_86</td></tr>
    <tr><td style="text-align: center;">AF38</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AT36</td><td style="text-align: left;">GPIO[4]_90</td></tr>
    <tr><td style="text-align: center;">AF39</td><td style="text-align: left;">MIPI_CSI0_D1P</td><td style="text-align: center;">AT37</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AF40</td><td style="text-align: left;">MIPI_CSI0_D1N</td><td style="text-align: center;">AT38</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AG21</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AT39</td><td style="text-align: left;">EDP0_TX1P</td></tr>
    <tr><td style="text-align: center;">AG22</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AT40</td><td style="text-align: left;">EDP0_TX1N</td></tr>
    <tr><td style="text-align: center;">AG23</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AU21</td><td style="text-align: left;">MMC1_DAT2</td></tr>
    <tr><td style="text-align: center;">AG26</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU22</td><td style="text-align: left;">MMC1_DAT1</td></tr>
    <tr><td style="text-align: center;">AG27</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AU23</td><td style="text-align: left;">GPIO[5]_125</td></tr>
    <tr><td style="text-align: center;">AG28</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AU25</td><td style="text-align: left;">GPIO[5]_116</td></tr>
    <tr><td style="text-align: center;">AG29</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AU26</td><td style="text-align: left;">GPIO[5]_111</td></tr>
    <tr><td style="text-align: center;">AG30</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AU28</td><td style="text-align: left;">GPIO[5]_101</td></tr>
    <tr><td style="text-align: center;">AG31</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AU29</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG32</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AU31</td><td style="text-align: left;">GPIO[1]_09</td></tr>
    <tr><td style="text-align: center;">AG33</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AU32</td><td style="text-align: left;">GPIO[1]_03</td></tr>
    <tr><td style="text-align: center;">AG34</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AU34</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG35</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AU35</td><td style="text-align: left;">GPIO[4]_87</td></tr>
    <tr><td style="text-align: center;">AG36</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AU37</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AG37</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AU38</td><td style="text-align: left;">EDP0_TX0P</td></tr>
    <tr><td style="text-align: center;">AG38</td><td style="text-align: left;">MIPI_CSI0_D0P</td><td style="text-align: center;">AU39</td><td style="text-align: left;">EDP0_TX0N</td></tr>
    <tr><td style="text-align: center;">AG39</td><td style="text-align: left;">MIPI_CSI0_D0N</td><td style="text-align: center;">AU40</td><td style="text-align: left;">AVSS_EDP0</td></tr>
    <tr><td style="text-align: center;">AG40</td><td style="text-align: left;">AVSS_MIPI012</td><td style="text-align: center;">AV21</td><td style="text-align: left;">MMC1_CLK</td></tr>
    <tr><td style="text-align: center;">AH21</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV22</td><td style="text-align: left;">MMC1_DAT0</td></tr>
    <tr><td style="text-align: center;">AH22</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AV23</td><td style="text-align: left;">GPIO[5]_126</td></tr>
    <tr><td style="text-align: center;">AH23</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV25</td><td style="text-align: left;">GPIO[5]_117</td></tr>
    <tr><td style="text-align: center;">AH24</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AV26</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH25</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV28</td><td style="text-align: left;">GPIO[5]_102</td></tr>
    <tr><td style="text-align: center;">AH26</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AV29</td><td style="text-align: left;">GPIO[1]_17</td></tr>
    <tr><td style="text-align: center;">AH27</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV31</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH28</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AV32</td><td style="text-align: left;">GPIO[1]_02</td></tr>
    <tr><td style="text-align: center;">AH29</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AV34</td><td style="text-align: left;">GPIO[4]_82</td></tr>
    <tr><td style="text-align: center;">AH30</td><td style="text-align: left;">AVDD12_DSI</td><td style="text-align: center;">AV35</td><td style="text-align: left;">GPIO[4]_88</td></tr>
    <tr><td style="text-align: center;">AH31</td><td style="text-align: left;">AVDD18_CSI0</td><td style="text-align: center;">AV37</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH32</td><td style="text-align: left;">AVDD18_CSI0</td><td style="text-align: center;">AV38</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH33</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AV39</td><td style="text-align: left;">GPIO[4]_96</td></tr>
    <tr><td style="text-align: center;">AH34</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AV40</td><td style="text-align: left;">GPIO[4]_98</td></tr>
    <tr><td style="text-align: center;">AH35</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AW21</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH36</td><td style="text-align: left;">MIPI_DSI0_D2P</td><td style="text-align: center;">AW22</td><td style="text-align: left;">MMC1_CMD</td></tr>
    <tr><td style="text-align: center;">AH37</td><td style="text-align: left;">MIPI_DSI0_D2N</td><td style="text-align: center;">AW23</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AH38</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AW24</td><td style="text-align: left;">GPIO[5]_122</td></tr>
    <tr><td style="text-align: center;">AH39</td><td style="text-align: left;">MIPI_DSI0_D1N</td><td style="text-align: center;">AW25</td><td style="text-align: left;">GPIO[5]_118</td></tr>
    <tr><td style="text-align: center;">AH40</td><td style="text-align: left;">MIPI_DSI0_D1P</td><td style="text-align: center;">AW26</td><td style="text-align: left;">GPIO[5]_112</td></tr>
    <tr><td style="text-align: center;">AJ21</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AW27</td><td style="text-align: left;">GPIO[5]_104</td></tr>
    <tr><td style="text-align: center;">AJ22</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW28</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ23</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AW29</td><td style="text-align: left;">GPIO[1]_14</td></tr>
    <tr><td style="text-align: center;">AJ24</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW30</td><td style="text-align: left;">GPIO[1]_12</td></tr>
    <tr><td style="text-align: center;">AJ25</td><td style="text-align: left;">VCC_CPUX</td><td style="text-align: center;">AW31</td><td style="text-align: left;">GPIO[1]_10</td></tr>
    <tr><td style="text-align: center;">AJ26</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW32</td><td style="text-align: left;">GPIO[1]_01</td></tr>
    <tr><td style="text-align: center;">AJ27</td><td style="text-align: left;">DVDD08_EDP0</td><td style="text-align: center;">AW33</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ28</td><td style="text-align: left;">DVDD08_EDP0</td><td style="text-align: center;">AW34</td><td style="text-align: left;">GPIO[4]_83</td></tr>
    <tr><td style="text-align: center;">AJ29</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AW35</td><td style="text-align: left;">GPIO[4]_89</td></tr>
    <tr><td style="text-align: center;">AJ30</td><td style="text-align: left;">AVDD12_DSI</td><td style="text-align: center;">AW36</td><td style="text-align: left;">GPIO[4]_91</td></tr>
    <tr><td style="text-align: center;">AJ31</td><td style="text-align: left;">AVDD18_DSI</td><td style="text-align: center;">AW37</td><td style="text-align: left;">GPIO[4]_93</td></tr>
    <tr><td style="text-align: center;">AJ32</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AW38</td><td style="text-align: left;">GPIO[4]_95</td></tr>
    <tr><td style="text-align: center;">AJ33</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AW39</td><td style="text-align: left;">GPIO[4]_97</td></tr>
    <tr><td style="text-align: center;">AJ34</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AW40</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ35</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AY21</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ36</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AY22</td><td style="text-align: left;">MMC1_DAT3</td></tr>
    <tr><td style="text-align: center;">AJ37</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AY23</td><td style="text-align: left;">GPIO[5]_127</td></tr>
    <tr><td style="text-align: center;">AJ38</td><td style="text-align: left;">MIPI_DSI0_CLKN</td><td style="text-align: center;">AY24</td><td style="text-align: left;">GPIO[5]_123</td></tr>
    <tr><td style="text-align: center;">AJ39</td><td style="text-align: left;">MIPI_DSI0_CLKP</td><td style="text-align: center;">AY25</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AJ40</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;">AY26</td><td style="text-align: left;">GPIO[5]_113</td></tr>
    <tr><td style="text-align: center;">AK21</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY27</td><td style="text-align: left;">GPIO[5]_107</td></tr>
    <tr><td style="text-align: center;">AK22</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AY28</td><td style="text-align: left;">GPIO[5]_103</td></tr>
    <tr><td style="text-align: center;">AK23</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY29</td><td style="text-align: left;">GPIO[1]_15</td></tr>
    <tr><td style="text-align: center;">AK24</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AY30</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK25</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY31</td><td style="text-align: left;">GPIO[1]_11</td></tr>
    <tr><td style="text-align: center;">AK26</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AY32</td><td style="text-align: left;">GPIO[1]_00</td></tr>
    <tr><td style="text-align: center;">AK27</td><td style="text-align: left;">AVSS_EDP0</td><td style="text-align: center;">AY33</td><td style="text-align: left;">GPIO[4]_85</td></tr>
    <tr><td style="text-align: center;">AK28</td><td style="text-align: left;">VCC_SYS</td><td style="text-align: center;">AY34</td><td style="text-align: left;">GPIO[4]_84</td></tr>
    <tr><td style="text-align: center;">AK29</td><td style="text-align: left;">AVSS_EDP0</td><td style="text-align: center;">AY35</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK30</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY36</td><td style="text-align: left;">GPIO[4]_92</td></tr>
    <tr><td style="text-align: center;">AK31</td><td style="text-align: left;">AVDD18_DSI</td><td style="text-align: center;">AY37</td><td style="text-align: left;">GPIO[4]_94</td></tr>
    <tr><td style="text-align: center;">AK32</td><td style="text-align: left;">VSS</td><td style="text-align: center;">AY38</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK33</td><td style="text-align: left;">MIPI_DSI0_D0P</td><td style="text-align: center;">AY39</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK34</td><td style="text-align: left;">MIPI_DSI0_D0N</td><td style="text-align: center;">AY40</td><td style="text-align: left;">VSS</td></tr>
    <tr><td style="text-align: center;">AK35</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
    <tr><td style="text-align: center;">AK36</td><td style="text-align: left;">MIPI_DSI0_D3P</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
    <tr><td style="text-align: center;">AK37</td><td style="text-align: left;">MIPI_DSI0_D3N</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
    <tr><td style="text-align: center;">AK38</td><td style="text-align: left;">AVSS_DSI</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
    <tr><td style="text-align: center;">AK39</td><td style="text-align: left;">MIPI_DSI1_D2N</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
    <tr><td style="text-align: center;">AK40</td><td style="text-align: left;">MIPI_DSI1_D2P</td><td style="text-align: center;"></td><td style="text-align: left;"></td></tr>
  </tbody>
</table>

### 4.2 I/O Pin Parameters

#### 4.2.1 For 1.8V I/O Pins

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="150">
    <col width="100">
    <col width="450">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Power Domain</th>
      <th style="text-align: center;">Symbol</th>
      <th style="text-align: left;">Description</th>
      <th style="text-align: center;">Min</th>
      <th style="text-align: center;">Typ</th>
      <th style="text-align: center;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- 1.8V Input Section -->
    <tr>
      <td rowspan="5" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">1.8V Input</td>
      <td style="text-align: center;">Vih</td>
      <td style="text-align: left;">High level input</td>
      <td style="text-align: center;">VCC×0.7V</td>
      <td style="text-align: center;">1.8V</td>
      <td style="text-align: center;">VCC+0.2V</td>
    </tr>
    <tr>
      <td style="text-align: center;">Vil</td>
      <td style="text-align: left;">Low level input</td>
      <td style="text-align: center;">-0.3V</td>
      <td style="text-align: center;">0V</td>
      <td style="text-align: center;">VCC×0.3V</td>
    </tr>
    <tr>
      <td style="text-align: center;">Rpu</td>
      <td style="text-align: left;">Pull up resistor</td>
      <td style="text-align: center;">55kΩ</td>
      <td style="text-align: center;">79kΩ</td>
      <td style="text-align: center;">121kΩ</td>
    </tr>
    <tr>
      <td style="text-align: center;">Rpd</td>
      <td style="text-align: left;">Pull down resistor</td>
      <td style="text-align: center;">51kΩ</td>
      <td style="text-align: center;">87kΩ</td>
      <td style="text-align: center;">169kΩ</td>
    </tr>
    <tr>
      <td style="text-align: center;">Iil</td>
      <td style="text-align: left;">Input leakage current (Pad in input mode)</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">10µA</td>
    </tr>
    <!-- 1.8V Output Section -->
    <tr>
      <td rowspan="10" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">1.8V Output</td>
      <td style="text-align: center;">Voh</td>
      <td style="text-align: left;">High level output</td>
      <td style="text-align: center;">VCC−0.2V</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: center;">Vol</td>
      <td style="text-align: left;">Low level output</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">0.2V</td>
    </tr>
    <!-- IOL Rows (Split for clarity within 500px col) -->
    <tr>
      <td rowspan="4" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Iol<br><span style="font-size:11px; color:#666;">DCS[1:0]</span></td>
      <td style="text-align: left;">Low level output current (Vpad=0.2V) <strong>DCS=00</strong></td>
      <td style="text-align: center;">13mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.2V) <strong>DCS=01</strong></td>
      <td style="text-align: center;">25mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.2V) <strong>DCS=10</strong></td>
      <td style="text-align: center;">37mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.2V) <strong>DCS=11</strong></td>
      <td style="text-align: center;">49mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <!-- IOH Rows (Split for clarity within 500px col) -->
    <tr>
      <td rowspan="4" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Ioh<br><span style="font-size:11px; color:#666;">DCS[1:0]</span></td>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.2V) <strong>DCS=00</strong></td>
      <td style="text-align: center;">11mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.2V) <strong>DCS=01</strong></td>
      <td style="text-align: center;">21mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.2V) <strong>DCS=10</strong></td>
      <td style="text-align: center;">32mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.2V) <strong>DCS=11</strong></td>
      <td style="text-align: center;">42mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
  </tbody>
</table>

### 4.2.2 For 3.3V I/O Pins

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="150">
    <col width="100">
    <col width="450">
    <col width="100">
    <col width="100">
    <col width="100">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">Power Domain</th>
      <th style="text-align: center;">Symbol</th>
      <th style="text-align: left;">Description</th>
      <th style="text-align: center;">Min</th>
      <th style="text-align: center;">Typ</th>
      <th style="text-align: center;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- 3.3V Input Section -->
    <tr>
      <td rowspan="5" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">3.3V Input</td>
      <td style="text-align: center;">Vih</td>
      <td style="text-align: left;">High level input voltage</td>
      <td style="text-align: center;">2V</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">VCC+0.3V</td>
    </tr>
    <tr>
      <td style="text-align: center;">Vil</td>
      <td style="text-align: left;">Low level input voltage</td>
      <td style="text-align: center;">-0.3V</td>
      <td style="text-align: center;">0V</td>
      <td style="text-align: center;">0.8V</td>
    </tr>
    <tr>
      <td style="text-align: center;">Rpu</td>
      <td style="text-align: left;">Pull-up resistor</td>
      <td style="text-align: center;">26kΩ</td>
      <td style="text-align: center;">47kΩ</td>
      <td style="text-align: center;">72kΩ</td>
    </tr>
    <tr>
      <td style="text-align: center;">Rpd</td>
      <td style="text-align: left;">Pull-down resistor</td>
      <td style="text-align: center;">27kΩ</td>
      <td style="text-align: center;">54kΩ</td>
      <td style="text-align: center;">267kΩ</td>
    </tr>
    <tr>
      <td style="text-align: center;">Iil</td>
      <td style="text-align: left;">Input leakage current</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">10µA</td>
    </tr>
    <!-- 3.3V Output Section -->
    <tr>
      <td rowspan="18" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">3.3V Output</td>
      <td style="text-align: center;">Voh</td>
      <td style="text-align: left;">High level output voltage</td>
      <td style="text-align: center;">2.4V</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: center;">Vol</td>
      <td style="text-align: left;">Low level output voltage</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">0.4V</td>
    </tr>
    <!-- IOL Rows (8 configurations) -->
    <tr>
      <td rowspan="8" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Iol<br><span style="font-size:11px; color:#666;">DS[2:0]</span></td>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=000</strong></td>
      <td style="text-align: center;">7mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=001</strong></td>
      <td style="text-align: center;">10mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=010</strong></td>
      <td style="text-align: center;">14mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=011</strong></td>
      <td style="text-align: center;">18mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=100</strong></td>
      <td style="text-align: center;">21mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=101</strong></td>
      <td style="text-align: center;">24mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=110</strong></td>
      <td style="text-align: center;">28mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">Low level output current (Vpad=0.4V) <strong>DS=111</strong></td>
      <td style="text-align: center;">31mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <!-- IOH Rows (8 configurations) -->
    <tr>
      <td rowspan="8" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Ioh<br><span style="font-size:11px; color:#666;">DS[2:0]</span></td>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=000</strong></td>
      <td style="text-align: center;">7mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=001</strong></td>
      <td style="text-align: center;">10mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=010</strong></td>
      <td style="text-align: center;">13mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=011</strong></td>
      <td style="text-align: center;">16mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=100</strong></td>
      <td style="text-align: center;">19mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=101</strong></td>
      <td style="text-align: center;">23mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=110</strong></td>
      <td style="text-align: center;">26mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
    </tr>
    <tr>
      <td style="text-align: left;">High level output current (Vpad=VCC−0.5V) <strong>DS=111</strong></td>
      <td style="text-align: center;">29mA</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: center;">—</td>
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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Signal/Pin</th>
      <th style="text-align: center;">Type</th>
      <th style="text-align: left;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">PRI_TCK</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">Primary JTAG interface 1 test clock. Used for all transfers on the JTAG test interface.</td>
    </tr>
    <tr>
      <td style="text-align: left;">PRI_TDI</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">Primary JTAG interface 1 test data input. Used to send data from the JTAG controller to the K3 processor. This pin has an internal pullup resistor.</td>
    </tr>
    <tr>
      <td style="text-align: left;">PRI_TDO</td>
      <td style="text-align: center;">O</td>
      <td style="text-align: left;">Primary JTAG Interface 1 test data output. Used to return data from the K1 processor to the JTAG controller.</td>
    </tr>
    <tr>
      <td style="text-align: left;">PRI_TMS</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">Primary JTAG Interface 1 test mode select. Used to select the test mode required from the JTAG controller. This pin has an internal pullup resistor.</td>
    </tr>
    <tr>
      <td style="text-align: left;">PRI_TRSTn</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">Primary JTAG Interface 1 test reset. Used for IEEE 1194.1 test reset.</td>
    </tr>
    <tr>
      <td style="text-align: left;">VCXO_OUT</td>
      <td style="text-align: center;">O</td>
      <td style="text-align: left;">24 MHz VCXO output clock</td>
    </tr>
    <tr>
      <td style="text-align: left;">VCXO_REQ</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">OCLK1 request</td>
    </tr>
  </tbody>
</table>

#### 4.3.2 Miscellaneous

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Signal/Pin</th>
      <th style="text-align: center;">Type</th>
      <th style="text-align: left;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">MPLL_TST_CK</td>
      <td style="text-align: center;">—</td>
      <td style="text-align: left;">PLL test pin</td>
    </tr>
    <tr>
      <td style="text-align: left;">MN_CLK_OUT</td>
      <td style="text-align: center;">O</td>
      <td style="text-align: left;">Fractional (M/N) divided clock. Main PMU general purpose M/N fractional clock divider clock output. CLK_REQ must be set as Function 0 and pulled high for the 13 MHz clock to be output on GPIO[122] (MN_CLK_OUT).</td>
    </tr>
    <tr>
      <td style="text-align: left;">Sleep_OUT</td>
      <td style="text-align: center;">O</td>
      <td style="text-align: left;">PMIC sleep setting</td>
    </tr>
  </tbody>
</table>

#### 4.3.3 SPIx

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Signal/Pin</th>
      <th style="text-align: center;">Type</th>
      <th style="text-align: left;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">SPIx_FRM</td>
      <td style="text-align: center;">I/O</td>
      <td style="text-align: left;">Synchronous serial port frame 0/2. The serial frame sync can be configured as an output (master mode operation) or an input (slave mode operation).</td>
    </tr>
    <tr>
      <td style="text-align: left;">SPIx_RXD</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">Synchronous serial port receive data 0/2. Serial data latched using the bit clock.</td>
    </tr>
    <tr>
      <td style="text-align: left;">SPIx_SCLK</td>
      <td style="text-align: center;">I/O</td>
      <td style="text-align: left;">Synchronous serial port clock 0/2. The serial bit clock can be configured as an output (master mode operation) or an input (slave mode operation).</td>
    </tr>
    <tr>
      <td style="text-align: left;">SPIx_TXD</td>
      <td style="text-align: center;">O</td>
      <td style="text-align: left;">Synchronous serial port transmit data 0/2. Serial data driven out synchronously with the bit clock.</td>
    </tr>
  </tbody>
</table>

#### 4.3.4 TWSI

**Dedicated**

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Signal/Pin</th>
      <th style="text-align: center;">Type</th>
      <th style="text-align: left;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">PWR_SDA</td>
      <td style="text-align: center;">I/O</td>
      <td style="text-align: left;">TWSI serial data/address signal</td>
    </tr>
    <tr>
      <td style="text-align: left;">PWR_SCL</td>
      <td style="text-align: center;">I/O</td>
      <td style="text-align: left;">TWSI serial clock line signal</td>
    </tr>
  </tbody>
</table>

**Common**

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Signal/Pin</th>
      <th style="text-align: center;">Type</th>
      <th style="text-align: left;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">I²Cx_SCL</td>
      <td style="text-align: center;">I/O,OD</td>
      <td style="text-align: left;">TWSIx clock</td>
    </tr>
    <tr>
      <td style="text-align: left;">I²Cx_SDA</td>
      <td style="text-align: center;">I/O,OD</td>
      <td style="text-align: left;">TWSIx data</td>
    </tr>
  </tbody>
</table>

#### 4.3.5 UARTx

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Signal/Pin</th>
      <th style="text-align: center;">Type</th>
      <th style="text-align: left;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">UARTx_CTSn</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">UARTx clear-to-send</td>
    </tr>
    <tr>
      <td style="text-align: left;">UARTx_RTSn</td>
      <td style="text-align: center;">O</td>
      <td style="text-align: left;">UARTx request-to-send</td>
    </tr>
    <tr>
      <td style="text-align: left;">UARTx_RXD</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">UARTx receive data</td>
    </tr>
    <tr>
      <td style="text-align: left;">UARTx_TXD</td>
      <td style="text-align: center;">O</td>
      <td style="text-align: left;">UARTx transmit data</td>
    </tr>
  </tbody>
</table>

#### 4.3.6 USB

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Signal/Pin</th>
      <th style="text-align: center;">Type</th>
      <th style="text-align: left;">Description</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">USBx_N</td>
      <td style="text-align: center;">I/O</td>
      <td style="text-align: left;">USB D±</td>
    </tr>
    <tr>
      <td style="text-align: left;">USBx_P</td>
      <td style="text-align: center;">I/O</td>
      <td style="text-align: left;"></td>
    </tr>
    <tr>
      <td style="text-align: left;">VBUS_ON</td>
      <td style="text-align: center;">I</td>
      <td style="text-align: left;">USB VBUS present indicator</td>
    </tr>
  </tbody>
</table>

### 4.4 Multi-Function I/O Pin Assignments

The General-Purpose Input/Output (GPIO) module provides flexible pin control and signal multiplexing capabilities. Each GPIO pin can operate as a standard input/output or be configured for one of several alternate functions, allowing efficient connection between the system and on-chip peripherals.

The tables below provide a detailed description of the signal assignments for Function 0 through Function 6, organized according to their respective interface groups.

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 12px;">
  <colgroup>
    <col width="100">
    <col width="90"><col width="90"><col width="90">
    <col width="90"><col width="90"><col width="90">
    <col width="90"><col width="90"><col width="90"><col width="90">
  </colgroup>
  <thead>
    <tr style="background-color: #f6f8fa; text-align: center;">
      <th style="padding: 8px 4px;">Group</th>
      <th style="padding: 8px 4px;">Pad Name</th>
      <th style="padding: 8px 4px;">Default Pull</th>
      <th style="padding: 8px 4px;">Pad Edge Wakeup</th>
      <th style="padding: 8px 4px;">Function 0</th>
      <th style="padding: 8px 4px;">Function 1</th>
      <th style="padding: 8px 4px;">Function 2</th>
      <th style="padding: 8px 4px;">Function 3</th>
      <th style="padding: 8px 4px;">Function 4</th>
      <th style="padding: 8px 4px;">Function 5</th>
      <th style="padding: 8px 4px;">Function 6</th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">QSPI [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">QSPI_DAT3</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">QSPI_DAT[3]</td>
      <td style="padding: 4px 2px;">GPIO[0]</td>
      <td style="padding: 4px 2px;">R.UART1_TXD</td>
      <td style="padding: 4px 2px;">R.GPIO[0]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">QSPI [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">QSPI_DAT2</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">QSPI_DAT[2]</td>
      <td style="padding: 4px 2px;">GPIO[1]</td>
      <td style="padding: 4px 2px;">R.UART1_RXD</td>
      <td style="padding: 4px 2px;">R.GPIO[1]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">QSPI [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">QSPI_DAT1</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">QSPI_DAT[1]</td>
      <td style="padding: 4px 2px;">GPIO[2]</td>
      <td style="padding: 4px 2px;">R.UART1_CTS</td>
      <td style="padding: 4px 2px;">R.GPIO[2]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">QSPI [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">QSPI_DAT0</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">QSPI_DAT[0]</td>
      <td style="padding: 4px 2px;">GPIO[3]</td>
      <td style="padding: 4px 2px;">R.UART1_RTS</td>
      <td style="padding: 4px 2px;">R.GPIO[3]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">QSPI [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">QSPI_CLK</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">QSPI_CLK</td>
      <td style="padding: 4px 2px;">GPIO[4]</td>
      <td style="padding: 4px 2px;">R.CAN1_TXD</td>
      <td style="padding: 4px 2px;">R.GPIO[4]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">QSPI [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">QSPI_CS0</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">QSPI_CS0</td>
      <td style="padding: 4px 2px;">GPIO[5]</td>
      <td style="padding: 4px 2px;">R.CAN1_RXD</td>
      <td style="padding: 4px 2px;">R.GPIO[5]</td>
      <td style="padding: 4px 2px;">I2C3_SCL</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">QSPI [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">QSPI_CS1</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">QSPI_CS1</td>
      <td style="padding: 4px 2px;">GPIO[6]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">I2C3_SDA</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">SD/MMC1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">MMC1_DAT3</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">MMC1_DAT[3]</td>
      <td style="padding: 4px 2px;">GPIO[93]</td>
      <td style="padding: 4px 2px;">UART0_TXD</td>
      <td style="padding: 4px 2px;">R.GPIO[6]</td>
      <td style="padding: 4px 2px;">R.UART0_TXD</td>
      <td style="padding: 4px 2px;">PRI_TDI</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">SD/MMC1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">MMC1_DAT2</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">MMC1_DAT[2]</td>
      <td style="padding: 4px 2px;">GPIO[94]</td>
      <td style="padding: 4px 2px;">UART0_RXD</td>
      <td style="padding: 4px 2px;">R.GPIO[7]</td>
      <td style="padding: 4px 2px;">R.UART0_RXD</td>
      <td style="padding: 4px 2px;">PRI_TMS</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">SD/MMC1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">MMC1_DAT1</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">MMC1_DAT[1]</td>
      <td style="padding: 4px 2px;">GPIO[95]</td>
      <td style="padding: 4px 2px;">UART2_TXD</td>
      <td style="padding: 4px 2px;">R.GPIO[8]</td>
      <td style="padding: 4px 2px;">PWM2</td>
      <td style="padding: 4px 2px;">PRI_TDO</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">SD/MMC1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">MMC1_DAT0</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">MMC1_DAT[0]</td>
      <td style="padding: 4px 2px;">GPIO[96]</td>
      <td style="padding: 4px 2px;">UART2_RXD</td>
      <td style="padding: 4px 2px;">R.GPIO[9]</td>
      <td style="padding: 4px 2px;">PWM3</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">SD/MMC1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">MMC1_CMD</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">MMC1_CMD</td>
      <td style="padding: 4px 2px;">GPIO[97]</td>
      <td style="padding: 4px 2px;">UART2_CTS</td>
      <td style="padding: 4px 2px;">R.GPIO[10]</td>
      <td style="padding: 4px 2px;">PWM4</td>
      <td style="padding: 4px 2px;">I2C4_SCL</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">SD/MMC1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">MMC1_CLK</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">MMC1_CLK</td>
      <td style="padding: 4px 2px;">GPIO[98]</td>
      <td style="padding: 4px 2px;">UART2_RTS</td>
      <td style="padding: 4px 2px;">R.GPIO[11]</td>
      <td style="padding: 4px 2px;">PWM5</td>
      <td style="padding: 4px 2px;">PRI_TCK</td>
      <td style="padding: 4px 2px;">I2C4_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">RESET_IN_N</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">RESET_IN_N</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM10</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">EXT_32K_IN</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">EXT_32K_IN</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM11</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PWR_SCL</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">PWR_SCL</td>
      <td style="padding: 4px 2px;">R_PWR_SCL</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM12</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PWR_SDA</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">PWR_SDA</td>
      <td style="padding: 4px 2px;">R_PWR_SDA</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM13</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">VCXO_EN</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">VCXO_EN</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM14</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PMIC_WDT_N</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">PMIC_WDT_N</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM15</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PMIC_INT_N</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">PMIC_INT_N</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM16</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PWR_SSP_TXD</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">PWR_SSP_TXD</td>
      <td style="padding: 4px 2px;">GPIO[120]</td>
      <td style="padding: 4px 2px;">I2C6_SCL</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PWR_SSP_RXD</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">PWR_SSP_RXD</td>
      <td style="padding: 4px 2px;">GPIO[121]</td>
      <td style="padding: 4px 2px;">I2C6_SDA</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PWR_SSP_SCLK</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">PWR_SSP_SCLK</td>
      <td style="padding: 4px 2px;">GPIO[122]</td>
      <td style="padding: 4px 2px;">UART0_TXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PWR_SSP_FRM</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">PWR_SSP_FRM</td>
      <td style="padding: 4px 2px;">GPIO[123]</td>
      <td style="padding: 4px 2px;">UART0_RXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PRI_TDI</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">PRI_TDI</td>
      <td style="padding: 4px 2px;">GPIO[124]</td>
      <td style="padding: 4px 2px;">R.GPIO[17]</td>
      <td style="padding: 4px 2px;">PWM6</td>
      <td style="padding: 4px 2px;">UART5_TXD</td>
      <td style="padding: 4px 2px;">UART0_TXD</td>
      <td style="padding: 4px 2px;">R.UART0_TXD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PRI_TMS</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">PRI_TMS</td>
      <td style="padding: 4px 2px;">GPIO[125]</td>
      <td style="padding: 4px 2px;">R.GPIO[14]</td>
      <td style="padding: 4px 2px;">PWM7</td>
      <td style="padding: 4px 2px;">UART5_RXD</td>
      <td style="padding: 4px 2px;">UART0_RXD</td>
      <td style="padding: 4px 2px;">R.UART0_RXD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PRI_TCK</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">PRI_TCK</td>
      <td style="padding: 4px 2px;">GPIO[126]</td>
      <td style="padding: 4px 2px;">R.GPIO[15]</td>
      <td style="padding: 4px 2px;">PWM8</td>
      <td style="padding: 4px 2px;">UART9_TXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PRI_TDO</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">PRI_TDO</td>
      <td style="padding: 4px 2px;">GPIO[127]</td>
      <td style="padding: 4px 2px;">R.GPIO[16]</td>
      <td style="padding: 4px 2px;">PWM9</td>
      <td style="padding: 4px 2px;">UART9_RXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">PMIC [1.8V only]</td>
      <td style="padding: 4px 2px;">PRI_TRST_N</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">NO</td>
      <td style="padding: 4px 2px;">PRI_TRSTn</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D0</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D0</td>
      <td style="padding: 4px 2px;">GPIO[32]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D1</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D1</td>
      <td style="padding: 4px 2px;">GPIO[33]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D2</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D2</td>
      <td style="padding: 4px 2px;">GPIO[34]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D3</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D3</td>
      <td style="padding: 4px 2px;">GPIO[35]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D4</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D4</td>
      <td style="padding: 4px 2px;">GPIO[36]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D5</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D5</td>
      <td style="padding: 4px 2px;">R.GPIO[8]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D6</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D6</td>
      <td style="padding: 4px 2px;">R.GPIO[9]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_D7</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_D7</td>
      <td style="padding: 4px 2px;">R.GPIO[10]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_DS</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_DS</td>
      <td style="padding: 4px 2px;">R.GPIO[11]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_CLK</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_CLK</td>
      <td style="padding: 4px 2px;">R.GPIO[12]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">EMMC5 [1.8V only]</td>
      <td style="padding: 4px 2px;">EMMC_CMD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">EMMC_CMD</td>
      <td style="padding: 4px 2px;">R.GPIO[13]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[0]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[0]</td>
      <td style="padding: 4px 2px;">GMAC0_RXDV</td>
      <td style="padding: 4px 2px;">SSPA5_CLK</td>
      <td style="padding: 4px 2px;">PWM0</td>
      <td style="padding: 4px 2px;">IR1_RX</td>
      <td style="padding: 4px 2px;">eSPI0_D0</td>
      <td style="padding: 4px 2px;">I2C0_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[1]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[1]</td>
      <td style="padding: 4px 2px;">GMAC0_RX_D0</td>
      <td style="padding: 4px 2px;">SSPA5_FRM</td>
      <td style="padding: 4px 2px;">PWM1</td>
      <td style="padding: 4px 2px;">R.IR1_RX</td>
      <td style="padding: 4px 2px;">eSPI0_D1</td>
      <td style="padding: 4px 2px;">I2C0_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[2]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[2]</td>
      <td style="padding: 4px 2px;">GMAC0_RX_D1</td>
      <td style="padding: 4px 2px;">SSPA5_TXD</td>
      <td style="padding: 4px 2px;">PWM2</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">eSPI0_D2</td>
      <td style="padding: 4px 2px;">I2C1_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[3]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[3]</td>
      <td style="padding: 4px 2px;">GMAC0_RX_CLK</td>
      <td style="padding: 4px 2px;">SSPA5_RXD</td>
      <td style="padding: 4px 2px;">PWM3</td>
      <td style="padding: 4px 2px;">PCIeD_PERSTn</td>
      <td style="padding: 4px 2px;">eSPI0_D3</td>
      <td style="padding: 4px 2px;">I2C1_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[4]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[4]</td>
      <td style="padding: 4px 2px;">GMAC0_RX_D2</td>
      <td style="padding: 4px 2px;">SSPA5_SYSCLK</td>
      <td style="padding: 4px 2px;">PWM4</td>
      <td style="padding: 4px 2px;">PCIeD_WAKEn</td>
      <td style="padding: 4px 2px;">eSPI0_CS</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[5]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[5]</td>
      <td style="padding: 4px 2px;">GMAC0_RX_D3</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM5</td>
      <td style="padding: 4px 2px;">PCIeD_CLKREQn</td>
      <td style="padding: 4px 2px;">eSPI0_CLK</td>
      <td style="padding: 4px 2px;">I2C2_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[6]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[6]</td>
      <td style="padding: 4px 2px;">GMAC0_TX_D0</td>
      <td style="padding: 4px 2px;">R.SSPA0_CLK</td>
      <td style="padding: 4px 2px;">PWM6</td>
      <td style="padding: 4px 2px;">PCIeD_PRSNT2n</td>
      <td style="padding: 4px 2px;">eSPI0_RESETN</td>
      <td style="padding: 4px 2px;">I2C2_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[7]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[7]</td>
      <td style="padding: 4px 2px;">GMAC0_TX_D1</td>
      <td style="padding: 4px 2px;">R.SSPA0_FRM</td>
      <td style="padding: 4px 2px;">PWM7</td>
      <td style="padding: 4px 2px;">PCIeD_ATTn</td>
      <td style="padding: 4px 2px;">eSPI0_ALERT</td>
      <td style="padding: 4px 2px;">I2C6_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[8]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[8]</td>
      <td style="padding: 4px 2px;">GMAC0_TX_CLK</td>
      <td style="padding: 4px 2px;">R.SSPA0_TXD</td>
      <td style="padding: 4px 2px;">PWM8</td>
      <td style="padding: 4px 2px;">PCIeD_AUXen</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">I2C6_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[9]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[9]</td>
      <td style="padding: 4px 2px;">GMAC0_TX_D2</td>
      <td style="padding: 4px 2px;">R.SSPA0_RXD</td>
      <td style="padding: 4px 2px;">PWM9</td>
      <td style="padding: 4px 2px;">PCIeD_PWRCTn</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">e/DP0_HPD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[10]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[10]</td>
      <td style="padding: 4px 2px;">GMAC0_TX_D3</td>
      <td style="padding: 4px 2px;">R.SSPA0_SYSCLK</td>
      <td style="padding: 4px 2px;">PWM10</td>
      <td style="padding: 4px 2px;">PCIeD_PWRDet</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">e/DP1_HPD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[11]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[11]</td>
      <td style="padding: 4px 2px;">GMAC0_TX_EN</td>
      <td style="padding: 4px 2px;">UART7_RTSn</td>
      <td style="padding: 4px 2px;">CAN0_TXD</td>
      <td style="padding: 4px 2px;">UART8_RXD</td>
      <td style="padding: 4px 2px;">I2C4_SCL</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[12]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[12]</td>
      <td style="padding: 4px 2px;">GMAC0_MDC</td>
      <td style="padding: 4px 2px;">UART7_CTSn</td>
      <td style="padding: 4px 2px;">CAN0_RXD</td>
      <td style="padding: 4px 2px;">PCIeC_PERSTn</td>
      <td style="padding: 4px 2px;">UART8_TXD</td>
      <td style="padding: 4px 2px;">I2C4_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[13]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[13]</td>
      <td style="padding: 4px 2px;">GMAC0_MDIO</td>
      <td style="padding: 4px 2px;">UART7_TXD</td>
      <td style="padding: 4px 2px;">PWM13</td>
      <td style="padding: 4px 2px;">PCIeC_WAKEn</td>
      <td style="padding: 4px 2px;">CLK_CAMCK1</td>
      <td style="padding: 4px 2px;">DSI0_TE</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[14]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[14]</td>
      <td style="padding: 4px 2px;">GMAC0_INT_N</td>
      <td style="padding: 4px 2px;">UART7_RXD</td>
      <td style="padding: 4px 2px;">PWM14</td>
      <td style="padding: 4px 2px;">PCIeC_CLKREQn</td>
      <td style="padding: 4px 2px;">MNCLK_OUT1</td>
      <td style="padding: 4px 2px;">I2C6_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[15]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[15]</td>
      <td style="padding: 4px 2px;">GMAC0_RXER</td>
      <td style="padding: 4px 2px;">SSPA1_CLK</td>
      <td style="padding: 4px 2px;">R.PWM0</td>
      <td style="padding: 4px 2px;">PCIeC_PRSNT2n</td>
      <td style="padding: 4px 2px;">MNCLK_OUT2</td>
      <td style="padding: 4px 2px;">I2C6_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[16]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[16]</td>
      <td style="padding: 4px 2px;">GMAC0_TXER</td>
      <td style="padding: 4px 2px;">SSPA1_FRM</td>
      <td style="padding: 4px 2px;">R.PWM1</td>
      <td style="padding: 4px 2px;">PCIeC_ATTn</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">USB20_HOST_DRV</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[17]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[17]</td>
      <td style="padding: 4px 2px;">GMAC0_CRS</td>
      <td style="padding: 4px 2px;">SSPA1_TXD</td>
      <td style="padding: 4px 2px;">R.PWM2</td>
      <td style="padding: 4px 2px;">PCIeC_PWRCTn</td>
      <td style="padding: 4px 2px;">R.UART1_TXD</td>
      <td style="padding: 4px 2px;">USB30_DRD_ID</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[18]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[18]</td>
      <td style="padding: 4px 2px;">GMAC0_COL</td>
      <td style="padding: 4px 2px;">SSPA1_RXD</td>
      <td style="padding: 4px 2px;">R.PWM3</td>
      <td style="padding: 4px 2px;">PCIeC_AUXen</td>
      <td style="padding: 4px 2px;">R.UART1_RXD</td>
      <td style="padding: 4px 2px;">USB30_DRD_VBUSON</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[19]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[19]</td>
      <td style="padding: 4px 2px;">GMAC0_PPS</td>
      <td style="padding: 4px 2px;">SSPA1_SYSCLK</td>
      <td style="padding: 4px 2px;">R.PWM4</td>
      <td style="padding: 4px 2px;">PCIeC_PWRDet</td>
      <td style="padding: 4px 2px;">R.UART1_CTSn</td>
      <td style="padding: 4px 2px;">USB30_DRD_DRV</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO1 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[20]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[20]</td>
      <td style="padding: 4px 2px;">GMAC0_CLK_REF</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.PWM5</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.UART1_RTSn</td>
      <td style="padding: 4px 2px;">USB30_D_DRV</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[21]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[21]</td>
      <td style="padding: 4px 2px;">GMAC1_RXDV</td>
      <td style="padding: 4px 2px;">UART5_TXD</td>
      <td style="padding: 4px 2px;">PWM15</td>
      <td style="padding: 4px 2px;">PCIeB_PERSTn</td>
      <td style="padding: 4px 2px;">R.UART4_TXD</td>
      <td style="padding: 4px 2px;">R.GPIO[28]</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[22]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[22]</td>
      <td style="padding: 4px 2px;">GMAC1_RX_D0</td>
      <td style="padding: 4px 2px;">UART5_RXD</td>
      <td style="padding: 4px 2px;">PWM16</td>
      <td style="padding: 4px 2px;">PCIeB_WAKEn</td>
      <td style="padding: 4px 2px;">R.UART4_RXD</td>
      <td style="padding: 4px 2px;">R.GPIO[29]</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[23]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[23]</td>
      <td style="padding: 4px 2px;">GMAC1_RX_D1</td>
      <td style="padding: 4px 2px;">UART5_CTS</td>
      <td style="padding: 4px 2px;">PWM17</td>
      <td style="padding: 4px 2px;">PCIeB_CLKREQn</td>
      <td style="padding: 4px 2px;">UART7_TXD</td>
      <td style="padding: 4px 2px;">e/DP0_HPD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[24]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[24]</td>
      <td style="padding: 4px 2px;">GMAC1_RX_CLK</td>
      <td style="padding: 4px 2px;">UART5_RTS</td>
      <td style="padding: 4px 2px;">PWM18</td>
      <td style="padding: 4px 2px;">PCIeB_PRSNT2n</td>
      <td style="padding: 4px 2px;">UART7_RXD</td>
      <td style="padding: 4px 2px;">e/DP1_HPD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[25]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[25]</td>
      <td style="padding: 4px 2px;">GMAC1_RX_D2</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM19</td>
      <td style="padding: 4px 2px;">PCIeC_PERSTn</td>
      <td style="padding: 4px 2px;">UART7_CTSn</td>
      <td style="padding: 4px 2px;">I2C5_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[26]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[26]</td>
      <td style="padding: 4px 2px;">GMAC1_RX_D3</td>
      <td style="padding: 4px 2px;">UART3_TXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeC_WAKEn</td>
      <td style="padding: 4px 2px;">UART7_RTSn</td>
      <td style="padding: 4px 2px;">I2C5_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[27]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[27]</td>
      <td style="padding: 4px 2px;">GMAC1_TX_D0</td>
      <td style="padding: 4px 2px;">UART3_RXD</td>
      <td style="padding: 4px 2px;">R.PWM0</td>
      <td style="padding: 4px 2px;">PCIeC_CLKREQn</td>
      <td style="padding: 4px 2px;">USB30_D_DRV</td>
      <td style="padding: 4px 2px;">R.I2C0_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[28]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[28]</td>
      <td style="padding: 4px 2px;">GMAC1_TX_D1</td>
      <td style="padding: 4px 2px;">UART3_CTS</td>
      <td style="padding: 4px 2px;">R.PWM1</td>
      <td style="padding: 4px 2px;">PCIeC_PRSNT2n</td>
      <td style="padding: 4px 2px;">SSP2_TXD</td>
      <td style="padding: 4px 2px;">R.I2C0_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[29]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[29]</td>
      <td style="padding: 4px 2px;">GMAC1_TX_CLK</td>
      <td style="padding: 4px 2px;">UART3_RTS</td>
      <td style="padding: 4px 2px;">R.PWM2</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">SSP2_RXD</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[30]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[30]</td>
      <td style="padding: 4px 2px;">GMAC1_TX_D2</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.PWM3</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">SSP2_SCLK</td>
      <td style="padding: 4px 2px;">EDP0_HPD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[31]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[31]</td>
      <td style="padding: 4px 2px;">GMAC1_TX_D3</td>
      <td style="padding: 4px 2px;">UART10_TXD</td>
      <td style="padding: 4px 2px;">R.PWM4</td>
      <td style="padding: 4px 2px;">PCIeE_PERSTn</td>
      <td style="padding: 4px 2px;">SSP2_FRM</td>
      <td style="padding: 4px 2px;">EDP1_HPD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[32]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[32]</td>
      <td style="padding: 4px 2px;">GMAC1_TX_EN</td>
      <td style="padding: 4px 2px;">UART10_RXD</td>
      <td style="padding: 4px 2px;">R.PWM5</td>
      <td style="padding: 4px 2px;">PCIeE_WAKEn</td>
      <td style="padding: 4px 2px;">SSP1_TXD</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[33]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[33]</td>
      <td style="padding: 4px 2px;">GMAC1_MDC</td>
      <td style="padding: 4px 2px;">UART10_CTS</td>
      <td style="padding: 4px 2px;">R.PWM6</td>
      <td style="padding: 4px 2px;">PCIeE_CLKREQn</td>
      <td style="padding: 4px 2px;">SSP1_RXD</td>
      <td style="padding: 4px 2px;">R.I2C1_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[34]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[34]</td>
      <td style="padding: 4px 2px;">GMAC1_MDIO</td>
      <td style="padding: 4px 2px;">UART10_RTS</td>
      <td style="padding: 4px 2px;">R.PWM7</td>
      <td style="padding: 4px 2px;">CLK_CAMCK2</td>
      <td style="padding: 4px 2px;">SSP1_SCLK</td>
      <td style="padding: 4px 2px;">R.I2C1_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[35]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[35]</td>
      <td style="padding: 4px 2px;">GMAC1_INT_N</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.PWM8</td>
      <td style="padding: 4px 2px;">CLK_CAMCK3</td>
      <td style="padding: 4px 2px;">SSP1_FRM</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[36]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[36]</td>
      <td style="padding: 4px 2px;">GMAC1_CLK_REF</td>
      <td style="padding: 4px 2px;">R.SSPA1_CLK</td>
      <td style="padding: 4px 2px;">R.PWM9</td>
      <td style="padding: 4px 2px;">I2C3_SCL</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[37]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[37]</td>
      <td style="padding: 4px 2px;">GMAC1_RXER</td>
      <td style="padding: 4px 2px;">R.SSPA1_FRM</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">I2C3_SDA</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[38]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[38]</td>
      <td style="padding: 4px 2px;">GMAC1_TXER</td>
      <td style="padding: 4px 2px;">R.SSPA1_TXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">DSI0_TE</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[39]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[39]</td>
      <td style="padding: 4px 2px;">GMAC1_CRS</td>
      <td style="padding: 4px 2px;">R.SSPA1_RXD</td>
      <td style="padding: 4px 2px;">MNCLK_OUT1</td>
      <td style="padding: 4px 2px;">R.I2C1_SCL</td>
      <td style="padding: 4px 2px;">USB20_HOST_DRV</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[40]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[40]</td>
      <td style="padding: 4px 2px;">GMAC1_COL</td>
      <td style="padding: 4px 2px;">R.SSPA1_SYSCLK</td>
      <td style="padding: 4px 2px;">MNCLK_OUT2</td>
      <td style="padding: 4px 2px;">R.I2C1_SDA</td>
      <td style="padding: 4px 2px;">R.IR0_RX</td>
      <td style="padding: 4px 2px;">CAN4_TXD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO2 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[41]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[41]</td>
      <td style="padding: 4px 2px;">GMAC1_PPS</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">CLK32K_OUT</td>
      <td style="padding: 4px 2px;">IR0_RX</td>
      <td style="padding: 4px 2px;">CAN4_RXD</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[42]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[42]</td>
      <td style="padding: 4px 2px;">GMAC2_RXDV</td>
      <td style="padding: 4px 2px;">UART0_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_PERSTn</td>
      <td style="padding: 4px 2px;">I2C0_SCL</td>
      <td style="padding: 4px 2px;">PWM0</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[43]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[43]</td>
      <td style="padding: 4px 2px;">GMAC2_RX_D0</td>
      <td style="padding: 4px 2px;">UART0_RXD</td>
      <td style="padding: 4px 2px;">CLK_CAMCK4</td>
      <td style="padding: 4px 2px;">I2C0_SDA</td>
      <td style="padding: 4px 2px;">PWM1</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[44]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[44]</td>
      <td style="padding: 4px 2px;">GMAC2_RX_D1</td>
      <td style="padding: 4px 2px;">UART10_TXD</td>
      <td style="padding: 4px 2px;">CAN0_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_CLKREQn</td>
      <td style="padding: 4px 2px;">PWM2</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[45]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[45]</td>
      <td style="padding: 4px 2px;">GMAC2_RX_CLK</td>
      <td style="padding: 4px 2px;">UART10_RXD</td>
      <td style="padding: 4px 2px;">CAN0_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_PRSNT2n</td>
      <td style="padding: 4px 2px;">PWM3</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[46]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[46]</td>
      <td style="padding: 4px 2px;">GMAC2_RX_D2</td>
      <td style="padding: 4px 2px;">UART10_CTSn</td>
      <td style="padding: 4px 2px;">CLK_CAMCK1</td>
      <td style="padding: 4px 2px;">PCIeA_ATTn</td>
      <td style="padding: 4px 2px;">I2C2_SCL</td>
      <td style="padding: 4px 2px;">PWM4</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[47]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[47]</td>
      <td style="padding: 4px 2px;">GMAC2_RX_D3</td>
      <td style="padding: 4px 2px;">UART10_RTSn</td>
      <td style="padding: 4px 2px;">CLK_CAMCK2</td>
      <td style="padding: 4px 2px;">PCIeA_PWRCTn</td>
      <td style="padding: 4px 2px;">I2C2_SDA</td>
      <td style="padding: 4px 2px;">PWM5</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[48]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[48]</td>
      <td style="padding: 4px 2px;">GMAC2_TX_D0</td>
      <td style="padding: 4px 2px;">UART6_TXD</td>
      <td style="padding: 4px 2px;">CAN1_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_AUXen</td>
      <td style="padding: 4px 2px;">I2C0_SCL</td>
      <td style="padding: 4px 2px;">PWM6</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[49]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[49]</td>
      <td style="padding: 4px 2px;">GMAC2_TX_D1</td>
      <td style="padding: 4px 2px;">UART6_RXD</td>
      <td style="padding: 4px 2px;">CAN1_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_PWRDet</td>
      <td style="padding: 4px 2px;">I2C0_SDA</td>
      <td style="padding: 4px 2px;">PWM7</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[50]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[50]</td>
      <td style="padding: 4px 2px;">GMAC2_TX_CLK</td>
      <td style="padding: 4px 2px;">UART6_CTS</td>
      <td style="padding: 4px 2px;">CAN2_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_MRLn</td>
      <td style="padding: 4px 2px;">I2C4_SCL</td>
      <td style="padding: 4px 2px;">PWM8</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[51]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[51]</td>
      <td style="padding: 4px 2px;">GMAC2_TX_D2</td>
      <td style="padding: 4px 2px;">UART6_RTS</td>
      <td style="padding: 4px 2px;">CAN2_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_ATNLED</td>
      <td style="padding: 4px 2px;">I2C4_SDA</td>
      <td style="padding: 4px 2px;">PWM9</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[52]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[52]/Strap[5]</td>
      <td style="padding: 4px 2px;">GMAC2_TX_D3</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeA_PWRLED</td>
      <td style="padding: 4px 2px;">CLK_CAMCK3</td>
      <td style="padding: 4px 2px;">PWM10</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[53]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[53]</td>
      <td style="padding: 4px 2px;">GMAC2_TX_EN</td>
      <td style="padding: 4px 2px;">UART3_CTSn</td>
      <td style="padding: 4px 2px;">SSP0_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_EINT</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM11</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[54]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[54]</td>
      <td style="padding: 4px 2px;">GMAC2_MDC</td>
      <td style="padding: 4px 2px;">UART3_RTSn</td>
      <td style="padding: 4px 2px;">SSP0_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_EINTEG</td>
      <td style="padding: 4px 2px;">I2C1_SCL</td>
      <td style="padding: 4px 2px;">PWM12</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[55]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[55]</td>
      <td style="padding: 4px 2px;">GMAC2_MDIO</td>
      <td style="padding: 4px 2px;">UART3_RXD</td>
      <td style="padding: 4px 2px;">SSP0_SCLK</td>
      <td style="padding: 4px 2px;">R.UART3_RXD</td>
      <td style="padding: 4px 2px;">I2C1_SDA</td>
      <td style="padding: 4px 2px;">PWM13</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[56]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[56]</td>
      <td style="padding: 4px 2px;">GMAC2_INT_N</td>
      <td style="padding: 4px 2px;">UART3_TXD</td>
      <td style="padding: 4px 2px;">SSP0_FRM</td>
      <td style="padding: 4px 2px;">R.UART3_TXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM14</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[57]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[57]</td>
      <td style="padding: 4px 2px;">GMAC2_CLK_REF</td>
      <td style="padding: 4px 2px;">R.UART2_TXD</td>
      <td style="padding: 4px 2px;">R.CAN0_RXD</td>
      <td style="padding: 4px 2px;">EDP0_HPD</td>
      <td style="padding: 4px 2px;">R.I2C0_SCL</td>
      <td style="padding: 4px 2px;">PWM15</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[58]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[58]</td>
      <td style="padding: 4px 2px;">GMAC2_PPS</td>
      <td style="padding: 4px 2px;">R.UART2_RXD</td>
      <td style="padding: 4px 2px;">R.CAN0_TXD</td>
      <td style="padding: 4px 2px;">PCIeC_PERSTn</td>
      <td style="padding: 4px 2px;">R.I2C0_SDA</td>
      <td style="padding: 4px 2px;">PWM16</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[59]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[59]</td>
      <td style="padding: 4px 2px;">R.GMAC3_RXDV</td>
      <td style="padding: 4px 2px;">R.UART5_TXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeC_WAKEn</td>
      <td style="padding: 4px 2px;">R.I2C1_SCL</td>
      <td style="padding: 4px 2px;">PWM17</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[60]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[60]</td>
      <td style="padding: 4px 2px;">R.GMAC3_RX_D0</td>
      <td style="padding: 4px 2px;">R.UART5_RXD</td>
      <td style="padding: 4px 2px;">R.SSP0_TXD</td>
      <td style="padding: 4px 2px;">PCIeC_CLKREQn</td>
      <td style="padding: 4px 2px;">R.I2C1_SDA</td>
      <td style="padding: 4px 2px;">PWM18</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[61]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[61]</td>
      <td style="padding: 4px 2px;">R.GMAC3_RX_D1</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.SSP0_RXD</td>
      <td style="padding: 4px 2px;">PCIeC_PRSNT2n</td>
      <td style="padding: 4px 2px;">I2C6_SCL</td>
      <td style="padding: 4px 2px;">PWM19</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[62]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[62]</td>
      <td style="padding: 4px 2px;">R.GMAC3_RX_CLK</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.SSP0_SCLK</td>
      <td style="padding: 4px 2px;">PCIeC_ATTn</td>
      <td style="padding: 4px 2px;">I2C6_SDA</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[63]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[63]</td>
      <td style="padding: 4px 2px;">R.GMAC3_RX_D2</td>
      <td style="padding: 4px 2px;">R.GPIO[18]</td>
      <td style="padding: 4px 2px;">R.SSP0_FRM</td>
      <td style="padding: 4px 2px;">PCIeC_PWRCTn</td>
      <td style="padding: 4px 2px;">I2C5_SCL</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[64]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[64]/Strap[4]</td>
      <td style="padding: 4px 2px;">R.GMAC3_RX_D3</td>
      <td style="padding: 4px 2px;">R.GPIO[19]</td>
      <td style="padding: 4px 2px;">R.SSP1_TXD</td>
      <td style="padding: 4px 2px;">PCIeC_AUXen</td>
      <td style="padding: 4px 2px;">I2C5_SDA</td>
      <td style="padding: 4px 2px;">R.PWM0</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[65]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[65]/Strap[0]</td>
      <td style="padding: 4px 2px;">R.GMAC3_TX_D0</td>
      <td style="padding: 4px 2px;">R.GPIO[20]</td>
      <td style="padding: 4px 2px;">R.SSP1_RXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.PWM1</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[66]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[66]/Strap[1]</td>
      <td style="padding: 4px 2px;">R.GMAC3_TX_D1</td>
      <td style="padding: 4px 2px;">R.GPIO[21]</td>
      <td style="padding: 4px 2px;">R.SSP1_SCLK</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.PWM2</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[67]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[67]</td>
      <td style="padding: 4px 2px;">R.GMAC3_TX_CLK</td>
      <td style="padding: 4px 2px;">R.GPIO[22]</td>
      <td style="padding: 4px 2px;">R.SSP1_FRM</td>
      <td style="padding: 4px 2px;">CLK_CAMCK4</td>
      <td style="padding: 4px 2px;">PCIeC_PWRDet</td>
      <td style="padding: 4px 2px;">R.PWM3</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[68]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[68]/Strap[2]</td>
      <td style="padding: 4px 2px;">R.GMAC3_TX_D2</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">eSPI0_D0</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">SSP3_TXD</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[69]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[69]/Strap[3]</td>
      <td style="padding: 4px 2px;">R.GMAC3_TX_D3</td>
      <td style="padding: 4px 2px;">SSPA4_CLK</td>
      <td style="padding: 4px 2px;">eSPI0_D1</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">SSP3_RXD</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[70]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[70]</td>
      <td style="padding: 4px 2px;">R.GMAC3_TX_EN</td>
      <td style="padding: 4px 2px;">SSPA4_FRM</td>
      <td style="padding: 4px 2px;">eSPI0_D2</td>
      <td style="padding: 4px 2px;">IR1_RX</td>
      <td style="padding: 4px 2px;">MNCLK_OUT1</td>
      <td style="padding: 4px 2px;">SSP3_SCLK</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[71]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[71]</td>
      <td style="padding: 4px 2px;">R.GMAC3_MDC</td>
      <td style="padding: 4px 2px;">SSPA4_TXD</td>
      <td style="padding: 4px 2px;">eSPI0_D3</td>
      <td style="padding: 4px 2px;">R.IR0_RX</td>
      <td style="padding: 4px 2px;">MNCLK_OUT2</td>
      <td style="padding: 4px 2px;">SSP3_FRM</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[72]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[72]</td>
      <td style="padding: 4px 2px;">R.GMAC3_MDIO</td>
      <td style="padding: 4px 2px;">SSPA4_RXD</td>
      <td style="padding: 4px 2px;">eSPI0_CS</td>
      <td style="padding: 4px 2px;">e/DP1_HPD</td>
      <td style="padding: 4px 2px;">DSI0_TE</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[73]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[73]</td>
      <td style="padding: 4px 2px;">R.GMAC3_INT_N</td>
      <td style="padding: 4px 2px;">SSPA4_SYSCLK</td>
      <td style="padding: 4px 2px;">eSPI0_CLK</td>
      <td style="padding: 4px 2px;">R.IR1_RX</td>
      <td style="padding: 4px 2px;">USB20_HOST_DRV</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[74]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[74]</td>
      <td style="padding: 4px 2px;">R.GMAC3_CLK_REF</td>
      <td style="padding: 4px 2px;">CLK_CAMCK2</td>
      <td style="padding: 4px 2px;">eSPI0_RESETN</td>
      <td style="padding: 4px 2px;">VCXO_REQ</td>
      <td style="padding: 4px 2px;">USB30H-1_DRV</td>
      <td style="padding: 4px 2px;">R.I2C0_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO3 [1.8V only]</td>
      <td style="padding: 4px 2px;">GPIO_[75]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[75]</td>
      <td style="padding: 4px 2px;">R.GMAC3_PPS</td>
      <td style="padding: 4px 2px;">CLK_CAMCK1</td>
      <td style="padding: 4px 2px;">eSPI0_ALERT</td>
      <td style="padding: 4px 2px;">VCXO_OUT</td>
      <td style="padding: 4px 2px;">USB30H-2_DRV</td>
      <td style="padding: 4px 2px;">R.I2C0_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[76]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[76]</td>
      <td style="padding: 4px 2px;">R.SSPA0_CLK</td>
      <td style="padding: 4px 2px;">SSPA2_CLK</td>
      <td style="padding: 4px 2px;">UART8_TXD</td>
      <td style="padding: 4px 2px;">CAN0_TXD</td>
      <td style="padding: 4px 2px;">PCIeE_PERSTn</td>
      <td style="padding: 4px 2px;">I2C0_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[77]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[77]</td>
      <td style="padding: 4px 2px;">R.SSPA0_FRM</td>
      <td style="padding: 4px 2px;">SSPA2_FRM</td>
      <td style="padding: 4px 2px;">UART8_RXD</td>
      <td style="padding: 4px 2px;">CAN0_RXD</td>
      <td style="padding: 4px 2px;">PCIeE_WAKEn</td>
      <td style="padding: 4px 2px;">I2C0_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[78]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[78]</td>
      <td style="padding: 4px 2px;">R.SSPA0_TXD</td>
      <td style="padding: 4px 2px;">SSPA2_TXD</td>
      <td style="padding: 4px 2px;">UART8_CTS</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeE_CLKREQn</td>
      <td style="padding: 4px 2px;">I2C1_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[79]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[79]</td>
      <td style="padding: 4px 2px;">R.SSPA0_RXD</td>
      <td style="padding: 4px 2px;">SSPA2_RXD</td>
      <td style="padding: 4px 2px;">UART8_RTS</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeA_PERSTn</td>
      <td style="padding: 4px 2px;">I2C1_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[80]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[80]</td>
      <td style="padding: 4px 2px;">R.SSPA0_SYSCLK</td>
      <td style="padding: 4px 2px;">SSPA2_SYSCLK</td>
      <td style="padding: 4px 2px;">R.UART4_TXD</td>
      <td style="padding: 4px 2px;">CAN3_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_WAKEn</td>
      <td style="padding: 4px 2px;">I2C2_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[81]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[81]</td>
      <td style="padding: 4px 2px;">SSP0_TXD</td>
      <td style="padding: 4px 2px;">SSA0_CLK</td>
      <td style="padding: 4px 2px;">R.UART4_RXD</td>
      <td style="padding: 4px 2px;">CAN3_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_CLKREQn</td>
      <td style="padding: 4px 2px;">I2C2_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[82]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[82]</td>
      <td style="padding: 4px 2px;">SSP0_RXD</td>
      <td style="padding: 4px 2px;">SSA0_FRM</td>
      <td style="padding: 4px 2px;">UART9_CTSn</td>
      <td style="padding: 4px 2px;">UART5_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_PRSNT2n</td>
      <td style="padding: 4px 2px;">I2C3_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[83]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[83]</td>
      <td style="padding: 4px 2px;">SSP0_SCLK</td>
      <td style="padding: 4px 2px;">SSA0_TXD</td>
      <td style="padding: 4px 2px;">UART9_RTSn</td>
      <td style="padding: 4px 2px;">UART5_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_ATTn</td>
      <td style="padding: 4px 2px;">I2C3_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[84]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[84]</td>
      <td style="padding: 4px 2px;">SSP0_FRM</td>
      <td style="padding: 4px 2px;">SSA0_RXD</td>
      <td style="padding: 4px 2px;">UART9_TXD</td>
      <td style="padding: 4px 2px;">USB30_B_DRV</td>
      <td style="padding: 4px 2px;">PCIeA_PWRCTn</td>
      <td style="padding: 4px 2px;">DSI0_TE</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[85]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[85]</td>
      <td style="padding: 4px 2px;">CLK_CAMCK3</td>
      <td style="padding: 4px 2px;">SSA0_SYSCLK</td>
      <td style="padding: 4px 2px;">UART9_RXD</td>
      <td style="padding: 4px 2px;">USB30_C_DRV</td>
      <td style="padding: 4px 2px;">PCIeA_AUXen</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[86]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[86]</td>
      <td style="padding: 4px 2px;">R.SSP0_TXD</td>
      <td style="padding: 4px 2px;">R.eSPI0_D0</td>
      <td style="padding: 4px 2px;">UART4_TXD</td>
      <td style="padding: 4px 2px;">CAN2_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_PWRDet</td>
      <td style="padding: 4px 2px;">USB30_DRD_DIR</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[87]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[87]</td>
      <td style="padding: 4px 2px;">R.SSP0_RXD</td>
      <td style="padding: 4px 2px;">R.eSPI0_D1</td>
      <td style="padding: 4px 2px;">UART4_RXD</td>
      <td style="padding: 4px 2px;">CAN2_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_MRLn</td>
      <td style="padding: 4px 2px;">PCIeB_PRSNT2n</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[88]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[88]</td>
      <td style="padding: 4px 2px;">R.SSP0_SCLK</td>
      <td style="padding: 4px 2px;">R.eSPI0_D2</td>
      <td style="padding: 4px 2px;">R.UART3_TXD</td>
      <td style="padding: 4px 2px;">PCIeB_PERSTn</td>
      <td style="padding: 4px 2px;">PCIeA_ATNLED</td>
      <td style="padding: 4px 2px;">CAN1_RXD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[89]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[89]</td>
      <td style="padding: 4px 2px;">R.SSP0_FRM</td>
      <td style="padding: 4px 2px;">R.eSPI0_D3</td>
      <td style="padding: 4px 2px;">R.UART3_RXD</td>
      <td style="padding: 4px 2px;">PCIeB_WAKEn</td>
      <td style="padding: 4px 2px;">PCIeA_PWRLED</td>
      <td style="padding: 4px 2px;">CAN1_TXD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[90]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[90]</td>
      <td style="padding: 4px 2px;">DSI0_TE</td>
      <td style="padding: 4px 2px;">R.eSPI0_CS</td>
      <td style="padding: 4px 2px;">UART4_CTSn</td>
      <td style="padding: 4px 2px;">PCIeB_CLKREQn</td>
      <td style="padding: 4px 2px;">PCIeA_EINT</td>
      <td style="padding: 4px 2px;">R.CAN0_RXD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[91]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[91]</td>
      <td style="padding: 4px 2px;">R.GPIO[23]</td>
      <td style="padding: 4px 2px;">R.eSPI0_CLK</td>
      <td style="padding: 4px 2px;">UART4_RTSn</td>
      <td style="padding: 4px 2px;">eSPI0_D0</td>
      <td style="padding: 4px 2px;">PCIeA_EINTEG</td>
      <td style="padding: 4px 2px;">R.CAN0_TXD</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[92]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[92]</td>
      <td style="padding: 4px 2px;">R.GPIO[24]</td>
      <td style="padding: 4px 2px;">R.eSPI0_RESETN</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">eSPI0_D1</td>
      <td style="padding: 4px 2px;">R.PWM5</td>
      <td style="padding: 4px 2px;">DSI0_TE</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[93]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[93]</td>
      <td style="padding: 4px 2px;">R.GPIO[25]</td>
      <td style="padding: 4px 2px;">R.eSPI0_ALERT</td>
      <td style="padding: 4px 2px;">UART0_TXD</td>
      <td style="padding: 4px 2px;">eSPI0_D2</td>
      <td style="padding: 4px 2px;">I2C5_SCL</td>
      <td style="padding: 4px 2px;">R.PWM4</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[94]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[94]</td>
      <td style="padding: 4px 2px;">R.GPIO[26]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">UART0_RXD</td>
      <td style="padding: 4px 2px;">eSPI0_D3</td>
      <td style="padding: 4px 2px;">I2C5_SDA</td>
      <td style="padding: 4px 2px;">R.PWM6</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[95]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[95]</td>
      <td style="padding: 4px 2px;">R.GPIO[27]</td>
      <td style="padding: 4px 2px;">UART1_TXD&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">USB30_DRD_ID</td>
      <td style="padding: 4px 2px;">eSPI0_CS</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM1</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[96]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[96]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">UART1_RXD&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">USB30_DRD_VBUSON</td>
      <td style="padding: 4px 2px;">eSPI0_CLK</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PWM2</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[97]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[97]</td>
      <td style="padding: 4px 2px;">UART2_TXD</td>
      <td style="padding: 4px 2px;">UART1_CTS&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">USB30_DRD_DRV</td>
      <td style="padding: 4px 2px;">eSPI0_RESETN</td>
      <td style="padding: 4px 2px;">e/DP0_HPD</td>
      <td style="padding: 4px 2px;">PWM3</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO4 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[98]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[98]</td>
      <td style="padding: 4px 2px;">UART2_RXD</td>
      <td style="padding: 4px 2px;">UART1_RTS&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">CLK32K_OUT</td>
      <td style="padding: 4px 2px;">eSPI0_ALERT</td>
      <td style="padding: 4px 2px;">e/DP1_HPD</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[99]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[99]</td>
      <td style="padding: 4px 2px;">SSP3_TXD</td>
      <td style="padding: 4px 2px;">SSPA3_CLK</td>
      <td style="padding: 4px 2px;">UART4_TXD</td>
      <td style="padding: 4px 2px;">R.CAN2_TXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">CLK_CAMCK4</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[100]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[100]</td>
      <td style="padding: 4px 2px;">SSP3_RXD</td>
      <td style="padding: 4px 2px;">SSPA3_FRM</td>
      <td style="padding: 4px 2px;">UART4_RXD</td>
      <td style="padding: 4px 2px;">R.CAN2_RXD</td>
      <td style="padding: 4px 2px;">PCIeD_PRSNT2n</td>
      <td style="padding: 4px 2px;">CLK32K_OUT</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[101]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[101]</td>
      <td style="padding: 4px 2px;">SSP3_SCLK</td>
      <td style="padding: 4px 2px;">SSPA3_TXD</td>
      <td style="padding: 4px 2px;">UART4_CTS</td>
      <td style="padding: 4px 2px;">CAN4_RXD</td>
      <td style="padding: 4px 2px;">PCIeD_ATTn</td>
      <td style="padding: 4px 2px;">MNCLK_OUT1</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[102]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[102]</td>
      <td style="padding: 4px 2px;">SSP3_FRM</td>
      <td style="padding: 4px 2px;">SSPA3_RXD</td>
      <td style="padding: 4px 2px;">UART4_RTS</td>
      <td style="padding: 4px 2px;">CAN4_TXD</td>
      <td style="padding: 4px 2px;">PCIeD_PWRCTn</td>
      <td style="padding: 4px 2px;">I2C1_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[103]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[103]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">SSPA3_SYSCLK</td>
      <td style="padding: 4px 2px;">USB20_HOST_DRV</td>
      <td style="padding: 4px 2px;">CAN3_TXD</td>
      <td style="padding: 4px 2px;">PCIeD_AUXen</td>
      <td style="padding: 4px 2px;">I2C1_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[104]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[104]</td>
      <td style="padding: 4px 2px;">SSP0_TXD</td>
      <td style="padding: 4px 2px;">SSP2_TXD</td>
      <td style="padding: 4px 2px;">USB30H-1_DRV</td>
      <td style="padding: 4px 2px;">CAN3_RXD</td>
      <td style="padding: 4px 2px;">PCIeD_PWRDet</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[105]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[105]</td>
      <td style="padding: 4px 2px;">SSP0_RXD</td>
      <td style="padding: 4px 2px;">SSP2_RXD</td>
      <td style="padding: 4px 2px;">R.I2C1_SCL</td>
      <td style="padding: 4px 2px;">I2C3_SCL</td>
      <td style="padding: 4px 2px;">PCIeD_PERSTn</td>
      <td style="padding: 4px 2px;">PWM17</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[106]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[106]</td>
      <td style="padding: 4px 2px;">SSP0_SCLK</td>
      <td style="padding: 4px 2px;">SSP2_SCLK</td>
      <td style="padding: 4px 2px;">R.I2C1_SDA</td>
      <td style="padding: 4px 2px;">I2C3_SDA</td>
      <td style="padding: 4px 2px;">PCIeD_WAKEn</td>
      <td style="padding: 4px 2px;">PWM18</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[107]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[107]</td>
      <td style="padding: 4px 2px;">SSP0_FRM</td>
      <td style="padding: 4px 2px;">SSP2_FRM</td>
      <td style="padding: 4px 2px;">R.CAN4_TXD</td>
      <td style="padding: 4px 2px;">USB30_DRD_DIR</td>
      <td style="padding: 4px 2px;">PCIeD_CLKREQn</td>
      <td style="padding: 4px 2px;">PWM19</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[108]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[108]</td>
      <td style="padding: 4px 2px;">R.SSP1_TXD</td>
      <td style="padding: 4px 2px;">USB20_HOST_DRV</td>
      <td style="padding: 4px 2px;">R.CAN4_RXD</td>
      <td style="padding: 4px 2px;">IR0_RX</td>
      <td style="padding: 4px 2px;">PCIeA_PERSTn</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[109]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[109]</td>
      <td style="padding: 4px 2px;">R.SSP1_RXD</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.UART0_TXD</td>
      <td style="padding: 4px 2px;">CAN1_TXD</td>
      <td style="padding: 4px 2px;">PCIeA_WAKEn</td>
      <td style="padding: 4px 2px;">R.PWM6</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[110]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[110]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">R.UART0_RXD</td>
      <td style="padding: 4px 2px;">CAN1_RXD</td>
      <td style="padding: 4px 2px;">PCIeA_CLKREQn</td>
      <td style="padding: 4px 2px;">R.PWM7</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[111]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[111]</td>
      <td style="padding: 4px 2px;">SSP1_TXD</td>
      <td style="padding: 4px 2px;">SSPA0_CLK</td>
      <td style="padding: 4px 2px;">ucie_deSCL</td>
      <td style="padding: 4px 2px;">I2C4_SCL</td>
      <td style="padding: 4px 2px;">USB30_DRD_INT</td>
      <td style="padding: 4px 2px;">R.PWM8</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[112]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[112]</td>
      <td style="padding: 4px 2px;">SSP1_RXD</td>
      <td style="padding: 4px 2px;">SSPA0_FRM</td>
      <td style="padding: 4px 2px;">ucie_deSDA</td>
      <td style="padding: 4px 2px;">I2C4_SDA</td>
      <td style="padding: 4px 2px;">USB30_D_DRV</td>
      <td style="padding: 4px 2px;">R.PWM9</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[113]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[113]</td>
      <td style="padding: 4px 2px;">SSP1_SCLK</td>
      <td style="padding: 4px 2px;">SSPA0_TXD</td>
      <td style="padding: 4px 2px;">R.GPIO[30]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeB_PERSTn</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[114]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[114]</td>
      <td style="padding: 4px 2px;">SSP1_FRM</td>
      <td style="padding: 4px 2px;">SSPA0_RXD</td>
      <td style="padding: 4px 2px;">R.GPIO[31]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeB_WAKEn</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[115]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[115]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">SSPA0_SYSCLK</td>
      <td style="padding: 4px 2px;">R.GPIO[32]</td>
      <td style="padding: 4px 2px;">I2C0_SCL</td>
      <td style="padding: 4px 2px;">PCIeB_CLKREQn</td>
      <td style="padding: 4px 2px;">R.I2C0_SCL</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[116]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[116]</td>
      <td style="padding: 4px 2px;">R.SSP1_SCLK</td>
      <td style="padding: 4px 2px;">USB30_DRD_ID</td>
      <td style="padding: 4px 2px;">R.GPIO[33]</td>
      <td style="padding: 4px 2px;">I2C0_SDA</td>
      <td style="padding: 4px 2px;">PCIeB_PRSNT2n</td>
      <td style="padding: 4px 2px;">R.I2C0_SDA</td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[117]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[117]</td>
      <td style="padding: 4px 2px;">R.SSP1_FRM</td>
      <td style="padding: 4px 2px;">USB30_DRD_VBUSON</td>
      <td style="padding: 4px 2px;">R.GPIO[34]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeB_ATTn</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[118]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[118]</td>
      <td style="padding: 4px 2px;">UART1_RTSn&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">USB30_DRD_DRV</td>
      <td style="padding: 4px 2px;">R.GPIO[35]</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeB_PWRCTn</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[119]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[119]</td>
      <td style="padding: 4px 2px;">UART1_CTSn&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">USB30_DRD_INT</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeB_AUXen</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[120]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[120]</td>
      <td style="padding: 4px 2px;">UART1_RXD&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">I2C2_SCL</td>
      <td style="padding: 4px 2px;">R.CAN3_TXD</td>
      <td style="padding: 4px 2px;">CAN4_TXD</td>
      <td style="padding: 4px 2px;">PCIeB_PWRDet</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[121]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[121]</td>
      <td style="padding: 4px 2px;">UART1_TXD&lt;secure domain&gt;</td>
      <td style="padding: 4px 2px;">I2C2_SDA</td>
      <td style="padding: 4px 2px;">R.CAN3_RXD</td>
      <td style="padding: 4px 2px;">CAN4_RXD</td>
      <td style="padding: 4px 2px;">PCIeB_MRLn</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[122]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[122]</td>
      <td style="padding: 4px 2px;">MMC2_DAT[3]</td>
      <td style="padding: 4px 2px;">SSPA1_CLK</td>
      <td style="padding: 4px 2px;">UART6_TXD</td>
      <td style="padding: 4px 2px;">R.UART0_TXD</td>
      <td style="padding: 4px 2px;">PCIeB_ATNLED</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[123]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[123]</td>
      <td style="padding: 4px 2px;">MMC2_DAT[2]</td>
      <td style="padding: 4px 2px;">SSPA1_FRM</td>
      <td style="padding: 4px 2px;">UART6_RXD</td>
      <td style="padding: 4px 2px;">R.UART0_RXD</td>
      <td style="padding: 4px 2px;">PCIeB_PWRLED</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[124]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[124]</td>
      <td style="padding: 4px 2px;">MMC2_DAT[1]</td>
      <td style="padding: 4px 2px;">SSPA1_TXD</td>
      <td style="padding: 4px 2px;">PCIeD_PERSTn</td>
      <td style="padding: 4px 2px;">e/DP0_HPD</td>
      <td style="padding: 4px 2px;">PCIeB_EINT</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[125]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[125]</td>
      <td style="padding: 4px 2px;">MMC2_DAT[0]</td>
      <td style="padding: 4px 2px;">SSPA1_RXD</td>
      <td style="padding: 4px 2px;">PCIeD_WAKEn</td>
      <td style="padding: 4px 2px;">e/DP1_HPD</td>
      <td style="padding: 4px 2px;">PCIeB_EINTEG</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[126]</td>
      <td style="padding: 4px 2px;">UP</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[126]</td>
      <td style="padding: 4px 2px;">MMC2_CMD</td>
      <td style="padding: 4px 2px;">SSPA1_SYSCLK</td>
      <td style="padding: 4px 2px;">PCIeD_CLKREQn</td>
      <td style="padding: 4px 2px;">I2C5_SCL</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;"></td>
    </tr>
    <tr style="text-align: center;">
      <td style="padding: 4px 2px;">GPIO5 [1.8V/3.3V]</td>
      <td style="padding: 4px 2px;">GPIO_[127]</td>
      <td style="padding: 4px 2px;">DOWN</td>
      <td style="padding: 4px 2px;">enable</td>
      <td style="padding: 4px 2px;">GPIO[127]</td>
      <td style="padding: 4px 2px;">MMC2_CLK</td>
      <td style="padding: 4px 2px;"></td>
      <td style="padding: 4px 2px;">PCIeD_PRSNT2n</td>
      <td style="padding: 4px 2px;">I2C5_SDA</td>
      <td style="padding: 4px 2px;">USB30_C_DRV</td>
      <td style="padding: 4px 2px;"></td>
    </tr>
  </tbody>
</table>

## 5. Electrical Characteristics

### 5.1 Pin AC/DC Operating Conditions

The following table describes the recommended operating conditions.

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
    <col width="200">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Module</th>
      <th style="text-align: left;">Symbol/Pin</th>
      <th style="text-align: left;">Min</th>
      <th style="text-align: left;">Typ</th>
      <th style="text-align: left;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="text-align: left; font-weight: bold;">CPU</td><td style="text-align: left;">VDD08_X100</td><td style="text-align: left;">0.72V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">1.05V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDD08_M1A100</td><td style="text-align: left;">0.72V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PLL</td><td style="text-align: left;">AVDD08_PLL1</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_PLL234</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_PLL567</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PLL1</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PLL234</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PLL567</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PLL-DDR</td><td style="text-align: left;">AVDD08_PLL_DDR0</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_PLL_DDR1</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD1V8_PLL_DDR0</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD1V8_PLL_DDR1</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">CSI</td><td style="text-align: left;">AVDD08_CSI0</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_CSI1</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_CSI2</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_CSI0</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_CSI1</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_CSI2</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">DDR</td><td style="text-align: left;">VAA1V8_VDD2H_DDR</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDD2H_DDR</td><td style="text-align: left;">1.01V/1.045V (LP5/LP4x)</td><td style="text-align: left;">1.05V/1.1V (LP5/LP4x)</td><td style="text-align: left;">1.12V/1.155V (LP5/LP4x)</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: left;">0.47V/0.57V (LP5/LP4x)</td><td style="text-align: left;">0.5V/0.6V (LP5/LP4x)</td><td style="text-align: left;">0.57V/0.63V (LP5/LP4x)</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">DSI</td><td style="text-align: left;">AVDD08_DSI</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD12_DSI</td><td style="text-align: left;">1.14V</td><td style="text-align: left;">1.2V</td><td style="text-align: left;">1.32V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_DSI</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">EDP</td><td style="text-align: left;">AVDD18_EDP0</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">DVDD08_EDP0</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">EDP1</td><td style="text-align: left;">AVDD18_EDP1</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">DVDD08_EDP1</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">EMMC</td><td style="text-align: left;">AVDD08_EMMC</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_EMMC</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">FUSE</td><td style="text-align: left;">FUSE_AVDD18</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">GPIO</td><td style="text-align: left;">VCC18_GPIO1</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO2</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO3</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO4</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO5</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_PMIC</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO1</td><td style="text-align: left;">1.674V/2.97V</td><td style="text-align: left;">1.8V/3.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO2</td><td style="text-align: left;">1.674V/2.97V</td><td style="text-align: left;">1.8V/3.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO4</td><td style="text-align: left;">1.674V/2.97V</td><td style="text-align: left;">1.8V/3.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO5</td><td style="text-align: left;">1.674V/2.97V</td><td style="text-align: left;">1.8V/3.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_QSPI</td><td style="text-align: left;">1.674V/2.97V</td><td style="text-align: left;">1.8V/3.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_MMC1</td><td style="text-align: left;">1.674V/2.97V</td><td style="text-align: left;">1.8V/3.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">OSC</td><td style="text-align: left;">AVDD08_OSC</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_OSC</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY0</td><td style="text-align: left;">AVDD08_PCIeA</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeA</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY1</td><td style="text-align: left;">AVDD08_PCIeB</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeB</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY2</td><td style="text-align: left;">AVDD08_PCIeC/USB3-B</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeC/USB3-B</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY3</td><td style="text-align: left;">AVDD08_PCIeD/USB3-C</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeD/USB3-C</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY4</td><td style="text-align: left;">AVDD08_PCIeE/USB3-D</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeE/USB3-D</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY5</td><td style="text-align: left;">AVDD08_PCIe5</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIe5</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">UCIE</td><td style="text-align: left;">UCIE_VCCAON_0V8</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.84V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VCCIO_0V8</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.84V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VCCPLL_1P2V</td><td style="text-align: left;">1.116V</td><td style="text-align: left;">1.2V</td><td style="text-align: left;">1.236V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VDD_0V8</td><td style="text-align: left;">0.76V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.84V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VDDBH_0V9</td><td style="text-align: left;">0.855V</td><td style="text-align: left;">0.9V</td><td style="text-align: left;">0.945V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VDDVPH0_0V9</td><td style="text-align: left;">0.855V</td><td style="text-align: left;">0.9V</td><td style="text-align: left;">0.945V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">UFS</td><td style="text-align: left;">UFS_VCC_1V8</td><td style="text-align: left;">1.71V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UFS_VCCQ_1V2</td><td style="text-align: left;">1.14V</td><td style="text-align: left;">1.2V</td><td style="text-align: left;">1.32V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UFS_VDDU_0V8</td><td style="text-align: left;">0.76</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">USB2</td><td style="text-align: left;">AVDD08_B_USB20</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_C_USB20</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_D_USB20</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_USB20_Host</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_B_USB20</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_C_USB20</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_D_USB20</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_USB20_Host</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_B_USB20</td><td style="text-align: left;">3.069V</td><td style="text-align: left;">3.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_C_USB20</td><td style="text-align: left;">3.069V</td><td style="text-align: left;">3.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_D_USB20</td><td style="text-align: left;">3.069V</td><td style="text-align: left;">3.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_DRD_USB</td><td style="text-align: left;">3.069V</td><td style="text-align: left;">3.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_USB20_Host</td><td style="text-align: left;">3.069V</td><td style="text-align: left;">3.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">USB3-DRD</td><td style="text-align: left;">AVDD08_DRD_USB</td><td style="text-align: left;">0.744V</td><td style="text-align: left;">0.8V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_DRD_USB</td><td style="text-align: left;">1.674V</td><td style="text-align: left;">1.8V</td><td style="text-align: left;">1.98V</td></tr>
  </tbody>
</table>

### 5.2 Absolute Maximum DC Ratings

#### 5.2.1 For Pins

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Module</th>
      <th style="text-align: left;">Symbol/Pin</th>
      <th style="text-align: left;">Min</th>
      <th style="text-align: left;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="text-align: left; font-weight: bold;">CPU</td><td style="text-align: left;">VDD08_X100</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.05V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDD08_M1A100</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">Digital Power</td><td style="text-align: left;">VCC_M1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PLL</td><td style="text-align: left;">AVDD08_PLL1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_PLL234</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_PLL567</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PLL1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PLL234</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PLL567</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PLL-DDR</td><td style="text-align: left;">AVDD08_PLL_DDR0</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_PLL_DDR1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD1V8_PLL_DDR0</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD1V8_PLL_DDR1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">CSI</td><td style="text-align: left;">AVDD08_CSI0</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_CSI1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_CSI2</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_CSI0</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_CSI1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_CSI2</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">DDR</td><td style="text-align: left;">VAA1V8_VDD2H_DDR</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDD2H_DDR</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.12V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDDQ_DDR</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.57V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VDD0V8_DDR</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">DSI</td><td style="text-align: left;">AVDD08_DSI</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD12_DSI</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.32V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_DSI</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">EDP</td><td style="text-align: left;">AVDD18_EDP0</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">DVDD08_EDP0</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">EDP1</td><td style="text-align: left;">AVDD18_EDP1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">DVDD08_EDP1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">EMMC</td><td style="text-align: left;">AVDD08_EMMC</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_EMMC</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">FUSE</td><td style="text-align: left;">FUSE_AVDD18</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">GPIO</td><td style="text-align: left;">VCC18_GPIO1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO2</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO3</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO4</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_GPIO5</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC18_PMIC</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO2</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO4</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_GPIO5</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_QSPI</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">VCC1833_MMC1</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V/3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">OSC</td><td style="text-align: left;">AVDD08_OSC</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_OSC</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY0</td><td style="text-align: left;">AVDD08_PCIeA</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeA</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY1</td><td style="text-align: left;">AVDD08_PCIeB</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeB</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY2</td><td style="text-align: left;">AVDD08_PCIeC/USB3-B</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeC/USB3-B</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY3</td><td style="text-align: left;">AVDD08_PCIeD/USB3-C</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeD/USB3-C</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY4</td><td style="text-align: left;">AVDD08_PCIeE/USB3-D</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIeE/USB3-D</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">PICE PHY5</td><td style="text-align: left;">AVDD08_PCIe5</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_PCIe5</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">UCIE</td><td style="text-align: left;">UCIE_VCCAON_0V8</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.84V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VCCIO_0V8</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.84V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VCCPLL_1P2V</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.236V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VDD_0V8</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.84V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VDDBH_0V9</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.945V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UCIE_VDDVPH0_0V9</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.945V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">UFS</td><td style="text-align: left;">UFS_VCC_1V8</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.96V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UFS_VCCQ_1V2</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.32V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">UFS_VDDU_0V8</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">USB2</td><td style="text-align: left;">AVDD08_B_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_C_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_D_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD08_USB20_Host</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_B_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_C_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_D_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_USB20_Host</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_B_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_C_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_D_USB20</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_DRD_USB</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD33_USB20_Host</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">3.63V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;">USB3-DRD</td><td style="text-align: left;">AVDD08_DRD_USB</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">0.88V</td></tr>
    <tr><td style="text-align: left; font-weight: bold;"></td><td style="text-align: left;">AVDD18_DRD_USB</td><td style="text-align: left;">-0.3V</td><td style="text-align: left;">1.98V</td></tr>
  </tbody>
</table>

#### 5.2.2 For Packages

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 13px;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: left;">Item</th>
      <th style="text-align: left;">Symbol</th>
      <th style="text-align: left;">Min</th>
      <th style="text-align: left;">Max</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="text-align: left;">Operating Temperature (Industrial Standard)</td>
      <td style="text-align: left;">Ta</td>
      <td style="text-align: left;">-40°C</td>
      <td style="text-align: left;">85°C</td>
    </tr>
    <tr>
      <td style="text-align: left;">Junction Temperature</td>
      <td style="text-align: left;">Tj</td>
      <td style="text-align: left;">N/A</td>
      <td style="text-align: left;">125°C</td>
    </tr>
    <tr>
      <td style="text-align: left;">Storage Temperature</td>
      <td style="text-align: left;">Tstg</td>
      <td style="text-align: left;">-40°C</td>
      <td style="text-align: left;">125°C</td>
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
