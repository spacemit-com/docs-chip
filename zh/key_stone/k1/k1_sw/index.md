# K1 SDK 使用说明总览

K1 芯片提供多套软件开发套件（SDK），覆盖嵌入式系统、IoT 平台及机器人应用。每套 SDK 包含 BSP、工具链、示例与文档，可根据不同产品需求选择使用。

## Buildroot SDK  

Buildroot SDK 为 SpacemiT Stone 系列芯片提供完整的 Linux BSP，包括 OpenSBI、U-Boot/UEFI、Linux 内核以及可裁剪的根文件系统（含中间件与示例）。面向需要快速构建定制化嵌入式系统的开发场景，支持驱动与应用扩展。

- **使用说明：** [Buildroot 使用指南](#)

## OpenWrt SDK  

OpenWrt SDK 基于原生 OpenWrt 23.05（bl-v2.0.y 基于 master）构建，集成 SpacemiT Stone 系列芯片的完整 BSP，包括 OpenSBI、U-Boot/UEFI、Linux 内核以及网络特性完整的根文件系统。主要面向软路由、NAS 与网络设备开发。

- **使用说明：** [OpenWrt 使用指南](#)

## Bianbu SDK  

Bianbu 是针对 RISC-V 架构深度优化的操作系统，基于 Ubuntu 社区源码构建，具备良好兼容性与可扩展性，适用于通用计算、智能终端及行业场景的产品化开发。

- **使用说明：** [Bianbu SDK 使用指南](#)

## OpenHarmony（K1 OH5.0）  

K1 OH5.0 是全球首个基于 RISC-V + OpenHarmony 5.0 的原生鸿蒙解决方案，采用 K1 RISC-V AI CPU，并运行 OpenHarmony 5.0.0.71。方案集成 AI、大模型和分布式能力，经过完整系统集成测试，并提供量产工具链及开发文档。

- **使用说明：** [K1 OH5.0 使用指南](#)

## ROS2 SDK（AI Robot 方案）  

AI Robot 是面向下一代智能机器人的协同方案，基于 K1 芯片与自研 Bianbu OS，结合 ROS2 运行框架，集成 MediaEngine、RVV-Opt 优化库与 RDK 套件。系统内置大量 AI 模型与工具链，可快速部署服务机器人、四足机器人、无人机与机械臂等应用。

- **使用说明：** [ROS2 SDK 使用指南](#)
