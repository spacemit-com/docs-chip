sidebar_position: 1

# K1 Datasheet

## Complete Version in PDF

Please click to download the complete version in PDF: **[K1 Datasheet (PDF)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Datasheet_%28V7.5_2025.08.06%29.pdf)**

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
    - For camera, G-Sensor, E-COMPASS, Proximit-Sensor, Light-Sensor, Gyro, Fingerprint, NFC, PMIC, Touch, etc.
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
    - Compatible with 8bit eMMC5.1, up to HS400 (200MHz)
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
  - Secure Boot
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
  - Support for OpenCL3.0 / OpenGL ES 3.2 / Vulkan1.3
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
> - The system supports dual-camera video stream processing (RAW). In the “4-Lane + 2-Lane + 2-Lane mode (triple sensor)” as per **Section 2.3.1**, one sensor must be a YUV input format source, and the write path should not use the MMU.
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

<img src="static/V2D_work_scenario.png" alt="" width="600">

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

<table>
<tbody>
<tr>
<td><strong>Variable</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>Rect_left<br/>Rect_top</td>
<td>16bit unsigned</td>
<td>Range [0, 65535]</td>
</tr>
<tr>
<td>Rect_width<br/>Rect_height</td>
<td>5bit unsigned</td>
<td>Range [1, 16]</td>
</tr>
<tr>
<td>Rect_x<br/>Rect_y</td>
<td>16bit unsigned</td>
<td>Range [0, 65535]<br/>Pixel global position</td>
</tr>
<tr>
<td>c0, c1, c2, c3</td>
<td>8bit unsigned</td>
<td>Range [0, 255]</td>
</tr>
<tr>
<td>byte_low<br/>byte_high</td>
<td>8bit unsigned</td>
<td>Range [0, 255]<br/>byte_low: lower byte in RGB565<br/>byte_high: higher byte in RGB565</td>
</tr>
<tr>
<td>data[4][256]</td>
<td>8bit unsigned × 4 × 256</td>
<td>Range [0, 255]</td>
</tr>
<tr>
<td>index</td>
<td>8bit unsigned</td>
<td>Range [0, 255]</td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr>
<td><strong>Register</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>LayerX_format</td>
<td>X is either 0 or 1, refer to module register</td>
</tr>
<tr>
<td>LayerX_swap</td>
<td>X is either 0 or 1, refer to module register</td>
</tr>
</tbody>
</table>

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

<table>
<tbody>
<tr>
<td><strong>Variable</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>Rect_left, Rect_top</td>
<td>16bit unsigned</td>
<td>Range [0, 65535]</td>
</tr>
<tr>
<td>Rect_width, Rect_height</td>
<td>5bit unsigned</td>
<td>Range [1, 16]</td>
</tr>
<tr>
<td>Rect_x, Rect_y</td>
<td>16bit unsigned<br/></td>
<td>Range [0, 65535]<br/>Pixel global position</td>
</tr>
<tr>
<td>c0, c1, c2, c3</td>
<td>8bit unsigned</td>
<td>Range [0, 255]</td>
</tr>
<tr>
<td>data[4][256]</td>
<td>8bit unsigned × 4 × 256</td>
<td>Range [0, 255]</td>
</tr>
<tr>
<td>index</td>
<td>8bit unsigned</td>
<td>Range [0, 255]</td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr>
<td><strong>Register</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>LayerX_solid_enable</td>
<td>X is 0 or 1, refer to module register</td>
</tr>
<tr>
<td>LayerX_solid_R</td>
<td>X is 0 or 1, refer to module register</td>
</tr>
<tr>
<td>LayerX_solid_G</td>
<td>X is 0 or 1, refer to module register</td>
</tr>
<tr>
<td>LayerX_solid_B</td>
<td>X is 0 or 1, refer to module register</td>
</tr>
<tr>
<td>LayerX_solid_A</td>
<td>X is 0 or 1, refer to module register</td>
</tr>
</tbody>
</table>

###### Rotation

Support for 0°, 90°, 180°, 270° rotation (performed clockwise) as well as mirror and flip option, as depicted below (example).

<img src="static/Rotation.png" alt="" width="200">

The code for rotating, mirroring and flipping graphical content is listed below, and the details of the specific variables and registers involved are tabled immediately after).

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

<table>
<tbody>
<tr>
<td><strong>Variable</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>Rect_left, Rect_top</td>
<td>16bit unsigned</td>
<td>Range [0, 65535]</td>
</tr>
<tr>
<td>Rect_width, Rect_height</td>
<td>5bit unsigned</td>
<td>Range [1, 16]</td>
</tr>
<tr>
<td>Block_rect_left, Block_rect_top</td>
<td>16bit unsigned</td>
<td>Range [0, 65535]</td>
</tr>
<tr>
<td>Block_rect_width, Block_rect_height</td>
<td>5bit unsigned</td>
<td>Range [1, 16]</td>
</tr>
<tr>
<td>data_in[4][256], <br/>data_out[4][256]</td>
<td>8bit unsigned × 4 × 256</td>
<td>Range [0, 255]</td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr>
<td><strong>Register</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>LayerX_degree</td>
<td>3bit unsigned</td>
<td>X is 0 or 1, refer to module register</td>
</tr>
<tr>
<td>LayerX_width, LayerX_height</td>
<td>16bit unsigned</td>
<td>X is 0 or 1, refer to module register</td>
</tr>
</tbody>
</table>

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

<table>
<tbody>
<tr>
<td><strong>Variable</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>C0in, C1in, C2in, C3in</td>
<td>8bit unsigned</td>
<td>Input channel</td>
</tr>
<tr>
<td>C0inter, C1inter, C2inter</td>
<td>10bit signed</td>
<td>Intermediate channel value</td>
</tr>
<tr>
<td>C0out, C1out, C2out, C3out</td>
<td>8bit unsigned</td>
<td>Output channel</td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr>
<td><strong>Register</strong></td>
<td><strong>Index</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>LayerX_CSC_enable<br/></td>
<td>-</td>
<td>1bit unsigned<br/></td>
<td>0: disable<br/>1: enable</td>
</tr>
<tr>
<td>Layer_matrix[#][#]</td>
<td>0-11</td>
<td>13bit signed<br/></td>
<td>Range [-4096, 4095] </td>
</tr>
</tbody>
</table>

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

<table>
<tbody>
<tr>
<td><strong>Variable</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>Rect_left<br/>Rect_top</td>
<td>16bit unsigned</td>
<td>Range [0, 65535]</td>
</tr>
<tr>
<td>Rect_width<br/>Rect_height</td>
<td>5bit unsigned</td>
<td>Range [1, 16]</td>
</tr>
<tr>
<td>pixel_index</td>
<td>8bit unsigned</td>
<td>Range [0, 65535]</td>
</tr>
<tr>
<td>s0, s1, s2, s3</td>
<td>8bit unsigned</td>
<td>Range [0, 255]</td>
</tr>
<tr>
<td>Y00, Y01, Y10, Y11, U00, U01, <br/>U10, U11, V00, V01, V10, V11, <br/>U, V, R, G, B, A</td>
<td>8bit unsigned</td>
<td>Range [0, 255]</td>
</tr>
<tr>
<td>data_in[4][256]</td>
<td>8bit unsigned × 4 × 256</td>
<td>Range [0, 255]</td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr>
<td><strong>Register</strong></td>
<td><strong>Bit</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr>
<td>Output_format</td>
<td>3bit unsigned</td>
<td>0: RGB888  (R at low address, B at high address)<br/>1: RGBX8888<br/>2: RGBA8888<br/>3: ARGB8888 (A at low address, B at high address)<br/>5: yuv420sp (U at low address, V at high address)</td>
</tr>
<tr>
<td>Output_swap</td>
<td>1bit unsigned</td>
<td>0: No swap<br/>1: RGB swap RB, YUV swap UV</td>
</tr>
<tr>
<td>Output_layout</td>
<td>1bit unsigned</td>
<td>0: Linear<br/>1: FBC compressed </td>
</tr>
<tr>
<td>Output_crop_left</td>
<td>16bit unsigned</td>
<td>Range [0, 65534] crop_left &lt; output_left + output_width</td>
</tr>
<tr>
<td>Output_crop_top</td>
<td>16bit unsigned</td>
<td>Range [0, 65534] crop_top &lt; output_top + output_height</td>
</tr>
<tr>
<td>Output_crop_width</td>
<td>16bit unsigned</td>
<td>Range [1, 65535] <br/>crop_left + crop_wdith ≤ output_left + output_width</td>
</tr>
<tr>
<td>Output_crop_height</td>
<td>16bit unsigned</td>
<td>Range [1, 65535] <br/>crop_top + crop_height ≤ output_top + output_height</td>
</tr>
</tbody>
</table>

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

### MIPI DSI Interface

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

<img src="static/blending_function.png" alt="" width="500">

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

  > **Not****e.** Alpha value is not supported for write-back in this case
  >

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
  >

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

  - $$
    L'=L1+L0×a1
    $$
- For **3 layers** (<u>not recommended</u>), the formula implemented is

  - $$
    L'=L2+L1×a2+L0×a1×a2
    $$

  > **Note****.**Alpha value is not supported for write-back in this case
  >

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
- Support forAutomatic Lane Flip and Reversal
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

<table>
<tbody>
<tr>
<td></td>
<td><strong>Internal Mem</strong><strong>ory</strong></td>
<td><strong>External Mem</strong><strong>ory</strong></td>
<td><strong>Internal Peri</strong><strong>pheral</strong></td>
<td><strong>External Peri</strong><strong>pheral</strong></td>
</tr>
<tr>
<td><strong>Internal Mem</strong><strong>ory</strong></td>
<td>Flow-Through Mode</td>
<td> ___</td>
<td> ___</td>
<td> ___</td>
</tr>
<tr>
<td><strong>External Mem</strong><strong>ory</strong></td>
<td>Flow-Through Mode</td>
<td>Flow-Through Mode</td>
<td> ___</td>
<td> ___</td>
</tr>
<tr>
<td><strong>Internal Peri</strong><strong>pheral</strong></td>
<td>Flow-Through Mode</td>
<td>Flow-Through Mode</td>
<td>___</td>
<td>___ </td>
</tr>
<tr>
<td><strong>External Peri</strong><strong>pheral</strong></td>
<td>Flow-Through Mode</td>
<td>Flow-Through Mode</td>
<td>___</td>
<td>___</td>
</tr>
</tbody>
</table>

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
  - Fast count mode by input clock frequency of 12.8 MHz, 6.4 MHz, 3 MHz or 1 MHz)
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

#### GPI

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

###### PLL

PLL1 is designed to generate fixed frequency points for the CPU cores and other peripherals, where

- Changes of the run-time frequency in the PLL1 output are only available for debugging purposes and should not be used in production systems
- PLL1 is enabled by default at system reset and shutdown only when the entire chip entered sleep mode with VCXO shutdown enabled
- The settings configured in the PLL1 and oscillator control registers of the Main PMU control the delay required for the PLL1 output clocks to stabilize after system reset or shutdown
- Updating the PLL1 configuration registers to change frequency during normal operations is not recommended

###### PLL2

PLL2 is designed to generate various fixed frequencies, working alongside PLL1 to provide a full range of frequencies required for different modules, where

- Changes of run-time frequency in the PLL2 output are only available for debugging purposes and should not be used in production systems
- PLL2 is disabled at system reset and must be enabled through software when required
- The settings configured in the PLL2 and oscillator control registers of the Main PMU control the delay required for the PLL2 output clocks to stabilize after system reset or shutdown
- Updating the PLL2 configuration registers to change frequency during normal operations is not recommended

###### PLL3

PLL3 is designed to provide frequencies for CPU frequency scaling and switching, where

- PLL3 is disabled at system reset and must be enabled through software when required
- The settings configured in the PLL3 and oscillator control register of the Main PMU control the delay required for the PLL3 output clocks to stabilize after system reset or shutdown
- Updating the PLL3 configuration registers to change frequency during normal operations is not recommended

##### Resource Reset Scheme

K1 allows applying different schemes of resource reset as tabled below.

<table>
<tbody>
<tr>
<td><strong>No.</strong></td>
<td><strong>Resource Reset Scheme</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr>
<td>1</td>
<td>Power-On-Reset</td>
<td>Reset the whole chip during power-on sequence</td>
</tr>
<tr>
<td>2</td>
<td>WatchDog Reset</td>
<td>Reset the whole chip excluding pinmux registers and debug registers</td>
</tr>
<tr>
<td>3</td>
<td>Module Software Reset</td>
<td>Reset each module individually through software</td>
</tr>
<tr>
<td>4</td>
<td>Power Island POR Reset</td>
<td>Reset the whole power island during its power-on sequence</td>
</tr>
</tbody>
</table>

### 2.12 Boot Modes

#### Introduction

K1 supports booting from

- SPI NAND Flash
- SPI NOR Flash
- eMMC
- SD/TF Card

The details of the boot mode selection are tabled below.

<table>
<tbody>
<tr>
<td><strong>N</strong><strong>o</strong><strong>.</strong></td>
<td><strong>QSPI_DATA[1]</strong><strong> </strong><strong>/</strong><strong> </strong><strong>STRAP[1]</strong></td>
<td><strong>QSPI_DATA[0]</strong><strong> </strong><strong>/</strong><strong> </strong><strong>STRAP[0]</strong></td>
<td><strong>Boot Mode</strong></td>
</tr>
<tr>
<td>1</td>
<td>Down</td>
<td>Down</td>
<td>SD/TF Card -&gt; EMMC (default)</td>
</tr>
<tr>
<td>2</td>
<td>Up</td>
<td>Down</td>
<td>SD/TF Card -&gt; SPI NAND Flash</td>
</tr>
<tr>
<td>3</td>
<td>Down</td>
<td>Up</td>
<td>SD/TF Card -&gt; SPI NOR Flash</td>
</tr>
<tr>
<td>4</td>
<td>Up</td>
<td>Up</td>
<td>SD/TF Card</td>
</tr>
</tbody>
</table>

### 2.13 Power Management Unit

#### Introduction

A two-level power management strategy is implemented to control various granularities of power consumption. Different power domains and power states are also defined to achieve ultra-low power consumption.

A total of 9 power domains are implemented, and they are for

- CPU cores

  > **Note.** Each CPU core has its own power domain independently controlled
  >
- CPU clusters

  > **Note.** Each CPU cluster has its own power domain independently controlled
  >
- Video Encoder/Decoder
- GPU
- HDMI Display Subsystem
- MIPI DSI Subsystem
- Video Input Subsystem
- RCPU (including N308, Audio Codec, RCPU Peripherals)
- Always-On-Domain (AON)

All those power domains, except AON, can be powered off depending on specific application scenarios.

In order to achieve the minimal power consumption, different power states are designed as tabled below:

<table>
<tbody>
<tr>
<td><strong>No.</strong></td>
<td><strong>Power State Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr>
<td>1</td>
<td>ACTIVE </td>
<td>The system is alive and active, with all power domains on, except those power domains with power switches that can be turned off selectively and independently.</td>
</tr>
<tr>
<td>2</td>
<td>CORE-IDLE</td>
<td>Each core stops executing instructions and enters an idle state, with clock gating automatically after a Wait-for-Interrupt (WFI) execution. The core exits this state  when receiving an interrupt routed to it and continues execution.</td>
</tr>
<tr>
<td>3</td>
<td>Core-Power-Off</td>
<td>Each core, when voted, enters a power-off state after Core-Idle sleep mode. The core exits this state when receiving an interrupt, with power turned on and reset released.</td>
</tr>
<tr>
<td>4</td>
<td>CPU-Cluster-Power-Off<br/></td>
<td>Each CPU cluster, when voted, enters this low-power state after all cores within this cluster have entered the Core-Power-Off state, with L2/TCM memory also shut down. <br/>Any active interrupt routing to CPU cores in this cluster would bring CPU cluster out of this state, then power on, clock resume and reset release.  </td>
</tr>
<tr>
<td>5</td>
<td>Home-Screen</td>
<td>The main bus fabric AXI clock is gated off (if voted) after both CPU clusters enter CPU-Cluster-Power-Off mode.<br/>Any interrupt will wake up the chip from this state by resuming the main bus AXI clock, and powering up the corresponding CPU cluster and CPU core to which the interrupt is routed, resuming the CPU clock, and releasing the reset to service the interrupt routine. </td>
</tr>
<tr>
<td>6</td>
<td>Chip-Sleep</td>
<td>This is the most ultra-low power state, with all PLLs/Power islands off. Only 32K RTC clock remains alive, and the 24M VCXO can be configured to be on or off. <br/>In this state only the logic/IO in AON domain alives, and a pin named SLEEP_OUT connected to PMIC would be deasserted to signal PMIC to lower the VCC power supply voltage to reduce lower power comsumption.</td>
</tr>
<tr>
<td>7</td>
<td>RCPU with SOC LP</td>
<td>RCPU power domain is an independent power island and can function in any of above PMU states. RCPU can vote for different SoC low-power states according to its specific scenario requirements. <br/>The RCPU itself has four low-power states as follows: <br/>- Active Mode: Clock running<br/>- ClkGate Mode: Clock gating <br/>- PLL Off Mode: PLL powered off<br/>- Power Off Mode: RCPU power is shut down, but the RCPU AON domain remains alive</td>
</tr>
</tbody>
</table>

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

<table>
<tbody>
<tr>
<td><strong>Type</strong></td>
<td><strong>Size</strong></td>
<td><strong>Pin P</strong><strong>itch</strong></td>
<td><strong>Pin Count</strong></td>
</tr>
<tr>
<td>FCCSP</td>
<td>17×17 mm</td>
<td>0.65 mm</td>
<td>676<br/>(26x26)</td>
</tr>
<tr>
<td>FCBGA</td>
<td>19×19 mm</td>
<td>0.65 mm</td>
<td>676<br/>(26x26)</td>
</tr>
</tbody>
</table>

The related package outline drawing (POD) are depicted in the following sections.

### 3.2 FCCSP Type

![](static/POD_1.png)

![](static/POD_2.png)

<table>
<tbody>
<tr>
<td rowspan=3 colspan=2><strong>Item</strong></td>
<td rowspan=3 colspan=1><strong>Symbol</strong></td>
<td rowspan=2 colspan=3><strong>Dimen</strong><strong>sion (in mm)</strong></td>
</tr>
<tr>
</tr>
<tr>
<td><strong>M</strong><strong>in</strong></td>
<td><strong>Typ</strong></td>
<td><strong>M</strong><strong>ax</strong></td>
</tr>
<tr>
<td rowspan=1 colspan=2>Total thickness</td>
<td>A</td>
<td>0.890 </td>
<td>0.990 </td>
<td>1.090 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin stand off</td>
<td>A1</td>
<td>0.160 </td>
<td>0.210 </td>
<td>0.260 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>Substrate + Die + Mold</td>
<td>A2</td>
<td>0.710 </td>
<td>0.780 </td>
<td>0.850 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>Substrate + Die</td>
<td>c</td>
<td>0.290 </td>
<td>0.330 </td>
<td>0.370 </td>
</tr>
<tr>
<td rowspan=2 colspan=1>Body size</td>
<td>X direction</td>
<td>D</td>
<td>16.900 </td>
<td>17.000 </td>
<td>17.100 </td>
</tr>
<tr>
<td>Y direction</td>
<td>E</td>
<td>16.900 </td>
<td>17.000 </td>
<td>17.100 </td>
</tr>
<tr>
<td rowspan=2 colspan=1>Edge pin center to center</td>
<td>X direction</td>
<td>D1</td>
<td>—</td>
<td>16.250 </td>
<td>—</td>
</tr>
<tr>
<td>Y direction</td>
<td>E1</td>
<td>—</td>
<td>16.250</td>
<td>—</td>
</tr>
<tr>
<td>Pin pitch </td>
<td>X/Y direction</td>
<td>e</td>
<td>—</td>
<td>0.650 </td>
<td>—</td>
</tr>
<tr>
<td>Pin width</td>
<td></td>
<td>b</td>
<td>0.250 </td>
<td>0.300 </td>
<td>0.350 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>Package edge tolerance</td>
<td>aaa</td>
<td rowspan=1 colspan=3>0.100 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>HAT flatness</td>
<td>bbb</td>
<td rowspan=1 colspan=3>0.100 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>Coplanarity</td>
<td>ddd</td>
<td rowspan=1 colspan=3>0.100 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin offset (package)</td>
<td>eee</td>
<td rowspan=1 colspan=3>0.150 </td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin offset (ball)</td>
<td>fff</td>
<td rowspan=1 colspan=3>0.080 </td>
</tr>
<tr>
<td rowspan=1 colspan=3>Pin diameter</td>
<td rowspan=1 colspan=3>0.300 </td>
</tr>
<tr>
<td rowspan=1 colspan=3>Pin count</td>
<td rowspan=1 colspan=3>676 </td>
</tr>
<tr>
<td rowspan=1 colspan=3>MD/ME</td>
<td rowspan=1 colspan=3>26/26</td>
</tr>
</tbody>
</table>

### 3.3 FCBGA Type

![](static/POD_3.png)

<table>
<tbody>
<tr>
<td rowspan=2 colspan=2><strong>Item </strong></td>
<td rowspan=2 colspan=1><strong>Symbol </strong></td>
<td rowspan=1 colspan=3><strong>Dimension</strong><strong> (in mm)</strong></td>
</tr>
<tr>
<td><strong>M</strong><strong>in</strong></td>
<td><strong>Typ</strong></td>
<td><strong>M</strong><strong>ax</strong></td>
</tr>
<tr>
<td rowspan=2 colspan=1>Body size</td>
<td>X direction</td>
<td>D</td>
<td>18.900</td>
<td>19.000</td>
<td>19.100</td>
</tr>
<tr>
<td>Y direction</td>
<td>E</td>
<td>18.900</td>
<td>19.000</td>
<td>19.100</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Pin pitch </td>
<td>X direction</td>
<td>eD</td>
<td rowspan=1 colspan=3>0.650</td>
</tr>
<tr>
<td>Y direction</td>
<td>eE</td>
<td rowspan=1 colspan=3>0.650</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Total thickness</td>
<td>A</td>
<td>2.157</td>
<td>2.257</td>
<td>2.357</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Hat + Adhesive</td>
<td>A3</td>
<td>1.322</td>
<td>1.375</td>
<td>1.428</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Substrate thickness</td>
<td>c</td>
<td>0.602</td>
<td>0.672</td>
<td>0.742</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin stand off</td>
<td>A1</td>
<td>0.169</td>
<td>0.210</td>
<td>0.260</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin width</td>
<td>b</td>
<td>0.250</td>
<td>0.300</td>
<td>0.350</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Package edge tolerance</td>
<td>aaa</td>
<td rowspan=1 colspan=3>0.150</td>
</tr>
<tr>
<td rowspan=1 colspan=2>HAT flatness</td>
<td>ccc</td>
<td rowspan=1 colspan=3>0.350</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Coplanarity</td>
<td>ddd</td>
<td rowspan=1 colspan=3>0.080</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin offset (package)</td>
<td>eee</td>
<td rowspan=1 colspan=3>0.150</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin offset (ball)</td>
<td>fff</td>
<td rowspan=1 colspan=3>0.080</td>
</tr>
<tr>
<td rowspan=1 colspan=2>Pin count</td>
<td>n</td>
<td rowspan=1 colspan=3>676</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Edge pin center to center</td>
<td>X direction</td>
<td>D1</td>
<td rowspan=1 colspan=3>16.250</td>
</tr>
<tr>
<td>Y direction</td>
<td>E1</td>
<td rowspan=1 colspan=3>16.250</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Edge pin center to package edge</td>
<td>X direction</td>
<td>gD</td>
<td rowspan=1 colspan=3>1.375</td>
</tr>
<tr>
<td>Y direction</td>
<td>gE</td>
<td rowspan=1 colspan=3>1.375</td>
</tr>
</tbody>
</table>

## 4. Pinout

### 4.1 Introduction

The two available packages of K1 as per **Chapter 3** are <u>pin-to-pin</u>.

### 4.2 Pinout Diagram & Description

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

<table>
<tbody>
<tr>
<td><strong>Pin ID</strong></td>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
<td><strong>Power Domain</strong></td>
<td><strong>Function</strong></td>
</tr>
<tr>
<td>A1</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>A2</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>A3</td>
<td>DQ_B_2</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ2 <br/>LPDDR3: DQ28</td>
</tr>
<tr>
<td>A4</td>
<td>DMI0_B</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Channel B DM0 <br/>LPDDR3: DQ25</td>
</tr>
<tr>
<td>A5</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>A6</td>
<td>DQ_B_6</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ6 <br/>LPDDR3: DQ24</td>
</tr>
<tr>
<td>A7</td>
<td>DQ_B_4</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ4 <br/>LPDDR3: DQ30</td>
</tr>
<tr>
<td>A8</td>
<td>DQ_B_13</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ13 <br/>LPDDR3: DQ15</td>
</tr>
<tr>
<td>A9</td>
<td>DQ_B_15</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ15 <br/>LPDDR3: DQ12</td>
</tr>
<tr>
<td>A10</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>A11</td>
<td>DQ_B_9</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ9<br/>LPDDR3: DQ8</td>
</tr>
<tr>
<td>A12</td>
<td>DQ_B_12</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ12<br/>LPDDR3: DQ10</td>
</tr>
<tr>
<td>A13</td>
<td>DQ_B_11</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ11<br/>LPDDR3: DQ11</td>
</tr>
<tr>
<td>B1</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>B2</td>
<td>DQ_B_3</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ3<br/>LPDDR3: DQM3</td>
</tr>
<tr>
<td>B3</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>B4</td>
<td>DQ_B_1</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ1<br/>LPDDR3: DQ27</td>
</tr>
<tr>
<td>B5</td>
<td>DQ_B_0</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ0<br/>LPDDR3: DQ31</td>
</tr>
<tr>
<td>B6</td>
<td>DQ_B_7</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ7<br/>LPDDR3: DQ29</td>
</tr>
<tr>
<td>B7</td>
<td>DQ_B_5</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ5<br/>LPDDR3: DQ26</td>
</tr>
<tr>
<td>B8</td>
<td>VDDQ_V1P2</td>
<td>P</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR3 IO power</td>
</tr>
<tr>
<td>B9</td>
<td>DQ_B_14</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ14<br/>LPDDR3: DQ13</td>
</tr>
<tr>
<td>B10</td>
<td>DMI1_B</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Channel B DM1<br/>LPDDR3: DQ14</td>
</tr>
<tr>
<td>B11</td>
<td>DQ_B_8</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ12<br/>LPDDR3: DQM1</td>
</tr>
<tr>
<td>B12</td>
<td>DQ_B_10</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ10<br/>LPDDR3: DQ9</td>
</tr>
<tr>
<td>B13</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>C1</td>
<td>GPIO_58</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 58</td>
</tr>
<tr>
<td>C2</td>
<td>GPIO_57</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 57</td>
</tr>
<tr>
<td>C3</td>
<td>GPIO_56</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 56</td>
</tr>
<tr>
<td>C4</td>
<td>GPIO_55</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 55</td>
</tr>
<tr>
<td>C5</td>
<td>GPIO_54</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 54</td>
</tr>
<tr>
<td>C6</td>
<td>DQS0_T_B</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Positive of CHB DQS0<br/>LPDDR3: Positive of DQS3</td>
</tr>
<tr>
<td>C7</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>C8</td>
<td>CS1_B</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Active-low chip select 1 of CHB<br/>LPDDR3: N/A</td>
</tr>
<tr>
<td>C9</td>
<td>CA_B_1</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB CA1<br/>LPDDR3: CA5</td>
</tr>
<tr>
<td>C10</td>
<td>CKE0_B</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 1.1V</td>
<td>LPDDR4X: clock enabling 0 of CHB<br/>LPDDR3: N/A</td>
</tr>
<tr>
<td>C11</td>
<td>CKE1_B</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 1.1V</td>
<td>LPDDR4X: clock enabling 1 of CHB<br/>LPDDR3: N/A</td>
</tr>
<tr>
<td>C12</td>
<td>VDDQ_V1P2</td>
<td>P</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR3 IO power</td>
</tr>
<tr>
<td>C13</td>
<td>CA_B_5</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB CA5<br/>LPDDR3: CA8</td>
</tr>
<tr>
<td>D1</td>
<td>GPIO_114</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 114</td>
</tr>
<tr>
<td>D2</td>
<td>GPIO_113</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 113</td>
</tr>
<tr>
<td>D3</td>
<td>GPIO_112</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 112</td>
</tr>
<tr>
<td>D4</td>
<td>GPIO_111</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 111</td>
</tr>
<tr>
<td>D5</td>
<td>GPIO_53</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 53</td>
</tr>
<tr>
<td>D6</td>
<td>DQS0_C_B</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Negative of CHB DQS0<br/>LPDDR3: Negtive of DQS3</td>
</tr>
<tr>
<td>D7</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>D8</td>
<td>CA_B_0</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB CA0</td>
</tr>
<tr>
<td>D9</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>D10</td>
<td>DDR_lp4x_SEL</td>
<td>AIO</td>
<td>1.8V</td>
<td>LPDDR4X: connect to 1.8V<br/>LP234: connect to Ground</td>
</tr>
<tr>
<td>D11</td>
<td>CK_C_B</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: negative LPDDR differential clock of CHB <br/>LPDDR3: negative LPDDR differential clock</td>
</tr>
<tr>
<td>D12</td>
<td>CA_B_2</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB CA2<br/>LPDDR3: CA9</td>
</tr>
<tr>
<td>D13</td>
<td>CA_B_4</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA CA4<br/>LPDDR3: CA7</td>
</tr>
<tr>
<td>E1</td>
<td>GPIO_67</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 67</td>
</tr>
<tr>
<td>E2</td>
<td>GPIO_65</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 65</td>
</tr>
<tr>
<td>E3</td>
<td>GPIO_64</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 64</td>
</tr>
<tr>
<td>E4</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>E5</td>
<td>GPIO_63</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 63</td>
</tr>
<tr>
<td>E6</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>E7</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>E8</td>
<td>VDDQ_V1P2</td>
<td>P</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR3 IO power</td>
</tr>
<tr>
<td>E9</td>
<td>DDR_LP23_VREFDQ</td>
<td>P</td>
<td>lp3: 0.6V<br/>lp4: high-z</td>
<td>DQ VREF for lpddr23 , LP4/4x<br/>Keep the pin NC</td>
</tr>
<tr>
<td>E10</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>E11</td>
<td>CK_T_B</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: positive LPDDR differential clock of CHB<br/>LPDDR3: positive LPDDR differential clock</td>
</tr>
<tr>
<td>E12</td>
<td>CA_B_3</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB CA3 <br/>LPDDR3: CA6</td>
</tr>
<tr>
<td>E13</td>
<td>AVSS18_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>F1</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>F2</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>F3</td>
<td>GPIO_69</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 69</td>
</tr>
<tr>
<td>F4</td>
<td>GPIO_68</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 68</td>
</tr>
<tr>
<td>F5</td>
<td>GPIO_66</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 66</td>
</tr>
<tr>
<td>F6</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>F7</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>F8</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>F9</td>
<td>VDDQ_V1P2</td>
<td>P</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR3 IO power</td>
</tr>
<tr>
<td>F10</td>
<td>VDDQ_V1P2</td>
<td>P</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR3 IO power</td>
</tr>
<tr>
<td>F11</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>F12</td>
<td>CS0_B</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: clock enabling 1 of CHB<br/>LPDDR3: N/A</td>
</tr>
<tr>
<td>F13</td>
<td>DDR_RESET_N</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 1.1V</td>
<td>LPDDR SDRAM reset</td>
</tr>
<tr>
<td>G1</td>
<td>MIPI_CSI1_D1N</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA1LANEN</td>
</tr>
<tr>
<td>G2</td>
<td>MIPI_CSI1_D1P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA1LANEP</td>
</tr>
<tr>
<td>G3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>G4</td>
<td>MIPI_CSI1_D0N</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA0LANEN</td>
</tr>
<tr>
<td>G5</td>
<td>MIPI_CSI1_D0P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA0LANEP</td>
</tr>
<tr>
<td>G6</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>G7</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>G8</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>G9</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>G10</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>G11</td>
<td>VDDQ_V1P2</td>
<td>P</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR3 IO power</td>
</tr>
<tr>
<td>G12</td>
<td>AVDD11_DDR</td>
<td>P</td>
<td>lp4x: 1.1V<br/>lp4: 1.1V<br/>lp3: 1.2V</td>
<td>LPDDR PHY power supply<br/></td>
</tr>
<tr>
<td>G13</td>
<td>VDDQ_V1P2</td>
<td>P</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR3 IO power</td>
</tr>
<tr>
<td>H1</td>
<td>MIPI_CSI1_D2N</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA2LANEN</td>
</tr>
<tr>
<td>H2</td>
<td>MIPI_CSI1_D2P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA2LANEP</td>
</tr>
<tr>
<td>H3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>H4</td>
<td>MIPI_CSI1_CLKN</td>
<td>AO</td>
<td>1.8V</td>
<td>CSI1 CKLANEN</td>
</tr>
<tr>
<td>H5</td>
<td>MIPI_CSI1_CLKP</td>
<td>AO</td>
<td>1.8V</td>
<td>CSI1 CKLANEP</td>
</tr>
<tr>
<td>H6</td>
<td>AVSS18_AFEAP</td>
<td>G</td>
<td>0V</td>
<td>DCXO Ground</td>
</tr>
<tr>
<td>H7</td>
<td>XI_PAD</td>
<td>AI</td>
<td>1.8V</td>
<td>DCXO crystal input</td>
</tr>
<tr>
<td>H8</td>
<td>AVSS18_AFEAP</td>
<td>G</td>
<td>0V</td>
<td>DCXO Ground</td>
</tr>
<tr>
<td>H9</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>H10</td>
<td>VSSU_DDR</td>
<td>G</td>
<td>0V</td>
<td>system DDR Ground</td>
</tr>
<tr>
<td>H11</td>
<td>VSSU_DDR</td>
<td>G</td>
<td>0V</td>
<td>system DDR Ground</td>
</tr>
<tr>
<td>H12</td>
<td>AVDD18_PHY</td>
<td>P</td>
<td>1.8V</td>
<td>Analog 1.8V power</td>
</tr>
<tr>
<td>H13</td>
<td>AVDDU_DDR</td>
<td>P</td>
<td>0.9V</td>
<td>LPDDR PHY PLL logical power</td>
</tr>
<tr>
<td>J1</td>
<td>MIPI_CSI3_D0N</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI3 DATA0LANEN</td>
</tr>
<tr>
<td>J2</td>
<td>MIPI_CSI3_D0P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI3 DATA0LANEP</td>
</tr>
<tr>
<td>J3</td>
<td>AVSS_CSI</td>
<td>G</td>
<td>0V</td>
<td>MIPI_CSI Ground</td>
</tr>
<tr>
<td>J4</td>
<td>MIPI_CSI1_D3N</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA3LANEN</td>
</tr>
<tr>
<td>J5</td>
<td>MIPI_CSI1_D3P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI1 DATA3LANEP</td>
</tr>
<tr>
<td>J6</td>
<td>AVSS_CSI</td>
<td>G</td>
<td>0V</td>
<td>MIPI_CSI Ground</td>
</tr>
<tr>
<td>J7</td>
<td>XO_PAD</td>
<td>AO</td>
<td>1.8V</td>
<td>DCXO crystal output</td>
</tr>
<tr>
<td>J8</td>
<td>AVSS18_AFEAP</td>
<td>G</td>
<td>0V</td>
<td>DCXO Ground</td>
</tr>
<tr>
<td>J9</td>
<td>AVSS18_AFEAP</td>
<td>G</td>
<td>0V</td>
<td>DCXO Ground</td>
</tr>
<tr>
<td>J10</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>J11</td>
<td>AVDDU_PHY</td>
<td>P</td>
<td>0.9V</td>
<td>LPDDR PHY core logical power </td>
</tr>
<tr>
<td>J12</td>
<td>AVDDU_PHY</td>
<td>P</td>
<td>0.9V</td>
<td>LPDDR PHY core logical power</td>
</tr>
<tr>
<td>J13</td>
<td>AVDDU_PHY</td>
<td>P</td>
<td>0.9V</td>
<td>LPDDR PHY core logical power</td>
</tr>
<tr>
<td>K1</td>
<td>MIPI_CSI3_CLKN</td>
<td>AO</td>
<td>1.8V</td>
<td>CSI3 CKLANEN for CSI3 DATALANE0/1 when CSI3 is configured as two 2ch CSI; <br/>CSI3 CKLANEN for CSI3 DATALANE0/1/2/3 when CSI3 is configured as 4ch CSI</td>
</tr>
<tr>
<td>K2</td>
<td>MIPI_CSI3_CLKP</td>
<td>AO</td>
<td>1.8V</td>
<td>CSI3 CKLANEP for CSI3 DATALANE0/1 when CSI3 is configured as two 2ch CSI; <br/>CSI3 CKLANEP for CSI3 DATALANE0/1/2/3 when CSI3 is configured as 4ch CSI</td>
</tr>
<tr>
<td>K3</td>
<td>AVSS_CSI</td>
<td>G</td>
<td>0V</td>
<td>MIPI_CSI Ground</td>
</tr>
<tr>
<td>K4</td>
<td>MIPI_CSI3_D1N</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI3 DATA1LANEN</td>
</tr>
<tr>
<td>K5</td>
<td>MIPI_CSI3_D1P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI3 DATA1LANEP</td>
</tr>
<tr>
<td>K6</td>
<td>AVDD18_CSI</td>
<td>P</td>
<td>1.8V</td>
<td>MIPI_CSI analog power</td>
</tr>
<tr>
<td>K7</td>
<td>AVDD09_CSI</td>
<td>P</td>
<td>0.9V</td>
<td>MIPI_CSI digtial power</td>
</tr>
<tr>
<td>K8</td>
<td>AVSS_CSI</td>
<td>G</td>
<td>0V</td>
<td>MIPI_CSI Ground</td>
</tr>
<tr>
<td>K9</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>K10</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>K11</td>
<td>BG_OUT</td>
<td>AO</td>
<td>1.8V</td>
<td>Bandgap output</td>
</tr>
<tr>
<td>K12</td>
<td>AVDD18_AFEAP</td>
<td>P</td>
<td>1.8V</td>
<td>1.8V power for DCXO</td>
</tr>
<tr>
<td>K13</td>
<td>MPLL_TST_CK</td>
<td>AIO</td>
<td>1.8V</td>
<td>Analog testpin</td>
</tr>
<tr>
<td>L2</td>
<td>MIPI_CSI3_D2P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI3 DATA2LANEP</td>
</tr>
<tr>
<td>L3</td>
<td>AVSS_CSI</td>
<td>G</td>
<td>0V</td>
<td>MIPI_CSI Ground</td>
</tr>
<tr>
<td>L4</td>
<td>MIPI_CSI2_CLKN</td>
<td>AO</td>
<td>1.8V</td>
<td>CKLANEN for CSI3 DATALANE2/3 when CSI3 is configured as two 2ch CSI; <br/>Disabled when CSI3 is configured as 4ch CSI</td>
</tr>
<tr>
<td>L5</td>
<td>MIPI_CSI2_CLKP</td>
<td>AO</td>
<td>1.8V</td>
<td>CKLANEP for CSI3 DATALANE2/3 when CSI3 is configured as two 2ch CSI; <br/>Disabled when CSI3 is configured as 4ch CSI</td>
</tr>
<tr>
<td>L6</td>
<td>AVDD18_CSI</td>
<td>P</td>
<td>1.8V</td>
<td>MIPI_CSI analog power</td>
</tr>
<tr>
<td>L7</td>
<td>AVDD09_CSI</td>
<td>P</td>
<td>0.9V</td>
<td>MIPI_CSI digtial power</td>
</tr>
<tr>
<td>L8</td>
<td>AVSS_CSI</td>
<td>G</td>
<td>0V</td>
<td>MIPI_CSI Ground</td>
</tr>
<tr>
<td>L9</td>
<td>AVSS_CSI</td>
<td>G</td>
<td>0V</td>
<td>MIPI_CSI Ground</td>
</tr>
<tr>
<td>L10</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>L11</td>
<td>AVDD09_AFEAP</td>
<td>P</td>
<td>0.9V</td>
<td>0.9V power for DCXO</td>
</tr>
<tr>
<td>L12</td>
<td>VSSU_AFEAP</td>
<td>G</td>
<td>0V</td>
<td>DCXO Ground</td>
</tr>
<tr>
<td>L13</td>
<td>AVSS_PLL</td>
<td>G</td>
<td>0V</td>
<td>Analog Core Ground</td>
</tr>
<tr>
<td>M1</td>
<td>MIPI_CSI3_D3N</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI3 DATA3LANEN</td>
</tr>
<tr>
<td>M2</td>
<td>MIPI_CSI3_D3P</td>
<td>AI</td>
<td>1.8V</td>
<td>CSI3 DATA3LANEP</td>
</tr>
<tr>
<td>M3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>M4</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>M5</td>
<td>VSSU_PCIEA</td>
<td>G</td>
<td>0V</td>
<td>PCIEA Ground</td>
</tr>
<tr>
<td>M6</td>
<td>AVDD18_USB</td>
<td>P</td>
<td>1.8V</td>
<td>USB2.0 1.8V power</td>
</tr>
<tr>
<td>M7</td>
<td>AVDD09_USB</td>
<td>P</td>
<td>0.9V</td>
<td>USB2.0 digital power</td>
</tr>
<tr>
<td>M8</td>
<td>VSSU_PCIEA</td>
<td>G</td>
<td>0V</td>
<td>PCIEA Ground</td>
</tr>
<tr>
<td>M9</td>
<td>AVDD33_USB</td>
<td>P</td>
<td>3.3V</td>
<td>USB2.0 3.3V power</td>
</tr>
<tr>
<td>M10</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>M11</td>
<td>AVDD09_PLL</td>
<td>P</td>
<td>0.9</td>
<td>System PLL power supply</td>
</tr>
<tr>
<td>M12</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>M13</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>N1</td>
<td>USB2_DN</td>
<td>AIO</td>
<td>3.3V</td>
<td>USB2.0_2 D- differential data line</td>
</tr>
<tr>
<td>N2</td>
<td>USB2_DP</td>
<td>AIO</td>
<td>3.3V</td>
<td>USB2.0_2 D+ differential data line</td>
</tr>
<tr>
<td>N3</td>
<td>AVSS_USB</td>
<td>G</td>
<td>0V</td>
<td>USB2.0 Ground</td>
</tr>
<tr>
<td>N4</td>
<td>PCIEA_TXN</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEA TXLANEN</td>
</tr>
<tr>
<td>N5</td>
<td>PCIEA_TXP</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEA TXLANEP</td>
</tr>
<tr>
<td>N6</td>
<td>AVDD18_PCIEA</td>
<td>P</td>
<td>1.8V</td>
<td>PCIEA analog power</td>
</tr>
<tr>
<td>N7</td>
<td>AVDD09_PCIEA</td>
<td>P</td>
<td>0.9V</td>
<td>PCIEA digital power</td>
</tr>
<tr>
<td>N8</td>
<td>AVSS_PCIEA</td>
<td>G</td>
<td>0V</td>
<td>PCIEA Ground</td>
</tr>
<tr>
<td>N9</td>
<td>AVDD33_USB</td>
<td>P</td>
<td>3.3V</td>
<td>USB2.0 3.3V power</td>
</tr>
<tr>
<td>N10</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>N11</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>N12</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>N13</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
</tbody>
</table>

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

<table>
<tbody>
<tr>
<td><strong>Pin ID</strong></td>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
<td><strong>Power Domain</strong></td>
<td><strong>Function</strong></td>
</tr>
<tr>
<td>A14</td>
<td>DQS1_C_B</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Negative of CHB DQS1 <br/>LPDDR3: Negtive of DQS1</td>
</tr>
<tr>
<td>A15</td>
<td>DQS1_C_A</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Negative of CHA DQS1<br/>LPDDR3: Negtive of DQS0</td>
</tr>
<tr>
<td>A16</td>
<td>DQ_A_12</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ12<br/>LPDDR3: DQM0</td>
</tr>
<tr>
<td>A17</td>
<td>DQ_A_9</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ9<br/>LPDDR3: DQ7</td>
</tr>
<tr>
<td>A18</td>
<td>DQ_A_8</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ8<br/>LPDDR3: DQ5</td>
</tr>
<tr>
<td>A19</td>
<td>DQ_A_15</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ15<br/>LPDDR3: DQ3</td>
</tr>
<tr>
<td>A20</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>A21</td>
<td>DQ_A_5</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ5<br/>LPDDR3: DQ21</td>
</tr>
<tr>
<td>A22</td>
<td>DQ_A_7</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ7<br/>LPDDR3: DQ17</td>
</tr>
<tr>
<td>A23</td>
<td>DMI0_A</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Channel A DM0<br/>LPDDR3: DQ22</td>
</tr>
<tr>
<td>A24</td>
<td>DQ_A_1</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ1<br/>LPDDR3: DQ16</td>
</tr>
<tr>
<td>A25</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>A26</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>B14</td>
<td>DQS1_T_B</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Positive of CHB DQS1<br/>LPDDR3: Positive of DQS1</td>
</tr>
<tr>
<td>B15</td>
<td>DQS1_T_A</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Positive of CHA DQS1<br/>LPDDR3: Positive of DQS0</td>
</tr>
<tr>
<td>B16</td>
<td>DQ_A_11</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ11<br/>LPDDR3: DQ4</td>
</tr>
<tr>
<td>B17</td>
<td>DQ_A_10</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ10<br/>LPDDR3: DQ6</td>
</tr>
<tr>
<td>B18</td>
<td>DMI1_A</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Channel A DM1<br/>LPDDR3: DQ2</td>
</tr>
<tr>
<td>B19</td>
<td>DQ_A_14</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ14<br/>LPDDR3: DQ1</td>
</tr>
<tr>
<td>B20</td>
<td>DQ_A_13</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ13 <br/>LPDDR3: DQ0</td>
</tr>
<tr>
<td>B21</td>
<td>DQ_A_4</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ4<br/>LPDDR3: DQ18</td>
</tr>
<tr>
<td>B22</td>
<td>DQ_A_6</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ6<br/>LPDDR3: DQ23</td>
</tr>
<tr>
<td>B23</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>B24</td>
<td>DQ_A_2</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ2<br/>LPDDR3: DQ19</td>
</tr>
<tr>
<td>B25</td>
<td>DQ_A_3</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHB DQ3<br/>LPDDR3: DQM2</td>
</tr>
<tr>
<td>B26</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>C14</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>C15</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>C16</td>
<td>CA_A_4</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA CA4<br/>LPDDR3: CA3</td>
</tr>
<tr>
<td>C17</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>C18</td>
<td>CKE1_A</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 1.1V</td>
<td>LPDDR4X: clock enabling 1 of CHA<br/>LPDDR3: clock enabling 1</td>
</tr>
<tr>
<td>C19</td>
<td>CA_A_1</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA CA1<br/>LPDDR3: CA2</td>
</tr>
<tr>
<td>C20</td>
<td>CS1_A</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Active-low chip select 1 of CHA<br/>LPDDR3: Active-low chip select 1</td>
</tr>
<tr>
<td>C21</td>
<td>AVDD06_DDR</td>
<td>P</td>
<td>lp4x: 0.6V<br/>lp4: TBD/lp3: TBD</td>
<td>LPDDR4X IO power</td>
</tr>
<tr>
<td>C22</td>
<td>DQ_A_0</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA DQ0 <br/>LPDDR3: DQ20</td>
</tr>
<tr>
<td>C23</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>C24</td>
<td>EMMC_DS</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data strobe</td>
</tr>
<tr>
<td>C25</td>
<td>EMMC_D7</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data7</td>
</tr>
<tr>
<td>C26</td>
<td>EMMC_D2</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data2</td>
</tr>
<tr>
<td>D14</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>D15</td>
<td>AVDD06_DDR</td>
<td>P</td>
<td>lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD</td>
<td>LPDDR4X IO power</td>
</tr>
<tr>
<td>D16</td>
<td>CA_A_2</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA CA2</td>
</tr>
<tr>
<td>D17</td>
<td>CK_C_A</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: negative LPDDR differential clock of CHA<br/>LPDDR3: N/A</td>
</tr>
<tr>
<td>D18</td>
<td>CKE0_A</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 1.1V</td>
<td>LPDDR4X: clock enabling 0 of CHA<br/>LPDDR3: clock enabling 0</td>
</tr>
<tr>
<td>D19</td>
<td>CA_A_0</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA CA0<br/>LPDDR3: CA4</td>
</tr>
<tr>
<td>D20</td>
<td>DQS0_T_A</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Positive of CHA DQS0<br/>LPDDR3: Positive of DQS2</td>
</tr>
<tr>
<td>D21</td>
<td>DQS0_C_A</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Negative of CHA DQS0<br/>LPDDR3: Negative of DQS2</td>
</tr>
<tr>
<td>D22</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>D23</td>
<td>EMMC_D4</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data4</td>
</tr>
<tr>
<td>D24</td>
<td>EMMC_D1</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data1</td>
</tr>
<tr>
<td>D25</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>D26</td>
<td>EMMC_D0</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data0</td>
</tr>
<tr>
<td>E14</td>
<td>AVDD18_DDR</td>
<td>P</td>
<td>1.8V</td>
<td>LPDDR PHY PLL 1.8V power</td>
</tr>
<tr>
<td>E15</td>
<td>CA_A_5</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA CA5 <br/>LPDDR3: CA1</td>
</tr>
<tr>
<td>E16</td>
<td>CS0_A</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: Active-low chip select 0 of CHA<br/>LPDDR3: Active-low chip select 0</td>
</tr>
<tr>
<td>E17</td>
<td>CK_T_A</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: positive  LPDDR differential clock of CHA <br/>LPDDR3: N/A</td>
</tr>
<tr>
<td>E18</td>
<td>AVDD06_DDR</td>
<td>P</td>
<td>lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD</td>
<td>LPDDR4X IO power</td>
</tr>
<tr>
<td>E19</td>
<td>AVDD06_DDR</td>
<td>P</td>
<td>lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD</td>
<td>LPDDR4X IO power</td>
</tr>
<tr>
<td>E20</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>E21</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>E22</td>
<td>EMMC_D6</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data6</td>
</tr>
<tr>
<td>E23</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>E24</td>
<td>EMMC_CLK</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC Clock</td>
</tr>
<tr>
<td>E25</td>
<td>EMMC_D3</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data3</td>
</tr>
<tr>
<td>E26</td>
<td>EMMC_D5</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC data5</td>
</tr>
<tr>
<td>F14</td>
<td>ZQ_DDR_PHY</td>
<td>AIO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>DDR ZQ calibration</td>
</tr>
<tr>
<td>F15</td>
<td>CA_A_3</td>
<td>AO</td>
<td>lp3: 1.2V<br/>lp4x: 0.6V</td>
<td>LPDDR4X: CHA CA3<br/>LPDDR3: CA0</td>
</tr>
<tr>
<td>F16</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>F17</td>
<td>DDR_LDO_CAP</td>
<td>RO</td>
<td>0.7~0.9V</td>
<td>External LDO output ball;<br/>Connect to a 100nF capacitor on PCB board</td>
</tr>
<tr>
<td>F18</td>
<td>AVDD06_DDR</td>
<td>P</td>
<td>lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD</td>
<td>LPDDR4X IO power<br/></td>
</tr>
<tr>
<td>F19</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>F20</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>F21</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>F22</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>F23</td>
<td>QSPI_DAT2</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>QSPI data2</td>
</tr>
<tr>
<td>F24</td>
<td>QSPI_DAT1</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>QSPI data1</td>
</tr>
<tr>
<td>F25</td>
<td>EMMC_CMD</td>
<td>I/O</td>
<td>1.8V</td>
<td>eMMC command</td>
</tr>
<tr>
<td>F26</td>
<td>QSPI_DAT0</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>QSPI data0</td>
</tr>
<tr>
<td>G14</td>
<td>DDR_LP23_VREFCA</td>
<td>P</td>
<td>lp3: 0.6V<br/>lp4: high-z</td>
<td>CA VREF for lpddr23, LP4/4x <br/>Keep the pin NC</td>
</tr>
<tr>
<td>G15</td>
<td>AVDD11_DDR</td>
<td>P</td>
<td>lp4x: 1.1V<br/>lp4: 1.1V<br/>lp3: 1.2V</td>
<td>LPDDR PHY power supply</td>
</tr>
<tr>
<td>G16</td>
<td>AVDD06_DDR</td>
<td>P</td>
<td>lp4x: 0.6V<br/>lp4: TBD<br/>lp3: TBD</td>
<td>LPDDR4X IO power</td>
</tr>
<tr>
<td>G17</td>
<td>VSSQ_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>G18</td>
<td>AVDD18_EFUSE</td>
<td>P</td>
<td>1.8V</td>
<td>ANAGRP</td>
</tr>
<tr>
<td>G19</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>G20</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>G21</td>
<td>AVSS_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>G22</td>
<td>QSPI_DAT3</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>QSPI data3</td>
</tr>
<tr>
<td>G23</td>
<td>QSPI_CLK</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>QSPI CLK</td>
</tr>
<tr>
<td>G24</td>
<td>QSPI_CS1</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>QSPI CS</td>
</tr>
<tr>
<td>G25</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>G26</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>H14</td>
<td>AVSSU_DDR</td>
<td>G</td>
<td>0V</td>
<td>DDR Ground</td>
</tr>
<tr>
<td>H15</td>
<td>AVDD18_PHY</td>
<td>P</td>
<td>1.8V</td>
<td>Analog 1.8V power</td>
</tr>
<tr>
<td>H16</td>
<td>VSSU_DDR</td>
<td>G</td>
<td>0V</td>
<td>System DDR Ground</td>
</tr>
<tr>
<td>H17</td>
<td>VSSU_DDR</td>
<td>G</td>
<td>0V</td>
<td>System DDR Ground</td>
</tr>
<tr>
<td>H18</td>
<td>VSSU_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>H19</td>
<td>AVDD18_EMMC</td>
<td>P</td>
<td>1.8V</td>
<td>eMMC analog power</td>
</tr>
<tr>
<td>H20</td>
<td>AVDD09_EMMC</td>
<td>P</td>
<td>0.9V</td>
<td>eMMC digtial power</td>
</tr>
<tr>
<td>H21</td>
<td>VCC1833_QSPI</td>
<td>P</td>
<td>1.8V/3.3V</td>
<td>QSPI IO power</td>
</tr>
<tr>
<td>H22</td>
<td>PCIEC_TX0P</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEC TX0LANEP</td>
</tr>
<tr>
<td>H23</td>
<td>PCIEC_TX0N</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEC TX0LANEN</td>
</tr>
<tr>
<td>H24</td>
<td>AVSS_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>H25</td>
<td>PCIEC_RX0P</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEC RX0LANEP</td>
</tr>
<tr>
<td>H26</td>
<td>PCIEC_RX0N</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEC RX0LANEN</td>
</tr>
<tr>
<td>J14</td>
<td>AVDDU_PHY</td>
<td>P</td>
<td>0.9V</td>
<td>LPDDR PHY core logical power</td>
</tr>
<tr>
<td>J15</td>
<td>AVDDU_PHY</td>
<td>P</td>
<td>0.9V</td>
<td>LPDDR PHY core logical power</td>
</tr>
<tr>
<td>J16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>J17</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>J18</td>
<td>VSSU_EMMC</td>
<td>G</td>
<td>0V</td>
<td>eMMC Ground</td>
</tr>
<tr>
<td>J19</td>
<td>QSPI_VCC_CAP</td>
<td>RO</td>
<td>1.8V</td>
<td>QSPI 1.8V LDO cap</td>
</tr>
<tr>
<td>J20</td>
<td>AVDD09_EMMC</td>
<td>P</td>
<td>0.9V</td>
<td>eMMC digtial power</td>
</tr>
<tr>
<td>J21</td>
<td>AVSS_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>J22</td>
<td>PCIEC_REFCLK_P</td>
<td>AIO</td>
<td>1.8V</td>
<td>PCIEC CKLANEP</td>
</tr>
<tr>
<td>J23</td>
<td>PCIEC_REFCLK_N</td>
<td>AIO</td>
<td>1.8V</td>
<td>PCIEC CKLANEN</td>
</tr>
<tr>
<td>J24</td>
<td>AVSS_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>J25</td>
<td>PCIEC_RX1P</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEC RX1LANEP</td>
</tr>
<tr>
<td>J26</td>
<td>PCIEC_RX1N</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEC RX1LANEN</td>
</tr>
<tr>
<td>K14</td>
<td>AVDD18_PLL</td>
<td>P</td>
<td>1.8</td>
<td>System PLL power supply</td>
</tr>
<tr>
<td>K15</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>K16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital core Ground</td>
</tr>
<tr>
<td>K17</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>K18</td>
<td>VSSU_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>K19</td>
<td>VSSU_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>K20</td>
<td>AVDD09_PCIEC</td>
<td>P</td>
<td>0.9V</td>
<td>PCIEC digital power</td>
</tr>
<tr>
<td>K21</td>
<td>AVSS_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>K22</td>
<td>PCIEC_TX1P</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEC TX1LANEP</td>
</tr>
<tr>
<td>K23</td>
<td>PCIEC_TX1N</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEC TX1LANEN</td>
</tr>
<tr>
<td>K24</td>
<td>AVSS_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>K25</td>
<td>PCIEB_RX0P</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEB RX0LANEP</td>
</tr>
<tr>
<td>K26</td>
<td>PCIEB_RX0N</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEB RX0LANEN</td>
</tr>
<tr>
<td>L14</td>
<td>VSSU_PLL</td>
<td>G</td>
<td>0V</td>
<td>System PLL Ground</td>
</tr>
<tr>
<td>L15</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital core Ground</td>
</tr>
<tr>
<td>L16</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>L17</td>
<td>VSSU_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>L18</td>
<td>VSSU_PCIEC</td>
<td>G</td>
<td>0V</td>
<td>PCIEC Ground</td>
</tr>
<tr>
<td>L19</td>
<td>AVDD18_PCIEC</td>
<td>P</td>
<td>1.8V</td>
<td>PCIEC analog power</td>
</tr>
<tr>
<td>L20</td>
<td>AVDD09_PCIEB</td>
<td>P</td>
<td>0.9V</td>
<td>PCIEB digital power</td>
</tr>
<tr>
<td>L21</td>
<td>AVDD09_PCIEB</td>
<td>P</td>
<td>0.9V</td>
<td>PCIEB digital power</td>
</tr>
<tr>
<td>L22</td>
<td>PCIEB_TX0P</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEB TX0LANEP</td>
</tr>
<tr>
<td>L23</td>
<td>PCIEB_TX0N</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEB TX0LANEN</td>
</tr>
<tr>
<td>L24</td>
<td>AVSS_PCIEB</td>
<td>G</td>
<td>0V</td>
<td>PCIEB Ground</td>
</tr>
<tr>
<td>L25</td>
<td>PCIEB_REFCLK_P</td>
<td>AIO</td>
<td>1.8V</td>
<td>PCIEB CKLANEP</td>
</tr>
<tr>
<td>L26</td>
<td>PCIEB_REFCLK_N</td>
<td>AIO</td>
<td>1.8V</td>
<td>PCIEB CKLANEN</td>
</tr>
<tr>
<td>M14</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>M15</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>M16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>M17</td>
<td>VSSU_PCIEB</td>
<td>G</td>
<td>0V</td>
<td>PCIEB Ground</td>
</tr>
<tr>
<td>M18</td>
<td>VSSU_PCIEB</td>
<td>G</td>
<td>0V</td>
<td>PCIEB Ground</td>
</tr>
<tr>
<td>M19</td>
<td>AVDD18_PCIEB</td>
<td>P</td>
<td>1.8V</td>
<td>PCIEB analog power</td>
</tr>
<tr>
<td>M20</td>
<td>AVSS_PCIEB</td>
<td>G</td>
<td>0V</td>
<td>PCIEB Ground</td>
</tr>
<tr>
<td>M21</td>
<td>AVSS_PCIEB</td>
<td>G</td>
<td>0V</td>
<td>PCIEB Ground</td>
</tr>
<tr>
<td>M22</td>
<td>PCIEB_TX1P</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEB TX1LANEP</td>
</tr>
<tr>
<td>M23</td>
<td>PCIEB_TX1N</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEB TX1LANEN</td>
</tr>
<tr>
<td>M24</td>
<td>AVSS_PCIEB</td>
<td>G</td>
<td>0V</td>
<td>PCIEB Ground</td>
</tr>
<tr>
<td>M25</td>
<td>PCIEB_RX1P</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEB RX1LANEP</td>
</tr>
<tr>
<td>M26</td>
<td>PCIEB_RX1N</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEB RX1LANEN</td>
</tr>
<tr>
<td>N14</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>N15</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>N16</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>N17</td>
<td>AVSS18_AUD</td>
<td>G</td>
<td>0V</td>
<td>Audio Ground</td>
</tr>
<tr>
<td>N18</td>
<td>AVDD3V3_AUD</td>
<td>P</td>
<td>3.3V</td>
<td>3.3V power for earphone driver</td>
</tr>
<tr>
<td>N19</td>
<td>AVSS18_AUD</td>
<td>G</td>
<td>0V</td>
<td>Audio Ground</td>
</tr>
<tr>
<td>N20</td>
<td>AVSS18_AUD</td>
<td>G</td>
<td>0V</td>
<td>Audio Ground</td>
</tr>
<tr>
<td>N21</td>
<td>NA</td>
<td>P</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>N22</td>
<td>NA</td>
<td>P</td>
<td> -1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>N23</td>
<td>NA</td>
<td>AO</td>
<td>+/-1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>N24</td>
<td>NA</td>
<td>AO</td>
<td>+/-1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>N25</td>
<td>NA</td>
<td>AO</td>
<td>3.3V</td>
<td>NA</td>
</tr>
<tr>
<td>N26</td>
<td>NA</td>
<td>AO</td>
<td>3.3V</td>
<td>NA</td>
</tr>
</tbody>
</table>

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

<table>
<tbody>
<tr>
<td><strong>Pin ID</strong></td>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
<td><strong>Power Domain</strong></td>
<td><strong>Function</strong></td>
</tr>
<tr>
<td>P1</td>
<td>PCIEA_RXN</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEA RXLANEN</td>
</tr>
<tr>
<td>P2</td>
<td>PCIEA_RXP</td>
<td>AI</td>
<td>1.8V</td>
<td>PCIEA RXLANEP</td>
</tr>
<tr>
<td>P3</td>
<td>AVSS_USB</td>
<td>G</td>
<td>0V</td>
<td>USB2.0 Ground</td>
</tr>
<tr>
<td>P4</td>
<td>PCIEA_R_EXT</td>
<td>AO</td>
<td>1.8V</td>
<td>PCIEA External calibration resistor</td>
</tr>
<tr>
<td>P5</td>
<td>AVSS_USB</td>
<td>G</td>
<td>0V</td>
<td>USB2.0 Ground</td>
</tr>
<tr>
<td>P6</td>
<td>AVDD18_USB</td>
<td>P</td>
<td>1.8V<br/></td>
<td>USB2.0 1.8V power</td>
</tr>
<tr>
<td>P7</td>
<td>AVDD09_USB</td>
<td>P</td>
<td>0.9V</td>
<td>USB2.0 digital power</td>
</tr>
<tr>
<td>P8</td>
<td>AVDD09_USB</td>
<td>P</td>
<td>0.9V</td>
<td>USB2.0 digital power</td>
</tr>
<tr>
<td>P9</td>
<td>AVDD33_USB</td>
<td>P</td>
<td>3.3V</td>
<td>USB2.0 3.3V power</td>
</tr>
<tr>
<td>P10</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>P11</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>P12</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>P13</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>R1</td>
<td>PCIEA_REFCLK_N</td>
<td>AIO</td>
<td>1.8V</td>
<td>PCIEA CKLANEN</td>
</tr>
<tr>
<td>R2</td>
<td>PCIEA_REFCLK_P</td>
<td>AIO</td>
<td>1.8V</td>
<td>PCIEA CKLANEP</td>
</tr>
<tr>
<td>R3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital core Ground</td>
</tr>
<tr>
<td>R4</td>
<td>USB1_DN</td>
<td>AIO</td>
<td>3.3V</td>
<td>USB2.0_1 D- differential data line</td>
</tr>
<tr>
<td>R5</td>
<td>USB1_DP</td>
<td>AIO</td>
<td>3.3V</td>
<td>USB2.0_1 D+ differential data line</td>
</tr>
<tr>
<td>R6</td>
<td>AVDD18_DSI1</td>
<td>P</td>
<td>1.8V</td>
<td>DSI analog power</td>
</tr>
<tr>
<td>R7</td>
<td>AVSS_USB</td>
<td>G</td>
<td>0V</td>
<td>USB2.0 Ground</td>
</tr>
<tr>
<td>R8</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>R9</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>R10</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>R11</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>R12</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>R13</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>T1</td>
<td>MIPI_DSI1_D3N</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA3LANEN</td>
</tr>
<tr>
<td>T2</td>
<td>MIPI_DSI1_D3P</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA3LANEP</td>
</tr>
<tr>
<td>T3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital core ground</td>
</tr>
<tr>
<td>T4</td>
<td>USB0_DN</td>
<td>AIO</td>
<td>3.3V</td>
<td>USB2.0_0 D- differential data line</td>
</tr>
<tr>
<td>T5</td>
<td>USB0_DP</td>
<td>AIO</td>
<td>3.3V</td>
<td>USB2.0_0 D+ differential data line</td>
</tr>
<tr>
<td>T6</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital core ground</td>
</tr>
<tr>
<td>T7</td>
<td>AVDD09_DSI1</td>
<td>P</td>
<td>0.9V</td>
<td>DSI digital power</td>
</tr>
<tr>
<td>T8</td>
<td>AVDD12_DSI1</td>
<td>P</td>
<td>1.2V</td>
<td>DSI driver power</td>
</tr>
<tr>
<td>T9</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>T10</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T11</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>T12</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T13</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>U1</td>
<td>MIPI_DSI1_D2N</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA2LANEN</td>
</tr>
<tr>
<td>U2</td>
<td>MIPI_DSI1_D2P</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA2LANEP</td>
</tr>
<tr>
<td>U3</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>U4</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>U5</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>U6</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>U7</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>U8</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>U9</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>U10</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>U11</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>U12</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>U13</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V1</td>
<td>MIPI_DSI1_CLKN</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI CKLANEN</td>
</tr>
<tr>
<td>V2</td>
<td>MIPI_DSI1_CLKP</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI CKLANEP</td>
</tr>
<tr>
<td>V3</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>V4</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>V5</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>V6</td>
<td>AVSS_DSI1</td>
<td>G</td>
<td>0V</td>
<td>DSI Ground</td>
</tr>
<tr>
<td>V7</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>V8</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V9</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>V10</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V11</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>V12</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V13</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W1</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W2</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W4</td>
<td>MIPI_DSI1_D1N</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA1LANEN</td>
</tr>
<tr>
<td>W5</td>
<td>MIPI_DSI1_D1P</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA1LANEP</td>
</tr>
<tr>
<td>W6</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W7</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W8</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W9</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W10</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W11</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W12</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W13</td>
<td>GPIO3_VCC_CAP</td>
<td>RO</td>
<td>1.8V</td>
<td>GPIO3 1.8V LDO cap</td>
</tr>
<tr>
<td>Y1</td>
<td>PRI_TRST_N</td>
<td>I/O</td>
<td>1.8V</td>
<td>JTAG reset</td>
</tr>
<tr>
<td>Y2</td>
<td>GPIO_74</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 74</td>
</tr>
<tr>
<td>Y3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y4</td>
<td>MIPI_DSI1_D0N</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA0LANEN</td>
</tr>
<tr>
<td>Y5</td>
<td>MIPI_DSI1_D0P</td>
<td>AO</td>
<td>1.2V</td>
<td>DSI DATA0LANEP</td>
</tr>
<tr>
<td>Y6</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y7</td>
<td>AVDD33_HDMI</td>
<td>P</td>
<td>3.3V</td>
<td>HDMI 3.3V power</td>
</tr>
<tr>
<td>Y8</td>
<td>AVDD33_HDMI</td>
<td>P</td>
<td>3.3V</td>
<td>HDMI 3.3V power</td>
</tr>
<tr>
<td>Y9</td>
<td>AVDD09_HDMI</td>
<td>P</td>
<td>0.9V</td>
<td>HDMI digtial power</td>
</tr>
<tr>
<td>Y10</td>
<td>AVDD09_HDMI</td>
<td>P</td>
<td>0.9V</td>
<td>HDMI digtial power</td>
</tr>
<tr>
<td>Y11</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y12</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y13</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA1</td>
<td>PRI_TCK</td>
<td>I/O</td>
<td>1.8V</td>
<td>JTAG clock</td>
</tr>
<tr>
<td>AA2</td>
<td>PRI_TDO</td>
<td>I/O</td>
<td>1.8V</td>
<td>JTAG output data</td>
</tr>
<tr>
<td>AA3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA4</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA5</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA6</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA7</td>
<td>AVSS_HDMI</td>
<td>G</td>
<td>0V</td>
<td>HDMI Ground</td>
</tr>
<tr>
<td>AA8</td>
<td>HDMI_TX2N</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI data2n</td>
</tr>
<tr>
<td>AA9</td>
<td>AVDD18_HDMI</td>
<td>P</td>
<td>1.8V</td>
<td>HDMI 1.8V power</td>
</tr>
<tr>
<td>AA10</td>
<td>AVDD18_HDMI</td>
<td>P</td>
<td>1.8V</td>
<td>HDMI 1.8V power</td>
</tr>
<tr>
<td>AA11</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA12</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA13</td>
<td>VCC1833_GPIO3</td>
<td>P</td>
<td>1.8V/3.3V</td>
<td>GPIO3 IO power</td>
</tr>
<tr>
<td>AB1</td>
<td>PRI_TDI</td>
<td>I/O</td>
<td>1.8V</td>
<td>JTAG input data</td>
</tr>
<tr>
<td>AB2</td>
<td>PRI_TMS</td>
<td>I/O</td>
<td>1.8V</td>
<td>JTAG mode selection</td>
</tr>
<tr>
<td>AB3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB4</td>
<td>HDMI_TXCN</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI clkn</td>
</tr>
<tr>
<td>AB5</td>
<td>HDMI_TX0N</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI data0n</td>
</tr>
<tr>
<td>AB6</td>
<td>AVSS_HDMI</td>
<td>G</td>
<td>0V</td>
<td>HDMI Ground</td>
</tr>
<tr>
<td>AB7</td>
<td>HDMI_TX1N</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI data1n</td>
</tr>
<tr>
<td>AB8</td>
<td>HDMI_TX2P</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI data2p</td>
</tr>
<tr>
<td>AB9</td>
<td>AVSS_HDMI</td>
<td>G</td>
<td>0V</td>
<td>HDMI Ground</td>
</tr>
<tr>
<td>AB10</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB11</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB12</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB13</td>
<td>GPIO_51</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General purpose I/O 51</td>
</tr>
<tr>
<td>AC1</td>
<td>GPIO_61</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 61</td>
</tr>
<tr>
<td>AC2</td>
<td>GPIO_62</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 62</td>
</tr>
<tr>
<td>AC3</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>AC4</td>
<td>HDMI_TXCP</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI clkp</td>
</tr>
<tr>
<td>AC5</td>
<td>HDMI_TX0P</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI data0p</td>
</tr>
<tr>
<td>AC6</td>
<td>AVSS_HDMI</td>
<td>G</td>
<td>0V</td>
<td>HDMI Ground</td>
</tr>
<tr>
<td>AC7</td>
<td>HDMI_TX1P</td>
<td>AO</td>
<td>1.8V</td>
<td>HDMI data1p</td>
</tr>
<tr>
<td>AC8</td>
<td>AVSS_HDMI</td>
<td>G</td>
<td>0V</td>
<td>HDMI Ground</td>
</tr>
<tr>
<td>AC9</td>
<td>AVSS_HDMI</td>
<td>G</td>
<td>0V</td>
<td>HDMI Ground</td>
</tr>
<tr>
<td>AC10</td>
<td>GPIO_86</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 86</td>
</tr>
<tr>
<td>AC11</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>AC12</td>
<td>GPIO_52</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 52</td>
</tr>
<tr>
<td>AC13</td>
<td>GPIO_47</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 47</td>
</tr>
<tr>
<td>AD1</td>
<td>GPIO_59</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 59</td>
</tr>
<tr>
<td>AD2</td>
<td>GPIO_60</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 60</td>
</tr>
<tr>
<td>AD3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AD4</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AD5</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AD6</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AD7</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AD8</td>
<td>GPIO_87</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 87</td>
</tr>
<tr>
<td>AD9</td>
<td>GPIO_85</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 85</td>
</tr>
<tr>
<td>AD10</td>
<td>PMIC_INT_N</td>
<td>I/O</td>
<td>1.8V</td>
<td>PMIC interrupt</td>
</tr>
<tr>
<td>AD11</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>AD12</td>
<td>GPIO_50</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 50</td>
</tr>
<tr>
<td>AD13</td>
<td>GPIO_48</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 48</td>
</tr>
<tr>
<td>AE1</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AE2</td>
<td>MPLL_TST_AD</td>
<td>AIO</td>
<td>1.8V</td>
<td>Analog testpin</td>
</tr>
<tr>
<td>AE3</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AE4</td>
<td>GPIO_92</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 92</td>
</tr>
<tr>
<td>AE5</td>
<td>GPIO_90</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 90</td>
</tr>
<tr>
<td>AE6</td>
<td>GPIO_91</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 91</td>
</tr>
<tr>
<td>AE7</td>
<td>GPIO_89</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 89</td>
</tr>
<tr>
<td>AE8</td>
<td>GPIO_84</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 84</td>
</tr>
<tr>
<td>AE9</td>
<td>GPIO_81</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 81</td>
</tr>
<tr>
<td>AE10</td>
<td>DVL0</td>
<td>I/O</td>
<td>1.8V</td>
<td>Hardware dynamic voltage regulation signal0</td>
</tr>
<tr>
<td>AE11</td>
<td>PWR_SCL</td>
<td>I/O</td>
<td>1.8V</td>
<td>PMIC I2C bus clock</td>
</tr>
<tr>
<td>AE12</td>
<td>EXT_32K_IN</td>
<td>I/O</td>
<td>1.8V</td>
<td>32K clock input</td>
</tr>
<tr>
<td>AE13</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF1</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF2</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF3</td>
<td>RESET_IN_N</td>
<td>I/O</td>
<td>1.8V</td>
<td>Reset input</td>
</tr>
<tr>
<td>AF4</td>
<td>JTAG_SEL</td>
<td>I/O</td>
<td>1.8V</td>
<td>Primary JTAG selection</td>
</tr>
<tr>
<td>AF5</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF6</td>
<td>GPIO_88</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 88</td>
</tr>
<tr>
<td>AF7</td>
<td>GPIO_82</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 82</td>
</tr>
<tr>
<td>AF8</td>
<td>GPIO_83</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 83</td>
</tr>
<tr>
<td>AF9</td>
<td>DVL1</td>
<td>I/O</td>
<td>1.8V</td>
<td>Hardware dynamic voltage regulation signal1</td>
</tr>
<tr>
<td>AF10</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF11</td>
<td>SLEEP_OUT</td>
<td>I/O</td>
<td>1.8V</td>
<td>VCXO enabling</td>
</tr>
<tr>
<td>AF12</td>
<td>PWR_SDA</td>
<td>I/O</td>
<td>1.8V</td>
<td>PMIC I2C bus data/address</td>
</tr>
<tr>
<td>AF13</td>
<td>GPIO_49</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 49</td>
</tr>
</tbody>
</table>

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

<table>
<tbody>
<tr>
<td><strong>Pin ID</strong></td>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
<td><strong>Power Domain</strong></td>
<td><strong>Function</strong></td>
</tr>
<tr>
<td>P14</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>P15</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>P16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>P17</td>
<td>AUD_GNDSNS</td>
<td>G<br/></td>
<td>0V</td>
<td>Headphone sense_Ground</td>
</tr>
<tr>
<td>P18</td>
<td>AVDD18_AUD</td>
<td>P</td>
<td>1.8V</td>
<td>1.8V power for audio</td>
</tr>
<tr>
<td>P19</td>
<td>AVDD18_AUD</td>
<td>P</td>
<td>1.8V</td>
<td>1.8V power for audio</td>
</tr>
<tr>
<td>P20</td>
<td>NA</td>
<td>AO</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>P21</td>
<td>NA</td>
<td>AO</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>P22</td>
<td>NA</td>
<td>AO</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>P23</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>P24</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>P25</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>P26</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>R14</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>R15</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core Ground</td>
</tr>
<tr>
<td>R16</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>R17</td>
<td>AUD_VSSU</td>
<td>G</td>
<td>0V</td>
<td>Audio Ground</td>
</tr>
<tr>
<td>R18</td>
<td>AUD_VDDU09</td>
<td>P</td>
<td>0.9V</td>
<td>0.9V power for audio</td>
</tr>
<tr>
<td>R19</td>
<td>AUD_REFGND</td>
<td>G</td>
<td>0V</td>
<td>Audio Reference Ground</td>
</tr>
<tr>
<td>R20</td>
<td>NA<br/></td>
<td>AO<br/></td>
<td>1.8V</td>
<td>NA<br/></td>
</tr>
<tr>
<td>R21</td>
<td>AUD_AUREF10</td>
<td>RO</td>
<td>1.8V</td>
<td>Audio reference voltage</td>
</tr>
<tr>
<td>R22</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>R23</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>R24</td>
<td>VSS</td>
<td>G<br/></td>
<td>0V</td>
<td>Digital core ground</td>
</tr>
<tr>
<td>R25</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>R26</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>T14</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T15</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>T16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T17</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>T18</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T19</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T20</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T21</td>
<td>AVSS18_AUD</td>
<td>G</td>
<td>0V</td>
<td>Audio Ground</td>
</tr>
<tr>
<td>T22</td>
<td>AVSS18_AUD</td>
<td>G</td>
<td>0V</td>
<td>Audio Ground</td>
</tr>
<tr>
<td>T23</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>T24</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>T25</td>
<td>NA</td>
<td>AO</td>
<td>3.3V</td>
<td>NA</td>
</tr>
<tr>
<td>T26</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital core ground</td>
</tr>
<tr>
<td>U14</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>U15</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>U16</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>U17</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>U18</td>
<td>VCC_M1_FB</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power FeedBack</td>
</tr>
<tr>
<td>U19</td>
<td>VSS_FB</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground FeedBack</td>
</tr>
<tr>
<td>U20</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital core ground</td>
</tr>
<tr>
<td>U21</td>
<td>GPIO_123</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 123</td>
</tr>
<tr>
<td>U22</td>
<td>GPIO_125</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 125</td>
</tr>
<tr>
<td>U23</td>
<td>NA</td>
<td>AI</td>
<td>1.8V</td>
<td>NA</td>
</tr>
<tr>
<td>U24</td>
<td>NA</td>
<td>AO</td>
<td>3.3V</td>
<td>NA</td>
</tr>
<tr>
<td>U25</td>
<td>GPIO_126</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 126</td>
</tr>
<tr>
<td>U26</td>
<td>GPIO_127</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 127</td>
</tr>
<tr>
<td>V14</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V15</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>V16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V17</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>V18</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V19</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V20</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V21</td>
<td>GPIO_121</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 121</td>
</tr>
<tr>
<td>V22</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V23</td>
<td>GPIO_124</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 124</td>
</tr>
<tr>
<td>V24</td>
<td>GPIO_120</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 120</td>
</tr>
<tr>
<td>V25</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>V26</td>
<td>GPIO_122</td>
<td>I/O</td>
<td>1.8V</td>
<td>General purpose I/O 122</td>
</tr>
<tr>
<td>W14</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W15</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W16</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W17</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W18</td>
<td>VCC_M1</td>
<td>P</td>
<td>0.9V</td>
<td>Digital Core power</td>
</tr>
<tr>
<td>W19</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W20</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W21</td>
<td>GPIO_110</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 110</td>
</tr>
<tr>
<td>W22</td>
<td>GPIO_117</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 117</td>
</tr>
<tr>
<td>W23</td>
<td>GPIO_116</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 116</td>
</tr>
<tr>
<td>W24</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>W25</td>
<td>GPIO_119</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 119</td>
</tr>
<tr>
<td>W26</td>
<td>GPIO_118</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 118</td>
</tr>
<tr>
<td>Y14</td>
<td>MMC1_VCC_CAP</td>
<td>RO</td>
<td>1.8V</td>
<td>SD card 1.8V LDO cap</td>
</tr>
<tr>
<td>Y15</td>
<td>GPIO2_VCC_CAP</td>
<td>RO</td>
<td>1.8V</td>
<td>GPIO2 1.8V LDO cap</td>
</tr>
<tr>
<td>Y16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y17</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y18</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y19</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y20</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y21</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>Y22</td>
<td>GPIO_26</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 26</td>
</tr>
<tr>
<td>Y23</td>
<td>GPIO_27</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 27</td>
</tr>
<tr>
<td>Y24</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>Y25</td>
<td>GPIO_28</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 28</td>
</tr>
<tr>
<td>Y26</td>
<td>GPIO_115</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 115</td>
</tr>
<tr>
<td>AA14</td>
<td>VCC1833_MMC1</td>
<td>P</td>
<td>1.8V/3.3V</td>
<td>SD card IO power</td>
</tr>
<tr>
<td>AA15</td>
<td>VCC1833_GPIO2</td>
<td>P</td>
<td>1.8V/3.3V</td>
<td>GPIO2 IO power</td>
</tr>
<tr>
<td>AA16</td>
<td>MMC1_DAT2</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>SD card data 2</td>
</tr>
<tr>
<td>AA17</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA18</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AA19</td>
<td>GPIO_32</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 32</td>
</tr>
<tr>
<td>AA20</td>
<td>GPIO_29</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 29</td>
</tr>
<tr>
<td>AA21</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>AA22</td>
<td>GPIO_21</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 21</td>
</tr>
<tr>
<td>AA23</td>
<td>GPIO_24</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 24</td>
</tr>
<tr>
<td>AA24</td>
<td>GPIO_23</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 23</td>
</tr>
<tr>
<td>AA25</td>
<td>GPIO_25</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 25</td>
</tr>
<tr>
<td>AA26</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB14</td>
<td>MMC1_DAT0</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>SD card data 0</td>
</tr>
<tr>
<td>AB15</td>
<td>GPIO_78</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 78</td>
</tr>
<tr>
<td>AB16</td>
<td>GPIO_77</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 77</td>
</tr>
<tr>
<td>AB17</td>
<td>GPIO_02</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 02</td>
</tr>
<tr>
<td>AB18</td>
<td>GPIO_03</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 03</td>
</tr>
<tr>
<td>AB19</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB20</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB21</td>
<td>GPIO_41</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 41</td>
</tr>
<tr>
<td>AB22</td>
<td>GPIO_44</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 44</td>
</tr>
<tr>
<td>AB23</td>
<td>GPIO_19</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 19</td>
</tr>
<tr>
<td>AB24</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AB25</td>
<td>GPIO_20</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 20</td>
</tr>
<tr>
<td>AB26</td>
<td>GPIO_22</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 22</td>
</tr>
<tr>
<td>AC14</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>AC15</td>
<td>GPIO_79</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 79</td>
</tr>
<tr>
<td>AC16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AC17</td>
<td>GPIO_05</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 05</td>
</tr>
<tr>
<td>AC18</td>
<td>GPIO_00</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 00</td>
</tr>
<tr>
<td>AC19</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AC20</td>
<td>GPIO_31</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 31</td>
</tr>
<tr>
<td>AC21</td>
<td>GPIO_34</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 34</td>
</tr>
<tr>
<td>AC22</td>
<td>GPIO_42</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 42</td>
</tr>
<tr>
<td>AC23</td>
<td>GPIO_43</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 43</td>
</tr>
<tr>
<td>AC24</td>
<td>GPIO_17</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 17</td>
</tr>
<tr>
<td>AC25</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AC26</td>
<td>GPIO_18</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 18</td>
</tr>
<tr>
<td>AD14</td>
<td>MMC1_CMD</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>SD card command</td>
</tr>
<tr>
<td>AD15</td>
<td>GPIO_76</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 76</td>
</tr>
<tr>
<td>AD16</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AD17</td>
<td>GPIO_04</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 04</td>
</tr>
<tr>
<td>AD18</td>
<td>GPIO_01</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 01</td>
</tr>
<tr>
<td>AD19</td>
<td>GPIO_30</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 30</td>
</tr>
<tr>
<td>AD20</td>
<td>GPIO_33</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 33</td>
</tr>
<tr>
<td>AD21</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>AD22</td>
<td>VCC18_GPIO</td>
<td>P</td>
<td>1.8V</td>
<td>GPIO1/4/5/PMIC I/O power</td>
</tr>
<tr>
<td>AD23</td>
<td>GPIO_14</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 14</td>
</tr>
<tr>
<td>AD24</td>
<td>GPIO_12</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 12</td>
</tr>
<tr>
<td>AD25</td>
<td>GPIO_16</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 16</td>
</tr>
<tr>
<td>AD26</td>
<td>GPIO_15</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 15</td>
</tr>
<tr>
<td>AE14</td>
<td>MMC1_CLK</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>SD card clock</td>
</tr>
<tr>
<td>AE15</td>
<td>MMC1_DAT3</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>SD card data 3</td>
</tr>
<tr>
<td>AE16</td>
<td>GPIO_75</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 75</td>
</tr>
<tr>
<td>AE17</td>
<td>GPIO_11</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 11</td>
</tr>
<tr>
<td>AE18</td>
<td>GPIO_07</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 07</td>
</tr>
<tr>
<td>AE19</td>
<td>GPIO_10</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 10</td>
</tr>
<tr>
<td>AE20</td>
<td>GPIO_37</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 37</td>
</tr>
<tr>
<td>AE21</td>
<td>GPIO_35</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 35</td>
</tr>
<tr>
<td>AE22</td>
<td>GPIO_38</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 38</td>
</tr>
<tr>
<td>AE23</td>
<td>GPIO_46</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 46</td>
</tr>
<tr>
<td>AE24</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AE25</td>
<td>GPIO_13</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 13</td>
</tr>
<tr>
<td>AE26</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF14</td>
<td>MMC1_DAT1</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>SD card  data 1</td>
</tr>
<tr>
<td>AF15</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF16</td>
<td>GPIO_80</td>
<td>I/O</td>
<td>1.8V/3.3V</td>
<td>General Purpose I/O 80</td>
</tr>
<tr>
<td>AF17</td>
<td>GPIO_08</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 08</td>
</tr>
<tr>
<td>AF18</td>
<td>GPIO_06</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 06</td>
</tr>
<tr>
<td>AF19</td>
<td>GPIO_09</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 09</td>
</tr>
<tr>
<td>AF20</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF21</td>
<td>GPIO_40</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 40</td>
</tr>
<tr>
<td>AF22</td>
<td>GPIO_36</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 36</td>
</tr>
<tr>
<td>AF23</td>
<td>GPIO_39</td>
<td>I/O</td>
<td>1.8V<br/></td>
<td>General Purpose I/O 39</td>
</tr>
<tr>
<td>AF24</td>
<td>GPIO_45</td>
<td>I/O</td>
<td>1.8V</td>
<td>General Purpose I/O 45</td>
</tr>
<tr>
<td>AF25</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
<tr>
<td>AF26</td>
<td>VSS</td>
<td>G</td>
<td>0V</td>
<td>Digital Core ground</td>
</tr>
</tbody>
</table>

### 4.3 I/O Pin Parameters

#### For 1.8V I/O Pins

<table>
<tbody>
<tr>
<td><strong>Power Domain</strong></td>
<td><strong>Symbol</strong></td>
<td><strong>Description</strong></td>
<td><strong>Min</strong></td>
<td><strong>Typ</strong></td>
<td><strong>Max</strong></td>
</tr>
<tr>
<td rowspan=5 colspan=1>1.8V Input</td>
<td>Vih</td>
<td>High level input</td>
<td>VCC×0.7V</td>
<td>1.8V</td>
<td>VCC+0.2V</td>
</tr>
<tr>
<td>Vil</td>
<td>Low level input</td>
<td>-0.3V</td>
<td>0V</td>
<td>VCCx0.3V</td>
</tr>
<tr>
<td>Rpu</td>
<td>Pull up resister</td>
<td>55kOhm</td>
<td>79KOhm</td>
<td>121kOhm</td>
</tr>
<tr>
<td>Rpd</td>
<td>Pull down resister</td>
<td>51kOhm</td>
<td>87kOhm</td>
<td>169kOhm</td>
</tr>
<tr>
<td>Iil</td>
<td>Input leakage current<br/>Pad in input mode</td>
<td>　</td>
<td>　</td>
<td>10uA</td>
</tr>
<tr>
<td rowspan=4 colspan=1>1.8V Ouput</td>
<td>Voh</td>
<td>High level output</td>
<td>VCC-0.2V</td>
<td>　</td>
<td>　</td>
</tr>
<tr>
<td>Vol</td>
<td>Low level output</td>
<td>　</td>
<td>　</td>
<td>0.2V</td>
</tr>
<tr>
<td>Iol DCS[1:0]=<br/>00<br/>01<br/>10<br/>11</td>
<td>Low level output current when <br/>Vpad=0.2V</td>
<td><br/>13mA<br/>25mA<br/>37mA<br/>49mA</td>
<td>　</td>
<td>　</td>
</tr>
<tr>
<td>Ioh DCS[1:0]=<br/>00<br/>01<br/>10<br/>11</td>
<td>High level output current when<br/>Vpad=VCC-0.2V</td>
<td><br/>11mA<br/>21mA<br/>32mA<br/>42mA</td>
<td>　</td>
<td>　</td>
</tr>
</tbody>
</table>

#### For 3.3V I/O Pins

<table>
<tbody>
<tr>
<td><strong>Power Domain</strong></td>
<td><strong>Symbol</strong></td>
<td><strong>Description</strong></td>
<td><strong>Min</strong></td>
<td><strong>Typ</strong></td>
<td><strong>Max</strong></td>
</tr>
<tr>
<td rowspan=5 colspan=1>3.3V Input</td>
<td>Vih</td>
<td>High level input</td>
<td>2V</td>
<td> </td>
<td>VCC+0.3V</td>
</tr>
<tr>
<td>Vil</td>
<td>Low level input</td>
<td>-0.3V</td>
<td>0V</td>
<td>0.8V</td>
</tr>
<tr>
<td>Rpu</td>
<td>Pull up resister</td>
<td>26kOhm　　</td>
<td>47kOhm</td>
<td>72kOhm　</td>
</tr>
<tr>
<td>Rpd</td>
<td>Pull down resister</td>
<td>27kOhm　　</td>
<td>54kOhm</td>
<td>267kOhm　　</td>
</tr>
<tr>
<td>Iil</td>
<td>Input leakage current</td>
<td>　</td>
<td>　</td>
<td>10uA</td>
</tr>
<tr>
<td rowspan=4 colspan=1>3.3V Ouput</td>
<td>Voh</td>
<td>High level output</td>
<td>2.4V</td>
<td>　</td>
<td>　</td>
</tr>
<tr>
<td>Vol</td>
<td>Low level output</td>
<td>　</td>
<td>　</td>
<td>0.4V</td>
</tr>
<tr>
<td>Iol DS[2:0]=<br/>000<br/>001<br/>010<br/>011<br/>100<br/>101<br/>110<br/>111</td>
<td>Low level output current when <br/>Vpad=0.4V<br/></td>
<td><br/>7mA<br/>10mA<br/>14mA<br/>18mA<br/>21mA<br/>24mA<br/>28mA<br/>31mA</td>
<td>　</td>
<td>　</td>
</tr>
<tr>
<td>Ioh DS[2:0]=<br/>000<br/>001<br/>010<br/>011<br/>100<br/>101<br/>110<br/>111</td>
<td>High level output current when<br/>Vpad=VCC-0.5V<br/></td>
<td><br/>7mA<br/>10mA<br/>13mA<br/>16mA<br/>19mA<br/>23mA<br/>26mA<br/>29mA</td>
<td>　</td>
<td>　</td>
</tr>
</tbody>
</table>

### 4.4 Multiplexed Signal/Pin Functions

The **Function 0** through 7 signals is assigned to the I/O pins of K1.

Most I/O pins of K1 are multi-function allowing them to be configured for one of several available functions using Multi-Function Pin Registers (MFPRs). Additionally, some functions can be configured to be present on several different pins.

The assigned signals are organized by their functions (e.g. power supply, clock, etc.) which are arranged in groups according to their interfaces (e.g. JTAG, SPIx, etc.) as per description in the following subsections (sorted alphabetically for user convenience).

> **Note.**Definition of symbols used for signal/pin type:
>
> - I = Input
> - O = Output
> - I/O = Input/Output
> - OD = Open-Drain
> - RO = Reference output

#### JTAG

##### Primary

<table>
<tbody>
<tr>
<td rowspan=1 colspan=2><strong>Signal/Pin</strong></td>
<td rowspan=2 colspan=1><strong>Description</strong></td>
</tr>
<tr>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
</tr>
<tr>
<td>PRI_TCK</td>
<td>I</td>
<td>Primary JTAG interface 1 test clock.<br/>Used for all transfers on the JTAG test interface.</td>
</tr>
<tr>
<td>PRI_TDI</td>
<td>I</td>
<td>Primary JTAG interface 1 test data input.<br/>Used to send data from the JTAG controller to the K1 processor. This pin has an internal pullup resistor.</td>
</tr>
<tr>
<td>PRI_TDO</td>
<td>O</td>
<td>Primary JTAG Interface 1 test data output<br/>Used to return data from the K1 processor to the JTAG controller.</td>
</tr>
<tr>
<td>PRI_TMS</td>
<td>I</td>
<td>Primary JTAG Interface 1 test mode select.<br/>Used to select the test mode required from the JTAG controller. This pin has an internal pullup resistor.</td>
</tr>
<tr>
<td>PRI_TRSTn<br/></td>
<td>I</td>
<td>Primary JTAG Interface 1 test reset.<br/>Used for IEEE 1194.1 test reset.</td>
</tr>
<tr>
<td>VCXO_OUT</td>
<td>O</td>
<td>24 MHz VCXO output clock</td>
</tr>
<tr>
<td>VCXO_REQ</td>
<td>I</td>
<td>OCLK1 request </td>
</tr>
</tbody>
</table>

##### Secondary

<table>
<tbody>
<tr>
<td rowspan=1 colspan=2><strong>Signal/Pin</strong></td>
<td rowspan=2 colspan=1><strong>Description</strong></td>
</tr>
<tr>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
</tr>
<tr>
<td>SEC2_TCK</td>
<td>I</td>
<td>Secondary JTAG Interface 2 test clock.<br/>Used for all transfers on the JTAG test interface.</td>
</tr>
<tr>
<td>SEC2_TDI</td>
<td>I</td>
<td>Secondary JTAG Interface 2 test data input.<br/>Used to send data from the JTAG controller to the K1 processor. This pin has an internal pullup resistor.</td>
</tr>
<tr>
<td>SEC2_TDO</td>
<td>O</td>
<td>Secondary JTAG Interface 2 test data output.<br/>Used to return data from the K1 processor to the JTAG controller.</td>
</tr>
<tr>
<td>SEC2_TMS</td>
<td>I</td>
<td>Secondary JTAG Interface 2 test mode select.<br/>Used to select the test mode required from the JTAG controller. This pin has an internal pullup resistor.</td>
</tr>
<tr>
<td>SEC2_TRSTn</td>
<td>I</td>
<td>Secondary JTAG Interface 2 test reset.<br/>Used for IEEE 1194.1 test reset.</td>
</tr>
</tbody>
</table>

#### Keypad Controller

<table>
<tbody>
<tr>
<td rowspan=1 colspan=2><strong>Signal/Pin</strong></td>
<td rowspan=2 colspan=1><strong>Description</strong></td>
</tr>
<tr>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
</tr>
<tr>
<td>KP_DK[4: 0]</td>
<td>I</td>
<td>Keypad direct key inputs [4: 0]</td>
</tr>
<tr>
<td>KP_MKIN[3: 0]</td>
<td>I</td>
<td>Keypad matrix key inputs [3: 0]</td>
</tr>
<tr>
<td>KP_MKOUT[3: 0]</td>
<td>O</td>
<td>Keypad matrix key outputs [3: 0]</td>
</tr>
</tbody>
</table>

##### Miscellaneous

<table>
<tbody>
<tr>
<td rowspan=1 colspan=2><strong>Signal/Pin</strong></td>
<td rowspan=2 colspan=1><strong>Description</strong></td>
</tr>
<tr>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
</tr>
<tr>
<td>MPLL_TST_CK</td>
<td> </td>
<td>PLL test pin</td>
</tr>
<tr>
<td>MN_CLK_OUT</td>
<td>O</td>
<td>Fractional (M/N) divided clock.<br/>Main PMU general purpose M/N fractional clock divider clock output. <br/>CLK_REQ must be set as Function 0 and pulled high for the 13 MHz clock to be output on GPIO[122] (MN_CLK_OUT).</td>
</tr>
<tr>
<td>Sleep_OUT</td>
<td>O</td>
<td>PMIC sleep setting</td>
</tr>
</tbody>
</table>

#### SPIx

<table>
<tbody>
<tr>
<td rowspan=1 colspan=2><strong>Signal/Pin</strong></td>
<td rowspan=2 colspan=1><strong>Description</strong></td>
</tr>
<tr>
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
</tr>
<tr>
<td>SPIx_FRM<br/></td>
<td>I/O<br/></td>
<td>Synchronous serial port frame 0/2.<br/>The serial frame sync can be configured as an output (master mode operation) or an input (slave mode operation).</td>
</tr>
<tr>
<td>SPIx_RXD</td>
<td>I</td>
<td>Synchronous serial port receive data 0/2.<br/>Serial data latched using the bit clock.</td>
</tr>
<tr>
<td>SPIx_SCLK</td>
<td>I/O</td>
<td>Synchronous serial port clock 0/2.<br/>The serial bit clock can be configured as an output (master mode operation) or an input (slave mode operation).</td>
</tr>
<tr>
<td>SPIx_TXD</td>
<td>O</td>
<td>Synchronous serial port transmit data 0/2.<br/>Serial data driven out synchronously with the bit clock.</td>
</tr>
</tbody>
</table>

#### TWSI

##### Dedicated

| Signal/Pin Name      | Type | Description                     |
|-----------|------|---------------------------------|
| PWR_SDA   | I/O  | TWSI serial data/address signal |
| PWR_SCL   | I/O  | TWSI serial clock line signal   |

##### Common

| Signal/Pin Name       | Type   | Description |
|------------|--------|-------------|
| I2Cx_SCL   | I/O,OD | TWSIx clock |
| I2Cx_SDA   | I/O,OD | TWSIx data  |

#### UARTx

| Signal/Pin Name          | Type | Description           |
|---------------|------|-----------------------|
| UARTx_CTSn    | I    | UARTx clear-to-send   |
| UARTx_RTSn    | O    | UARTx request-to-send |
| UARTx_RXD     | I    | UARTx receive data    |
| UARTx_TXD     | O    | UARTx transmit data   |

#### USB

| Signal/Pin Name | Type | Description           |
|------------|------|-----------------------|
| USBx_N     | I/O  | USB D±                |
| USBx_P     | I/O  | USB D±                |
| VBUS_ON    | I    | USB VBUS present indicator |

### 4.5 Multi-Function I/O Pin Assignments

All functions that are assigned to a pin as its primary functions are tabled below.

| Group     | Pad Name           | Default Pulling | Pad Edge Detected | Function 0                     | Function 1                        | Function 2                   | Function 3                    | Function 4            | Function 5        | Function 6        |
|-----------|--------------------|------------------|--------------------|--------------------------------|-----------------------------------|------------------------------|-------------------------------|-----------------------|-------------------|-------------------|
| **QSPI**      | QSPI_DAT3          | DOWN             | ENABLE             | QSPI_DAT[3]/strap[3]           | GPIO[98]                          |                              | UART1_TXD <secure domain>     |                       |                   |                   |
|           | QSPI_DAT2          | DOWN             | ENABLE             | QSPI_DAT[2]/strap[2]           | GPIO[99]                          |                              | UART1_RXD <secure domain>     |                       |                   |                   |
|           | QSPI_DAT1          | DOWN             | ENABLE             | QSPI_DAT[1]/strap[1]           | GPIO[100]                         |                              | UART1_CTS <secure domain>     | UART4_TXD             |                   |                   |
|           | QSPI_DAT0          | DOWN             | ENABLE             | QSPI_DAT[0]/strap[0]           | GPIO[101]                         |                              | UART1_RTS <secure domain>     | UART4_RXD             |                   |                   |
|           | QSPI_CLK           | DOWN             | ENABLE             | QSPI_CLK                       | GPIO[102]                         |                              | UART5_TXD                     |                       |                   |                   |
|           | QSPI_CS1           | UP               | ENABLE             | QSPI_CS1                       | GPIO[103]                         |                              | UART5_RXD                     |                       |                   |                   |
| **SD/MMC**    | MMC1_DAT3          | UP               | ENABLE             | MMC1_DAT[3]                    | R_I2S2_SCLK                       | SEC2_TMS                     | UART0_TXD                     | GPIO[104]             | PWM0              |                   |
|           | MMC1_DAT2          | UP               | ENABLE             | MMC1_DAT[2]                    | R_I2S2_LRCK                       | SEC2_TDI                     | UART0_RXD                     | GPIO[105]             | PWM1              |                   |
|           | MMC1_DAT1          | UP               | ENABLE             | MMC1_DAT[1]                    | R_I2S2_TXD                        | SEC2_TDO                     |                               | GPIO[106]             | PWM2              |                   |
|           | MMC1_DAT0          | UP               | ENABLE             | MMC1_DAT[0]                    | R_I2S2_RXD                        | SEC2_TRSTn                   |                               | GPIO[107]             | PWM3              |                   |
|           | MMC1_CMD           | UP               | ENABLE             | MMC1_CMD                       | UART0_TXD                         | CPU_SEL                      | R_UART0_TXD                   | GPIO[108]             | PWM4              |                   |
|           | MMC1_CLK           | DOWN             | ENABLE             | MMC1_CLK                       | R_I2S2_SYSCLK                     | SEC2_TCK                     |                               | GPIO[109]             | PWM5              |                   |
| **PMIC**      | RESET_IN_N         | UP               | NO                 | RESET_IN_N                     |                                   |                              |                               |                       |                   |                   |
|           | EXT_32K_IN         | DOWN             | NO                 | EXT_32K_IN                     |                                   |                              |                               |                       |                   |                   |
|           | PWR_SCL            | UP               | ENABLE             | PWR_SCL                        | GPIO[93]                          |                              |                               |                       |                   |                   |
|           | PWR_SDA            | UP               | ENABLE             | PWR_SDA                        | GPIO[94]                          |                              |                               |                       |                   |                   |
|           | SLEEP_OUT          | NO               | ENABLE             | SLEEP_OUT                      | GPIO[95]                          |                              |                               |                       |                   |                   |
|           | DVL0               | DOWN             | ENABLE             | DVL0                           | GPIO[96]                          | VCXO_REQ                     |                               |                       |                   |                   |
|           | DVL1               | DOWN             | ENABLE             | DVL1                           | GPIO[97]                          | IR_RX<br>VCXO_OUT            |                               |                       |                   |                   |
|           | PMIC_INT_N         | UP               | ENABLE             | PMIC_INT_N                     |                                   |                              |                               |                       |                   |                   |
|           | GPIO[81]           | UP               | ENABLE             | GPIO[81]                       | R_I2S3_SCLK                       | UART3_TXD                    | UART4_CTS_N                   | MN_CLK                | AP_I2C5_SCL       |                   |
|           | GPIO[82]           | UP               | ENABLE             | GPIO[82]                       | R_I2S3_LRCK                       | UART3_RXD                    | UART4_RTS_N                   | UART8_TXD             | AP_I2C5_SDA       |                   |
|           | GPIO[83]           | UP               | ENABLE             | GPIO[83]                       | R_I2S3_TXD                        | UART3_CTS_N                  | UART4_TXD                     | UART8_RXD             | AP_I2C6_SCL       |                   |
|           | GPIO[84]           | UP               | ENABLE             | GPIO[84]                       | R_I2S3_RXD                        | UART3_RTS_N                  | UART4_RXD                     | AP_I2C2_SCL           |                   |                   |
|           | GPIO[85]           | UP               | ENABLE             | GPIO[85]                       | R_I2S3_SYSCLK                     | UART6_CTS_N                  | MN_CLK2                       | AP_I2C2_SDA           |                   |                   |
|           | GPIO[86]           | UP               | ENABLE             | GPIO[86]                       | HDMI_TX_HSCL                      | UART6_TXD                    | DCLK <SPI_LCD>                | UART7_CTS_N           |                   |                   |
|           | GPIO[87]           | UP               | ENABLE             | GPIO[87]                       | HDMI_TX_HSDA                      | UART6_RXD                    | DCX/DOUT1 <SPI_LCD>           | UART7_RTS_N           |                   |                   |
|           | GPIO[88]           | DOWN             | ENABLE             | GPIO[88]                       | HDMI_TX_HCEC                      | UART7_TXD                    | DIN <SPI_LCD>                 | PWM6                  |                   |                   |
|           | GPIO[89]           | DOWN             | ENABLE             | GPIO[89]                       | HDMI_TX_PDP                       | UART7_RXD                    | DOUT0 <SPI_LCD>               | VCXO_REQ              |                   |                   |
|           | GPIO[90]           | DOWN             | ENABLE             | GPIO[90]/strap[4]              |                                   | UART6_RTS_N                  | CS<SPI_LCD>                   | VCXO_OUT              | AP_I2C6_SDA       |                   |
|           | GPIO[91]           | UP               | ENABLE             | GPIO[91]                       | MN_CLK2                           | VCXO_OUT                     | DSI_TE                        | R_I2C0_SCL            |                   |                   |
|           | GPIO[92]           | UP               | ENABLE             | GPIO[92]                       | MN_CLK                            | PWM7                         | R_I2C0_SDA                    |                       |                   |                   |
|           | JTAG_SEL           | DOWN             | NO                 | JTAG_SEL                       |                                   |                              |                               |                       |                   |                   |
| **GPIO 1**    | GPIO[0]            | DOWN             | ENABLE             | GPIO[0]                        | GMAC0_RXDV                        | UART6_TXD                    | PWM8                          |                       |                   |                   |
|           | GPIO[1]            | DOWN             | ENABLE             | GPIO[1]                        | GMAC0_RX_D0                       | UART6_RXD                    | PWM9                          |                       |                   |                   |
|           | GPIO[2]            | DOWN             | ENABLE             | GPIO[2]                        | GMAC0_RX_D1                       | UART6_CTS_N                  | PWM10                         |                       |                   |                   |
|           | GPIO[3]            | DOWN             | ENABLE             | GPIO[3]                        | GMAC0_RX_CLK                      | UART6_RTS_N                  | PWM11                         |                       |                   |                   |
|           | GPIO[4]            | DOWN             | ENABLE             | GPIO[4]                        | GMAC0_RX_D2                       | UART7_TXD                    | PWM12                         |                       |                   |                   |
|           | GPIO[5]            | DOWN             | ENABLE             | GPIO[5]                        | GMAC0_RX_D3                       | UART7_RXD                    | PWM13                         |                       |                   |                   |
|           | GPIO[6]            | DOWN             | ENABLE             | GPIO[6]                        | GMAC0_TX_D0                       | UART7_CTS_N                  | PWM14                         |                       |                   |                   |
|           | GPIO[7]            | DOWN             | ENABLE             | GPIO[7]                        | GMAC0_TX_D1                       | UART7_RTS_N                  | PWM15                         |                       |                   |                   |
|           | GPIO[8]            | DOWN             | ENABLE             | GPIO[8]                        | GMAC0_TX                          | UART8_TXD                    |                               |                       |                   |                   |
|           | GPIO[9]            | DOWN             | ENABLE             | GPIO[9]                        | GMAC0_TX_D2                       | UART8_RXD                    | PWM16                         |                       |                   |                   |
|           | GPIO[10]           | DOWN             | ENABLE             | GPIO[10]                       | GMAC0_TX_D3                       | UART8_CTS_N                  | PWM17                         |                       |                   |                   |
|           | GPIO[11]           | DOWN             | ENABLE             | GPIO[11]                       | GMAC0_TX_EN                       | UART8_RTS_N                  | PWM18                         |                       |                   |                   |
|           | GPIO[12]           | DOWN             | ENABLE             | GPIO[12]                       | GMAC0_MDC                         | UART9_TXD                    | VCXO_OUT                      |                       |                   |                   |
|           | GPIO[13]           | DOWN             | ENABLE             | GPIO[13]                       | GMAC0_MDIO                        | UART9_RXD                    | PWM19                         |                       |                   |                   |
|           | GPIO[14]           | DOWN             | ENABLE             | GPIO[14]                       | GMAC0_INT_N                       | PWM0                         |                               |                       |                   |                   |
|           | GPIO[15]           | UP               | ENABLE             | GPIO[15]                       | MMC2_DATA3                        | PCIe0_PERSTN                 | PCIe1_PERSTN                  |                       |                   |                   |
|           | GPIO[16]           | UP               | ENABLE             | GPIO[16]                       | MMC2_DATA2                        | PCIe0_WAKEN<br>VCXO_REQ      | PCIe1_WAKEN                   |                       |                   |                   |
|           | GPIO[17]           | UP               | ENABLE             | GPIO[17]                       | MMC2_DATA1                        | PCIe0_CLKREQN<br>VCXO_OUT    | PCIe1_CLKREQN                 |                       |                   |                   |
|           | GPIO[18]           | UP               | ENABLE             | GPIO[18]                       | MMC2_DATA0                        | UART3_TXD                    | PCIe2_PERSTN                  |                       |                   |                   |
|           | GPIO[19]           | UP               | ENABLE             | GPIO[19]                       | MMC2_CMD                          | UART3_RXD                    | PCIe2_WAKEN                   |                       |                   |                   |
|           | GPIO[20]           | UP               | ENABLE             | GPIO[20]                       | MMC2_CLK                          | UART3_CTS_N<br>MN_CLK        | PCIe2_CLKREQN                 |                       |                   |                   |
|           | GPIO[21]           | DOWN             | ENABLE             | GPIO[21]                       | UART2_TXD                         | UART3_RTS_N                  | 32K_OUT                       |                       |                   |                   |
|           | GPIO[22]           | DOWN             | ENABLE             | GPIO[22]                       | UART2_RXD                         | PWM2                         | PWM0                          |                       |                   |                   |
|           | GPIO[23]           | DOWN             | ENABLE             | GPIO[23]                       | UART2_CTS_N                       | UART4_TXD<br>MN_CLK          | PWM1                          |                       |                   |                   |
|           | GPIO[24]           | DOWN             | ENABLE             | GPIO[24]                       | UART2_RTS_N                       | UART4_RXD<br>I2S1_SYSCLK     | PWM2                          |                       |                   |                   |
|           | GPIO[25]           | DOWN             | ENABLE             | GPIO[25]                       | I2S1_SCLK                         | UART5_TXD                    | PWM3                          |                       |                   |                   |
|           | GPIO[26]           | DOWN             | ENABLE             | GPIO[26]                       | I2S1_LRCK                         | UART5_RXD                    |                               |                       |                   |                   |
|           | GPIO[27]           | DOWN             | ENABLE             | GPIO[27]                       | I2S1_TXD                          | UART5_CTS_N                  |                               |                       |                   |                   |
|           | GPIO[28]           | DOWN             | ENABLE             | GPIO[28]                       | I2S1_RXD                          | UART5_RTS_N                  | 32K_OUT                       |                       |                   |                   |
|           | GPIO[29]           | DOWN             | ENABLE             | GPIO[29]                       | GMAC1_RXDV                        | UART1_TXD <secure domain><br>PWM1 | PCIe0_PERSTN              |                       |                   |                   |
|           | GPIO[30]           | DOWN             | ENABLE             | GPIO[30]                       | GMAC1_RX_D0                       | UART1_RXD <secure domain><br>PWM2 | PCIe0_WAKEN               |                       |                   |                   |
|           | GPIO[31]           | DOWN             | ENABLE             | GPIO[31]                       | GMAC1_RX_D1                       | UART1_CTS_N <secure domain><br>32K_OUT | PCIe0_CLKREQN         |                       |                   |                   |
|           | GPIO[32]           | DOWN             | ENABLE             | GPIO[32]                       | GMAC1_RX_CLK                      | UART1_RTS_N <secure domain><br>MN_CLK | PCIe1_PERSTN          |                       |                   |                   |
|           | GPIO[33]           | DOWN             | ENABLE             | GPIO[33]                       | GMAC1_RX_D2                       | UART4_TXD<br>PWM3            | PCIe1_WAKEN                   |                       |                   |                   |
|           | GPIO[34]           | DOWN             | ENABLE             | GPIO[34]                       | GMAC1_RX_D3                       | UART4_RXD<br>PWM4            | PCIe1_CLKREQN                 |                       |                   |                   |
|           | GPIO[35]           | DOWN             | ENABLE             | GPIO[35]                       | GMAC1_TX_D0                       | UART4_CTS_N<br>PWM5          | PCIe2_PERSTN                  |                       |                   |                   |
|           | GPIO[36]           | DOWN             | ENABLE             | GPIO[36]                       | GMAC1_TX_D1                       | UART4_RTS_N<br>PWM6          | PCIe2_WAKEN                   |                       |                   |                   |
|           | GPIO[37]           | DOWN             | ENABLE             | GPIO[37]                       | GMAC1_TX                          | PWM7                         | PCIe2_CLKREQN                 |                       |                   |                   |
|           | GPIO[38]           | UP               | ENABLE             | GPIO[38]                       | GMAC1_TX_D2                       | AP_I2C3_SCL <secure domain><br>R_I2S3_SCLK | PWM8              |                       |                   |                   |
|           | GPIO[39]           | UP               | ENABLE             | GPIO[39]                       | GMAC1_TX_D3                       | AP_I2C3_SDA <secure domain><br>R_I2S3_LRCK | PWM9              |                       |                   |                   |
|           | GPIO[40]           | UP               | ENABLE             | GPIO[40]                       | GMAC1_TX_EN                       | AP_I2C4_SCL<br>R_I2S3_TXD    | PWM10                         |                       |                   |                   |
|           | GPIO[41]           | UP               | ENABLE             | GPIO[41]                       | GMAC1_MDC                         | AP_I2C4_SDA<br>R_I2S3_RXD    | PWM11                         |                       |                   |                   |
|           | GPIO[42]           | DOWN             | ENABLE             | GPIO[42]                       | GMAC1_MDIO                        | UART5_TXD<br>R_I2S3_SYSCLK   | PWM12                         |                       |                   |                   |
|           | GPIO[43]           | DOWN             | ENABLE             | GPIO[43]                       | GMAC1_INT_N                       | UART5_RXD                    | PWM13                         |                       |                   |                   |
|           | GPIO[44]           | DOWN             | ENABLE             | GPIO[44]                       | MN_CLK                            | UART5_CTS_N<br>R_IR_RX       | PWM14                         |                       |                   |                   |
|           | GPIO[45]           | DOWN             | ENABLE             | GPIO[45]                       | GMAC0_CLK_REF                     | UART5_RTS_N                  | PWM15                         |                       |                   |                   |
|           | GPIO[46]           | DOWN             | ENABLE             | GPIO[46]                       | GMAC1_CLK_REF                     |                              | PWM16                         |                       |                   |                   |
|           | GPIO[110]          | DOWN             | ENABLE             | GPIO[110]                      | R_CAN_TX0                         | R_UART1_TXD                  | UART9_CTS_N                   | PCIe0_PERSTN          | ONE_WIRE          |                   |
|           | GPIO[115]          | DOWN             | ENABLE             | GPIO[115]                      | R_CAN_RX0                         | R_UART1_RXD                  | UART9_RTS_N                   | PCIe0_WAKEN           |                   |                   |
|           | GPIO[116]          | DOWN             | ENABLE             | GPIO[116]                      | R_PWM1                            | R_UART1_CTS_N                | UART9_TXD                     | PCIe0_CLKREQN         | VCXO_REQ[1]       |                   |
|           | GPIO[117]          | DOWN             | ENABLE             | GPIO[117]                      | R_PWM2                            | R_UART1_RTS_N                | UART9_RXD                     | PCIe2_CLKREQN         | VCXO_CLK_OUT      |                   |
|           | GPIO[118]          | UP               | ENABLE             | GPIO[118]                      | AP_I2C7_SCL (CAM)                 | AP_I2C6_SCL                  | I2S0_SCLK                     | R_PWM8                | KP_MKIN[0]        |                   |
|           | GPIO[119]          | UP               | ENABLE             | GPIO[119]                      | AP_I2C7_SDA (CAM)                 | AP_I2C6_SDA                  | I2S0_LRCK                     | R_PWM9                | KP_MKOUT[0]       |                   |
|           | GPIO[120]          | DOWN             | ENABLE             | GPIO[120]                      | CAM_MCLK2                         | I2S0_TXD                     | R_PWM6                        | KP_MKIN[1]            |                   |                   |
|           | GPIO[121]          | DOWN             | ENABLE             | GPIO[121]                      | CAMERA2_RST                       | VBUS_ON2                     | I2S0_RXD                      | R_PWM7                | KP_MKOUT[1]       |                   |
|           | GPIO[122]          | DOWN             | ENABLE             | GPIO[122]                      | CAMERA2_PDN                       | USB_ID2                      | I2S0_SYSCLK                   | KP_MKIN[2]            |                   |                   |
|           | GPIO[123]          | DOWN             | ENABLE             | GPIO[123]                      | DRIVE_VBUS2_ISO                   | KP_DKIN[0]                   | KP_MKIN[0]                    |                       |                   |                   |
|           | GPIO[124]          | DOWN             | ENABLE             | GPIO[124]                      | DRIVE_VBUS1_ISO                   | KP_DKIN[1]                   | KP_MKOUT[0]                   |                       |                   |                   |
|           | GPIO[125]          | DOWN             | ENABLE             | GPIO[125]                      | VBUS_ON0                          | KP_DKIN[2]                   | KP_MKIN[1]                    |                       |                   |                   |
|           | GPIO[126]          | DOWN             | ENABLE             | GPIO[126]                      | USB_ID0                           | KP_DKIN[3]                   | KP_MKOUT[1]                   |                       |                   |                   |
|           | GPIO[127]          | DOWN             | ENABLE             | GPIO[127]                      | DRIVE_VBUS0_ISO                   | KP_DKIN[4]                   | KP_MKIN[2]                    |                       |                   |                   |
| **GPIO 2**    | GPIO[75]           | UP               | ENABLE             | GPIO[75]                       | SPI2_SCLK <secure domain>         | SPI3_SCLK                    | CAN_TX0                       | UART8_TXD             | AP_I2C4_SCL       |                   |
|           | GPIO[76]           | UP               | ENABLE             | GPIO[76]                       | SPI2_FRM <secure domain>          | SPI3_FRM                     | CAN_RX0                       | UART8_RXD             | AP_I2C4_SDA       |                   |
|           | GPIO[77]           | UP               | ENABLE             | GPIO[77]                       | SPI2_TXD <secure domain>          | SPI3_TXD                     | AP_I2C3_SCL <secure domain>   | UART8_CTS_N           | R_PWM0            | KP_MKOUT[2]       |
|           | GPIO[78]           | UP               | ENABLE             | GPIO[78]                       | SPI2_RXD <secure domain>          | SPI3_RXD                     | AP_I2C3_SDA <secure domain>   | UART8_RTS_N           | R_PWM1            | KP_MKIN[3]        |
|           | GPIO[79]           | DOWN             | ENABLE             | GPIO[79]                       | IR_RX                             | R_PWM2                       |                               |                       |                   | KP_MKOUT[3]       |
|           | GPIO[80]           | DOWN             | ENABLE             | GPIO[80]                       | MMC_Card_detect                   | R_PWM3                       | UART0_RXD<br>R_UART0_RXD      |                       |                   |                   |
| **GPIO 3**    | GPIO[47]           | UP               | ENABLE             | GPIO[47]                       | R_UART0_TXD                       | R_CAN_TX0                    | R_PWM8                        | AP_I2C3_SCL<secure domain> | ONE_WIRE          |                   |
|           | GPIO[48]           | UP               | ENABLE             | GPIO[48]                       | R_UART0_RXD                       | R_CAN_RX0                    | R_IR_RX                       | AP_I2C3_SDA<secure domain> | KP_MKOUT[2]       |                   |
|           | GPIO[49]           | UP               | ENABLE             | GPIO[49]                       | R_SPI_SCLK                        | R_UART1_CTS_N                | R_PWM4                        | R_I2C0_SCL            | KP_MKIN[3]        |                   |
|           | GPIO[50]           | UP               | ENABLE             | GPIO[50]                       | R_SPI_FRM                         | R_UART1_RTS_N                | R_PWM5                        | R_I2C0_SDA            | KP_MKOUT[3]       |                   |
|           | GPIO[51]           | UP               | ENABLE             | GPIO[51]                       | R_SPI_TXD                         | R_UART1_TXD                  | R_PWM6                        | AP_I2C4_SCL           |                   |                   |
|           | GPIO[52]           | UP               | ENABLE             | GPIO[52]                       | R_SPI_RXD                         | R_UART1_RXD                  | R_PWM7                        | AP_I2C4_SDA           |                   |                   |
| **GPIO 4**    | GPIO[53]           | DOWN             | ENABLE             | GPIO[53]                       | CAM_MCLK0                         | PWM17                        | PCIe0_CLKREQN                 | UART3_TXD             |                   |                   |
|           | GPIO[54]           | UP               | ENABLE             | GPIO[54]                       | AP_I2C0_SCL (CAM)                 | CAN_TX0                      | PCIe0_PERSTN                  | UART3_RXD             | AP_I2C5_SCL       |                   |
|           | GPIO[55]           | UP               | ENABLE             | GPIO[55]                       | AP_I2C0_SDA (CAM)                 | CAN_RX0                      | PCIe0_WAKEN                   | UART3_CTS_N           | AP_I2C5_SDA       |                   |
|           | GPIO[56]           | UP               | ENABLE             | GPIO[56]                       | AP_I2C1_SCL (CAM)                 | UART6_TXD                    | PCIe1_PERSTN                  | UART3_RTS_N           | AP_I2C6_SCL       |                   |
|           | GPIO[57]           | UP               | ENABLE             | GPIO[57]                       | AP_I2C1_SDA (CAM)                 | UART6_RXD                    | PCIe1_WAKEN                   | PWM18                 | AP_I2C6_SDA       |                   |
|           | GPIO[58]           | DOWN             | ENABLE             | GPIO[58]                       | CAM_MCLK1                         | I2S0_SYSCLK                  | PCIe1_CLKREQN                 | IR_RX                 |                   |                   |
|           | GPIO[111]          | DOWN             | ENABLE             | GPIO[111]                      | CAMERA0_RST                       | I2S0_SCLK                    | PCIe2_PERSTN                  | UART4_TXD             |                   |                   |
|           | GPIO[112]          | DOWN             | ENABLE             | GPIO[112]                      | CAMERA1_RST                       | I2S0_LRCK                    | PCIe2_WAKEN                   | UART4_RXD             |                   |                   |
|           | GPIO[113]          | DOWN             | ENABLE             | GPIO[113]                      | CAMERA0_PDN                       | I2S0_TXD                     | PCIe2_CLKREQN                 | UART4_CTS_N           |                   |                   |
|           | GPIO[114]          | DOWN             | ENABLE             | GPIO[114]                      | CAMERA1_PDN                       | I2S0_RXD                     | DSI_TE                        | UART4_RTS_N           |                   |                   |
|           | GPIO[63]           | DOWN             | ENABLE             | GPIO[63]                       | DRIVE_VBUS0_ISO                   | R_I2S2_SYSCLK                | PWM19                         | KP_DKIN[0]            |                   |                   |
|           | GPIO[64]           | DOWN             | ENABLE             | GPIO[64]                       | VBUS_ON0                          | R_I2S2_SCLK                  | SPI2_SCLK <secure domain>     | R_PWM0                | KP_DKIN[1]        |                   |
|           | GPIO[65]           | UP               | ENABLE             | GPIO[65]                       | USB_ID0                           | R_I2S2_LRCK                  | SPI2_FRM <secure domain>      | R_PWM1                | KP_DKIN[2]        |                   |
|           | GPIO[66]           | DOWN             | ENABLE             | GPIO[66]                       | DRIVE_VBUS1_ISO                   | R_I2S2_TXD                   | SPI2_TXD <secure domain>      | R_PWM2                | KP_DKIN[3]        |                   |
|           | GPIO[67]           | DOWN             | ENABLE             | GPIO[67]                       | DRIVE_VBUS2_ISO                   | R_I2S2_RXD                   | SPI2_RXD <secure domain>      | R_PWM3                | KP_DKIN[4]        |                   |
|           | GPIO[68]           | DOWN             | ENABLE             | GPIO[68]                       | VBUS_ON2                          | UART0_TXD                    | AP_I2C2_SCL                   | R_PWM4                |                   |                   |
|           | GPIO[69]           | UP               | ENABLE             | GPIO[69]                       | USB_ID2                           | UART0_RXD                    | AP_I2C2_SDA                   | R_PWM5                |                   |                   |
| **GPIO 5**    | GPIO[59]           | UP               | ENABLE             | GPIO[59]                       | HDMI_TX_HSCL                      | SPI3_SCLK                    | UART1_TXD <secure domain>     | PCIe1_PERSTN          |                   |                   |
|           | GPIO[60]           | UP               | ENABLE             | GPIO[60]                       | HDMI_TX_HSDA                      | SPI3_FRM                     | UART1_RXD <secure domain>     | PCIe1_WAKEN           |                   |                   |
|           | GPIO[61]           | UP               | ENABLE             | GPIO[61]                       | HDMI_TX_HCEC                      | SPI3_TXD                     | UART1_CTS_N <secure domain>   | PCIe1_CLKREQN         |                   |                   |
|           | GPIO[62]           | UP               | ENABLE             | GPIO[62]                       | HDMI_TX_PDP                       | SPI3_RXD                     | UART1_RTS_N <secure domain>   | PCIe2_PERSTN          |                   |                   |
|           | PRI_TDI            | UP               | NO                 | PRI_TDI                        | GPIO[70]                          | AP_I2C2_SCL                  | DCLK <SPI_LCD>                | UART5_TXD             |                   |                   |
|           | PRI_TMS            | UP               | NO                 | PRI_TMS                        | GPIO[71]                          | AP_I2C2_SDA                  | DCX/DOUT1 <SPI_LCD>           | UART5_RXD             |                   |                   |
|           | PRI_TCK            | DOWN             | NO                 | PRI_TCK                        | GPIO[72]                          | UART9_TXD                    | DIN<SPI_LCD>                  | UART5_CTS_N           |                   |                   |
|           | PRI_TDO            | UP               | NO                 | PRI_TDO                        | GPIO[73]                          | UART9_RXD                    | DOUT0 <SPI_LCD>               | UART5_RTS_N           |                   |                   |
|           | PRI_TRSTn          | UP               | NO                 | PRI_TRSTn                      |                                   |                              |                               |                       |                   |                   |
|           | GPIO[74]           | UP               | ENABLE             | GPIO[74]                       |                                   | PWM9                         | CS<SPI_LCD>                   | PCIe2_WAKEN           |                   |                   |
| **EMMC5.1**   | EMMC_D0            |                  |                    | EMMC_D0                        | GPIO[93]                          |                              |                               |                       |                   |                   |
|           | EMMC_D1            |                  |                    | EMMC_D1                        | GPIO[94]                          |                              |                               |                       |                   |                   |
|           | EMMC_D2            |                  |                    | EMMC_D2                        | GPIO[95]                          |                              |                               |                       |                   |                   |
|           | EMMC_D3            |                  |                    | EMMC_D3                        | GPIO[96]                          |                              |                               |                       |                   |                   |
|           | EMMC_D4            |                  |                    | EMMC_D4                        | GPIO[97]                          |                              |                               |                       |                   |                   |
|           | EMMC_D5            |                  |                    | EMMC_D5                        | GPIO[98]                          |                              |                               |                       |                   |                   |
|           | EMMC_D6            |                  |                    | EMMC_D6                        | GPIO[99]                          |                              |                               |                       |                   |                   |
|           | EMMC_D7            |                  |                    | EMMC_D7                        | GPIO[100]                         |                              |                               |                       |                   |                   |
|           | EMMC_DS            |                  |                    | EMMC_DS                        | GPIO[101]                         |                              |                               |                       |                   |                   |
|           | EMMC_CLK           |                  |                    | EMMC_CLK                       | GPIO[102]                         |                              |                               |                       |                   |                   |
|           | EMMC_CMD           |                  |                    | EMMC_CMD                       | GPIO[103]                         |                              |                               |                       |                   |                   |

### 4.6 Power Supply Pins

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

### 4.7 Multi-Function Pin Registers

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

| Item             | Symbol/Pin        | Min    | Typ   | Max    | Unit | Note               |
|------------------|-------------------|--------|-------|--------|------|--------------------|
| Digital Power    | VCC_M1            | 0.85   | 0.9   | 1.0    | V    |                    |
| PLL              | AVDD09_PLL        | 0.855  | 0.9   | 0.945  | V    |                    |
| PLL              | AVDD18_PLL        | 1.71   | 1.8   | 1.89   | V    |                    |
| OSC              | AVDD09_AFEAP      | 0.855  | 0.9   | 0.945  | V    |                    |
| OSC              | AVDD18_AFEAP      | 1.71   | 1.8   | 1.89   | V    |                    |
| PCIeC            | AVDD18_PCIEC      | 1.71   | 1.8   | 1.89   | V    |                    |
| PCIeC            | AVDD09_PCIEC      | 0.855  | 0.9   | 0.945  | V    |                    |
| PCIeB            | AVDD18_PCIEB      | 1.71   | 1.8   | 1.89   | V    |                    |
| PCIeB            | AVDD09_PCIEB      | 0.855  | 0.9   | 0.945  | V    |                    |
| PCIeA            | AVDD18_PCIEA      | 1.71   | 1.8   | 1.89   | V    |                    |
| PCIeA            | AVDD09_PCIEA      | 0.855  | 0.9   | 0.945  | V    |                    |
| USB IO           | AVDD33_USB        | 3.135  | 3.3   | 3.465  | V    |                    |
| USB PHY          | AVDD18_USB        | 1.71   | 1.8   | 1.89   | V    |                    |
| USB PHY          | AVDD09_USB        | 0.855  | 0.9   | 0.945  | V    |                    |
| MIPI DSI PHY     | AVDD09_DSI1       | 0.855  | 0.9   | 0.945  | V    |                    |
| MIPI DSI PHY     | AVDD18_DSI1       | 1.71   | 1.8   | 1.89   | V    |                    |
| MIPI DSI IO      | AVDD12_DSI1       | 1.14   | 1.2   | 1.26   | V    |                    |
| MIPI CSI PHY     | AVDD09_CSI        | 0.855  | 0.9   | 0.945  | V    |                    |
| MIPI CSI PHY     | AVDD18_CSI        | 1.71   | 1.8   | 1.89   | V    |                    |
| HDMI             | AVDD09_HDMI       | 0.855  | 0.9   | 0.945  | V    |                    |
| HDMI             | AVDD18_HDMI       | 1.71   | 1.8   | 1.89   | V    |                    |
| HDMI             | AVDD33_HDMI       | 3.135  | 3.3   | 3.465  | V    |                    |
| eMMC             | VDD09_EMMC        | 0.855  | 0.9   | 0.945  | V    |                    |
| eMMC             | V18_EMMC          | 1.71   | 1.8   | 1.89   | V    |                    |
| QSPI             | VCC1833_QSPI      | 1.71   | 1.8   | 1.89   | V    | Dual power domain  |
| QSPI             | VCC1833_QSPI      | 3.135  | 3.3   | 3.465  | V    | Dual power domain  |
| SD               | VCC1833_MMC1      | 1.71   | 1.8   | 1.89   | V    | Dual power domain  |
| SD               | VCC1833_MMC1      | 3.135  | 3.3   | 3.465  | V    | Dual power domain  |
| DDR PHY          | AVDD18_PHY        | 1.71   | 1.8   | 1.89   | V    |                    |
| DDR PHY          | AVDD18_DDR        | 1.71   | 1.8   | 1.89   | V    |                    |
| DDR PHY          | AVDD11_DDR        | 1.045  | 1.1   | 1.155  | V    | LP4/4X             |
| DDR PHY          | AVDD11_DDR        | 1.14   | 1.2   | 1.26   | V    | LP3                |
| DDR PHY          | AVDDU_PHY         | 0.855  | 0.9   | 0.945  | V    |                    |
| DDR PHY          | AVDDU_DDR         | 0.855  | 0.9   | 0.945  | V    |                    |
| DDR IO           | AVDD06_DDR        | 0.57   | 0.6   | 0.63   | V    |                    |
| DDR IO           | VDDQ_V1P2         | 1.14   | 1.2   | 1.26   | V    |                    |
| eFuse            | AVDD18_EFUSE      | 1.71   | 1.8   | 1.89   | V    |                    |
| Audio Logic      | AUD_VDDU09        | 0.855  | 0.9   | 0.945  | V    |                    |
| Audio Power NEG  | AUD_VNEG          | -1.71  | -1.8  | -1.89  | V    |                    |
| Audio Power POS  | AUD_VPOS          | 1.71   | 1.8   | 1.89   | V    |                    |
| Audio Analog     | AVDD18_AUD        | 1.71   | 1.8   | 1.89   | V    |                    |
| Audio Analog     | AVDD3V3_AUD       | 3.135  | 3.3   | 3.465  | V    |                    |
| GPIO             | VCC18_GPIO        | 1.71   | 1.8   | 1.89   | V    |                    |
| GIOP3            | VCC1833_GPIO3     | 1.71   | 1.8   | 1.89   | V    | Dual power domain  |
| GIOP3            | VCC1833_GPIO3     | 3.135  | 3.3   | 3.465  | V    | Dual power domain  |
| GIOP2            | VCC1833_GPIO2     | 1.71   | 1.8   | 1.89   | V    | Dual power domain  |
| GIOP2            | VCC1833_GPIO2     | 3.135  | 3.3   | 3.465  | V    | Dual power domain  |

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
