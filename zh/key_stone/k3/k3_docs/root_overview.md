sidebar_position: 1

# K3 产品简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/chip/K3/K3_brief_zh.pdf)**

## 概述

**K3 是运行 30B 大模型的高性能 RISC-V AI CPU**

SpacemiT Key Stone K3 系列芯片采用 RISC-V 同构融合计算技术，集成进迭时空的 8 个高性能计算大核 X100 及 8 个超宽并行计算 AI 核 A100，可提供 130 KDMIPS 通用算力及 60TOPS 通用 AI 算力，可流畅运行 300 亿参数模型。
K3 系列芯片主要应用在 AI 消费硬件如 AI 智慧家居、AI 会议办公、AI 内容创作、AI 电商零售等领域。

- **卓越的 CPU 性能**
  8 个高性能计算大核 X100，最大主频 2.4GHz，130KDMIPS 算力
  支持完整 RVA23 Profile，单核Specint2006>9.0/GHz，等效ARM-A76

- **通用 AI 算力**
  60TOPS AI算力，支持 BF16、FP16、FP8、INT8、INT4 等数据类型
  可流畅运行 30B 本地模型，综合智力性能是 235B 模型的 84%

- **最新的 RISC-V 架构，超级并行计算能力**
  A100 支持高达 1024bit 的 RVV 1.0 并行计算
  提供专用 TCM 缓存及 DMA 加速通道

- **丰富的IO扩展接口**
  集成多套高速扩展接口，灵活应对各类计算机扩展需求：
  8-lanes PCIe、4 套 USB3.0、4 套 GMAC 等

- **完整的硬件虚拟化**
  支持RV Hypervisor 1.0、RV AIA、RV IOMMU 扩展
  提供 CPU、内存、中断、IO 的完整硬件虚拟化能力

- **更高等级的安全防御技术**
  支持 M/S/U 三种处理器权限，硬件抵抗幽灵、熔断等攻击
  支持国密 SM2/3/4 硬件安全技术

- **符合工业级标准**
  在 -40˚C ～ 85˚C 的温度下仍能提供稳定可靠的持续算力输出，满足工业应用的苛刻环境需求

## 产品特性

- **八大核高性能 RISC-V 处理器**
  - 8 核 X100™ 64 位 RISC-V AI 处理器
  - X100™ 是四发射乱序执行的高性能计算大核
  - 每 8 核共享 8MB L2 Cache
- **60TOPS 通用 AI 算力**
  - 8 核 A100™ 提供 60TOPS AI 算力
  - 模型性能 > 10Tokens/S@30B
  - 支持 FP16、BF16、FP8、INT8、INT4 等数据格式
  - 支持所有 AI 算法和模型部署
- **RISC-V 硬件虚拟化**
  - 支持 RVH1.0 扩展，提供 CPU 及内存虚拟化能力
  - 支持 RV AIA 扩展，提供中断虚拟化能力
  - 支持 RV IOMMU 扩展，提供外设虚拟化能力
- **RISC-V 安全架构**
  - 支持 RISC-V PMP 和 ePMP，结合 RISC-V 特有的 IOPMP，实现高等级的安全防御能力
  - 支持安全启动、安全存储、签名校验
  - 支持 AES/SHA/RSA/SM2/SM3/SM4 等算法
  - 支持产品生命周期安全管理
- **内存**
  - 64-bit LPDDR5 - 6400Mbps
  - 64-bit LPDDR4x - 4266Mbps
  - 最大支持 32GB 内存容量，带宽可达 51GB/s
- **存储**
  - 支持 SPI 闪存
  - 支持 eMMC 5.1
  - 支持 UFS 2.2
  - 支持 SDIO3.0 SD 卡
  - 支持 SSD：NVMe over PCIe
- **实时 RISC-V 处理器**
  - 双核 RT24™-64 位 RISC-V 实时处理器
  - 六级单发按序流水线
- **多媒体和显示**
  - 集成 3D 图形引擎支持 Vulkan、OpenCL、OpenGLES 
  - 4K120fps H.265/H.264/VP9 等格式解码能力
  - 4K60fps H.265/H.264 等格式编码能力
  - 2 路 3840*2160@60fps 屏异显
  - MIPI-DSI 8Lane 显示输出，4.5Gbps/Lane
    - 支持 3840*2160@60fps
    - 支持 2560*1440@90fps
    - 支持 1920*1080@60fps 等
  - 2 路 DP/eDP 显示输出
    - 支持 3840*2160@60fps
    - 支持 2560*1440@144fps 等
  - 4 路 MIPI-CSI 12Lanes 4 + 4 +（ 2 + 2 ）
  - 支持 12 路摄像头输入
- **接口**
  - 8×PCIe lanes（8Gbps/Lane），5 套 PCIe 控制器
    - PCIe x8 支持 RC&EP 模式
    - 支持热插拔功能
  - 3× USB3.0 Host（Combo with PCIe、含 USB2.0）
  - 1× USB3.0 DRD（Type-C、含 USB2.0 OTG）
  - 1× USB2.0 Host
  - 4× GMAC（RGMII & RMII & MII）
    - 支持 TSN 协议
  - 6× SPI、2× eSPI、17× UART、10× Can-FD、9× I2C、30× PWM
- **功耗**
  - TDP：15W～25W

## 框图

![](./static/k3_block_diagram.png)
