# 1. Overview

```
Last Version: 2025/xx/xx
```

## 1.1 Introduction

SpacemiT Key Stone® K1 is a high-performance and ultra-low-power SoC that integrates 8 RISC-V CPU cores with SpacemiT® Daoyi™ AI computing power. It comes with the following most relevant advantages:

- Integration with SpacemiT® self-innovated X60™ RISC-V core processor which adheres to the RISC-V 64GCVB architecture and RVA22 standard
- Capable of delivering 2.0 TOPS AI computing power by leveraging customized RISC-V instructions to enable CPU AI fusion computing
- Support for the popular AI inference frameworks such as TensorFlow Lite, TensorFlow, and ONNX Runtime
- Attainment of ultra-low power consumption through the incorporation of multiple granular power islands and dynamic power state adjustments, making K1 highly competitive in energy efficiency
- Availability of full-feature interfaces for enabling innovative applications and products
- Compatibility with mainstream OS to meet the needs of various application scenarios
- Compliance with the industrial-grade reliability standards

## 1.2 General Features

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

## 1.3 Multimedia Features

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

## 1.4 Block Diagram

The architecture of K1 is depicted below.  
![K1 Block Diagram](./static/k1_blockdiagram.png)