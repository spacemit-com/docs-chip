---
title: V100 产品简介
sidebar_position: 1
---

# V100 产品简介

点击下载 **[V100 产品简介（PDF）](https://cdn-resource.spacemit.com/file/chip/V100/v100_brief_zh.pdf)**

## 概述

SpacemiT Vital Stone RISC-V 服务器级 CPU V100 兼具高主频、高核数、高可靠性、强可扩展性与高安全性等核心优势。芯片集成 46 个RISC-V CPU 核，全面兼容 RISC-V RVA23 Profile，主频最高可达 2.4GHz，为数据中心提供强劲算力支撑。

作为首颗完整符合 RISC-V 服务器规范的计算芯片，其应用覆盖数据中心 AI 训练服务器、推理服务器、计算服务器、存储服务器及边缘服务器等多元场景。

- **卓越的数据中心 CPU 性能**

  46 个 RISC-V 高性能计算核，6 个香山昆明湖 V2R2 CPU 核 + 40 个进迭时空 X100 CPU 核；香山昆明湖 V2R2 最高主频 2.1 GHz，单核 SPECint2006 ≥ 15.0/GHz；X100 最高主频 2.4 GHz，单核 SPECint2006 ≥ 9.0/GHz；支持 RVA23 Profile

- **RISC-V 服务器级虚拟化**

  支持 CPU 虚拟化，支持 Hypervisor 1.0 扩展，支持内存虚拟化，支持中断虚拟化，支持标准 AIA 中断控制器，支持基于 IOMMU 的外设虚拟化。

- **RISC-V 数据中心级安全架构**

  支持服务器可信计算、硬件信任根（RoT）、安全启动、密钥管理、生命周期管理、安全调试，支持国密主流算法。

- **高带宽大容量 DDR5**

  单芯片支持 8 个 DDR5 通道，支持 1DPC，兼容主流 DDR5 RDIMM，速率达 4800 MT/s，最大带宽 307 GB/s，具备多级仲裁、QoS 策略及带宽限制与性能监控功能。

- **RAS（Reliability, Availability, Serviceability）**

  支持完整的 RISC-V 服务器 RAS 特性，覆盖 CPU、内存、PCIe、总线等核心部件；集成多位置温度传感器，BMC 实时监控并动态调节；通过固件实现高效带内/带外管理，保障系统稳定。

- **满足智算场景的高性能 PCIe 5.0**

  支持 PCIe 5.0 标准，最大可支持 52 条高速通道，兼容 x16 至 x1 多种配置模式，可外扩 AI 智算卡，支持 4/8 卡部署，兼容 SAS/SATA、NVMe 等多类型存储设备。

- **完整符合 RISC-V 服务器规范**

  遵循 RISC-V 服务器相关标准规范，包括 RISC-V Server SoC Specification、RISC-V Server Platform Specification、RISC-V RVA23 Profile、Boot & Runtime Services（BRS）、RISC-V Security Model 等规范。

## 特性

- **46 核高性能 RISC-V 处理器**
  - 集成 6 个香山昆明湖 V2R2 CPU核+ 40 个进迭时空 X100 CPU核，支持 RVA23
  - 香山昆明湖 V2R2
    - 主频 2.1GHz
    - 支持十三级六发射乱序流水线
    - 支持 64KB L1 I-Cache, 64KB L1 D-Cache，1MB L2 Cache
  - 进迭时空 X100
    - 主频 2.4GHz
    - 支持 DVFS
    - 支持十二级四发射乱序流水线
    - 支持 64KB L1 I-Cache, 64KB L1 D-Cache，2MB L2 Cache
  - 支持 64MB SLC Cache

- **RISC-V 服务器级虚拟化**
  - CPU 虚拟化：Hypervisor 1.0 扩展，内存虚拟化（SV48×4/SV39×4 Guest地址翻译）
  - 中断虚拟化：基于 RISC-V AIA 中断架构，支持 255 个 M-mode MSI，255 个 S-mode MSI，63 个 VS-mode MSI，VS 每个 Hart 配置了 7 个vCPU
  - 外设虚拟化：支持基于 IOMMU 的 I/O 虚拟化, 实现 SR-IOV 功能，提升虚拟机 I/O 性能

- **RISC-V 服务器安全架构**
  - RISC-V 规范：支持 RISC-V 规范的 PMP/ePMP 以及 IOPMP（Rapid-k Model）等安全组件
  - 服务器安全：支持可信计算、安全启动、密钥管理、生命周期管理、安全调试
  - 安全硬件：集成 HSM 硬件安全模块，支持密钥管理以及基于硬件信任根（RoT）的安全启动
  - 安全算法：支持AES / SHA / RSA / SM2 / SM3 / SM4等密码学算法

- **RISC-V 服务器 RAS 特性**
  - RISC-V 规范：支持 RERI RAS 规范
  - CPU RAS：支持 CE / UEC 差异化处理及中断日志
  - 内存RAS：ECC / CRC 校验、巡检、故障隔离及地址保护
  - PCIe RAS：链路恢复、错误报告、热插拔及日志记录
  - 总线RAS：总线数据校验/标记、SRAM ECC 保护
  - 系统RAS：支持主板网络 / GPU / 硬盘RAS管理
  - RAS管理：遵循 Firmware First 原则，保障带内 / 带外管理高效性

- **内存**
  - 最大支持 8×DDR5 Channels，支持 1DPC
  - 支持主流 DDR5 RDIMM
  - 最高速率支持 4800MT/s，最大带宽 307GB/s
  - 单个内存通道支持 80bit DIMM（带ECC），支持 Sideband ECC 边带纠错码
  - 每个 DIMM 最大支持 256GB，单芯片最大支持 2TB

- **高速接口**
  - 支持 PCIe 5.0，提供 52 条高速通道
  - 支持 3 组 x16 / x8x8 / x8x4x4，支持1组 x2x1x1
  - 支持 SAS / SATA over PCIe、NVMe over PCIe、USB over PCIe 等
  - 1 × GMAC，支持 IEEE 1588

- **外围 I/O 接口**
  - 1×QSPI
  - 1×LPC、1×eSPI
  - 3×SPIMaster、1×SPISlave
  - 4×I3C、12×I2C、12×SMBUS
  - 5×UART

- **RISC-V 服务器基础软件**
  - 遵循 UEFI-2.11、ACPI-6.6 规范，支持基于 EDK2 的服务器 BIOS 固件
  - 支持基于 openBMC 的带内/带外管理固件
  - 支持主流的编译工具 GCC、LLVM
  - 支持 Linux 内核 6.6 及以上版本
  - 支持主流服务器操作系统，包括 openEuler、openKylin、银河麒麟（规划）、Ubuntu、Debian、Fedora 等
  - 支持主流的开源中间件及数据库，包括 Tomcat、Redis、Apache、MySQL、PostgreSQL 等
  - 支持虚拟化的基础软件 KVM、QEMU 等
  - 支持容器 Docker 部署

- **功耗**
  - TDP：120W
  - 工作环境温度：0 ~ 40°C

- **封装**
  - FCBGA，58.5 mm × 75.4 mm，0.94 mm pitch

## 产品框图

![V100 产品框图](../static/block_diagram.png)
