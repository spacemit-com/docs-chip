---
sidebar_position: 2
---

# K3 数据手册（评估版）

## 版权声明

**版权所有 ©2026 进迭时空（杭州）科技有限公司。保留一切权利。**

非经进迭时空（杭州）科技有限公司（**进迭时空**）书面许可，任何单位和个人不得擅自以任何形式摘抄、复制、传播本文档的部分或全部内容。
本文档所载的所有资料和内容的版权均为进迭时空和/或其子公司所有，但注明引用其他方的内容除外（如有）。

由于产品版本升级或其他原因，本文档内容会不定期进行更新。除非另有约定，本文档仅作为使用指导，本文档所提供的信息和建议不构成任何明示或暗示的担保。在法律允许的范围内，进迭时空不对因本文档所造成的任何形式的损害负责。

## 评估版本说明

<span style="color: red; font-weight: bold;">本文档为 评估版本，仅供技术参考与评估使用。</span>
<span style="color: red; font-weight: bold;">本文档所描述的产品仍处于开发或最终验证阶段。文中所载规格、参数、性能指标及功能描述均为阶段性信息，可能在最终版本发布前进行修改、优化或删除，请持续关注文档修订记录。</span>
<span style="color: red; font-weight: bold;">本文档不构成最终产品规格说明，不得作为量产设计、商业部署或生产交付的依据。</span>
<span style="color: red; font-weight: bold;">进迭时空有权随时自行决定对本文档或相关产品进行更新、修订、暂停或撤回，且无需承担任何责任。</span>
<span style="color: red; font-weight: bold;">文中任何计划性的发布安排（包括但不限于 V1.0 版本发布时间）仅供规划参考，不构成具有法律约束力的承诺或合同义务。</span>
<span style="color: red; font-weight: bold;">本文档内容不构成销售要约、产品路线图承诺或具有法律约束力的技术规格保证。</span>

## 免责声明

除非另有书面约定，本文档所提供的信息按“现状（AS IS）”提供。
进迭时空不提供任何形式的明示或默示担保，包括但不限于适销性、特定用途适用性、不侵权性或性能保证。
本文档仅作为信息参考，不构成任何合同权利或义务。

## 责任限制

在法律允许的最大范围内，进迭时空不对因以下情形产生的任何直接、间接、附带、特殊、后果性或惩罚性损害承担责任：
- 使用本文档，
- 依赖本文档信息，
- 或基于本文档进行产品设计、开发或制造

用户应自行承担使用本文档所带来的全部风险。

---

## 修订记录

> 以下修订记录仅供参考，未必涵盖所有变更。规格及产品信息如有调整，恕不另行通知。

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">
  <colgroup>
    <col width="200">
    <col width="200">
    <col width="600">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">版本号</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">日期</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">修订说明</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- Row 1 -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;"><b>V0.9</b></td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">2026.02.28</td>
      <td style="padding: 8px; text-align: left; border: 1px solid #dfe2e5;">评估版本发布</td>
    </tr>
  </tbody>
</table>

---

## 1. 概述

### 1.1 产品简介

SpacemiT Key Stone K3 系列芯片采用 RISC-V 同构融合计算技术，成进迭时空的 8 个高性能计算大核 X100 及 8 个超宽并行计算 AI 核 A100，可提供 130 KDMIPS 通用算力及 60TOPS 通用 AI 算力，可流畅运行 300 亿参数模型。
K3 系列芯片主要应用在 AI 消费硬件如 AI 智慧家居、AI 会议办公、AI 内容创作、AI 电商零售等领域。

### 1.2 主要特性

**理器子系统**  

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
- 支持 4K@120fps 视频解码与 4K@60fps 视频编码（兼容 H.265、H.264 及 VP9 编解码格式）  
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
- AI 计算性能：60 TOPS（@FP4 sparse）  
- RISC-V 合规性：完全符合 RISC-V RVA23* 标准  
- 缓存架构：  
  - 每核心配备 32 KB L1 指令缓存（I-Cache）和 32 KB L1 数据缓存（D-Cache）  
  - 每簇共享 1 MB L2 缓存  
  - 每簇配备 1.5 MB 片上暂存存储器（Scratchpad）  
  - L1 D-Cache 支持 MESI 一致性协议  
  - L2 Cache 支持 MOESI 一致性协议  
- 向量扩展：RVV 1.0，VLEN = 1024  
- 高级中断架构（AIA）：  
  - M 模式 MSI：512
  - S 模式 MSI：512
- 中断控制器：支持 ACLINT 与 APLIC，共支持 512 个中断源  
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
视频处理单元（Video Processing Unit, VPU）是一款四核视频加速器，支持多种视频标准的编解码操作。VPU 内置一个主机 CPU，运行固件以控制硬件引擎，负责比特流解析、子模块调度及错误恢复等任务。

VPU 最高可运行于 1 GHz，支持广泛的视频标准，包括 H.265、H.264、VP8、VP9、MPEG4、MPEG2 和 H.263。典型并发操作能力包括：
- 同时进行 4K@60fps 编码与解码  
- 4K@60fps H.264/H.265 编码  
- 4K@120fps H.264/H.265 解码  

各视频编解码标准的实际处理由专用硬件逻辑完成。宏块序列控制器（Macroblock Sequencer）作为主控单元，负责调度各子模块的处理流程，从而减轻处理器负载并简化固件复杂度。

此外，多个独立于标准的模块在运行时共享通用逻辑，确保在不同的视频标准下都能实现高效率和流畅的性能。

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
- 编码性能：4K@60fps
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
- 编码性能：4K@60fps
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
- 编码性能：4K@60fps
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
- 编码性能：4K@60fps
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
- VP9：Profile 0  
- VC-1：Simple Profile（SP）、Main Profile（MP）、Advanced Profile（AP）  
- MPEG-4：Simple Profile（SP）、Advanced Simple Profile（ASP）  
- MPEG-2：Main Profile（MP）  
- H.263：Profile 0

**HEVC（H.265）解码特性**  
- 完全符合 Main Profile  
- 解码性能：4K@120fps
- 最大帧尺寸：4096 × 4096 像素

**H.264 解码特性**
- 完全符合 Baseline、Main、High 及 High 10 Progressive Profiles  
- 解码性能：4K@120fps
- 无论 NAL 数据包格式设置如何，始终启用转义选项，以防止模拟网络抽象层 (NAL) 单元起始码  

> **注意**：更多细节请参见 ITU-T H.264 Annex B: VC-1 Compressed Video Bitstream Format and Decoding Process

**VP8 解码特性**  
- 完全符合 VP8 规范  
- 解码性能：4K@120fps
- 最大帧尺寸：2048 × 2048 像素

**VP9 解码特性**  
- 完全符合 Profile 0  
- 解码性能：4K@120fps
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
        源 / 目标<br><span style="font-weight: normal; font-size: 0.8em; color: #555;">Source / Destination</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        片上内存<br><span style="font-weight: normal; font-size: 0.8em; color: #555;">Internal Memory</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        片外内存<br><span style="font-weight: normal; font-size: 0.8em; color: #555;">External Memory</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        片上外设<br><span style="font-weight: normal; font-size: 0.8em; color: #555;">Internal Peripheral</span>
      </th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">
        片外外设<br><span style="font-weight: normal; font-size: 0.8em; color: #555;">External Peripheral</span>
      </th>
    </tr>
  </thead>
  
  <tbody>
    <!-- Row 1: Internal Memory -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; font-size: 13px;">
        片上内存<br><span style="font-weight: normal; font-size: 0.85em;">Internal Memory</span>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">直通模式</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <!-- Row 2: External Memory -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; font-size: 13px;">
        片外内存<br><span style="font-weight: normal; font-size: 0.85em;">External Memory</span>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">直通模式</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">直通模式</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <!-- Row 3: Internal Peripheral -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; font-size: 13px;">
        片上外设<br><span style="font-weight: normal; font-size: 0.85em;">Internal Peripheral</span>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">直通模式</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">直通模式</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <!-- Row 4: External Peripheral -->
    <tr>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; font-size: 13px;">
        片外外设<br><span style="font-weight: normal; font-size: 0.85em;">External Peripheral</span>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">直通模式</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">直通模式</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
  </tbody>
</table>

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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">
  <colgroup>
    <col width="100">
    <col width="300">
    <col width="600">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">编号</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">复位方案</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">说明</th>
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
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">启动模式</th>
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

> **注意**：表中 “x” 表示该引脚状态 不影响 启动模式选择。

## 3. 封装（Package）

### 3.1 概述

K3 提供以下封装选项：

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">封装类型</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">尺寸</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚间距 (Pitch)</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚数量 (阵列)</th>
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

相关封装外形图（Package Outline Drawing, POD）详见下节。

### 3.2 封装外形图（POD）

<img src="static/package1.png" alt="" width="500">

<img src="static/package2.png" alt="" width="800">

## 4. 引脚定义（Pinout）

### 4.1 引脚分布图与说明

K3 的完整引脚分布图如下所示：
<img src="static/k3_pinmap.png" alt="" width="900">

为便于描述，K3 的引脚按 四个象限（Quadrant） 进行划分。以下各小节将基于该分区方式，详细说明各引脚的功能定义。

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
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 8px 4px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 8px 4px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PCIE0_TX0N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIE0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_B_USB20</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXCKN_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDDBH_0V9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCPLL_1P2V</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXCKP_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCIO_0V8</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXCKSB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_21</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_45</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_25</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_50</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_29</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_32</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_57</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_34</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_60</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">A39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_66</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PCIE0_TX0P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">L40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_72</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_M</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_USB20_HOST</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXCKP_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDDVPH0_0V9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDDVPH0_0V9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXCKN_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_22</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_26</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_46</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_30</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_51</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_58</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_33</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_38</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_61</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">B40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_67</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">M40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_73</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXTRK_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXTRK_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_23</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">DTEST_PAD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_27</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">ATEST_PAD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_31</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_52</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_35</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_62</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_36</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">N40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_74</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">C40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_40</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PCIE0_RX1P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXVLD_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_28</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_37</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_DS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_39</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_63</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">D40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_41</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_68</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PCIE0_RX1N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">P40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_75</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATASB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_OSC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_O_CKNT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_OSC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXCKSB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATASB_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]_24</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PMIC_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PMIC_WDT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_CLK</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_CMD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TRST_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">E40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D5</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">R40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PCIE0_RX0P</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL234</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_O_CKPT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_OSCPLL234567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXVLD_M0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC1833_GPIO2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_FUSE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TMS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EXT_32K_IN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">T40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D7</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDI</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">F40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PCIE/USB3_RCAL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_USB20_HOST</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL234</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PCIE0_RX0N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_PMIC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_TXDATA_M0[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_PMIC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_RXDATA_M0[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">EMMC_D0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TCK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">U40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">RESET_IN_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD18_PLL567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">G40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PLL567</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD33_B_USB20</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_ATEST</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_BGR_EAREFCLKN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDD_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_EW_VCTRL_EXT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_GPIO3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D3N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_42</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D3P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_47</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_53</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D2N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_55</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">V40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D2P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_54</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">H40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_69</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIE0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCAON_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCAON_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_BGR_EAREFCLKP</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VDD_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">XI_PAD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_OSCPLL234567</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_43</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_48</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI3_CLKN</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI3_CLKP</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_56</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">W40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_59</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_64</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">J40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_70</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K21</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_PCIE0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K22</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVDD08_USB20_HOST</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K23</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K24</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_PCIEUSB</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K25</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCAON_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K26</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCPLL_1P2V</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K27</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC_SYS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K28</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K29</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K30</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">UCIE_VCCIO_0V8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCC18_EMMC</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K31</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS_UCIE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K32</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">XO_PAD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K33</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_OSCPLL234567</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y36</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D1P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K34</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_44</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y37</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D1N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K35</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_49</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">AVSS_MIPI012</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K38</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VSS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D0P</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K39</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_65</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">Y40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MIPI_CSI2_D0N</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">K40</td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]_71</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;"></td>
      <td style="padding: 6px 4px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;"></td>
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
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
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
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">引脚编号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">引脚名称</th>
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

### 4.2 I/O 引脚电气参数

#### 4.2.1 1.8V I/O 引脚

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333; margin-bottom: 20px;">

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
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">电源域</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">符号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">参数说明</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">最小值 (Min)</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">典型值 (Typ)</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">最大值 (Max)</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- 1.8V Input Section -->
    <tr>
      <td rowspan="5" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">1.8V 输入</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vih</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输入高电平阈值</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC×0.7V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">1.8V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC+0.2V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输入低电平阈值</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">-0.3V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC×0.3V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpu</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">上拉电阻</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">55kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">79kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">121kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpd</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">下拉电阻</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">51kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">87kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">169kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Iil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输入漏电流（引脚配置为输入模式）</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10µA</td>
    </tr>
    <!-- 1.8V Output Section -->
    <tr>
      <td rowspan="10" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">1.8V 输出</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Voh</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输出高电平电压</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC−0.2V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vol</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输出低电平电压</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0.2V</td>
    </tr>
    <!-- IOL Rows -->
    <tr>
      <td rowspan="4" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Iol<br><span style="font-size:11px; color:#666;">DCS[1:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.2V） (<strong>DCS=00</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">13mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.2V） (<strong>DCS=01</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">25mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.2V） (<strong>DCS=10</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">37mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.2V） (<strong>DCS=11</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">49mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <!-- IOH Rows -->
    <tr>
      <td rowspan="4" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Ioh<br><span style="font-size:11px; color:#666;">DCS[1:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.2V） (<strong>DCS=00</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">11mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.2V） (<strong>DCS=01</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">21mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.2V） (<strong>DCS=10</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">32mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.2V） (<strong>DCS=11</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">42mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
  </tbody>
</table>

#### 4.2.2 3.3V I/O 引脚

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
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">电源域</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">符号</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">参数说明</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">最小值 (Min)</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">典型值 (Typ)</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">最大值 (Max)</th>
    </tr>
  </thead>
  
  <tbody>
    <!-- 3.3V Input Section -->
    <tr>
      <td rowspan="5" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">3.3V 输入</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vih</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输入高电平阈值</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">2V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">VCC+0.3V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输入低电平阈值</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">-0.3V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0.8V</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpu</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">上拉电阻</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">26kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">47kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">72kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Rpd</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">下拉电阻</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">27kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">54kΩ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">267kΩ</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Iil</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输入漏电流</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10µA</td>
    </tr>
    <!-- 3.3V Output Section -->
    <tr>
      <td rowspan="18" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; font-weight: bold; vertical-align: middle;">3.3V 输出</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Voh</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输出高电平电压</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">2.4V</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">Vol</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">输出低电平电压</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">0.4V</td>
    </tr>
    <!-- IOL Rows (8 configurations) -->
    <tr>
      <td rowspan="8" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Iol<br><span style="font-size:11px; color:#666;">DS[2:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=000</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">7mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=001</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=010</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">14mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=011</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">18mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=100</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">21mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=101</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">24mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=110</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">28mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">低电平输出电流（Vpad=0.4V） (<strong>DS=111</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">31mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <!-- IOH Rows (8 configurations) -->
    <tr>
      <td rowspan="8" style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5; vertical-align: middle;">Ioh<br><span style="font-size:11px; color:#666;">DS[2:0]</span></td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=000</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">7mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=001</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">10mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=010</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">13mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=011</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">16mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=100</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">19mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=101</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">23mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=110</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">26mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">高电平输出电流（Vpad = VCC - 0.5V） (<strong>DS=111</strong>)</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">29mA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
    </tr>
  </tbody>
</table>

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

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">
  <!-- 列宽定义：100 + 100 + 800 = 1000px -->
  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">信号/引脚</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">类型</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">描述</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TCK</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">主 JTAG 接口 1 的测试时钟。用于 JTAG 测试接口上的所有数据传输。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDI</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">主 JTAG 接口 1 的测试数据输入。用于将数据从 JTAG 调试器发送至 K3 处理器。该引脚内置上拉电阻。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDO</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">主 JTAG 接口 1 的测试数据输出。用于将数据从 K3 处理器返回至 JTAG 调试器。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TMS</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">主 JTAG 接口 1 的测试模式选择。用于从 JTAG 调试器选择所需的测试模式。该引脚内置上拉电阻。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TRSTn</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">主 JTAG 接口 1 的测试复位信号。符合 IEEE 1149.1 标准，用于触发 JTAG 复位。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_OUT</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">24 MHz VCXO 输出时钟</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_REQ</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">OCLK1 时钟请求信号</td>
    </tr>
  </tbody>
</table>

#### 4.3.2 杂项（Miscellaneous）

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">信号/引脚</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">类型</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">描述</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MPLL_TST_CK</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">—</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PLL 测试引脚</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MN_CLK_OUT</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">分数分频（M/N）时钟输出。由主 PMU 提供的通用 M/N 分数分频器产生的时钟信号。若需在 GPIO[122]（即 MN_CLK_OUT）上输出 13 MHz 时钟，必须将 <code>CLK_REQ</code> 配置为 <strong>Function 0</strong> 并拉高。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Sleep_OUT</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">PMIC 睡眠设置</td>
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
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">信号/引脚</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">类型</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">描述</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">SPIx_FRM</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">同步串行端口帧信号 0/2。串行帧同步可配置为输出（主模式）或输入（从模式）。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">SPIx_RXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">同步串行端口接收数据 0/2。串行数据在位时钟作用下锁存。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">SPIx_SCLK</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">同步串行端口时钟 0/2。串行位时钟可配置为输出（主模式）或输入（从模式）。</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">SPIx_TXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">同步串行端口发送数据 0/2。串行数据随位时钟同步驱动输出。</td>
    </tr>
  </tbody>
</table>

#### 4.3.4 TWSI

**专用信号（Dedicated）**

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">信号/引脚</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">类型</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">描述</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SDA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSI 串行数据/地址线</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SCL</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSI 串行时钟线</td>
    </tr>
  </tbody>
</table>

**通用信号（Common）**

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="100">
    <col width="100">
    <col width="800">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">信号/引脚</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">类型</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">描述</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">I²Cx_SCL</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O, OD</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSIx 时钟线</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">I²Cx_SDA</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O, OD</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">TWSIx 数据线</td>
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
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">信号/引脚</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">类型</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">描述</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">UARTx_CTSn</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx Clear-To-Send（清除发送）</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">UARTx_RTSn</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx Request-To-Send（请求发送）</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">UARTx_RXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx 接收数据</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">UARTx_TXD</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">UARTx 发送数据</td>
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
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">信号/引脚</th>
      <th style="padding: 10px 8px; text-align: center; border: 1px solid #dfe2e5;">类型</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">描述</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">USBx_N</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB D± 差分信号（负）</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">USBx_P</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I/O</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB D± 差分信号（正）</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">VBUS_ON</td>
      <td style="padding: 6px 8px; text-align: center; border: 1px solid #dfe2e5;">I</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">USB VBUS 供电检测指示</td>
    </tr>
  </tbody>
</table>

### 4.4 多功能 I/O 引脚分配

通用输入/输出（GPIO）模块提供灵活的引脚控制与信号复用能力。每个 GPIO 引脚既可作为标准输入/输出使用，也可配置为多种 **备用功能（Alternate Function）** 之一，从而高效连接系统与片上外设。

下表按接口分组，详细列出了 **Function 0 至 Function 6** 的信号分配情况。

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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上/下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">QSPI_DAT3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">QSPI_DAT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">QSPI_DAT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">QSPI_DAT0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">QSPI_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">QSPI_CS0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CS0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">QSPI_CS1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CS1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上/下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">MMC1_DAT3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[93]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDI</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">MMC1_DAT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[94]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TMS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">MMC1_DAT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[95]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">MMC1_DAT0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[96]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">MMC1_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[97]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">MMC1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">RESET_IN_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EXT_32K_IN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R_PWR_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM12</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R_PWR_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM13</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">VCXO_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">NO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM14</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PMIC_WDT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PMIC_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PMIC_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM16</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SSP_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[120]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SSP_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[121]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SSP_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[122]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PWR_SSP_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[123]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PRI_TDI</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PRI_TMS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PRI_TCK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PRI_TDO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">PRI_TRST_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D0</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D1</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D2</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D3</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D4</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D5</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D6</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_D7</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_DS</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_CLK</td>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">EMMC_CMD</td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA5_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[6]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM6</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[7]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM7</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_ALERT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[8]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[9]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM9</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[10]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM10</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[11]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[12]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[13]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM13</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[14]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM14</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[15]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_RXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[16]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[16]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_TXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[17]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[17]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_CRS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_ID</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[18]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[18]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_COL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_VBUSON</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[19]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[19]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_PPS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART1_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DRV</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[20]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[20]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC0_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[21]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[21]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM15</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[28]</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[22]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[22]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM16</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[29]</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[23]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[23]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM17</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[24]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[24]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM18</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[25]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[25]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM19</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[26]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[26]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART7_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[27]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[27]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[28]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[28]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[29]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[29]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[30]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[30]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EDP0_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[31]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[31]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EDP1_HPD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[32]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[32]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[33]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[33]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM6</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[34]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[34]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM7</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[35]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[35]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM8</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[36]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[36]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM9</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[37]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[37]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_RXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[38]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[38]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_TXER</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[39]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[39]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_CRS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[40]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[40]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_COL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA1_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR0_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[41]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[41]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC1_PPS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK32K_OUT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;"></td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[42]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[42]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[43]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[43]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[44]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[44]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[45]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[45]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[46]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[46]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[47]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[47]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART10_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM5</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[48]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[48]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[49]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[49]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM7</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[50]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[50]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_MRLn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM8</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[51]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[51]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATNLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[52]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[52]/Strap[5]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM10</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[53]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[53]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM11</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[54]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[54]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINTEG</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM12</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[55]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[55]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM13</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[56]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[56]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM14</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[57]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[57]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">EDP0_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM15</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[58]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[58]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GMAC2_PPS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM16</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[59]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[59]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RXDV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM17</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[60]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[60]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM18</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[61]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[61]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM19</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[62]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[62]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C6_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[63]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[63]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[18]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[64]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[64]/Strap[4]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_RX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[19]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM0</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[65]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[65]/Strap[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[20]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[66]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[66]/Strap[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[21]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[67]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[67]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[22]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK4</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeC_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[68]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[68]/Strap[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[69]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[69]/Strap[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_RXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[70]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[70]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_TX_EN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_SCLK</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[71]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[71]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_MDC</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR0_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_FRM</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[72]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[72]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_MDIO</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[73]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[73]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_INT_N</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA4_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.IR1_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[74]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[74]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GMAC3_CLK_REF</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_REQ</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30H-1_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[75]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[76]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[76]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[77]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[77]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[78]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[78]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeE_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[79]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[79]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART8_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[80]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[80]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA2_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[81]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[81]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[82]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[82]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[83]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[83]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART5_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[84]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[84]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_B_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[85]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[85]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART9_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_C_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[86]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[86]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DIR</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[87]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[87]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_MRLn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PRSNT2n</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[88]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[88]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_ATNLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_RXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[89]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[89]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PWRLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[90]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[90]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_RXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[91]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[91]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[23]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D0</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_EINTEG</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN0_TXD</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[92]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[92]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[24]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D1</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM5</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">DSI0_TE</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[93]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[93]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[25]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.eSPI0_ALERT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D2</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[94]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[94]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[26]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_D3</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[95]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[95]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[27]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_ID</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[96]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[96]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_VBUSON</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM2</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[97]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[97]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">eSPI0_RESETN</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM3</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[98]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
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
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">引脚名称</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">默认上下拉</th>
      <th style="padding: 8px 4px; text-align: center; border: 1px solid #dfe2e5;">边沿唤醒功能</th>
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
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[99]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[99]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK_CAMCK4</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[100]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[100]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CLK32K_OUT</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[101]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[101]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_CTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MNCLK_OUT1</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[102]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[102]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP3_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART4_RTS</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[103]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[103]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA3_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C1_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[104]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[104]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30H-1_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[105]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[105]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM17</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[106]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[106]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C1_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C3_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM18</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[107]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[107]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP2_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DIR</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PWM19</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[108]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[108]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB20_HOST_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">IR0_RX</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[109]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[109]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM6</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[110]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[110]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeA_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM7</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[111]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[111]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">ucie_deSCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_INT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM8</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[112]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[112]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">ucie_deSDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C4_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_D_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.PWM9</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[113]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[113]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[30]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[114]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[114]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[31]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[115]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[115]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA0_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[32]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SCL</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[116]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[116]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_SCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_ID</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[33]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C0_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PRSNT2n</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.I2C0_SDA</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[117]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[117]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.SSP1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_VBUSON</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[34]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_ATTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[118]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[118]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_RTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_DRV</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.GPIO[35]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PWRCTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[119]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[119]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_CTSn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">USB30_DRD_INT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_AUXen</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[120]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[120]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN3_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PWRDet</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[121]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[121]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C2_SDA</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.CAN3_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">CAN4_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_MRLn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[122]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[122]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[3]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_CLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_ATNLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[123]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[123]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[2]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_FRM</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">UART6_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">R.UART0_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_PWRLED</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[124]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[124]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[1]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_TXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_PERSTn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP0_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_EINT</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[125]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[125]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_DAT[0]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_RXD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_WAKEn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">e/DP1_HPD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeB_EINTEG</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[126]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">上拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">GPIO[126]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">MMC2_CMD</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">SSPA1_SYSCLK</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">PCIeD_CLKREQn</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace;">I2C5_SCL</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;"></td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5; font-family: monospace; font-weight: bold;">GPIO_[127]</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">下拉</td>
      <td style="padding: 6px 4px; text-align: center; border: 1px solid #dfe2e5;">启用</td>
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

### 4.5 多功能引脚寄存器（MFPRs）

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="150">
    <col width="200">
    <col width="150">
    <col width="150">
    <col width="200">
    <col width="150">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">MFPR ID</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">地址</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">偏移量</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">MFPR ID</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">地址</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">偏移量</th>
    </tr>
  </thead>
  
  <tbody>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_00</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E000</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_77</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E134</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x134</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_01</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E004</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_78</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E138</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x138</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_02</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E008</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_79</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E13C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x13C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_03</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E00C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_80</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E140</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x140</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_04</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E010</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_81</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E144</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x144</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_05</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E014</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_82</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E148</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x148</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_06</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E018</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_83</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E14C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x14C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_07</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E01C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_84</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E150</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x150</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_08</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E020</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_85</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E154</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x154</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_09</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E024</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_86</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E158</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x158</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_10</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E028</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_87</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E15C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x15C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_11</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E02C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x2C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_88</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E160</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x160</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_12</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E030</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_89</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E164</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x164</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_13</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E034</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_90</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E168</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x168</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_14</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E038</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_91</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E16C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x16C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_15</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E03C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x3C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_92</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E170</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x170</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_16</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E040</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_93</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E174</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x174</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_17</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E044</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x44</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_94</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E178</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x178</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_18</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E048</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x48</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_95</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E17C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x17C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_19</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E04C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x4C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_96</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E180</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x180</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_20</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E050</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x50</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_97</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E184</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x184</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_21</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E054</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x54</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_98</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E188</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x188</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_22</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E058</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x58</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_99</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E18C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x18C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_23</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E05C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x5C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_100</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E190</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x190</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_24</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E060</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x60</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_101</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E194</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x194</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_25</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E064</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x64</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_102</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E198</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x198</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_26</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E068</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x68</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_103</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E19C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x19C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_27</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E06C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x6C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_104</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1A0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1A0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_28</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E070</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x70</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_105</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1A4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1A4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_29</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E074</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x74</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_106</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1A8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1A8</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_30</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E078</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x78</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_107</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1AC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1AC</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_31</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E07C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x7C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_108</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1B0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1B0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_32</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E080</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x80</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_109</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1B4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1B4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_33</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E084</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x84</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_110</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1B8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1B8</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_34</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E088</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x88</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_111</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1BC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1BC</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_35</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E08C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x8C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_112</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1C0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1C0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_36</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E090</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x90</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_113</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1C4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1C4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_37</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E094</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x94</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_114</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1C8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1C8</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_38</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E098</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x98</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_115</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1CC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1CC</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_39</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E09C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x9C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_116</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1D0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1D0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_40</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0A0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xA0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_117</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1D4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1D4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_41</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0A4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xA4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_118</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1D8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1D8</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_42</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0A8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xA8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_119</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1DC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1DC</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_43</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0AC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xAC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_120</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1E0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1E0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_44</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0B0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xB0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_121</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1E4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1E4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_45</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0B4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xB4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_122</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1E8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1E8</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_46</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0B8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xB8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_123</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1EC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1EC</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_47</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0BC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xBC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_124</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1F0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1F0</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_48</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0C0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xC0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_125</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1F4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1F4</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_49</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0C4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xC4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_126</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1F8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1F8</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_50</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0C8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xC8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_127</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E1FC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x1FC</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_51</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0CC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xCC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SCL</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E200</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x200</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_52</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0D0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SDA</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E204</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x204</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_53</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0D4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">VCXO_EN</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E208</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x208</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_54</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0D8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PMIC_INT_N</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E214</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x214</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_55</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0DC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xDC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E218</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x218</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_56</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0E0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xE0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E21C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x21C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_57</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0E4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xE4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E220</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x220</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_58</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0E8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xE8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_DAT0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E224</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x224</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_59</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0EC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xEC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_CMD</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E228</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x228</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_60</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0F0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xF0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">MMC1_CLK</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E22C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x22C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_61</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0F4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xF4</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E230</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x230</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_62</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0F8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xF8</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E234</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x234</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_63</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E0FC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xFC</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT2</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E238</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x238</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_64</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E100</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x100</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_DAT3</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E23C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x23C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_65</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E104</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x104</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CS0</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E240</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x240</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_66</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E108</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x108</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CS1</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E244</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x244</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_67</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E10C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x10C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">QSPI_CLK</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E248</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x248</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_68</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E110</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x110</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDI</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E24C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x24C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_69</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E114</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x114</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TMS</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E250</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x250</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_70</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E118</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x118</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TCK</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E254</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x254</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_71</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E11C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x11C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PRI_TDO</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E258</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x258</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_72</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E120</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x120</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_SCLK</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E25C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x25C</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_73</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E124</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x124</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_FRM</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E260</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x260</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_74</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E128</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x128</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_TXD</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E264</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x264</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_75</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E12C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x12C</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">PWR_SSP_RXD</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E268</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x268</td></tr>
    <tr><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">GPIO_76</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0xD401E130</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">0x130</td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;"></td><td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;"></td></tr>
  </tbody>
</table>

## 5. 电气特性

### 5.1 引脚交流/直流工作条件

下表列出了推荐的工作条件。

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
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">模块（Module）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">符号/引脚（Symbol/Pin）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">最小值（Min）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">典型值（Typ）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">最大值（Max）</th>
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

### 5.2 绝对最大直流额定值

#### 5.2.1 引脚参数

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">模块（Module）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">符号/引脚（Symbol/Pin）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">最小值（Min）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">最大值（Max）</th>
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

#### 5.2.2 封装参数

<table width="1000" style="table-layout: fixed; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 13px; color: #333;">

  <colgroup>
    <col width="250">
    <col width="250">
    <col width="250">
    <col width="250">
  </colgroup>
  
  <thead>
    <tr style="background-color: #f6f8fa; border-bottom: 2px solid #dfe2e5;">
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">项目（Item）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">符号（Symbol）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">最小值（Min）</th>
      <th style="padding: 10px 8px; text-align: left; border: 1px solid #dfe2e5;">最大值（Max）</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">工作温度（工业级标准）</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Ta</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-40°C</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">85°C</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">结温</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Tj</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">N/A</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">125°C</td>
    </tr>
    <tr>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">存储温度</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5; font-family: monospace;">Tstg</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">-40°C</td>
      <td style="padding: 6px 8px; text-align: left; border: 1px solid #dfe2e5;">125°C</td>
    </tr>
  </tbody>
</table>

### 5.3 热特性

热阻：0.23℃/W （带散热盖）

### 5.4 引脚最大电流

TBD

### 5.5 上电/掉电时序

TBD

## 6. 回流焊温度曲线

TBD
