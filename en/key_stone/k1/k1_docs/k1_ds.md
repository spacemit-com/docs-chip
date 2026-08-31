sidebar_position: 2

# K1 Datasheet

## PDF Version

Click to download **[K1 Datasheet (PDF)](https://cdn-resource.spacemit.com/file/chip/K1/K1_datasheet_en.pdf)**

## Revision History

| Version | Date       | Notes    |
|---------|------------|----------|
| V7.1    | 2026.08.31 | Removed Secure Boot feature from Section 1.2 |
| V7.0    | 2025.05.20 | Updated K1 architecture block diagram:<br>- DDR clock rate change<br>- RCPU modules change<br>Updated K1 general features:<br>- RCPU modules related |
| V6.0    | 2025.05.09 | Updated pinout                                                                                    |
| V5.1    | 2025.05.08 | Fixed typos in several sections                                                                   |
| V5.0    | 2025.04.28 | Edited PDF from on-line version                                                                   |
| V4.0    | 2025.04.16 | Removed the Audio Subsystem then performed related updates                                        |
| V3.0    | 2025.03.19 | Restructured and improved the quality of all content of the whole document                         |
| V2.0    | 2025.02.25 | Updated security algorithms, in particular removed SM2, SM3, SM4                                   |
| V1.6    | 2025.01.20 | Reviewed and updated the whole document for grammar, clarity and consistency                       |
| V1.5    | 2024.07.24 | Added V2D content                                                                                 |
| V1.4    | 2024.06.07 | Updated data                                                                                      |
| V1.3    | 2024.05.09 | Added supplementary packaging information                                                         |
| V1.2    | 2024.03.08 | Updated data                                                                                      |
| V1.1    | 2024.02.08 | Added supplementary packaging information                                                         |

## 1. Overview

### 1.1 Introduction

SpacemiT Key Stone® K1 is a high-performance and ultra-low-power SoC that integrates 8 RISC-V CPU cores with SpacemiT® Daoyi™ AI computing power. It comes with the following most relevant advantages:

- Integration with SpacemiT® self-innovated X60™ RISC-V core processor which adheres to the RISC-V 64GCVB architecture and RVA22 standard
- Capable of delivering 2.0 TOPS AI computing power by leveraging customized RISC-V instructions to enable CPU AI fusion computing
- Support for the popular AI inference frameworks such as TensorFlow Lite, TensorFlow, and ONNX Runtime
- Attainment of ultra-low power consumption through the incorporation of multiple granular power islands and dynamic power state adjustments, making K1 highly competitive in energy efficiency
- Availability of full-feature interfaces for enabling innovative applications and products
- Compatibility with mainstream OS to meet the needs of various application scenarios
- Compliance with the industrial-grade reliability standards

### 1.2 General Features

- Application Processor (AP)
  - SpacemiT® X60™ RISC-V Dual-Cluster 8-Core Processor
  - Adherence to the RISC-V 64GCVB architecture and RVA22 standard
  - Cluster 0
    - Quad-Core with 2.0 TOPS AI computing power
    - 32K L1-Cache per core
    - 512K L2-Cache
    - 512KB TCM
    - 256bit vector
  - Cluster 1
    - Quad-Core
    - 32K L1-Cache per core
    - 512K L2-Cache
    - 256bit vector
  - DVFS with adaptive operating voltage from 0.6V to 1.05V
- DDR Memory
  - Dual-Chip selection, 32-bit LPDDR4/LPDDR4x SDRAM with 2666 Mbps transfer rate, supporting up to 16 GB of RAM
  - Dual-Chip selection, 32-bit LPDDR3 SDRAM with 1866 Mbps transfer rate, supporting up to 4 GB of RAM
- RCPU (Real-Time CPU)
  - SRAM 256KB x1
  - R_CAN-FD x1
  - R_I2C x1
  - R_SPI x2
  - HDMI Audio
  - R_Debug
  - R_UART x2
  - R_PWM x10
  - DMA x1
  - R_IR_RX x1
- Peripheral Controller
  - GPIO (×128)
    - 128 pins
    - Pull-up/pull-down programmable
    - 104x 1.8V IO8
    - 24x 1.8V/3.3V IO
  - UART (×10)
    - AP/BT/print
  - I2C (×10)
    - For camera, G-Sensor, E-COMPASS, Proximity-Sensor, Light-Sensor, Gyro, Fingerprint, NFC, PMIC, Touch, etc.
    - 8x AP_I2C (AP I2C0/1/7 dedicated for camera) + 1x HDMI I2C + 1x PWR I2C
  - SPI (×4)
    - Support for both master and slave mode
    - For IMU, codec etc.
    - Platform with 4 SPI (1x QSPI, 1x SPI LCD, 2x SPI)
  - USB (×3)
    - USB 2.0 OTG
    - USB 2.0 Host
    - USB 3.0 (combo PCIE PortA)
  - PCIE (×3)
    - PCIE PortA Gen2x1
    - PCIE PortB Gen2x2
    - PCIE PortC Gen2x2
  - GMAC (×2)
    - 10/100/1000 Mbps
    - RGMII
  - SDIO (×1 for WIFI)
    - Compatible with 4-bit SDIO 3.0 UHS-I protocol, up to SDR104 (208MHz)
  - SD (×1 for TF card)
    - Compatible with 4-bit SD 3.0 UHS-I protocol, up to SDR104 (208MHz)
  - eMMC (×1)
    - Compatible with 8-bit eMMC 5.1, up to HS400 (200MHz)
  - MIPI CSI (CSI-2 v1.1) 4-Lane (×2)
    - 4-Lane + 4-Lane mode
    - 4-Lane + 2-Lane mode
    - 4-Lane + 2-Lane + 2-Lane mode (triple sensor)
  - MIPI DSI (DSI v1.1) (×1)
    - 4-Lane DSI
  - PWM (×20)
  - CAN-FD (×1)
  - IR-RX (×1)
- Security System
  - RISC-V PMP Security
  - Secure eFuse 4K bits
  - Cryptographic engine (TRNG, AES, RSA, ECC, SHA2, HMAC)
- Debug System
  - Two JTAGs for both CPU and MCU subsystem
  - UARTs
  - CPU/IO register snapshot after watchdog reboot
- Boot System
  - Initial AP boot from SPI-Nand/SPI-NorFlash/eMMC/SD
  - 128KB boot-ROM
- Aided System
  - Watchdog design for each CPU/MCU subsystem
- Operating Temperature
  - -40°C ~ +85°C (Industrial Standard)

### 1.3 Multimedia Features

- GPU
  - IMG BXE-2-32@819MHz, 32KB SLC
  - Support for OpenCL 3.0 / OpenGL ES 3.2 / Vulkan 1.3
- VPU (Video Processing Unit)
  - H.265/H.264/VP8/VP9/MPEG4/MPEG2 decoder 4K@60fps
  - H.265/H.264/VP8/VP9 encoder 4K@30fps
  - Support for simultaneous encoding and decoding at 1080P@60fps
  - Support for simultaneous H264/H265 encoding at 1080P@30fps and H264/H265 decoding at 4K@30fps
- Display
  - 1 MIPI DSI-4 lane or SPI interface
  - Support for up to HD+ (1920x1080@60fps)
  - Support for up to 4-full-size-layer composer and maximum 8-layer composer by up-down layer reuse in RDMA channel
  - Support for cmdlist mechanism which can configure register parameters by hardware
  - Support for concurrent write-back with both raw and AFBC format
  - Support for dither/crop/rotation in write-back path
  - Support for an advanced MMU (virtual address) mechanism with nearly no page missing in 90/270 degree rotation
  - Support for color key and solid color
  - Support for both advanced error diffusion and pattern based dither for panel
  - Support for both raw and AFBC format image source
  - Support for color saturation/contrast enhancement
  - Support for both video mode and cmd mode for panel
  - Support for DDR frequency dynamic changing with embedded DFC buffer
  - HDMI 1.4
- Camera
  - Dual-ISP
    - 16M (max) 30fps Dual ISP
    - One 4-Lane CSI + one 4-Lane CSI, or 4-Lane + 2-Lane + 2-Lane
    - RAW sensor, output YUV data to DRAM
    - Hardware JPEG encoder, supporting up to 23M
    - Support for YUV/EXIF/JFIF format
    - AF/AE/AWB
    - Face detection
    - Digital zoom, panorama view
    - PDAF
    - PiP (Picture-in-Picture)
    - Continuous video AF
    - HW 3D denoise
- Audio
  - 2 × Full-Duplex I2S Interfaces
  - 1 × HDMI Audio Interface

### 1.4 Block Diagram

The architecture of K1 is depicted below.  
![K1 Block Diagram](./static/k1_blockdiagram.png)

## 2. Specifications

### 2.1 CPU Subsystem

- Availability of two asymmetric CPU clusters, where

  - Cluster 0 includes Quad RISC-V SpacemiT® X60™ cores with 2.0 TOPS AI-Power extension
  - Cluster 1 includes Quad RISC-V SpacemiT® X60™ cores without AI capability
- High-performance: low-power SpacemiT® X60™ CPU core adheres to RISC-V 64GCVB architecture and RVA22 standard
- Support for a processor core local interrupt controller (CLINT) and a platform level interrupt controller (PLIC)
- Compliance with RISC-V debug V0.13.2 standard
- Capture of a snapshot of critical CPU information upon watchdog reset to aid debugging
- Power islands and two-level power strategies design for each CPU core and clusters in order to achieve ultra-low power consumption

#### SpacemiT® X60™ RISC-V Core

##### Introduction

X60™ is an innovative high-efficiency processor core with SpacemiT® Daoyi™ AI innovation deployment that adheres to RISC-V 64GCVB and RVA22 standards.

In order to meet the current and future computational demand, X60™ incorporates numerous DSA technologies and micro-architecture optimizations, and provides robust computing power for AI applications, machine learning, SLAM, etc.

##### Features

- Compliance with RISC-V 64GCVB and RVA22 standards
- Each core has 32KB L1-I cache and 32KB L1-D cache
- Each cluster contains 512KB L2 cache
- Cluster 0 integrates 512KB TCM (Tight-Coupled Memory) for AI extension
- L1 cache supports MESI consistency protocol, instead L2 cache supports MOESI consistency protocol
- Vector extension: RVV1.0 with VLEN 256/128-bit and x2 execution width
- AI customized instructions explored and implemented in Cluster 0
- Support for CLINT and PLIC with a total of 256 interrupts
- Support for RISC-V performance PMU
- Support for SV39 virtual memory
- Support for 32 PMP entries adhering to RISC-V security framework
- Support for RISC-V debug framework
- Support for the following extensions:

  - RV64I
  - M
  - A
  - F
  - D
  - C
  - V
  - Sscofpmf
  - Sstc
  - Svinval
  - Svnapot
  - Svpbmt
  - Zicbom
  - Zicbop
  - Zicboz
  - Zicntr
  - Zicond
  - Zicsr
  - Zifencei
  - Zihintpause
  - Zihpm
  - Zfh
  - Zfhmin
  - Zkt
  - Zba
  - Zbb
  - Zbc
  - Zbs
  - Zbkc
  - Zvfh
  - Zvfhmin
  - Zvkt
- Support for the following AI customized instructions:

  - Category "<u>Integer dot-product matrix multiply-accumulate (int8 type)</u>", including
    - smt.vmadot
    - smt.vmadotu
    - smt.vmadotsu
    - smt.vmadotus
  - Category "<u>Integer sliding-window dot-product matrix multiply-accumulate (int8 type)</u>", including
    - smt.vmadot1
    - smt.vmadot1u
    - smt.vmadot1su
    - smt.vmadot1us
    - smt.vmadot2
    - smt.vmadot2u
    - smt.vmadot2su
    - smt.vmadot2us
    - smt.vmadot3
    - smt.vmadot3u
    - smt.vmadot3su
    - smt.vmadot3us

  **Note.** For details on all these AI-customized instructions, please refer to [https://github.com/spacemit-com/riscv-ime-extension-spec](https://github.com/spacemit-com/riscv-ime-extension-spec)

##### Block Diagram

The micro-architecture of X60™ is depicted below.

![](static/X60.png)

#### Interrupt Controller

##### Introduction

K1 contains

- One Processor Core Local Interrupt Controller (CLINT)
- One Platform Level Interrupt Controller (PLIC)

to manage interrupts for two processor clusters.

The exception handling, which includes exceptions and external interrupts, is an important function of the processor. When specific events occur, the processor redirects to handle them. Such events can include hardware faults, instruction execution errors, user program service requests, and more.

CLINT is a memory address mapped module for handling software interrupts and timer interrupts.

Instead, PLIC samples external interrupt sources, then prioritizes and distributes them accordingly. In the PLIC model, both the machine mode and supervisor mode of each core are valid interrupt targets. PLIC supports up to 256 external interrupt sources. Each interrupt supports both level and edge formats.

#### Debug & Trace

##### Introduction

The debugging interface serves as the channel for software to interact with the processor. Through this interface, users can access CPU registers and memory contents, as well as other on-chip device information. Additionally, tasks such as downloading programs can be performed via the debugging interface.

##### Block Diagram

The micro-architecture of the debugging interface is depicted below.

<img src="static/debugging_interface.png" alt="" width="600">

As can be seen, the debugging system consists of

- A debugging software
- A debugging agent service
- A debugger
- A debugging interface

These components are interconnected as follows:

- The debugging software communicates with the debugging agent service over a network
- The debugging agent service connects to the debugger via USB
- The debugger interacts with the CPU through the JTAG interface

The JTAG memory access method could be either _progbuf_ or _sysbus_ mode, where

- The _progbuf_ mode is a standard JTAG method that accesses memory through the CPU
- The _sysbus_ mode bypasses the CPU to access on-chip resources via the System Bus Access (SBA) port

### 2.2 Memory & Storage

#### On-Chip Memory

##### Introduction

K1 includes the following on-chip memory:

- 128KB boot-ROM
- 256KB SRAM shared between Main CPU and RCPU

#### DDR

##### Introduction

The DDR controller features a cutting-edge design that optimizes DRAM access by rearranging requests into an efficient order, rather than processing them in their original sequence. It uses re-ordering buffers (ROBs) to reorganize accesses to the SRAM device for improving performance, while maintaining the original transaction order for requests with the same ID on the AXI interface.

Additionally, the DDR controller includes a unified write pool to temporarily store write transactions. Such write pool minimizes write latency and reduces the performance penalty due to switching between read and write operation at the DRAM interface. With a built-in heuristic write buffer control and user-programmable write buffer control, the DDR controller dynamically balances read and write operation performance in real-time.

The DDR controller is also designed to support AMBA AXI4 bus protocols. It is fully scalable and supports up to 4 AXI ports.

##### Features

- Priority-based arbitration with a starvation prevention scheme
- Merge of write operations to the same address by using a write buffer to reduce DDR write operation traffic
- Direct forward of read operations of the write buffer to the ROB without accessing DDR
- Two levels dynamic scheduling with bandwidth guarantee
- Support of power-saving features, including active/pre-charge power-off and self-refresh, with control options available automatically (via idle timer), manually (through registers) or externally (via dedicated ports)
- Support for dynamic frequency change
- Support for JEDEC compliant LPDDR3 and LPDDR4 devices
- Support for DRAM size from 64MB to 16GB
- One DRAM channel with a x32 DDR PHY, programmable by software to support x32, x16 or x8 data width
- Support for x16, x32 DRAM devices (1 DQS per 8 DQ)
- Support for up to 2 Chip Select (CS) or Rank per channel
- Support for up to 8 banks per CS for LPDDRx
- Each CS can be mapped to a different starting address
- Each CS can be programmed for 8MB to 16GB
- DRAM banks can be kept open after access (no auto-pre-charge)
- Support for burst length of 8 and 16 for the applicable DDR type
- Programmable address order
- Flexible bank placement between CS and data width
- Implementation of memory controller performance counters
- Global monitors for RISC-V exclusive load/store access
- Secure access management for DDR transactions
- Frequency change register update: implementation of a register table for hardware-triggered sequence update after frequency changes

##### Block Diagram

The architecture of the DDR controller interface is depicted below.

<img src="static/DDR_controller.png" alt="" width="600">

#### Quad-SPI

##### Introduction

Quad-SPI acts as an interface to external serial flash devices with up to four bidirectional data lines.

##### Features

- Flexible sequence engine to support various flash vendor devices
- Single, dual and quad mode operation
- DMA supports reading RX buffer data via AMBA AHB bus (64-bit width interface) or IP register space (32-bit access), and filling TX buffer via IP register space (32-bit access)
- Configurable DMA inner loop size
- Fifteen interrupt conditions
- Memory-mapped read access for connected flash devices
- Programmable sequence engine for future command/protocol changes, and able to support all existing vendor commands and operations
- Support for all types of addressing
- Support for standard SPI, Fast, Dual, Dual I/O, Quad, Quad I/O mode
- Operation up to 104MHz clock frequency

#### eMMC Interface

##### Introduction

The eMMC interface is a hardware block that acts as a host of the eMMC bus to transfer data between eMMC card and the internal bus master.

##### Features

- Compliance with the 8 bits eMMC 5.1 protocol specification
- Use of the same SD-HCI register set for eMMC transfers, with additional vendor-specific registers
- Support for 1-bit/8-bit MMC and CE-ATA cards
- Support for the following data transfer types defined in the SD-HCI specification:

  - PIO
  - SDMA
  - ADMA
  - ADMA2
- Support for the SPI mode for eMMC card
- Support for the following speed modes defined in eMMC 5.1:

  - Legacy (up to 26MB/s, 1.8V signal)
  - High-speed SDR (up to 52MB/s, 1.8V signal)
  - High-speed DDR (up to 52MB/s, 1.8V signal)
  - HS200 (up to 200MB/s, 1.8V signal)
  - HS400 (up to 400MB/s, 1.8V signal)
- Hardware generation/checking of CRC for all command and data transactions on the card bus
- 1024-byte FIFO (2 x 512-byte data blocks) for data transmission and reception

#### SD/MMC Interface

##### Introduction

The SD/MMC interface is a hardware block that acts as a host of the SD/MMC bus to transfer data between SD/MMC card and the internal bus master.

##### Features

- Compliance with the 4-bit SD 3.0 UHS-I protocol specification
- Adoption of the SD-HCI register set with additional vendor-specific registers
- Support for 1-bit/4-bit SD memory
- Support for the following data transfer types defined in the SD-HCI specification:

  - PIO
  - SDMA
  - ADMA
  - ADMA2
- Support for the following speed modes defined in the SD 3.0 specification:

  - Default Speed (up to 12.5MB/s, 3.3V signal)
  - High Speed (up to 25MB/s, 3.3V signal)
  - SDR12 (up to 25 MHz, 1.8V signal)
  - SDR25 (up to 50 MHz, 1.8V signal)
  - SDR50 (up to 100 MHz, 1.8V signal)
  - SDR104 (up to 208 MHz, 1.8V signal)
  - DDR50 (up to 50 MHz, 1.8V signal)
- Hardware generation/checking of CRC for all command and data transactions on the card bus
- Support for the read-wait control feature for SD/MMC cards
- Support for the suspend-resume feature for SD/MMC cards
- SD/MMC card insertion/removal detection feature via GPIO
- 1024 Bytes FIFO (2 x 512 Bytes data block) for data transmission and reception

### 2.3 Image Subsystem

#### MIPI Camera IN Interface

##### Introduction

The MIPI Camera IN interface features two MIPI-CSI2 v1.1 controllers both equipped with 4 lanes each of which supports a maximum transfer rate of 1.5Gbps.

##### Features

- Support for the following modes to allocate lanes to sensors:

  - 4-Lane + 4-Lane mode (double sensor)
  - 4-Lane + 2-Lane mode (double sensor)
  - 4-Lane + 2-Lane + 2-Lane mode (triple sensor)

  > **Note.** In "4-Lane + 2-Lane + 2-Lane mode (triple sensor)", only 2 Bayer RAW and 1 YUV input format are supported.
  >
- Support for the following input formats:

  - Legacy YUV420 8-bit
  - YUV420 8-bit
  - RAW8
  - RAW10
  - RAW12
  - RAW14
  - Embedded data type
- Support for the following types of data interleaving:

  - Data type interleaving
  - Virtual channel interleaving

#### ISP

##### Introduction

K1 includes a high-performance Image Signal Processor (ISP) which supports simultaneous processing of up to two raw video streams, with a total processing capacity of 21M@30fps.

##### Features

- Support for both video and picture mode
- Processing of RAW sensor data and output of YUV data to DRAM
- Hardware JPEG encoder/decoder (support for up to 23M)
- Support for YUV, EXIF, JFIF format
- Auto-focus (AF), Auto-exposure (AE) and Auto-white balance (AWB)
- Face detection
- Digital zoom and panorama view
- Phase Detection Auto-focus (PDAF)
- Picture-in-Picture (PiP)
- Continuous video AF
- Hardware 3D denoise
- Multi-layer 2D YUV denoise
- Post-processing for lens shading correction
- Edge enhancement

> **Notes.** To be highlighted the following limitations:
>
> - The system supports dual-camera video stream processing (RAW). In the “4-Lane + 2-Lane + 2-Lane mode (triple sensor)” as per **[MIPI Camera IN Interface](#mipi-camera-in-interface)**, one sensor must be a YUV input format source, and the write path should not use the MMU.
> - When processing dual-camera video stream (RAW), the total input width of each channel should not exceed 4750 pixels. The combination of the instantaneous speed of the output pixel from both sensors must be less than "_ISP's clock / 6_"
> - For video recording, the maximum width of the output video is 1920 pixels, regardless of the input resolution.
> - For photo capture, the output image size can match the input resolution.

#### GPU

##### Introduction

GPU is built around multi-threaded Unified Shading Clusters (USCs) that features an ALU architecture with high SIMD efficiency, and supports tile-based deferred rendering with concurrent processing of multiple tiles.

The GPU engine handles a number of different workloads, including:

- 3D graphics workload: vertex and pixel data processing for rendering 3D scenes
- Compute workload (GP-GPU): general purpose data processing

> **Note.** 3D graphics and compute (with barriers) workloads cannot be overlapped at the same time

The GPU core has an AXI 128bits bus for accessing SOC's DDR memory with a core frequency of up to 819MHz.

##### General Features

- Base architecture which is fully compliant with the following APIs:

  - OpenGL ES 1.1/3.2
  - EGL1.5
  - OpenCL 3.0
  - Vulkan 1.3
- Tile-based deferred rendering architecture (TBDR) for 3D graphics workloads, with concurrent processing of multiple tiles where data are processed in two phases as follows:

  - Geometry Processing Phase: involvement of vertex operations such as transformation and vertex lighting as well as dividing a 3D scene into tiles
  - Fragment Processing Phase: involvement of pixel operations such as rasterization, texturing and shading of pixels
- Programmable high quality image anti-aliasing
- Fine grain triangle culling
- Support for Digital Right Management (DRM) security
- Support for GPU virtualization as follows:

  - Up to 8 virtual GPUs
  - IMG hyperlane technology with 8 hyperlanes available
  - Separate IRQs per OSI
- Multi-threaded Unified Shading Cluster (USC) engine incorporating pixel shader, vertex shader and GP-GPU (compute shader) functionality
- USC incorporates an ALU architecture with high SIMD efficiency
- Fully virtualized memory addressing (up to 64 GB address space), supporting unified memory architecture
- Fine-grained task switching, workload balancing and power management
- Advanced DMA driven operation for minimum host CPU interaction
- Cache type as follows:

  - 32KB System Level Cache (SLC)
  - Specialized Texture Cache Unit (TCU)
- Compressed Texture Decoding
- Lossless and/or visually lossless low area image compression, using imagination frame buffer compression and decompression (TFBC) algorithm
- Dedicated processor for B-Series core firmware execution
- Single-threaded firmware processor with a 2KB instruction cache and a 2KB data cache
- Separated power island for the firmware processor
- On-chip performance, power and statistics registers

##### 3D Graphics Features

- **Rasterization**

  - Deferred pixel shading
  - On-chip tile floating point depth buffer
  - 8-bit stencil with on-chip tile stencil buffer
  - Maximum 2 tiles in flight (per ISP)
  - 16 parallel depth/stencil tests per clock
  - 1 fixed-function rasterisation pipeline(s)

- **Texture Lookups**

  - Support for loading from source instruction
  - Texture write enabled through the Texture Processing Unit (TPU)

- **Filtering**

  - Point, bilinear and trilinear filtering
  - Anisotropic filtering
  - Corner filtering support for cube environment mapped textures and filtering across faces

- **Texture Formats**

  - ASTC LDR compressed texture format support
  - TFBC lossless and/or lossy compression format support for non-compressed textures and YUV textures
  - ETC
  - YUV planar support

- **Resolution Support**

  - Max frame buffer size: 8K×8K
  - Max texture max size: 8K×8K

- **Anti-Aliasing**

  - Max 4× multisampling

- **Primitive Assembly**

  - Early hidden object removal
  - Tile acceleration

- **Render to Buffers**

  - Twiddled format support
  - Multiple On-Chip Render Targets (MRT)
  - Lossless and/or lossy frame buffer compression/decompression
  - Programmable geometry shader support
  - Direct geometry stream out (transform feedback)

- **Compute**

  - 1, 2 and 3 dimensional compute primitives
  - Block DMA to/from USC Common Store (for local data)
  - Per task input data DMA (to USC Unified Store)
  - Conditional execution
  - Execution fences
  - Compute workload can be overlapped with any other workload
  - Round to nearest even

##### Unified Shading Cluster (USC) Features**

- 2 ALU pipelines
- 8 parallel instances per clock
- Local data, texture and instruction caches
- Variable length instruction set encoding
- Full support for OpenCL™ atomic operations
- Scalar and vector SIMD execution model
- USC F16 Sum-of-Products Multiply-Add (SOPMAD) Arithmetic Logic Unit (ALU)

#### V2D

##### Features

- Support for upscaling (up to 8x) and downscaling (down to 1/8x)
- Support for 0°, 90°, 180°, 270° rotation as well as mirror and flip option
- Support for simple layer and background blending
- Support for image cropping
- Support for fetch solid color
- Support for color space conversion between RGB, BT601 and BT709 (both narrow and full range)
- 4656x3596 or 4672x3504 as max NV12 resolution
- Support for dithering for smoother color transitions
- Support for MMU
- Support for APB3 and AXI3 bus interfaces
- Support for the following **input formats**:

  - RGB888 (with optional RB swap)
  - RGBX888 (with optional RB swap)
  - RGBA8888 (with optional RB swap)
  - ARGB8888 (with optional RB swap)
  - RGB565 (with optional RB swap)
  - RGBA5658 (with optional RB swap)
  - ARGB8565 (with optional RB swap)
  - A8 (8-bit alpha image)
  - Y8 (8-bit gray image)
  - YUV420 semi-planar (UV can swap)
  - AFBC 16x16 RGBA8888 (layerout0 split and non-split)
  - AFBC 16x16 NV12 (layerout1 split and non-split)
- Support for the following **output formats**:

  - RGB888 (with optional RB swap)
  - RGBX888 (with optional RB swap)
  - RGBA8888 (with optional RB swap)
  - ARGB8888 (with optional RB swap)
  - RGB565 (with optional RB swap)
  - RGBA5658 (with optional RB swap)
  - ARGB8565 (with optional RB swap)
  - A8 (8-bit alpha image)
  - Y8 (8-bit gray image)
  - YUV420 semi planar (UV can swap)
  - AFBC 16x16 RGBA8888 (layerout0 split and non-split)
  - AFBC 16x16 NV12 (layerout1 split and non-split)

##### Block Diagram

The micro-architecture of the V2D subsystem is depicted below.

<img src="static/V2D_subsystem.png" alt="" width="600">

Instead, the typical V2D work scenario is depicted below.

<img src="static/V2D_work_scenario.png" alt="" width="400">

##### Functions

###### Fetch Data

The process of fetching a 16×16 block of data from a source frame (src frame) and related mapping to the destination superblock (dst superblock) is depicted below, where

- **AFBC**: fetch rect left, top, width, height 4 align
- **Non-AFBC**: fetch rect left, top, width, height 1 align

<img src="static/Fetch_Data.png" alt="" width="400">

The code for fetching data for displaying is listed below, and the details of the specific variables and registers involved are tabled immediately after.

```
Input param: Rect_left, Rect_top, Rect_width, Rect_height
Rect_width = Rect_left%4 + Rect_width;
Rect_height = Rect_top%4 + Rect_height;
Rect_left = Rect_left/4 × 4;
Rect_top = Rect_top/4 × 4;
if LayerX_format == YUV420 
{
    Rect_width  = ALIGN(Rect_left %2 + Rect_width, 2);
    Rect_height   = ALIGN(Rect_top%2 + Rect_height, 2);
    Rect_left = Rect_left/2 × 2;
    Rect_top = Rect_top/2 × 2;
}
Take the data in the Rect
Loop every pixel in Rect
{
    if LayerX_format == YUV420
    {
        upsample YUV420 to YUV444;
        c0 = channel 0; // Y
        c1 = channel 1; // U
        c2 = channel 2; // V
        c3 = 0xff;
    }
    if LayerX_format == RGB888
    {
        c0 = channel 0; // R
        c1 = channel 1; // G
        c2 = channel 2; // B
        c3 = 0xff; // A
    }
    if LayerX_format == RGBX8888
    {
        c0 = channel 0; // R
        c1 = channel 1; // G
        c2 = channel 2; // B
        c3 = 0xff; // A
    }
    if LayerX_format == RGBA8888
    {
        c0 = channel 0; // R
        c1 = channel 1; // G
        c2 = channel 2; // B
        c3 = channel 3; // A
    }
    if LayerX_format == ARGB8888
    {
        c0 = channel 1; // R
        c1 = channel 2; // G
        c2 = channel 3; // B
        c3 = channel 0; // A
    }
    if LayerX_format == RGB565
    {
        c0 = byte_low &0x1f; // R5
        c1 = ((byte_high << 3) | (byte_low >> 5)) & 0x3f; // G6
        c2 = (byte_high >> 3) &0x1f; // B5
        c0 = (c0 << 3) | (c0 >> 2); // R8
        c1 = (c1 << 2) | (c1 >> 4); // G8
        c2 = (c2 << 3) | (c2 >> 2); // B8
        c3 = 0xff; // A8
    }
    if LayerX_format == YUV420 && LayerX_swap == 1
        Swap(c1, c2);
    else if LayerX_swap == 1
        Swap(c0, c2);
    Index = Rect_y%16 × 16 + Rect_x;
    data[0][index] = c0;
    data[1][index] = c1;
    data[2][index] = c2;
    data[3][index] = c3;
}
```

| Variable           | Bit                    | Comment        |
|--------------------|------------------------|--------------------------|
| Rect_left<br/>Rect_top          | 16bit unsigned         | Range [0, 65535]                                                        |
| Rect_width<br/>Rect_height      | 5bit unsigned          | Range [1, 16]                                                           |
| Rect_x<br/>Rect_y               | 16bit unsigned         | Range [0, 65535]<br/>Pixel global position                              |
| c0, c1, c2, c3                  | 8bit unsigned          | Range [0, 255]                                                          |
| byte_low<br/>byte_high          | 8bit unsigned          | Range [0, 255]<br/>byte_low: lower byte in RGB565<br/>byte_high: higher byte in RGB565 |
| data[4][256]                    | 8bit unsigned × 4 × 256 | Range [0, 255]                                                          |
| index                           | 8bit unsigned          | Range [0, 255]                                                          |

| Register        | Comment                              |
|-----------------|--------------------------------------|
| LayerX_format   | X is either 0 or 1, refer to module register |
| LayerX_swap     | X is either 0 or 1, refer to module register |

###### Solid Color

The code for applying the solid color within a specific rectangle is listed below, and the details of the specific variables and registers involved are tabled immediately after.

> **Notes.**
>
> - If the register `LayerX_solid` is enabled, the fetched data is set to solid R, G, B, A
> - The coordinates of the fetch rect and solid rect are updated after rotation

```sql
Input param: Rect_left, Rect_top, Rect_width, Rect_height.
if LayerX_solid_enable = 1
{
    c0 = LayerX_solid_R;
    c1 = LayerX_solid_G;
    c2 = LayerX_solid_B;
    c3 = LayerX_solid_A;
    Loop all pixels in Rect
    {
        Index = Rect_y%16 × 16 + Rect_x;
        data[0][index] = c0;
        data[1][index] = c1;
        data[2][index] = c2;
        data[3][index] = c3;
    }
    Skip fetch data from ddr
}
```

| Variable           | Bit                    | Comment                     |
|--------------------|------------------------|-----------------------------|
| Rect_left, Rect_top          | 16bit unsigned         | Range [0, 65535]            |
| Rect_width, Rect_height      | 5bit unsigned          | Range [1, 16]               |
| Rect_x, Rect_y               | 16bit unsigned         | Range [0, 65535]<br/>Pixel global position |
| c0, c1, c2, c3               | 8bit unsigned          | Range [0, 255]              |
| data[4][256]                 | 8bit unsigned × 4 × 256 | Range [0, 255]              |
| index                        | 8bit unsigned          | Range [0, 255]              |

| Register               | Comment                            |
|------------------------|------------------------------------|
| LayerX_solid_enable    | X is 0 or 1, refer to module register |
| LayerX_solid_R         | X is 0 or 1, refer to module register |
| LayerX_solid_G         | X is 0 or 1, refer to module register |
| LayerX_solid_B         | X is 0 or 1, refer to module register |
| LayerX_solid_A         | X is 0 or 1, refer to module register |
###### Rotation

Support for 0°, 90°, 180°, 270° rotation (performed clockwise) as well as mirror and flip option, as depicted below (example).

<img src="static/Rotation.png" alt="" width="200">

The code for rotating, mirroring and flipping graphical content is listed below, and the details of the specific variables and registers involved are tabled immediately after.

```sql
Input param: Rect_left, Rect_top, Rect_width, Rect_height, data_in[4][256].
Output: Block_rect_left, Block_rect_top,  Block_rect_width,  Block_rect_height, data_out[4][256].
Block_rect_left = Rect_left;
Block_rect_top = Rect_top;
Block_rect_width = Rect_width;
Block_rect_height = Rect_height;
if LayerX_degree == ROT_0{
    Org_rect_left = Rect_left;
    Org_rect_top = Rect_top;
    Org_rect_width = Rect_width;
    Org_rect_height = Rect_height;
}
if LayerX_degree == ROT_90{
    Org_rect_left = Rect_top;
    Org_rect_top = ALIGN(LayerX_height,16) - Rect_left - Rect_width;
    Org_rect_width = Rect_height;
    Org_rect_height = Rect_width;
} 
if LayerX_degree == ROT_180{
    Org_rect_left = ALIGN(LayerX_width,16) - Rect_left - Rect_width;
    Org_rect_top = ALIGN(LayerX_height,16) - Rect_top - Rect_height;
    Org_rect_width = Rect_width;
    Org_rect_height = Rect_height;
}
if LayerX_degree == ROT_270{
    Org_rect_left = ALIGN(LayerX_width,16)-Rect_top-Rect_height;
    Org_rect_top = Rect_left;
    Org_rect_width = Rect_height;
    Org_rect_height = Rect_width;
}
if LayerX_degree == ROT_MIRROR{
    Org_rect_left = ALIGN(LayerX_width,16) - Rect_left - Rect_width;
    Org_rect_top = Rect_top;
    Org_rect_width = Rect_width;
    Org_rect_height = Rect_height;
}
if LayerX_degree == ROT_FLIP{
    Org_rect_left = Rect_left;
    Org_rect_top = ALIGN(LayerX_height,16) - Rect_top - Rect_height;
    Org_rect_width = Rect_width;
    Org_rect_height = Rect_height;
}
//fetch data in Org_rect
Fetch_data(Org_rect, &data_in[4][256]);
Loop all pixels in data_in{
    dst_index=jx16 + i;
    if LayerX_degree == ROT_0
        src_index=jx16 + i;
    if LayerX_degree == ROT_90
        src_index=(15-i)x16 + j;
    if LayerX_degree == ROT_180
        src_index=(15-j)x16 + (15-i);
    if LayerX_degree == ROT_270
        src_index= ix16+(15-j);
    if LayerX_degree == ROT_MIRROR
        src_index = jx16 + (15-i);
    if LayerX_degree == ROT_FLIP
        src_index = (15-j)x16 + i;
    data_out[0][dst_index]= data_in[0][src_index];
    data_out[1][dst_index]= data_in[1][src_index];
    data_out[2][dst_index]= data_in[2][src_index];
    data_out[3][dst_index]= data_in[3][src_index];
}
```

| Variable                              | Bit                    | Comment          |
|---------------------------------------|------------------------|------------------|
| Rect_left, Rect_top                   | 16bit unsigned         | Range [0, 65535] |
| Rect_width, Rect_height               | 5bit unsigned          | Range [1, 16]    |
| Block_rect_left, Block_rect_top       | 16bit unsigned         | Range [0, 65535] |
| Block_rect_width, Block_rect_height   | 5bit unsigned          | Range [1, 16]    |
| data_in[4][256],<br/>data_out[4][256] | 8bit unsigned × 4 × 256 | Range [0, 255]   |

| Register                    | Bit             | Comment                            |
|-----------------------------|-----------------|------------------------------------|
| LayerX_degree               | 3bit unsigned   | X is 0 or 1, refer to module register |
| LayerX_width, LayerX_height | 16bit unsigned  | X is 0 or 1, refer to module register |

###### CSC

Support for Color Space Conversion (CSC) as per formats below:

- BT601 and BT709: conversion between narrow and full range
- RGB to YUV
- YUV to RGB

The conversion process transforms input channels into output channels by using a transformation matrix with clamping in order to ensure valid output values, i.e. within the range [0, 255].

For that purpose, the formulas below are implemented, and the details of the specific variables and registers involved are tabled immediately after.

**[Firstly for computing the intermediate channel values]**

$$
C0_{inter} = (Layer_matrix[0][0]*C0_{in} + Layer_matrix[0][1]*C1_{in} + Layer_matrix[0][2]*C2_{in} + 512)>>(10+Layer_matrix[0][3])
$$

$$
C1_{inter} = (Layer_matrix[1][0]*C0_{in} + Layer_matrix[1][1]*C1_{in} + Layer_matrix[1][2]*C2_{in} + 512)>>(10+Layer_matrix[1][3])
$$

$$
C2_{inter} = (Layer_matrix[2][0]*C0_{in} + Layer_matrix[2][1]*C1_{in} + Layer_matrix[2][2]*C2_{in} + 512)>>(10+Layer_matrix[2][3])
$$

**[Then for clamping in order to ensure valid output values]**

$$
C0_{out}=clamp(C0_{inter},0,255)
$$

$$
C1_{out}=clamp(C1_{inter},0,255)
$$

$$
C2_{out}=clamp(C2_{inter},0,255)
$$

$$
C3_{out}=clamp(C3_{in},0,255)
$$

| Variable                     | Bit            | Comment                   |
|------------------------------|----------------|---------------------------|
| C0in, C1in, C2in, C3in       | 8bit unsigned  | Input channel             |
| C0inter, C1inter, C2inter    | 10bit signed   | Intermediate channel value|
| C0out, C1out, C2out, C3out   | 8bit unsigned  | Output channel            |

| Register               | Index | Bit           | Comment              |
|------------------------|-------|---------------|----------------------|
| LayerX_CSC_enable      | -     | 1bit unsigned | 0: disable<br/>1: enable |
| Layer_matrix[#][#]     | 0-11  | 13bit signed  | Range [-4096, 4095]  |

In the code, the conversion process is applied with the following condition:

```
if LayerX_CSC_enable == 0
    skip CSC function
```

###### Scaling

The scaling operation follows a systematic superblock-based approach, where

- The first four superblocks are outputted horizontally then vertically
- After the vertical output is completed, the process restarts from the first row of superblocks

###### Storing

A 16×16 image block can be stored in DDR memory, however only the portion that falls within the output crop region is stored which is converted to the specified output color format, such as YUV, RGB, etc.

The code for storing an image block is listed below, and the details of the specific variables and registers involved are tabled immediately after.

```sql
Input param: Rect_left, Rect_top, Rect_width, Rect_height, data_in[4][256]
if output_format == YUV420
{
    s0=0;
    s1=1;
    s2=2;
    if(output_swap){
        Swap(s1, s2);
    }
    Loop all pixels by 2x2{
        if(pixel in output_crop_rect){
            Y00=data_in[s0][pixel_index00];
            Y01=data_in[s0][pixel_index01];
            Y10=data_in[s0][pixel_index10];
            Y11=data_in[s0][pixel_index11];
            U00=data_in[s1][pixel_index00];
            U01=data_in[s1][pixel_index01];
            U10=data_in[s1][pixel_index10];
            U11=data_in[s1][pixel_index11];
            V00=data_in[s2][pixel_index00];
            V01=data_in[s2][pixel_index01];
            V10=data_in[s2][pixel_index10];
            V11=data_in[s2][pixel_index11];
            Downsample and store to output frame
            U=(U00+U01+U10+U11+2)>>2;
            V=(V00+V01+V10+V11+2)>>2;
        }
    }
}
if output_format == RGB888 
{
    s0=0;
    s1=1;
    s2=2;
    if(output_swap){
        Swap(s0, s2);
    }
    Loop all pixels{
        if(pixel in output_crop_rect){
            R=data_in[s0][pixel_index];
            G=data_in[s1][pixel_index];
            B=data_in[s2][pixel_index];
            store to output frame.
        }
    }
}
if output_format == RGBX888 || output_format == RGBA888
{
    s0=0;
    s1=1;
    s2=2;
    s3=3;
    if(output_swap){
        Swap(s0, s2);
    }
    Loop all pixels{
        if(pixel in output_crop_rect){
            R=data_in[s0][pixel_index];
            G=data_in[s1][pixel_index];
            B=data_in[s2][pixel_index];
            A=data_in[s3][pixel_index];
            store to output frame.
        }
    }
}
if output_format == ARGB8888 
{
    s0=3;
    s1=0;
    s2=1;
    s3=2;
    if(output_swap){
        Swap(s1, s3);
    }
    Loop all pixels{
        if(pixel in output_crop_rect){
            R=data_in[s0][pixel_index];
            G=data_in[s1][pixel_index];
            B=data_in[s2][pixel_index];
            A=data_in[s3][pixel_index];
            store to output frame.
        }
    }
}
```

| Variable                                      | Bit                    | Comment        |
|-----------------------------------------------|------------------------|----------------|
| Rect_left<br/>Rect_top                        | 16bit unsigned         | Range [0, 65535] |
| Rect_width<br/>Rect_height                    | 5bit unsigned          | Range [1, 16]    |
| pixel_index                                   | 8bit unsigned          | Range [0, 65535] |
| s0, s1, s2, s3                                | 8bit unsigned          | Range [0, 255]   |
| Y00, Y01, Y10, Y11, U00, U01,<br/>U10, U11, V00, V01, V10, V11,<br/>U, V, R, G, B, A | 8bit unsigned | Range [0, 255] |
| data_in[4][256]                               | 8bit unsigned × 4 × 256 | Range [0, 255]   |

| Register           | Bit             | Comment            |
|--------------------|-----------------|-----------------------------------------|
| Output_format      | 3bit unsigned   | 0: RGB888 (R at low address, B at high address)<br/>1: RGBX8888<br/>2: RGBA8888<br/>3: ARGB8888 (A at low address, B at high address)<br/>5: yuv420sp (U at low address, V at high address) |
| Output_swap        | 1bit unsigned   | 0: No swap<br/>1: RGB swap RB, YUV swap UV                                                  |
| Output_layout      | 1bit unsigned   | 0: Linear<br/>1: FBC compressed                                                             |
| Output_crop_left   | 16bit unsigned  | Range [0, 65534]; `crop_left < output_left + output_width`                                  |
| Output_crop_top    | 16bit unsigned  | Range [0, 65534]; `crop_top < output_top + output_height`                                   |
| Output_crop_width  | 16bit unsigned  | Range [1, 65535]<br/>`crop_left + crop_width ≤ output_left + output_width`                  |
| Output_crop_height | 16bit unsigned  | Range [1, 65535]<br/>`crop_top + crop_height ≤ output_top + output_height`                  |

### 2.4 Video Subsystem

#### Introduction

The Video Processing Unit (VPU) is a video accelerator engine with two cores designed for decoding and encoding multiple video standards. It includes a host CPU to run firmware to control the hardware engine of functions, such as bit stream parsing, control of video hardware sub-blocks and error resilience.

The VPU can work at up to 819MHz clock frequency, and supports a wide range of video standards, including H.265, H.264, VP8, VP9, MPEG4, MPEG2 and H263. It supports simultaneous

- Encoding and decoding at 1080P@60fps
- H264/H265 encoding at 1080P@30fps and H264/H265 decoding at 4K@30fps

The video codec core block executes the actual decoding and encoding for each standard by using hardwired logic. Among them, Macroblock Sequencer is the main controller that schedules process flows of the sub-blocks, and aims to reduce loads on the processor and complexity of the firmware.

As mentioned, several standard-independent blocks share common logics while they are in operation in order to ensure efficiency and streamlined performance.

#### Video Encoder

##### Encoding Features

- Configurable Arm Frame Buffer Compression (AFBC) 1.0 or 1.2 for input
- Support for YUV422 and YUV420 AFBC block split for 16 x 16
- Support for stride (not applicable to AFBC input formats)
- Horizontal and vertical mirroring (not applicable to AFBC input formats)
- Optional source frame rotation in 90-degree steps before encoding (not applicable to AFBC input format)

  > **Note.** If YUV422 is rotated by 90 or 270 degrees and not converting to YUV420, the result will be converted to YUV440.
  >
- Encoding support for the following source-frame input formats:

  - 1-plane YUV422, scan-line format, interleaved in YUYV or UYVY order
    > **Note.** YUV422 input scan be converted to YUV420
    >
  - 1-plane RGB (8-bit) in byte-address order: RGBA, BGRA, ARGB or ABGR
  - 2-plane YUV420, scan-line format, with chroma interleaved in UV or VU order
  - 3-plane YUV420, scan-line format
    > **Note.** 3-plane format is supported for testing purposes only, and should not be used for optimal performance
    >
  - AFBC YUV422
  - AFBC YUV420

##### Supported Encoding Formats

- HEVC (H.265) Main
- H.264 Baseline Profile (BP)
- H.264 Main Profile (MP)
- H.264 High Profile (HP)
- VP8
- VP9 Profile 0

###### HEVC (H.265) Encoding Features

- Encoded bit stream is compliant with the HEVC (H.265) Main Profile
- Encoding speed of 1080p@60fps (dual cores at approximately 300 MHz)
- Bitrates up to 50MBit/s using a single core operating at 300MHz
- Max frame width and height: 4096 pixels
- 8-bit encoding with I, P, and B frames
- Progressive encoding with 64×64 CTU size
- Support for tiled mode up to four tiles with horizontal splits only
- Wave front parallel encoding
- Motion Estimation (ME) search window dimensions: ±128 pixels horizontally, ±64 pixels vertically
- ME search precision: down to Quarter Picture Element (QPEL) resolution
- Luma intra-modes: 8×8, 16×16, and 32×32
- Chroma intra-modes: 4×4, 8×8, and 16×16
- Inter-modes: 8×8, 16×16, and 32×32
- Transform size for luma: 8×8, 16×16, and 32×32
- Transform size for chromas: 4×4, 8×8, and 16×16
- Skipped CUs and Merge modes
- Deblocking
- Sample Adaptive Offset (SAO)
- Constrained intra-prediction selectable
- Fixed Quantization Parameters (QP) or rate-controlled operation.
- Rate control uses a leaky bucket model based on bitrate and buffer size settings
- Long term reference frame support
- Selectable intra-frame refresh interval
- Slice insertion on a CTU row granularity
- Selectable limits for the search window and split options
- Encoders do not prevent the output from exceeding the maximum number of bits per CTU

###### H.264 Encoding Features

- Encoded bitstream is compliant with the Baseline, Main, High Profiles
- Encoding speed of 1080p@60fps (dual cores at approximately 300 MHz)
- Bitrates up to 50MBit/s using a single core operating at 300MHz
- Max frame width and height: 4096 pixels.
- Support for I, P, and B frames
- Support for progressive encoding
- Context Adaptive Binary Arithmetic Coding (CABAC) or Context Adaptive Variable Length Coding (CAVLC) entropy coding

  > **Note.** B frames are not supported with CAVLC entropy coding
  >
- Motion Estimation (ME) search window dimensions: ±128 pixels horizontally, ±64 pixels vertically
- ME search precision: down to Quarter Picture Element (QPEL) resolution
- Luma intra-modes: 4×4, 8×8, 16×16
- Chroma intra-modes: 8×8
- Inter-modes: 8×8, and 16×16
- Transform size: 4×4 and 8×8
- Support for skipped macroblocks
- Deblocking
- Constrained intra-prediction selectable
- Fixed QP operation or rate-controlled operation
- Rate control uses a leaky bucket model based on bitrate and buffer size settings
- Support for long term reference frame
- Selectable intra-frame refresh intervals
- Slice insertion granularity of 32-pixel high rows
- Possible to limit the search window and the macroblock split options
- Always enabled the escape option to prevent the emulation of a Network Abstraction Layer (NAL) unit start code regardless of the NAL packet format setting

  > **Notes.**
    > - For further details, please refer to ITU-T H.264 Annex B: [VC-1 Compressed Video Bitstream Format and Decoding Process](https://multimedia.cx/mirror/VC-1_Compressed_Video_Bitstream_Format_and_Decoding_Process.pdf)
    > - Encoders do not prevent the output from exceeding the maximum number of bits per macroblock

###### VP8 Encoding Features

- Encoding speed of 1080p@60fps (dual core at approximately 400 MHz)
- Bitrate up to 50MBit/s using a single core operating at 400MHz
- Max frame width and height: 2048 pixels
- Support for I and P frames
- Support for progressive encoding
- Motion Estimation (ME) search window dimensions: ±128 pixels horizontally, ±64 pixels vertically
- ME search precision: down to QPEL resolution
- Luma intra-modes: 4×4, 8×8, 16×16
- Chroma intra-modes: 8×8
- Inter-modes: 8x8, and 16×16
- Support for macroblocks skipping
- Deblocking
- Fixed QP operation or rate-controlled operation
- Rate control uses a leaky bucket model based on bitrate and buffer size settings
- Selectable intra-frame refresh intervals
- Possible to limit the search window and the macroblock split

###### VP9 Encoding Features

- Encoded bitstream is compliant with VP9 Profile 0 at 8-bit depth
- Encoding speed of 1080p@60fps (dual core at approximately 300 MHz)
- Bitrate up to 50MBit/s using a single core operating at 300MHz
- Max frame width and height: 4096 pixels
- Support for 8-bit sample depth
- Support for I and P frames
- Support for progressive encoding
- Tiled rows and columns
- Motion Estimation (ME) search window dimensions: ± 128 pixels horizontally, ± 64 pixels vertically
- ME search precision: down to Quarter Picture ELement (QPEL) resolution
- Luma intra-modes: 8×8, 16×16, and 32×32
- Chroma intra-modes: 4×4, 8×8, and 16×16
- Inter-modes: 8×8, 16×16, and 32×32
- Transform size for luma: 8×8, 16×16, and 32×32
- Transform size for chroma: 4×4, 8×8, and 16×16
- Support for superblocks skipping
- Deblocking
- Fixed QP operation or rate-controlled operation
- Rate control uses a leaky bucket model based on bitrate and buffer size settings
- Selectable intra-frame refresh intervals
- Support for implicit or explicit probability update using delayed contexts

#### Video Decoder

##### Decoding Features

- Support for the following source frame output formats:
  - 2-plane YUV420 scan line format: chroma interleaved in UV or VU order
  - 3-plane YUV420 scan line format
    > **Notes.**
    > - Support for 3-plane format is included for testing purposes only, do not use such max performance for normal applications
    > - Ensure of correct alignment of YUV buffer and stride for optima performance

- YUV420 AFBC format, 8-bit color depth
- Configurable for AFBC 1.0 or AFBC 1.2 output
- Support for stride for scan-line formats only
- Decoded frame rotation is supported in 90-degree steps before output

  > **Note.** Not applicable for AFBC output formats
  >
- Support for output average luminance (brightness) and chrominance (color) values for each 32×32 pixel block in every displayed output frame

##### Supported Decoding Formats

- HEVC (H.265): Main Profile
- H.264: Baseline, Main, High Profile
- VP8
- VP9: Profile 0
- VC-1: SP/MP/AP
- MPEG4: SP/ASP
- MPEG2: MP
- H.263: Profile 0

###### HEVC (H.265) Decoding Features

- Fully compliance with the Main Profiles
- Support for 2160p@30fps using dual core operating at approximately 300MHz
- Capability of handling average bitrate up to 100MBit/s with a single core at 600MHz
- Max frame width and height: 4096 pixels
- Error concealment is performed for handling bit errors
- Output of relevant stream parameter information during decoding

###### H.264 Decoding Features

- Fully compliance with H.264 Baseline, Main, High and High 10 progressive Profiles
- For streams using Flexible Macroblock Ordering (FMO) or Arbitrary Slice Ordering (ASO) in Baseline Profile, it is used WVGA resolution with decoding speed of 30fps with a single core at 400MHz
- For streams without FMA and ASO, the decoding speeds are as follows:

  - 2160p@30fps using dual core at approximately 300MHz
  - 1080i@120fps using dual core at 400MHz
- For progressive streams:

  - Average bitrate up to 100MBit/s with a single core at 600MHz
  - Max frame width and height: 4096 pixels
- For interlaced streams:

  - Average bitrate up to 50MBit/s with a single core at 400MHz
  - Max frame width: 2048 pixels
  - Max frame height: 4096 pixels
- Error concealment is performed for managing bitstream errors
- Output of relevant stream parameter information during decoding
- Always enabled the escape option to prevent the emulation of a Network Abstraction Layer (NAL) unit start code, regardless of the NAL packet format setting

  > **Note.** For further details, please refer to ITU-T H.264 Annex B: [VC-1 Compressed Video Bitstream Format and Decoding Process](https://multimedia.cx/mirror/VC-1_Compressed_Video_Bitstream_Format_and_Decoding_Process.pdf)
  >

###### VP8 Decoding Features

- Fully compliance with the VP8 Specification
- Support for decoding speed of 1080p@60fps using dual core at approximately 400MHz
- Average bitrate up to 50MBit/s with single core at 400MHz
- Max frame width and height: 2048 pixels
- Error concealment is performed for managing bitstream errors

###### VP9 Decoding Features

- Fully compliance with Profile 0
- Support for decoding speed of 2160p@30fps using dual core at approximately 300MHz and assuming no non-visible and no Alt-Ref frames
- Support for decoding speed of 2160p@30fps using dual core at approximately 400MHz and assuming an Alt-Ref frame distance of 4
- Average bitrate up to 60MBit/s using single core at 600MHz
- Max frame width and height: 4096 pixels
- Error concealment is performed for managing bitstream errors
- Output of relevant stream parameter information during decoding

###### VC-1 Decoding Features

- Fully compliance with VC-1 Simple, Main, and Advanced Profiles
- Support for decoding speeds of 1080p@60fps and 1080i@120fps using dual core at approximately 400MHz
- Average bitrate up to 40MBit/s with single core at 400MHz
- Max frame width: 2048 pixels
- Max frame height: 4096 pixels
- Error concealment is performed for managing bitstream errors

  > **Notes.**
  > - Advanced Profile bitstream data must always include the Encapsulation Mechanism regardless of the NAL packet format setting
  > - For further details, please refer to SMPTE-421M-2006 Annex E
  > - The range mapping feature of the VC-1 Advanced Profile does not apply to AFBC output

###### MPEG4 Decoding Features

- Compliance with MPEG4 Simple Profile and Advanced Simple Profile
- Support for Global Motion Compensation (GMC) with a limitation of a single warp point
- Support for decoding speed of 1080p@60fps or 1080i@120fps using dual core at 400MHz
- Capability of handling average bitrate up to 20MBit/s with a single core operating at 400MHz
- Max frame width and height: 2048 pixels
- Error concealment is performed for managing bitstream errors

###### MPEG2 Decoding Features

- Compliance with MPEG2 Main Profile
- Support for decoding speed of  1080p@60fps or 1080i@120fps using dual core at 400MHz
- Capability of handling average bitrate up to 20MBit/s with single core operating at 400MHz
- Max frame width: 4906 pixels (2,048 pixels for interlaced stream)
- Max frame height: 4096 pixels
- Error concealment is performed for managing bitstream errors

###### H.263 Decoding Features

- Compliance with H.263 Profile 0
- Support for decoding speed of 1080p@60fps using dual core at approximately 400MHz
- Capability of handling average bitrates up to 20MBit/s with single core operating at 400MHz
- Max frame width and height: 2048 pixels
- Error concealment is performed for managing bitstream errors

### 2.5 Display Subsystem

#### Display Controller

##### Introduction

The Display Controller is a hardware block that is used to transfer display data from the display's internal memory to the DSI controller. It supports one independent display device through MIPI DSI.

##### Features

- Support for up to HD+ (1920x1080@60fps)
- Support for up to 4-full-size-layer composer and maximum 8 layer-composers by up-down layer reuse in the RDMA channel
- Support for _cmdlist_ mechanism allowing hardware register parameters to be configured
- Support for concurrent write-back operations with both raw and AFBC format
- Support for dithering, cropping, rotation in write-back path
- Advanced MMU (virtual address) mechanism for nearly no page missing during 90° and 270° rotation
- Support for color keying and solid color generation
- Support for both advanced error diffusion and pattern-based dithering for the panel
- Support for both AFBC and raw format image sources
- Color saturation and contrast enhancement
- Support for both video mode and _cmd_ mode (with frame buffer in LCM) for the panel
- Support for dynamic DDR frequency adjustment with an embedded DFC buffer
- Support for the following **input formats** (see also the map shown immediately after):

  - A2BGR101010, A2RGB101010, BGR101010A2, RGB101010A2
  - ABGR8888, ARGB8888, BGRA8888, RGBA8888
  - XBGR8888, XRGB8888, BGRX8888, RGBX8888
  - BGR888, RGB888, ABGR1555, RGBA5551, BGR565/RGB565
  - XYUV_444_P1_8, XYUV_444_P1_10, YVYU_422_P1_8, VYUY_422_P1_8
  - YUV_420_P2_8, YUV_420_P3_8
    ![](static/input_formats.png)
- Support for the following **output formats**:

  - RGB888, RGB565, RGB666

##### Block Diagram

The micro-architecture of the display subsystem is depicted below.

<img src="static/display_subsystem.png" alt="" width="600">

#### HDMI Interface

##### Features

- Compliance with HDMI Specification v1.4
- Dual-channel audio stream within the range 32~192KHz
- Physical lane speed up to 2.4Gbps/lane × 3lane
- Support for up to 1920x1440@60Hz
- Support for RGB and YcbCr 4:2:2 / 4:4:4 input video format
- Support for RGB and YcbCr 4:2:2 / 4:4:4 output video formats
- Support for 8bpc / 10bpc / 12bpc input and output color depths
- Support for EIA/CEA-861-F video timing and InfoFrame structure
- Support for L-PCM(IEC 60958), 32~192KHz dual channel audio data
- Support for Consumer Electronic Control (CEC) standard packets and user-defined packets
- Inclusion of an Internal I2C Master for remote ED access supporting 100~400Kbps speed

##### Block Diagram

The architecture of the HDMI interface is depicted below.

<img src="static/HDMI_interface.png" alt="" width="600">

#### MIPI DSI Interface

##### Introduction

The MIPI Display Serial Interface (MIPI DSI) is a high-speed interface between a host processor and peripheral devices that adheres to MIPI Alliance specifications for mobile device interfaces.

##### Features

- Compliance with the MIPI DSI standard v1.0
- Compliance with the MIPI DPHY specification v1.1
- Support for MIPI DPHY up to 4 data lanes and speed up to 1200Mbps per lane
- Support for 1 active panel per DPHY link
- Compliance with the Display Command Set (DCS) standard
- Support for all pixel formats defined in DSI and DCS
- Support for video burst mode with DPHY up to 1.2Ghz per lane
- Support for virtual channels in the MIPI Link
- Support for up to 1080p resolution
- Support for command, video and burst modes
- Support for HS-TX, LP-TX, LP-RX and LP-CD signaling

#### SPI LCD Display Interface

##### Introduction

The SPI LCD Display Interface is used to

- Send image data commands
- Read image data
- Transmit image data

It supports the operational modes

- Single data line mode
- Dual data line mode

where each of which support the work modes

- 3-line/9bit mode
- 4-line/8bit mode

By software, it is possible to configure which line will be the first for transmitting data. Further, it is possible to configure the transfer mode choosing between

- Packet transfer mode
- Unpacked transfer mode

As example, below are depicted the transfers modes for some color formats, highlighting how data are organized and transmitted.

**[Packet transfer mode for RGB565]**

<img src="static/packet_transfer_mode_RGB565.png" alt="" width="700">

**[Packet transfer mode for RGB666]**

<img src="static/packet_transfer_mode_RGB666.png" alt="" width="700">

**[Packet transfer mode for RGB888]**

<img src="static/packet_transfer_mode_RGB888.png" alt="" width="700">

**[Unpacked transfer mode for RGB666]**

<img src="static/unpacked_transfer_mode_RGB666.png" alt="" width="700">

**[Unpacked transfer mode for RGB888]**

<img src="static/unpacked_transfer_mode_RGB888.png" alt="" width="700">

##### Features

- Support for SPI LCD module with resolution up to 320x240
- Support for 3-/4-line Serial Peripheral Interface (SPI) and 2-line SPI data transmission
- Support for up to 3 simultaneous overlays (2 for RGB, 1 for YUV & RGB)
- Support for dithering
- Support for gamma curve
- Alpha blending with configurable alpha values or per-pixel alpha blending
- Support for YUV to RGB color space conversion
- Support for image scaling
- Support for color keying
- Support for memory write-back
- Support for the following **input formats** for **image layer**:

  - YUV422 planar
  - YUV422 packet
  - YUV420 planar
  - RGB888
  - RGB565
  - RGB666
  - BGR888
  - BGR565
  - BGR666

  > **Note.** As can be seen, it is supported **R-B swap option** for the sake of flexibility
  >
- Support for the following **input formats** for **OSD layer**:

  - RGB888
  - RGB565
  - RGB666
  - BGR888
  - BGR565
  - BGR666

  > **Note.** As can be seen, it is supported **R-B swap option** for the sake of flexibility
  >

##### Block Diagram

The architecture of the SPI LCD Display Interface is depicted below.

![](static/SPI_LCD_Display_Interface.png)

It is clearly understandable how the display data are efficiently processed, then converted into SPI-compatible signals, then transmitted to the connected LCD display.

##### Functions

###### Blending Function

The blending function of the DSI controller is used to combine multiple layers of images or overlays with different levels of transparency (alpha values).

An example of layers and their respective alpha values is depicted below, where

- **L0**: Bottom layer, base image
- **L1**: Middle layer, alpha value **a1**
- **L2**: Top layer, alpha value **a2**

<img src="static/blending_function.png" alt="" width="400">

The following blending modes are supported:

- Normal Alpha Blending Mode
- Pre-Multiple Alpha Blending Mode
- Special Alpha Blending Mode

In the code, a different formula is implemented for each blending mode that uses the alpha value **a1** as per the following conditions:

```c
if (L1 == color_key)
a1 = 8’h0;
else if (layer_alpha_sel == 1)
a1 = layer_alpha;
else
a1 = pixel_alpha;
```

Details for each blending mode are explained in the following subsections.

**[Normal Alpha Blending Mode]**

With reference to the example figure shown above,

- For **2 layers**, the formula implemented is

  - $$
    L'=L1×a1+L0×(1-a1)
    $$
- For **3 layers** (<u>not recommended</u>), the formula implemented is

  - $$
    L'=L2×a2+L1×a1×(1-a2)+L0×(1-a1)×(1-a2)
    $$

  > **Note.** Alpha value is not supported for write-back in this case
  

In the code, the pixel value **L'** depends on the alpha value **a1** as per the following conditions:

```c
if (a1 == 8’hFF)
L' = L1;
else if (a1 == 8’h00)
L' = L0;
else
L' = (L1-L0) × a1/256 + L0
```

**[Pre-Multiple Alpha Blending Mode]**

With reference to the example figure shown above,

- For **2 layers**, the formula implemented is

  - $$
    L'=L1+L0×(1−a1)
    $$
- For **3 layers** (<u>not recommended</u>), the formula implemented is

  - $$
    L'=L2+L1×(1−a2)+L0×(1−a1)×(1−a2)
    $$

  > **Note.** Alpha value is supported for write-back and its value is given by the formula $a'=a1+a2−a1×a2$

In the code, the pixel value **L'** depends on the alpha value **a1** as per the following conditions:

```c
if (a1 == 8’hFF)
L' = L1;
else if (a1 == 8’h00)
L' = L0;
else
L' = L1-L0 × (1-a1)/256;
```

**[Special Alpha Blending Mode]**

With reference to the example figure shown above,

- For **2 layers**, the formula implemented is

   $$
    L'=L1+L0×a1
    $$
- For **3 layers** (<u>not recommended</u>), the formula implemented is

   $$
    L'=L2+L1×a2+L0×a1×a2
    $$

  > **Note.** Alpha value is not supported for write-back in this case
  

In the code, the pixel value **L'** depends on the alpha value **a1** as per the following conditions:

```c
if (a1 == 8’hFF)
L' = L0;
else
L' = L1 + L0 × a1/256;
```

###### Dither Function

The process of the Dither function is depicted below.

<img src="static/Dither_function.png" alt="" width="600">

The Dither function can be enabled/disabled by software.

###### Fmark Function

The Fmark function controls the start of displaying output. In particular,

- If Fmark function is **enabled**, displaying output will wait until the Fmark signal is received
- If Fmark function is **disabled**, displaying output will start immediately after initiated by software

By software is possible to enable/disable Fmark function as well as control the polarity of the Fmark signal.

It is recommended to have a register to set how long displaying output is delayed after LCDC received the Fmark signal.

###### Background Color Display Function

When no layer is enabled, a background color can be displayed without fetching data from DDR. The background color can be configured by software.

###### Image Capture Function

To apply the image capture function, the following parameters should be configured by software firstly:

- **startx** = X coordinate of the start point of the capture
- **starty** = Y coordinate of the start point of the capture
- **width** = Width (in pixels) of the capture from (X,Y) start point
- **height** = Height (in pixels) of the capture from (X, Y) start point
- **base_addr** = Memory start address for storing the capture
- **pitch** = Distance (in bytes) between the start of two consecutive rows of pixels stored in the memory, including any padding for alignment or hardware requirements

The process of the image capture function is depicted below.

<img src="static/image_capture.png" alt="" width="800">

### 2.6 Audio Subsystem

#### Introduction

Audio subsystem integrates two primary interfaces:

- 2 × Full-Duplex I2S Interfaces
- 1 × HDMI Audio Interface

#### Features

- **I2S Interfaces**

  - Full-duplex operation with simultaneous playback and recording support
  - Compliance with standard I2S format with fixed parameters:
    - 48 kHz sample rate
    - 16-bit data depth
    - 2 channels
  - Configurable system clock (sysclk) modes: 64fs, 128fs or 256fs

- **HDMI Audio Interface**

  - Playback-only functionality with fixed parameters:
    - 48 kHz sample rate
    - 16-bit data depth
    - 2 channels

### 2.7 Connectivity Subsystem

#### PCIe 2.0

##### Introduction

K1 implements three PCIe Dual-Mode ports which can be configured as either Root Complex (RC) or Endpoint (EP) device.

All ports support Gen2 with a data transfer speed of 5GT/s per lane. However, one port supports one lane only and two ports support two lanes each.

##### Features

- Support for Dual-Mode, programmable as either Complex (RC) or Endpoint (EP) device
- Support for all non-optional features of the PCI Express Base Specification - Revision 5.0 - Version 1.0 (limited to Gen2 speed scope)
- Support for Internal Address Translation Unit (iATU) with 8 entries for outbound and 8 entries for inbound traffic
- Support for Embedded DMA with Hardware Flow Control which includes 4 write channels and 4 read channels
- Support for ECRC generation and check
- Support for max payload size up to 256 bytes
- Support for Automatic Lane Flip and Reversal
- Support for L0 and L1 Power State of Active State Link PM
- Support for Latency Tolerance Reporting (LTR)
- Support for only Virtual Channel 0
- Support for ID Based Ordering (IDO)
- Support for Completion Timeout Ranges
- Support for Separate Reference Clock With Independent Spread (SRIS)
- Support for up to 64 outbound Non-Post Requests
- Support for up to 32 outstanding AXI slave Non-Post requests
- Support for only Function 0 with 6 size-programmable BARs in EP Mode
- Support for MSI Capability in EP Mode
- Support for Integrated MSI Reception Module in RC Mode

##### Block Diagram

The architecture of the PCIe Dual-Mode port set is depicted below.

<img src="static/PCIe_Dual-Mode_port.png" alt="" width="700">

As can be seen, there are

- One PCIe Gen2x1 Dual-Mode port (hereafter Port A)
- Two PCIe Gen2x2 Dual-Mode ports (hereafter Port B and Port C)

as said previously, and all them consists of

- A **controller** integrated into SoC via **3 AXI ports** which are designed as

  - **AXI Master Port** to manages inbound traffic (i.e. data coming into the system) either from a remote device or through the PCIe controller's internal DMA, allowing the access to DDR memory for transferring data both to and from the remote device
  - **AXI Data Slave Port** to allows the local CPU accessing itself for outbound traffic
  - **AXI DBI Slave Port** to be used for the PCIe controller's configuration interface
- A **PHY** complied with PIPE 3 specification and distinguished in

  - **Phy2x1_22** which
    - Supports Gen2 with one lane (x1)
    - Is built using a 22nm process
    - Is shared between Port A and USB3 controller but <u>not simultaneously</u>, i.e. both Port A and USB3 controller can operate but <u>not at the same time</u>
  - **Phy2x2_22** which
    - Supports Gen2 with two lanes (x2)
    - Is built using a 22nm process
    - Comes for Port B and Port C <u>distinctly</u>, i.e. Port B and Port C have their own dedicated PHY
- A **miscellaneous logic**, in particular **chip I/O with remote links partner** as follows:

  - **Differential Data Signals**: Rx_p/n, Tx_p/n (x2 lanes for Port B/C, x1 lane for Port A)
  - **Reference Clock Signals**: refclk_p/n (support for both input and output mode)
  - **Warm Reset Signal**: PERST# (input in EP mode, output in RC mode)
  - **Wake-Up signal**: WAKE# (output in EP mode, input in RC mode)

#### USB

##### Introduction

K1 includes three USB ports as follows:

- A USB2.0 OTG Port
- A USB2.0 Host Only Port
- A USB3.0 Port with a USB2.0 DRD interface

##### Features

###### USB2.0 OTG Port Features

- **Controller:**

  - Support for both USB2.0 Host and Device mode
  - Compliance with the USB2.0 standard
  - Support for USB2.0 High Speed (480Mb/s) and Full Speed (12Mb/s) for both Host and Device modes
  - Support for USB2.0 Low Speed (1.5Mb/s) for Host Only Mode
  - Host controller registers and data structures are compliant with the Intel EHCI specification
  - Device controller registers and data structures are implemented as extensions to the EHCI programming interface
  - Bus interface is compliant with AMBA-AHB specification

- **Communication Interface:**

  - Implementation of UTMI+ interface to communicate with USB2.0 PHY

- **Protocols:**

  - Support for the Session Request Protocol (SRP)
  - Support for the Host Negotiation Protocol (HNP)

- **Channel & Endpoint:**

  - Support for up to 16 host channels
  - In Device mode, support for 16 IN and 16 OUT endpoints, where
    - 16KB buffer is for transmitting data
    - 2KB buffer is for receiving data

###### USB2.0 Host Only Port Features

- **Controller:**

  - Support for USB2.0 HS, USB2.0 FS, USB2.0 LS Host modes
  - Compliance with the USB2.0 standard
  - Support for High Speed (480Mb/s), Full Speed (12Mb/s), Low Speed (1.5Mb/s) for Host mode
  - Host controller registers and data structures are compliant with the Intel EHCI specification
  - Bus interface is compliant with AMBA-AHB specification

- **Communication Interface:**

  - Implementation of UTMI+ interface to communicate with USB2.0 PHY

- **Channel Support:**

  - Support for up to 16 host channels

###### USB3.0 Port with a USB2.0 DRD Interface Features

- **Controller**

  - Support for both USB3.0 Host and Device modes
  - Support for both USB2.0 Host and Device modes
  - Compliance with both the USB3.0 and USB2.0 standards
  - Support for USB3.0 (Super Speed) and USB2.0 Host and Device mode
  - USB3.0 Host Controller registers and data structures are compliant with the Intel xHCI specification
  - USB3.0 Device controller registers and data structures are self-defined requiring software configuration
  - Support for one USB3.0 port and one USB2.0 port
  - Support for High Speed (480Mb/s) and Full Speed (12Mb/s) for Host and Device mode
  - Support for Low Speed (1.5Mb/s) for Host-Only mode

- **Communication Interface:**

  - Use of PIPE3 (125MHz) interface for USB3.0 PHY
  - Use of UTMI+ (30/60MHz) interface for USB2.0 PHY

- **Clock Domains:**

  - PIPE3 PHY (125MHz)
  - UTMI+ PHY (30/60MHz)
  - MAC (nominal 125MHz)
  - BUS clock domain
  - RAM clock domain

- **System & Power Management:**

  - Internal DMA controller
  - Support for USB2.0 suspend mode
  - Support for U1/U2/U3 low-power modes for USB3.0

- **Endpoint & Memory:**

  - Support for up to 32 endpoints in Device mode
  - Flexible endpoint FIFO sizes (not limited to powers of 2) allowing the use of contiguous memory locations
  - Descriptor caching and data pre-fetching for improving performance in high-latency systems

- **Additional Features:**

  - Software-controlled standard USB commands (USB SETUP commands forwarded to application for decoding)
  - Hardware-level error handling for USB bus and packet-level issues
  - Support for interrupts

##### Block Diagram

The architecture of the USB port set is depicted below, where

- **USB#0 Port =** USB2.0 OTG Port
- **USB#1 Port =** USB2.0 Host-Only Port
- **USB#2 Port =** USB3.0 Port with a USB2.0 DRD interface

<img src="static/USB_port.png" alt="" width="700">

#### Ethernet GMAC

##### Introduction

K1 features a GMAC IP core which includes the essential protocol requirements for the operation of 10/100/1000 Mbps Ethernet/IEEE 802.3-2012 compliant node.

The GMAC IP core can operate at 10 Mbps, 100 Mbps (Fast Ethernet) or 1000 Mbps (Gigabit Ethernet). Additionally, it includes a powerful 64-bit Scatter-Gather DMA to transfer packets between HOST Memory and Internal FIFOs to achieve high performance.

##### Features

- Capability of handling transmit/receive data encapsulation functions, including Framing (frame boundary delimitation, frame synchronization) and Error Detection (physical medium transmission errors)
- Media access management with medium allocation (collision avoidance) and contention resolution (collision handling) in Half-Duplex Mode of operation at speeds of 10/100 Mbps
- Retransmission of frames that result in Collision in Half-Duplex mode
- Support for Flow Control functions in Full Duplex mode by decoding PAUSE control frames, disabling the transmitter and generating PAUSE control Frames
- Support for a 4-bit data path based RGMII Interface to connect with RGMII-based PHY
- Support for Management Interface by generating management frames on the MDC/MDIO pins to communicate with external PHY devices
- Bus mastering on the AXI interface to transfer packets between the HOST memory and the internal FIFOs using 64-bit transfer mode
- Automatic transfer of packets between the HOST memory and internal FIFOs (based on descriptors) to minimize CPU overhead

##### Block Diagram

The micro-architecture of Ethernet GMAC unit is depicted below.

<img src="static/Ethernet_GMAC.png" alt="" width="600">

#### SDIO Interface

##### Introduction

The SDIO interface is a hardware block that serves as the host of the SDIO bus to transfer data between the SDIO Wi-Fi module and the internal bus master.

##### Features

- Compliance with with 4-bit SDIO 4.10 protocol specification
- Consistent with the register set defined in SD-HCI specification with additional vendor-specific registers
- Support for 1-bit and 4-bit SDIO bus
- Support for the following data transfer type defined in the SD-HCI specification:

  - PIO
  - SDMA
  - ADMA
  - ADMA2
- Support for the following speed modes defined in SD 3.0 specification:

  - Default Speed mode, up to 12.5MB/s, 3.3V signal level
  - High Speed mode, up to 25MB/s, 3.3V signal
  - SDR12, SDR up to 25 MHz, 1.8V signal
  - SDR25, SDR up to 50 MHz, 1.8V signal
  - SDR50, SDR up to 100 MHz, 1.8V signal
  - SDR104, SDR up to 208 MHz, 1.8V signal
  - DDR50, DDR up to 100MHz, 1.8V signal
- Hardware-based CRC generation and check for all command and data transactions on the card bus
- Support for read-wait control in SDIO cards
- Support for suspend/resume functionality in SDIO cards
- 1024 Bytes (2 x 512 Bytes data block) FIFO for sending and receiving data

#### CAN-FD Interface

##### Introduction

The CAN-FD controller is a full implementation of the CAN protocol specification which is compliant with both the CAN with Flexible Data-Rate (CAN-FD) protocol and CAN 2.0 Part B protocol.

##### Features

- Full implementation of the CAN-FD protocol and CAN specification 2.0 Part B with

  - Standard data frames
  - Extended data frames
  - Data lengths from 0 to 64 bytes
  - Programmable bit rate
  - Content-related addressing
- Compliant with the ISO 11898-1 standard
- Silicon-proven implementation passing ISO 16845-1:2016 CAN conformance tests
- Flexible mailboxes configurable to store 0, 8, 16, 32 or 64 bytes of data
- Each mailbox configurable to either receive or transmit supporting both standard and extended messages
- Distinct receive mask registers per mailbox
- Full-featured receive FIFO with a storage capacity of up to 6 frames with automatic internal pointer handling and DMA support
- Transmission abort capability
- Support for flexible message buffers with a total of 128 message buffer slots (8 bytes each) which can be configurable as transmitter or receiver
- Programmable clock source for the CAN Protocol Engine, either peripheral clock or oscillator clock
- RAM is not used for reception or transmission but can be used as general purpose RAM space
- Support for Listen-Only Mode (LOM)
- Programmable Loop-Back mode for self-test operation
- Programmable transmission priority scheme: based on lowest ID, lowest buffer number or highest priority
- 16-bit free-running timer for time stamps with an optional external time tick
- Global network time synchronized by a specific message
- Maskable interrupts
- Independence from the transmission medium (required an external transceiver)
- Short latency for high-priority messages due to an arbitration scheme
- Low-power modes with programmable wakeup on bus activity or frame matching (pretended networking)
- Transceiver Delay Compensation (TDC) when transmitting CAN-FD messages at faster data rates
- Remote request frames can be managed automatically by software
- CAN bit time settings and configuration can only be written in Freeze mode
- Configurable transmission mailbox status: either lowest priority buffer or empty buffer
- Support for Identifier Acceptance Filter Hit Indicator (IDHIT) register for received frames
- SYNCH bit in Error Status 1 register indicates synchronization with the CAN bus
- Support for CRC status for transmitted message
- Support for reception FIFO Global Mask register
- Selectable priority between mailboxes and reception FIFO during matching process
- Advanced receive FIFO ID filtering, capable of matching incoming IDs against either 128 extended IDs, 256 standard IDs, or 512 partial (8 bit) IDs, with up to 32 elements in the ID Filter Table
- Fully backward compatibility with previous CAN-FD version
- Support for detection and correction of errors in memory read accesses. Each byte of CAN-FD memory is paired with 5 parity bits, forming a 13-bit word. The error correction mechanism can

  - Detect and correct single-bit errors (correctable errors)
  - Detect, but not correct, two-bit errors (non-correctable errors)
- Support for pretended networking functionality in low-power modes: Doze mode and Stop mode

#### SPI Interface

##### Introduction

The SPI interface is a synchronous serial interface that allows the communication with external devices using Motorola Serial Peripheral Interface (SPI) protocol for data transfer. It can be configured to operate in either Master mode (where the attached peripheral functions as a slave) or Slave mode (where the attached peripheral functions as a master).

##### Features

- Support for four combinations of CPOL and CPHA for Serial Peripheral Interface (SPI)
- Configurable to operate in either Master mode (where the attached peripheral functions as a slave) or Slave mode (where the attached peripheral functions as a master)
- Support for Receive-without-Transmit operation
- Support for serial bit rate from 6.3Kps (min recommended) to 52Mbps (max)
- Data size configurable to 8, 16, 18 or 32 bits in length
- Availability of a transmit FIFO (TXFIFO) and another independent receive FIFO (RXFIFO), where

  - In Non-Packed Data mode, both FIFOs are 32 rows deep x 32 bits wide supporting a total of 32 samples
  - In Packed Data mode, double-depth FIFOs are used when the data samples are 8 bits or 16 bits wide, and both FIFOs are 64 locations deep x 16 bits wide supporting a total of 64 samples
  - Both FIFOs can be loaded or emptied by using either programmed I/O (PIO) or DMA burst transfers

#### UART Interface

##### Introduction

The Universal Asynchronous Receiver/Transmitter (UART) interface is controlled via Direct-Memory Access (DMA) or programmed I/O.

##### Features

- Support for up to 10 UART interfaces
- Compatible with the 16550A and 16750 UART standards
- Support for adding and deleting standard asynchronous communication bits (start, stop and parity) in the serial data stream
- Independent control of transmission, reception, line status, data-set interrupts
- Modem control functions (CTSn and RTSn for both UART2 and UART3)
- Auto-flow capability for data I/O management without generating interrupts, where

  - RTSn (output) is controlled by the UART receive FIFO
  - CTSn (input) is from UART modem transmission controls
- Programmable serial interface with configurable options as follow:

  - 7-bit or 8-bit character length
  - Even, odd or no parity detection
  - 1 stop-bit generation
  - Baud rate generation up to 3.6Mbps for the 4 Fast UARTs
  - False start-bit detection
- 64-byte transmit FIFO
- 64-byte receive FIFO
- Support for complete status reporting
- Support for generating and detecting line breaks
- Support for internal diagnostics including:

  - Loopback control for fault isolation in communications link
  - Break, parity and framing error simulation
- Fully prioritized interrupt system
- Support for separated DMA requests for both transmit and receive data services
- Serial infrared asynchronous interface compliant with the Infrared Data Association (IrDA) specification

#### Bus Interface

##### Introduction

The Inter-Integrated Circuit (I2C) bus is a true multi-master bus including collision detection and arbitration.

A dedicated I2C module, referred to as the power I2C module, is used to interface to the power management IC.

The I2C bus interface can function as both a master and a slave device on the I2C bus. This serial bus, developed by Philips Corporation, uses a 2-pin interface as follows:

- **SDA**: Data pin for input and output functions
- **SCL**: Clock pin for timing reference and control of the I2C bus

The I2C bus allows the I2C unit to interface with other I2C peripherals and microcontrollers. It requires minimal hardware, providing an economical solution for communicating status and control information between chips and external devices.

The I2C bus interface is a peripheral device residing on the peripheral bus that performs

- **Data transfer**, handled through a buffered interface for reliable communication
- **Control and status management**, accessed via memory-mapped registers

##### Features

- Compliance with I2C bus specification with the exception of the support for the hardware general call, 10-bit slave addressing and CBUS compatibility
- Support for Multi-Master and Arbitration
- **Operation modes and speeds** as follows:

  - Standard Operation Mode: up to 100 Kbps
  - Fast Operation Mode: up to 400 Kbps
  - High-Speed Slave Operation Mode: up to 3.4 Mbps (High-Speed I2C only)
  - High-Speed Master Operation Mode: up to 3.3 Mbps (High-Speed I2C only)

  > **Note.** In High-Speed Master Operation Mode, I2C operational frequencies decrease due to the pull-up resistors on the bus. The SCL frequency is inversely proportional to the pull-up resistor value (1/R).

##### Block Diagram

The architecture of the I2C bus interface is depicted below.

<img src="static/I2C_bus_interface.png" alt="" width="500">

#### IR-RX Interface

##### Features

- Infrared input signals are transformed into the Run-Length-Code (RLC) format
- Configurable signal width threshold for noise detection
- 32 Bytes FIFO for received data storage

#### One-Wir Bus Master Interface

##### Introduction

The One-Wire Bus Master Interface Controller is responsible for receiving and transmitting data on the One-Wire bus. It fully controls the One-Wire bus using 8-bit commands. The processor interacts with the controller by loading commands, reading and writing data, and configuring interrupt controls through 5 specific registers.

All One-Wire bus timing and control are generated within the One-Wire Bus Master Interface Controller once a command or data is loaded by the host. When there is activity on the bus that requires the CPU to respond, the One-Wire Bus Master Interface Controller sets a status bit and, if enabled, sends an interrupt to the CPU.

For detailed information about specific slave implementations, please refer to the **Book of iButton® Standards** which describes the operation of the One-Wire bus master interface.

##### Block Diagram

The architecture of the One-Wire Bus Master Interface is depicted below.

<img src="static/One-Wire_Bus_Master_Interface.png" alt="" width="500">

#### I2S Interface

##### Introduction

The I2S interface is a synchronous serial interface designed to connect to various external devices, including Analog-to-Digital converters (ADC), audio and telecommunication codec. It directly supports the Inter-IC Sound (I2S) Protocol for data transfer.

##### Features

- Configurable to operate in either Master mode (where the attached peripheral functions as a slave) or Slave mode (where the attached peripheral functions as a master)
- Support for Receive-without-Transmit operation
- Support for serial bit rate from 6.3Kbps (min recommended) up to 52Mbps (max)
- Data sizes configurable to 8, 16, 18 or 32 bits in lenght
- Availability of a transmit FIFO (TXFIFO) and another independent receive FIFO (RXFIFO), where

  - In Non-Packed Data mode, both FIFOs are 32 rows deep x 32 bits wide supporting a total of 32 samples
  - In Packed Data mode, double-depth FIFOs are used when the data samples are 8 bits or 16 bits wide, and both FIFOs are 64 locations deep x 16 bits wide supporting a total of 64 samples
  - Both FIFOs can be loaded or emptied by using either programmed I/O (PIO) or DMA burst transfers
- Support for up to eight time slots with independent transmit/receive operation in any/all/none of the time slots
- Audio clock control provides a 4x or 8x output clock to support most standard audio frequencies

### 2.8 Security Subsystem

#### Encryption Engin

##### Features

- Support for symmetric encryption algorithms including AES
- Support for public key algorithms including RSA/ECC
- Support for HASH algorithms including SHA2

#### TRNG

##### Features

- Support for True Random Number Generator (TRNG) for security applications

#### eFuse

#### Features

- Support for total 4K eFuse bits organized into 16 banks
- User keys storage
- Anti-Rollback bits for secure firmware update
- Life Cycle Stage (LCS) bits for secure life cycle management
- Hardware lock for each eFuse bank

#### AES Engine

##### Features

- Dedicated high-performance AES Engine for massive data encryption/decryption

### 2.9 System Peripherals

#### DMA

##### Introduction

The Direct-Memory Access (DMA) controller is designed to transfer data between memory and peripheral devices without CPU intervention.

Peripheral devices do not directly supply addresses or commands to the memory controller. Each DMA request from a peripheral triggers a memory-bus transaction. The processor can directly access the peripheral bus by using the DMA controller which acts as a DMA bridge to bypass the DMA of the system

The DMA controller can manage different data transfer types in DMA Flow-Through Mode through 16 configurable DMA channels as tabled below.

|               | Internal Memory | External Memory | Internal Peripheral | External Peripheral |
|---------------|-----------------|-----------------|---------------------|---------------------|
| Internal Memory | Flow-Through Mode | ___             | ___                 | ___                 |
| External Memory | Flow-Through Mode | Flow-Through Mode | ___                 | ___                 |
| Internal Peripheral | Flow-Through Mode | Flow-Through Mode | ___                 | ___                 |
| External Peripheral | Flow-Through Mode | Flow-Through Mode | ___                 | ___                 |

##### Features

- Capability of handling data transfers by two instances of the DMA controller, in particular

  - One for secure domains
  - One for non-secure domains
- Support for the following data transfer types in DMA Flow-Through Mode:

  - Memory-to-memory
  - Peripheral-to-memory
  - Memory-to-peripheral
- Support for DMA Flow-Through Mode for data transfers between Flash and DDR
- Implementation of a priority mechanism to process active channels at any time (up to 4 channels with outstanding DMA requests)
- Each of the 16 DMA channels is allow to operate for descriptor-fetch or non-descriptor-fetch transfers
- Support for the following special descriptor modes:

  - Descriptor Comparison
  - Descriptor branching
- Retrieval of trailing bytes from the receive peripheral-device buffers
- Support for programmable data-burst sizes (8, 16, 32 or 64 bytes) and configurable peripheral device data widths (byte, half-word or word)
- Support for up to 8191 bytes of data transfer per descriptor (larger data transfers can be performed by chaining multiple descriptors)
- Support for a flow control bit to manage requests from peripheral device (requests are not processed unless a flow control bit is set)

##### Block Diagram

The architecture of the DMA controller is depicted below.

<img src="static/DMA_controller.png" alt="" width="500">

#### Timer

##### Introduction

K1 includes three general-purpose 32bit timers for system applications, and each one has its own 32bit Timer Counter Control Register (TCCRn) functioning as an up counter.

#### Features

- Programmable count mode as follows:
  - Fast count mode by input clock frequency of 12.8 MHz, 6.4 MHz, 3 MHz or 1 MHz
  - Slow count mode by input clock frequency of 32.768 KHz

#### WatchDog

##### Introduction

K1 includes one 16bit WatchDog Timer (WDT).

##### Features

- Programmable count mode as follows:
  - Fast count mode by input clock frequency of 12.8 MHz, 6.4 MHz, 3 MHz or 1 MHz
  - Slow count mode by input clock frequency of 32.768 KHz

#### Temperature Sensor

##### Introduction

The Temperature Sensor Module (TSEN) provides temperature sensing and conversion functions, using a temperature-dependent voltage to time conversion method.

TSEN has an alarm function that triggers an interrupt when the temperature exceeds a specified warning threshold. It also includes a programmable self-repeating mode which performs temperature sensing operations automatically at intervals by a programmed delay.

TSEN can be used by software to monitor the on-die temperature to let take all necessary actions, such as reducing the core frequency when a temperature interrupt is triggered.

##### Features

- Possibility to turn on/off TSEN (by software)
- Possibility to configure (by software) a high and low warning threshold of a BJT temperature for triggering related interrupts
- Record of the highest detected temperature of a BJT and its corresponding ID, and keeping track of the two most recent detected temperatures
- Possibility to enable (by software) the emergency system reset/reboot when a temperature violation occurs (the temperature sensor will trigger a system reset/reboot similar to the one performed by the Watchdog if the detected temperature exceeds the configured threshold)

##### Block Diagram

The architecture of the Temperature Sensor Module is depicted below.

<img src="static/Temperature_Sensor.png" alt="" width="400">

#### PWM

##### Introduction

K1 contains 20 Pulse-Width Modulation (PWM) channels labeled as PWMx where x=[0,19].

Each PWM channel operates independently with its own configuration registers and generates an output PWM signal on a multi-function pin.

Each PWM channel allows controlling over both the leading-edge timing and the trailing-edge timing of its output signal.

The timing of each PWM channel can be set to run continuously or be adjusted dynamically to meet the change of requirements.

The power-saving mode allows stopping the internal clock of a PWM channel (PSCLK_PWM), resulting to a constant high or low state of the output signal of that PWM channel (PWM_OUT), thus saving power when the output signal of that PWM channel is not needed.

##### Features

- Support for 50% duty-cycle ranging from 198.4Hz to 6.5MHz (additional duty-cycle options depend on the choice of the preferred frequency)
- Enhanced period time controlled through 6-bit clock divider and 10-bit period time counter
- 15-bit pulse counter control

#### Mailbox

##### Introduction

The Mailbox is designed to deliver messages or signals between SoC and MCU subsystem.

##### Features

- A processor is allow to generate an interrupt for another processor
- Support for a polling word to enable signaling an event from one party to another without the need of interrupts
- Reception of an ACK interrupt indicates that the other party is active
- A processor can wake up another processor (supported)

##### Block Diagram

The architecture of the Mailbox is depicted below.

<img src="static/Mailbox.png" alt="" width="600">

#### GPIO

##### Introduction

K1 provides General-Purpose Input/Output (GPIO) ports for generating and capturing application-specific input and output. These ports are accessed through the alternate function muxing, and the GPIO unit manages their control and status.

##### Features

- A GPIO port configured as an input can also serve as an interrupt source
- At system reset, by default all GPIO ports are configured as an input until changed by the boot process or user software
- Each GPIO port has a dedicated control signal
- Support for separated interrupts over either leading-edge timing or trailing-edge timing or both
- The GPIO port output can be individually set or cleared
- The GPIO port input can be individually read

#### RTC

##### Features

- Count of the number of seconds basing on the internal 1-Hz clock
- Possibility to calibrate the frequency of the internal oscillator
- Support for an alarm interrupt and 1-Hz interrupt

#### Time-Out Monitor

##### Features

- Configurable time-out monitor threshold
- Configurable auto response function for time-out monitor events
- Storage of the address and ID of the first timeout monitor transaction for debugging
- Configurable check for AW/ARREADY signals

### 2.10 Sensor-Hub Subsystem

#### Features

- Support for 1 I2C interface
- Support for 1 SPP interface
- Support for 2 UART interfaces
- Support for 1 CAN interface

### 2.11 Clock & Reset

#### Introduction

K1 comes with the following clocks:

- One 32K RTC clock
- One 24M OSC clock

#### Features

- Three PLLs implemented inside to provide various frequencies to meet different scenario requirements
- DVFS feature supported to balance the tradeoff between power and performance
- Glitch-free clock switches and clock dividers implemented to provide all required frequencies with limited PLLs cost
- Clock gating and software reset schemes applied to modules in fine granularity to achieve power saving and flexible management

#### Block Diagram

##### Clock System

The detailed clock tree structure is depicted below, where is highlighted how the clock signals are generated, managed and distributed across the system to support various modules and functions.

![](static/clock_tree.png)

Instead, the high-level architecture of the clock system is depicted below.

<img src="static/clock_system.png" alt="" width="600">

VCXO_OUT is driven with the OSC frequency if either of the following occurs:

- VCXO_REQ is asserted, and the relevant REQ_EN bit field is set in the VCXO software request control register
- Software request bit field is enabled in the VCXO software request control register

There are three Phase-Locked Loop (PLL) designed to accept a wide range of input frequencies, and generate a broad range of output frequencies to all modules for functioning properly in different application scenario. Details for each PLL are provided in the following subsections.

##### PLL

- **PLL1** is designed to generate fixed frequency points for the CPU cores and other peripherals, where
  - Changes of the run-time frequency in the PLL1 output are only available for debugging purposes and should not be used in production systems
  - PLL1 is enabled by default at system reset and shutdown only when the entire chip entered sleep mode with VCXO shutdown enabled
  - The settings configured in the PLL1 and oscillator control registers of the Main PMU control the delay required for the PLL1 output clocks to stabilize after system reset or shutdown
  - Updating the PLL1 configuration registers to change frequency during normal operations is not recommended

- **PLL2** is designed to generate various fixed frequencies, working alongside PLL1 to provide a full range of frequencies required for different modules, where
  - Changes of run-time frequency in the PLL2 output are only available for debugging purposes and should not be used in production systems
  - PLL2 is disabled at system reset and must be enabled through software when required
  - The settings configured in the PLL2 and oscillator control registers of the Main PMU control the delay required for the PLL2 output clocks to stabilize after system reset or shutdown
  - Updating the PLL2 configuration registers to change frequency during normal operations is not recommended

- **PLL3** is designed to provide frequencies for CPU frequency scaling and switching, where
  - PLL3 is disabled at system reset and must be enabled through software when required
  - The settings configured in the PLL3 and oscillator control register of the Main PMU control the delay required for the PLL3 output clocks to stabilize after system reset or shutdown
  - Updating the PLL3 configuration registers to change frequency during normal operations is not recommended

##### Resource Reset Scheme

K1 allows applying different schemes of resource reset as tabled below.

| No. | Resource Reset Scheme     | Description   |
|-----|----------------------------|------------------|
| 1   | Power-On-Reset             | Reset the whole chip during power-on sequence                   |
| 2   | WatchDog Reset             | Reset the whole chip excluding pinmux registers and debug registers |
| 3   | Module Software Reset      | Reset each module individually through software                 |
| 4   | Power Island POR Reset     | Reset the whole power island during its power-on sequence       |

### 2.12 Boot Modes

#### Introduction

K1 supports booting from

- SPI NAND Flash
- SPI NOR Flash
- eMMC
- SD/TF Card

The details of the boot mode selection are tabled below.

| No. | QSPI_DATA[1] / STRAP[1] | QSPI_DATA[0] / STRAP[0] | Boot Mode                     |
|-----|--------------------------|--------------------------|-------------------------------|
| 1   | Down                     | Down                     | SD/TF Card → EMMC (default)   |
| 2   | Up                       | Down                     | SD/TF Card → SPI NAND Flash   |
| 3   | Down                     | Up                       | SD/TF Card → SPI NOR Flash    |
| 4   | Up                       | Up                       | SD/TF Card                    |

### 2.13 Power Management Unit

#### Introduction

A two-level power management strategy is implemented to control various granularities of power consumption. Different power domains and power states are also defined to achieve ultra-low power consumption.

A total of 9 power domains are implemented, and they are for

- CPU cores

  > **Note.** Each CPU core has its own power domain independently controlled

- CPU clusters

  > **Note.** Each CPU cluster has its own power domain independently controlled

- Video Encoder/Decoder
- GPU
- HDMI Display Subsystem
- MIPI DSI Subsystem
- Video Input Subsystem
- RCPU (including N308, Audio Codec, RCPU Peripherals)
- Always-On-Domain (AON)

All those power domains, except AON, can be powered off depending on specific application scenarios.

In order to achieve the minimal power consumption, different power states are designed as tabled below:

| No. | Power State Name        | Description                                                                                                                                                                                                 |
|-----|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | ACTIVE                   | The system is alive and active, with all power domains on, except those power domains with power switches that can be turned off selectively and independently.                                               |
| 2   | CORE-IDLE                | Each core stops executing instructions and enters an idle state, with clock gating automatically after a Wait-for-Interrupt (WFI) execution. The core exits this state when receiving an interrupt routed to it and continues execution. |
| 3   | Core-Power-Off           | Each core, when voted, enters a power-off state after Core-Idle sleep mode. The core exits this state when receiving an interrupt, with power turned on and reset released.                                   |
| 4   | CPU-Cluster-Power-Off    | Each CPU cluster, when voted, enters this low-power state after all cores within this cluster have entered the Core-Power-Off state, with L2/TCM memory also shut down.<br/>Any active interrupt routing to CPU cores in this cluster would bring CPU cluster out of this state, then power on, clock resume and reset release. |
| 5   | Home-Screen              | The main bus fabric AXI clock is gated off (if voted) after both CPU clusters enter CPU-Cluster-Power-Off mode.<br/>Any interrupt will wake up the chip from this state by resuming the main bus AXI clock, and powering up the corresponding CPU cluster and CPU core to which the interrupt is routed, resuming the CPU clock, and releasing the reset to service the interrupt routine. |
| 6   | Chip-Sleep               | This is the most ultra-low power state, with all PLLs/Power islands off. Only 32K RTC clock remains alive, and the 24M VCXO can be configured to be on or off.<br/>In this state only the logic/IO in AON domain alives, and a pin named SLEEP_OUT connected to PMIC would be deasserted to signal PMIC to lower the VCC power supply voltage to reduce lower power comsumption. |
| 7   | RCPU with SOC LP         | RCPU power domain is an independent power island and can function in any of above PMU states. RCPU can vote for different SoC low-power states according to its specific scenario requirements.<br/>The RCPU itself has four low-power states as follows:<br/>- Active Mode: Clock running<br/>- ClkGate Mode: Clock gating<br/>- PLL Off Mode: PLL powered off<br/>- Power Off Mode: RCPU power is shut down, but the RCPU AON domain remains alive |

> **Note.** VPU, GPU, ISP, DPU power islands can be turned on or off by software, and are independent of the power states **No. 1~5** in the table above

In the **Chip-Sleep low power state** (see **No. 6** in the table above), the following interrupts or events can wake up the chip:

- Pad edge detection
- Keypad press
- RTC/Timer/WDT
- USB/RCPU/AP2AUDIO_IPC
- SD/EMMC/PCIE
- PMIC

In the **RCPU power off state** (see **No. 7** in the table above), the following interrupts or events can wake up RCPU PMU to resume its power supply:

- Audio plug interrupt / Hook key interrupt / Class-G short power interrupt / Audio OCP interrupt
- AP IPC power-on request
- RCPU AON Timer wakeup request
- Sensor-Hub GPIO wakeup request

## 3. Package

### 3.1 Introduction

K1 is available in two packages as tabled below.

| Type   | Size (mm) | Pin Pitch (mm) | Pin Count       |
|--------|-----------|----------------|-----------------|
| FCCSP  | 17×17     | 0.65           | 676 (26×26)     |
| FCBGA  | 19×19     | 0.65           | 676 (26×26)     |

The related package outline drawing (POD) are depicted in the following sections.

### 3.2 FCCSP Type

![](static/POD_1.png)

![](static/POD_2.png)

<img src="static/fccsp00.png" alt="" width="600">

### 3.3 FCBGA Type

![](static/POD_3.png)

<img src="static/fcbga00.png" alt="" width="600">

## 4. Pinout

### 4.1 Pinout Diagram & Description

The overall pinout diagram of K1 is depicted below.

![](static/K1_pinout.png)

> **Note.** Meaning of the different colors:
>
> - Power supplies (different voltages):
>   - Brown
>   - Dark Blue
>   - Grey
>   - Light Blue
>   - Orange
>   - Purple
>   - Red
>   - Yellow
> - Grounds:
>   - Dark Green
>   - Light Green
> - Signals:
>   - White

Let's consider the division into the quadrants

- (A~N, 1~13)
- (A~N, 14~26)
- (M~AF, 1~13)
- (M~AF, 14~26)

in order to provide conveniently the pinout description of K1 in the following subsections.

#### (A~N, 1~13)

![](static/K1_pinout_1.png)

> **Note.** Definition of symbols used for pin type:
>
> - AO = Analog output
> - AI = Analog input
> - AIO = Analog input/output
> - G = Ground
> - I/O = Input/Output
> - P = Power
> - RO = Reference output

| Pin ID       | Name                | Type | Power Domain                          | Function                                                                 |
|--------------|---------------------|------|----------------------------------------|--------------------------------------------------------------------------|
| A1           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| A2           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| A3           | DQ_B_2              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ2 <br/>LPDDR3: DQ28                                      |
| A4           | DMI0_B              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: Channel B DM0 <br/>LPDDR3: DQ25                                |
| A5           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| A6           | DQ_B_6              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ6 <br/>LPDDR3: DQ24                                      |
| A7           | DQ_B_4              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ4 <br/>LPDDR3: DQ30                                      |
| A8           | DQ_B_13             | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ13 <br/>LPDDR3: DQ15                                     |
| A9           | DQ_B_15             | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ15 <br/>LPDDR3: DQ12                                     |
| A10          | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| A11          | DQ_B_9              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ9<br/>LPDDR3: DQ8                                        |
| A12          | DQ_B_12             | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ12<br/>LPDDR3: DQ10                                      |
| A13          | DQ_B_11             | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ11<br/>LPDDR3: DQ11                                      |
| B1           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| B2           | DQ_B_3              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ3<br/>LPDDR3: DQM3                                       |
| B3           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| B4           | DQ_B_1              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ1<br/>LPDDR3: DQ27                                       |
| B5           | DQ_B_0              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ0<br/>LPDDR3: DQ31                                       |
| B6           | DQ_B_7              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ7<br/>LPDDR3: DQ29                                       |
| B7           | DQ_B_5              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ5<br/>LPDDR3: DQ26                                       |
| B8           | VDDQ_V1P2           | P    | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR3 IO power                                                         |
| B9           | DQ_B_14             | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ14<br/>LPDDR3: DQ13                                      |
| B10          | DMI1_B              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: Channel B DM1<br/>LPDDR3: DQ14                                 |
| B11          | DQ_B_8              | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHA DQ12<br/>LPDDR3: DQM1                                      |
| B12          | DQ_B_10             | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB DQ10<br/>LPDDR3: DQ9                                       |
| B13          | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| C1           | GPIO_58             | I/O  | 1.8V                                   | General Purpose I/O 58                                                  |
| C2           | GPIO_57             | I/O  | 1.8V                                   | General Purpose I/O 57                                                  |
| C3           | GPIO_56             | I/O  | 1.8V                                   | General Purpose I/O 56                                                  |
| C4           | GPIO_55             | I/O  | 1.8V                                   | General Purpose I/O 55                                                  |
| C5           | GPIO_54             | I/O  | 1.8V                                   | General Purpose I/O 54                                                  |
| C6           | DQS0_T_B            | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: Positive of CHB DQS0<br/>LPDDR3: Positive of DQS3              |
| C7           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| C8           | CS1_B               | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: Active-low chip select 1 of CHB<br/>LPDDR3: N/A                |
| C9           | CA_B_1              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB CA1<br/>LPDDR3: CA5                                        |
| C10          | CKE0_B              | AO   | lp3: 1.2V<br/>lp4x: 1.1V               | LPDDR4X: clock enabling 0 of CHB<br/>LPDDR3: N/A                        |
| C11          | CKE1_B              | AO   | lp3: 1.2V<br/>lp4x: 1.1V               | LPDDR4X: clock enabling 1 of CHB<br/>LPDDR3: N/A                        |
| C12          | VDDQ_V1P2           | P    | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR3 IO power                                                         |
| C13          | CA_B_5              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB CA5<br/>LPDDR3: CA8                                        |
| D1           | GPIO_114            | I/O  | 1.8V                                   | General Purpose I/O 114                                                 |
| D2           | GPIO_113            | I/O  | 1.8V                                   | General Purpose I/O 113                                                 |
| D3           | GPIO_112            | I/O  | 1.8V                                   | General Purpose I/O 112                                                 |
| D4           | GPIO_111            | I/O  | 1.8V                                   | General Purpose I/O 111                                                 |
| D5           | GPIO_53             | I/O  | 1.8V                                   | General Purpose I/O 53                                                  |
| D6           | DQS0_C_B            | AIO  | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: Negative of CHB DQS0<br/>LPDDR3: Negtive of DQS3               |
| D7           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| D8           | CA_B_0              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB CA0                                                        |
| D9           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| D10          | DDR_lp4x_SEL        | AIO  | 1.8V                                   | LPDDR4X: connect to 1.8V<br/>LP234: connect to Ground                   |
| D11          | CK_C_B              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: negative LPDDR differential clock of CHB <br/>LPDDR3: negative LPDDR differential clock |
| D12          | CA_B_2              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB CA2<br/>LPDDR3: CA9                                        |
| D13          | CA_B_4              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHA CA4<br/>LPDDR3: CA7                                        |
| E1           | GPIO_67             | I/O  | 1.8V                                   | General Purpose I/O 67                                                  |
| E2           | GPIO_65             | I/O  | 1.8V                                   | General Purpose I/O 65                                                  |
| E3           | GPIO_64             | I/O  | 1.8V                                   | General Purpose I/O 64                                                  |
| E4           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| E5           | GPIO_63             | I/O  | 1.8V                                   | General Purpose I/O 63                                                  |
| E6           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| E7           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| E8           | VDDQ_V1P2           | P    | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR3 IO power                                                         |
| E9           | DDR_LP23_VREFDQ     | P    | lp3: 0.6V<br/>lp4: high-z              | DQ VREF for lpddr23 , LP4/4x<br/>Keep the pin NC                        |
| E10          | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| E11          | CK_T_B              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: positive LPDDR differential clock of CHB<br/>LPDDR3: positive LPDDR differential clock |
| E12          | CA_B_3              | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: CHB CA3 <br/>LPDDR3: CA6                                       |
| E13          | AVSS18_DDR          | G    | 0V                                     | DDR Ground                                                              |
| F1           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| F2           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| F3           | GPIO_69             | I/O  | 1.8V                                   | General Purpose I/O 69                                                  |
| F4           | GPIO_68             | I/O  | 1.8V                                   | General Purpose I/O 68                                                  |
| F5           | GPIO_66             | I/O  | 1.8V                                   | General Purpose I/O 66                                                  |
| F6           | VCC18_GPIO          | P    | 1.8V                                   | GPIO1/4/5/PMIC I/O power                                                |
| F7           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| F8           | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| F9           | VDDQ_V1P2           | P    | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR3 IO power                                                         |
| F10          | VDDQ_V1P2           | P    | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR3 IO power                                                         |
| F11          | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| F12          | CS0_B               | AO   | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR4X: clock enabling 1 of CHB<br/>LPDDR3: N/A                        |
| F13          | DDR_RESET_N         | AO   | lp3: 1.2V<br/>lp4x: 1.1V               | LPDDR SDRAM reset                                                       |
| G1           | MIPI_CSI1_D1N       | AI   | 1.8V                                   | CSI1 DATA1LANEN                                                         |
| G2           | MIPI_CSI1_D1P       | AI   | 1.8V                                   | CSI1 DATA1LANEP                                                         |
| G3           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| G4           | MIPI_CSI1_D0N       | AI   | 1.8V                                   | CSI1 DATA0LANEN                                                         |
| G5           | MIPI_CSI1_D0P       | AI   | 1.8V                                   | CSI1 DATA0LANEP                                                         |
| G6           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| G7           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| G8           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| G9           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| G10          | VSSQ_DDR            | G    | 0V                                     | DDR Ground                                                              |
| G11          | VDDQ_V1P2           | P    | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR3 IO power                                                         |
| G12          | AVDD11_DDR          | P    | lp4x: 1.1V<br/>lp4: 1.1V<br/>lp3: 1.2V | LPDDR PHY power supply                                                  |
| G13          | VDDQ_V1P2           | P    | lp3: 1.2V<br/>lp4x: 0.6V               | LPDDR3 IO power                                                         |
| H1           | MIPI_CSI1_D2N       | AI   | 1.8V                                   | CSI1 DATA2LANEN                                                         |
| H2           | MIPI_CSI1_D2P       | AI   | 1.8V                                   | CSI1 DATA2LANEP                                                         |
| H3           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| H4           | MIPI_CSI1_CLKN      | AO   | 1.8V                                   | CSI1 CKLANEN                                                            |
| H5           | MIPI_CSI1_CLKP      | AO   | 1.8V                                   | CSI1 CKLANEP                                                            |
| H6           | AVSS18_AFEAP        | G    | 0V                                     | DCXO Ground                                                             |
| H7           | XI_PAD              | AI   | 1.8V                                   | DCXO crystal input                                                      |
| H8           | AVSS18_AFEAP        | G    | 0V                                     | DCXO Ground                                                             |
| H9           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| H10          | VSSU_DDR            | G    | 0V                                     | system DDR Ground                                                       |
| H11          | VSSU_DDR            | G    | 0V                                     | system DDR Ground                                                       |
| H12          | AVDD18_PHY          | P    | 1.8V                                   | Analog 1.8V power                                                       |
| H13          | AVDDU_DDR           | P    | 0.9V                                   | LPDDR PHY PLL logical power                                             |
| J1           | MIPI_CSI3_D0N       | AI   | 1.8V                                   | CSI3 DATA0LANEN                                                         |
| J2           | MIPI_CSI3_D0P       | AI   | 1.8V                                   | CSI3 DATA0LANEP                                                         |
| J3           | AVSS_CSI            | G    | 0V                                     | MIPI_CSI Ground                                                         |
| J4           | MIPI_CSI1_D3N       | AI   | 1.8V                                   | CSI1 DATA3LANEN                                                         |
| J5           | MIPI_CSI1_D3P       | AI   | 1.8V                                   | CSI1 DATA3LANEP                                                         |
| J6           | AVSS_CSI            | G    | 0V                                     | MIPI_CSI Ground                                                         |
| J7           | XO_PAD              | AO   | 1.8V                                   | DCXO crystal output                                                     |
| J8           | AVSS18_AFEAP        | G    | 0V                                     | DCXO Ground                                                             |
| J9           | AVSS18_AFEAP        | G    | 0V                                     | DCXO Ground                                                             |
| J10          | VCC_M1              | P    | 0.9V                                   | Digital Core power                                                      |
| J11          | AVDDU_PHY           | P    | 0.9V                                   | LPDDR PHY core logical power                                            |
| J12          | AVDDU_PHY           | P    | 0.9V                                   | LPDDR PHY core logical power                                            |
| J13          | AVDDU_PHY           | P    | 0.9V                                   | LPDDR PHY core logical power                                            |
| K1           | MIPI_CSI3_CLKN      | AO   | 1.8V                                   | CSI3 CKLANEN for CSI3 DATALANE0/1 when CSI3 is configured as two 2ch CSI; <br/>CSI3 CKLANEN for CSI3 DATALANE0/1/2/3 when CSI3 is configured as 4ch CSI |
| K2           | MIPI_CSI3_CLKP      | AO   | 1.8V                                   | CSI3 CKLANEP for CSI3 DATALANE0/1 when CSI3 is configured as two 2ch CSI; <br/>CSI3 CKLANEP for CSI3 DATALANE0/1/2/3 when CSI3 is configured as 4ch CSI |
| K3           | AVSS_CSI            | G    | 0V                                     | MIPI_CSI Ground                                                         |
| K4           | MIPI_CSI3_D1N       | AI   | 1.8V                                   | CSI3 DATA1LANEN                                                         |
| K5           | MIPI_CSI3_D1P       | AI   | 1.8V                                   | CSI3 DATA1LANEP                                                         |
| K6           | AVDD18_CSI          | P    | 1.8V                                   | MIPI_CSI analog power                                                   |
| K7           | AVDD09_CSI          | P    | 0.9V                                   | MIPI_CSI digtial power                                                  |
| K8           | AVSS_CSI            | G    | 0V                                     | MIPI_CSI Ground                                                         |
| K9           | VCC_M1              | P    | 0.9V                                   | Digital Core power                                                      |
| K10          | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| K11          | BG_OUT              | AO   | 1.8V                                   | Bandgap output                                                          |
| K12          | AVDD18_AFEAP        | P    | 1.8V                                   | 1.8V power for DCXO                                                     |
| K13          | MPLL_TST_CK         | AIO  | 1.8V                                   | Analog testpin                                                          |
| L2           | MIPI_CSI3_D2P       | AI   | 1.8V                                   | CSI3 DATA2LANEP                                                         |
| L3           | AVSS_CSI            | G    | 0V                                     | MIPI_CSI Ground                                                         |
| L4           | MIPI_CSI2_CLKN      | AO   | 1.8V                                   | CKLANEN for CSI3 DATALANE2/3 when CSI3 is configured as two 2ch CSI; <br/>Disabled when CSI3 is configured as 4ch CSI |
| L5           | MIPI_CSI2_CLKP      | AO   | 1.8V                                   | CKLANEP for CSI3 DATALANE2/3 when CSI3 is configured as two 2ch CSI; <br/>Disabled when CSI3 is configured as 4ch CSI |
| L6           | AVDD18_CSI          | P    | 1.8V                                   | MIPI_CSI analog power                                                   |
| L7           | AVDD09_CSI          | P    | 0.9V                                   | MIPI_CSI digtial power                                                  |
| L8           | AVSS_CSI            | G    | 0V                                     | MIPI_CSI Ground                                                         |
| L9           | AVSS_CSI            | G    | 0V                                     | MIPI_CSI Ground                                                         |
| L10          | VCC_M1              | P    | 0.9V                                   | Digital Core power                                                      |
| L11          | AVDD09_AFEAP        | P    | 0.9V                                   | 0.9V power for DCXO                                                     |
| L12          | VSSU_AFEAP          | G    | 0V                                     | DCXO Ground                                                             |
| L13          | AVSS_PLL            | G    | 0V                                     | Analog Core Ground                                                      |
| M1           | MIPI_CSI3_D3N       | AI   | 1.8V                                   | CSI3 DATA3LANEN                                                         |
| M2           | MIPI_CSI3_D3P       | AI   | 1.8V                                   | CSI3 DATA3LANEP                                                         |
| M3           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| M4           | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| M5           | VSSU_PCIEA          | G    | 0V                                     | PCIEA Ground                                                            |
| M6           | AVDD18_USB          | P    | 1.8V                                   | USB2.0 1.8V power                                                       |
| M7           | AVDD09_USB          | P    | 0.9V                                   | USB2.0 digital power                                                    |
| M8           | VSSU_PCIEA          | G    | 0V                                     | PCIEA Ground                                                            |
| M9           | AVDD33_USB          | P    | 3.3V                                   | USB2.0 3.3V power                                                       |
| M10          | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| M11          | AVDD09_PLL          | P    | 0.9                                    | System PLL power supply                                                 |
| M12          | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| M13          | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| N1           | USB2_DN             | AIO  | 3.3V                                   | USB2.0_2 D- differential data line                                      |
| N2           | USB2_DP             | AIO  | 3.3V                                   | USB2.0_2 D+ differential data line                                      |
| N3           | AVSS_USB            | G    | 0V                                     | USB2.0 Ground                                                           |
| N4           | PCIEA_TXN           | AO   | 1.8V                                   | PCIEA TXLANEN                                                           |
| N5           | PCIEA_TXP           | AO   | 1.8V                                   | PCIEA TXLANEP                                                           |
| N6           | AVDD18_PCIEA        | P    | 1.8V                                   | PCIEA analog power                                                      |
| N7           | AVDD09_PCIEA        | P    | 0.9V                                   | PCIEA digital power                                                     |
| N8           | AVSS_PCIEA          | G    | 0V                                     | PCIEA Ground                                                            |
| N9           | AVDD33_USB          | P    | 3.3V                                   | USB2.0 3.3V power                                                       |
| N10          | VCC_M1              | P    | 0.9V                                   | Digital Core power                                                      |
| N11          | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |
| N12          | VCC_M1              | P    | 0.9V                                   | Digital Core power                                                      |
| N13          | VSS                 | G    | 0V                                     | Digital Core Ground                                                     |

#### (A~N, 14~26)

![](static/K1_pinout_2.png)

> **Note.** Definition of symbols used for pin type:
>
> - AO = Analog output
> - AI = Analog input
> - AIO = Analog input/output
> - G = Ground
> - I/O = Input/Output
> - P = Power
> - RO = Reference output

| Pin ID       | Name            | Type | Power Domain                     | Function                                                                 |
|--------------|-----------------|------|----------------------------------|--------------------------------------------------------------------------|
| A14          | DQS1_C_B        | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Negative of CHB DQS1<br/>LPDDR3: Negtive of DQS1                |
| A15          | DQS1_C_A        | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Negative of CHA DQS1<br/>LPDDR3: Negtive of DQS0                |
| A16          | DQ_A_12         | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ12<br/>LPDDR3: DQM0                                       |
| A17          | DQ_A_9          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ9<br/>LPDDR3: DQ7                                         |
| A18          | DQ_A_8          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHB DQ8<br/>LPDDR3: DQ5                                         |
| A19          | DQ_A_15         | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHB DQ15<br/>LPDDR3: DQ3                                        |
| A20          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| A21          | DQ_A_5          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ5<br/>LPDDR3: DQ21                                        |
| A22          | DQ_A_7          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ7<br/>LPDDR3: DQ17                                        |
| A23          | DMI0_A          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Channel A DM0<br/>LPDDR3: DQ22                                  |
| A24          | DQ_A_1          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ1<br/>LPDDR3: DQ16                                        |
| A25          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| A26          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| B14          | DQS1_T_B        | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Positive of CHB DQS1<br/>LPDDR3: Positive of DQS1               |
| B15          | DQS1_T_A        | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Positive of CHA DQS1<br/>LPDDR3: Positive of DQS0               |
| B16          | DQ_A_11         | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ11<br/>LPDDR3: DQ4                                        |
| B17          | DQ_A_10         | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ10<br/>LPDDR3: DQ6                                        |
| B18          | DMI1_A          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Channel A DM1<br/>LPDDR3: DQ2                                   |
| B19          | DQ_A_14         | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ14<br/>LPDDR3: DQ1                                        |
| B20          | DQ_A_13         | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ13<br/>LPDDR3: DQ0                                        |
| B21          | DQ_A_4          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHB DQ4<br/>LPDDR3: DQ18                                        |
| B22          | DQ_A_6          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHB DQ6<br/>LPDDR3: DQ23                                        |
| B23          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| B24          | DQ_A_2          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ2<br/>LPDDR3: DQ19                                        |
| B25          | DQ_A_3          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHB DQ3<br/>LPDDR3: DQM2                                        |
| B26          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| C14          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| C15          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| C16          | CA_A_4          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA CA4<br/>LPDDR3: CA3                                         |
| C17          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| C18          | CKE1_A          | AO   | lp3: 1.2V<br/>lp4x: 1.1V         | LPDDR4X: clock enabling 1 of CHA<br/>LPDDR3: clock enabling 1            |
| C19          | CA_A_1          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA CA1<br/>LPDDR3: CA2                                         |
| C20          | CS1_A           | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Active-low chip select 1 of CHA<br/>LPDDR3: Active-low chip select 1 |
| C21          | AVDD06_DDR      | P    | lp4x: 0.6V<br/>lp4: TBD/lp3: TBD | LPDDR4X IO power                                                         |
| C22          | DQ_A_0          | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA DQ0<br/>LPDDR3: DQ20                                        |
| C23          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| C24          | EMMC_DS         | I/O  | 1.8V                             | eMMC data strobe                                                         |
| C25          | EMMC_D7         | I/O  | 1.8V                             | eMMC data7                                                               |
| C26          | EMMC_D2         | I/O  | 1.8V                             | eMMC data2                                                               |
| D14          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| D15          | AVDD06_DDR      | P    | lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD | LPDDR4X IO power                                                     |
| D16          | CA_A_2          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA CA2                                                         |
| D17          | CK_C_A          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: negative LPDDR differential clock of CHA<br/>LPDDR3: N/A        |
| D18          | CKE0_A          | AO   | lp3: 1.2V<br/>lp4x: 1.1V         | LPDDR4X: clock enabling 0 of CHA<br/>LPDDR3: clock enabling 0            |
| D19          | CA_A_0          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA CA0<br/>LPDDR3: CA4                                         |
| D20          | DQS0_T_A        | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Positive of CHA DQS0<br/>LPDDR3: Positive of DQS2               |
| D21          | DQS0_C_A        | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Negative of CHA DQS0<br/>LPDDR3: Negative of DQS2               |
| D22          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| D23          | EMMC_D4         | I/O  | 1.8V                             | eMMC data4                                                               |
| D24          | EMMC_D1         | I/O  | 1.8V                             | eMMC data1                                                               |
| D25          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| D26          | EMMC_D0         | I/O  | 1.8V                             | eMMC data0                                                               |
| E14          | AVDD18_DDR      | P    | 1.8V                             | LPDDR PHY PLL 1.8V power                                                 |
| E15          | CA_A_5          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA CA5<br/>LPDDR3: CA1                                         |
| E16          | CS0_A           | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: Active-low chip select 0 of CHA<br/>LPDDR3: Active-low chip select 0 |
| E17          | CK_T_A          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: positive LPDDR differential clock of CHA<br/>LPDDR3: N/A        |
| E18          | AVDD06_DDR      | P    | lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD | LPDDR4X IO power                                                     |
| E19          | AVDD06_DDR      | P    | lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD | LPDDR4X IO power                                                     |
| E20          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| E21          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| E22          | EMMC_D6         | I/O  | 1.8V                             | eMMC data6                                                               |
| E23          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| E24          | EMMC_CLK        | I/O  | 1.8V                             | eMMC Clock                                                               |
| E25          | EMMC_D3         | I/O  | 1.8V                             | eMMC data3                                                               |
| E26          | EMMC_D5         | I/O  | 1.8V                             | eMMC data5                                                               |
| F14          | ZQ_DDR_PHY      | AIO  | lp3: 1.2V<br/>lp4x: 0.6V         | DDR ZQ calibration                                                       |
| F15          | CA_A_3          | AO   | lp3: 1.2V<br/>lp4x: 0.6V         | LPDDR4X: CHA CA3<br/>LPDDR3: CA0                                         |
| F16          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| F17          | DDR_LDO_CAP     | RO   | 0.7~0.9V                         | External LDO output ball;<br/>Connect to a 100nF capacitor on PCB board  |
| F18          | AVDD06_DDR      | P    | lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD | LPDDR4X IO power                                                     |
| F19          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| F20          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| F21          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| F22          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| F23          | QSPI_DAT2       | I/O  | 1.8V/3.3V                        | QSPI data2                                                               |
| F24          | QSPI_DAT1       | I/O  | 1.8V/3.3V                        | QSPI data1                                                               |
| F25          | EMMC_CMD        | I/O  | 1.8V                             | eMMC command                                                             |
| F26          | QSPI_DAT0       | I/O  | 1.8V/3.3V                        | QSPI data0                                                               |
| G14          | DDR_LP23_VREFCA | P    | lp3: 0.6V<br/>lp4: high-z        | CA VREF for lpddr23, LP4/4x<br/>Keep the pin NC                          |
| G15          | AVDD11_DDR      | P    | lp4x: 1.1V<br/>lp4: 1.1V<br/>lp3: 1.2V | LPDDR PHY power supply                                               |
| G16          | AVDD06_DDR      | P    | lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD | LPDDR4X IO power                                                     |
| G17          | VSSQ_DDR        | G    | 0V                               | DDR Ground                                                               |
| G18          | AVDD18_EFUSE    | P    | 1.8V                             | ANAGRP                                                                   |
| G19          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| G20          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| G21          | AVSS_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| G22          | QSPI_DAT3       | I/O  | 1.8V/3.3V                        | QSPI data3                                                               |
| G23          | QSPI_CLK        | I/O  | 1.8V/3.3V                        | QSPI CLK                                                                 |
| G24          | QSPI_CS1        | I/O  | 1.8V/3.3V                        | QSPI CS                                                                  |
| G25          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| G26          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| H14          | AVSSU_DDR       | G    | 0V                               | DDR Ground                                                               |
| H15          | AVDD18_PHY      | P    | 1.8V                             | Analog 1.8V power                                                        |
| H16          | VSSU_DDR        | G    | 0V                               | System DDR Ground                                                        |
| H17          | VSSU_DDR        | G    | 0V                               | System DDR Ground                                                        |
| H18          | VSSU_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| H19          | AVDD18_EMMC     | P    | 1.8V                             | eMMC analog power                                                        |
| H20          | AVDD09_EMMC     | P    | 0.9V                             | eMMC digtial power                                                       |
| H21          | VCC1833_QSPI    | P    | 1.8V/3.3V                        | QSPI IO power                                                            |
| H22          | PCIEC_TX0P      | AO   | 1.8V                             | PCIEC TX0LANEP                                                           |
| H23          | PCIEC_TX0N      | AO   | 1.8V                             | PCIEC TX0LANEN                                                           |
| H24          | AVSS_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| H25          | PCIEC_RX0P      | AI   | 1.8V                             | PCIEC RX0LANEP                                                           |
| H26          | PCIEC_RX0N      | AI   | 1.8V                             | PCIEC RX0LANEN                                                           |
| J14          | AVDDU_PHY       | P    | 0.9V                             | LPDDR PHY core logical power                                             |
| J15          | AVDDU_PHY       | P    | 0.9V                             | LPDDR PHY core logical power                                             |
| J16          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| J17          | VCC_M1          | P    | 0.9V                             | Digital Core power                                                       |
| J18          | VSSU_EMMC       | G    | 0V                               | eMMC Ground                                                              |
| J19          | QSPI_VCC_CAP    | RO   | 1.8V                             | QSPI 1.8V LDO cap                                                        |
| J20          | AVDD09_EMMC     | P    | 0.9V                             | eMMC digtial power                                                       |
| J21          | AVSS_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| J22          | PCIEC_REFCLK_P  | AIO  | 1.8V                             | PCIEC CKLANEP                                                            |
| J23          | PCIEC_REFCLK_N  | AIO  | 1.8V                             | PCIEC CKLANEN                                                            |
| J24          | AVSS_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| J25          | PCIEC_RX1P      | AI   | 1.8V                             | PCIEC RX1LANEP                                                           |
| J26          | PCIEC_RX1N      | AI   | 1.8V                             | PCIEC RX1LANEN                                                           |
| K14          | AVDD18_PLL      | P    | 1.8                              | System PLL power supply                                                  |
| K15          | VCC_M1          | P    | 0.9V                             | Digital Core power                                                       |
| K16          | VSS             | G    | 0V                               | Digital core Ground                                                      |
| K17          | VCC_M1          | P    | 0.9V                             | Digital Core power                                                       |
| K18          | VSSU_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| K19          | VSSU_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| K20          | AVDD09_PCIEC    | P    | 0.9V                             | PCIEC digital power                                                      |
| K21          | AVSS_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| K22          | PCIEC_TX1P      | AO   | 1.8V                             | PCIEC TX1LANEP                                                           |
| K23          | PCIEC_TX1N      | AO   | 1.8V                             | PCIEC TX1LANEN                                                           |
| K24          | AVSS_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| K25          | PCIEB_RX0P      | AI   | 1.8V                             | PCIEB RX0LANEP                                                           |
| K26          | PCIEB_RX0N      | AI   | 1.8V                             | PCIEB RX0LANEN                                                           |
| L14          | VSSU_PLL        | G    | 0V                               | System PLL Ground                                                        |
| L15          | VSS             | G    | 0V                               | Digital core Ground                                                      |
| L16          | VCC_M1          | P    | 0.9V                             | Digital Core power                                                       |
| L17          | VSSU_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| L18          | VSSU_PCIEC      | G    | 0V                               | PCIEC Ground                                                             |
| L19          | AVDD18_PCIEC    | P    | 1.8V                             | PCIEC analog power                                                       |
| L20          | AVDD09_PCIEB    | P    | 0.9V                             | PCIEB digital power                                                      |
| L21          | AVDD09_PCIEB    | P    | 0.9V                             | PCIEB digital power                                                      |
| L22          | PCIEB_TX0P      | AO   | 1.8V                             | PCIEB TX0LANEP                                                           |
| L23          | PCIEB_TX0N      | AO   | 1.8V                             | PCIEB TX0LANEN                                                           |
| L24          | AVSS_PCIEB      | G    | 0V                               | PCIEB Ground                                                             |
| L25          | PCIEB_REFCLK_P  | AIO  | 1.8V                             | PCIEB CKLANEP                                                            |
| L26          | PCIEB_REFCLK_N  | AIO  | 1.8V                             | PCIEB CKLANEN                                                            |
| M14          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| M15          | VCC_M1          | P    | 0.9V                             | Digital Core power                                                       |
| M16          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| M17          | VSSU_PCIEB      | G    | 0V                               | PCIEB Ground                                                             |
| M18          | VSSU_PCIEB      | G    | 0V                               | PCIEB Ground                                                             |
| M19          | AVDD18_PCIEB    | P    | 1.8V                             | PCIEB analog power                                                       |
| M20          | AVSS_PCIEB      | G    | 0V                               | PCIEB Ground                                                             |
| M21          | AVSS_PCIEB      | G    | 0V                               | PCIEB Ground                                                             |
| M22          | PCIEB_TX1P      | AO   | 1.8V                             | PCIEB TX1LANEP                                                           |
| M23          | PCIEB_TX1N      | AO   | 1.8V                             | PCIEB TX1LANEN                                                           |
| M24          | AVSS_PCIEB      | G    | 0V                               | PCIEB Ground                                                             |
| M25          | PCIEB_RX1P      | AI   | 1.8V                             | PCIEB RX1LANEP                                                           |
| M26          | PCIEB_RX1N      | AI   | 1.8V                             | PCIEB RX1LANEN                                                           |
| N14          | VCC_M1          | P    | 0.9V                             | Digital Core power                                                       |
| N15          | VSS             | G    | 0V                               | Digital Core Ground                                                      |
| N16          | VCC_M1          | P    | 0.9V                             | Digital Core power                                                       |
| N17          | AVSS18_AUD      | G    | 0V                               | Audio Ground                                                             |
| N18          | AVDD3V3_AUD     | P    | 3.3V                             | 3.3V power for earphone driver                                           |
| N19          | AVSS18_AUD      | G    | 0V                               | Audio Ground                                                             |
| N20          | AVSS18_AUD      | G    | 0V                               | Audio Ground                                                             |
| N21          | NA              | P    | 1.8V                             | NA                                                                       |
| N22          | NA              | P    | -1.8V                            | NA                                                                       |
| N23          | NA              | AO   | +/-1.8V                          | NA                                                                       |
| N24          | NA              | AO   | +/-1.8V                          | NA                                                                       |
| N25          | NA              | AO   | 3.3V                             | NA                                                                       |
| N26          | NA              | AO   | 3.3V                             | NA                                                                       |

#### (P~AF, 1~13)

![](static/K1_pinout_3.png)

> **Note.** Definition of symbols used for pin type:
>
> - AO = Analog output
> - AI = Analog input
> - AIO = Analog input/output
> - G = Ground
> - I/O = Input/Output
> - P = Power
> - RO = Reference output

| Pin ID | Name                | Type | Power Domain   | Function                                |
|--------|---------------------|------|----------------|-----------------------------------------|
| P1     | PCIEA_RXN           | AI   | 1.8V           | PCIEA RXLANEN                           |
| P2     | PCIEA_RXP           | AI   | 1.8V           | PCIEA RXLANEP                           |
| P3     | AVSS_USB            | G    | 0V             | USB2.0 Ground                           |
| P4     | PCIEA_R_EXT         | AO   | 1.8V           | PCIEA External calibration resistor     |
| P5     | AVSS_USB            | G    | 0V             | USB2.0 Ground                           |
| P6     | AVDD18_USB          | P    | 1.8V           | USB2.0 1.8V power                       |
| P7     | AVDD09_USB          | P    | 0.9V           | USB2.0 digital power                    |
| P8     | AVDD09_USB          | P    | 0.9V           | USB2.0 digital power                    |
| P9     | AVDD33_USB          | P    | 3.3V           | USB2.0 3.3V power                       |
| P10    | VSS                 | G    | 0V             | Digital Core Ground                     |
| P11    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| P12    | VSS                 | G    | 0V             | Digital Core Ground                     |
| P13    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| R1     | PCIEA_REFCLK_N      | AIO  | 1.8V           | PCIEA CKLANEN                           |
| R2     | PCIEA_REFCLK_P      | AIO  | 1.8V           | PCIEA CKLANEP                           |
| R3     | VSS                 | G    | 0V             | Digital core Ground                     |
| R4     | USB1_DN             | AIO  | 3.3V           | USB2.0_1 D- differential data line      |
| R5     | USB1_DP             | AIO  | 3.3V           | USB2.0_1 D+ differential data line      |
| R6     | AVDD18_DSI1         | P    | 1.8V           | DSI analog power                        |
| R7     | AVSS_USB            | G    | 0V             | USB2.0 Ground                           |
| R8     | VSS                 | G    | 0V             | Digital Core Ground                     |
| R9     | VSS                 | G    | 0V             | Digital Core Ground                     |
| R10    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| R11    | VSS                 | G    | 0V             | Digital Core Ground                     |
| R12    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| R13    | VSS                 | G    | 0V             | Digital Core Ground                     |
| T1     | MIPI_DSI1_D3N       | AO   | 1.2V           | DSI DATA3LANEN                          |
| T2     | MIPI_DSI1_D3P       | AO   | 1.2V           | DSI DATA3LANEP                          |
| T3     | VSS                 | G    | 0V             | Digital core ground                     |
| T4     | USB0_DN             | AIO  | 3.3V           | USB2.0_0 D- differential data line      |
| T5     | USB0_DP             | AIO  | 3.3V           | USB2.0_0 D+ differential data line      |
| T6     | VSS                 | G    | 0V             | Digital core ground                     |
| T7     | AVDD09_DSI1         | P    | 0.9V           | DSI digital power                       |
| T8     | AVDD12_DSI1         | P    | 1.2V           | DSI driver power                        |
| T9     | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| T10    | VSS                 | G    | 0V             | Digital Core ground                     |
| T11    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| T12    | VSS                 | G    | 0V             | Digital Core ground                     |
| T13    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| U1     | MIPI_DSI1_D2N       | AO   | 1.2V           | DSI DATA2LANEN                          |
| U2     | MIPI_DSI1_D2P       | AO   | 1.2V           | DSI DATA2LANEP                          |
| U3     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| U4     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| U5     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| U6     | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| U7     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| U8     | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| U9     | VSS                 | G    | 0V             | Digital Core ground                     |
| U10    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| U11    | VSS                 | G    | 0V             | Digital Core ground                     |
| U12    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| U13    | VSS                 | G    | 0V             | Digital Core ground                     |
| V1     | MIPI_DSI1_CLKN      | AO   | 1.2V           | DSI CKLANEN                             |
| V2     | MIPI_DSI1_CLKP      | AO   | 1.2V           | DSI CKLANEP                             |
| V3     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| V4     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| V5     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| V6     | AVSS_DSI1           | G    | 0V             | DSI Ground                              |
| V7     | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| V8     | VSS                 | G    | 0V             | Digital Core ground                     |
| V9     | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| V10    | VSS                 | G    | 0V             | Digital Core ground                     |
| V11    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| V12    | VSS                 | G    | 0V             | Digital Core ground                     |
| V13    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| W1     | VSS                 | G    | 0V             | Digital Core ground                     |
| W2     | VSS                 | G    | 0V             | Digital Core ground                     |
| W3     | VSS                 | G    | 0V             | Digital Core ground                     |
| W4     | MIPI_DSI1_D1N       | AO   | 1.2V           | DSI DATA1LANEN                          |
| W5     | MIPI_DSI1_D1P       | AO   | 1.2V           | DSI DATA1LANEP                          |
| W6     | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| W7     | VSS                 | G    | 0V             | Digital Core ground                     |
| W8     | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| W9     | VSS                 | G    | 0V             | Digital Core ground                     |
| W10    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| W11    | VSS                 | G    | 0V             | Digital Core ground                     |
| W12    | VCC_M1              | P    | 0.9V           | Digital Core power                      |
| W13    | GPIO3_VCC_CAP       | RO   | 1.8V           | GPIO3 1.8V LDO cap                      |
| Y1     | PRI_TRST_N          | I/O  | 1.8V           | JTAG reset                              |
| Y2     | GPIO_74             | I/O  | 1.8V           | General Purpose I/O 74                  |
| Y3     | VSS                 | G    | 0V             | Digital Core ground                     |
| Y4     | MIPI_DSI1_D0N       | AO   | 1.2V           | DSI DATA0LANEN                          |
| Y5     | MIPI_DSI1_D0P       | AO   | 1.2V           | DSI DATA0LANEP                          |
| Y6     | VSS                 | G    | 0V             | Digital Core ground                     |
| Y7     | AVDD33_HDMI         | P    | 3.3V           | HDMI 3.3V power                         |
| Y8     | AVDD33_HDMI         | P    | 3.3V           | HDMI 3.3V power                         |
| Y9     | AVDD09_HDMI         | P    | 0.9V           | HDMI digtial power                      |
| Y10    | AVDD09_HDMI         | P    | 0.9V           | HDMI digtial power                      |
| Y11    | VSS                 | G    | 0V             | Digital Core ground                     |
| Y12    | VSS                 | G    | 0V             | Digital Core ground                     |
| Y13    | VSS                 | G    | 0V             | Digital Core ground                     |
| AA1    | PRI_TCK             | I/O  | 1.8V           | JTAG clock                              |
| AA2    | PRI_TDO             | I/O  | 1.8V           | JTAG output data                        |
| AA3    | VSS                 | G    | 0V             | Digital Core ground                     |
| AA4    | VSS                 | G    | 0V             | Digital Core ground                     |
| AA5    | VSS                 | G    | 0V             | Digital Core ground                     |
| AA6    | VSS                 | G    | 0V             | Digital Core ground                     |
| AA7    | AVSS_HDMI           | G    | 0V             | HDMI Ground                             |
| AA8    | HDMI_TX2N           | AO   | 1.8V           | HDMI data2n                             |
| AA9    | AVDD18_HDMI         | P    | 1.8V           | HDMI 1.8V power                         |
| AA10   | AVDD18_HDMI         | P    | 1.8V           | HDMI 1.8V power                         |
| AA11   | VSS                 | G    | 0V             | Digital Core ground                     |
| AA12   | VSS                 | G    | 0V             | Digital Core ground                     |
| AA13   | VCC1833_GPIO3       | P    | 1.8V/3.3V      | GPIO3 IO power                          |
| AB1    | PRI_TDI             | I/O  | 1.8V           | JTAG input data                         |
| AB2    | PRI_TMS             | I/O  | 1.8V           | JTAG mode selection                     |
| AB3    | VSS                 | G    | 0V             | Digital Core ground                     |
| AB4    | HDMI_TXCN           | AO   | 1.8V           | HDMI clkn                               |
| AB5    | HDMI_TX0N           | AO   | 1.8V           | HDMI data0n                             |
| AB6    | AVSS_HDMI           | G    | 0V             | HDMI Ground                             |
| AB7    | HDMI_TX1N           | AO   | 1.8V           | HDMI data1n                             |
| AB8    | HDMI_TX2P           | AO   | 1.8V           | HDMI data2p                             |
| AB9    | AVSS_HDMI           | G    | 0V             | HDMI Ground                             |
| AB10   | VSS                 | G    | 0V             | Digital Core ground                     |
| AB11   | VSS                 | G    | 0V             | Digital Core ground                     |
| AB12   | VSS                 | G    | 0V             | Digital Core ground                     |
| AB13   | GPIO_51             | I/O  | 1.8V/3.3V      | General purpose I/O 51                  |
| AC1    | GPIO_61             | I/O  | 1.8V           | General Purpose I/O 61                  |
| AC2    | GPIO_62             | I/O  | 1.8V           | General Purpose I/O 62                  |
| AC3    | VCC18_GPIO          | P    | 1.8V           | GPIO1/4/5/PMIC I/O power                |
| AC4    | HDMI_TXCP           | AO   | 1.8V           | HDMI clkp                               |
| AC5    | HDMI_TX0P           | AO   | 1.8V           | HDMI data0p                             |
| AC6    | AVSS_HDMI           | G    | 0V             | HDMI Ground                             |
| AC7    | HDMI_TX1P           | AO   | 1.8V           | HDMI data1p                             |
| AC8    | AVSS_HDMI           | G    | 0V             | HDMI Ground                             |
| AC9    | AVSS_HDMI           | G    | 0V             | HDMI Ground                             |
| AC10   | GPIO_86             | I/O  | 1.8V           | General Purpose I/O 86                  |
| AC11   | VCC18_GPIO          | P    | 1.8V           | GPIO1/4/5/PMIC I/O power                |
| AC12   | GPIO_52             | I/O  | 1.8V/3.3V      | General Purpose I/O 52                  |
| AC13   | GPIO_47             | I/O  | 1.8V/3.3V      | General Purpose I/O 47                  |
| AD1    | GPIO_59             | I/O  | 1.8V           | General Purpose I/O 59                  |
| AD2    | GPIO_60             | I/O  | 1.8V           | General Purpose I/O 60                  |
| AD3    | VSS                 | G    | 0V             | Digital Core ground                     |
| AD4    | VSS                 | G    | 0V             | Digital Core ground                     |
| AD5    | VSS                 | G    | 0V             | Digital Core ground                     |
| AD6    | VSS                 | G    | 0V             | Digital Core ground                     |
| AD7    | VSS                 | G    | 0V             | Digital Core ground                     |
| AD8    | GPIO_87             | I/O  | 1.8V           | General Purpose I/O 87                  |
| AD9    | GPIO_85             | I/O  | 1.8V           | General Purpose I/O 85                  |
| AD10   | PMIC_INT_N          | I/O  | 1.8V           | PMIC interrupt                          |
| AD11   | VCC18_GPIO          | P    | 1.8V           | GPIO1/4/5/PMIC I/O power                |
| AD12   | GPIO_50             | I/O  | 1.8V/3.3V      | General Purpose I/O 50                  |
| AD13   | GPIO_48             | I/O  | 1.8V/3.3V      | General Purpose I/O 48                  |
| AE1    | VSS                 | G    | 0V             | Digital Core ground                     |
| AE2    | MPLL_TST_AD         | AIO  | 1.8V           | Analog testpin                          |
| AE3    | VSS                 | G    | 0V             | Digital Core ground                     |
| AE4    | GPIO_92             | I/O  | 1.8V           | General Purpose I/O 92                  |
| AE5    | GPIO_90             | I/O  | 1.8V           | General Purpose I/O 90                  |
| AE6    | GPIO_91             | I/O  | 1.8V           | General Purpose I/O 91                  |
| AE7    | GPIO_89             | I/O  | 1.8V           | General Purpose I/O 89                  |
| AE8    | GPIO_84             | I/O  | 1.8V           | General Purpose I/O 84                  |
| AE9    | GPIO_81             | I/O  | 1.8V           | General Purpose I/O 81                  |
| AE10   | DVL0                | I/O  | 1.8V           | Hardware dynamic voltage regulation signal0 |
| AE11   | PWR_SCL             | I/O  | 1.8V           | PMIC I2C bus clock                      |
| AE12   | EXT_32K_IN          | I/O  | 1.8V           | 32K clock input                         |
| AE13   | VSS                 | G    | 0V             | Digital Core ground                     |
| AF1    | VSS                 | G    | 0V             | Digital Core ground                     |
| AF2    | VSS                 | G    | 0V             | Digital Core ground                     |
| AF3    | RESET_IN_N          | I/O  | 1.8V           | Reset input                             |
| AF4    | JTAG_SEL            | I/O  | 1.8V           | Primary JTAG selection                  |
| AF5    | VSS                 | G    | 0V             | Digital Core ground                     |
| AF6    | GPIO_88             | I/O  | 1.8V           | General Purpose I/O 88                  |
| AF7    | GPIO_82             | I/O  | 1.8V           | General Purpose I/O 82                  |
| AF8    | GPIO_83             | I/O  | 1.8V           | General Purpose I/O 83                  |
| AF9    | DVL1                | I/O  | 1.8V           | Hardware dynamic voltage regulation signal1 |
| AF10   | VSS                 | G    | 0V             | Digital Core ground                     |
| AF11   | SLEEP_OUT           | I/O  | 1.8V           | VCXO enabling                           |
| AF12   | PWR_SDA             | I/O  | 1.8V           | PMIC I2C bus data/address               |
| AF13   | GPIO_49             | I/O  | 1.8V/3.3V      | General Purpose I/O 49                  |

#### (P~AF, 14~26)

![](static/K1_pinout_4.png)

> **Note.** Definition of symbols used for pin type:
>
> - AO = Analog output
> - AI = Analog input
> - AIO = Analog input/output
> - G = Ground
> - I/O = Input/Output
> - P = Power
> - RO = Reference output

| Pin ID | Name             | Type | Power Domain | Function                          |
|--------|------------------|------|--------------|-----------------------------------|
| P14    | VSS              | G    | 0V           | Digital Core Ground               |
| P15    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| P16    | VSS              | G    | 0V           | Digital Core Ground               |
| P17    | AUD_GNDSNS       | G    | 0V           | Headphone sense_Ground            |
| P18    | AVDD18_AUD       | P    | 1.8V         | 1.8V power for audio              |
| P19    | AVDD18_AUD       | P    | 1.8V         | 1.8V power for audio              |
| P20    | NA               | AO   | 1.8V         | NA                                |
| P21    | NA               | AO   | 1.8V         | NA                                |
| P22    | NA               | AO   | 1.8V         | NA                                |
| P23    | NA               | AI   | 1.8V         | NA                                |
| P24    | NA               | AI   | 1.8V         | NA                                |
| P25    | NA               | AI   | 1.8V         | NA                                |
| P26    | NA               | AI   | 1.8V         | NA                                |
| R14    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| R15    | VSS              | G    | 0V           | Digital Core Ground               |
| R16    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| R17    | AUD_VSSU         | G    | 0V           | Audio Ground                      |
| R18    | AUD_VDDU09       | P    | 0.9V         | 0.9V power for audio              |
| R19    | AUD_REFGND       | G    | 0V           | Audio Reference Ground            |
| R20    | NA               | AO   | 1.8V         | NA                                |
| R21    | AUD_AUREF10      | RO   | 1.8V         | Audio reference voltage           |
| R22    | NA               | AI   | 1.8V         | NA                                |
| R23    | NA               | AI   | 1.8V         | NA                                |
| R24    | VSS              | G    | 0V           | Digital Core Ground               |
| R25    | NA               | AI   | 1.8V         | NA                                |
| R26    | NA               | AI   | 1.8V         | NA                                |
| T14    | VSS              | G    | 0V           | Digital Core Ground               |
| T15    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| T16    | VSS              | G    | 0V           | Digital Core Ground               |
| T17    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| T18    | VSS              | G    | 0V           | Digital Core Ground               |
| T19    | VSS              | G    | 0V           | Digital Core Ground               |
| T20    | VSS              | G    | 0V           | Digital Core Ground               |
| T21    | AVSS18_AUD       | G    | 0V           | Audio Ground                      |
| T22    | AVSS18_AUD       | G    | 0V           | Audio Ground                      |
| T23    | NA               | AI   | 1.8V         | NA                                |
| T24    | VSS              | G    | 0V           | Digital Core Ground               |
| T25    | NA               | AO   | 3.3V         | NA                                |
| T26    | VSS              | G    | 0V           | Digital Core Ground               |
| U14    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| U15    | VSS              | G    | 0V           | Digital Core Ground               |
| U16    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| U17    | VSS              | G    | 0V           | Digital Core Ground               |
| U18    | VCC_M1_FB        | P    | 0.9V         | Digital Core power FeedBack       |
| U19    | VSS_FB           | G    | 0V           | Digital Core ground FeedBack      |
| U20    | VSS              | G    | 0V           | Digital Core Ground               |
| U21    | GPIO_123         | I/O  | 1.8V         | General Purpose I/O 123           |
| U22    | GPIO_125         | I/O  | 1.8V         | General Purpose I/O 125           |
| U23    | NA               | AI   | 1.8V         | NA                                |
| U24    | NA               | AO   | 3.3V         | NA                                |
| U25    | GPIO_126         | I/O  | 1.8V         | General Purpose I/O 126           |
| U26    | GPIO_127         | I/O  | 1.8V         | General Purpose I/O 127           |
| V14    | VSS              | G    | 0V           | Digital Core Ground               |
| V15    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| V16    | VSS              | G    | 0V           | Digital Core Ground               |
| V17    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| V18    | VSS              | G    | 0V           | Digital Core Ground               |
| V19    | VSS              | G    | 0V           | Digital Core Ground               |
| V20    | VSS              | G    | 0V           | Digital Core Ground               |
| V21    | GPIO_121         | I/O  | 1.8V         | General Purpose I/O 121           |
| V22    | VSS              | G    | 0V           | Digital Core Ground               |
| V23    | GPIO_124         | I/O  | 1.8V         | General Purpose I/O 124           |
| V24    | GPIO_120         | I/O  | 1.8V         | General Purpose I/O 120           |
| V25    | VSS              | G    | 0V           | Digital Core Ground               |
| V26    | GPIO_122         | I/O  | 1.8V         | General purpose I/O 122           |
| W14    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| W15    | VSS              | G    | 0V           | Digital Core Ground               |
| W16    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| W17    | VSS              | G    | 0V           | Digital Core Ground               |
| W18    | VCC_M1           | P    | 0.9V         | Digital Core power                |
| W19    | VSS              | G    | 0V           | Digital Core Ground               |
| W20    | VSS              | G    | 0V           | Digital Core Ground               |
| W21    | GPIO_110         | I/O  | 1.8V         | General Purpose I/O 110           |
| W22    | GPIO_117         | I/O  | 1.8V         | General Purpose I/O 117           |
| W23    | GPIO_116         | I/O  | 1.8V         | General Purpose I/O 116           |
| W24    | VSS              | G    | 0V           | Digital Core Ground               |
| W25    | GPIO_119         | I/O  | 1.8V         | General Purpose I/O 119           |
| W26    | GPIO_118         | I/O  | 1.8V         | General Purpose I/O 118           |
| Y14    | MMC1_VCC_CAP     | RO   | 1.8V         | SD card 1.8V LDO cap              |
| Y15    | GPIO2_VCC_CAP    | RO   | 1.8V         | GPIO2 1.8V LDO cap                |
| Y16    | VSS              | G    | 0V           | Digital Core Ground               |
| Y17    | VSS              | G    | 0V           | Digital Core Ground               |
| Y18    | VSS              | G    | 0V           | Digital Core Ground               |
| Y19    | VSS              | G    | 0V           | Digital Core Ground               |
| Y20    | VSS              | G    | 0V           | Digital Core Ground               |
| Y21    | VCC18_GPIO       | P    | 1.8V         | GPIO1/4/5/PMIC I/O power          |
| Y22    | GPIO_26          | I/O  | 1.8V         | General Purpose I/O 26            |
| Y23    | GPIO_27          | I/O  | 1.8V         | General Purpose I/O 27            |
| Y24    | VSS              | G    | 0V           | Digital Core Ground               |
| Y25    | GPIO_28          | I/O  | 1.8V         | General Purpose I/O 28            |
| Y26    | GPIO_115         | I/O  | 1.8V         | General Purpose I/O 115           |
| AA14   | VCC1833_MMC1     | P    | 1.8V/3.3V    | SD card IO power                  |
| AA15   | VCC1833_GPIO2    | P    | 1.8V/3.3V    | GPIO2 IO power                    |
| AA16   | MMC1_DAT2        | I/O  | 1.8V/3.3V    | SD card data 2                    |
| AA17   | VSS              | G    | 0V           | Digital Core Ground               |
| AA18   | VSS              | G    | 0V           | Digital Core Ground               |
| AA19   | GPIO_32          | I/O  | 1.8V         | General Purpose I/O 32            |
| AA20   | GPIO_29          | I/O  | 1.8V         | General Purpose I/O 29            |
| AA21   | VCC18_GPIO       | P    | 1.8V         | GPIO1/4/5/PMIC I/O power          |
| AA22   | GPIO_21          | I/O  | 1.8V         | General Purpose I/O 21            |
| AA23   | GPIO_24          | I/O  | 1.8V         | General Purpose I/O 24            |
| AA24   | GPIO_23          | I/O  | 1.8V         | General Purpose I/O 23            |
| AA25   | GPIO_25          | I/O  | 1.8V         | General Purpose I/O 25            |
| AA26   | VSS              | G    | 0V           | Digital Core Ground               |
| AB14   | MMC1_DAT0        | I/O  | 1.8V/3.3V    | SD card data 0                    |
| AB15   | GPIO_78          | I/O  | 1.8V/3.3V    | General Purpose I/O 78            |
| AB16   | GPIO_77          | I/O  | 1.8V/3.3V    | General Purpose I/O 77            |
| AB17   | GPIO_02          | I/O  | 1.8V         | General Purpose I/O 02            |
| AB18   | GPIO_03          | I/O  | 1.8V         | General Purpose I/O 03            |
| AB19   | VSS              | G    | 0V           | Digital Core Ground               |
| AB20   | VSS              | G    | 0V           | Digital Core Ground               |
| AB21   | GPIO_41          | I/O  | 1.8V         | General Purpose I/O 41            |
| AB22   | GPIO_44          | I/O  | 1.8V         | General Purpose I/O 44            |
| AB23   | GPIO_19          | I/O  | 1.8V         | General Purpose I/O 19            |
| AB24   | VSS              | G    | 0V           | Digital Core Ground               |
| AB25   | GPIO_20          | I/O  | 1.8V         | General Purpose I/O 20            |
| AB26   | GPIO_22          | I/O  | 1.8V         | General Purpose I/O 22            |
| AC14   | VCC18_GPIO       | P    | 1.8V         | GPIO1/4/5/PMIC I/O power          |
| AC15   | GPIO_79          | I/O  | 1.8V/3.3V    | General Purpose I/O 79            |
| AC16   | VSS              | G    | 0V           | Digital Core Ground               |
| AC17   | GPIO_05          | I/O  | 1.8V         | General Purpose I/O 05            |
| AC18   | GPIO_00          | I/O  | 1.8V         | General Purpose I/O 00            |
| AC19   | VSS              | G    | 0V           | Digital Core Ground               |
| AC20   | GPIO_31          | I/O  | 1.8V         | General Purpose I/O 31            |
| AC21   | GPIO_34          | I/O  | 1.8V         | General Purpose I/O 34            |
| AC22   | GPIO_42          | I/O  | 1.8V         | General Purpose I/O 42            |
| AC23   | GPIO_43          | I/O  | 1.8V         | General Purpose I/O 43            |
| AC24   | GPIO_17          | I/O  | 1.8V         | General Purpose I/O 17            |
| AC25   | VSS              | G    | 0V           | Digital Core Ground               |
| AC26   | GPIO_18          | I/O  | 1.8V         | General Purpose I/O 18            |
| AD14   | MMC1_CMD         | I/O  | 1.8V/3.3V    | SD card command                   |
| AD15   | GPIO_76          | I/O  | 1.8V/3.3V    | General Purpose I/O 76            |
| AD16   | VSS              | G    | 0V           | Digital Core Ground               |
| AD17   | GPIO_04          | I/O  | 1.8V         | General Purpose I/O 04            |
| AD18   | GPIO_01          | I/O  | 1.8V         | General Purpose I/O 01            |
| AD19   | GPIO_30          | I/O  | 1.8V         | General Purpose I/O 30            |
| AD20   | GPIO_33          | I/O  | 1.8V         | General Purpose I/O 33            |
| AD21   | VCC18_GPIO       | P    | 1.8V         | GPIO1/4/5/PMIC I/O power          |
| AD22   | VCC18_GPIO       | P    | 1.8V         | GPIO1/4/5/PMIC I/O power          |
| AD23   | GPIO_14          | I/O  | 1.8V         | General Purpose I/O 14            |
| AD24   | GPIO_12          | I/O  | 1.8V         | General Purpose I/O 12            |
| AD25   | GPIO_16          | I/O  | 1.8V         | General Purpose I/O 16            |
| AD26   | GPIO_15          | I/O  | 1.8V         | General Purpose I/O 15            |
| AE14   | MMC1_CLK         | I/O  | 1.8V/3.3V    | SD card clock                     |
| AE15   | MMC1_DAT3        | I/O  | 1.8V/3.3V    | SD card data 3                    |
| AE16   | GPIO_75          | I/O  | 1.8V/3.3V    | General Purpose I/O 75            |
| AE17   | GPIO_11          | I/O  | 1.8V         | General Purpose I/O 11            |
| AE18   | GPIO_07          | I/O  | 1.8V         | General Purpose I/O 07            |
| AE19   | GPIO_10          | I/O  | 1.8V         | General Purpose I/O 10            |
| AE20   | GPIO_37          | I/O  | 1.8V         | General Purpose I/O 37            |
| AE21   | GPIO_35          | I/O  | 1.8V         | General Purpose I/O 35            |
| AE22   | GPIO_38          | I/O  | 1.8V         | General Purpose I/O 38            |
| AE23   | GPIO_46          | I/O  | 1.8V         | General Purpose I/O 46            |
| AE24   | VSS              | G    | 0V           | Digital Core Ground               |
| AE25   | GPIO_13          | I/O  | 1.8V         | General Purpose I/O 13            |
| AE26   | VSS              | G    | 0V           | Digital Core Ground               |
| AF14   | MMC1_DAT1        | I/O  | 1.8V/3.3V    | SD card data 1                    |
| AF15   | VSS              | G    | 0V           | Digital Core Ground               |
| AF16   | GPIO_80          | I/O  | 1.8V/3.3V    | General Purpose I/O 80            |
| AF17   | GPIO_08          | I/O  | 1.8V         | General Purpose I/O 08            |
| AF18   | GPIO_06          | I/O  | 1.8V         | General Purpose I/O 06            |
| AF19   | GPIO_09          | I/O  | 1.8V         | General Purpose I/O 09            |
| AF20   | VSS              | G    | 0V           | Digital Core Ground               |
| AF21   | GPIO_40          | I/O  | 1.8V         | General Purpose I/O 40            |
| AF22   | GPIO_36          | I/O  | 1.8V         | General Purpose I/O 36            |
| AF23   | GPIO_39          | I/O  | 1.8V         | General Purpose I/O 39            |
| AF24   | GPIO_45          | I/O  | 1.8V         | General Purpose I/O 45            |
| AF25   | VSS              | G    | 0V           | Digital Core Ground               |
| AF26   | VSS              | G    | 0V           | Digital Core Ground               |

### 4.2 I/O Pin Parameters

#### For 1.8V I/O Pins

| Power Domain | Symbol                                      | Description                                | Min         | Typ     | Max         |
|--------------|---------------------------------------------|--------------------------------------------|-------------|---------|-------------|
| **1.8V Input**   | Vih                                         | High level input                           | VCC×0.7V    | 1.8V    | VCC+0.2V    |
|   | Vil                                         | Low level input                            | -0.3V       | 0V      | VCC×0.3V    |
|    | Rpu                                         | Pull up resistor                           | 55kΩ        | 79kΩ    | 121kΩ       |
|    | Rpd                                         | Pull down resistor                         | 51kΩ        | 87kΩ    | 169kΩ       |
|    | Iil                                         | Input leakage current (Pad in input mode)  |             |         | 10µA        |
| **1.8V Output**  | Voh                                         | High level output                          | VCC−0.2V    |         |             |
|   | Vol                                         | Low level output                           |             |         | 0.2V        |
|   | Iol (DCS[1:0]=00/01/10/11)                 | Low level output current when Vpad=0.2V    | 13/25/37/49mA |         |             |
|   | Ioh (DCS[1:0]=00/01/10/11)                 | High level output current when Vpad=VCC−0.2V | 11/21/32/42mA |         |             |

#### For 3.3V I/O Pins

| Power Domain | Symbol                                                                 | Description                                      | Min        | Typ   | Max         |
|--------------|------------------------------------------------------------------------|--------------------------------------------------|------------|-------|-------------|
| **3.3V Input**   | Vih                                                                    | High level input                                 | 2V         |       | VCC+0.3V    |
|    | Vil                                                                    | Low level input                                  | -0.3V      | 0V    | 0.8V        |
|    | Rpu                                                                    | Pull up resistor                                 | 26kΩ       | 47kΩ  | 72kΩ        |
|    | Rpd                                                                    | Pull down resistor                               | 27kΩ       | 54kΩ  | 267kΩ       |
|    | Iil                                                                    | Input leakage current                            |            |       | 10µA        |
| **3.3V Output**  | Voh                                                                    | High level output                                | 2.4V       |       |             |
|   | Vol                                                                    | Low level output                                 |            |       | 0.4V        |
|   | Iol (DS[2:0]=000/001/010/011/100/101/110/111)                         | Low level output current when Vpad=0.4V          | 7/10/14/18/21/24/28/31mA |       |             |
|   | Ioh (DS[2:0]=000/001/010/011/100/101/110/111)                         | High level output current when Vpad=VCC-0.5V     | 7/10/13/16/19/23/26/29mA |       |             |

### 4.3 Multiplexed Signal/Pin Functions

The **Function 0** through 7 signals is assigned to the I/O pins of K1.

Most I/O pins of K1 are multi-function allowing them to be configured for one of several available functions using Multi-Function Pin Registers (MFPRs). Additionally, some functions can be configured to be present on several different pins.

The assigned signals are organized by their functions (e.g. power supply, clock, etc.) which are arranged in groups according to their interfaces (e.g. JTAG, SPIx, etc.) as per description in the following subsections (sorted alphabetically for user convenience).

> **Note.** Definition of symbols used for signal/pin type:
>
> - I = Input
> - O = Output
> - I/O = Input/Output
> - OD = Open-Drain
> - RO = Reference output

#### JTAG

##### Primary

| Signal/Pin        | Type | Description                                                                                                                                     |
|-------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| PRI_TCK     | I    | Primary JTAG interface 1 test clock. Used for all transfers on the JTAG test interface.                                                          |
| PRI_TDI     | I    | Primary JTAG interface 1 test data input. Used to send data from the JTAG controller to the K1 processor. This pin has an internal pullup resistor. |
| PRI_TDO     | O    | Primary JTAG Interface 1 test data output. Used to return data from the K1 processor to the JTAG controller.                                     |
| PRI_TMS     | I    | Primary JTAG Interface 1 test mode select. Used to select the test mode required from the JTAG controller. This pin has an internal pullup resistor. |
| PRI_TRSTn   | I    | Primary JTAG Interface 1 test reset. Used for IEEE 1194.1 test reset.                                                                            |
| VCXO_OUT    | O    | 24 MHz VCXO output clock                                                                                                                        |
| VCXO_REQ    | I    | OCLK1 request                                                                                                                                   |

##### Secondary

| Signal/Pin         | Type | Description               |
|--------------|------|-----------------------|
| SEC2_TCK     | I    | Secondary JTAG Interface 2 test clock. Used for all transfers on the JTAG test interface.                                                        |
| SEC2_TDI     | I    | Secondary JTAG Interface 2 test data input. Used to send data from the JTAG controller to the K1 processor. This pin has an internal pullup resistor. |
| SEC2_TDO     | O    | Secondary JTAG Interface 2 test data output. Used to return data from the K1 processor to the JTAG controller.                                   |
| SEC2_TMS     | I    | Secondary JTAG Interface 2 test mode select. Used to select the test mode required from the JTAG controller. This pin has an internal pullup resistor. |
| SEC2_TRSTn   | I    | Secondary JTAG Interface 2 test reset. Used for IEEE 1194.1 test reset.                                                                          |

#### Keypad Controller

| Signal/Pin           | Type | Description                     |
|----------------|------|---------------------------------|
| KP_DK[4:0]     | I    | Keypad direct key inputs [4:0]  |
| KP_MKIN[3:0]   | I    | Keypad matrix key inputs [3:0]  |
| KP_MKOUT[3:0]  | O    | Keypad matrix key outputs [3:0] |

##### Miscellaneous

| Signal/Pin           | Type | Description    |
|----------------|------|----------------|
| MPLL_TST_CK    |      | PLL test pin                                                                                                                                                                                                |
| MN_CLK_OUT     | O    | Fractional (M/N) divided clock. Main PMU general purpose M/N fractional clock divider clock output. CLK_REQ must be set as Function 0 and pulled high for the 13 MHz clock to be output on GPIO[122] (MN_CLK_OUT). |
| Sleep_OUT      | O    | PMIC sleep setting                                                                                                                                                                                          |

#### SPIx

| Signal/Pin        | Type | Description  |
|-------------|------|------------------------|
| SPIx_FRM    | I/O  | Synchronous serial port frame 0/2. The serial frame sync can be configured as an output (master mode operation) or an input (slave mode operation). |
| SPIx_RXD    | I    | Synchronous serial port receive data 0/2. Serial data latched using the bit clock.                                                               |
| SPIx_SCLK   | I/O  | Synchronous serial port clock 0/2. The serial bit clock can be configured as an output (master mode operation) or an input (slave mode operation). |
| SPIx_TXD    | O    | Synchronous serial port transmit data 0/2. Serial data driven out synchronously with the bit clock.                                              |

#### TWSI

##### Dedicated

| Signal/Pin      | Type | Description                     |
|-----------|------|---------------------------------|
| PWR_SDA   | I/O  | TWSI serial data/address signal |
| PWR_SCL   | I/O  | TWSI serial clock line signal   |

##### Common

| Signal/Pin       | Type   | Description |
|------------|--------|-------------|
| I2Cx_SCL   | I/O,OD | TWSIx clock |
| I2Cx_SDA   | I/O,OD | TWSIx data  |

#### UARTx

| Signal/Pin          | Type | Description           |
|---------------|------|-----------------------|
| UARTx_CTSn    | I    | UARTx clear-to-send   |
| UARTx_RTSn    | O    | UARTx request-to-send |
| UARTx_RXD     | I    | UARTx receive data    |
| UARTx_TXD     | O    | UARTx transmit data   |

#### USB

| Signal/Pin | Type | Description           |
|------------|------|-----------------------|
| USBx_N     | I/O  | USB D±                |
| USBx_P     | I/O  | USB D±                |
| VBUS_ON    | I    | USB VBUS present indicator |

### 4.4 Multi-Function I/O Pin Assignments

All functions that are assigned to a pin as its primary functions are tabled below.

![Pin Function](./static/pin_func_en.png)

### 4.5 Power Supply Pins

| Pin Name           | Domain Name        | Domain Voltage                     | Description                                                                 |
|--------------------|--------------------|------------------------------------|-----------------------------------------------------------------------------|
| AUD_VDDU09         | AUDIO              | 0.9V                               | 0.9V power for audio                                                        |
| AUD_VNEG           | AUDIO              | -1.8V                              | Negative voltage for headphone driver                                       |
| AUD_VPOS           | AUDIO              | 1.8V                               | Positive voltage for headphone driver                                       |
| AVDD18_AUD         | AUDIO              | 1.8V                               | 1.8V power for audio                                                        |
| AVDD3V3_AUD        | AUDIO              | 3.3V                               | 3.3V power for earphone driver                                              |
| VCC_M1             | CORE               | 0.9V                               | Digital core power                                                          |
| AVDD09_CSI         | CSI                | 0.9V                               | MIPI_CSI digital power                                                      |
| AVDD18_CSI         | CSI                | 1.8V                               | MIPI_CSI analog power                                                       |
| AVDD09_AFEAP       | DCXO               | 0.9V                               | 0.9V power for DCXO                                                         |
| AVDD18_AFEAP       | DCXO               | 1.8V                               | 1.8V power for DCXO                                                         |
| AVDD06_DDR         | DDR                | lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD | LPDDR4X IO power                                                            |
| AVDD11_DDR         | DDR                | lp4x: 1.1V<br/>lp4: 1.1V<br/>lp3: 1.2V | LPDDR PHY power supply                                                      |
| AVDD18_DDR         | DDR                | 1.8V                               | LPDDR PHY PLL 1.8V power                                                    |
| AVDD18_PHY         | DDR                | 1.8V                               | Analog 1.8V power                                                           |
| AVDDU_DDR          | DDR                | 0.9V                               | LPDDR PHY PLL logical power                                                 |
| AVDDU_PHY          | DDR                | 0.9V                               | LPDDR PHY core logical power                                                |
| DDR_LDO_CAP        | DDR                | 0.7~0.9V                           | External LDO output ball.<br/>Connect to a 100nF capacitor on PCB board.    |
| DDR_LP23_VREFCA    | DDR                | lp3: 0.6V<br/>lp4: high-z          | CA VREF for lpddr23.<br/>LP4/4x, Keep the pin NC.                           |
| DDR_LP23_VREFDQ    | DDR                | lp3: 0.6V<br/>lp4: high-z          | DQ VREF for lpddr23.<br/>LP4/4x, keep the pin NC.                           |
| VDDQ_V1P2          | DDR                | lp3: 1.2V<br/>lp4x: 0.6V           | LPDDR3 IO power                                                             |
| AVDD09_DSI1        | DSI                | 0.9V                               | DSI digital power                                                           |
| AVDD12_DSI1        | DSI                | 1.2V                               | DSI driver power                                                            |
| AVDD18_DSI1        | DSI                | 1.8V                               | DSI analog power                                                            |
| AVDD18_EFUSE       | EFUSE              | 1.8V                               | ANAGRP                                                                      |
| AVDD09_EMMC        | EMMC               | 0.9V                               | eMMC digital power                                                          |
| AVDD18_EMMC        | EMMC               | 1.8V                               | eMMC analog power                                                           |
| VCC18_GPIO         | GPIO1/4/5/PMIC     | 1.8V                               | GPIO1/4/5/PMIC I/O power                                                    |
| VCC1833_GPIO2      | GPIO2              | 1.8V/3.3V                          | GPIO2 IO power                                                              |
| VCC1833_GPIO3      | GPIO3              | 1.8V/3.3V                          | GPIO3 IO power                                                              |
| AVDD09_HDMI        | HDMI               | 0.9V                               | HDMI digital power                                                          |
| AVDD18_HDMI        | HDMI               | 1.8V                               | HDMI 1.8V power                                                             |
| AVDD33_HDMI        | HDMI               | 3.3V                               | HDMI 3.3V power                                                             |
| AVDD09_PCIEA       | PCIEA              | 0.9V                               | PCIEA digital power                                                         |
| AVDD18_PCIEA       | PCIEA              | 1.8V                               | PCIEA analog power                                                          |
| AVDD09_PCIEB       | PCIEB              | 0.9V                               | PCIEB digital power                                                         |
| AVDD18_PCIEB       | PCIEB              | 1.8V                               | PCIEB analog power                                                          |
| AVDD09_PCIEC       | PCIEC              | 0.9V                               | PCIEC digital power                                                         |
| AVDD18_PCIEC       | PCIEC              | 1.8V                               | PCIEC analog power                                                          |
| AVDD09_PLL         | PLL                | 0.9V                               | System PLL power supply                                                     |
| AVDD18_PLL         | PLL                | 1.8V                               | System PLL power supply                                                     |
| VCC1833_QSPI       | QSPI               | 1.8V/3.3V                          | QSPI IO power                                                               |
| VCC1833_MMC1       | SD card            | 1.8V/3.3V                          | SD card IO power                                                            |
| AVDD09_USB         | USB2.0             | 0.9V                               | USB2.0 digital power                                                        |
| AVDD18_USB         | USB2.0             | 1.8V                               | USB2.0 1.8V power                                                           |
| AVDD33_USB         | USB2.0             | 3.3V                               | USB2.0 3.3V power                                                           |

### 4.6 Multi-Function Pin Registers

In K1 are defined and implemented Multi-Function Pin Registers (MFPRs). In particular, there are 129 MFPR in total, starting from the base address 0xD401E000 with a stride of 0x4, as tabled below.

| MFPR ID      | Address       | Offset |
|--------------|---------------|--------|
| GPIO_00      | 0xD401E004    | 0x4    |
| GPIO_01      | 0xD401E008    | 0x8    |
| GPIO_02      | 0xD401E00C    | 0xC    |
| GPIO_03      | 0xD401E010    | 0x10   |
| GPIO_04      | 0xD401E014    | 0x14   |
| GPIO_05      | 0xD401E018    | 0x18   |
| GPIO_06      | 0xD401E01C    | 0x1C   |
| GPIO_07      | 0xD401E020    | 0x20   |
| GPIO_08      | 0xD401E024    | 0x24   |
| GPIO_09      | 0xD401E028    | 0x28   |
| GPIO_10      | 0xD401E02C    | 0x2C   |
| GPIO_11      | 0xD401E030    | 0x30   |
| GPIO_12      | 0xD401E034    | 0x34   |
| GPIO_13      | 0xD401E038    | 0x38   |
| GPIO_14      | 0xD401E03C    | 0x3C   |
| GPIO_15      | 0xD401E040    | 0x40   |
| GPIO_16      | 0xD401E044    | 0x44   |
| GPIO_17      | 0xD401E048    | 0x48   |
| GPIO_18      | 0xD401E04C    | 0x4C   |
| GPIO_19      | 0xD401E050    | 0x50   |
| GPIO_20      | 0xD401E054    | 0x54   |
| GPIO_21      | 0xD401E058    | 0x58   |
| GPIO_22      | 0xD401E05C    | 0x5C   |
| GPIO_23      | 0xD401E060    | 0x60   |
| GPIO_24      | 0xD401E064    | 0x64   |
| GPIO_25      | 0xD401E068    | 0x68   |
| GPIO_26      | 0xD401E06C    | 0x6C   |
| GPIO_27      | 0xD401E070    | 0x70   |
| GPIO_28      | 0xD401E074    | 0x74   |
| GPIO_29      | 0xD401E078    | 0x78   |
| GPIO_30      | 0xD401E07C    | 0x7C   |
| GPIO_31      | 0xD401E080    | 0x80   |
| GPIO_32      | 0xD401E084    | 0x84   |
| GPIO_33      | 0xD401E088    | 0x88   |
| GPIO_34      | 0xD401E08C    | 0x8C   |
| GPIO_35      | 0xD401E090    | 0x90   |
| GPIO_36      | 0xD401E094    | 0x94   |
| GPIO_37      | 0xD401E098    | 0x98   |
| GPIO_38      | 0xD401E09C    | 0x9C   |
| GPIO_39      | 0xD401E0A0    | 0xA0   |
| GPIO_40      | 0xD401E0A4    | 0xA4   |
| GPIO_41      | 0xD401E0A8    | 0xA8   |
| GPIO_42      | 0xD401E0AC    | 0xAC   |
| GPIO_43      | 0xD401E0B0    | 0xB0   |
| GPIO_44      | 0xD401E0B4    | 0xB4   |
| GPIO_45      | 0xD401E0B8    | 0xB8   |
| GPIO_46      | 0xD401E0BC    | 0xBC   |
| GPIO_47      | 0xD401E0C0    | 0xC0   |
| GPIO_48      | 0xD401E0C4    | 0xC4   |
| GPIO_49      | 0xD401E0C8    | 0xC8   |
| GPIO_50      | 0xD401E0CC    | 0xCC   |
| GPIO_51      | 0xD401E0D0    | 0xD0   |
| GPIO_52      | 0xD401E0D4    | 0xD4   |
| GPIO_53      | 0xD401E0D8    | 0xD8   |
| GPIO_54      | 0xD401E0DC    | 0xDC   |
| GPIO_55      | 0xD401E0E0    | 0xE0   |
| GPIO_56      | 0xD401E0E4    | 0xE4   |
| GPIO_57      | 0xD401E0E8    | 0xE8   |
| GPIO_58      | 0xD401E0EC    | 0xEC   |
| GPIO_59      | 0xD401E0F0    | 0xF0   |
| GPIO_60      | 0xD401E0F4    | 0xF4   |
| GPIO_61      | 0xD401E0F8    | 0xF8   |
| GPIO_62      | 0xD401E0FC    | 0xFC   |
| GPIO_63      | 0xD401E100    | 0x100  |
| GPIO_64      | 0xD401E104    | 0x104  |
| GPIO_65      | 0xD401E108    | 0x108  |
| GPIO_66      | 0xD401E10C    | 0x10C  |
| GPIO_67      | 0xD401E110    | 0x110  |
| GPIO_68      | 0xD401E114    | 0x114  |
| GPIO_69      | 0xD401E118    | 0x118  |
| PRI_TDI      | 0xD401E11C    | 0x11C  |
| PRI_TMS      | 0xD401E120    | 0x120  |
| PRI_TCK      | 0xD401E124    | 0x124  |
| PRI_TDO      | 0xD401E128    | 0x128  |
| GPIO_74      | 0xD401E12C    | 0x12C  |
| GPIO_75      | 0xD401E130    | 0x130  |
| GPIO_76      | 0xD401E134    | 0x134  |
| GPIO_77      | 0xD401E138    | 0x138  |
| GPIO_78      | 0xD401E13C    | 0x13C  |
| GPIO_79      | 0xD401E140    | 0x140  |
| GPIO_80      | 0xD401E144    | 0x144  |
| GPIO_81      | 0xD401E148    | 0x148  |
| GPIO_82      | 0xD401E14C    | 0x14C  |
| GPIO_83      | 0xD401E150    | 0x150  |
| GPIO_84      | 0xD401E154    | 0x154  |
| GPIO_85      | 0xD401E158    | 0x158  |
| QSPI_DAT0    | 0xD401E168    | 0x168  |
| QSPI_DAT1    | 0xD401E16C    | 0x16C  |
| QSPI_DAT2    | 0xD401E170    | 0x170  |
| QSPI_DAT3    | 0xD401E174    | 0x174  |
| QSPI_CS1     | 0xD401E178    | 0x178  |
| QSPI_CLK     | 0xD401E17C    | 0x17C  |
| MMC1_DAT3    | 0xD401E1B8    | 0x1B8  |
| MMC1_DAT2    | 0xD401E1BC    | 0x1BC  |
| MMC1_DAT1    | 0xD401E1C0    | 0x1C0  |
| MMC1_DAT0    | 0xD401E1C4    | 0x1C4  |
| MMC1_CMD     | 0xD401E1C8    | 0x1C8  |
| MMC1_CLK     | 0xD401E1CC    | 0x1CC  |
| GPIO_110     | 0xD401E1D0    | 0x1D0  |
| PWR_SCL      | 0xD401E1D4    | 0x1D4  |
| PWR_SDA      | 0xD401E1D8    | 0x1D8  |
| VCXO_EN      | 0xD401E1DC    | 0x1DC  |
| DVL0         | 0xD401E1E0    | 0x1E0  |
| DVL1         | 0xD401E1E4    | 0x1E4  |
| PMIC_INT_N   | 0xD401E1E8    | 0x1E8  |
| GPIO_86      | 0xD401E1EC    | 0x1EC  |
| GPIO_87      | 0xD401E1F0    | 0x1F0  |
| GPIO_88      | 0xD401E1F4    | 0x1F4  |
| GPIO_89      | 0xD401E1F8    | 0x1F8  |
| GPIO_90      | 0xD401E1FC    | 0x1FC  |
| GPIO_91      | 0xD401E200    | 0x200  |
| GPIO_92      | 0xD401E204    | 0x204  |
| GPIO_111     | 0xD401E20C    | 0x20C  |
| GPIO_112     | 0xD401E210    | 0x210  |
| GPIO_113     | 0xD401E214    | 0x214  |
| GPIO_114     | 0xD401E218    | 0x218  |
| GPIO_115     | 0xD401E21C    | 0x21C  |
| GPIO_116     | 0xD401E220    | 0x220  |
| GPIO_117     | 0xD401E224    | 0x224  |
| GPIO_118     | 0xD401E228    | 0x228  |
| GPIO_119     | 0xD401E22C    | 0x22C  |
| GPIO_120     | 0xD401E230    | 0x230  |
| GPIO_121     | 0xD401E234    | 0x234  |
| GPIO_122     | 0xD401E238    | 0x238  |
| GPIO_123     | 0xD401E23C    | 0x23C  |
| GPIO_124     | 0xD401E240    | 0x240  |
| GPIO_125     | 0xD401E244    | 0x244  |
| GPIO_126     | 0xD401E248    | 0x248  |
| GPIO_127     | 0xD401E24C    | 0x24C  |

#### MFPR Functional Description

##### I/O PAD Parameter Definition

The input thresholds of Buffer Mode of I/O PADs are tabled below.

**ST1:ST0 == 2'b00**

| Input Threshold | Min  | Typ  | Max  | Unit |
|-----------------|------|------|------|------|
| VT              | 0.75 | 0.91 | 1.09 | V    |
| VT PU           | 0.74 | 0.90 | 1.08 | V    |
|                 |      |      |      |      |
| VT PD           | 0.76 | 0.92 | 1.10 | V    |

Instead, the input thresholds of Schmitt Trigger Mode of I/O PADs are tabled below.

**ST1:ST0 == 2'b01**

| Input Threshold | Min  | Typ  | Max  | Unit |
|-----------------|------|------|------|------|
| VT+             | 0.82 | 0.97 | 1.13 | V    |
| VT-             | 0.72 | 0.85 | 1.02 | V    |
| VT+PU           | 0.81 | 0.96 | 1.12 | V    |
| VT-PU           | 0.71 | 0.84 | 1.01 | V    |
| VT+PD           | 0.82 | 0.98 | 1.14 | V    |
| VT-PD           | 0.73 | 0.86 | 1.03 | V    |

**ST1:ST0 == 2'b10 / 2'b11**

| Input Threshold | Min  | Typ  | Max  | Unit |
|-----------------|------|------|------|------|
| VT+             | 0.87 | 1.04 | 1.19 | V    |
| VT-             | 0.69 | 0.80 | 0.95 | V    |
| VT+PU           | 0.86 | 1.03 | 1.18 | V    |
| VT-PU           | 0.68 | 0.79 | 0.94 | V    |
| VT+PD           | 0.88 | 1.05 | 1.20 | V    |
| VT-PD           | 0.69 | 0.81 | 0.96 | V    |

##### MFPR Field Description

| Bit(s)   | Field         | Type | Reset | Description |
|----------|---------------|------|-------|-------------|
| 31:16    | RSVD          | RO   | 0     | This field is reserved for future use |
| 15       | PULL SEL      | RW   | 0x1   | This field selects between two sets of controls for the pull-up and pull-down functionality as follows:<br/>- 0: The pull-up and pull-down resistors are controlled by the selected alternate function for the pin<br/>- 1: The pull-up and pull-down resistors are controlled by the &lt;PULLUP EN&gt; and &lt;PULLDN EN&gt; fields in this register, overriding the function indicated by the selected alternate function.<br/>During low-power states, this field is overridden to 1 and controlled by the &lt;PULLUP EN&gt; and &lt;PULLDN EN&gt; fields.<br/>In these low-power states, this field is effectively 1, although the register value is not changed (refer to low-power (sleep) mode operation for more information). |
| 14       | PULLUP EN     | RW   | 0x0   | This field controls the output function while the &lt;PULL SEL&gt; field is set to 1 (or is effectively 1) as follows:<br/>- 0: The internal pull-up resistor of the pin is disabled<br/>- 1: The internal pull-up resistor of the pin is enabled<br/>The address and reset value is on a pin-by-pin basis. Do not rely on the reset value of this field. It must be configured by software to the desired settings. |
| 13       | PULLDN EN     | RW   | 0x0   | This field controls the output function while &lt;PULL SEL&gt; is set to 1 (or is effectively 1) as follows:<br/>- 0: The internal pull-down resistor of the pin is disabled<br/>- 1: The internal pull-down resistor of the pin is enabled<br/>The address and reset value is on a pin-by-pin basis. Do not rely on the reset value of this field. It must be configured by software to the desired settings. |
| 12:11    | DRIVE[1:0]    | RW   | 0x2   | This field defines the drive strength and slew rate for this pin (in functional mode when the pin is driving HIGH or LOW value) as follows:<br/>- 2'b00: SLOW<br/>- 2'b01: SLOW<br/>- 2'b10: MEDIUM<br/>- 2'b11: FAST<br/>They are the DS1 and DS0 bit of the drive strength in the current table. |
| 10       | DRIVE[2]      | RW   | 0x0   | This is the DS2 bit to program for higher level of driving strength in the current table.<br/>The address and reset value is on a pin-by-pin basis. Do not rely on the reset value of this field. It must be configured by software to the desired settings.<br/>For Medium (all GPIOs except for SD card), it is 010.<br/>For Fast (SD card I/O), it is 110. |
| 9:8      | ST[1:0]       | RW   | 0x0   | This field controls the Schmitt trigger input threshold as follows:<br/>- 2'b00: buffer input, threshold is 0.9v<br/>- 2'b01/10/11: enabled the Schmitt trigger with larger hysteresis for VT- and VT+ threshold (refer to <strong>Section 4.7</strong>) |
| 7        | SLE           | RW   | 0x0   | This field enables/disables the slew rate output control as follows:<br/>- 1'b1: Enabled<br/>- 1'b0: Disabled<br/>Enabling the slew rate output control will slow down the output ramp for EMI considerations. |
| 6        | EDGE_CLEAR    | RW   | 0x1   | This field enable/disable the edge-detection logic as follows:<br/>- 1'b0: Enabled and ready to detect an edge<br/>- 1'b1: Disabled and no edge is detected<br/>This is an enable for the &lt;EDGE_FALL_EN&gt; and &lt;EDGE_RISE_EN&gt; control fields.<br/>This field is only present when a pin has been defined as potentially waking up on an edge.<br/>If the device is not configured in this manner, this field is not present (i.e. reserved) and writing to it has no effect (refer to <strong>Section 4.5</strong> for more information about which MFPRs include or not include these bits). |
| 5        | EDGE_FALL_EN  | RW   | 0x0   | This field enables/disable to detect a falling edge as follows:<br/>- 1'b0: Disabled<br/>- 1'b1: Enable<br/>To detect a falling edge on this pin,<br/>- The pin needs not be an output<br/>- This field must be set to 1<br/>- The &lt;EDGE_CLEAR&gt; field must be set to 0<br/>This field is only present when a pin has been defined as potentially waking up on an edge.<br/>If the device is not configured in this manner, this field is not present (i.e. reserved) and writing to it has no effect (refer to <strong>Section 4.5</strong> for more information about which MFPRs include or not include these bits). |
| 4        | EDGE_RISE_EN  | RW   | 0x0   | This field enables/disable to detect a rising edge as follows:<br/>- 1'b0: Disables<br/>- 1'b1: Enabled<br/>To detect a rising edge on this pin,<br/>- The pin need not be an output<br/>- This field must be set to 1<br/>- The &lt;EDGE_CLEAR&gt; field must be set to 0<br/>This field is only present when a pin has been defined as potentially waking up on an edge.<br/>If the device is not configured in this manner, this field is not present (i.e. reserved) and writing to it has no effect (refer to <strong>Section 4.5</strong> for more information about which MFPRs include or not include these bits). |
| 3        | SPU           | RW   | 0x0   | This field enables/disables a strong pull resistor as follows:<br/>- 1'b0: Disabled<br/>- 1'b1: Enabled<br/>This field is used for I2C or SD card PADs which require a strong pull resistor. |
| 2:0      | AF SEL        | RW   | 0x0   | This field is used for the selection of an alternate function for a pin between eight possible options as follows:<br/>- 0x0: Alternate function 0 (always as the primary at reset)<br/>- 0x1: Alternate function 1<br/>- 0x2: Alternate function 2<br/>- 0x3: Alternate function 3<br/>- 0x4: Alternate function 4<br/>- 0x5: Alternate function 5<br/>- 0x6: Alternate function 6<br/>- 0x7: Alternate function 7 |

## 5. Electrical Characteristics

### 5.1 Pin AC/DC Operating Conditions

<img src="static/pin_ac_dc_en.png" alt="" width="500">

### 5.2 Absolute Max Ratings

#### For Pins

| Item             | Symbol/Pin        | Min   | Max    | Unit |
|------------------|-------------------|-------|--------|------|
| Digital Power    | VCC_M1            | -0.1  | 1.035  | V    |
| PLL              | AVDD09_PLL        | -0.1  | 1.035  | V    |
| PLL              | AVDD18_PLL        | -0.1  | 2.07   | V    |
| OSC              | AVDD09_AFEAP      | -0.1  | 1.035  | V    |
| OSC              | AVDD18_AFEAP      | -0.1  | 2.07   | V    |
| PCIeC            | AVDD18_PCIEC      | -0.1  | 2.07   | V    |
| PCIeC            | AVDD09_PCIEC      | -0.1  | 1.035  | V    |
| PCIeB            | AVDD18_PCIEB      | -0.1  | 2.07   | V    |
| PCIeB            | AVDD09_PCIEB      | -0.1  | 1.035  | V    |
| PCIeA            | AVDD18_PCIEA      | -0.1  | 2.07   | V    |
| PCIeA            | AVDD09_PCIEA      | -0.1  | 1.035  | V    |
| USB IO           | AVDD33_USB        | -0.1  | 3.795  | V    |
| USB PHY          | AVDD18_USB        | -0.1  | 2.07   | V    |
| USB PHY          | AVDD09_USB        | -0.1  | 1.035  | V    |
| MIPI DSI IO      | AVDD12_DSI1       | -0.1  | 1.38   | V    |
| MIPI DSI PHY     | AVDD09_DSI1       | -0.1  | 1.035  | V    |
| MIPI DSI PHY     | AVDD18_DSI1       | -0.1  | 2.07   | V    |
| MIPI CSI PHY     | AVDD09_CSI        | -0.1  | 1.035  | V    |
| MIPI CSI PHY     | AVDD18_CSI        | -0.1  | 2.07   | V    |
| HDMI             | AVDD09_HDMI       | -0.1  | 1.035  | V    |
| HDMI             | AVDD18_HDMI       | -0.1  | 2.07   | V    |
| HDMI             | AVDD33_HDMI       | -0.1  | 3.795  | V    |
| eMMC             | VDD09_EMMC        | -0.1  | 1.035  | V    |
| eMMC             | V18_EMMC          | -0.1  | 2.07   | V    |
| QSPI             | VCC1833_QSPI      | -0.1  | 2.07   | V    |
| QSPI             | VCC1833_QSPI      | -0.1  | 3.795  | V    |
| SD               | VCC1833_MMC1      | -0.1  | 2.07   | V    |
| SD               | VCC1833_MMC1      | -0.1  | 3.795  | V    |
| DDR PHY          | AVDD18_PHY        | -0.1  | 2.07   | V    |
| DDR PHY          | AVDD18_DDR        | -0.1  | 2.07   | V    |
| DDR PHY          | AVDD11_DDR        | -0.1  | 1.265  | V    |
| DDR PHY          | AVDD11_DDR        | -0.1  | 1.38   | V    |
| DDR PHY          | AVDDU_PHY         | -0.1  | 1.035  | V    |
| DDR PHY          | AVDDU_DDR         | -0.1  | 1.035  | V    |
| DDR IO           | AVDD06_DDR        | -0.1  | 0.69   | V    |
| DDR IO           | VDDQ_V1P2         | -0.1  | 1.38   | V    |
| eFuse            | AVDD18_EFUSE      | -0.1  | 2.07   | V    |
| Audio Logic      | AUD_VDDU09        | -0.1  | 1.035  | V    |
| Audio Power NEG  | AUD_VNEG          | N/A   | -2.07  | V    |
| Audio Power POS  | AUD_VPOS          | -0.1  | 2.07   | V    |
| Audio Analog     | AVDD18_AUD        | -0.1  | 2.07   | V    |
| Audio Analog     | AVDD3V3_AUD       | -0.1  | 3.795  | V    |
| GPIO             | VCC18_GPIO        | -0.1  | 2.07   | V    |
| GPIO3            | VCC1833_GPIO3     | -0.1  | 2.07   | V    |
| GPIO3            | VCC1833_GPIO3     | -0.1  | 3.795  | V    |
| GPIO2            | VCC1833_GPIO2     | -0.1  | 2.07   | V    |
| GPIO2            | VCC1833_GPIO2     | -0.1  | 3.795  | V    |

#### For Packages

| Item                              | Symbol | Min  | Max  | Unit |
|-----------------------------------|--------|------|------|------|
| Operating Temperature<br>(Industrial Standard) | Ta     | -40  | +85  | °C   |
| Junction Temperature              | Tj     | N/A  | 125  | ℃    |
| Storage Temperature               | Tstg   | -40  | 125  | ℃    |

### 5.3 Pin Max Currents

| Item             | Symbol/Pin       | Max   | Unit |
|------------------|------------------|-------|------|
| Digital Power    | VCC_M1           | 10000 | mA   |
| PLL              | AVDD09_PLL       | 5     | mA   |
| PLL              | AVDD18_PLL       | 5     | mA   |
| OSC              | AVDD09_AFEAP     | 5     | mA   |
| OSC              | AVDD18_AFEAP     | 5     | mA   |
| PCIeC            | AVDD18_PCIEC     | 50    | mA   |
| PCIeC            | AVDD09_PCIEC     | 100   | mA   |
| PCIeB            | AVDD18_PCIEB     | 50    | mA   |
| PCIeB            | AVDD09_PCIEB     | 100   | mA   |
| PCIeA            | AVDD18_PCIEA     | 50    | mA   |
| PCIeA            | AVDD09_PCIEA     | 100   | mA   |
| USB IO           | AVDD33_USB       | 90    | mA   |
| USB PHY          | AVDD18_USB       | 90    | mA   |
| USB PHY          | AVDD09_USB       | 15    | mA   |
| MIPI DSI PHY     | AVDD09_DSI1      | 20    | mA   |
| MIPI DSI PHY     | AVDD18_DSI1      | 50    | mA   |
| MIPI DSI IO      | AVDD12_DSI1      | 50    | mA   |
| MIPI CSI PHY     | AVDD09_CSI       | 70    | mA   |
| MIPI CSI PHY     | AVDD18_CSI       | 100   | mA   |
| HDMI             | AVDD09_HDMI      | 10    | mA   |
| HDMI             | AVDD18_HDMI      | 10    | mA   |
| HDMI             | AVDD33_HDMI      | 10    | mA   |
| eMMC             | VDD09_EMMC       | 50    | mA   |
| eMMC             | V18_EMMC         | 50    | mA   |
| QSPI             | VCC1833_QSPI     | 150   | mA   |
| SD               | VCC1833_MMC1     | 150   | mA   |
| DDR PHY          | AVDD18_PHY       | 200   | mA   |
| DDR PHY          | AVDD18_DDR       | 20    | mA   |
| DDR PHY          | AVDD11_DDR       | 100   | mA   |
| DDR PHY          | AVDDU_PHY        | 100   | mA   |
| DDR PHY          | AVDDU_DDR        | 100   | mA   |
| DDR IO           | AVDD06_DDR       | 100   | mA   |
| DDR IO           | VDDQ_V1P2        | 600   | mA   |
| eFuse            | AVDD18_EFUSE     | 150   | mA   |
| Audio Logic      | AUD_VDDU09       | 1     | mA   |
| Audio Power NEG  | AUD_VNEG         | 102   | mA   |
| Audio Power POS  | AUD_VPOS         | 102   | mA   |
| Audio Analog     | AVDD18_AUD       | 10    | mA   |
| Audio Analog     | AVDD3V3_AUD      | 100   | mA   |

### 5.4 Power On/Off Sequence

#### Power On Sequence

- A short pressure (i.e. 1 second) of the power button will turn on the K1 processor automatically if it was off before (cold start)
- The Power Management IC (PMIC) will turn on <u>firstly</u> the core logic <u>then</u> the external I/O to ensure proper initialization
- PMIC will asserts a Power-On-Reset (POR) to initialize the system and ensure a defined starting state

The order of the involved pins with state change during the power on sequence is depicted below.

<img src="static/power_on.png" alt="" width="600">

#### Power Off Sequence

- A long pressure (i.e. 6 seconds) of the power button will turn off the K1 processor.

The order of the involved pins with state change during the power off sequence is depicted below.

<img src="static/power_off.png" alt="" width="600">

### 5.5 Power Consumption

#### In Typical Application Scenarios

> TBD

#### In Particular Application Scenarios

> TBD
