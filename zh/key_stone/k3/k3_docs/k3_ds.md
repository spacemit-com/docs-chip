---
sidebar_position: 2
---

# K3 数据手册

## PDF 版本下载

点击下载 [K3 数据手册（PDF）](https://cdn-resource.spacemit.com/file/chip/K3/k3_datasheet_zh.pdf)

## 修订记录

| 版本号 | 日期 | 修订说明 |
| --- | --- | --- |
| **V1.7** | 2026.08.19 | 新增第 4.4 节引脚分配表交叉引用 |
| **V1.6** | 2026.07.15 | 更新视频子系统参数 |
| **V1.5** | 2026.07.01 | 更新 A100 特性描述 |
| **V1.4** | 2026.06.10 | 增添 Part Number 描述 |
| **V1.3** | 2026.05.21 | 更新 A100 中断描述 |
| **V1.2** | 2026.05.19 | 更新视频子系统参数 |
| **V1.1** | 2026.05.08 | 更新图像子系统特性 |
| **V1.0** | 2026.04.30 | 首版 |

---

## 1. 概述

### 1.1 产品简介

SpacemiT Key Stone K3 系列芯片采用 RISC-V 同构融合计算技术，集成进迭时空的 8 个高性能计算大核 X100 及 8 个超宽并行计算 AI 核 A100，可提供 130 KDMIPS 通用算力及 60TOPS 通用 AI 算力，可流畅运行 300 亿参数模型。
K3 系列芯片主要应用在 AI 消费硬件如 AI 智慧家居、AI 会议办公、AI 内容创作、AI 电商零售等领域。

### 1.2 主要特性

**处理器子系统**  

- 8 个 X100™ 64 位 RISC-V 核心（四发射、乱序执行）  
- 总 CPU 性能：130 KDMIPS  
- SpecINT2006 > 9.0 /GHz；最高主频 2.4 GHz  
- 每 8 核共享 8MB L2 缓存

**AI 计算子系统**

- 8 核 A100™ 提供 60TOPS AI 算力  
- 支持最高 300 亿参数模型推理（>10 tokens/s @ 30B）  
- 兼容 RVV 1.0、RVA23 及 Vector Crypto 标准  
- 遵循 CPU 编程范式，实现零成本AI算法的部署

**内存子系统**  

- 64 位 LPDDR5（6400 Mbps）/ LPDDR4x（4266 Mbps）  
- 最大支持 32GB 内存容量，带宽可达 51GB/s

**实时处理子系统**  

- 双核 RT24™ 64 位 RISC-V 处理器  
- 六级单发按序流水线

**虚拟化与安全**  

- 支持 RVH 1.0、AIA 和 IOMMU 扩展，提供CPU、内存、中断、IO的完整硬件虚拟化能力  
- 硬件级防护机制，抵御 Spectre、Meltdown 等推测执行攻击  
- 支持 RISC-V PMP、ePMP 和 IOPMP 安全框架  
- 安全启动、安全存储与签名验证  
- 加密算法支持：AES、SHA、RSA、SM2、SM3、SM4  
- 支持产品生命周期安全管理

**存储接口**  

- SPI Flash、eMMC 5.1、UFS 2.2、SDIO 3.0、PCIe NVMe  

**多媒体与显示**

- 集成 3D 图形引擎，支持 Vulkan、OpenCL、OpenGL ES  
- 支持 4K@180fps 视频解码与 4K@90fps 视频编码（兼容 H.265、H.264、VP8 及 VP9 编解码格式）
- 通过 MIPI-DSI（8 通道，4.5 Gbps/通道）和 DP/eDP 接口，可实现双路 3840×2160@60fps 显示输出。  
- 4 个 MIPI-CSI 接口（共 12 条通道），最多支持 12 路摄像头输入。

**IO 扩展接口**  

- 8 条 PCIe Gen3 通道（8 Gbps/通道），支持 RC/EP 模式及热插拔  
- 3 × USB 3.0 Host，1 × USB 3.0 DRD（Type-C），1 × USB 2.0 Host  
- 4 × GMAC（支持 RGMII/RMII/MII），集成 TSN 协议  
- 6 × SPI，2 × eSPI，17 × UART，10 × CAN，9 × I²C，30 × PWM

**功耗**  

- TDP: 15–25 W  

**环境与可靠性**  

- 工作温度范围：–40 °C 至 +85 °C（工业级）

## 1.3 架构框图

<img src="static/k3_block_diagram.png" alt="K3 Block Diagram" width="800">

## 2. 规格参数

### 2.1 CPU 子系统

#### 2.1.1 SpacemiT® X100™ RISC-V 核

**简介**  
SpacemiT® X100™ 是一款高性能、四发射、乱序执行的多核多簇 RISC-V 处理器，符合 RVA23 指令集架构规范，专为服务器、自动驾驶系统及云端 AI 推理平台等高负载计算场景优化设计。  
X100 在追求极致性能的同时，具备完善的虚拟化能力、强大的安全韧性以及 RAS（可靠性、可用性、可服务性）特性，是面向数据密集型与任务关键型应用的可扩展高性能解决方案。

**特性**
- 合规性：完全符合 RISC-V RVA23 标准  
- 缓存架构：  
  - 每核心配备 64 KB L1 指令缓存（I-Cache）和 64 KB L1 数据缓存（D-Cache）  
  - 每簇共享 4 MB L2 缓存  
  - L1 D-Cache 支持 MESI 一致性协议  
  - L2 Cache 支持 MOESI 一致性协议  
- 向量扩展：RVV 1.0，VLEN = 256  
- 虚拟化扩展：RVH 1.0，GEILEN = 8  
- 高级中断架构（AIA）：  
  - M 模式 MSI：512
  - S 模式 MSI：512
  - VS 模式 MSI：64
- 中断控制器：支持 ACLINT 与 APLIC，共支持 512 个中断源  
- 性能监控：RISC-V性能监控单元（PMU）支持  
- 虚拟内存：支持 SV39 虚拟内存管理  
- 安全框架：  
  - 符合 RISC-V 安全规范，提供 16 项 PMP（物理内存保护）条目  
  - 支持 RISC-V 调试（Debug）、追踪（Trace）及 RERI（运行时错误报告与恢复）框架  
- RVA23 可选扩展（未包含在 RVA23 基础规范中）：  
  - 向量加密扩展：`zvkng`, `zvksg`  
  - 其他扩展：`zvbc`, `zfh`, `zbc`, `zvfh`, `zfbmin`, `zvfbfmin`, `zvfbfwma`  
  - 系统与安全扩展：`sdtri`, `svvptc`, `sspm`, `smepmp`, `smstateen`, `smcntrpmf`

**架构框图**  

<img src="static/x100_block_diagram.png" alt="" width="600">

#### 2.1.2 SpacemiT® A100™ AI 核

**简介**  
SpacemiT® A100™ 是一款以 AI 为中心的 RISC-V AI处理器，通过自研的 SpacemiT-IME 指令集提供原生的AI计算能力。其微架构针对算子级并行性、内存带宽效率和数据局部性进行了深度优化，可高效执行各类真实场景下的 AI 工作负载。  
除强大的 AI 加速能力外，A100 完整支持 RVA23* 规范定义的通用 CPU 功能，并采用标准 RISC-V 统一编程模型，为本地语言模型（SLM）及广泛的 AI 原生应用提供强大算力支撑。

**特性**  
- AI 计算性能：60 TOPS（@INT4 sparse）  
- RISC-V 合规性：完全符合 RISC-V RVA23* 标准  
- 缓存架构：  
  - 每核心配备 32 KB L1 指令缓存（I-Cache）和 32 KB L1 数据缓存（D-Cache）  
  - 每簇共享 1 MB L2 缓存  
  - 每簇配备 1.5 MB 片上暂存存储器（Scratchpad）  
  - L1 D-Cache 支持 MESI 一致性协议  
  - L2 Cache 支持 MOESI 一致性协议  
- 向量扩展：RVV 1.0，VLEN = 1024  
- 中断控制器：符合 AIA 标准的 ACLINT 和 APLIC 中断控制器
- MSI 中断数量：
  - M 模式：511
  - S 模式：511
  - VS 模式：7 个 VS 中断文件，每个中断文件支持 63 个 MSI 中断  
- 性能监控：集成 RISC-V 性能监控单元（PMU）  
- 虚拟内存：支持SV39虚拟内存管理  
- 安全框架：  
  - 符合 RISC-V 安全规范，提供 32 项 PMP（物理内存保护）条目  
  - 支持 RISC-V 调试（Debug）与追踪（Trace）功能  
- RVA23* 可选扩展（未包含在 RVA23 基础规范中）：  
  - 向量加密扩展：`zvkng`, `zvksg`  
  - 其他扩展：`zvbc`, `zfh`, `zbc`, `zvfh`, `zfbmin`, `zvfbfmin`, `zvfbfwma`  
  - 系统与安全扩展：`sdtri`, `svvptc`, `sspm`, `smepmp`, `smstateen`, `smcntrpmf`

> **注意**：A100 AI 核心中的 RVA23* 不包含 Hypervisor 虚拟化扩展。

**架构框图**

<img src="static/a100_block_diagram.png" alt="" width="400">

#### 2.1.3 RT24 RISC-V 核

**简介**  
RT24 作为 K3 SoC 中的系统管理核心，基于 OpenHW Group 开源的 64 位 RISC-V 处理器 CVA6 构建，采用六级顺序单发射流水线架构，支持 RV64GC 指令集，并兼容类 Unix 操作系统。该核心专为高能效与高可靠性设计，负责全芯片的控制协调、电源管理及低功耗任务调度等关键功能。

**特性**  
- 超低待机与运行功耗  
- 实现 RV64IMAFDC（即 RV64GC）指令集  
- 支持 RISC-V 三级特权模式：M（机器态）、S（监管态）、U（用户态）  
- 通过 ITLB、DTLB 和 PTW 单元实现虚拟地址转换  

**架构框图**  

<img src="static/rt24_block_diagram.png" alt="" width="600">

#### 2.1.4 调试子系统（Debug）

**简介**  
调试接口是软件与处理器进行交互的关键通道。通过该接口，用户可访问 CPU 寄存器、内存内容以及其他片上设备信息此外。还可以通过调试接口执行程序下载等任务。

**架构框图**  
调试接口的微架构如下图所示：

<img src="static/debug_block_diagram.png" alt="" width="600">

如图所示，调试系统由以下组件构成：  

- 调试软件（例如 GDB）  
- 调试代理服务（例如 OpenOCD）  
- 调试器（例如 JTAG 调试探针）  
- 调试接口（例如 Debug Transport Module, DTM）

各组件之间的连接关系如下：  

- 调试软件通常通过网络与调试代理服务通信  
- 调试代理服务一般通过 USB 与调试器连接  
- 调试器通过 JTAG 接口与 CPU 交互  

JTAG 内存访问支持两种模式：progbuf 和 sysbus：  

- progbuf 模式：标准 JTAG 访问方式，通过 CPU 执行指令缓冲区（program buffer）来访问内存  
- sysbus 模式：绕过 CPU，直接通过系统总线访问（System Bus Access, SBA）端口读写片上资源  

#### 2.1.5 追踪子系统（Trace）

**简介**  
RISC-V 追踪系统提供了一套硬件与软件协同的接口，用于调试和分析单个硬件线程（hart）的执行轨迹，包括其内存访问的详细信息。  
当 RISC-V hart 通过 RISC-V 追踪规范定义的入口端口（ingress port）输出程序执行流与内存访问轨迹时，片上追踪编码器会对数据进行压缩，以实现高效传输。  
压缩后的追踪数据可暂存于片上存储中，随后由主机端的解码软件重建完整的执行流程，使开发者能够精确观测 hart 的运行时行为。

**特性**  
K3 中 X100 与 A100 核心的追踪组件完全符合 RISC-V N-Trace 协议，并支持其配套接口——RISC-V 追踪控制接口（Trace Control Interface）与 RISC-V Hart-to-Trace 接口。关键特性包括：

- 每个 X100 核 / A100 核 配备独立的追踪编码器  
- 集成 ATB（AMBA Trace Bus）桥接模块，用于连接至 ATB 总线  
- 支持 BTM（Branch Trace Mode）分支轨迹压缩  
- 可选消息类型（如所有权消息），提升在复杂操作系统环境下的追踪处理能力  
- 通过调试触发器（debug triggers）实现精准的追踪启停控制  
- 扩展压缩能力，例如虚拟地址压缩，进一步提升追踪效率  

**架构框图**
<img src="static/trace_block_diagram.png" alt="" width="600">

### 2.2 内存与存储

#### 2.2.1 片上存储（On-Chip Memory）

**简介**  
K3 集成了以下片上存储资源：
- 128 KB Boot ROM：用于存放一级引导代码，支持从多种外部介质启动，并支持通过 USB 与 UART 下载程序；支持基于 eFuse 的安全启动。
- 512 KB SRAM：由主 CPU 与 RCPU 共享使用。  

#### 2.2.2 LPDDR4x/5

**简介**  
动态内存接口为外部 LPDDR4x 和 LPDDR5 DRAM 提供高性能、低功耗的连接，支持灵活配置与动态频率调节，可在不同应用场景下平衡带宽与能效。

**特性**
- 支持 LPDDR4x 与 LPDDR5 内存类型：  
  - LPDDR4x 最高数据速率：4266 MT/s  
  - LPDDR5 最高数据速率：6400 MT/s  
- 最大寻址空间：32 GB  
- 双通道架构，每通道 32 位数据宽度  
- 每通道支持两个 Rank  
- 支持动态频率调节（DFS），可根据带宽需求实时调整频率以优化功耗  

#### 2.2.3 Quad-SPI

**简介**  
Quad-SPI 接口用于 SoC 与外部串行 Flash 存储器之间的通信，支持最多四条双向数据线传输，具备高灵活性并兼容多种 Flash 器件。

**特性**  
- 支持 XIP（Execute-In-Place）模式与 Page 模式  
- 数据线宽度可独立配置为 1/2/4 线  
- 时钟频率范围：13.25 MHz 至 102 MHz  
- 支持 SPI NOR Flash 与 SPI NAND Flash  
- 支持 1.8 V 与 3.3 V 信号电平  

#### 2.2.4 eMMC 接口

**简介**  
eMMC 接口作为 eMMC 总线的主机控制器，实现外部 eMMC 卡与内部系统总线主设备之间的数据传输。

**特性**  
- 符合 8 位 eMMC 5.1 规范  
- 兼容SDHCI寄存器集，并包含额外的供应商专用寄存器  
- 支持 1 位 / 8 位 MMC 及 CE-ATA 卡  
- 支持 SDHCI 规范定义的数据传输方式：  
  - PIO  
  - SDMA  
  - ADMA  
  - ADMA2  
- 支持 eMMC 卡的 SPI 模式操作  
- 支持 eMMC 5.1 定义的以下速度模式：  
  - 传统模式：带宽高达26 MB/s，信号电压1.8 V  
  - 高速SDR：带宽高达52 MB/s，信号电压1.8 V  
  - 高速DDR：带宽高达52 MB/s，信号电压1.8 V  
  - HS200：带宽高达200 MB/s，信号电压1.8 V  
  - HS400：带宽高达400 MB/s，信号电压1.8 V  
- 支持硬件自动生成所有命令与数据事务，并进行 CRC 校验  
- 配备 1024 字节数据 FIFO 缓冲区（2 × 512 字节数据块）  

#### 2.2.5 SD/MMC 接口

**简介**
SD/MMC 接口作为 SD/MMC 总线的主机控制器，实现外部 SD/MMC 卡与内部系统总线主设备之间的数据传输。

**特性**
- 符合 4 位 SD 3.0 UHS-I 规范  
- 兼容 SDHCI 寄存器集，并包含额外的供应商专用寄存器  
- 支持 1 位 / 4 位 SD 存储卡  
- 支持 SDHCI 规范定义的数据传输方式：  
  - PIO  
  - SDMA  
  - ADMA  
  - ADMA2  
- 支持 SD 3.0 定义的以下速度模式：  
  - 默认速度：带宽高达 12.5 MB/s，信号电压 3.3 V  
  - 高速：带宽高达 25 MB/s，信号电压 3.3 V  
  - SDR12：时钟频率高达 25 MHz，信号电压 1.8 V  
  - SDR25：时钟频率高达 50 MHz，信号电压 1.8 V  
  - SDR50：时钟频率高达 100 MHz，信号电压 1.8 V  
  - SDR104：时钟频率高达 208 MHz，信号电压 1.8 V  
  - DDR50：时钟频率高达 50 MHz，信号电压 1.8 V  
- 支持硬件自动生成所有命令与数据事务，并进行 CRC 校验  
- 支持读等待控制及 SD/MMC 卡的挂起/恢复功能  
- 通过 GPIO 模式支持卡插拔检测  
- 配备 1024 字节数据 FIFO 缓冲区（2 × 512 字节数据块）  

#### 2.2.6 UFS 接口

**简介**  
UFS（Universal Flash Storage）接口为 SoC 提供高性能、低功耗的大容量存储解决方案，符合 JEDEC UFS 2.2、MIPI UniPro v1.6 及 MIPI M-PHY v3.0 规范。  

UFS 通过串行接口支持最多 2 条通道，提供 2 路发送（TX）和 2 路接收（RX），实现全双工通信。支持高速模式（HS-GEAR3）与低速模式（PWM-GEAR1），兼具高带宽与低延迟特性。支持标准 SCSI 命令集，并允许系统直接从 UFS 存储启动。

**特性**  
- 符合 JEDEC UFS 2.2 规范  
- 符合 MIPI UniPro v1.6 与 MIPI M-PHY v3.0 规范  
- 支持串行接口协议：  
  - 高速模式（HS-GEAR3）：最多 2 TX + 2 RX 通道  
  - 低速模式（PWM-GEAR1）  
- 支持标准 SCSI 命令操作  
- 支持从 UFS 存储直接启动系统

### 2.3 图像子系统

#### 2.3.1 MIPI 摄像头输入接口（MIPI Camera IN Interface）

**简介**  
MIPI 摄像头输入接口集成了四个 MIPI-CSI2 v1.1 控制器，每个控制器配备最多四条数据通道，单通道最高传输速率达 1.5 Gbps。

**特性**  
- 可配置数据通道数：1、2 或 4 条  
- 独立 D-PHY 资源：  
  - CSI0 与 CSI1 各自拥有专用的 D-PHY 接口  
- 共享 D-PHY 资源：  
  - CSI2 与 CSI3 共享一个 4-lane D-PHY 接口；  
    - 单独使用时，每个接口最多支持 4 条通道；  
    - 同时使用时，每个接口最多支持 2 条通道  
- 支持的输入数据格式：  
  - Legacy YUV420 8-bit  
  - YUV420 8-bit
  - YUV422 8-bit  
  - RAW8  
  - RAW10  
  - RAW12  
  - 嵌入式数据类型（Embedded Data）  
- 支持的数据交织类型：  
  - 数据类型交织（Data-type Interleaving）  
  - 虚拟通道交织（Virtual-channel Interleaving）

**架构框图**
<img src="static/mipi_block_diagram.png" alt="" width="800">

#### 2.3.2 GPU（图形处理单元）

**简介**  
本 GPU 架构基于多线程统一着色集群设计，采用高 SIMD 效率的 ALU 架构，并采用基于图块的延迟渲染（Tile-Based Deferred Rendering, TBDR）管线，支持多图块并发处理，可高效执行高性能 3D 图形与通用计算（GPGPU）任务。

**特性**  
- 全面兼容主流图形与计算 API：  
  - OpenGL ES 1.1 / 3.2  
  - EGL 1.5  
  - OpenCL 3.0  
  - Vulkan 1.3  
- 基于图块的延迟渲染 (TBDR) 技术，用于 3D 图形处理，支持并发多图块处理  
- 可编程、抗锯齿（Anti-Aliasing）高质量图像
- 细粒度三角形剔除（Triangle Culling），提高渲染效率  
- 支持 DRM 安全 
- 支持 GPU 虚拟化，最多可创建 8 个虚拟 GPU 实例  
- 多通道隔离技术，提供最多 8 个独立逻辑通道  
- 每个通道/OS 上下文拥有独立 IRQ  
- 与神经网络加速器配合使用时，可选 AI 加速协作 
- 多线程统一着色引擎，支持：  
  - 像素着色（Pixel Shading）  
  - 顶点着色（Vertex Shading）  
  - 通用计算着色器（Compute Shader / GPGPU）  
- ALU 架构针对高 SIMD 利用率优化  
- 采用统一内存架构（UMA）下的全虚拟化内存寻址  
- 细粒度任务切换、负载均衡与电源管理
- 高级 DMA 驱动操作，最小化主机 CPU 干预  
- 128 KB 系统级缓存（SLC）  
- 专用纹理缓存单元
- 压缩纹理解码支持
- 几何处理阶段执行无损几何压缩
- 帧缓冲区支持无损或视觉无损压缩，显著降低带宽需求  
- 用于 GPU 内核管理的专用固件处理器：  
  - 单线程设计  
  - 2 KB 指令缓存 + 2 KB 数据缓存  
  - 独立功耗域（Power Island）  
- 片上性能、功耗与统计寄存器，用于系统实时监控  

#### 2.3.3 V2D（2D 图形加速模块）

**简介**  
V2D 是一个专用的 2D 硬件加速模块，支持常见的 2D 图像操作，包括格式转换、旋转、镜像、缩放、裁剪、纯色填充及 Alpha 混合等。

**特性**  
- 缩放能力：  
  - 最大支持 8× 放大  
  - 最小支持 1/8× 缩小  
- 旋转与镜像：  
  - 支持 0°、90°、180°、270° 旋转  
  - 支持水平/垂直镜像与翻转  
- 混合与合成：  
  - 支持简单图层与背景混合  
- 图像裁剪（Cropping）  
- 纯色填充（Solid Fill）
- 色彩空间转换：  
  - RGB 与 BT.601 / BT.709（窄域与全域）互转  
- 最大分辨率支持：4096 × 2160  
- 抖动（Dithering）处理，实现更平滑的色彩过渡  
- 支持内存管理单元（MMU）  
- 总线接口：APB3、AXI3  
- 支持的输入格式：  
  - RGB888、RGBX888、RGBA8888、ARGB8888（可选 R/B 交换）  
  - RGB565、RGBA5658、ARGB8565（可选 R/B 交换）  
  - A8（8-bit Alpha 图像）、Y8（8-bit 灰度图）  
  - YUV420 半平面格式（UV 可交换）  
  - AFBC 16×16 RGBA8888（Layout0，支持 split/non-split）  
  - AFBC 16×16 NV12（Layout1，支持 split/non-split）  
- 支持的输出格式：  
  - 与输入格式一致，包括 RGB、ARGB、A8、Y8、YUV420 及各类 AFBC 变体

### 2.4 视频子系统

#### 2.4.1 简介

视频处理单元（Video Processing Unit，VPU）是一款四核视频加速器，支持多种视频标准的编解码处理。VPU 内置主机 CPU，并通过运行固件对硬件引擎进行控制，负责比特流解析、子模块调度以及错误恢复等任务。

VPU 最高运行频率可达 1 GHz，支持广泛的视频标准，包括 H.265、H.264、VP8、VP9、MPEG4、MPEG2 和 H.263。其典型并发处理能力包括：
- 支持 4K@60fps 同编同解 
- 4K@90fps H.264/H.265 编码  
- 4K@180fps H.264/H.265 解码  

各视频编解码标准的实际处理均由专用硬件逻辑完成。宏块序列控制器（Macroblock Sequencer）作为主控单元，负责调度各子模块的处理流程，从而减轻处理器负载并降低固件复杂度。

此外，多个与标准无关的模块在运行时共享通用逻辑，以确保在不同视频标准下均具备高效率与流畅的性能表现。

#### 2.4.2 视频编码器（Video Encoder）

**通用编码特性**  
- 可配置的 Arm 帧缓冲压缩 (AFBC) 1.0 或 1.2 版本用于输入  
- 支持 YUV422 与 YUV420 AFBC 块分割（16×16）  
- 支持 stride（不适用于 AFBC 输入格式）  
- 支持水平/垂直镜像（不适用于 AFBC 输入格式）  
- 可选在编码前对输入帧进行 90° 步进旋转（不适用于 AFBC 输入格式）  

> **注意**：若 YUV422 格式在未转换为 YUV420 的情况下进行 90° 或 270° 旋转，输出将自动转为 YUV440 格式。

**支持的源帧输入格式**  
- 单平面 YUV422，逐行扫描，YUYV 或 UYVY 交错排列  
  > **注意**：YUV422 输入可转换为 YUV420  
- 单平面 RGB（8-bit），字节顺序：RGBA、BGRA、ARGB、ABGR  
- 双平面 YUV420，逐行扫描，色度分量 UV 或 VU 交错  
- 三平面 YUV420，逐行扫描  
  > **注意**：仅支持用于测试目的；不建议用于最佳性能  
- AFBC YUV422  
- AFBC YUV420  

**支持的编码格式**  
- HEVC（H.265）Main Profile  
- HEVC (H.265) Main 10 Profile
- H.264 Baseline Profile（BP）  
- H.264 Main Profile（MP）  
- H.264 High Profile（HP）  
- VP8  
- VP9 Profile 0
- JPEG, baseline sequential

**HEVC (H.265) 编码特性**  
- 输出比特流符合 HEVC Main Profile  
- 编码性能：4K@90fps
- 最大帧尺寸：4096 × 4096 像素  
- 位深：8-bit，支持 I、P、B 帧  
- 支持分块模式（Tiled Mode），最多 4 个分块（仅支持水平分割）
- 运动估计（ME）：  
  - 搜索窗口：水平方向 ±128 像素，垂直方向 ±64 像素  
  - 精度：支持低至 1/4 像素（QPEL）  
- 帧内预测模式：  
  - 亮度（Luma）：8×8、16×16、32×32  
  - 色度（Chroma）：4×4、8×8、16×16  
- 帧间预测模式：8×8、16×16、32×32  
- 变换尺寸：  
  - 亮度：8×8、16×16、32×32  
  - 色度：4×4、8×8、16×16  
- 去块滤波（Deblocking Filter）  
- 量化方式：固定 QP 或基于漏桶模型的码率控制（依据目标码率与缓冲区大小）  
- 支持长参考帧（Long-term Reference Frames）
- 支持按 CTU 行粒度插入 Slice

> **注意**：编码器不阻止输出超过每 CTU 的最大比特数限制

**H.264 编码特性**  
- 编码比特流符合 Baseline、Main 与 High Profile  
- 编码性能：4K@90fps
- 最大帧尺寸：4096 × 4096 像素  
- 帧类型：支持 I 帧、P 帧和 B 帧  
- 熵编码：CABAC 或 CAVLC  
  > 注意：CAVLC 不支持 B 帧  
- 运动估计（ME）：  
  - 搜索窗口：水平方向 ±128 像素，垂直方向 ±64 像素  
  - 精度：支持低至 1/4 像素（QPEL）  
- 帧内预测模式：  
  - 亮度：4×4、8×8、16×16  
  - 色度：8×8  
- 帧间预测模式：8×8、16×16  
- 变换尺寸：4×4、8×8  
- 去块滤波（Deblocking Filter）  
- 量化方式：固定 QP 或基于漏桶模型的码率控制（依据目标码率与缓冲区大小）  
- 支持长参考帧（Long-term Reference Frames）  
- Slice 插入粒度：32 像素高的行  

> **注意**：  
> 1. 更多细节请参见 ITU-T H.264 Annex B: VC-1 Compressed Video Bitstream Format and Decoding Process  
> 2. 编码器不阻止输出超过每宏块的最大比特数限制

**VP8 编码特性**  
- 编码性能：4K@90fps
- 最大帧尺寸：2048 × 2048 像素  
- 帧类型：支持 I 帧与P 帧  
- 运动估计（ME）：  
  - 搜索窗口：水平方向±128 像素，垂直方向±64 像素  
  - 精度：支持低至 1/4 像素（QPEL）  
- 帧内预测模式：  
  - 亮度：4×4、8×8、16×16  
  - 色度：8×8  
- 帧间预测模式：8×8、16×16  
- 去块滤波  
- 量化方式：固定 QP 或基于漏桶模型的码率控制（依据目标码率与缓冲区大小）  

**VP9 编码特性**  
- 输出比特流符合 VP9 Profile 0（8-bit）  
- 编码性能：4K@90fps
- 最大帧尺寸：4096 × 4096 像素  
- 采样深度：8-bit  
- 帧类型：支持 I 与 P 帧
- 运动估计（ME）：  
  - 搜索窗口：水平方向±128像素，垂直方向±64像素  
  - 精度：支持低至1/4像素（QPEL）  
- 帧内预测模式：  
  - 亮度：8×8、16×16、32×32  
  - 色度：4×4、8×8、16×16  
- 帧间预测模式：8×8、16×16、32×32  
- 变换尺寸：  
  - 亮度：8×8、16×16、32×32  
  - 色度：4×4、8×8、16×16  
- 去块滤波  
- 量化方式：固定 QP 或基于漏桶模型的码率控制（依据目标码率与缓冲区大小）

#### 2.4.3 视频解码器（Video Decoder）

**通用解码特性**  
- 支持以下输出帧格式：  
  - 双平面 YUV420，逐行扫描，色度 UV 或 VU 交错  
  - 三平面 YUV420，逐行扫描  
    > **注意**：三平面格式仅用于测试，常规应用中不推荐以获得最佳性能  
- 为获得最佳性能，请确保 YUV 缓冲区对齐与 stride 设置正确  
- 支持 8-bit YUV420 AFBC 输出格式  
- 可配置 AFBC 1.0 或 AFBC 1.2 输出  
- Stride 仅适用于逐行扫描格式  
- 支持解码后输出前进行 90° 步进旋转  
  > **注意**：不适用于 AFBC 输出格式  
- 支持在每帧输出中报告每个 32×32 像素块的平均亮度（luminance）与色度（chrominance）值  

**支持的解码格式**
- HEVC（H.265）：Main Profile  
- H.264：Baseline、Main、High Profiles  
- VP8  
- VP9：Profile 0 和 Profile 2（10-bit）
- VC-1：Simple Profile（SP）、Main Profile（MP）、Advanced Profile（AP）  
- MPEG-4：Simple Profile（SP）、Advanced Simple Profile（ASP）  
- MPEG-2：Main Profile（MP）  
- H.263：Profile 0

**HEVC（H.265）解码特性**  
- 完全符合 Main Profile  
- 解码性能：4K@180fps
- 最大帧尺寸：4096 × 4096 像素

**H.264 解码特性**
- 完全符合 Baseline、Main、High 及 High 10 Progressive Profiles  
- 解码性能：4K@180fps
- 无论 NAL 数据包格式设置如何，始终启用转义选项，以防止模拟网络抽象层 (NAL) 单元起始码  

> **注意**：更多细节请参见 ITU-T H.264 Annex B: VC-1 Compressed Video Bitstream Format and Decoding Process

**VP8 解码特性**  
- 完全符合 VP8 规范  
- 解码性能：4K@180fps
- 最大帧尺寸：2048 × 2048 像素

**VP9 解码特性**  
- 完全符合 Profile 0  
- 解码性能：4K@180fps
- 最大帧尺寸：4096 × 4096 像素  

**VC-1 解码特性**  
- 完全符合 VC-1 SP (Simple Profile), MP (Main Profile), and AP (Advanced Profile)  
- 解码性能：4K@120fps
- 最大帧尺寸：2048 × 4096 像素

**MPEG4 解码特性**  
- 符合 MPEG-4 SP (Simple Profile) 与 ASP (Advanced Simple Profile)  
- 支持全局运动补偿（GMC），限制为单 warp 点  
- 解码性能：4K@120fps
- 最大帧尺寸：2048 × 2048 像素

**MPEG2 解码特性**  
- 符合 MPEG-2 MP (Main Profile)  
- 解码性能：4K@120fps
- 最大帧尺寸：  
  - 逐行流：宽度最高 4096 像素  
  - 隔行流：宽度最高 2048 像素，高度最高 4096 像素

**H.263 解码特性**  
- 符合 H.263 Profile 0  
- 解码性能：4K@120fps  
- 最大帧尺寸：宽高均达 2048 像素

### 2.5 显示子系统

#### 2.5.1 显示控制器

**简介**  
显示控制器是一个硬件模块，负责将内部存储器中的显示数据传输至 DSI 和 DP/eDP 控制器。该模块支持高分辨率面板及多种高级图像处理功能。

**特性**  
- 分辨率支持：    
  - 3840 × 2160 @ 60 fps  s
  - 2560 × 1440 @ 144 fps  
- 图层合成（Layer Composition）：  
  - 支持最多 4 个全尺寸图层合成器  
  - 通过 RDMA 通道的上下图层复用机制，最多可支持 16 个图层合成器  
- 命令与回写（Command & Write-Back）：  
  - 采用 `cmdlist` 机制配置硬件寄存器  
  - 支持原始格式与 AFBC 格式的并发回写  
  - 回写路径中支持抖动（Dithering）、裁剪（Cropping）和旋转（Rotation）  
- 内存管理：  
  - 配备高级 MMU，在 90° 与 270° 旋转操作中几乎无页缺失（Page Miss）  
- 色彩与显示增强：  
  - 支持色键（Color Keying）与纯色生成  
  - 支持高级误差扩散（Error Diffusion）与基于图案的抖动算法  
  - 支持色彩饱和度与对比度增强  
  - 支持显示效果动态调节  
- 输入格式：  
  - ABGR2101010、ARGB2101010、BGRA2101010、RGBA2101010  
  - ABGR8888、ARGB8888、BGRA8888、RGBA8888  
  - XBGR8888、XRGB8888、BGRX8888、RGBX8888  
  - BGR888、RGB888、ABGR1555、RGBA5551、BGR565 / RGB565  
  - XYUV_444_P1_8、XYUV_444_P1_10、YVYU_422_P1_8、VYUY_422_P1_8  
  - YUV_420_P2_8、YUV_420_P3_8
   <img src="static/disp_input_addr.png" alt="" width="800">
- 输出格式：  
  - RGB888、RGB565、RGB666  
- 面板与模式支持：  
  - 支持视频模式（Video Mode）与命令模式（Command Mode，帧缓冲位于 LCM 中）  
  - 支持嵌入式 DFC 缓冲区实现 DDR 频率动态调节  
- 源格式支持：  
  - 同时支持 AFBC 与原始图像源  

#### 2.5.2 MIPI DSI 接口

**简介**  
MIPI 显示串行接口（MIPI Display Serial Interface, DSI）是一种高速接口，用于连接主处理器与显示外设，完全符合 MIPI 联盟针对移动与嵌入式设备制定的相关规范。

**特性**  
- 标准合规性：  
  - MIPI DSI v1.2  
  - MIPI D-PHY v1.2  
  - Display Command Set (DCS) 标准  
- 通道与速率支持：  
  - 最多支持 8 条数据通道  
  - 单通道最高传输速率可达 4.5 Gbps  
  - 每个 D-PHY 链路支持 1 个活动面板  
- 分辨率支持：  
  - 最高支持 3840 × 2160 @ 60 fps 或 2560 × 1440 @ 90 fps  
- 工作模式：  
  - 命令模式（Command Mode）  
  - 视频模式（Video Mode）  
  - 视频突发模式（Video Burst Mode）  
- 信号类型支持：  
  - HS-TX（高速发送）  
  - LP-TX / LP-RX（低功耗发送 / 接收）  
  - LP-CLK / LP-CD（低功耗时钟 / 数据）  
- 数据与通道特性：  
  - 支持 DSI 与 DCS 规范定义的所有像素格式  
  - 支持 MIPI 链路上的虚拟通道（Virtual Channels）  
  - 支持突发视频模式，D-PHY 单通道速率最高达 4.5 Gbps

#### 2.5.3 DP/eDP 控制器

**简介**  
DP/eDP 控制器是一种显示接口控制器，用于管理从 SoC 到外部 DisplayPort (DP) 或嵌入式 DisplayPort (eDP) 面板的数据传输。

**特性**  
- 符合 DisplayPort（DP）v1.2 标准  
- 符合嵌入式 DisplayPort（eDP）v1.4 标准  
- 支持最高分辨率：3840 × 2160 @ 60 fps 或 2560 × 1440 @ 144 fps

### 2.6 音频子系统

#### 2.6.1 简介 

K3 SoC 集成了一个功能完备的音频子系统，旨在提供高音质、低延迟的音频性能。该子系统包含多个 I²S 接口和 DisplayPort 音频接口，可广泛支持多媒体播放、语音通信等多样化应用场景中的录音与回放需求。

子系统包含以下主要接口：  
- 6 路全双工 I²S 接口 
- 4 路半双工 I²S 接口（其中两路连接至 DP/eDP 控制器）  
- 2 路 DP/eDP 音频接口

#### 2.6.2 全双工 I²S 接口特性

- 支持全双工操作，可同时进行播放与录音  
- 符合标准 I²S 音频格式规范  
- 固定音频参数：  
  - 采样率：48 kHz  
  - 数据位宽：16 位  
  - 声道数：2（立体声）  
- 可配置系统时钟（sysclk）模式：64fs、128fs 或 256fs  

#### 2.6.3 半双工 I²S 接口特性  

- 支持半双工模式下的播放或录音  
- 兼容标准 I²S、左对齐（Left-Justified）和右对齐（Right-Justified）格式  
- 基础音频参数：  
  - 采样率：48 kHz  
  - 数据位宽：16 位  
  - 声道数：2（立体声）  
- 支持 TDM（时分复用）模式：  
  - 支持 DSP_A 与 DSP_B 模式  
  - 采样率：48 kHz  
  - 数据位宽：16 位 / 32 位  
  - 最多支持 4 个声道

#### 2.6.4 DP/eDP 音频接口特性 

- 支持通过 DisplayPort 或嵌入式 DisplayPort（eDP）链路传输音频  
- 兼容 I²S、左对齐及右对齐格式  
- 音频参数：  
  - 采样率：最高达 192 kHz  
  - 数据位宽：16 位 / 20 位 / 24 位  
  - 声道数：2（立体声）

### 2.7 互联子系统

#### 2.7.1 PCIe 3.0 （含IOMMU）

**简介**  
K3 SoC 集成了五个 PCIe 端口 —— PCIeA、PCIeB、PCIeC、PCIeD 和 PCIeE，每个端口均支持 PCIe Gen3 规范，单通道速率高达 8 GT/s。

- 通道配置：  
  - PCIeA 提供 8 条通道  
  - PCIeB 与 PCIeC 各提供 2 条通道  
  - PCIeD 与 PCIeE 各提供 1 条通道  
- 模式支持：  
  - PCIeA 支持双模式操作（Root Complex / Endpoint）  
  - PCIeB、PCIeC、PCIeD 和 PCIeE 仅支持 Root Complex（RC）模式  
- 虚拟通道（Virtual Channel）：  
  - PCIeB、PCIeC、PCIeD 和 PCIeE 支持 VC0 与 VC1  
- IOMMU 支持：  
  - PCIeA、PCIeB 和 PCIeE 支持 IOMMU，用于设备虚拟化  
- PHY 配置：  
  - 共集成 6 个 PHY，提供 8 条通道  
  - PHY0 与 PHY1 为双通道 PHY  
  - PHY2、PHY3、PHY4 与 PHY5 为单通道 PHY  
  - PHY2、PHY3 和 PHY4 在 PCIe 与 USB 之间共享

**特性**  
- 支持双模式操作，可通过编程配置为 Root Complex（RC）或 Endpoint（EP）  
- 集成内部地址转换单元（Internal Address Translation Unit, iATU），包含 8 个出站（Outbound）和 8 个入站（Inbound）映射表项  
- 集成 DMA 引擎，具备硬件流控机制，包含 4 个写通道和 4 个读通道  
- 支持 ECRC（End-to-End CRC）生成与校验  
- 支持最大有效载荷（Max Payload Size）达 256 字节  
- 支持自动通道翻转（Lane Flip）与极性反转（Lane Reversal）  
- 支持 Active State Link Power Management（ASPM），涵盖 L0 与 L1 电源状态  
- 支持延迟容忍度报告（Latency Tolerance Reporting, LTR）  
- 支持虚拟通道 VC0 与 VC1
- 支持精确时间测量（Precision Time Measurement，PTM）  
- 支持基于 ID 的排序（ID-Based Ordering, IDO）  
- 支持 Completion Timeout 范围配置  
- 支持独立展频的分离参考时钟（Separate Reference Clock with Independent Spread, SRIS）  
- 支持最多 64 个出站 Non-Posted 请求  
- 支持最多 32 个未完成的 AXI 从设备 Non-Posted 请求  
- Endpoint（EP）模式下：  
  - 支持 Function 0，配备 6 个可编程尺寸的 BAR（Base Address Register）  
  - 支持 MSI（Message Signaled Interrupt）能力  
- Root Complex（RC）模式下：  
  - 集成 MSI 与 MSI-X 接收模块  

#### 2.7.2 USB

**简介**  
K3 SoC 集成了多个 USB 接口，以支持高速连接和灵活的设备配置。USB 子系统包含以下端口：
- 1 个 USB 2.0 Host 端口 
- 1 个 USB 3.0 DRD（Dual-Role Device，双角色设备）端口，集成 USB 2.0 DRD 接口（称为 USB 3.0 Port A）  
- 3 个 USB 3.0 Host 端口（USB 3.0 Port B/C/D）——其 SuperSpeed PHY 与 PCIe 共享，可在 USB 或 PCIe 模式下运行，但同一时间仅能启用其中一种功能

##### USB 2.0 Host 端口特性

**控制器**  
- 仅支持 USB 2.0 Host 模式  
- 完全符合 USB 2.0 规范  
- 主机控制器寄存器及数据结构遵循 Intel xHCI 规范  
- 支持 High-Speed（480 Mb/s）、Full-Speed（12 Mb/s）和 Low-Speed（1.5 Mb/s）操作  

**通信接口**  
- 采用 UTMI+（30/60 MHz）接口连接 USB 2.0 PHY  

**时钟域**  
- UTMI+ PHY（30/60 MHz）  
- MAC（标称 125 MHz）  
- 总线时钟域  
- RAM 时钟域  

**系统与电源管理**  
- 集成 DMA 控制器  
- 支持 USB 2.0 Suspend 模式  

**端点与内存**  
- Device 模式下最多支持 32 个端点  
- 端点 FIFO 大小可灵活配置（不强制为 2 的幂次），便于连续内存分配  
- 支持描述符缓存与数据预取，提升高延迟系统中的性能  

**其他特性**  
- 软件控制的标准 USB 命令（SETUP 包可转发至应用层进行解析）  
- 硬件级 USB 总线及包级错误处理机制  
- 支持中断

##### USB 3.0 DRD 端口特性（Port A，含 USB 2.0 DRD 接口）

**控制器**  
- 同时支持 USB 3.0 与 USB 2.0 的 Host 和 Device 模式  
- 完全符合 USB 3.0 与 USB 2.0 规范  
- USB 3.0 Host 控制器寄存器及数据结构遵循 Intel xHCI 规范  
- USB 3.0 Device 控制器寄存器及数据结构为自定义格式，需通过软件配置  
- 支持1个USB 3.0 端口和 1 个USB 2.0端口  
- 支持 SuperSpeed（5 Gb/s）、High-Speed（480 Mb/s）、Full-Speed（12 Mb/s）及 Low-Speed（1.5 Mb/s，仅限 Host 模式）  

**通信接口**  
- USB 3.0 PHY 采用 PIPE3（125 MHz）接口  
- USB 2.0 PHY 采用 UTMI+（30/60 MHz）接口  

**时钟域**  
- PIPE3 PHY（125 MHz）  
- UTMI+ PHY（30/60 MHz）  
- MAC（标称 125 MHz）  
- 总线时钟域  
- RAM 时钟域  

**系统与电源管理**  
- 集成 DMA 控制器  
- 支持 USB 2.0 Suspend 模式  
- 支持 USB 3.0 U1/U2/U3 低功耗状态  

**端点与内存**  
- Device 模式下最多支持 32 个端点  
- 端点 FIFO 大小可灵活配置  
- 支持描述符缓存与数据预取，优化吞吐性能  

**其他特性**  
- 软件控制的标准 USB 命令  
- 硬件级 USB 总线及包级错误检测与恢复机制  
- 中断支持  
- USB 3.0 SuperSpeed PHY 集成内部 Type-C 插拔方向切换开关，可通过 GPIO 输入控制  

##### USB 3.0 Host 端口特性（Ports B/C/D）

**控制器**  
- 支持 USB 3.0 与 USB 2.0 Host 模式  
- 完全符合 USB 3.0 与 USB 2.0 规范  
- USB 3.0 Host 控制器寄存器及数据结构遵循 Intel xHCI 规范  
- 支持 1 个USB 3.0 端口和 1 个 USB 2.0 端口  
- 支持 SuperSpeed（5 Gb/s）、High-Speed（480 Mb/s）、Full-Speed（12 Mb/s）和 Low-Speed（1.5 Mb/s）操作  

**通信接口**  
- USB 3.0 PHY 采用 PIPE3（125 MHz）接口  
- SuperSpeed PHY 与相应的 PCIe 端口共享（一次只能激活一个功能）  
- USB 2.0 PHY 采用 UTMI+（30/60 MHz）接口  

**时钟域**  
- PIPE3 PHY（125 MHz）  
- UTMI+ PHY（30/60 MHz）  
- MAC（标称 125 MHz）  
- 总线时钟域  
- RAM 时钟域  

**系统与电源管理**  
- 集成 DMA 控制器  
- 支持 USB 2.0 Suspend 模式  
- 支持 USB 3.0 U1/U2/U3 低功耗状态  

**端点与内存**  
- Device 模式下最多支持 32 个端点  
- 端点 FIFO 大小可灵活配置  
- 描述符缓存与数据预取，提升性能  

**其他特性**  
- 软件控制的 USB 命令  
- 硬件级 USB 总线及包级错误处理机制  
- 支持中断

**模块框图**

<img src="static/usb_block_diagram.png" alt="" width="800">

#### 2.7.3 以太网 GMAC

**产品简介**  
K3 集成了四个千兆媒体访问控制器（Gigabit Media Access Controller, GMAC）接口，符合 IEEE 802.3-2015 标准，适用于音视频（AV）桥接/节点、交换机、网络接口卡（NIC）以及数据中心桥接等应用场景。

**特性**
- 支持 10 / 100 / 1000 Mbps 链路速度
- 支持 MII、RMII 和 RGMII 接口
- 提供一组丰富的数据包（packet）过滤功能，包括：  
  - MAC 地址的哈希（Hash）与精确（Perfect）匹配过滤  
  - 源/目的 IP 地址过滤  
  - 源/目的 TCP/UDP 端口过滤  
- 兼容 IEEE 1588 v1/v2，时间同步精度可达亚微秒级  
- 支持基于 UDP 的 PTP 一阶段（One-step）时间戳  
- 传输流量控制：  
  - 全双工模式下支持 IEEE Pause 帧或优先级流控（Priority Flow Control, PFC）帧  
  - 半双工模式下采用背压（Backpressure）机制  
  - 通过 IEEE Pause 帧实现接收方向流控  
- 提供全面的 TCP/IP 卸载功能：  
  - 源地址和 VLAN 的插入、替换和删除  
  - 通过基于硬件的校验和计算和插入来传输校验和卸载  
  - 通过硬件校验和验证接收校验和卸载  
  - IP 校验和卸载：支持硬件计算并插入  
  - TCP/UDP 校验和卸载：支持硬件计算并插入  
  - 支持报文头与有效载荷分离存储（Header/Payload Split）  
  - TCP/UDP 分段卸载（TSO, TCP Segmentation Offload）  
- 支持时间敏感网络（TSN）：  
  - 调度流量增强（IEEE 802.1Qbv-2015）  
  - 帧抢占（Frame Preemption, IEEE 802.1Qbu-2016）  
  - 基于时间的调度（Time-based Scheduling）  

#### 2.7.4 CAN-FD 接口

**简介**  
K3 最多集成 10 路 CAN-FD 接口。每个 CAN-FD 控制器均为完整的 CAN 协议实现，同时兼容 CAN with Flexible Data-Rate（CAN-FD） 与 CAN 2.0 Part B 规范，适用于高性能汽车电子及工业通信场景。

**特性**
- 完全符合 CAN-FD 协议与 CAN 2.0 Part B 标准，支持：  
  - 标准帧与扩展帧格式  
  - 数据载荷长度从 0 至 64 字节  
  - 可编程码率 （Bit Rate）  
  - 基于内容的寻址（Content-Related Addressing）  
- 符合 ISO 11898-1 标准  
- 硅验证通过 ISO 16845-1:2016 CAN 一致性测试  
- 灵活的消息邮箱（Mailbox）配置：  
  - 每个邮箱可配置为 0、8、16、32 或 64 字节  
  - 支持独立配置为发送或接收标准/扩展消息  
- 接收 FIFO：  
  - 最多支持 6 帧深度  
  - 自动指针管理，并支持 DMA 传输  
- 传输特性：支持中止功能，可配置优先级（最低ID、最低缓冲区编号或最高优先级）
- 灵活的消息缓冲区：128个槽位（每个8字节），可配置为发送器或接收器
- 可编程时钟源：外设时钟或振荡器  
- 可用于通用存储的RAM（非传输/接收必需）  
- 特殊工作模式：  
  - 监听模式（Listen-Only Mode, LOM）  
  - 自环回模式（Loop-Back Mode），用于自检  
  - 在低功耗模式（Doze 和 Stop）下支持“伪网络”（Pretended Networking）唤醒功能  
- 定时与同步：  
  - 16位自由运行定时器，可选外部时钟信号  
  - 通过特定报文实现全局网络时间同步  
  - 错误状态寄存器 1（Error Status 1）中的 SYNCH 位指示同步状态  
- 错误处理机制：  
  - 发送报文提供 CRC 状态反馈  
  - 每字节配备 5 位奇偶校验码，可纠正单比特错误、检测双比特错误（SEC-DED）  
- 高级接收过滤功能：  
  - ID过滤支持128个扩展ID、256个标准ID或512个部分（8位）ID  
  - ID 过滤表中最多可包含 32 个元素  
  - 支持标识符匹配命中指示（Identifier Acceptance Filter Hit Indicator, IDHIT）  
- 支持 CAN-FD 高速模式下的收发器延迟补偿（Transceiver Delay Compensation, TDC）  
- 低延迟高优先级通信：  
  - 通过仲裁机制确保高优先级消息的低传输延迟  
- 每个邮箱/FIFO 支持独立且可屏蔽的中断  
- 完全向后兼容早期 CAN-FD 版本  

#### 2.7.5 SPI 接口

**简介**  
SPI（Serial Peripheral Interface，串行外设接口）是一种同步串行通信接口，支持通过 Motorola SPI 协议与外部设备进行数据交互。该接口可配置为 Master 模式（连接的外设作为 Slave）或 Slave 模式（连接的外设作为 Master）。

**特性**
- 支持SPI规范定义的所有四种 CPOL/CPHA 组合。  
- 可灵活配置为 Master 或 Slave 工作模式。  
- 支持仅接收（Receive-without-Transmit）操作模式。  
- 串行波特率范围：  
  - 最低推荐速率：6.3 Kbps  
  - 最高支持速率：52 Mbps  
- 数据大小可配置为 8 位、16 位、18 位或 32 位。  
- 配备独立的发送（TXFIFO）与接收（RXFIFO）缓冲区：  
  - 在非打包数据模式下，两个 FIFO 均为 32 个条目 ×32 位，总共支持 32 个样本  
  - 在打包数据模式下，8 位或 16 位数据使用双深度FIFO，提供 64 个条目 ×16 位，总共支持 64 个样本  
  - 两种 FIFO 均支持通过 程序化 I/O（PIO） 或 DMA 突发传输 进行数据加载与卸载。

#### 2.7.6 UART 接口

**简介**  
UART（Universal Asynchronous Receiver/Transmitter，通用异步收发器）模块提供系统与外部设备之间的异步串行通信。该模块支持灵活配置、高效数据处理及诊断功能，适用于低速至高速等多种通信场景。

**特性**
- 接口：支持多达 17 个独立的UART接口。包括 11 个 AP 域 UART 和 6 个 RCPU 域 UART  
- 兼容性：完全兼容业界标准的 8250 UART 规范  
- 异步通信：在串行数据流中自动插入和移除起始位、停止位和奇偶校验位  
- 中断控制：可独立控制发送、接收、线路状态和数据设置中断（Data Set Interrupt）  
- 调制解调器控制（Modem Control）：AP 域的 UART1–UART10 和 RCPU 域的 UART1 支持 CTS 和 RTS  
- 自动流控（Auto Flow Control）：  
  - RTS（输出）：由 UART 接收 FIFO 自动驱动  
  - CTS（输入）：由外部调制解调器的发送信号控制  
- 可编程串行参数：  
  - 字符长度：7 或 8 位  
  - 校验方式：偶校验、奇校验或无校验  
  - 停止位：1 位  
  - 波特率：最高达 3.6 Mbps（适用于 4 路高速 UART）  
  - 支持伪起始位（False Start-Bit）检测  
- FIFO 缓冲区：  
  - 发送 FIFO：256 字节  
  - 接收 FIFO：256 字节  
- 诊断功能：  
  - 环回模式（Loopback Mode），用于通信链路验证  
  - 中断、奇偶校验和帧错误模拟  
- DMA 支持：提供独立的 DMA 请求通道，分别用于发送和接收操作  

#### 2.7.7 I²C 总线接口

**产品简介**  
Inter-Integrated Circuit（I²C）总线是一种支持多主设备的串行通信总线，具备冲突检测与总线仲裁能力。  
I²C 总线接口可在 I²C 总线上配置为 主设备（Master） 或 从设备（Slave）。该串行接口由 Philips 公司开发，仅需两条信号线即可实现通信：
- SDA：双向数据线，用于输入和输出  
- SCL：时钟线，提供时序基准与总线控制  

I²C 总线可实现 I²C 控制器与各类外部 I²C 外设或微控制器之间的无缝通信。其简洁的硬件设计为片上与片外设备之间传输控制与状态信息提供了高效且低成本的解决方案。

该 I²C 总线接口挂接于外设总线（Peripheral Bus），并支持以下功能：
- 通过带缓冲的接口进行可靠的数据传输  
- 通过内存映射寄存器（Memory-Mapped Registers）实现控制与状态管理  

**特性**
- 最多支持 10 路独立 I²C 接口  
- 符合 I²C 总线规范 Version 2.1，但以下功能除外：  
  - 硬件通用呼叫（General Call）支持  
  - 10 位从设备地址（10-bit Slave Addressing）  
  - CBUS 兼容性  
- 支持 多主设备（Multi-Master）操作 与 总线仲裁机制  
- 支持以下工作模式及速率：  
  - 标准模式（Standard Mode）：最高 100 Kbps  
  - 快速模式（Fast Mode）：最高 400 Kbps  
  - 高速从设备模式（High-Speed Slave Mode）：最高 3.4 Mbps（仅限高速 I²C）  
  - 高速主设备模式（High-Speed Master Mode）：最高 3.3 Mbps（仅限高速 I²C）  

> **注意：**  
> 1. 在高速主设备模式下，实际工作频率受限于总线上上拉电阻的阻值。  
> 2. SCL 时钟频率 *f* 与上拉电阻 *R* 成反比关系，即 *f ∝ 1/R*。

**模块框图**  

I²C 总线接口的架构如下图所示：  

<img src="static/i2c_block_diagram.png" alt="" width="600">

#### 2.7.8 红外接收接口（IR-RX Interface）

**简介**  
IRC（红外控制器，Infrared Remote Control Receiver）用于接收来自外部红外源的红外信号。

**特性**
- 最多支持 4 路 IRC 模块  
- 将接收到的红外信号转换为 游程编码（Run-Length Code, RLC）格式 
- 可配置的信号脉宽阈值，用于噪声滤波与有效信号检测  
- 配备 32 字节 FIFO，用于暂存接收到的数据  
- 采样时钟最高可达 102.4 MHz，内置 24 位频率分频器，允许用户灵活配置采样时钟频率  

#### 2.7.9 eSPI

**简介**  
eSPI 控制器完整实现了 Enhanced Serial Peripheral Interface（eSPI）v1.0 协议，该协议由 Intel 于 2016 年正式发布，旨在替代传统的 LPC（Low Pin Count）接口，显著降低引脚数量与功耗。eSPI 广泛应用于嵌入式控制器（EC）、基板管理控制器（BMC）、Super I/O（SIO）器件、Port-80 调试卡等场景。

eSPI 在电气特性上沿用 SPI 总线基础，但重新定义了协议层。相比 LPC 接口，eSPI 具备以下优势：
- 将所有 LPC/SMBus/边带信号统一转换为 带内（in-band）信号，大幅减少所需引脚数  
- 支持 20 MHz、25 MHz、33 MHz、50 MHz 和 66 MHz 多种工作频率，提供更高带宽  
- 采用 1.8 V 接口电压

**基本特性**
- 完全符合 eSPI v1.0（2016）规范  
- 支持四种通道类型：外设通道（Peripheral Channel, PR）， 带外通道（Out-of-Band Channel, OOB）， 虚拟线通道（Virtual Wires Channel, VW）， Flash 访问通道（Flash Access Channel）
- I/O 模式支持：1×、2×、4×  
- 频率模式支持：20 / 25 / 33 / 50 / 66 MHz  
- 支持最多连接 1 个从设备（SLAVE0）  
- 支持自动 CRC 插入与校验，可通过设置 `CRC_CHECK_EN`（0x68，SLAVE0_CONFIG）启用 CRC 校验  
- 提供两路合并中断输出：控制器状态/错误中断和VW 中断；CPU 通过读取状态寄存器识别具体中断源  
- 集成看门狗与软件复位机制，防止在通过 AXI3 从接口执行 PR 读操作时因从设备无响应导致总线挂死  
- 支持主接口自动门控，在空闲期间降低功耗  
- 允许软件重写内部从设备状态寄存器，便于调试  
- 提供寄存器映射的 `RESET#` 信号，用于复位 eSPI 从设备  

**PR 通道特性**  
- PR 通道为软件提供对从设备进行透明读写操作的机制  
- eSPI 控制器的 AXI 从接口可转换为 eSPI 总线上的 PR 读写操作；反之，eSPI 总线上从设备发起的请求将转换为 AXI 主接口读写操作，简化 PR 通道通信流程  
- 发送（TX）与接收（RX）数据分别存储于独立的 32 位 × 16 深度 FIFO 
- 使用两个 32 MB 地址窗口通过配置 `PR_BASE_ADDR_MEM_0`（0x38）和 `PR_BASE_ADDR_MEM_1`（0x3C），可访问从设备完整的 32 位内存地址空间  
- 一个 16 KB 的地址空间用于 PR I/O 读写操作，允许直接访问 16 位 I/O 空间  
- PR通道上的消息类型传输通过操作寄存器进行启动和接收，并使用独立的32字节FIFO  
- 最大传输单元：`PR_MAX_SIZE = 64 字节`，要求主从设备在 PR 通道上的每次传输不得跨越 64 字节边界  

**VW 通道特性**
- 支持 VW 中断 0–23 
- 最多支持 16 路 GPIO，划分为 4 组，对应 4 个索引；GPIO 组与 VW 通道索引的映射关系可配置  
- 单次 VW 传输最大计数为 16 
- 可通过寄存器配置触发从设备的中断或 GPIO 操作  
- 支持中断与 GPIO 状态的自动更新  
- 支持系统事件索引 2–7，并生成相应中断  
- 每个中断均关联一个状态寄存器，支持中断屏蔽与极性配置

**OOB 通道特性**
- OOB 请求转发由 CPU 通过中断处理  
- 单次 OOB 传输最大长度为 128 字节  

**Flash 访问通道特性**
- Flash 访问请求转发由 CPU 通过中断处理  
- 单次 Flash 访问传输最大长度为 128 字节

**模块框图**
eSPI 控制器架构如下图所示：

<img src="static/espi_block_diagram.png" alt="" width="800">

### 2.8 安全子系统

#### 2.8.1 密码引擎（Crypto Engine）

**简介**  
支持国际通用密码算法及中国商用密码算法。

**特性**
- 哈希算法：SHA1 / SHA224 / SHA256、SM3  
- 对称加密算法：AES-128 / 192 / 256、SM4  
- 非对称加密算法：RSA-1024 / 2048 / 4096、ECC-128 / 256 / 512、SM2  

#### 2.8.2 TRNG

**简介**  
符合中国商用密码标准的真随机数发生器（True Random Number Generator, TRNG）。

**特性**
- 内置 32 位 TRNG  
- 满足 随机性、不可预测性与不可重现性 的安全要求

#### 2.8.3 eFuse

**简介**  
集成 4096 位 eFuse，划分为 16 个 Bank，每个 Bank 为 256 位，其中*256 位可供用户自定义使用。

**特性**
- 支持 eFuse Bank 锁定（防篡改）  
- 支持 硬件参数自动加载  
- 支持 芯片生命周期管理
- 支持 安全启动（Secure Boot）配置  
- 支持 根密钥（Root Key）及加密保护密钥的存储 
- 支持 256 位非易失性计数器（NV Counter） 

#### 2.8.4 IOPMP

**简介**  
IOPMP（I/O Physical Memory Protection，I/O 物理内存保护）模块与 PMP（Physical Memory Protection）协同设计，用于保障平台外设的安全访问控制。
- PMP 负责校验由 RISC-V 核心发起的总线访问请求；  
- IOPMP 则负责验证由其他总线主设备。

IOPMP 仅可由 安全世界（Secure World） 配置，用于定义非 CPU 主设备所发起事务的访问权限与属性。
所有此类事务均需通过 IOPMP 条目检查，仅当权限验证通过后才允许访问。

**特性**
- 支持对 读、写、执行 权限的细粒度访问控制  
- 总线请求在权限检查后会产生一个周期的延迟  
- 支持 访问违规事件信息记录  
- 支持 访问违规中断生成
- 集成 9 个 IOPMP 实例，为各类硬件模块与子系统提供独立的安全管控能力

### 2.9 系统外设

#### 2.9.1 DMA

**简介**  
直接存储器访问（Direct Memory Access, DMA）控制器用于在内存与外设之间传输数据，无需 CPU 干预，从而显著提升系统性能并降低处理器开销。

外设不会直接向内存控制器发起地址或命令请求。取而代之的是，每个来自外设的 DMA 请求将触发一次对应的内存总线事务。

此外，处理器亦可通过 DMA 控制器访问外设总线。此时，DMA 控制器作为 DMA 桥接器（DMA Bridge），可在必要时绕过系统的主 DMA 路径，实现灵活的数据通路。

DMA 控制器通过 16 个可配置 DMA 通道，在 DMA 直通模式（Flow-Through Mode） 下支持多种数据传输类型。支持的传输路径如下表所示：

| 源 / 目标<br>Source / Destination | 片上内存<br>Internal Memory | 片外内存<br>External Memory | 片上外设<br>Internal Peripheral | 片外外设<br>External Peripheral |
| --- | --- | --- | --- | --- |
| **片上内存**<br>Internal Memory | 直通模式 | — | — | — |
| **片外内存**<br>External Memory | 直通模式 | 直通模式 | — | — |
| **片上外设**<br>Internal Peripheral | 直通模式 | 直通模式 | — | — |
| **片外外设**<br>External Peripheral | 直通模式 | 直通模式 | — | — |

**特性**
- 集成 两个独立的 DMA 控制器实例，分别用于：  
  - 安全域（Secure Domain）  
  - 非安全域（Non-Secure Domain）  
- 在 DMA 直通模式 下支持以下数据传输类型：  
  - 内存 ↔ 内存（Memory-to-Memory）  
  - 外设 → 内存（Peripheral-to-Memory）  
  - 内存 → 外设（Memory-to-Peripheral）  
- 支持 Flash 与 DDR 内存之间的直通模式数据传输  
- 优先级机制：最多可同时处理 4 个存在未完成请求的 DMA 通道  
- 16 个 DMA 通道均支持两种工作模式：  
  - 描述符获取模式（Descriptor-Fetch Mode）  
  - 非描述符获取模式（Non-Descriptor-Fetch Mode）  
- 支持以下 高级描述符模式：  
  - 描述符比较（Descriptor Comparison）  
  - 描述符跳转（Descriptor Branching）  
- 支持从外设接收缓冲区中 提取尾部字节（Trailing Bytes）  
- 可配置突发传输长度：8、16、32 或 64 字节  
- 可编程外设数据宽度：字节（Byte）、半字（Half-Word）或字（Word）  
- 单个描述符最大支持 8191 字节 数据传输；更大传输通过 多描述符链式连接（Chaining） 实现  
- 支持 流控位（Flow Control Bit），用于同步 DMA 请求与外设就绪状态（仅当流控位有效时才执行传输）  
- 64 位地址总线，支持对 4 GB 以上物理地址空间 的直接访问

**模块框图**

DMA 控制器架构如下图所示：

<img src="static/dma_block_diagram.png" alt="" width="500">

#### 2.9.2 HDMA

**产品简介**  
K3 集成了 8 个 AXI DMA 控制器（HDMA）。HDMA IP 核是一款高性能、高吞吐量的通用 DMA 控制器，专为在系统内存与高速外设（如高速数据转换器）之间高效传输数据而设计。

**特性**
- 支持 非对齐地址传输（Unaligned Address Transfers）  
- 支持 自动跨越 4KB 地址边界（Automatic 4K Boundary Crossing）  
- 采用 零延迟传输切换架构，确保高速流式数据的连续无中断传输  
- 支持 循环传输模式（Cyclic Transfers）  
- 支持 二维传输（2D Transfers）  
- 支持 分散-聚集传输（Scatter-Gather Transfers）  
- 支持 帧锁（Framelock）机制，用于多路数据流的精确同步  
- 支持 自动运行模式，实现自主传输操作  

#### 2.9.3 定时器（Timer）

**简介**  
K3 SoC 集成了 9 个通用 32 位定时器，用于各类系统级应用。每个定时器均配备独立的 32 位定时器计数控制寄存器（TCCRn），并以 向上计数（Up-Counter） 模式工作。

**特性**
- 可编程计数模式：  
  - 快速计数模式（Fast Count Mode）：输入时钟频率可选 12.8 MHz、6.4 MHz、3 MHz 或 1 MHz  
  - 慢速计数模式（Slow Count Mode）：输入时钟频率为 32.768 kHz 

#### 2.9.4 看门狗定时器（Watchdog Timer, WDT）

**简介**  
K3 SoC 集成了 6 个 24 位看门狗定时器（WDT），用于监控系统运行状态，并在发生软件故障或系统挂死时触发恢复操作。

**特性**
- 可编程计数模式：  
  - WDT 使用 256 Hz 的输入时钟频率  
  - 每个 WDT 包含一个 24 位计数器

#### 2.9.5 温度传感器（Temperature Sensor）

**简介**  
K3 集成了一个温度传感器（TSEN）模块，支持 7 个独立的温度采样点，用于监测芯片内部多个关键位置的热状态。该模块可提供实时温度数据，使系统能够执行动态热管理（Dynamic Thermal Management）及过温保护操作。

**特性**
- 支持系统重启温度阈值配置
- 提供 7 个独立的温度测量点  分别如下：
  - top sensor
  - Vpu sensor
  - Gpu sensor
  - Cluster0 sensor
  - Cluster1 sensor
  - Cluster2 sensor
  - Cluster3 sensor  
- 具备 12 位温度采样精度，实现高精度热监控

#### 2.9.6 脉宽调制接口（PWM）

**产品简介**  
脉宽调制（Pulse Width Modulation, PWM）接口通过数字信号实现对模拟电路及外设的精确控制。该接口支持可编程波形生成，频率、占空比和相位均可调节，适用于电机控制、LED 调光、音频调制等多种应用场景。

**特性**
- 通道：K3 包含 20 路独立 PWM 通道（PWM0–PWM19），每路均配备专属配置寄存器  
- 独立控制能力：  
  - 每个通道可独立运行，并通过多功能引脚输出 PWM 信号  
- 时序控制：  
  - 可单独控制每个 PWM 输出的上升沿和下降沿时序  
  - 支持 连续模式运行 或 动态可调波形，灵活适配不同应用需求  
- 频率与占空比：  
  - 频率范围：195.3 Hz 至 12.8 MHz  
  - 支持 50% 固定占空比；其他占空比值取决于所选频率下的分辨率  
- 计数器与分频器：  
  - 6 位时钟分频器和10位周期计数器，用于精细的频率控制  
  - 15 位脉冲计数器，用于高精度脉冲生成  
- 省电功能：  
  - 支持省电模式，可通过停止通道的内部时钟（`PSCLK_PWM`）并将输出（`PWM_OUT`）保持在恒定的高电平或低电平状态，从而在不需要PWM输出时降低功耗  

#### 2.9.7 邮箱（Mailbox）

**简介**  
邮箱（Mailbox）模块提供一种 片上多处理器间通信机制，支持不同处理器高效地交换消息。

**特性**
- 每个实例支持四个邮箱通道和两个用户
- 每个邮箱通道配备一个 8 × 32 位 FIFO
- 提供独立的阈值寄存器，用于生成新消息和非空中断  
- 每个邮箱通道的消息方向（发送/接收）可通过软件灵活配置

**模块框图**  
Mailbox 架构如下图所示：
<img src="static/mailbox_block_diagram.png" alt="" width="800">

#### 2.9.8 自旋锁（Spinlock）

**简介**  
自旋锁是一种用于多核系统的硬件同步机制。它可以防止同时访问共享资源，从而确保数据一致性。

**特性**
- 每个 Spinlock 实例支持 32 个独立锁单元（Lock Units）  
- 支持两种锁状态：已锁定（Locked） 与 未锁定（Unlocked） 

#### 2.9.9 通用输入输出（GPIO）

**简介**  
K3 提供通用输入输出（General-Purpose Input/Output, GPIO）端口，用于生成或捕获应用特定的数字信号。这些端口通过 复用功能选择器（Alternate Function Muxing） 接入系统，由 GPIO 控制单元统一管理其配置与状态。

**特性**
- 配置为 输入模式 的 GPIO 端口可作为 中断源
- 系统复位后，所有 GPIO 端口默认配置为输入，直到被启动过程或用户软件更改  
- 每个 GPIO 端口都有专用的控制信号  
- 支持基于 上升沿、下降沿或双边沿 触发的 独立中断配置  
- 可以单独设置或清除 GPIO 端口的输出  
- 可以单独读取 GPIO 端口的输入  

#### 2.9.10 超时监控器（Time-Out Monitor, TOM）

**简介**  
超时监控器（Time-Out Monitor, TOM）是一个 AXI 总线事件检测模块，用于监控 AXI 事务，并识别系统组件间数据传输过程中可能出现的 超时异常。

**特性**
- 可配置的超时阈值，用于灵活检测停滞的总线事务  
- 检测到超时事件触发时 可编程的自动响应行为 
- 调试支持：捕获 第一个超时事务的地址与 ID 以进行分析  
- 可配置的 AW/ARREADY 信号监控，以确保总线事务的可靠性与完整性  

### 2.10 时钟与复位（Clock & Reset）

#### 2.10.1 简介

K3 集成了多种片上时钟源与复位控制机制，以支持多样化的运行场景，在 灵活性、稳定性与能效 之间实现优异平衡。

K3 提供以下基础时钟源：
- 1 路 24 MHz 晶振时钟（OSC） 
- 1 路 32.768 kHz 实时时钟（RTC） 
- 1 路 3 MHz 晶振时钟（OSC）
- 1 路 1 MHz 晶振时钟（OSC）

#### 2.10.2 特性

- 集成 8 个锁相环（PLL），为不同系统模块提供丰富的频率选项  
- 支持 动态电压与频率调节（DVFS），实现性能与功耗的最优平衡  
- 支持 无毛刺（Glitch-Free）时钟切换 与 可编程时钟分频器，在降低 PLL 资源占用的同时高效生成所需频率  
- 精细的时钟门控和软件控制的复位机制，可提高节能效果并实现灵活的系统管理

#### 2.10.3  时钟系统

K3 SoC 集成了 8 个锁相环（PLL），为各类模块及 CPU 核心提供稳定、可配置的频率源。每个 PLL 均可通过主 PMU 寄存器进行编程控制，并针对 低抖动 与 快速锁定时间 进行优化。

- **PLL1**：用于为 CPU 内核和系统外设生成固定频率点  
- **PLL2**：用于生成多种固定频率，与 PLL1 相辅相成，为外设模块提供全方位的时钟源  
- **PLL3**：为 CPU 内核 0 的频率缩放和动态切换提供时钟频率  
- **PLL4**：为 CPU 内核 1 的频率缩放和切换提供时钟频率  
- **PLL5**：为 CPU 内核 2 的频率缩放和切换提供时钟频率  
- **PLL6**：生成额外的固定频率，与 PLL1 一起扩展系统时钟的灵活性  
- **PLL7**：生成补充固定频率，以支持各种系统和外设模块  
- **PLL8**：为 CPU Core 3 的频率缩放和动态切换提供时钟频率  

#### 2.10.4 资源复位方案  

K3 支持多种资源复位策略，如下表所示：

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-size: 14px;">
  <colgroup>
    <col width="100">
    <col width="300">
    <col width="600">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="text-align: center;">编号</th>
      <th style="text-align: center;">复位方案</th>
      <th style="text-align: left;">说明</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- Row 1 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">1</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">上电复位<br>（Power-On-Reset）</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">在芯片上电过程中对整个 SoC 执行复位</td>
    </tr>
    <!-- Row 2 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">2</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">看门狗复位<br>（WatchDog Reset）</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">复位整个芯片，但保留 引脚复用（Pinmux）寄存器 和 调试寄存器</td>
    </tr>
    <!-- Row 3 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">3</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">模块级软件复位<br>（Module Software Reset）</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">通过软件对各功能模块进行独立复位</td>
    </tr>
    <!-- Row 4 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">4</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">电源岛上电复位<br>（Power Island POR Reset）</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">在特定电源岛上电时，对该电源岛内所有逻辑执行复位</td>
    </tr>
  </tbody>
</table>

### 2.11 启动模式（Boot Mode）

#### 2.11.1 简介

K3 平台支持多种启动方式：
1. 在线下载启动（Online Download）：通过标准通信协议下载并启动 Bootloader  
2. 本地存储启动（Local Boot）：从本地存储介质加载并启动 Bootloader  

启动模式由 Boot Strap 引脚 的配置决定。

#### 2.11.2 特性

K3 平台支持两类启动模式：

1. 下载模式（Download Mode）
   用于固件下载、调试或测试。在此模式下，设备通过有线接口与主机通信，依据预定义协议接收数据并完成系统初始化。

   支持的下载模式包括：

    - USB Fastboot 模式：通过 USB 2.0 接口，使用 Fastboot 协议连接主机  
    - UART Xmodem 模式：通过 UART 接口，使用 Xmodem 或 Xmodem-1K 协议连接主机  

2. 正常启动模式（Normal Boot Mode）  
   当有效镜像已预置在存储介质中时，系统可直接从指定设备启动。K3 支持从以下存储设备加载 Bootloader：  
   - SD 卡  
   - eMMC  
   - SPI NOR Flash  
   - SPI NAND Flash  
   - UFS  

启动优先级：  
K3 始终优先尝试从 SD 卡启动。  
若未检测到 SD 卡，或 SD 卡中无有效 Bootloader 镜像，系统将自动回退至 次级启动设备。  
次级启动设备可通过 Boot Strap 引脚 配置选择。

K3 使用 4 个 Boot Strap 引脚（GPIO_69、GPIO_68、GPIO_66、GPIO_65）组合选择启动模式，具体映射如下：

| Download Select<br>GPIO_69 | Download Mode<br>GPIO_68 | Boot Select 1<br>GPIO_66 | Boot Select 0<br>GPIO_65 | 启动模式 |
| --- | --- | --- | --- | --- |
| 1 | 0 | x | x | USB Fastboot |
| 1 | 1 | x | x | UART Xmodem |
| 0 | x | 0 | 0 | SD Card → eMMC |
| 0 | x | 0 | 1 | SD Card → SPI NOR |
| 0 | x | 1 | 0 | SD Card → SPI NAND |
| 0 | x | 1 | 1 | SD Card → UFS |

> **注意**：表中 “x” 表示该引脚状态 不影响 启动模式选择。

## 3. 封装（Package）

### 3.1 概述

K3 提供以下封装选项：

| 封装类型 | 尺寸 | 引脚间距 (Pitch) | 引脚数量 (阵列) |
| --- | --- | --- | --- |
| **FBGA** | 27×27 mm | 0.650 mm | 1563 (40×40) |

相关封装外形图（Package Outline Drawing, POD）详见下节。

### 3.2 封装外形图（POD）

<img src="static/package1.png" alt="" width="500">

<img src="static/package2.png" alt="" width="800">

### 3.3 Part Number

下图给出了 K3 Part Number 的组成及字段定义。

<img src="static/k3_partno.png" alt="" width="800">

## 4. 引脚定义（Pinout）

### 4.1 引脚分布图与说明

K3 的完整引脚分布图如下所示：
<img src="static/k3_pinmap.png" alt="" width="900">

为便于描述，K3 的引脚按 四个象限（Quadrant） 进行划分。以下各小节将基于该分区方式，详细说明各引脚的功能定义。

#### 4.1.1 (A~Y, 1~20)

<img src="static/k3_pinmap_a-y_1-20.png" alt="" width="800">
  
| 引脚编号 | 引脚名称 | 引脚编号 | 引脚名称 |
| --- | --- | --- | --- |
| A2 | VSS | K20 | AVDD08_PCIE1 |
| A3 | DDR1_DQ_B_08 | L1 | DDR1_CKT_B |
| A4 | DDR1_DMI1_B | L2 | DDR1_CKC_B |
| A5 | DDR1_DQ_B_09 | L3 | VSS |
| A6 | AVSS_PCIEUSB | L4 | VSS |
| A7 | PCIE5_TX0N | L5 | VSS |
| A8 | AVSS_PCIEUSB | L6 | VSS |
| A9 | PCIE4/USB3-D_TX0N | L7 | DDR1_CA_A_01 |
| A10 | AVSS_PCIEUSB | L8 | VSS |
| A11 | PCIE3/USB3-C_TX0N | L9 | VSS |
| A12 | AVSS_PCIEUSB | L10 | VSS |
| A13 | PCIE2/USB3-B_TX0N | L11 | VSS |
| A14 | AVSS_PCIEUSB | L12 | VSS |
| A15 | PCIE1_TX1P | L13 | VSS |
| A16 | AVSS_PCIEUSB | L14 | AVSS_PCIEUSB |
| A17 | PCIE1_TX0N | L15 | AVSS_PCIEUSB |
| A18 | AVSS_PCIEUSB | L16 | AVSS_PCIEUSB |
| A19 | PCIE0_TX1P | L17 | AVSS_PCIEUSB |
| A20 | AVSS_PCIEUSB | L18 | AVSS_PCIEUSB |
| B1 | VSS | L19 | AVDD08_PCIE3/USB3-C |
| B2 | VSS | L20 | AVDD08_PCIE2/USB3-B |
| B3 | VSS | M1 | DDR1_CKT_A |
| B4 | DDR1_DQ_B_11 | M2 | DDR1_CKC_A |
| B5 | DDR1_DQ_B_10 | M3 | VSS |
| B6 | AVSS_PCIEUSB | M4 | DDR1_DQ_A_00 |
| B7 | PCIE5_TX0P | M5 | DDR1_DQ_A_02 |
| B8 | PCIE5_REFCLK_N | M6 | VSS |
| B9 | PCIE4/USB3-D_TX0P | M7 | DDR1_CA_A_00 |
| B10 | PCIE4_REFCLK_P | M8 | VDDQ_DDR |
| B11 | PCIE3/USB3-C_TX0P | M9 | VSS |
| B12 | PCIE3_REFCLK_N | M10 | VDD0V8_DDR |
| B13 | PCIE2/USB3-B_TX0P | M11 | AVDD18_PLL_DDR1 |
| B14 | PCIE2_REFCLK_P | M12 | VSS |
| B15 | PCIE1_TX1N | M13 | VSS |
| B16 | PCIE1_REFCLK_P | M14 | VSS |
| B17 | PCIE1_TX0P | M15 | VSS |
| B18 | USB20_B_USB_P | M16 | VSS |
| B19 | PCIE0_TX1N | M17 | VSS |
| B20 | PCIE0_REFCLK_P | M18 | AVSS_PCIEUSB |
| C1 | DDR1_DQ_B_00 | M19 | VSS |
| C2 | DDR1_DQ_B_02 | M20 | AVDD08_PCIE2/USB3-B |
| C3 | VSS | N1 | DDR1_DQ_A_15 |
| C4 | DDR1_DQS1_T_B | N2 | DDR1_DQ_A_14 |
| C5 | DDR1_DQS1_C_B | N3 | VSS |
| C6 | DDR1_ZN | N4 | DDR1_DQ_A_01 |
| C7 | AVSS_PCIEUSB | N5 | DDR1_DQ_A_03 |
| C8 | PCIE5_REFCLK_P | N6 | VSS |
| C9 | AVSS_PCIEUSB | N7 | DDR1_CKE0_A |
| C10 | PCIE4_REFCLK_N | N8 | VSS |
| C11 | AVSS_PCIEUSB | N9 | VDD0V8_DDR |
| C12 | PCIE3_REFCLK_P | N10 | VSS |
| C13 | AVSS_PCIEUSB | N11 | AVDD08_PLL_DDR1 |
| C14 | PCIE2_REFCLK_N | N12 | VSS |
| C15 | AVSS_PCIEUSB | N13 | VCC_SYS |
| C16 | PCIE1_REFCLK_N | N14 | VSS |
| C17 | AVSS_PCIEUSB | N15 | VCC_SYS |
| C18 | USB20_B_USB_M | N16 | VSS |
| C19 | AVSS_PCIEUSB | N17 | VCC_SYS |
| C20 | PCIE0_REFCLK_N | N18 | VSS |
| D1 | DDR1_DQ_B_03 | N19 | VCC_SYS |
| D2 | DDR1_DQ_B_01 | N20 | VSS |
| D3 | VSS | P1 | DDR1_DQ_A_13 |
| D4 | VSS | P2 | DDR1_DQ_A_12 |
| D5 | VSS | P3 | VSS |
| D6 | DDR1_CKE1_B | P4 | DDR1_DQS0_C_A |
| D7 | DDR1_CA_B_00 | P5 | DDR1_DQS0_T_A |
| D8 | AVSS_PCIEUSB | P6 | VSS |
| D9 | PCIE5_RX0P | P7 | DDR1_CS1_A |
| D10 | AVSS_PCIEUSB | P8 | VDDQ_DDR |
| D11 | USB20_D_USB_P | P9 | VSS |
| D12 | AVSS_PCIEUSB | P10 | VDD0V8_DDR |
| D13 | PCIE4/USB3-D_RX0N | P11 | VSS |
| D14 | AVSS_PCIEUSB | P12 | VSS |
| D15 | PCIE3/USB3-C_RX0N | P13 | VSS |
| D16 | AVSS_PCIEUSB | P14 | VCC_SYS |
| D17 | PCIE2/USB3-B_RX0P | P15 | VSS |
| D18 | AVSS_PCIEUSB | P16 | VCC_SYS |
| D19 | PCIE1_RX0P | P17 | VSS |
| D20 | AVSS_PCIEUSB | P18 | VCC_SYS |
| E1 | DDR1_WCK_T_B_0 | P19 | VSS |
| E2 | DDR1_WCK_C_B_0 | P20 | VCC_SYS |
| E3 | VSS | R1 | DDR1_WCK_C_A_1 |
| E4 | DDR1_WCK_T_B_1 | R2 | DDR1_WCK_T_A_1 |
| E5 | DDR1_WCK_C_B_1 | R3 | VSS |
| E6 | VSS | R4 | VSS |
| E7 | DDR1_CS1_B | R5 | VSS |
| E8 | VSS | R6 | VSS |
| E9 | PCIE5_RX0N | R7 | VDDQ_DDR |
| E10 | AVSS_PCIEUSB | R8 | VSS |
| E11 | USB20_D_USB_M | R9 | VDD0V8_DDR |
| E12 | AVSS_PCIEUSB | R10 | VSS |
| E13 | PCIE4/USB3-D_RX0P | R11 | VSS |
| E14 | AVSS_PCIEUSB | R12 | VSS |
| E15 | PCIE3/USB3-C_RX0P | R13 | VCC_SYS |
| E16 | AVSS_PCIEUSB | R14 | VSS |
| E17 | PCIE2/USB3-B_RX0N | R15 | VCC_SYS |
| E18 | AVSS_PCIEUSB | R16 | VSS |
| E19 | PCIE1_RX0N | R17 | VCC_SYS |
| E20 | AVSS_PCIEUSB | R18 | VSS |
| F1 | DDR1_DQS0_T_B | R19 | VCC_SYS |
| F2 | DDR1_DQS0_C_B | R20 | VSS |
| F3 | VSS | T1 | DDR1_DQS1_C_A |
| F4 | DDR1_DQ_B_12 | T2 | DDR1_DQS1_T_A |
| F5 | VSS | T3 | VSS |
| F6 | VSS | T4 | DDR1_WCK_C_A_0 |
| F7 | DDR1_CKE0_B | T5 | DDR1_WCK_T_A_0 |
| F8 | VSS | T6 | VSS |
| F9 | VSS | T7 | DDR1_CKE1_A |
| F10 | AVDD18_PCIE5 | T8 | VDDQ_DDR |
| F11 | AVDD18_PCIE4/USB3-D | T9 | VSS |
| F12 | AVSS_PCIEUSB | T10 | VDD0V8_DDR |
| F13 | AVDD18_B_USB20 | T11 | VSS |
| F14 | PCIE_USB_COMBO_ADTEST_0 | T12 | VCC_SYS |
| F15 | AVDD18_USB20_HOST | T13 | VSS |
| F16 | USB20_C_USB_M | T14 | VCC_SYS |
| F17 | AVSS_PCIEUSB | T15 | VSS |
| F18 | PCIE1_RX1N | T16 | VCC_SYS |
| F19 | AVSS_PCIEUSB | T19 | VSS |
| F20 | AVDD33_D_USB20 | T20 | VCC_SYS |
| G1 | DDR1_DMI0_B | U1 | DDR1_DMI1_A |
| G2 | VSS | U2 | DDR1_DQ_A_11 |
| G3 | VSS | U3 | VSS |
| G4 | DDR1_DQ_B_13 | U4 | DDR1_DMI0_A |
| G5 | DDR1_DQ_B_15 | U5 | DDR1_DQ_A_04 |
| G6 | VSS | U6 | VSS |
| G7 | DDR1_CA_B_01 | U7 | DDR1_CS0_A_CA06 |
| G8 | VSS | U8 | VSS |
| G9 | VSS | U9 | VDD0V8_DDR |
| G10 | AVDD18_PCIE5 | U10 | VSS |
| G11 | AVDD18_PCIE4/USB3-D | U11 | VSS |
| G12 | AVDD18_C_USB20 | U12 | VSS |
| G13 | AVDD18_PCIE1 | U13 | VCC_SYS |
| G14 | AVDD18_PCIE1 | U14 | VSS |
| G15 | AVSS_PCIEUSB | U15 | VCC_SYS |
| G16 | USB20_C_USB_P | U16 | VSS |
| G17 | AVDD18_PCIE0 | U19 | VCC_SYS |
| G18 | PCIE1_RX1P | U20 | VSS |
| G19 | AVSS_PCIEUSB | V1 | DDR1_DQ_A_10 |
| G20 | AVDD33_C_USB20 | V2 | DDR1_DQ_A_09 |
| H1 | DDR1_DQ_B_05 | V3 | VSS |
| H2 | DDR1_DQ_B_04 | V4 | DDR1_DQ_A_07 |
| H3 | VSS | V5 | DDR1_DQ_A_05 |
| H4 | DDR1_DQ_B_14 | V6 | VSS |
| H5 | DDR1_CA_B_03 | V7 | DDR1_CA_A_05 |
| H6 | VSS | V8 | VDDQ_DDR |
| H7 | DDR1_CA_B_02 | V9 | VSS |
| H8 | VSS | V10 | VDD0V8_DDR |
| H9 | VSS | V11 | VSS |
| H10 | VSS | V12 | VCC_SYS |
| H11 | AVSS_PCIEUSB | V13 | VSS |
| H12 | AVSS_PCIEUSB | V14 | VCC_SYS |
| H13 | AVDD18_PCIE3/USB3-C | V15 | VSS |
| H14 | AVDD18_PCIE1 | V16 | VCC_SYS |
| H15 | PCIE_USB_COMBO_ADTEST_1 | V19 | VSS |
| H16 | AVDD18_PCIE0 | V20 | VCC_SYS |
| H17 | AVDD18_PCIE0 | W1 | DDR1_DQ_A_08 |
| H18 | AVDD08_D_USB20 | W2 | VSS |
| H19 | AVDD08_C_USB20 | W3 | VSS |
| H20 | AVSS_PCIEUSB | W4 | DDR1_DQ_A_06 |
| J1 | DDR1_DQ_B_07 | W5 | VSS |
| J2 | DDR1_DQ_B_06 | W6 | VSS |
| J3 | VSS | W7 | VSS |
| J4 | DDR1_CA_A_03 | W8 | VDDQ_DDR |
| J5 | DDR1_CA_B_04 | W9 | VSS |
| J6 | VSS | W10 | VDD2H_DDR |
| J7 | DDR1_CS0_B_CA06 | W11 | VAA18_VDD2H_DDR |
| J8 | VSS | W12 | VSS |
| J9 | VSS | W13 | VCC_SYS |
| J10 | VSS | W14 | VSS |
| J11 | VSS | W15 | VCC_SYS |
| J12 | AVDD18_D_USB20 | W16 | VSS |
| J13 | AVDD18_PCIE3/USB3-C | W17 | VSS |
| J14 | AVSS_PCIEUSB | W18 | VCC_SYS |
| J15 | AVDD18_PCIE2/USB3-B | W19 | VCC_SYS |
| J16 | AVSS_PCIEUSB | W20 | VSS |
| J17 | AVDD08_PCIE5 | Y1 | DDR1_RESET_N |
| J18 | AVDD08_PCIE4/USB3-D | Y2 | DDR1_PWROK |
| J19 | AVDD08_PCIE1 | Y3 | VSS |
| J20 | AVDD08_PCIE1 | Y4 | DDR1_DTO |
| K1 | VSS | Y5 | DDR1_ATO |
| K2 | VSS | Y6 | VSS |
| K3 | VSS | Y7 | VSS |
| K4 | DDR1_CA_A_02 | Y8 | VSS |
| K5 | DDR1_CA_A_04 | Y9 | VDDQ_DDR |
| K6 | VSS | Y10 | VDD2H_DDR |
| K7 | DDR1_CA_B_05 | Y11 | VAA18_VDD2H_DDR |
| K8 | VDDQ_DDR | Y12 | VCC_SYS |
| K9 | VSS | Y13 | VSS |
| K10 | VSS | Y14 | VCC_SYS |
| K11 | VSS | Y15 | VSS |
| K12 | AVSS_PCIEUSB | Y16 | VCC_SYS |
| K13 | AVSS_PCIEUSB | Y17 | VSS |
| K14 | AVSS_PCIEUSB | Y18 | VCC_SYS |
| K15 | AVDD18_PCIE2/USB3-B | Y19 | VSS |
| K16 | AVSS_PCIEUSB | Y20 | VCC_SYS |
| K17 | AVDD08_PCIE5 | — | — |
| K18 | AVDD08_PCIE4/USB3-D | — | — |
| K19 | AVDD08_PCIE3/USB3-C | — | — |

#### 4.1.2 (A~Y, 21~40)

<img src="static/k3_pinmap_a-y_21-40.png" alt="" width="800">

| 引脚编号 | 引脚名称 | 引脚编号 | 引脚名称 |
| --- | --- | --- | --- |
| A21 | PCIE0_TX0N | L21 | AVDD08_PCIE0 |
| A22 | AVSS_PCIEUSB | L22 | AVDD08_B_USB20 |
| A23 | UCIE_EW_TXDATA_M0[2] | L23 | AVSS_PCIEUSB |
| A24 | VSS_UCIE | L24 | AVSS_PCIEUSB |
| A25 | UCIE_EW_TXCKN_M0 | L25 | UCIE_VDDBH_0V9 |
| A26 | UCIE_EW_TXDATA_M0[8] | L26 | UCIE_VCCPLL_1P2V |
| A27 | VSS_UCIE | L27 | VSS_UCIE |
| A28 | UCIE_EW_RXCKP_M0 | L28 | UCIE_VCCIO_0V8 |
| A29 | UCIE_EW_RXCKSB_M0 | L29 | VSS_UCIE |
| A30 | VSS_UCIE | L30 | VSS_UCIE |
| A31 | UCIE_EW_RXDATA_M0[7] | L31 | AVSS_OSCPLL234567 |
| A32 | UCIE_EW_RXDATA_M0[2] | L32 | VSS |
| A33 | VSS_UCIE | L33 | VSS |
| A34 | GPIO[2]_21 | L34 | GPIO[3]_45 |
| A35 | GPIO[2]_25 | L35 | GPIO[3]_50 |
| A36 | GPIO[2]_29 | L36 | VSS |
| A37 | GPIO[2]_32 | L37 | GPIO[3]_57 |
| A38 | GPIO[2]_34 | L38 | GPIO[3]_60 |
| A39 | VSS | L39 | GPIO[3]_66 |
| B21 | PCIE0_TX0P | L40 | GPIO[3]_72 |
| B22 | USB20_HOST_M | M21 | AVSS_PCIEUSB |
| B23 | UCIE_EW_TXDATA_M0[5] | M22 | AVSS_PCIEUSB |
| B24 | UCIE_EW_TXDATA_M0[3] | M23 | AVSS_USB20_HOST |
| B25 | VSS_UCIE | M24 | AVSS_PCIEUSB |
| B26 | UCIE_EW_TXCKP_M0 | M25 | VSS |
| B27 | UCIE_EW_TXDATA_M0[14] | M26 | UCIE_VDDVPH0_0V9 |
| B28 | VSS_UCIE | M27 | UCIE_VDDVPH0_0V9 |
| B29 | UCIE_EW_RXCKN_M0 | M28 | VCC_SYS |
| B30 | UCIE_EW_RXDATA_M0[15] | M29 | VSS |
| B31 | VSS_UCIE | M30 | VCC_SYS |
| B32 | UCIE_EW_RXDATA_M0[5] | M31 | AVSS_OSCPLL234567 |
| B33 | VSS | M32 | VSS |
| B34 | GPIO[2]_22 | M33 | VSS |
| B35 | GPIO[2]_26 | M34 | GPIO[3]_46 |
| B36 | GPIO[2]_30 | M35 | GPIO[3]_51 |
| B37 | VSS | M36 | GPIO[3]_58 |
| B38 | GPIO[2]_33 | M37 | VSS |
| B39 | GPIO[2]_38 | M38 | GPIO[3]_61 |
| B40 | VSS | M39 | GPIO[3]_67 |
| C21 | AVSS_PCIEUSB | M40 | GPIO[3]_73 |
| C22 | USB20_HOST_P | N21 | VCC_SYS |
| C23 | VSS_UCIE | N22 | VSS |
| C24 | UCIE_EW_TXDATA_M0[4] | N23 | VCC_SYS |
| C25 | UCIE_EW_TXTRK_M0 | N24 | VSS |
| C26 | VSS_UCIE | N25 | VCC_SYS |
| C27 | UCIE_EW_TXDATA_M0[11] | N26 | VSS |
| C28 | UCIE_EW_RXDATA_M0[11] | N27 | VCC_SYS |
| C29 | VSS_UCIE | N28 | VSS |
| C30 | UCIE_EW_RXDATA_M0[12] | N29 | VCC_SYS |
| C31 | UCIE_EW_RXTRK_M0 | N30 | VSS |
| C32 | VSS_UCIE | N31 | VCC_SYS |
| C33 | VSS | N32 | VSS |
| C34 | GPIO[2]_23 | N33 | DTEST_PAD |
| C35 | GPIO[2]_27 | N34 | ATEST_PAD |
| C36 | GPIO[2]_31 | N35 | GPIO[3]_52 |
| C37 | GPIO[2]_35 | N38 | GPIO[3]_62 |
| C38 | GPIO[2]_36 | N39 | VSS |
| C39 | VSS | N40 | GPIO[3]_74 |
| C40 | GPIO[2]_40 | P21 | VSS |
| D21 | PCIE0_RX1P | P22 | VCC_SYS |
| D22 | AVSS_PCIEUSB | P23 | VSS |
| D23 | UCIE_EW_TXDATA_M0[0] | P24 | VCC_SYS |
| D24 | VSS_UCIE | P25 | VSS |
| D25 | UCIE_EW_TXVLD_M0 | P26 | VCC_SYS |
| D26 | UCIE_EW_TXDATA_M0[12] | P27 | VSS |
| D27 | VSS_UCIE | P28 | VCC_SYS |
| D28 | UCIE_EW_RXDATA_M0[10] | P29 | VSS |
| D29 | UCIE_EW_RXDATA_M0[14] | P30 | VCC_SYS |
| D30 | VSS_UCIE | P31 | VSS |
| D31 | UCIE_EW_RXDATA_M0[6] | P32 | VSS |
| D32 | UCIE_EW_RXDATA_M0[1] | P33 | VSS |
| D33 | VSS | P34 | VSS |
| D34 | VSS | P35 | VSS |
| D35 | GPIO[2]_28 | P36 | VSS |
| D38 | GPIO[2]_37 | P37 | EMMC_DS |
| D39 | GPIO[2]_39 | P38 | GPIO[3]_63 |
| D40 | GPIO[2]_41 | P39 | GPIO[3]_68 |
| E21 | PCIE0_RX1N | P40 | GPIO[3]_75 |
| E22 | AVSS_PCIEUSB | R21 | VCC_SYS |
| E23 | UCIE_EW_TXDATASB_M0 | R22 | AVDD08_OSC |
| E24 | UCIE_EW_O_CKNT | R23 | AVDD18_OSC |
| E25 | VSS_UCIE | R24 | AVSS_OSCPLL234567 |
| E26 | UCIE_EW_TXCKSB_M0 | R25 | VCC_SYS |
| E27 | UCIE_EW_TXDATA_M0[13] | R26 | VSS |
| E28 | VSS_UCIE | R27 | VCC_SYS |
| E29 | UCIE_EW_RXDATA_M0[8] | R28 | VSS |
| E30 | UCIE_EW_RXDATA_M0[9] | R29 | VCC_SYS |
| E31 | VSS_UCIE | R30 | VSS |
| E32 | UCIE_EW_RXDATASB_M0 | R31 | VSS |
| E33 | VSS | R32 | VCC18_GPIO2 |
| E34 | GPIO[2]_24 | R33 | VCC18_GPIO2 |
| E35 | PMIC_INT_N | R34 | VSS |
| E36 | PWR_SSP_SCLK | R35 | VSS |
| E37 | PMIC_WDT_N | R36 | EMMC_CLK |
| E38 | PRI_TDO | R37 | EMMC_CMD |
| E39 | PRI_TRST_N | R38 | VSS |
| E40 | PWR_SSP_TXD | R39 | EMMC_D5 |
| F21 | AVSS_PCIEUSB | R40 | EMMC_D3 |
| F22 | PCIE0_RX0P | T21 | VSS |
| F23 | VSS_UCIE | T22 | AVDD08_PLL234 |
| F24 | UCIE_EW_O_CKPT | T23 | AVSS_OSCPLL234567 |
| F25 | UCIE_EW_TXDATA_M0[7] | T24 | VCC_SYS |
| F26 | VSS_UCIE | T25 | VSS |
| F27 | UCIE_EW_TXDATA_M0[9] | T26 | VCC_SYS |
| F28 | UCIE_EW_TXDATA_M0[15] | T30 | VCC_SYS |
| F29 | VSS_UCIE | T31 | VSS |
| F30 | UCIE_EW_RXVLD_M0 | T32 | VCC1833_GPIO2 |
| F31 | UCIE_EW_RXDATA_M0[3] | T33 | VCC1833_GPIO2 |
| F32 | VSS_UCIE | T34 | AVDD18_FUSE |
| F33 | VSS | T35 | VSS |
| F34 | PRI_TMS | T36 | EMMC_D4 |
| F35 | VSS | T37 | EMMC_D1 |
| F36 | PWR_SSP_RXD | T38 | EMMC_D6 |
| F37 | EXT_32K_IN | T39 | EMMC_D2 |
| F38 | PWR_SCL | T40 | EMMC_D7 |
| F39 | PRI_TDI | U21 | VCC_SYS |
| F40 | VSS | U22 | PCIE/USB3_RCAL |
| G21 | AVDD33_USB20_HOST | U23 | AVDD18_PLL234 |
| G22 | PCIE0_RX0N | U24 | VSS |
| G23 | VSS_UCIE | U25 | VCC_SYS |
| G24 | VSS_UCIE | U26 | VSS |
| G25 | UCIE_EW_TXDATA_M0[6] | U30 | VSS |
| G26 | UCIE_EW_TXDATA_M0[1] | U31 | VCC_SYS |
| G27 | VSS_UCIE | U32 | VCC18_PMIC |
| G28 | UCIE_EW_TXDATA_M0[10] | U33 | VCC18_PMIC |
| G29 | UCIE_EW_RXDATA_M0[13] | U34 | VSS |
| G30 | VSS_UCIE | U35 | VSS |
| G31 | UCIE_EW_RXDATA_M0[4] | U36 | VSS |
| G32 | UCIE_EW_RXDATA_M0[0] | U37 | VSS |
| G33 | VSS | U38 | EMMC_D0 |
| G34 | PRI_TCK | U39 | VSS |
| G35 | VCXO_EN | U40 | VSS |
| G38 | PWR_SDA | V21 | VSS |
| G39 | RESET_IN_N | V22 | AVDD18_PLL567 |
| G40 | PWR_SSP_FRM | V23 | AVDD08_PLL567 |
| H21 | AVDD33_B_USB20 | V24 | VCC_SYS |
| H22 | AVSS_PCIEUSB | V25 | VSS |
| H23 | AVSS_PCIEUSB | V26 | VCC_SYS |
| H24 | VSS_UCIE | V27 | VSS |
| H25 | UCIE_EW_ATEST | V28 | VCC_SYS |
| H26 | UCIE_BGR_EAREFCLKN | V29 | VSS |
| H27 | UCIE_VDD_0V8 | V30 | VCC_SYS |
| H28 | UCIE_EW_VCTRL_EXT | V31 | VSS |
| H29 | VSS_UCIE | V32 | VCC18_GPIO3 |
| H30 | VSS_UCIE | V33 | VCC18_GPIO3 |
| H31 | VSS_UCIE | V34 | VSS |
| H32 | VSS_UCIE | V35 | VSS |
| H33 | VSS | V36 | MIPI_CSI2_D3N |
| H34 | GPIO[3]_42 | V37 | MIPI_CSI2_D3P |
| H35 | GPIO[3]_47 | V38 | AVSS_MIPI012 |
| H36 | GPIO[3]_53 | V39 | MIPI_CSI2_D2N |
| H37 | GPIO[3]_55 | V40 | MIPI_CSI2_D2P |
| H38 | GPIO[3]_54 | W21 | VCC_SYS |
| H39 | VSS | W22 | VSS |
| H40 | GPIO[3]_69 | W23 | VCC_SYS |
| J21 | AVDD08_PCIE0 | W24 | VSS |
| J22 | AVSS_PCIEUSB | W25 | VCC_SYS |
| J23 | AVSS_PCIEUSB | W26 | VCC_SYS |
| J24 | UCIE_VCCAON_0V8 | W27 | VCC_SYS |
| J25 | UCIE_VCCAON_0V8 | W28 | VSS |
| J26 | UCIE_BGR_EAREFCLKP | W29 | VCC_SYS |
| J27 | UCIE_VDD_0V8 | W30 | VSS |
| J28 | VSS_UCIE | W31 | VCC_SYS |
| J29 | UCIE_VCCIO_0V8 | W32 | AVDD08_EMMC |
| J30 | VSS_UCIE | W33 | AVDD08_EMMC |
| J31 | VSS_UCIE | W34 | VSS |
| J32 | XI_PAD | W35 | VSS |
| J33 | AVSS_OSCPLL234567 | W36 | AVSS_MIPI012 |
| J34 | GPIO[3]_43 | W37 | AVSS_MIPI012 |
| J35 | GPIO[3]_48 | W38 | MIPI_CSI3_CLKN |
| J36 | VSS | W39 | MIPI_CSI3_CLKP |
| J37 | GPIO[3]_56 | W40 | AVSS_MIPI012 |
| J38 | GPIO[3]_59 | Y21 | VSS |
| J39 | GPIO[3]_64 | Y22 | VCC_SYS |
| J40 | GPIO[3]_70 | Y23 | VSS |
| K21 | AVDD08_PCIE0 | Y24 | VCC_SYS |
| K22 | AVDD08_USB20_HOST | Y25 | VCC_SYS |
| K23 | AVSS_PCIEUSB | Y26 | VCC_SYS |
| K24 | AVSS_PCIEUSB | Y27 | VSS |
| K25 | UCIE_VCCAON_0V8 | Y28 | VCC_SYS |
| K26 | UCIE_VCCPLL_1P2V | Y29 | VSS |
| K27 | VSS_UCIE | Y30 | VCC_SYS |
| K28 | UCIE_VCCIO_0V8 | Y31 | VSS |
| K29 | UCIE_VCCIO_0V8 | Y32 | VCC18_EMMC |
| K30 | UCIE_VCCIO_0V8 | Y33 | VCC18_EMMC |
| K31 | VSS_UCIE | Y34 | VSS |
| K32 | XO_PAD | Y35 | VSS |
| K33 | AVSS_OSCPLL234567 | Y36 | MIPI_CSI2_D1P |
| K34 | GPIO[3]_44 | Y37 | MIPI_CSI2_D1N |
| K35 | GPIO[3]_49 | Y38 | AVSS_MIPI012 |
| K38 | VSS | Y39 | MIPI_CSI2_D0P |
| K39 | GPIO[3]_65 | Y40 | MIPI_CSI2_D0N |
| K40 | GPIO[3]_71 | — | — |

#### 4.1.3 (AA~AY, 1~20)

<img src="static/k3_pinmap_aa-ay_1-20.png" alt="" width="800">

| 引脚编号 | 引脚名称 | 引脚编号 | 引脚名称 |
| --- | --- | --- | --- |
| AA1 | DDR0_DQ_B_15 | AL1 | VSS |
| AA2 | VSS | AL2 | VSS |
| AA3 | VSS | AL3 | VSS |
| AA4 | DDR0_ATO | AL4 | VSS |
| AA5 | DDR0_PWROK | AL5 | VSS |
| AA6 | DDR0_DTO | AL6 | VSS |
| AA7 | VSS | AL7 | DDR0_CA_A_05 |
| AA8 | VDDQ_DDR | AL8 | VSS |
| AA9 | VSS | AL9 | VSS |
| AA10 | VDD0V8_DDR | AL10 | AVSS_PLL1 |
| AA11 | VSS | AL11 | AVDD18_DRD_USB |
| AA12 | VSS | AL12 | VSS |
| AA13 | VCC_SYS | AL13 | VSS |
| AA14 | VSS | AL14 | AVSS_DRD |
| AA15 | VCC_SYS | AL15 | AVDD18_EDP1 |
| AA16 | VSS | AL16 | AVDD18_EDP1 |
| AA17 | VCC_SYS | AL17 | AVSS_EDP1 |
| AA18 | VSS | AL18 | VCC_SYS |
| AA19 | VCC_SYS | AL19 | VCC1833_QSPI |
| AA20 | VSS | AL20 | VCC1833_SD |
| AB1 | DDR0_DQ_B_13 | AM1 | DDR0_DQ_A_05 |
| AB2 | DDR0_DQ_B_14 | AM2 | VSS |
| AB3 | VSS | AM3 | VSS |
| AB4 | DDR0_DQ_B_02 | AM4 | DDR0_CA_A_04 |
| AB5 | DDR0_DQ_B_00 | AM5 | VSS |
| AB6 | VSS | AM6 | VSS |
| AB7 | DDR0_CA_B_00 | AM7 | DDR0_CA_A_02 |
| AB8 | VDDQ_DDR | AM8 | VSS |
| AB9 | VDD0V8_DDR | AM9 | AVDD08_DRD_USB |
| AB10 | VSS | AM10 | VSS |
| AB11 | VSS | AM11 | AVDD18_DRD_USB |
| AB12 | VCC_SYS | AM12 | VSS |
| AB13 | VSS | AM13 | AVSS_DRD |
| AB14 | VCC_SYS | AM14 | AVSS_DRD |
| AB15 | VSS | AM15 | VCC12_UFS |
| AB16 | VCC_SYS | AM16 | AVSS_UFS |
| AB17 | VSS | AM17 | AVSS_EDP1 |
| AB18 | VCC_SYS | AM18 | AVSS_EDP1 |
| AB19 | VSS | AM19 | VSS |
| AB20 | VCC_SYS | AM20 | VCC18_QSPI_CAP |
| AC1 | DDR0_DMI1_B | AN1 | DDR0_DQ_A_06 |
| AC2 | DDR0_DQ_B_12 | AN2 | DDR0_DQ_A_07 |
| AC3 | VSS | AN3 | VSS |
| AC4 | DDR0_DQ_B_03 | AN4 | VSS |
| AC5 | DDR0_DQ_B_01 | AN5 | VSS |
| AC6 | VSS | AN6 | VSS |
| AC7 | DDR0_CA_B_01 | AN7 | DDR0_CA_A_01 |
| AC8 | VDDQ_DDR | AN8 | VSS |
| AC9 | VSS | AN9 | AVDD08_DRD_USB |
| AC10 | VDD0V8_DDR | AN10 | VDD08_UFS |
| AC11 | VSS | AN11 | AVDD18_DRD_USB |
| AC12 | VSS | AN12 | VSS |
| AC13 | VCC_SYS | AN13 | AVDD33_DRD_USB |
| AC14 | VSS | AN14 | AVSS_DRD |
| AC15 | VCC_CPUX | AN15 | VCC12_UFS |
| AC16 | VSS | AN16 | AVSS_UFS |
| AC17 | VCC_CPUX | AN17 | AVSS_EDP1 |
| AC18 | VSS | AN18 | AVSS_EDP1 |
| AC19 | VCC_CPUX | AN19 | VSS |
| AC20 | VSS | AN20 | VCC1833_GPIO5 |
| AD1 | DDR0_DQS1_C_B | AP1 | DDR0_DQ_A_04 |
| AD2 | DDR0_DQS1_T_B | AP2 | DDR0_DMI0_A |
| AD3 | VSS | AP3 | VSS |
| AD4 | DDR0_WCK_T_B_0 | AP4 | DDR0_DQ_A_14 |
| AD5 | DDR0_WCK_C_B_0 | AP5 | DDR0_DQ_A_15 |
| AD6 | VSS | AP6 | VSS |
| AD7 | DDR0_CKE0_B | AP7 | DDR0_CA_A_00 |
| AD8 | VDDQ_DDR | AP8 | VSS |
| AD9 | VDD0V8_DDR | AP9 | AVDD08_DRD_USB |
| AD10 | VSS | AP10 | VDD08_UFS |
| AD11 | VSS | AP11 | VSS |
| AD12 | VSS | AP12 | AVDD18_DRD_USB |
| AD13 | VSS | AP13 | AVDD33_DRD_USB |
| AD14 | VCC_SYS | AP14 | AVDD18_UFS |
| AD15 | VSS | AP15 | AVSS_UFS |
| AD16 | VCC_CPUX | AP16 | AVSS_UFS |
| AD17 | VSS | AP17 | EDP1_EXTR |
| AD18 | VCC_CPUX | AP18 | AVSS_EDP1 |
| AD19 | VSS | AP19 | VSS |
| AD20 | VCC_CPUX | AP20 | VCC1833_GPIO5 |
| AE1 | DDR0_WCK_T_B_1 | AR1 | DDR0_WCK_T_A_0 |
| AE2 | DDR0_WCK_C_B_1 | AR2 | DDR0_WCK_C_A_0 |
| AE3 | VSS | AR3 | VSS |
| AE4 | VSS | AR4 | DDR0_DQ_A_12 |
| AE5 | VSS | AR5 | DDR0_DQ_A_13 |
| AE6 | VSS | AR6 | VSS |
| AE7 | DDR0_CA_B_02 | AR7 | DDR0_CKE0_A |
| AE8 | VDDQ_DDR | AR8 | VSS |
| AE9 | VSS | AR9 | AVDD08_DRD_USB |
| AE10 | VDD0V8_DDR | AR10 | AVDD08_DRD_USB |
| AE11 | VSS | AR11 | AVSS_DRD |
| AE12 | VSS | AR12 | AVSS_DRD |
| AE13 | VCC_SYS | AR13 | AVSS_DRD |
| AE14 | VSS | AR14 | AVDD18_UFS |
| AE15 | VCC_CPUX | AR15 | AVSS_UFS |
| AE16 | VSS | AR16 | AVSS_EDP1 |
| AE17 | VCC_CPUX | AR17 | UFS_REF_CLK |
| AE18 | VSS | AR18 | AVSS_EDP1 |
| AE19 | VCC_CPUX | AR19 | QSPI_CLK |
| AE20 | VSS | AR20 | QSPI_DAT3 |
| AF1 | DDR0_DQ_B_09 | AT1 | DDR0_DQS0_C_A |
| AF2 | DDR0_DQ_B_11 | AT2 | DDR0_DQS0_T_A |
| AF3 | VSS | AT3 | VSS |
| AF4 | DDR0_DQS0_C_B | AT4 | DDR0_DQS1_C_A |
| AF5 | DDR0_DQS0_T_B | AT5 | DDR0_DQS1_T_A |
| AF6 | VSS | AT6 | VSS |
| AF7 | DDR0_CKE1_B | AT7 | DDR0_CKE1_A |
| AF8 | VDDQ_DDR | AT8 | VSS |
| AF9 | VDD0V8_DDR | AT9 | AVDD08_DRD_USB |
| AF10 | VSS | AT10 | USB_PORTA_ADTEST |
| AF11 | VSS | AT11 | AVSS_DRD |
| AF12 | VSS | AT12 | USB30_A_DRD0_RXN |
| AF13 | VSS | AT13 | AVSS_DRD |
| AF14 | VCC_SYS | AT14 | USB20_A_DRD_USB_P |
| AF15 | VSS | AT15 | AVSS_UFS |
| AF16 | VCC_CPUX | AT16 | UFS_TXD0N |
| AF17 | VSS | AT17 | AVSS_EDP1 |
| AF18 | VCC_CPUX | AT18 | EDP1_TX0N |
| AF19 | VSS | AT19 | VSS |
| AF20 | VCC_CPUX | AT20 | QSPI_CS0 |
| AG1 | DDR0_DQ_B_08 | AU1 | DDR0_DQ_A_02 |
| AG2 | DDR0_DQ_B_10 | AU2 | DDR0_DQ_A_01 |
| AG3 | VSS | AU3 | VSS |
| AG4 | DDR0_DMI0_B | AU4 | VSS |
| AG5 | DDR0_DQ_B_04 | AU5 | VSS |
| AG6 | VSS | AU6 | VSS |
| AG7 | DDR0_CS0_B_CA06 | AU7 | DDR0_CS1_A |
| AG8 | VDDQ_DDR | AU8 | VSS |
| AG9 | VSS | AU9 | VSS |
| AG10 | VDD0V8_DDR | AU10 | AVSS_DRD |
| AG11 | AVDD08_PLL_DDR0 | AU11 | AVSS_DRD |
| AG12 | VSS | AU12 | USB30_A_DRD0_RXP |
| AG13 | VCC_SYS | AU13 | AVSS_DRD |
| AG14 | VSS | AU14 | USB20_A_DRD_USB_M |
| AG15 | VCC_SYS | AU15 | AVSS_UFS |
| AG16 | VSS | AU16 | UFS_TXD0P |
| AG17 | VCC_SYS | AU17 | AVSS_EDP1 |
| AG18 | VSS | AU18 | EDP1_TX0P |
| AG19 | VCC_SYS | AU19 | VSS |
| AG20 | VSS | AU20 | QSPI_DAT1 |
| AH1 | VSS | AV1 | DDR0_DQ_A_00 |
| AH2 | VSS | AV2 | DDR0_DQ_A_03 |
| AH3 | VSS | AV3 | VSS |
| AH4 | DDR0_DQ_B_06 | AV4 | DDR0_WCK_T_A_1 |
| AH5 | DDR0_DQ_B_05 | AV5 | DDR0_WCK_C_A_1 |
| AH6 | VSS | AV6 | VSS |
| AH7 | DDR0_CA_B_05 | AV7 | DDR0_ZN |
| AH8 | VSS | AV8 | VSS |
| AH9 | VDD0V8_DDR | AV9 | VSS |
| AH10 | VSS | AV10 | AVSS_DRD |
| AH11 | AVDD18_PLL_DDR0 | AV11 | USB30_A_DRD1_RXP |
| AH12 | VCC_SYS | AV12 | AVSS_DRD |
| AH13 | VSS | AV13 | UFS_RST_N |
| AH14 | VCC_SYS | AV14 | AVSS_UFS |
| AH15 | VSS | AV15 | UFS_TXD1N |
| AH16 | VCC_SYS | AV16 | AVSS_UFS |
| AH17 | VSS | AV17 | EDP1_AUXP |
| AH18 | VCC_SYS | AV18 | AVSS_EDP1 |
| AH19 | VSS | AV19 | EDP1_TX2P |
| AH20 | VCC_SYS | AV20 | VSS |
| AJ1 | DDR0_CKC_B | AW1 | VSS |
| AJ2 | DDR0_CKT_B | AW2 | VSS |
| AJ3 | VSS | AW3 | VSS |
| AJ4 | DDR0_DQ_B_07 | AW4 | DDR0_DQ_A_11 |
| AJ5 | DDR0_CA_B_04 | AW5 | DDR0_DQ_A_09 |
| AJ6 | VSS | AW6 | VSS |
| AJ7 | DDR0_CA_B_03 | AW7 | DDR0_RESET_N |
| AJ8 | VSS | AW8 | VSS |
| AJ9 | VSS | AW9 | AVSS_DRD |
| AJ10 | AVDD08_PLL1 | AW10 | USB30_A_DRD0_TXP |
| AJ11 | VCC_SYS | AW11 | USB30_A_DRD1_RXN |
| AJ12 | VSS | AW12 | USB30_A_DRD1_TXN |
| AJ13 | VCC_SYS | AW13 | AVSS_UFS |
| AJ14 | VSS | AW14 | UFS_RXD1P |
| AJ15 | VCC_SYS | AW15 | UFS_TXD1P |
| AJ16 | VSS | AW16 | UFS_RXD0N |
| AJ17 | DVDD08_EDP1 | AW17 | EDP1_AUXN |
| AJ18 | DVDD08_EDP1 | AW18 | EDP1_TX1N |
| AJ19 | VCC_SYS | AW19 | EDP1_TX2N |
| AJ20 | VSS | AW20 | EDP1_TX3N |
| AK1 | DDR0_CKC_A | AY2 | VSS |
| AK2 | DDR0_CKT_A | AY3 | DDR0_DMI1_A |
| AK3 | VSS | AY4 | DDR0_DQ_A_10 |
| AK4 | DDR0_CS0_A_CA06 | AY5 | DDR0_DQ_A_08 |
| AK5 | DDR0_CA_A_03 | AY6 | VSS |
| AK6 | VSS | AY7 | VSS |
| AK7 | DDR0_CS1_B | AY8 | VSS |
| AK8 | VSS | AY9 | AVSS_DRD |
| AK9 | AVDD18_PLL1 | AY10 | USB30_A_DRD0_TXN |
| AK10 | AVSS_PLL1 | AY11 | AVSS_DRD |
| AK11 | VSS | AY12 | USB30_A_DRD1_TXP |
| AK12 | VCC_SYS | AY13 | AVSS_UFS |
| AK13 | VSS | AY14 | UFS_RXD1N |
| AK14 | VSS | AY15 | AVSS_UFS |
| AK15 | VSS | AY16 | UFS_RXD0P |
| AK16 | VCC_SYS | AY17 | AVSS_EDP1 |
| AK17 | AVSS_EDP1 | AY18 | EDP1_TX1P |
| AK18 | VCC_SYS | AY19 | AVSS_EDP1 |
| AK19 | VSS | AY20 | EDP1_TX3P |
| AK20 | VCC_SYS | — | — |

#### 4.1.4 (AA~AY, 21~40)

<img src="static/k3_pinmap_aa-ay_21-40.png" alt="" width="800">

| 引脚编号 | 引脚名称 | 引脚编号 | 引脚名称 |
| --- | --- | --- | --- |
| AA21 | VCC_SYS | AL21 | VCC18_SD_CAP |
| AA22 | VSS | AL22 | VCC18_GPIO5 |
| AA23 | VCC_SYS | AL23 | VSS |
| AA24 | VSS | AL24 | VCC18_GPIO1 |
| AA25 | VCC_SYS | AL25 | VCC18_GPIO4 |
| AA26 | VSS | AL26 | VCC18_GPIO4 |
| AA27 | VCC_SYS | AL27 | VSS |
| AA28 | VSS | AL28 | VCC_SYS |
| AA29 | VCC_SYS | AL29 | VSS |
| AA30 | AVDD08_DSI | AL30 | VCC_SYS |
| AA31 | AVDD08_DSI | AL31 | VSS |
| AA32 | VSS | AL32 | AVDD18_EDP0 |
| AA33 | VSS | AL33 | VSS |
| AA34 | VSS | AL34 | VSS |
| AA35 | VSS | AL35 | VSS |
| AA36 | AVSS_MIPI012 | AL36 | AVSS_DSI |
| AA37 | AVSS_MIPI012 | AL37 | AVSS_DSI |
| AA38 | MIPI_CSI1_D2N | AL38 | MIPI_DSI1_CLKN |
| AA39 | MIPI_CSI1_D2P | AL39 | MIPI_DSI1_CLKP |
| AA40 | AVSS_MIPI012 | AL40 | AVSS_DSI |
| AB21 | VSS | AM21 | VCC18_SD_CAP |
| AB22 | VCC_SYS | AM22 | VCC18_GPIO5 |
| AB23 | VSS | AM23 | VSS |
| AB24 | VCC_SYS | AM24 | VCC18_GPIO1 |
| AB25 | VSS | AM25 | VSS |
| AB26 | VCC_SYS | AM26 | VCC1833_GPIO4 |
| AB27 | VSS | AM27 | VCC1833_GPIO1 |
| AB28 | VCC_SYS | AM28 | VSS |
| AB29 | VSS | AM29 | VSS |
| AB30 | AVDD08_CSI2 | AM30 | VCC_SYS |
| AB31 | AVDD08_CSI2 | AM31 | VSS |
| AB32 | VSS | AM32 | AVDD18_EDP0 |
| AB33 | MIPI_CSI2_CLKN | AM33 | MIPI_DSI1_D1P |
| AB34 | MIPI_CSI2_CLKP | AM34 | MIPI_DSI1_D1N |
| AB35 | AVSS_MIPI012 | AM35 | VSS |
| AB36 | MIPI_CSI1_D3N | AM36 | MIPI_DSI1_D3P |
| AB37 | MIPI_CSI1_D3P | AM37 | MIPI_DSI1_D3N |
| AB38 | AVSS_MIPI012 | AM38 | AVSS_DSI |
| AB39 | MIPI_CSI1_CLKN | AM39 | MIPI_DSI1_D0P |
| AB40 | MIPI_CSI1_CLKP | AM40 | MIPI_DSI1_D0N |
| AC21 | VCC_SYS | AN21 | VSS |
| AC22 | VSS | AN22 | VSS |
| AC23 | VCC_SYS | AN23 | VSS |
| AC24 | VSS | AN24 | VSS |
| AC25 | VCC_SYS | AN25 | VSS |
| AC26 | VSS | AN26 | VCC1833_GPIO4 |
| AC27 | VCC_SYS | AN27 | VCC1833_GPIO1 |
| AC28 | VSS | AN28 | VSS |
| AC29 | VCC_SYS | AN29 | VSS |
| AC30 | VSS | AN30 | VSS |
| AC31 | AVSS_MIPI012 | AN31 | VSS |
| AC32 | AVSS_MIPI012 | AN32 | VSS |
| AC33 | AVSS_MIPI012 | AN33 | VSS |
| AC34 | AVSS_MIPI012 | AN34 | VSS |
| AC35 | AVSS_MIPI012 | AN35 | VSS |
| AC36 | AVSS_MIPI012 | AN36 | EDP0_EXTR |
| AC37 | AVSS_MIPI012 | AN37 | AVSS_EDP0 |
| AC38 | MIPI_CSI1_D1P | AN38 | EDP0_AUXN |
| AC39 | MIPI_CSI1_D1N | AN39 | EDP0_AUXP |
| AC40 | AVSS_MIPI012 | AN40 | AVSS_EDP0 |
| AD21 | VSS | AP21 | QSPI_DAT2 |
| AD22 | VCC_CPUX | AP22 | VSS |
| AD23 | VSS | AP23 | VSS |
| AD24 | VCC_CPUX | AP24 | GPIO[5]_119 |
| AD25 | VSS | AP25 | GPIO[5]_114 |
| AD26 | VCC_CPUX | AP26 | GPIO[5]_108 |
| AD27 | VSS | AP27 | GPIO[5]_106 |
| AD28 | VCC_SYS | AP28 | VSS |
| AD29 | VSS | AP29 | GPIO[1]_20 |
| AD30 | AVDD08_CSI0 | AP30 | GPIO[1]_16 |
| AD31 | AVDD08_CSI0 | AP31 | GPIO[1]_06 |
| AD32 | AVDD08_CSI1 | AP32 | GPIO[1]_05 |
| AD33 | AVDD08_CSI1 | AP33 | VSS |
| AD34 | AVSS_MIPI012 | AP34 | GPIO[4]_79 |
| AD35 | AVSS_MIPI012 | AP35 | GPIO[4]_78 |
| AD36 | MIPI_CSI1_D0P | AP36 | VSS |
| AD37 | MIPI_CSI1_D0N | AP37 | AVSS_EDP0 |
| AD38 | AVSS_MIPI012 | AP38 | AVSS_EDP0 |
| AD39 | MIPI_CSI0_D3N | AP39 | EDP0_TX3P |
| AD40 | MIPI_CSI0_D3P | AP40 | EDP0_TX3N |
| AE21 | VCC_CPUX | AR21 | QSPI_CS1 |
| AE22 | VSS | AR22 | VSS |
| AE23 | VCC_CPUX | AR23 | VSS |
| AE24 | VSS | AR24 | GPIO[5]_120 |
| AE25 | VCC_CPUX | AR25 | VSS |
| AE26 | VSS | AR26 | GPIO[5]_109 |
| AE27 | VCC_CPUX | AR27 | GPIO[5]_105 |
| AE28 | VSS | AR28 | GPIO[5]_99 |
| AE29 | VCC_SYS | AR29 | GPIO[1]_19 |
| AE30 | VSS | AR30 | VSS |
| AE31 | AVSS_MIPI012 | AR31 | GPIO[1]_07 |
| AE32 | AVSS_MIPI012 | AR32 | GPIO[1]_04 |
| AE33 | AVSS_MIPI012 | AR33 | GPIO[4]_76 |
| AE34 | AVSS_MIPI012 | AR34 | GPIO[4]_80 |
| AE35 | AVSS_MIPI012 | AR35 | VSS |
| AE36 | AVSS_MIPI012 | AR36 | VSS |
| AE37 | AVSS_MIPI012 | AR37 | AVSS_EDP0 |
| AE38 | MIPI_CSI0_D2N | AR38 | EDP0_TX2P |
| AE39 | MIPI_CSI0_D2P | AR39 | EDP0_TX2N |
| AE40 | AVSS_MIPI012 | AR40 | AVSS_EDP0 |
| AF21 | VSS | AT21 | QSPI_DAT0 |
| AF22 | VCC_CPUX | AT22 | VSS |
| AF23 | VSS | AT23 | GPIO[5]_124 |
| AF26 | VCC_CPUX | AT24 | GPIO[5]_121 |
| AF27 | VSS | AT25 | GPIO[5]_115 |
| AF28 | VCC_SYS | AT26 | GPIO[5]_110 |
| AF29 | VSS | AT27 | VSS |
| AF30 | AVDD18_CSI1 | AT28 | GPIO[5]_100 |
| AF31 | AVDD18_CSI1 | AT29 | GPIO[1]_18 |
| AF32 | AVDD18_CSI2 | AT30 | GPIO[1]_13 |
| AF33 | AVDD18_CSI2 | AT31 | GPIO[1]_08 |
| AF34 | AVSS_MIPI012 | AT32 | VSS |
| AF35 | AVSS_MIPI012 | AT33 | GPIO[4]_77 |
| AF36 | MIPI_CSI0_CLKN | AT34 | GPIO[4]_81 |
| AF37 | MIPI_CSI0_CLKP | AT35 | GPIO[4]_86 |
| AF38 | AVSS_MIPI012 | AT36 | GPIO[4]_90 |
| AF39 | MIPI_CSI0_D1P | AT37 | AVSS_EDP0 |
| AF40 | MIPI_CSI0_D1N | AT38 | AVSS_EDP0 |
| AG21 | VCC_CPUX | AT39 | EDP0_TX1P |
| AG22 | VSS | AT40 | EDP0_TX1N |
| AG23 | VCC_CPUX | AU21 | MMC1_DAT2 |
| AG26 | VSS | AU22 | MMC1_DAT1 |
| AG27 | VCC_CPUX | AU23 | GPIO[5]_125 |
| AG28 | VSS | AU25 | GPIO[5]_116 |
| AG29 | VCC_SYS | AU26 | GPIO[5]_111 |
| AG30 | AVSS_DSI | AU28 | GPIO[5]_101 |
| AG31 | AVSS_DSI | AU29 | VSS |
| AG32 | AVSS_DSI | AU31 | GPIO[1]_09 |
| AG33 | AVSS_DSI | AU32 | GPIO[1]_03 |
| AG34 | AVSS_MIPI012 | AU34 | VSS |
| AG35 | AVSS_MIPI012 | AU35 | GPIO[4]_87 |
| AG36 | AVSS_MIPI012 | AU37 | VSS |
| AG37 | AVSS_MIPI012 | AU38 | EDP0_TX0P |
| AG38 | MIPI_CSI0_D0P | AU39 | EDP0_TX0N |
| AG39 | MIPI_CSI0_D0N | AU40 | AVSS_EDP0 |
| AG40 | AVSS_MIPI012 | AV21 | MMC1_CLK |
| AH21 | VSS | AV22 | MMC1_DAT0 |
| AH22 | VCC_CPUX | AV23 | GPIO[5]_126 |
| AH23 | VSS | AV25 | GPIO[5]_117 |
| AH24 | VCC_CPUX | AV26 | VSS |
| AH25 | VSS | AV28 | GPIO[5]_102 |
| AH26 | VCC_CPUX | AV29 | GPIO[1]_17 |
| AH27 | VSS | AV31 | VSS |
| AH28 | VCC_SYS | AV32 | GPIO[1]_02 |
| AH29 | VSS | AV34 | GPIO[4]_82 |
| AH30 | AVDD12_DSI | AV35 | GPIO[4]_88 |
| AH31 | AVDD18_CSI0 | AV37 | VSS |
| AH32 | AVDD18_CSI0 | AV38 | VSS |
| AH33 | AVSS_DSI | AV39 | GPIO[4]_96 |
| AH34 | AVSS_DSI | AV40 | GPIO[4]_98 |
| AH35 | AVSS_DSI | AW21 | VSS |
| AH36 | MIPI_DSI0_D2P | AW22 | MMC1_CMD |
| AH37 | MIPI_DSI0_D2N | AW23 | VSS |
| AH38 | AVSS_DSI | AW24 | GPIO[5]_122 |
| AH39 | MIPI_DSI0_D1N | AW25 | GPIO[5]_118 |
| AH40 | MIPI_DSI0_D1P | AW26 | GPIO[5]_112 |
| AJ21 | VCC_SYS | AW27 | GPIO[5]_104 |
| AJ22 | VSS | AW28 | VSS |
| AJ23 | VCC_CPUX | AW29 | GPIO[1]_14 |
| AJ24 | VSS | AW30 | GPIO[1]_12 |
| AJ25 | VCC_CPUX | AW31 | GPIO[1]_10 |
| AJ26 | VSS | AW32 | GPIO[1]_01 |
| AJ27 | DVDD08_EDP0 | AW33 | VSS |
| AJ28 | DVDD08_EDP0 | AW34 | GPIO[4]_83 |
| AJ29 | VCC_SYS | AW35 | GPIO[4]_89 |
| AJ30 | AVDD12_DSI | AW36 | GPIO[4]_91 |
| AJ31 | AVDD18_DSI | AW37 | GPIO[4]_93 |
| AJ32 | VSS | AW38 | GPIO[4]_95 |
| AJ33 | AVSS_DSI | AW39 | GPIO[4]_97 |
| AJ34 | AVSS_DSI | AW40 | VSS |
| AJ35 | AVSS_DSI | AY21 | VSS |
| AJ36 | AVSS_DSI | AY22 | MMC1_DAT3 |
| AJ37 | AVSS_DSI | AY23 | GPIO[5]_127 |
| AJ38 | MIPI_DSI0_CLKN | AY24 | GPIO[5]_123 |
| AJ39 | MIPI_DSI0_CLKP | AY25 | VSS |
| AJ40 | AVSS_DSI | AY26 | GPIO[5]_113 |
| AK21 | VSS | AY27 | GPIO[5]_107 |
| AK22 | VCC_SYS | AY28 | GPIO[5]_103 |
| AK23 | VSS | AY29 | GPIO[1]_15 |
| AK24 | VCC_SYS | AY30 | VSS |
| AK25 | VSS | AY31 | GPIO[1]_11 |
| AK26 | VCC_SYS | AY32 | GPIO[1]_00 |
| AK27 | AVSS_EDP0 | AY33 | GPIO[4]_85 |
| AK28 | VCC_SYS | AY34 | GPIO[4]_84 |
| AK29 | AVSS_EDP0 | AY35 | VSS |
| AK30 | VSS | AY36 | GPIO[4]_92 |
| AK31 | AVDD18_DSI | AY37 | GPIO[4]_94 |
| AK32 | VSS | AY38 | VSS |
| AK33 | MIPI_DSI0_D0P | AY39 | VSS |
| AK34 | MIPI_DSI0_D0N | AY40 | VSS |
| AK35 | AVSS_DSI | — | — |
| AK36 | MIPI_DSI0_D3P | — | — |
| AK37 | MIPI_DSI0_D3N | — | — |
| AK38 | AVSS_DSI | — | — |
| AK39 | MIPI_DSI1_D2N | — | — |
| AK40 | MIPI_DSI1_D2P | — | — |

### 4.2 I/O 引脚电气参数

#### 4.2.1 1.8V I/O 引脚

| 电源域 | 符号 | 参数说明 | 最小值<br>(Min) | 典型值<br>(Typ) | 最大值<br>(Max) |
| --- | --- | --- | --- | --- | --- |
| **1.8V 输入** | Vih | 输入高电平阈值 | VCC×0.7V | 1.8V | VCC+0.2V |
| | Vil | 输入低电平阈值 | -0.3V | 0V | VCC×0.3V |
| | Rpu | 上拉电阻 | 55kΩ | 79kΩ | 121kΩ |
| | Rpd | 下拉电阻 | 51kΩ | 87kΩ | 169kΩ |
| | Iil | 输入漏电流<br>（引脚配置为输入模式） | — | — | 10µA |
| **1.8V 输出** | Voh | 输出高电平电压 | VCC−0.2V | — | — |
| | Vol | 输出低电平电压 | — | — | 0.2V |
| | Iol (DCS=00) | 低电平输出电流<br>（Vpad=0.2V） | 13mA | — | — |
| | Iol (DCS=01) | 低电平输出电流<br>（Vpad=0.2V） | 25mA | — | — |
| | Iol (DCS=10) | 低电平输出电流<br>（Vpad=0.2V） | 37mA | — | — |
| | Iol (DCS=11) | 低电平输出电流<br>（Vpad=0.2V） | 49mA | — | — |
| | Ioh (DCS=00) | 高电平输出电流<br>（Vpad = VCC - 0.2V） | 11mA | — | — |
| | Ioh (DCS=01) | 高电平输出电流<br>（Vpad = VCC - 0.2V） | 21mA | — | — |
| | Ioh (DCS=10) | 高电平输出电流<br>（Vpad = VCC - 0.2V） | 32mA | — | — |
| | Ioh (DCS=11) | 高电平输出电流<br>（Vpad = VCC - 0.2V） | 42mA | — | — |

#### 4.2.2 3.3V I/O 引脚

| 电源域 | 符号 | 参数说明 | 最小值<br>(Min) | 典型值<br>(Typ) | 最大值<br>(Max) |
| --- | --- | --- | --- | --- | --- |
| **3.3V 输入** | Vih | 输入高电平阈值 | 2V | — | VCC+0.3V |
| | Vil | 输入低电平阈值 | -0.3V | 0V | 0.8V |
| | Rpu | 上拉电阻 | 26kΩ | 47kΩ | 72kΩ |
| | Rpd | 下拉电阻 | 27kΩ | 54kΩ | 267kΩ |
| | Iil | 输入漏电流 | — | — | 10µA |
| **3.3V 输出** | Voh | 输出高电平电压 | 2.4V | — | — |
| | Vol | 输出低电平电压 | — | — | 0.4V |
| | Iol (DS=000) | 低电平输出电流<br>（Vpad=0.4V） | 7mA | — | — |
| | Iol (DS=001) | 低电平输出电流<br>（Vpad=0.4V） | 10mA | — | — |
| | Iol (DS=010) | 低电平输出电流<br>（Vpad=0.4V） | 14mA | — | — |
| | Iol (DS=011) | 低电平输出电流<br>（Vpad=0.4V） | 18mA | — | — |
| | Iol (DS=100) | 低电平输出电流<br>（Vpad=0.4V） | 21mA | — | — |
| | Iol (DS=101) | 低电平输出电流<br>（Vpad=0.4V） | 24mA | — | — |
| | Iol (DS=110) | 低电平输出电流<br>（Vpad=0.4V） | 28mA | — | — |
| | Iol (DS=111) | 低电平输出电流<br>（Vpad=0.4V） | 31mA | — | — |
| | Ioh (DS=000) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 7mA | — | — |
| | Ioh (DS=001) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 10mA | — | — |
| | Ioh (DS=010) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 13mA | — | — |
| | Ioh (DS=011) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 16mA | — | — |
| | Ioh (DS=100) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 19mA | — | — |
| | Ioh (DS=101) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 23mA | — | — |
| | Ioh (DS=110) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 26mA | — | — |
| | Ioh (DS=111) | 高电平输出电流<br>（Vpad = VCC - 0.5V） | 29mA | — | — |

### 4.3 多功能信号/引脚功能

K3 的 I/O 引脚支持 **功能 0 至 功能 7（Function 0–7）** 的信号分配。  
绝大多数 K3 I/O 引脚均为 **多功能引脚**，可通过 **多功能引脚寄存器（Multi-Function Pin Registers, MFPRs）** 配置为多种可用功能之一。此外，部分功能可映射至多个不同的物理引脚，提供灵活的引脚复用方案。

所有分配的信号按其功能类别（如电源、时钟等）进行组织，并进一步按接口类型（如 JTAG、SPIx 等）分组，具体说明见后续小节（为便于查阅，各接口按字母顺序排序）。

> **注**：信号/引脚类型符号定义如下：  
>
> - **I** = 输入（Input）  
> - **O** = 输出（Output）  
> - **I/O** = 双向输入/输出（Input/Output）  
> - **OD** = 开漏输出（Open-Drain）  
> - **RO** = 参考输出（Reference Output）  

#### 4.3.1 JTAG – 主接口（Primary）

| 信号/引脚 | 类型 | 描述 |
| --- | --- | --- |
| PRI_TCK | I | 主 JTAG 接口 1 的测试时钟。用于 JTAG 测试接口上的所有数据传输。 |
| PRI_TDI | I | 主 JTAG 接口 1 的测试数据输入。用于将数据从 JTAG 调试器发送至 K3 处理器。该引脚内置上拉电阻。 |
| PRI_TDO | O | 主 JTAG 接口 1 的测试数据输出。用于将数据从 K3 处理器返回至 JTAG 调试器。 |
| PRI_TMS | I | 主 JTAG 接口 1 的测试模式选择。用于从 JTAG 调试器选择所需的测试模式。该引脚内置上拉电阻。 |
| PRI_TRSTn | I | 主 JTAG 接口 1 的测试复位信号。符合 IEEE 1149.1 标准，用于触发 JTAG 复位。 |
| VCXO_OUT | O | 24 MHz VCXO 输出时钟 |
| VCXO_REQ | I | OCLK1 时钟请求信号 |

#### 4.3.2 杂项（Miscellaneous）

| 信号/引脚 | 类型 | 描述 |
| --- | --- | --- |
| MPLL_TST_CK | — | PLL 测试引脚 |
| MN_CLK_OUT | O | 分数分频（M/N）时钟输出。由主 PMU 提供的通用 M/N 分数分频器产生的时钟信号。若需在 GPIO[122]（即 MN_CLK_OUT）上输出 13 MHz 时钟，必须将 `CLK_REQ` 配置为 **Function 0** 并拉高。 |
| Sleep_OUT | O | PMIC 睡眠设置 |

#### 4.3.3 SPIx

| 信号/引脚 | 类型 | 描述 |
| --- | --- | --- |
| SPIx_FRM | I/O | 同步串行端口帧信号 0/2。串行帧同步可配置为输出（主模式）或输入（从模式）。 |
| SPIx_RXD | I | 同步串行端口接收数据 0/2。串行数据在位时钟作用下锁存。 |
| SPIx_SCLK | I/O | 同步串行端口时钟 0/2。串行位时钟可配置为输出（主模式）或输入（从模式）。 |
| SPIx_TXD | O | 同步串行端口发送数据 0/2。串行数据随位时钟同步驱动输出。 |

#### 4.3.4 TWSI

**专用信号（Dedicated）**

| 信号/引脚 | 类型 | 描述 |
| --- | --- | --- |
| PWR_SDA | I/O | TWSI 串行数据/地址线 |
| PWR_SCL | I/O | TWSI 串行时钟线 |

**通用信号（Common）**

| 信号/引脚 | 类型 | 描述 |
| --- | --- | --- |
| I²Cx_SCL | I/O, OD | TWSIx 时钟线 |
| I²Cx_SDA | I/O, OD | TWSIx 数据线 |

#### 4.3.5 UARTx

| 信号/引脚 | 类型 | 描述 |
| --- | --- | --- |
| UARTx_CTSn | I | UARTx Clear-To-Send（清除发送） |
| UARTx_RTSn | O | UARTx Request-To-Send（请求发送） |
| UARTx_RXD | I | UARTx 接收数据 |
| UARTx_TXD | O | UARTx 发送数据 |

#### 4.3.6 USB

| 信号/引脚 | 类型 | 描述 |
| --- | --- | --- |
| USBx_N | I/O | USB D± 差分信号（负） |
| USBx_P | I/O | USB D± 差分信号（正） |
| VBUS_ON | I | USB VBUS 供电检测指示 |

### 4.4 多功能 I/O 引脚分配

通用输入/输出（GPIO）模块提供灵活的引脚控制与信号复用能力。每个 GPIO 引脚既可作为标准输入/输出使用，也可配置为多种 **备用功能（Alternate Function）** 之一，从而高效连接系统与片上外设。

完整的多功能引脚分配表请参阅 [K3 用户手册 — 第 3.4 节](https://www.spacemit.com/community/document/info?lang=en&nodepath=hardware/key_stone/k3/k3_docs/k3_usermanual/03_pinout.md)（仅英文版）。引脚分配的可下载版本亦可在 [K3 硬件资源](../k3_hw/k3_hw_resources.md) 中获取。

## 5. 电气特性

### 5.1 引脚交流/直流工作条件

下表列出了推荐的工作条件。

| 模块<br>（Module）| 符号/引脚<br>（Symbol/Pin）| 最小值<br>（Min）|	典型值<br>（Typ）| 最大值<br>（Max）|
| --- | --- | --- | --- | --- |
| **CPU** | VDD08_X100 | 0.72V | 0.8V | 1.05V |
|  | VDD08_M1A100 | 0.72V | 0.8V | 0.88V |
| **PLL** | AVDD08_PLL1 | 0.76V | 0.8V | 0.88V |
|  | AVDD08_PLL234 | 0.76V | 0.8V | 0.88V |
|  | AVDD08_PLL567 | 0.76V | 0.8V | 0.88V |
|  | AVDD18_PLL1 | 1.71V | 1.8V | 1.96V |
|  | AVDD18_PLL234 | 1.71V | 1.8V | 1.96V |
|  | AVDD18_PLL567 | 1.71V | 1.8V | 1.96V |
| **PLL-DDR** | AVDD08_PLL_DDR0 | 0.76V | 0.8V | 0.88V |
|  | AVDD08_PLL_DDR1 | 0.76V | 0.8V | 0.88V |
|  | AVDD1V8_PLL_DDR0 | 1.71V | 1.8V | 1.96V |
|  | AVDD1V8_PLL_DDR1 | 1.71V | 1.8V | 1.96V |
| **CSI** | AVDD08_CSI0 | 0.76V | 0.8V | 0.88V |
|  | AVDD08_CSI1 | 0.76V | 0.8V | 0.88V |
|  | AVDD08_CSI2 | 0.76V | 0.8V | 0.88V |
|  | AVDD18_CSI0 | 1.71V | 1.8V | 1.96V |
|  | AVDD18_CSI1 | 1.71V | 1.8V | 1.96V |
|  | AVDD18_CSI2 | 1.71V | 1.8V | 1.96V |
| **DDR** | VAA1V8_VDD2H_DDR | 1.674V | 1.8V | 1.98V |
|  | VDD2H_DDR | 1.01V/1.045V (LP5/LP4x) | 1.05V/1.1V (LP5/LP4x) | 1.12V/1.155V (LP5/LP4x) |
|  | VDDQ_DDR | 0.47V/0.57V (LP5/LP4x) | 0.5V/0.6V (LP5/LP4x) | 0.57V/0.63V (LP5/LP4x) |
|  | VDD0V8_DDR | 0.744V | 0.8V | 0.88V |
| **DSI** | AVDD08_DSI | 0.76V | 0.8V | 0.88V |
|  | AVDD12_DSI | 1.14V | 1.2V | 1.32V |
|  | AVDD18_DSI | 1.71V | 1.8V | 1.96V |
| **EDP** | AVDD18_EDP0 | 1.674V | 1.8V | 1.98V |
|  | DVDD08_EDP0 | 0.744V | 0.8V | 0.88V |
| **EDP1** | AVDD18_EDP1 | 1.674V | 1.8V | 1.98V |
|  | DVDD08_EDP1 | 0.744V | 0.8V | 0.88V |
| **EMMC** | AVDD08_EMMC | 0.744V | 0.8V | 0.88V |
|  | VCC18_EMMC | 1.674V | 1.8V | 1.98V |
| **FUSE** | FUSE_AVDD18 | 1.71V | 1.8V | 1.96V |
| **GPIO** | VCC18_GPIO1 | 1.674V | 1.8V | 1.98V |
|  | VCC18_GPIO2 | 1.674V | 1.8V | 1.98V |
|  | VCC18_GPIO3 | 1.674V | 1.8V | 1.98V |
|  | VCC18_GPIO4 | 1.674V | 1.8V | 1.98V |
|  | VCC18_GPIO5 | 1.674V | 1.8V | 1.98V |
|  | VCC18_PMIC | 1.674V | 1.8V | 1.98V |
|  | VCC1833_GPIO1 | 1.674V/2.97V | 1.8V/3.3V | 1.98V/3.63V |
|  | VCC1833_GPIO2 | 1.674V/2.97V | 1.8V/3.3V | 1.98V/3.63V |
|  | VCC1833_GPIO4 | 1.674V/2.97V | 1.8V/3.3V | 1.98V/3.63V |
|  | VCC1833_GPIO5 | 1.674V/2.97V | 1.8V/3.3V | 1.98V/3.63V |
|  | VCC1833_QSPI | 1.674V/2.97V | 1.8V/3.3V | 1.98V/3.63V |
|  | VCC1833_MMC1 | 1.674V/2.97V | 1.8V/3.3V | 1.98V/3.63V |
| **OSC** | AVDD08_OSC | 0.76V | 0.8V | 0.88V |
|  | AVDD18_OSC | 1.71V | 1.8V | 1.96V |
| **PICE PHY0** | AVDD08_PCIeA | 0.744V | 0.8V | 0.88V |
|  | AVDD18_PCIeA | 1.674V | 1.8V | 1.98V |
| **PICE PHY1** | AVDD08_PCIeB | 0.744V | 0.8V | 0.88V |
|  | AVDD18_PCIeB | 1.674V | 1.8V | 1.98V |
| **PICE PHY2** | AVDD08_PCIeC/USB3-B | 0.744V | 0.8V | 0.88V |
|  | AVDD18_PCIeC/USB3-B | 1.674V | 1.8V | 1.98V |
| **PICE PHY3** | AVDD08_PCIeD/USB3-C | 0.744V | 0.8V | 0.88V |
|  | AVDD18_PCIeD/USB3-C | 1.674V | 1.8V | 1.98V |
| **PICE PHY4** | AVDD08_PCIeE/USB3-D | 0.744V | 0.8V | 0.88V |
|  | AVDD18_PCIeE/USB3-D | 1.674V | 1.8V | 1.98V |
| **PICE PHY5** | AVDD08_PCIe5 | 0.744V | 0.8V | 0.88V |
|  | AVDD18_PCIe5 | 1.674V | 1.8V | 1.98V |
| **UCIE** | UCIE_VCCAON_0V8 | 0.76V | 0.8V | 0.84V |
|  | UCIE_VCCIO_0V8 | 0.76V | 0.8V | 0.84V |
|  | UCIE_VCCPLL_1P2V | 1.116V | 1.2V | 1.236V |
|  | UCIE_VDD_0V8 | 0.76V | 0.8V | 0.84V |
|  | UCIE_VDDBH_0V9 | 0.855V | 0.9V | 0.945V |
|  | UCIE_VDDVPH0_0V9 | 0.855V | 0.9V | 0.945V |
| **UFS** | UFS_VCC_1V8 | 1.71V | 1.8V | 1.96V |
|  | UFS_VCCQ_1V2 | 1.14V | 1.2V | 1.32V |
|  | UFS_VDDU_0V8 | 0.76 | 0.8V | 0.88V |
| **USB2** | AVDD08_B_USB20 | 0.744V | 0.8V | 0.88V |
|  | AVDD08_C_USB20 | 0.744V | 0.8V | 0.88V |
|  | AVDD08_D_USB20 | 0.744V | 0.8V | 0.88V |
|  | AVDD08_USB20_Host | 0.744V | 0.8V | 0.88V |
|  | AVDD18_B_USB20 | 1.674V | 1.8V | 1.98V |
|  | AVDD18_C_USB20 | 1.674V | 1.8V | 1.98V |
|  | AVDD18_D_USB20 | 1.674V | 1.8V | 1.98V |
|  | AVDD18_USB20_Host | 1.674V | 1.8V | 1.98V |
|  | AVDD33_B_USB20 | 3.069V | 3.3V | 3.63V |
|  | AVDD33_C_USB20 | 3.069V | 3.3V | 3.63V |
|  | AVDD33_D_USB20 | 3.069V | 3.3V | 3.63V |
|  | AVDD33_DRD_USB | 3.069V | 3.3V | 3.63V |
|  | AVDD33_USB20_Host | 3.069V | 3.3V | 3.63V |
| **USB3-DRD** | AVDD08_DRD_USB | 0.744V | 0.8V | 0.88V |
|  | AVDD18_DRD_USB | 1.674V | 1.8V | 1.98V |

### 5.2 绝对最大直流额定值

#### 5.2.1 引脚参数
  
| 模块<br>（Module） | 符号/引脚<br>（Symbol/Pin） | 最小值<br>（Min） | 最大值<br>（Max） |
| --- | --- | --- | --- |
| **CPU** | VDD08_X100 | -0.3V | 1.05V |
| | VDD08_M1A100 | -0.3V | 0.88V |
| **Digital Power** | VCC_M1 | -0.3V | 0.88V |
| **PLL** | AVDD08_PLL1 | -0.3V | 0.88V |
| | AVDD08_PLL234 | -0.3V | 0.88V |
| | AVDD08_PLL567 | -0.3V | 0.88V |
| | AVDD18_PLL1 | -0.3V | 1.96V |
| | AVDD18_PLL234 | -0.3V | 1.96V |
| | AVDD18_PLL567 | -0.3V | 1.96V |
| **PLL-DDR** | AVDD08_PLL_DDR0 | -0.3V | 0.88V |
| | AVDD08_PLL_DDR1 | -0.3V | 0.88V |
| | AVDD1V8_PLL_DDR0 | -0.3V | 1.96V |
| | AVDD1V8_PLL_DDR1 | -0.3V | 1.96V |
| **CSI** | AVDD08_CSI0 | -0.3V | 0.88V |
| | AVDD08_CSI1 | -0.3V | 0.88V |
| | AVDD08_CSI2 | -0.3V | 0.88V |
| | AVDD18_CSI0 | -0.3V | 1.96V |
| | AVDD18_CSI1 | -0.3V | 1.96V |
| | AVDD18_CSI2 | -0.3V | 1.96V |
| **DDR** | VAA1V8_VDD2H_DDR | -0.3V | 1.98V |
| | VDD2H_DDR | -0.3V | 1.12V |
| | VDDQ_DDR | -0.3V | 0.57V |
| | VDD0V8_DDR | -0.3V | 0.88V |
| | AVDD08_DSI | -0.3V | 0.88V |
| | AVDD12_DSI | -0.3V | 1.32V |
| | AVDD18_DSI | -0.3V | 1.96V |
| **EDP** | AVDD18_EDP0 | -0.3V | 1.98V |
| | DVDD08_EDP0 | -0.3V | 0.88V |
| **EDP1** | AVDD18_EDP1 | -0.3V | 1.98V |
| | DVDD08_EDP1 | -0.3V | 0.88V |
| **EMMC** | AVDD08_EMMC | -0.3V | 0.88V |
| | VCC18_EMMC | -0.3V | 1.98V |
| **FUSE** | FUSE_AVDD18 | -0.3V | 1.96V |
| **GPIO** | VCC18_GPIO1 | -0.3V | 1.98V |
| | VCC18_GPIO2 | -0.3V | 1.98V |
| | VCC18_GPIO3 | -0.3V | 1.98V |
| | VCC18_GPIO4 | -0.3V | 1.98V |
| | VCC18_GPIO5 | -0.3V | 1.98V |
| | VCC18_PMIC | -0.3V | 1.98V |
| | VCC1833_GPIO1 | -0.3V | 1.98V/3.63V |
| | VCC1833_GPIO2 | -0.3V | 1.98V/3.63V |
| | VCC1833_GPIO4 | -0.3V | 1.98V/3.63V |
| | VCC1833_GPIO5 | -0.3V | 1.98V/3.63V |
| | VCC1833_QSPI | -0.3V | 1.98V/3.63V |
| | VCC1833_MMC1 | -0.3V | 1.98V/3.63V |
| **OSC** | AVDD08_OSC | -0.3V | 0.88V |
| | AVDD18_OSC | -0.3V | 1.96V |
| **PICE PHY0** | AVDD08_PCIeA | -0.3V | 0.88V |
| | AVDD18_PCIeA | -0.3V | 1.98V |
| **PICE PHY1** | AVDD08_PCIeB | -0.3V | 0.88V |
| | AVDD18_PCIeB | -0.3V | 1.98V |
| **PICE PHY2** | AVDD08_PCIeC/USB3-B | -0.3V | 0.88V |
| | AVDD18_PCIeC/USB3-B | -0.3V | 1.98V |
| **PICE PHY3** | AVDD08_PCIeD/USB3-C | -0.3V | 0.88V |
| | AVDD18_PCIeD/USB3-C | -0.3V | 1.98V |
| **PICE PHY4** | AVDD08_PCIeE/USB3-D | -0.3V | 0.88V |
| | AVDD18_PCIeE/USB3-D | -0.3V | 1.98V |
| **PICE PHY5** | AVDD08_PCIe5 | -0.3V | 0.88V |
| | AVDD18_PCIe5 | -0.3V | 1.98V |
| **UCIE** | UCIE_VCCAON_0V8 | -0.3V | 0.84V |
| | UCIE_VCCIO_0V8 | -0.3V | 0.84V |
| | UCIE_VCCPLL_1P2V | -0.3V | 1.236V |
| | UCIE_VDD_0V8 | -0.3V | 0.84V |
| | UCIE_VDDBH_0V9 | -0.3V | 0.945V |
| | UCIE_VDDVPH0_0V9 | -0.3V | 0.945V |
| **UFS** | UFS_VCC_1V8 | -0.3V | 1.96V |
| | UFS_VCCQ_1V2 | -0.3V | 1.32V |
| | UFS_VDDU_0V8 | -0.3V | 0.88V |
| **USB2** | AVDD08_B_USB20 | -0.3V | 0.88V |
| | AVDD08_C_USB20 | -0.3V | 0.88V |
| | AVDD08_D_USB20 | -0.3V | 0.88V |
| | AVDD08_USB20_Host | -0.3V | 0.88V |
| | AVDD18_B_USB20 | -0.3V | 1.98V |
| | AVDD18_C_USB20 | -0.3V | 1.98V |
| | AVDD18_D_USB20 | -0.3V | 1.98V |
| | AVDD18_USB20_Host | -0.3V | 1.98V |
| | AVDD33_B_USB20 | -0.3V | 3.63V |
| | AVDD33_C_USB20 | -0.3V | 3.63V |
| | AVDD33_D_USB20 | -0.3V | 3.63V |
| | AVDD33_DRD_USB | -0.3V | 3.63V |
| | AVDD33_USB20_Host | -0.3V | 3.63V |
| **USB3-DRD** | AVDD08_DRD_USB | -0.3V | 0.88V |
| | AVDD18_DRD_USB | -0.3V | 1.98V |

#### 5.2.2 封装参数

| 项目（Item） | 符号（Symbol） | 最小值（Min） | 最大值（Max） |
| --- | --- | --- | --- |
| 工作温度（工业级标准） | Ta | -40°C | 85°C |
| 结温 | Tj | N/A | 125°C |
| 存储温度 | Tstg | -40°C | 125°C |

### 5.3 热特性

热阻：0.23℃/W （带散热盖）

### 5.4 引脚最大电流

TBD

### 5.5 上电/掉电时序

TBD

## 6. 回流焊温度曲线

TBD