---
sidebar_position: 2
---

# K3 硬件设计 Buglist

## 版本

| 版本 | 日期 | 修订说明 |
| --- | --- | --- |
| V1.0 | 2026.10.15 | 首版；针对[参数设计原理图](k3_hw_resources.md)和[硬件设计指南](k3_hw_design_guide.md)进行 Buglist 说明。 |

## 1. VDD0V8_DDR 设计要求 Buglist

### 1.1 设计可能问题

VDD0V8_DDR 由 VDD08_M1A100 经磁珠后供电。参考原理图中的磁珠 DCR 为 30 mΩ，额定电流为 5 A。

参考设计如下图所示。

![图片](./static/bug_00.png)

上述设计导致 VDD08_DDR 的末端压降经磁珠和 PCB 铜皮后与 VDD08_M1A100 压差大于 50mV（VDD08_DDR 最大电流约 2A），导致 VDD08_DDR 电压低于最低要求，从而导致 LPDDR5 读写出错，严重时会导致 OS 崩溃。

### 1.2 设计改进

#### 1.2.1 参考设计的快赢优化方案

如单板已按参考设计完成投板，并回板进行测试。短期的快赢方案把磁珠直接用焊锡短接，可缓解 LPDDR 的读写出错问题。问题必须通过长期解决方案彻底解决。

#### 1.2.2 参考设计的长期优化方案

VCC_SYS 和 VDD0V8_DDR 直接共用电源平面，不使用磁珠隔离。如下图拓扑所示。

![图片](./static/bug_01.png)

> **设计要求**
>
> VDD0V8_DDR 的纹波要求控制在 Vripple-pp ≤ 70 mV，建议 Vripple-min ≥ -35 mV、Vripple-max ≤ 35 mV。
>
> **噪声要求：** Vnoise-pp ≤ 140 mV，建议 Vnoise-min ≥ -70 mV、Vnoise-max ≤ 70 mV。
>
> 为满足该设计要求，需结合第 2 条 Buglist 统一考虑。

## 2. VCC_CPUX 和 VCC_SYS 的 CPU 核心电源设计要求 Buglist

### 2.1 设计可能问题

[硬件设计指南](k3_hw_design_guide.md)中的第 1.2.5 小节提到 X100/A100 分别独立供电。该设计的最优结果中，VCC_SYS（即 A100 电源）的纹波为：Vripple-pp > 130 mV、Vripple-min < -80 mV、Vripple-max > 50 mV。
芯片具有 16 个大核，分别为 X100 的 8 个核和 A100 的 8 个核。X100 和 A100 分别独立供电，由多相控制器的两个 rail 分别供电。

考虑到 VDD0V8_DDR 与 VCC_SYS 合并供电，该纹波不满足 VDD0V8_DDR 的设计要求。

### 2.2 设计改进

最新版[硬件设计指南](k3_hw_design_guide.md)已要求 X100/A100 合并供电。同一平面的 PCB 铜皮可大幅优化 PCB 上的 PDN，同时 X100/A100 的末端耦合电容可共同发挥作用。

验证结果可满足 Vripple-pp ≤ 70 mV 的设计要求。

> **注意事项**
>
> Vripple-pp 的最终结果与 PCB 设计、多相电源的动态响应特性及供电电容等因素强相关。内部验证结果表明该设计可达成设计目标。客户设计需充分考虑 Layout、电源选型和供电电容等因素的影响，建议进行 PI 仿真。
