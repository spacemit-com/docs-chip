sidebar_position: 1

# K1 数据手册

## PDF 版本下载

点击下载 PDF 版本 [K1 Datasheet (PDF)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Datasheet_%28V7.5_2025.08.06%29.pdf)

## 1. 概述

### 1.1 简介

进迭时空的 Key Stone® K1 是一款高性能、超低功耗的片上系统（SoC），集成了 8 个 RISC-V CPU 核心，并融合了 进迭时空的道义 AI 计算能力。其主要优势包括：

- 集成进迭时空自主研发的 X60™ RISC-V 核心处理器，符合 **RISC-V 64GCVB 指令集架构** 和 **RVA22 标准**；
- 通过定制化 RISC-V 指令实现 **CPU-AI 融合计算架构**，可提供高达 **2.0 TOPS（INT8）** 的 AI 算力；
- 支持主流 AI 推理框架，包括 **TensorFlow Lite、TensorFlow** 和 **ONNX Runtime**；
- 采用多粒度电源岛设计与动态电源状态调节技术，实现超低功耗运行，在能效方面具备显著竞争优势；
- 提供完整的外设接口组合，支持各类创新应用与产品开发；
- 兼容主流操作系统，满足多样化的应用场景需求；
- 符合工业级可靠性标准，适用于严苛环境下的稳定运行。

### 1.2 主要特性

- **应用处理器（Application Processor, AP）**
  - 进迭时空 X60™ RISC-V 双簇八核处理器
  - 符合 **RISC-V 64GCVB 指令集架构** 与 **RVA22 标准**
  - **簇 0（Cluster 0）**
    - 四核配置，集成 **2.0 TOPS（INT8）AI 算力**
    - 每核配备 **32 KB L1 缓存**
    - 共享 **512 KB L2 缓存**
    - 配置 **512 KB TCM（紧耦合存储器）**
    - 支持 **256 位向量扩展（Vector Extension）**
  - **簇 1（Cluster 1）**
    - 四核配置
    - 每核配备 **32 KB L1 缓存**
    - 共享 **512 KB L2 缓存**
    - 支持 **256 位向量扩展（Vector Extension）**
  - 支持 **动态电压频率调节（DVFS）**，工作电压自适应范围为 **0.6 V 至 1.05 V**

- **DDR 内存**
  - 支持双芯片片选，**32 位 LPDDR4/LPDDR4x SDRAM**，传输速率高达 **2666 Mbps**，最大支持 **16 GB 容量**
  - 支持双芯片片选，**32 位 LPDDR3 SDRAM**，传输速率高达 **1866 Mbps**，最大支持 **4 GB 容量**

- **实时处理器（Real-Time CPU, RCPU）**
  - **256 KB SRAM ×1**
  - **R_CAN-FD ×1**
  - **R_I²C ×1**
  - **R_SPI ×2**
  - **HDMI 音频接口**
  - **R_Debug 调试接口**
  - **R_UART ×2**
  - **R_PWM ×10**
  - **DMA 控制器 ×1**
  - **R_IR_RX（红外接收）×1**

- **外设控制器（Peripheral Controller）**
  - **GPIO（×128）**
    - 共 128 个引脚
    - 支持可编程上拉/下拉电阻
    - 其中 104 个为 **1.8 V IO8** 引脚
    - 其余 24 个支持 **1.8 V / 3.3 V** 双电压 IO

  - **UART（×10）**
    - 用于应用处理器（AP）、蓝牙（BT）及调试打印等用途

  - **I²C（×10）**
    - 用于连接摄像头、重力传感器（G-Sensor）、电子罗盘（E-Compass）、接近传感器（Proximity Sensor）、环境光传感器（Light Sensor）、陀螺仪（Gyro）、指纹模组、NFC、电源管理芯片（PMIC）、触摸屏等外设
    - 包含：
      - **8 路 AP_I²C**（其中 AP I²C0/1/7 专用于摄像头）
      - **1 路 HDMI I²C**
      - **1 路 PWR I²C**

  - **SPI（×4）**
    - 支持主/从模式
    - 用于 IMU、音频编解码器（Codec）等外设
    - 平台配置包括：
      - **1 路 QSPI**
      - **1 路 SPI LCD**
      - **2 路通用 SPI**

  - **USB（×3）**
    - **1 路 USB 2.0 OTG**
    - **1 路 USB 2.0 Host**
    - **1 路 USB 3.0**（与 PCIe PortA 复用）

  - **PCIe（×3）**
    - **PortA：Gen2 ×1**
    - **PortB：Gen2 ×2**
    - **PortC：Gen2 ×2**

  - **GMAC（×2）**
    - 支持 **10/100/1000 Mbps** 速率
    - 接口标准为 **RGMII**

  - **SDIO（×1，用于 Wi-Fi）**
    - 兼容 **4 位 SDIO 3.0 UHS-I** 协议，最高支持 **SDR104 模式（208 MHz）**

  - **SD 卡接口（×1，用于 TF 卡）**
    - 兼容 **4 位 SD 3.0 UHS-I** 协议，最高支持 **SDR104 模式（208 MHz）**

  - **eMMC（×1）**
    - 兼容 **8 位 eMMC 5.1** 标准，最高支持 **HS400 模式（200 MHz）**

  - **MIPI CSI（CSI-2 v1.1，×2）**
    - 支持多种组合模式：
      - **4-Lane + 4-Lane**
      - **4-Lane + 2-Lane**
      - **4-Lane + 2-Lane + 2-Lane**（三路图像传感器）

  - **MIPI DSI（DSI v1.1，×1）**
    - **4-Lane DSI** 接口

  - **PWM（×20）**

  - **CAN-FD（×1）**

  - **红外接收（IR-RX，×1）**

- **安全系统（Security System）**
  - 支持 **RISC-V PMP（Physical Memory Protection）** 安全机制
  - 支持 **安全启动（Secure Boot）**
  - 集成 **4 Kbit 安全 eFuse**
  - 内置 **硬件加密引擎**，支持以下算法：
    - **TRNG（真随机数发生器）**
    - **AES**
    - **RSA**
    - **ECC（椭圆曲线密码）**
    - **SHA-2**
    - **HMAC**

- **调试系统（Debug System）**
  - 提供 **两路 JTAG 接口**，分别用于 **CPU 子系统** 和 **MCU 子系统**
  - 支持通过 **UART** 进行调试输出
  - 在看门狗复位后，可自动保存 **CPU/IO 寄存器快照**

- **启动系统（Boot System）**
  - 应用处理器（AP）支持从以下介质启动：
    - **SPI NAND Flash**
    - **SPI NOR Flash**
    - **eMMC**
    - **SD 卡**
  - 内置 **128 KB Boot ROM**

- **辅助系统（Aided System）**
  - 为每个 **CPU/MCU 子系统** 独立配置 **看门狗定时器（Watchdog）**

- **工作温度范围（Operating Temperature）**
  - **-40°C ~ +85°C**，符合 **工业级标准**

### 1.3 多媒体特性

- **GPU**
  - 集成 **IMG BXE-2-32 GPU**，主频 **819 MHz**，配备 **32 KB SLC（系统级缓存）**
  - 支持图形 API：
    - **OpenCL 3.0**
    - **OpenGL ES 3.2**
    - **Vulkan 1.3**

- **VPU（视频处理单元）**
  - **解码能力**：支持 **H.265 / H.264 / VP8 / VP9 / MPEG-4 / MPEG-2**，最高达 **4K@60fps**
  - **编码能力**：支持 **H.265 / H.264 / VP8 / VP9**，最高达 **4K@30fps**
  - 支持 **1080p@60fps 同时编解码**
  - 支持 **1080p@30fps H.264/H.265 编码 + 4K@30fps H.264/H.265 解码** 并行处理

- **显示（Display）**
  - 输出接口：**1 路 MIPI DSI（4-lane）** 或 **SPI 接口**
  - 最高分辨率支持：**HD+（1920×1080@60fps）**
  - 支持最多 **4 个全尺寸图层合成**，通过 RDMA 通道的上下层复用机制可扩展至 **8 层合成**
  - 支持 **cmdlist 硬件机制**，可由硬件自动配置寄存器参数
  - 支持 **回写（Write-back）功能**，同时兼容 **原始格式（Raw）** 与 **AFBC 压缩格式**
  - 回写路径支持 **抖动（Dither）、裁剪（Crop）、旋转（Rotation）**
  - 采用 **高级 MMU（虚拟地址）机制**，在 **90°/270° 旋转** 场景下几乎无页缺失（page miss）
  - 支持 **色键（Color Key）** 与 **纯色填充（Solid Color）**
  - 面板输出支持 **高级误差扩散抖动（Error Diffusion Dither）** 和 **基于图案的抖动（Pattern-based Dither）**
  - 图像源支持 **Raw 格式** 与 **AFBC 压缩格式**
  - 支持 **色彩饱和度与对比度增强**
  - 面板支持 **视频模式（Video Mode）** 与 **命令模式（Command Mode）**
  - 支持 **DDR 频率动态切换**，内置 **DFC 缓冲区** 以保障显示流畅性
  - 集成 **HDMI 1.4** 输出接口

- **摄像头（Camera）**
  - **双 ISP 架构**
    - 最高支持 **1600 万像素 @30fps 双路 ISP 并行处理**
    - CSI 接口组合灵活：
      - **4-Lane + 4-Lane**
      - 或 **4-Lane + 2-Lane + 2-Lane**（支持三摄）
    - 支持 **RAW 格式图像传感器**，输出 **YUV 数据至 DRAM**
    - 内置 **硬件 JPEG 编码器**，最高支持 **2300 万像素**
    - 支持输出格式：**YUV / EXIF / JFIF**
    - 支持 **自动对焦（AF）、自动曝光（AE）、自动白平衡（AWB）**
    - 支持 **人脸检测**
    - 支持 **数字变焦、全景拼接（Panorama View）**
    - 支持 **相位检测自动对焦（PDAF）**
    - 支持 **画中画（PiP, Picture-in-Picture）**
    - 支持 **连续视频自动对焦**
    - 支持 **硬件加速 3D 降噪（3D Denoise）**

- **音频（Audio）**
  - **2 路全双工 I²S 接口**
  - **1 路 HDMI 音频接口**

### 1.4 架构框图

K1 的系统架构如下图所示。   
![K1 架构框图](./static/k1_blockdiagram.png)

## 2. 规格参数

### 2.1 CPU 子系统

- 采用 **双非对称 CPU 簇架构**，其中：
  - **簇 0（Cluster 0）**：包含 **4 个 SpacemiT® X60™ RISC-V 核心**，集成 **2.0 TOPS AI 算力扩展单元**
  - **簇 1（Cluster 1）**：包含 **4 个 SpacemiT® X60™ RISC-V 核心**，**不带 AI 加速能力**
- 高性能、低功耗的 **SpacemiT® X60™ CPU 核心**，符合 **RISC-V 64GCVB 指令集架构** 与 **RVA22 标准**
- 支持 **核心本地中断控制器（CLINT）** 与 **平台级中断控制器（PLIC）**
- 符合 **RISC-V Debug 规范 v0.13.2**
- 在看门狗复位触发时，可自动捕获 **关键 CPU 状态快照**，便于故障诊断与调试
- 采用 **电源岛（Power Island）设计** 与 **两级功耗管理策略**（针对每个 CPU 核心及整个簇），实现 **超低功耗运行**

#### SpacemiT® X60™ RISC-V 核心

##### 简介

X60™ 是一款创新型高能效处理器核心，集成了 进迭时空自主研发的 **道义 AI 创新部署方案**，严格遵循 **RISC-V 64GCVB 指令集架构** 与 **RVA22 标准**。

为满足当前及未来在人工智能、机器学习、SLAM（即时定位与地图构建）等场景下的计算需求，X60™ 引入了多项 **领域专用架构（DSA）技术** 与 **微架构优化**，提供强劲且高效的通用与 AI 融合计算能力。

##### Features

##### 特性

- 符合 **RISC-V 64GCVB 架构** 与 **RVA22 标准**
- 每个核心配备：
  - **32 KB L1 指令缓存（L1-I）**
  - **32 KB L1 数据缓存（L1-D）**
- 每个簇（Cluster）共享 **512 KB L2 缓存**
- **簇 0 （Cluster 0）额外集成 512 KB TCM（紧耦合存储器）**，专用于 AI 扩展加速
- 缓存一致性协议：
  - **L1 缓存支持 MESI 协议**
  - **L2 缓存支持 MOESI 协议**
- 向量扩展：**RVV 1.0**，支持 **VLEN = 256/128 位**，具备 **双发射（x2）执行宽度**
- **簇 0 （Cluster 0）实现了定制化的 AI 指令扩展**
- 支持 **CLINT（核心本地中断控制器）** 与 **PLIC（平台级中断控制器）**，共支持 **256 个中断源**
- 支持 **RISC-V 性能监控单元（PMU）**
- 支持 **SV39 虚拟内存机制**
- 支持 **32 项 PMP（物理内存保护）条目**，符合 RISC-V 安全框架
- 支持 **RISC-V 调试框架（Debug Spec v0.13.2）**
- 支持以下标准 RISC-V 扩展指令集：
  - `RV64I`
  - `M`
  - `A`
  - `F`
  - `D`
  - `C`
  - `V`
  - `Sscofpmf`
  - `Sstc`
  - `Svinval`
  - `Svnapot`
  - `Svpbmt`
  - `Zicbom`
  - `Zicbop`
  - `Zicboz`
  - `Zicntr`
  - `Zicond`
  - `Zicsr`
  - `Zifencei`
  - `Zihintpause`
  - `Zihpm`
  - `Zfh`
  - `Zfhmin`
  - `Zkt`
  - `Zba`
  - `Zbb`
  - `Zbc`
  - `Zbs`
  - `Zbkc`
  - `Zvfh`
  - `Zvfhmin`
  - `Zvkt`
- 支持以下 **AI 定制指令**：
  - **类别：<u>整型点积矩阵乘加（int8 类型）</u>**，包括：
    - `smt.vmadot`
    - `smt.vmadotu`
    - `smt.vmadotsu`
    - `smt.vmadotus`
  - **类别：<u>整型滑动窗口点积矩阵乘加（int8 类型）</u>**，包括：
    - `smt.vmadot1` / `smt.vmadot1u` / `smt.vmadot1su` / `smt.vmadot1us`
    - `smt.vmadot2` / `smt.vmadot2u` / `smt.vmadot2su` / `smt.vmadot2us`
    - `smt.vmadot3` / `smt.vmadot3u` / `smt.vmadot3su` / `smt.vmadot3us`

> **注**：有关上述所有 AI 定制指令的详细定义，请参阅官方规范文档：  
> [https://github.com/spacemit-com/riscv-ime-extension-spec](https://github.com/spacemit-com/riscv-ime-extension-spec)

##### 架构框图

X60™ 的微架构如下图所示。

![X60™ 微架构](static/X60.png)

#### 中断控制器

##### 简介

K1 集成了以下两类中断控制器，用于管理两个处理器簇的中断请求：

- **1 个处理器核心本地中断控制器（CLINT）**
- **1 个平台级中断控制器（PLIC）**

异常处理（包括异常和外部中断）是处理器的关键功能之一。当特定事件（如硬件故障、指令执行错误、用户程序系统调用请求等）发生时，处理器会跳转至相应的异常处理程序进行响应。

- **CLINT** 是一个基于内存映射的模块，主要用于处理 **软件中断** 和 **定时器中断**。
- **PLIC** 负责采集 **外部中断源**，并根据优先级进行仲裁后分发至目标处理器核心。在 PLIC 架构中，每个核心的 **机器模式（Machine Mode）** 和 **监督模式（Supervisor Mode）** 均可作为有效的中断目标。PLIC 最多支持 **256 个外部中断源**，且每个中断源均支持 **电平触发（Level-triggered）** 和 **边沿触发（Edge-triggered）** 两种格式。

#### 调试与追踪（Debug & Trace）

##### 简介

调试接口是软件与处理器交互的通道。通过该接口，用户可访问 CPU 寄存器、内存内容以及其他片上设备信息，并可执行程序下载等操作。

##### 架构框图

调试接口的微架构如下图所示：

![调试接口架构](static/debugging_interface.png)

如图所示，调试系统由以下组件构成：

- **调试软件（Debugging Software）**
- **调试代理服务（Debugging Agent Service）**
- **调试器（Debugger）**
- **调试接口（Debugging Interface）**

各组件之间的连接关系如下：

- **调试软件** 通过网络与 **调试代理服务** 通信；
- **调试代理服务** 通过 **USB** 连接至 **调试器**；
- **调试器** 通过 **JTAG 接口** 与 CPU 交互。

JTAG 内存访问支持两种模式：**`progbuf`** 和 **`sysbus`**，具体如下：

- **`progbuf` 模式**：标准 JTAG 访问方式，通过 CPU 执行指令来访问内存；
- **`sysbus` 模式**：绕过 CPU，直接通过 **系统总线访问端口（System Bus Access, SBA）** 访问片上资源，提升调试效率。

### 2.2 内存与存储

#### 片上存储器（On-Chip Memory）

##### 简介

K1 集成以下片上存储器资源：

- **128 KB Boot ROM**：用于存放一级引导代码，支持从多种外部介质启动；
- **256 KB SRAM**：由主应用处理器（Main CPU）与实时处理器（RCPU）共享使用。

### 2.2 内存与存储

#### DDR 控制器

##### 简介

DDR 控制器采用前沿架构设计，通过 **重排序缓冲区（Re-ordering Buffers, ROBs）** 对 DRAM 访问请求进行智能重排，以提升内存带宽利用率和访问效率。该设计不按原始请求顺序处理事务，而是根据地址局部性和 DRAM 物理特性优化调度顺序，同时在 AXI 接口上对相同 ID 的请求保持原有事务顺序，确保系统一致性。

此外，控制器内置 **统一写入池（Unified Write Pool）**，用于暂存写事务。该机制有效降低写入延迟，并减少因 DDR 接口频繁切换读/写操作带来的性能损失。结合 **启发式写缓冲控制** 与 **用户可编程写缓冲策略**，DDR 控制器可在运行时动态平衡读写性能。

该 DDR 控制器完全兼容 **AMBA AXI4 总线协议**，具备高度可扩展性，最多支持 **4 个 AXI 主端口**。

##### 特性

- 支持 **基于优先级的仲裁机制**，并配备 **防饥饿（Starvation Prevention）策略**
- 利用 **写缓冲合并（Write Buffer Merge）** 同一地址的多次写操作，显著降低 DDR 写流量
- 对写缓冲中的读请求可 **直接转发至 ROB**，无需访问 DDR，提升响应速度
- 支持 **两级动态调度机制**，并提供 **带宽保障（Bandwidth Guarantee）**
- 支持多种 **低功耗特性**：
  - 激活/预充电断电（Active/Pre-charge Power-off）
  - 自刷新（Self-refresh）
  - 控制方式支持：
    - **自动模式**（通过空闲计时器触发）
    - **手动模式**（通过寄存器配置）
    - **外部控制**（通过专用引脚）
- 支持 **动态频率切换（Dynamic Frequency Change）**
- 兼容 **JEDEC 标准的 LPDDR3 与 LPDDR4/LPDDR4x 存储器件**
- 支持 DRAM 容量范围：**64 MB 至 16 GB**
- 单通道 DDR PHY，**x32 位宽**，可通过软件配置为 **x32 / x16 / x8** 数据宽度
- 支持 **x16 与 x32 DRAM 芯片**（每 8 位数据对应 1 路 DQS）
- 每通道支持最多 **2 个片选（Chip Select, CS）或 Rank**
- 每个 CS 最多支持 **8 个 Bank**（适用于 LPDDRx）
- 每个 CS 可映射至 **独立的起始地址**
- 每个 CS 容量可配置为 **8 MB 至 16 GB**
- 支持 **Bank 保持开启（No Auto-Precharge）**，提升连续访问效率
- 支持 **突发长度（Burst Length）8 和 16**（依 DDR 类型而定）
- 支持 **可编程地址映射顺序**
- 支持 **CS 与数据宽度之间的灵活 Bank 布局**
- 集成 **内存控制器性能计数器（Performance Counters）**
- 支持 **RISC-V 独占加载/存储（Exclusive Load/Store）的全局监控**
- 提供 **DDR 事务的安全访问管理机制**
- 实现 **频率切换后的寄存器自动更新机制**：通过硬件触发的寄存器表，在频率变更后自动完成时序参数重配置

##### 架构框图

DDR 控制器接口架构如下图所示：

![DDR 控制器架构](static/DDR_controller.png)

#### Quad-SPI 控制器

##### 简介

Quad-SPI 控制器用于连接外部串行闪存（Serial Flash）设备，支持最多 **四条双向数据线**，实现高速、灵活的 SPI 通信。

##### 特性

- 内置 **灵活的序列引擎（Sequence Engine）**，可适配多种厂商的 Flash 器件；
- 支持 **单线（Single）、双线（Dual）和四线（Quad）** 操作模式；
- **DMA 支持**：
  - 通过 **AMBA AHB 总线（64 位宽接口）** 或 **IP 寄存器空间（32 位访问）** 读取 RX 缓冲区数据；
  - 通过 **IP 寄存器空间（32 位访问）** 填充 TX 缓冲区；
- DMA **内层循环大小可配置**；
- 支持 **15 种中断触发条件**；
- 支持对连接的 Flash 设备进行 **内存映射读取（Memory-Mapped Read Access）**，简化软件访问；
- **序列引擎可编程**，便于未来扩展新命令或协议，同时兼容所有现有厂商的指令与操作；
- 支持 **所有类型的地址模式**；
- 兼容多种 SPI 模式：
  - 标准 SPI（Standard SPI）
  - 快速读（Fast Read）
  - Dual / Dual I/O
  - Quad / Quad I/O
- 最高工作时钟频率达 **104 MHz**。

#### eMMC 接口

##### 简介

eMMC 接口是一个硬件模块，作为 eMMC 总线的主机（Host），用于在 eMMC 卡与内部总线主控之间传输数据。

##### 特性

- 符合 **8 位 eMMC 5.1 协议规范**；
- 使用与 SD-HCI 兼容的寄存器集进行 eMMC 数据传输，并扩展了厂商自定义寄存器；
- 支持 **1 位 / 8 位 MMC 卡** 以及 **CE-ATA 卡**；
- 支持 SD-HCI 规范中定义的以下数据传输方式：
  - **PIO（Programmed I/O）**
  - **SDMA（Simple DMA）**
  - **ADMA（Advanced DMA）**
  - **ADMA2**
- 支持 eMMC 卡的 **SPI 模式**；
- 支持 eMMC 5.1 定义的以下速度模式：
  - **Legacy 模式**：最高 **26 MB/s**（1.8 V 信号）
  - **High-Speed SDR**：最高 **52 MB/s**（1.8 V 信号）
  - **High-Speed DDR**：最高 **52 MB/s**（1.8 V 信号）
  - **HS200**：最高 **200 MB/s**（1.8 V 信号）
  - **HS400**：最高 **400 MB/s**（1.8 V 信号）
- 对卡总线上的所有命令与数据事务，**硬件自动生成并校验 CRC**；
- 配备 **1024 字节 FIFO**（由 2 个 512 字节数据块组成），用于数据收发缓冲。

#### SD/MMC 接口

##### 简介

SD/MMC 接口是一个硬件模块，作为 SD/MMC 总线的主机（Host），用于在 SD/MMC 卡与内部总线主控之间进行数据传输。

##### 特性

- 符合 **4 位 SD 3.0 UHS-I 协议规范**；
- 采用 **SD-HCI 寄存器集**，并扩展了厂商自定义寄存器；
- 支持 **1 位 / 4 位 SD 存储卡**；
- 支持 SD-HCI 规范中定义的以下数据传输方式：
  - **PIO（Programmed I/O）**
  - **SDMA（Simple DMA）**
  - **ADMA（Advanced DMA）**
  - **ADMA2**
- 支持 SD 3.0 规范定义的以下速度模式：
  - **Default Speed**：最高 **12.5 MB/s**（3.3 V 信号）
  - **High Speed**：最高 **25 MB/s**（3.3 V 信号）
  - **SDR12**：最高 **25 MHz**（1.8 V 信号）
  - **SDR25**：最高 **50 MHz**（1.8 V 信号）
  - **SDR50**：最高 **100 MHz**（1.8 V 信号）
  - **SDR104**：最高 **208 MHz**（1.8 V 信号）
  - **DDR50**：最高 **50 MHz**（1.8 V 信号，双倍数据速率）
- 对卡总线上的所有命令与数据事务，**硬件自动生成并校验 CRC**；
- 支持 **读等待控制（Read-Wait Control）** 功能，适用于低速或响应延迟的 SD/MMC 卡；
- 支持 **挂起/恢复（Suspend/Resume）** 功能，提升系统能效；
- 通过 **GPIO 实现 SD/MMC 卡插拔检测**；
- 配备 **1024 字节 FIFO**（由 2 个 512 字节数据块组成），用于高效的数据收发缓冲。

### 2.3 图像子系统

#### MIPI 摄像头输入接口（MIPI Camera IN Interface）

##### 简介

MIPI 摄像头输入接口包含 **两个 MIPI CSI-2 v1.1 控制器**，每个控制器均配备 **4 条数据通道（Lanes）**，每通道最高支持 **1.5 Gbps** 传输速率。

##### 特性

- 支持以下 **多摄像头 Lane 分配模式**：

  - **4-Lane + 4-Lane 模式**：支持双摄像头（双传感器）
  - **4-Lane + 2-Lane 模式**：支持双摄像头（不同带宽需求）
  - **4-Lane + 2-Lane + 2-Lane 模式**：支持三摄像头（三传感器）

  > **注**：在 **“4-Lane + 2-Lane + 2-Lane（三传感器）”** 模式下，仅支持 **2 路 Bayer RAW 格式** 和 **1 路 YUV 格式** 输入。

- 支持以下 **图像输入格式**：
  - Legacy YUV420 8-bit
  - YUV420 8-bit
  - RAW8
  - RAW10
  - RAW12
  - RAW14
  - 嵌入式数据类型（Embedded Data Type）

- 支持以下 **数据交织（Interleaving）方式**：
  - **数据类型交织（Data Type Interleaving）**
  - **虚拟通道交织（Virtual Channel Interleaving）**

#### ISP（图像信号处理器）

##### 简介

K1 集成高性能 **图像信号处理器（ISP）**，支持 **最多两路 RAW 视频流并发处理**，总处理能力达 **2100 万像素 @30fps**。

##### 特性

- 支持 **视频模式** 与 **拍照模式**
- 可处理 **RAW 格式传感器数据**，并将 **YUV 数据输出至 DRAM**
- 内置 **硬件 JPEG 编解码器**，最高支持 **2300 万像素**
- 支持输出格式：**YUV、EXIF、JFIF**
- 支持 **自动对焦（AF）、自动曝光（AE）、自动白平衡（AWB）**
- 支持 **人脸检测**
- 支持 **数字变焦** 与 **全景拼接（Panorama View）**
- 支持 **相位检测自动对焦（PDAF）**
- 支持 **画中画（PiP, Picture-in-Picture）**
- 支持 **连续视频自动对焦**
- 支持 **硬件加速 3D 降噪**
- 支持 **多层 2D YUV 降噪**
- 支持 **镜头阴影校正（Lens Shading Correction）** 后处理
- 支持 **边缘增强（Edge Enhancement）**

> **注意事项（限制说明）**：
>
> - 系统支持 **双路 RAW 摄像头视频流处理**。在 **[MIPI 摄像头输入接口](#mipi-摄像头输入接口mipi-camera-in-interface)** 章节中所述的 **“4-Lane + 2-Lane + 2-Lane（三传感器）”** 模式下，其中一路传感器必须为 **YUV 输入格式**，且该通路的写入路径 **不得使用 MMU**。
> - 在处理 **双路 RAW 摄像头视频流** 时，每通道输入图像的 **总宽度不得超过 4750 像素**，且两路传感器输出像素的 **瞬时速率之和必须小于 “ISP 时钟频率 / 6”**。
> - **视频录制** 时，无论输入分辨率如何，**输出视频最大宽度限制为 1920 像素**。
> - **拍照模式** 下，输出图像尺寸可与输入分辨率一致。

#### GPU

##### 简介

GPU 围绕多线程统一着色集群（USCs）构建，采用高效 SIMD 架构的 ALU 设计，并支持基于分块的延迟渲染（Tile-based Deferred Rendering），能够同时处理多个图块。

GPU 引擎可以处理多种不同类型的工作负载，包括：

- **3D 图形工作负载**：用于渲染 3D 场景的顶点和像素数据处理；
- **计算工作负载（GP-GPU）**：通用目的的数据处理；

> **注意**：3D 图形与计算（带有屏障）工作负载不能同时进行。

GPU 核心通过 **AXI 128 位总线** 访问 SOC 的 DDR 内存，核心频率最高可达 **819 MHz**。

##### 通用特性

- 基础架构完全符合以下 API 标准：
  - **OpenGL ES 1.1/3.2**
  - **EGL 1.5**
  - **OpenCL 3.0**
  - **Vulkan 1.3**
- **基于分块的延迟渲染架构（TBDR）** 用于 3D 图形工作负载，支持同时处理多个图块，数据处理分为两个阶段：
  - **几何处理阶段**：涉及顶点操作如变换、顶点光照以及将 3D 场景分割成图块；
  - **片段处理阶段**：涉及像素操作如光栅化、纹理映射及像素着色；
- 可编程高质量图像抗锯齿；
- 细粒度三角形剔除；
- 支持数字版权管理（DRM）安全；
- 支持 GPU 虚拟化，如下：
  - 最多支持 **8 个虚拟 GPU**；
  - IMG HyperLane 技术，提供 **8 条 HyperLanes**；
  - 每个 OSI 分离的 IRQ 支持；
- 多线程统一着色集群（USC）引擎，集成了像素着色器、顶点着色器及 GP-GPU（计算着色器）功能；
- USC 采用了具有高 SIMD 效率的 ALU 架构；
- 完全虚拟化的内存寻址（最多支持 64 GB 地址空间），支持统一内存架构；
- 细粒度的任务切换、工作负载平衡和电源管理；
- 先进的 DMA 驱动操作以最小化主机 CPU 的交互；
- 缓存类型如下：
  - **32 KB 系统级缓存（SLC）**；
  - 专用纹理缓存单元（TCU）；
- 压缩纹理解码；
- 使用 Imagination 帧缓冲压缩和解压缩（TFBC）算法实现无损或视觉上无损的低面积图像压缩；
- 专用处理器用于 B 系列核心固件执行；
- 单线程固件处理器，配备 **2 KB 指令缓存** 和 **2 KB 数据缓存**；
- 固件处理器独立的电源岛；
- 片上性能、功耗及统计寄存器。

##### 3D 图形特性

- **光栅化（Rasterization）**

  - 延迟像素着色；
  - 芯片内图块浮点深度缓冲区；
  - 具有芯片内图块模板缓冲区的 **8 位模板**；
  - 每个 ISP 最大支持 **2 个在飞图块**；
  - 每时钟周期 **16 个并行深度/模板测试**；
  - **1 条固定功能光栅化管线**；

- **纹理查找（Texture Lookups）**

  - 支持从源指令加载；
  - 通过纹理处理单元（TPU）启用纹理写入；

- **过滤（Filtering）**

  - 点采样、双线性及三线性过滤；
  - 各向异性过滤；
  - 对于立方环境映射纹理和跨面过滤的支持，包括角过滤；

- **纹理格式（Texture Formats）**

  - 支持 ASTC LDR 压缩纹理格式；
  - 对非压缩纹理和 YUV 纹理的 TFBC 无损或有损压缩格式支持；
  - ETC 格式；
  - YUV 平面支持；

- **分辨率支持（Resolution Support）**

  - 最大帧缓冲区尺寸：**8K×8K**；
  - 最大纹理尺寸：**8K×8K**；

- **抗锯齿（Anti-Aliasing）**

  - 最高支持 **4x 多重采样抗锯齿**；

- **图元装配（Primitive Assembly）**

  - 早期隐藏物体剔除；
  - 图块加速；

- **渲染至缓冲区（Render to Buffers）**

  - 扭曲格式支持；
  - 多个片上渲染目标（MRT）；
  - 无损或有损帧缓冲压缩/解压缩；
  - 可编程几何着色器支持；
  - 直接几何流输出（变换反馈）；

- **计算（Compute）**

  - 支持一维、二维和三维计算图元；
  - 块 DMA 到/自 USC 公共存储（用于局部数据）；
  - 每任务输入数据 DMA（到 USC 统一存储）；
  - 条件执行；
  - 执行围栏；
  - 计算工作负载可以与其他任何工作负载重叠；
  - 四舍五入到最近偶数。

##### 统一着色集群（USC）特性

- **2 条 ALU 流水线**  
- 每时钟周期支持 **8 个并行实例**  
- 配备 **本地数据缓存、纹理缓存和指令缓存**  
- 支持 **可变长度指令集编码**  
- 完整支持 **OpenCL™ 原子操作**  
- 采用 **标量与向量混合的 SIMD 执行模型**  
- 集成 **USC F16 累积乘加（SOPMAD）算术逻辑单元（ALU）**，用于高效半精度浮点计算

#### V2D（2D 视频加速引擎）

##### 特性

- 支持 **图像缩放**：
  - 最大 **8 倍放大（Upscaling）**
  - 最小 **1/8 倍缩小（Downscaling）**
- 支持 **旋转与翻转**：
  - 旋转角度：**0°、90°、180°、270°**
  - 支持 **镜像（Mirror）** 与 **翻转（Flip）** 操作
- 支持 **简单图层混合** 与 **背景合成**
- 支持 **图像裁剪（Cropping）**
- 支持 **纯色填充（Fetch Solid Color）**
- 支持 **色彩空间转换**，包括：
  - **RGB ↔ BT.601（窄域/全域）**
  - **RGB ↔ BT.709（窄域/全域）**
- 最大 **NV12 分辨率** 支持：
  - **4656 × 3596** 或 **4672 × 3504**
- 支持 **抖动（Dithering）**，实现更平滑的色彩过渡
- 支持 **MMU（内存管理单元）**
- 支持 **APB3** 与 **AXI3** 总线接口

- 支持以下 **输入格式**：

  - RGB888（可选 R/B 交换）
  - RGBX888（可选 R/B 交换）
  - RGBA8888（可选 R/B 交换）
  - ARGB8888（可选 R/B 交换）
  - RGB565（可选 R/B 交换）
  - RGBA5658（可选 R/B 交换）
  - ARGB8565（可选 R/B 交换）
  - A8（8 位 Alpha 图像）
  - Y8（8 位灰度图像）
  - YUV420 半平面格式（支持 UV 交换）
  - AFBC 16×16 RGBA8888（layerout0，支持 split 与 non-split 模式）
  - AFBC 16×16 NV12（layerout1，支持 split 与 non-split 模式）

- 支持以下 **输出格式**：

  - RGB888（可选 R/B 交换）
  - RGBX888（可选 R/B 交换）
  - RGBA8888（可选 R/B 交换）
  - ARGB8888（可选 R/B 交换）
  - RGB565（可选 R/B 交换）
  - RGBA5658（可选 R/B 交换）
  - ARGB8565（可选 R/B 交换）
  - A8（8 位 Alpha 图像）
  - Y8（8 位灰度图像）
  - YUV420 半平面格式（支持 UV 交换）
  - AFBC 16×16 RGBA8888（layerout0，支持 split 与 non-split 模式）
  - AFBC 16×16 NV12（layerout1，支持 split 与 non-split 模式）

##### 架构框图

V2D 子系统的微架构如下图所示：

![V2D 子系统架构](static/V2D_subsystem.png)

典型的 V2D 工作场景如下图所示：

![V2D 典型工作场景](static/V2D_work_scenario.png)

##### 功能

###### 获取数据（Fetch Data）

从源帧（src frame）中获取 16×16 块的数据，并将其映射到目标超级块（dst superblock）的过程如下图所示，其中：

- **AFBC**：获取矩形区域的左、上、宽度、高度需为 4 的倍数对齐；
- **非 AFBC**：获取矩形区域的左、上、宽度、高度需为 1 的倍数对齐；

![获取数据](static/Fetch_Data.png)

用于显示的数据获取代码如下所示，具体涉及的变量和寄存器详情紧接在表格后列出。

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

**变量详情**

| 变量名           | 位宽                    | 注释        |
|------------------|------------------------|--------------------------|
| Rect_left<br/>Rect_top | 16位无符号整数         | 范围 [0, 65535]                                                        |
| Rect_width<br/>Rect_height | 5位无符号整数          | 范围 [1, 16]                                                           |
| Rect_x<br/>Rect_y | 16位无符号整数         | 范围 [0, 65535]<br/>像素全局位置                              |
| c0, c1, c2, c3   | 8位无符号整数          | 范围 [0, 255]                                                          |
| byte_low<br/>byte_high | 8位无符号整数          | 范围 [0, 255]<br/>`byte_low`: RGB565格式中的低位字节<br/>`byte_high`: RGB565格式中的高位字节 |
| data[4][256]     | 8位无符号整数 × 4 × 256 | 范围 [0, 255]                                                          |
| index            | 8位无符号整数          | 范围 [0, 255]                                                          |

**寄存器详情**

| 寄存器名        | 注释                              |
|-----------------|------------------------------------|
| LayerX_format   | X 可以是 0 或 1，参见模块寄存器说明 |
| LayerX_swap     | X 可以是 0 或 1，参见模块寄存器说明 |

###### 纯色填充（Solid Color）

用于在特定矩形区域内应用纯色的代码如下所示，具体涉及的变量和寄存器详情紧接在表格后列出。

> **注意：**
>
> - 如果启用了寄存器 `LayerX_solid`，获取的数据将被设置为固定的 R、G、B、A 值。
> - 获取矩形和纯色矩形的坐标在旋转后会更新。

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

**变量定义**

| 变量名                  | 位宽               | 说明                                     |
|------------------------|--------------------|------------------------------------------|
| Rect_left, Rect_top    | 16 位无符号整数     | 范围 [0, 65535]                          |
| Rect_width, Rect_height| 5 位无符号整数      | 范围 [1, 16]                             |
| Rect_x, Rect_y         | 16 位无符号整数     | 范围 [0, 65535]<br/>像素的全局坐标位置   |
| c0, c1, c2, c3         | 8 位无符号整数      | 范围 [0, 255]                            |
| data[4][256]           | 8 位无符号 × 4 × 256| 范围 [0, 255]                            |
| index                  | 8 位无符号整数      | 范围 [0, 255]                            |

**寄存器定义**

| 寄存器名               | 说明                                      |
|------------------------|-------------------------------------------|
| LayerX_solid_enable    | X 为 0 或 1，具体定义参见模块寄存器文档   |
| LayerX_solid_R         | X 为 0 或 1，表示图层 X 的纯色红色分量    |
| LayerX_solid_G         | X 为 0 或 1，表示图层 X 的纯色绿色分量    |
| LayerX_solid_B         | X 为 0 或 1，表示图层 X 的纯色蓝色分量    |
| LayerX_solid_A         | X 为 0 或 1，表示图层 X 的纯色 Alpha 分量 |

##### 旋转（Rotation）

支持 **0°、90°、180°、270°**（顺时针方向）的图像旋转，以及 **镜像（Mirror）** 和 **翻转（Flip）** 操作，如下图所示（示例）：

![旋转示意图](static/Rotation.png)

用于执行图形内容旋转、镜像和翻转的代码逻辑如下所示，具体涉及的变量与寄存器定义紧随其后。

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

**变量定义**

| 变量名                              | 位宽               | 说明                                     |
|-------------------------------------|--------------------|------------------------------------------|
| Rect_left, Rect_top                | 16 位无符号整数     | 源矩形区域左上角坐标，范围 [0, 65535]    |
| Rect_width, Rect_height            | 5 位无符号整数      | 源矩形区域尺寸，范围 [1, 16]             |
| Block_rect_left, Block_rect_top    | 16 位无符号整数     | 块矩形区域左上角坐标，范围 [0, 65535]    |
| Block_rect_width, Block_rect_height| 5 位无符号整数      | 块矩形区域尺寸，范围 [1, 16]             |
| data_in[4][256],<br/>data_out[4][256] | 8 位无符号 × 4 × 256 | 输入和输出像素数据缓存（RGBA），范围 [0, 255] |

**寄存器定义**

| 寄存器名                    | 位宽               | 说明                                      |
|-----------------------------|--------------------|-------------------------------------------|
| LayerX_degree               | 3 位无符号整数      | X 是 0 或 1，用于指定图层 X 的旋转角度：<br> - 000 = 0°<br> - 001 = 90°<br> - 010 = 180°<br> - 011 = 270°<br>具体定义参见模块寄存器文档 |
| LayerX_width, LayerX_height | 16 位无符号整数     | X 是 0 或 1，分别表示图层 X 的宽度和高度，具体定义参见模块寄存器文档 |

###### 色彩空间转换（CSC）

支持以下格式的 **色彩空间转换（Color Space Conversion, CSC）**：

- **BT.601 与 BT.709**：支持窄域（Narrow Range）与全域（Full Range）之间的相互转换；
- **RGB ↔ YUV**：支持 RGB 到 YUV 及 YUV 到 RGB 的双向转换。

转换过程通过一个 **3×3 变换矩阵** 对输入通道进行线性变换，并对结果进行 **限幅（Clamping）**，以确保输出值始终处于有效范围 **[0, 255]** 内。

为此，系统实现如下公式，具体涉及的变量与寄存器定义紧随其后。

**第一步：计算中间通道值**

$$
C0_{inter} = (Layer_matrix[0][0]*C0_{in} + Layer_matrix[0][1]*C1_{in} + Layer_matrix[0][2]*C2_{in} + 512)>>(10+Layer_matrix[0][3])
$$

$$
C1_{inter} = (Layer_matrix[1][0]*C0_{in} + Layer_matrix[1][1]*C1_{in} + Layer_matrix[1][2]*C2_{in} + 512)>>(10+Layer_matrix[1][3])
$$

$$
C2_{inter} = (Layer_matrix[2][0]*C0_{in} + Layer_matrix[2][1]*C1_{in} + Layer_matrix[2][2]*C2_{in} + 512)>>(10+Layer_matrix[2][3])
$$

**第二步：限幅处理以确保合法输出**

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

**变量定义**

| 变量名                          | 位宽             | 说明                     |
|----------------------------------|------------------|--------------------------|
| C0in, C1in, C2in, C3in          | 8 位无符号整数    | 输入通道（如 R/G/B/A 或 Y/U/V/A） |
| C0inter, C1inter, C2inter       | 10 位有符号整数   | 中间通道值               |
| C0out, C1out, C2out, C3out      | 8 位无符号整数    | 输出通道                 |

**寄存器定义**

| 寄存器名              | 索引     | 位宽           | 说明                                      |
|-----------------------|----------|----------------|-------------------------------------------|
| LayerX_CSC_enable     | —        | 1 位无符号整数  | 0：禁用 CSC<br/>1：启用 CSC               |
| Layer_matrix[#][#]    | 0–11     | 13 位有符号整数 | 共 12 个系数（3×4），取值范围 [-4096, 4095] |

在代码中，CSC 功能按以下条件执行：

```
if LayerX_CSC_enable == 0
    skip CSC function
```

###### 缩放（Scaling）

缩放操作采用基于超级块（superblock）的系统化处理方式，具体流程如下：

- 首先按 **水平方向** 输出前四个超级块，随后按 **垂直方向** 继续输出；
- 当 **垂直方向输出完成** 后，处理流程将重新从 **第一行超级块** 开始。

###### 存储（Storing）

一个 16×16 的图像块可被写入 DDR 内存，但**仅位于输出裁剪区域（output crop region）内的部分会被实际存储**。该部分数据在存储前会转换为指定的输出色彩格式（如 YUV、RGB 等）。

用于存储图像块的代码逻辑如下所示，具体涉及的变量与寄存器定义紧随其后。

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

**变量定义**

| 变量名        | 位宽               | 说明         |
|----------------|--------------------|------------|
| Rect_left<br/>Rect_top                     | 16 位无符号整数     | 范围 [0, 65535]                          |
| Rect_width<br/>Rect_height                 | 5 位无符号整数      | 范围 [1, 16]                             |
| pixel_index                                | 8 位无符号整数      | 范围 [0, 65535]（注：实际有效范围受 16×16 块限制） |
| s0, s1, s2, s3                             | 8 位无符号整数      | 范围 [0, 255]，通常用于中间或通道数据    |
| Y00, Y01, Y10, Y11,<br/>U00, U01, U10, U11,<br/>V00, V01, V10, V11,<br/>U, V, R, G, B, A | 8 位无符号整数 | 范围 [0, 255]，表示像素的色彩分量（YUV/RGB/Alpha） |
| data_in[4][256]                            | 8 位无符号 × 4 × 256 | 输入像素数据缓存（RGBA 或其他四通道格式），范围 [0, 255] |

**寄存器定义**

| 寄存器名           | 位宽             | 说明                |
|--------------------|------------------|--------------------|
| Output_format      | 3 位无符号整数    | 指定输出色彩格式：<br/>• 0: RGB888（低地址为 R，高地址为 B）<br/>• 1: RGBX8888<br/>• 2: RGBA8888<br/>• 3: ARGB8888（低地址为 A，高地址为 B）<br/>• 5: YUV420 半平面格式（UV 交错，低地址为 U，高地址为 V） |
| Output_swap        | 1 位无符号整数    | 通道交换控制：<br/>• 0: 不交换<br/>• 1: RGB 模式下交换 R/B；YUV 模式下交换 U/V |
| Output_layout      | 1 位无符号整数    | 存储布局：<br/>• 0: 线性（Linear）<br/>• 1: FBC 压缩格式（Frame Buffer Compression） |
| Output_crop_left   | 16 位无符号整数   | 裁剪区域左边界，范围 [0, 65534]；需满足 `crop_left < output_left + output_width` |
| Output_crop_top    | 16 位无符号整数   | 裁剪区域上边界，范围 [0, 65534]；需满足 `crop_top < output_top + output_height` |
| Output_crop_width  | 16 位无符号整数   | 裁剪区域宽度，范围 [1, 65535]；需满足 `crop_left + crop_width ≤ output_left + output_width` |
| Output_crop_height | 16 位无符号整数   | 裁剪区域高度，范围 [1, 65535]；需满足 `crop_top + crop_height ≤ output_top + output_height` |

### 2.4 视频子系统

#### 概述

视频处理单元（Video Processing Unit, VPU）是一个配备双核的视频加速引擎，专为多种视频标准的**解码与编码**而设计。VPU 内置一个主机 CPU，用于运行固件以控制硬件引擎的各项功能，包括**码流解析**、**视频硬件子模块控制**以及**错误恢复机制**等。

VPU 最高可运行在 **819 MHz** 的时钟频率下，支持广泛的视频编解码标准，包括：**H.265（HEVC）**、**H.264（AVC）**、**VP8**、**VP9**、**MPEG-4**、**MPEG-2** 和 **H.263**。

VPU 支持以下并发工作模式：

- **1080p@60fps 的同时编码与解码**
- **H.264/H.265 编码 @1080p@30fps** 与 **H.264/H.265 解码 @4K@30fps** 同时进行

视频编解码核心模块通过**全硬件逻辑（hardwired logic）** 实现各标准的具体编解码操作。其中，**宏块序列器（Macroblock Sequencer）** 作为主控制器，负责调度各子模块的处理流程，旨在**降低处理器负载**并**简化固件复杂度**。

如前所述，多个与具体标准无关的通用功能模块在运行时共享公共逻辑，以确保整体处理效率和性能的流畅性。

#### 视频编码器（Video Encoder）

##### 编码特性

- 支持可配置的 **ARM 帧缓冲压缩（AFBC）1.0 或 1.2** 作为输入格式；
- 支持 **YUV422 和 YUV420** 格式的 AFBC **16×16 块拆分（block split）**；
- 支持 **跨距（stride）** 配置（**不适用于 AFBC 输入格式**）；
- 支持 **水平与垂直镜像**（**不适用于 AFBC 输入格式**）；
- 支持在编码前对源帧进行 **90 度步进的旋转**（**不适用于 AFBC 输入格式**）：

  > **注意**：若 YUV422 输入被旋转 90° 或 270°，且未转换为 YUV420，则输出将自动转换为 **YUV440** 格式。

- 支持以下源帧输入格式的编码：

  - **单平面 YUV422**，逐行扫描格式，色度分量交错排列，顺序为 **YUYV** 或 **UYVY**  
    > **注意**：YUV422 输入可选转换为 YUV420 进行编码。

  - **单平面 RGB（8 位）**，按字节地址顺序排列，支持 **RGBA、BGRA、ARGB 或 ABGR**；

  - **双平面 YUV420**，逐行扫描格式，色度分量交错排列，顺序为 **UV** 或 **VU**；

  - **三平面 YUV420**，逐行扫描格式  
    > **注意**：三平面格式**仅用于测试目的**，**不推荐用于追求最佳性能的场景**。

  - **AFBC YUV422**

  - **AFBC YUV420**

##### 支持的编码格式

- **HEVC（H.265）Main** 档案
- **H.264 Baseline Profile（BP）** 基础档
- **H.264 Main Profile（MP）** 主档
- **H.264 High Profile（HP）** 高级档
- **VP8**
- **VP9 Profile 0** 档案 0

###### HEVC（H.265）编码特性

- 编码输出的码流符合 **HEVC（H.265）Main Profile** 规范；
- 支持 **1080p@60fps** 编码性能（双核运行，频率约 300 MHz）；
- 单核在 300 MHz 下可支持最高 **50 Mbps** 码率；
- 最大帧宽与帧高：**4096 像素**；
- 支持 **8 位** 编码，包含 **I 帧、P 帧和 B 帧**；
- 仅支持 **逐行扫描（Progressive）** 编码，最大 **CTU（Coding Tree Unit）尺寸为 64×64**；
- 支持 **平铺模式（Tiled Mode）**，最多 **4 个水平方向切片（仅支持水平分割）**；
- 支持 **波前并行处理（Wavefront Parallel Processing, WPP）**；
- 运动估计（ME）搜索窗口范围：
  - 水平方向：±128 像素  
  - 垂直方向：±64 像素；
- ME 搜索精度可达 **四分之一像素（QPEL, Quarter-Pixel）**；
- 亮度（Luma）帧内预测块尺寸：**8×8、16×16、32×32**；
- 色度（Chroma）帧内预测块尺寸：**4×4、8×8、16×16**；
- 帧间预测（Inter-mode）块尺寸：**8×8、16×16、32×32**；
- 亮度变换块尺寸：**8×8、16×16、32×32**；
- 色度变换块尺寸：**4×4、8×8、16×16**；
- 支持 **跳过 CU（Skipped CUs）** 与 **Merge 模式**；
- 支持 **去块滤波（Deblocking Filter）**；
- 支持 **样本自适应偏移（Sample Adaptive Offset, SAO）**；
- 可选启用 **受限帧内预测（Constrained Intra Prediction）**；
- 支持 **固定量化参数（Fixed QP）** 或 **基于码率控制的动态 QP** 操作；
  - 码率控制采用基于 **漏桶模型（Leaky Bucket Model）**，依据设定的码率与缓冲区大小进行调节；
- 支持 **长期参考帧（Long Term Reference Frames）**；
- 可配置 **帧内刷新间隔（Intra-frame Refresh Interval）**；
- 支持以 **CTU 行粒度** 插入切片（Slice）；
- 可配置运动估计的 **搜索窗口范围** 与 **分割选项上限**；
- **注意**：编码器 **不会阻止单个 CTU 输出比特数超过标准规定的最大值**。

###### H.264 编码特性

- 编码输出的码流符合 **H.264 Baseline、Main 和 High Profile** 规范；
- 支持 **1080p@60fps** 编码性能（双核运行，频率约 300 MHz）；
- 单核在 300 MHz 下可支持最高 **50 Mbps** 码率；
- 最大帧宽与帧高：**4096 像素**；
- 支持 **I 帧、P 帧和 B 帧**；
- 仅支持 **逐行扫描（Progressive）** 编码；
- 支持两种熵编码方式：
  - **CABAC**（Context Adaptive Binary Arithmetic Coding）
  - **CAVLC**（Context Adaptive Variable Length Coding）  
  > **注意**：使用 CAVLC 时 **不支持 B 帧**。

- 运动估计（ME）搜索窗口范围：
  - 水平方向：±128 像素  
  - 垂直方向：±64 像素；
- ME 搜索精度可达 **四分之一像素（QPEL, Quarter-Pixel）**；
- 亮度（Luma）帧内预测块尺寸：**4×4、8×8、16×16**；
- 色度（Chroma）帧内预测块尺寸：**8×8**；
- 帧间预测（Inter-mode）块尺寸：**8×8、16×16**；
- 变换块尺寸：**4×4 和 8×8**；
- 支持 **跳过宏块（Skipped Macroblocks）**；
- 支持 **去块滤波（Deblocking Filter）**；
- 可选启用 **受限帧内预测（Constrained Intra Prediction）**；
- 支持 **固定量化参数（Fixed QP）** 或 **基于码率控制的动态 QP** 操作；
  - 码率控制采用基于 **漏桶模型（Leaky Bucket Model）**，依据设定的码率与缓冲区大小进行调节；
- 支持 **长期参考帧（Long Term Reference Frames）**；
- 可配置 **帧内刷新间隔（Intra-frame Refresh Interval）**；
- 切片（Slice）插入粒度为 **每 32 像素高的行**；
- 可限制运动估计的 **搜索窗口范围** 与 **宏块分割选项**；
- **始终启用转义机制（Escape Option）**，以防止在任何 NAL 单元包格式下出现 **NAL 起始码（Start Code）的误匹配（Emulation Prevention）**。

> **注**：
> - 更多细节请参阅 ITU-T H.264 附录 B：[VC-1 Compressed Video Bitstream Format and Decoding Process](https://multimedia.cx/mirror/VC-1_Compressed_Video_Bitstream_Format_and_Decoding_Process.pdf)  
> - 编码器 **不会阻止单个宏块输出比特数超过标准规定的最大值**，需由上层应用确保合规性。

###### VP8 编码特性

- 支持 **1080p@60fps** 编码性能（双核运行，频率约 400 MHz）；
- 单核在 400 MHz 下可支持最高 **50 Mbps** 码率；
- 最大帧宽与帧高：**2048 像素**；
- 支持 **I 帧和 P 帧**；
- 仅支持 **逐行扫描（Progressive）** 编码；
- 运动估计（ME）搜索窗口范围：
  - 水平方向：±128 像素  
  - 垂直方向：±64 像素；
- ME 搜索精度可达 **四分之一像素（QPEL, Quarter-Pixel）**；
- 亮度（Luma）帧内预测块尺寸：**4×4、8×8、16×16**；
- 色度（Chroma）帧内预测块尺寸：**8×8**；
- 帧间预测（Inter-mode）块尺寸：**8×8、16×16**；
- 支持 **跳过宏块（Macroblock Skipping）**；
- 支持 **去块滤波（Deblocking Filter）**；
- 支持 **固定量化参数（Fixed QP）** 或 **基于码率控制的动态 QP** 操作；
  - 码率控制采用基于 **漏桶模型（Leaky Bucket Model）**，依据设定的码率与缓冲区大小进行调节；
- 可配置 **帧内刷新间隔（Intra-frame Refresh Interval）**；
- 可限制运动估计的 **搜索窗口范围** 与 **宏块分割选项**。

###### VP9 编码特性

- 编码输出的码流符合 **VP9 Profile 0** 规范，支持 **8 位色深**；
- 支持 **1080p@60fps** 编码性能（双核运行，频率约 300 MHz）；
- 单核在 300 MHz 下可支持最高 **50 Mbps** 码率；
- 最大帧宽与帧高：**4096 像素**；
- 仅支持 **8 位样本精度**；
- 支持 **I 帧和 P 帧**；
- 仅支持 **逐行扫描（Progressive）** 编码；
- 支持 **平铺行与列（Tiled Rows and Columns）**，提升并行处理能力；
- 运动估计（ME）搜索窗口范围：
  - 水平方向：±128 像素  
  - 垂直方向：±64 像素；
- ME 搜索精度可达 **四分之一像素（QPEL, Quarter-Picture Element）**；
- 亮度（Luma）帧内预测块尺寸：**8×8、16×16、32×32**；
- 色度（Chroma）帧内预测块尺寸：**4×4、8×8、16×16**；
- 帧间预测（Inter-mode）块尺寸：**8×8、16×16、32×32**；
- 亮度变换块尺寸：**8×8、16×16、32×32**；
- 色度变换块尺寸：**4×4、8×8、16×16**；
- 支持 **超级块跳过（Superblock Skipping）**；
- 支持 **去块滤波（Deblocking Filter）**；
- 支持 **固定量化参数（Fixed QP）** 或 **基于码率控制的动态 QP** 操作；
  - 码率控制采用基于 **漏桶模型（Leaky Bucket Model）**，依据设定的码率与缓冲区大小进行调节；
- 可配置 **帧内刷新间隔（Intra-frame Refresh Interval）**；
- 支持使用延迟上下文（delayed contexts）进行 **隐式或显式概率更新（Implicit or Explicit Probability Update）**。

#### 视频解码器（Video Decoder）

##### 解码特性

- 支持以下源帧输出格式：
  - **双平面 YUV420** 逐行扫描格式：色度分量交错排列，顺序为 **UV 或 VU**；
  - **三平面 YUV420** 逐行扫描格式  
    > **注意**：
    > - 三平面格式的支持仅用于测试目的，不建议在追求高性能的应用中使用；
    > - 确保 YUV 缓冲区的正确对齐和跨距（stride）设置以获得最佳性能。

- 支持 **YUV420 AFBC 格式**，8 位色彩深度；
- 可配置输出为 **AFBC 1.0 或 AFBC 1.2** 标准；
- 仅对逐行扫描格式支持 **跨距（stride）** 配置；
- 在输出前支持对解码帧进行 **90 度步进的旋转**：

  > **注意**：该功能不适用于 AFBC 输出格式。

- 支持输出每个显示帧中每 **32×32 像素块** 的平均亮度（亮度值）和色度（颜色值）。

##### 支持的解码格式

- **HEVC（H.265）**：Main Profile  
- **H.264**：Baseline Profile、Main Profile、High Profile  
- **VP8**  
- **VP9**：Profile 0  
- **VC-1**：Simple Profile（SP）、Main Profile（MP）、Advanced Profile（AP）  
- **MPEG-4**：Simple Profile（SP）、Advanced Simple Profile（ASP）  
- **MPEG-2**：Main Profile（MP）  
- **H.263**：Profile 0

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

> **Note.**Definition of symbols used for signal/pin type:
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
