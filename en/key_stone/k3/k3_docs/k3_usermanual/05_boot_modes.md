---
sidebar_position: 6
---

# 5. Boot Modes

## 5.1 Introduction

K3 supports booting from:
- SPI NAND Flash
- SPI NOR Flash
- eMMC
- UFS
- SD/TF Card

## 5.2 Bootstrapping Pins

The boot process of K3 is controlled by a set of bootstrapping pins, which can be configured to determine the boot mode and other operating parameters. The definitions of the bootstrapping pins are listed below.

| Pin Name | Bootstrapping Pin | Default Value |
| --- | --- | --- |
| GPIO_65 | STRAP[0] | 0 |
| GPIO_66 | STRAP[1] | 0 |
| GPIO_68 | STRAP[2] | 0 |
| GPIO_69 | STRAP[3] | 0 |
| GPIO_64 | STRAP[4] | 0 |
| GPIO_52 | STRAP[5] | 0 |

Details about the purpose of the different configurations of the bootstrapping pins are provided in the following subsections.

### 5.2.1 Boot Mode Selection
The boot mode is selected based on the state of the STRAP[0] and STRAP[1] pins, as shown below.

| No. | STRAP[1] | STRAP[0] | Boot Mode |
| --- | --- | --- | --- |
| 1 | Down | Down | SD/TF Card → eMMC (default) |
| 2 | Up | Down | SD/TF Card → SPI NAND Flash |
| 3 | Down | Up | SD/TF Card → SPI NOR Flash |
| 4 | Up | Up | SD/TF Card → UFS |

### 5.2.2 Download Mode Selection

The download mode is selected based on the state of the STRAP[2] pin, as shown below.

| No. | STRAP[2] | Download Mode |
| --- | --- | --- |
| 1 | Down | USB (default) |
| 2 | Up | UART |

### 5.2.3 Boot Download Mode Selection
The boot download mode is selected based on the state of the STRAP[3] pin, as shown below.

| No. | STRAP[3] | Boot Download Mode |
| --- | --- | --- |
| 1 | Down | Boot mode as defined in **Boot Mode Selection** (default) |
| 2 | Up | Download mode as defined in **Download Mode Selection** |

### 5.2.4 SPI NAND/NOR Flash Boot Voltage Selection

The boot voltage of SPI NAND/NOR Flash is selected based on the state of the STRAP[4] pin, as shown below.

| No. | STRAP[4] | SPI NAND/NOR Flash Boot Voltage |
| --- | --- | --- |
| 1 | Up | 3.3V I/O |
| 2 | Down | 1.8V I/O |

### 5.2.5 DDR Type Selection

The DDR type is selected based on the state of the STRAP[5] pin, as shown below.

| No. | STRAP[5] | DDR Type |
| --- | --- | --- |
| 1 | Up | LPDDR4x |
| 2 | Down | LPDDR5 |