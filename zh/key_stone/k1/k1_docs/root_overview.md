sidebar_position: 1

# K1 产品简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_%E4%BA%A7%E5%93%81%E7%AE%80%E4%BB%8B_CN-V2.4-20260127-01.pdf)**

## 概述

K1 系列是 8 核 64 位 RISC-V AI CPU。
K1 采用同构融合计算技术，集成进迭时空自研的 8 个高性能计算核 X60，可提供 50KDMIPS 通用算力，同时融合 2 TOPS AI 算力，可流畅运行 0.5B、1B 的本地大模型。
K1 系列芯片主要应用在 AI 边缘计算机、AI + 硬件、智能机器人、工业主控、云电脑、开源鸿蒙应用等领域。

- **出色的 CPU 性能**
8 核 RISC-V AI CPU，提供 50KDMIPS CPU 算力，单核 CPU 性能 Specint2006 >4.0/GHz。

- **同构融合 AI 算力，卓越的本地大模型运行能力**
提供 2 TOPS AI 算力，以并行计算的 AI-CPU 核提供原生 AI 算力，实现与所有主流 AI 生态的快速对接，大模型算力 > 10 Tokens/S @1B 本地大模型。

- **最新的 RISC-V 架构，强大的并行计算能力**
支持 RVA22 Profile、256bit RVV 1.0 标准的 RISC-V CPU，提供 2 倍于 Neon 的并行处理算力，向量性能是 ARM NEON 的 150% 以上。

- **领先的算力能效**
RISC-V 架构的精简和卓越的微架构设计，同负载场景功耗只有同档芯片的 80% 。

- **丰富的 IO 能力**
集成多套 PCIe、USB、GMAC、SPI 等接口，提供全面的外设连接选型。

- **符合工业级标准**
CPU 在 -40˚C～85˚C 的环境温度下仍能提供稳定可靠的持续算力输出，满足工业应用的苛刻环境需求。

## 特性

- **处理器**
  - 最新的 RVA22 Profile 架构
  - 八核 X60™ 64 位 AI 处理器
  - 八级双发按序流水线
  - 支持 256-bit RVV1.0 标准
  - CPU 融合 2.0 TOPS AI 算力
  - 八核共享 1MB L2 Cache

- **RISC-V 融合 AI 技术**
  - AI-CPU 融合 2.0 TOPS AI 算力
  - 大模型算力 > 10Tokens/S@1B 本地大模型
  - 支持所有的 AI 算法和模型，支持所有的本地大模型
  - 遵循 CPU 编程范式，实现 AI 算法的部署成本为零

- **RISC-V 安全架构**
  - 支持 RISC-V PMP 安全规范和 ePMP 安全扩展
  - 支持安全启动、安全存储、签名校验
  - 支持 AES/SHA/RSA 等算法
  - 支持产品生命周期安全管理

- **RCPU**
  - RISC-V 实时 CPU，主频 300MHz
  - 支持异构双系统

- **内存**
  - 32bit LPDDR4/LPDDR4X - 最高支持 2400MT/s
  - 最大支持 16 GB、带宽可达 10.6 GB/s

- **存储**
  - 支持 SPI 闪存
  - 支持 eMMC 5.1
  - 支持 SDIO3.0 SD 卡
  - 支持 SSD：NVMe over PCIe

- **多媒体和显示**
  - 支持 3D 图形引擎 OpenCL 3.0、OpenGLES 1.1/3.2、Vulkan 1.3
  - 支持 4K H.265/H.264/VP9/VP8 等编解码格式
  - 支持双屏异显，最高可达 1920 ×1440@60fps
  - 通过 MIPI-DSI、HDMI 输出
  - 支持三摄输入，单摄最高支持 16MP
  - MIPI-CSI 8Lanes（4+2+2 或 4+4）

- **接口**
  - 5 × PCIe2.1（x2 + x2 + x1 组合、5Gbps/Lane）
  - 1 × USB3.0（Combo with PCIe2.1 x1）
  - 2 × USB2.0（OTG + Host）
  - 2 × GMAC（RGMII&1000M）
  - 4 × SPI、7 × I2C、12 × UART、2 × CAN-FD、30 × PWM

- **GPIO**
  - GPIO-3.3V 数量：24
  - GPIO-1.8V 数量：104

- **操作系统**
  - Bianbu OS
  - Linux 主流发行版本
  - RTOS

- **封装**
  - 封装类型：
    - FCCSP 17mm * 17mm
    - FCBGA 19mm * 19mm（pin to pin）
  - 管脚间距：0.65mm

- **功耗**
  - TDP：3 ～ 5W

## 框图

![](./static/k1_blockdiagram.png)
