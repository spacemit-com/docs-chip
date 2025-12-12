sidebar_position: 2

# K1 硬件文档中心

本页面为 **K1 平台** 的所有硬件文档与设计资源提供统一入口，便于开发者查阅与下载。

## 硬件设计指南

为硬件设计、板级点亮（Board Bring-up）以及系统集成提供的技术文档：

- **[硬件设计指南](./k1_hw_design_guide.md)**

## 硬件设计资源

### 原理图与 PCB 文件

基于 K1 平台的经验证、可量产的参考设计与设计检查项：

- **K1 最小系统参考设计**
  - [K1_minimum_system_schematic (PDF) – V3.1 (2024-06-20)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_minimum_system_schematic%28PDF%29-V3.1-20240620.pdf) – 最小系统参考原理图（PDF）
  - [K1_minimum_system_schematic (DSN) – V3.1 (2024-06-20)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_minimum_system_schematic%28DSN%29-V3.1-20240620.DSN) – OrCAD 原理图工程源文件
  - [K1_minimum_system_layout – V3.1 (2024-06-05)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_minimum_system_layout-V3.1-20240605.brd) – PCB Layout 工程源文件

- **设计检查项（Checklists）**
  - [K1_Schematic_Checklist – V1.2 (2025-07-09)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Schematic_checklist-V1.2-20250709.xlsx) – 原理图设计检查项
  - [K1_Layout_Design_Checklist – V1.1 (2025-07-09)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Layout_Design_Checklist-V1.1-20250709.xlsx) – PCB Layout 设计检查项

### 封装、引脚与电气资源

- **引脚配置与复用**
  - [K1X_Pin_Multiplex – V1.1 (2025-07-17)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1X_Pin_Multiplex-V1.1-20250717.xls) – 引脚复用配置表
  - [K1_Pinmap – V1.1 (2025-07-17)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_pinmap-V1.1-20250717.xlsm) – 完整芯片引脚定义（Pin Mapping）

- **信号时序与电气参数**
  - [K1_Pin_Delay – V1.2 (2024-09-26)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_pin_delay-V1.2-20240926.xlsx) – 引脚延时与时序特性

- **封装规格**
  - [K1_PODCSP – V1.0 (2024-03-01)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_PODCSP-V1.0-20240301.pdf) – CSP 封装规格及机械尺寸图
  - [M1_PODBGA – V1.0 (2024-04-24)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/M1_PODBGA-V1.0-20240424.pdf) – BGA 封装规格、球位（Ball Map）与焊盘设计建议

## 合格供应商列表（AVL）

**AVL（Approved Vendor List）** 包含经验证、可量产的 K1 平台兼容器件，包括但不限于：

- DDR  
- eMMC / UFS  
- Wi-Fi / Bluetooth 模组  
- SPI NOR / SPI NAND  
- LCD / 触摸屏  
- 摄像头模组  
- 传感器 / GPS  
- 其他可选外设

AVL 用于确保器件兼容性，辅助元器件选型，并支持供应链规划。

下载完整列表：

- **[K1 关键器件 AVL – V2.6 (2025-11-19)](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Key_Parts_AVL-V2.6-20251119.xlsm)**

