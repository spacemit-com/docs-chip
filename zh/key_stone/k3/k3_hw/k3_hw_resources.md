---
sidebar_position: 2
---

# K3 硬件资源

本节汇总 K3 芯片相关硬件资源文件，供硬件设计与系统开发使用。

## 管脚配置

### 管脚列表与复用（Pin List & Pinmux）

该文件包含全部管脚信息及其复用功能配置。  
[k3_pinlist_pinmux_v21.xlsx](https://cdn-resource.spacemit.com/file/chip/K3/k3_pinlist_pinmux_v21.xlsx)

### 管脚映射（Pin Map）

该文件描述封装物理管脚与芯片内部模块/接口之间的对应关系。  
[k3_PINMAP_V1.1.xlsx](https://cdn-resource.spacemit.com/file/chip/K3/k3_PINMAP_V1.1.xlsx)

## 时序配置

### 管脚延时（Pin Delay）

该文件用于高速接口的输入/输出时序延时配置。  
[k3_pin_delay_V1.0.xlsx](https://cdn-resource.spacemit.com/file/chip/K3/k3_pin_delay_V1.0.xlsx)

## 封装信息

### POD（封装外形图 / Package Outline Drawing）

该文件包含封装尺寸、BGA 球阵列、球间距及机械规格等信息。  
[k3_pod.pdf](https://cdn-resource.spacemit.com/file/chip/K3/k3_pod.pdf)

## 最小系统参考设计

### PCB 参考设计

该文件提供 K3 最小系统的 PCB 参考设计。
[K3_10L_minisys_2HDI.brd](https://cdn-resource.spacemit.com/file/chip/K3/K3_10L_minisys_2HDI.brd)

### 原理图

提供最小系统参考设计的原理图文件。

> 待补充
> - [下载原理图工程文件（DSN 格式）]()
> - [下载原理图（PDF 格式）]()

### 设计检查清单

用于指导硬件设计规范性审查与量产前验证。

- [原理图设计 Checklist](https://cdn-resource.spacemit.com/file/chip/K3/K3_Schematic_checklist-V1.0-20240417.xlsx)
- [PCB 设计 Checklist](https://cdn-resource.spacemit.com/file/chip/K3/K3_Layout_checklist-V1.0-20260417.xlsx)
- [硬件测试 Checklist](https://cdn-resource.spacemit.com/file/chip/K3/K3_Hardware_Tests_checklist-V1.0-20251028.xlsx)
