---
sidebar_position: 16
---

# 15. Security Subsystem

## 15.1 Crypto Engine

### 15.1.1 Overview

The Crypto Engine supports both internationally recognized cryptographic algorithms and China’s commercial cryptography standards.

### 15.1.2 Features

- Supports hash algorithms: SHA-1, SHA-224, SHA-256, SM3
- Supports symmetric algorithms: AES-128/192/256, SM4
  - Supports 3-stage key ladder for AES-128 and SM4
- Supports asymmetric algorithms: RSA-1024/2048/4096, ECC-128/256/512, SM2

## 15.2 TRNG

### 15.2.1 Overview

The True Random Number Generator (TRNG) complies with China’s commercial cryptography standards and provides high-quality random numbers for security applications.

### 15.2.2 Features

- Built-in 32-bit TRNG
- Ensures randomness, unpredictability, and non-reproducibility

## 15.3 eFuse

### 15.3.1 Overview

An integrated 4096-bit eFuse, divided into 16 banks of 256 bits each, with 256 bits available for user customization.

### 15.3.2 Features

- Supports eFuse bank locking
- Supports automatic hardware parameter loading
- Supports lifecycle management:
  - CM (Chip Manufacturing)
  - DM (Development Mode)
  - SP (Secure Production)
    - CPU cannot access AES keys; accessible only by the secure engine
  - RMA (Return Merchandise Authorization)
    - Forces JTAG debug mode to be enabled
    - Denies AES key access for all entities
  - Lifecycle priority: RMA > SP > DM > CM
- Supports secure boot configuration
- Supports encrypted boot configuration
- Supports storage of root keys and encryption-protected keys
- Supports 256-bit non-volatile counter (NV counter):
  - 224 bits for non-secure modules, 32 bits for secure modules

## 15.4 IOPMP

### 15.4.1 Overview

The IOPMP (I/O Physical Memory Protection) module is designed in coordination with the PMP to ensure secure access control across the platform peripherals.

While the PMP validates bus accesses initiated by RISC-V cores, the IOPMP verifies transactions issued by other bus masters or subsystems.

Configured exclusively by the secure world, the IOPMP defines access permissions and attributes for transactions initiated by non-CPU masters.

All transactions initiated by the slave devices of an IOPMP are subject to that IOPMP instance, and access is granted only when the permission verification passes.
  
### 15.4.2 Features

- Supports access control for read, write, and execute permissions
- Bus requests incur a one-cycle delay after permission checking
- Supports logging of access violation information
- Supports interrupt generation for access violation events
- Integrates 9 IOPMPs to provide security control for hardware modules and subsystems

### 15.4.3 Functional Description

#### 15.4.3.1 IOPMP Configuration Overview

Within the chip, the functionality of each IOPMP instance varies depending on its configuration at different nodes. The detailed configuration parameters are listed below.

IOPMP Configuration Parameters

| Parameter Name | Default Value | Configurable Range | Description |
| --- | --- | --- | --- |
| IOPMP_MD_K | 4 | 4 / 8 / 16 / 32 | Number of entries per MD |
| IOPMP_MD_NUM | 16 | 1 ~ 63 | Number of MDs in the IOPMP |
| IOPMP_SID_NUM | 64 | 1 ~ 1024 | Number of SIDs supported by the IOPMP |
| IOPMP_ID_WIDTH | 8 | 1 ~ 16 | AXI ID signal width |
| IOPMP_ADDR_WIDTH | 44 | 32 ~ 64 | AXI address signal width |
| IOPMP_DATA_WIDTH | 64 | 2^N (N = 5 ~ 10) | AXI data signal width |
| IOPMP_WSTRB_WIDTH | 8 | IOPMP_DATA_WIDTH / 8 | AXI WSTRB signal width |
| IOPMP_AWUSER_WIDTH | 3 | Not specified | AXI AWUSER signal width |
| IOPMP_ARUSER_WIDTH | 3 | Not specified | AXI ARUSER signal width |
| IOPMP_WUSER_WIDTH | 3 | Not specified | AXI WUSER signal width |
| IOPMP_BUSER_WIDTH | 3 | Not specified | AXI BUSER signal width |
| IOPMP_RUSER_WIDTH | 3 | Not specified | AXI RUSER signal width |
| IOPMP_LOOPBACK_WIDTH | 8 | Not specified | ACE5-Lite W/R LOOPBACK signal width |
| IOPMP_MMUSID_WIDTH | 16 | Not specified | ACE5-Lite W/R MMUSID signal width |
| IOPMP_MMUSSID_WIDTH | 16 | Not specified | ACE5-Lite W/R MMUSSID signal width |
| IOPMP_DATACHK_WIDTH | 8 | IOPMP_DATA_WIDTH / 8 | ACE5-Lite W/R DATACHK signal width |
| IOPMP_POISON_WIDTH | 1 | IOPMP_DATA_WIDTH / 64 | ACE5-Lite W/R POISON signal width |
| IOPMP_DEFAULT_AWADDR | 44'h0 | 4 KB aligned address | Default AXI write error address |
| IOPMP_DEFAULT_ARADDR | 44'h0 | 4 KB aligned address | Default AXI read error address |
| IOPMP_DEVICEID_WIDTH | 20 | 1 ~ 32 | Stream ID signal width |

#### 15.4.3.2 IOPMP Instance Overview

In K3, a total of 9 IOPMP instances are implemented. The configuration of each IOPMP instance within the chip is summarized in the table below.

| IOPMP Instance | Upstream Devices | MD_K | MD_NUM | SID_NUM | ADDR_W | DATA_W |
| --- | --- | --- | --- | --- | --- | --- |
| IOPMP1 / IOPMP_M2F | RCPU | 4 | 16 | 1 | 32 | 64 |
| IOPMP2 / IOPMP_F2M | Secure DMA / Non-secure DMA / USB3 / Security Engine / SD / USB OTG / UFS / eSPI (AP) / PCIe / CPU | 4 | 16 | 16 | 32 | 64 |
| IOPMP3 / IOPMP_DMA | Secure DMA / Non-secure DMA *(share one SID; treated as a single device by IOPMP)* | 4 | 16 | 1 | 38 | 64 |
| IOPMP4 | — | 16 | 16 | 16 | 32 | 64 |
| IOPMP5 / IOPMP_HSDMA | HSDMA | 4 | 16 | 1 | 40 | 128 |
| IOPMP6 / IOPMP_INT0 | DBG_AW / DBG_AR / GPU / VPU / ETR / REE_W / REE_R | 4 | 16 | 16 | 38 | 256 |
| IOPMP7 / IOPMP_INT1 | Secure DMA / Non-secure DMA / USB3 / Security Engine / SD / USB OTG / UFS / eSPI (AP) / GMAC0 / GMAC1 / AUD / UCIE / GMAC2 | 4 | 16 | 16 | 38 | 256 |
| IOPMP8 / IOPMP_INT2 | PCIe | 4 | 16 | 16 | 38 | 256 |
| IOPMP9 / IOPMP_INT3 | ISP / LCD0 / LCD1 | 4 | 16 | 16 | 38 | 256 |

#### 15.4.3.3 SID Mechanism

For K3, all IOPMP instances use static SIDs (i.e., AxUSER signals) to distinguish access permissions of different master devices to protected memory regions.
Each IOPMP instance is associated with a set of upstream masters, with a fixed SID assigned to each master. The SID configuration is shown in the table below.

| IOPMP Instance | Upstream Master | Static SID |
| --- | --- | --- |
| **IOPMP1 / IOPMP_M2F** | RCPU | 0x0 |
| **IOPMP2 / IOPMP_F2M** | Secure DMA | 0x0 *(security enable required)* |
| | Non-secure DMA | 0xF |
| | USB3 | 0x2 |
| | Security Engine | 0x3 |
| | SD | 0x4 |
| | USB OTG | 0x5 |
| | UFS | 0x6 |
| | eSPI (AP) | 0x9 |
| | PCIe | 0x8 |
| | CPU | 0x1 |
| **IOPMP3 / IOPMP_DMA** | Secure DMA / Non-secure DMA | 0x0 |
| **IOPMP4** | — | — |
| **IOPMP5 / IOPMP_HSDMA** | HSDMA | 0x0 |
| **IOPMP6 / IOPMP_INT0** | DBG_AW | See below |
| | DBG_AR | See below |
| | GPU | See below |
| | VPU | See below |
| | ETR | See below |
| | REE_W | See below |
| | REE_R | See below |
| **IOPMP7 / IOPMP_INT1** | Secure DMA | 0x0 |
| | Non-secure DMA | 0xF |
| | USB3 | 0x2 |
| | Security Engine | 0x3 |
| | SD | 0x4 |
| | USB OTG | 0x5 |
| | UFS | 0x6 |
| | eSPI (AP) | 0x9 |
| | GMAC0 | See below |
| | GMAC1 | See below |
| | AUD | See below |
| | UCIE | See below |
| | GMAC2 | See below |
| **IOPMP8 / IOPMP_INT2** | PCIe | See below |
| **IOPMP9 / IOPMP_INT3** | ISP | See below |
| | LCD0 | See below |
| | LCD1 | See below |

#### 15.4.3.4 SID Configuration via SEC_CIU

For certain devices, the SID must be configured via registers in the SEC_CIU module (base address: 0xF0580000). The relevant register fields are described below.

##### Secure DMA

By default, Secure DMA shares the same SID as Non-secure DMA.

When differentiation between Secure DMA and Non-secure DMA is required by the IOPMP, the security attribute of Secure DMA can be enabled through the DMA_SEC_CTRL_KEY_SEL[15:0] register field:

- Each bit corresponds to one DMA channel (bit n → channel n).
- When DMA_SEC_CTRL_KEY_SEL[n] = 1, the corresponding channel is marked as secure DMA, and its SID is assigned to the dedicated secure DMA SID.

###### DMA SECURE CONTROL REGISTER

DMA_SEC_CTRL_KEY_SEL
Offset: 0x0

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31 | ECO_KEY_SEL | RW | 0x0 | Key select (added by ECO): 1 = OTP_OEM_KEY_HASH; 0 = OTP_RKEK (ECO) |
| 30:23 | RSVD | RO | 0 | Reserved for future use. |
| 22 | DAP_SEC_EN | RW | 0x0 | DAP secure enable. |
| 21 | KEYPAD_SEC_EN | RW | 0x0 | KEYPAD secure enable. |
| 20 | TIMER_SEC_EN | RW | 0x0 | TIMER secure enable. |
| 19 | RTC_SEC_EN | RW | 0x0 | RTC secure enable. |
| 18 | I2C3_SEC_EN | RW | 0x0 | I2C3 secure enable. |
| 17 | SSP2_SEC_EN | RW | 0x0 | SSP2 secure enable. |
| 16 | UART_SEC_EN | RW | 0x0 | UART secure enable. |
| 15:0 | DMA_CHAN_SEC_EN | RW | 0x0 | DMA channel secure control. |

##### DBG_AW and DBG_AR

The SIDs are configured via the **NSAID_CTRL0 register** (offset: 0x10):

- DBG_AW.SID ← bits [27:24]
- DBG_AR.SID ← bits [31:28]

###### NSAID CONTROL REGISTER0

NSAID_CTRL0
Offset: 0x10

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:28 | APCORE_DBG_AR_NSAID | RW | 0x0 | APCORE DBG read NSAID. |
| 27:24 | APCORE_DBG_AW_NSAID | RW | 0x0 | APCORE DBG write NSAID. |
| 23:20 | APCORE_AR_NSAID | RW | 0x0 | APCORE read NSAID. |
| 19:16 | APCORE_AW_NSAID | RW | 0x0 | APCORE write NSAID. |
| 15:11 | Reserved | RO | 0 | Reserved for future use. |
| 10:8 | BOM_REE_KEY_SEL | RW | 0x0 | BOM_REE key select. |
| 7:4 | BOM_REE_AR_NSAID | RW | 0x0 | BOM_REE read NSAID. |
| 3:0 | BOM_REE_AW_NSAID | RW | 0x0 | BOM_REE write NSAID. |

##### GPU

To configure the SID for the GPU:

1. Set **NASID_CTRL1** (offset: 0x14) bit [30] = 1.
2. Specify the SID via **NASID_CTRL1** bits [19:16].

###### NSAID CONTROL REGISTER1

NSAID_CTRL1
Offset: 0x14

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31 | VPU_NSAID_SEL | RW | 0x0 | VPU NSAID select. |
| 30 | GPU_NSAID_SEL | RW | 0x0 | GPU NSAID select. |
| 29 | APPBRC_NSAID_SEL | RW | 0x0 | APPBRC NSAID select. |
| 28 | LCD_NSAID_SEL | RW | 0x0 | LCD NSAID select. |
| 27:24 | USB3_NSAID | RW | 0x0 | USB3 (M3) NSAID. |
| 23:20 | VPU_NSAID | RW | 0x0 | VPU NSAID. |
| 19:16 | GPU_NSAID | RW | 0x0 | GPU NSAID. |
| 15:12 | APFBRC_NSAID | RW | 0x0 | APFBRC NSAID. |
| 11:8 | V2D_NSAID | RW | 0x0 | V2D NSAID. |
| 7:4 | LCD_NSAID | RW | 0x0 | LCD NSAID. |
| 3:0 | EMAC0 NSAID | RW | 0x0 | EMAC0 NSAID. |

##### VPU

To configure the SID for the VPU:

1. Set **NASID_CTRL1** (offset: 0x14) bit [31] = 0.
2. Specify the SID via **NASID_CTRL1** bits [23:20].

##### V2D

To configure the SID for the V2D:

1. Set **MAS_SEC_CTRL** (offset: 0x8) bit [31] = 1.
2. Specify the SID via **NASID_CTRL1** (offset: 0x14) bits [11:8].

###### MASTER SECURE CONTROL REGISTER

MAS_SEC_CTRL
Offset: 0x8

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31 | V2D_AXUSER_SEL | RW | 0x0 | V2D AXUSER select. |
| 30 | PCIE_USB_COMBO_AXUSER_SEL | RW | 0x0 | PCIe/USB combo AXUSER select. |
| 29 | LCDSAT2_AXUSER_SEL | RW | 0x0 | LCDSAT2 AXUSER select. |
| 28:15 | RSVD | RO | 0 | Reserved for future use. |
| 14 | LCDSAT2_SECURE_EN | RW | 0x0 | LCDSAT2 master secure enable. |
| 13 | AUDMCU_SECURE_EN | RW | 0x0 | AUDMCU master secure enable. |
| 12 | LCD_SECURE_EN | RW | 0x0 | LCD master secure enable. |
| 11 | PCIE2DDR_SECURE_EN | RW | 0x0 | PCIE2DDR master secure enable. |
| 10 | UCIE_SECURE_EN | RW | 0x0 | UCIE master secure enable. |
| 9 | V2D_SECURE_EN | RW | 0x0 | V2D master secure enable. |
| 8 | VPU_SECURE_EN | RW | 0x0 | VPU master secure enable. |
| 7 | ESPI_SECURE_EN | RW | 0x0 | eSPI master secure enable. |
| 6 | PCIE_SECURE_EN | RW | 0x0 | PCIe master secure enable. |
| 5 | UFS_SECURE_EN | RW | 0x0 | UFS master secure enable. |
| 4 | GPU_SECURE_EN | RW | 0x0 | GPU master secure enable. |
| 3 | ISP_SECURE_EN | RW | 0x0 | ISP master secure enable. |
| 2 | USB3_SECURE_EN | RW | 0x0 | DDRC trustzoe disable. |
| 1 | USB2_HOST_SECURE_EN | RW | 0x0 | DDRC trustzone lock. |
| 0 | USB2_SECURE_EN | RW | 0x0 | DDR low 2GB remap to high address, 0x0, not remap. |

##### ETR

> TBD

##### REE_W and REE_R

The SIDs are configured via the **NSAID_CTRL0** register (offset: 0x10):

- REE_W.SID ← bits [3:0]
- REE_R.SID ← bits [7:4]

##### GMAC0/1/2

The SIDs are configured via the **DDRPORT_USER_CTRL** register (offset: 0x78):

- GMAC0.SID ← bits [3:0]
- GMAC1.SID ← bits [7:4]
- GMAC2.SID ← bits [19:16]

###### DDR PORT USER CONTROL REGISTER

DDRPORT_USER_CTRL
Offset: 0x78

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:28 | PCIE_USB_COMBO_AXUSER | RW | 0x0 | PCIe/USB combo AXUSER. |
| 27:20 | RSVD | RO | 0 | Reserved for future use. |
| 19:16 | GMAC2_AXUSER | RW | 0x0 | GMAC2_AXUSER. |
| 15:12 | UCIE_AXUSER | RW | 0x0 | UCIE_AXUSER. |
| 11:8 | AUD_AXUSER | RW | 0x0 | AUD_AXUSER. |
| 7:4 | GMAC1_AXUSER | RW | 0x0 | GMAC1_AXUSER. |
| 3:0 | GMAC0_AXUSER | RW | 0x0 | GMAC0_AXUSER. |

##### AUD (Little Core)

The SID is configured via the **DDRPORT_USER_CTRL** register (offset: 0x78) bits [11:8].

##### UCIE

The SID is configured via the **DDRPORT_USER_CTRL** register (offset: 0x78) bits [15:12].

##### ISP

The SID is configured via the **NASID_CTRL1** register (offset: 0x14) bits [3:0].

##### LCD0

To configure the SID for LCD0:

- Set **NASID_CTRL1** (offset: 0x14) bit [28] = 0.
- Specify the SID via **NASID_CTRL1** (offset: 0x14) bits [7:4].

##### LCD1

To configure the SID for LCD1:

- Set **MAS_SEC_CTRL** (offset: 0x8) bit [29] = 1.
- Specify the SID via **DDRPORT_USER_CTRL** (offset: 0x78) bits [27:24].

##### IOPMP8 PCIe

To configure the SID for PCIe on IOPMP8:

- Set **MAS_SEC_CTRL** (offset: 0x8) bit [30] = 1.
- Specify the SID via **DDRPORT_USER_CTRL** (offset: 0x78) bits [31:28].

### 15.4.4 Registers

#### 15.4.4.1 IOPMP Register Address Mapping

Each IOPMP instance occupies a 64 KB configuration register address space. The address allocation for each IOPMP instance in the chip is shown in the table below.

| IOPMP Instance | Upstream Devices | Base Address |
| --- | --- | --- |
| IOPMP1 / IOPMP_M2F | RCPU | 0xF080_0000 |
| IOPMP2 / IOPMP_F2M | Secure DMA / Non-secure DMA / USB3 / Security Engine <br>/ SD / USB OTG / UFS / eSPI (AP) / PCIe / CPU | 0xF085_0000 |
| IOPMP3 / IOPMP_DMA | Secure DMA / Non-secure DMA <br>*(share one SID; treated as a single device by IOPMP)* | 0xF087_0000 |
| IOPMP4 | — | 0xF086_0000 |
| IOPMP5 / IOPMP_HSDMA | HSDMA | 0xF088_0000 |
| IOPMP6 / IOPMP_INT0 | DBG_AW / DBG_AR / GPU / VPU / ETR / REE_W / REE_R | 0xF081_0000 |
| IOPMP7 / IOPMP_INT1 | Secure DMA / Non-secure DMA / USB3 / Security Engine <br>/ SD / USB OTG / UFS / eSPI (AP) / GMAC0 / GMAC1 <br>/ AUD / UCIE / GMAC2 | 0xF082_0000 |
| IOPMP8 / IOPMP_INT2 | PCIe | 0xF083_0000 |
| IOPMP9 / IOPMP_INT3 | ISP / LCD0 / LCD1 | 0xF084_0000 |

#### 15.4.4.2 Register List

##### INFO Registers

| Register Name | Offset | Description |
| --- | --- | --- |
| VERSION | 0x0000 | Specification version |
| IMPLEMENT | 0x0004 | Implementation ID |
| HWCFG0 | 0x0008 | IOPMP hardware configuration 0 |
| HWCFG1 | 0x000C | IOPMP hardware configuration 1 |
| HWCFG2 | 0x0010 | IOPMP hardware configuration 2 |
| ENTRYOFFSET | 0x0014 | Offset of Entry register array |

##### Configuration Protection Registers

| Register Name | Offset | Description |
| --- | --- | --- |
| MDLCK | 0x0040 | MD configuration lock |
| MDLCKH | 0x0044 | MD configuration lock (high bits) |
| ENTRYLCK | 0x004C | Entry configuration lock |

##### Error Capture Registers

| Register Name | Offset | Description |
| --- | --- | --- |
| ERR_CFG | 0x0060 | Error configuration |
| ERR_REQINFO | 0x0064 | Error request information |
| ERR_REQADDR | 0x0068 | Lower bits of error address |
| ERR_REQADDRH | 0x006C | Upper bits of error address |
| ERR_REQID | 0x0070 | Entry index where the error occurred |
| ERR_NUM_W | 0x0100 | Accumulated error count on write channel |
| ERR_NUM_R | 0x0104 | Accumulated error count on read channel |

##### DEVICEID Configuration Register

| Register Name | Offset | Description |
| --- | --- | --- |
| DEVICEIDCFG | 0x0200 | DeviceID type selection |

##### Default Address Registers

| Register Name | Offset | Description |
| --- | --- | --- |
| DFT_ADDR_W | 0x0210 | Bits [33:12] of default write address. <br>Reset value is defined by configuration parameter **IOPMP_DEFAULT_AWADDR**. Not writable after enable is set to 1. |
| DFT_ADDRH_W | 0x0214 | Bits [65:34] of default write address. <br>Valid width depends on the actual address width. Reset value is defined by **IOPMP_DEFAULT_AWADDR**. Not writable after enable is set to 1. |
| DFT_ADDR_R | 0x0218 | Bits [33:12] of default read address. <br>Reset value is defined by configuration parameter **IOPMP_DEFAULT_ARADDR**. Not writable after enable is set to 1. |
| DFT_ADDRH_R | 0x021C | Bits [65:34] of default read address. <br>Valid width depends on the actual address width. Reset value is defined by **IOPMP_DEFAULT_ARADDR**. Not writable after enable is set to 1. |

##### SRCMD Table Registers

| Register Name | Offset | Description |
| --- | --- | --- |
| SRCMD_EN(s) | 0x1000 + (s) × 32 | SID-to-MD mapping configuration |
| SRCMD_ENH(s) | 0x1004 + (s) × 32 | SID-to-MD mapping configuration (high bits) |

##### DeviceID to SID Registers

| Register Name | Offset | Description |
| --- | --- | --- |
| DEVICEID(s) | 0x9000 + (s) × 4 | DeviceID mapped to SIDs. Bit width is defined by configuration parameter **IOPMP_DEVICEID_WIDTH** |

##### Entry Array Registers

| Register Name | Offset | Description |
| --- | --- | --- |
| ENTRY_ADDR(i) | 0xA000 + (i) × 16 | Bits [33:12] of the entry physical address |
| ENTRY_ADDRH(i) | 0xA004 + (i) × 16 | Bits [65:34] of the entry physical address. <br>Valid width depends on actual address width |
| ENTRY_CFG(i) | 0xA008 + (i) × 16 | Entry configuration |

#### 15.4.4.3 Register Descriptions

##### VERSION(0x0000)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:24 | specver | RO | 8'h0 | Specification version. |
| 23:0 | vendor | RO | 24'h0 | JEDEC manufacturer ID. |

##### IMPLEMENT(0x0004)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | impid | RO | 32'h0 | Implementation ID. |

##### HWCFG0(0x0008)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31 | enable | W1SS | 1'h0 | IOPMP enable. Supports write-one-to-set only. |
| 30 | addrh_en | RO | CFG | Indicates support for ENTRY_ADDRH register. 0x0: ENTRY_ADDRH not supported; 0x1: ENTRY_ADDRH supported. |
| 29:24 | md_num | RO | CFG | Number of configured MDs. |
| 23:17 | md_entry_num | RO | CFG | Number of entries per MD minus 1. |
| 16 | mfr_en | RO | 1'h0 | Multiple Fault Recording (MFR) not supported. |
| 15 | pees | RO | 1'h0 | Per-entry bus error suppression not supported. |
| 14 | peis | RO | 1'h0 | Per-entry interrupt suppression not supported. |
| 13 | stall_en | RO | 1'h0 | MDSTALL / SIDSCP not supported. |
| 12 | no_w | RO | 1'h0 | Global write disable not supported. |
| 11 | no_x | RO | 1'h0 | Global execute (instruction fetch) disable not supported. |
| 10 | chk_x | RO | 1'h1 | Instruction fetch checking supported. |
| 9 | rrid_transl_prog | RO | 1'h0 | RRID translation programming not supported. |
| 8 | rrid_transl_en | RO | 1'h0 | RRID translation not supported. |
| 7 | prient_prog | RO | 1'h0 | Priority entry modification not supported. |
| 6 | user_cfg_en | RO | 1'h0 | Custom user attribute configuration not supported. |
| 5 | sps_en | RO | 1'h0 | Secondary permission not supported. |
| 4 | tor_en | RO | 1'h1 | TOR (Top of Range) address matching supported. |
| 3:2 | srcmd_fmt | RO | 2'h0 | Format 0 for Rapid-K model. |
| 1:0 | mdcfg_fmt | RO | 2'h1 | Format 1 for Rapid-K model. |

##### HWCFG1(0x000C)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:16 | entry_num | RO | CFG | Number of configured entries. |
| 15:0 | rrid_num | RO | CFG | Number of configured RRIDs. |

##### HWCFG2(0x0010)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:16 | rrid_transl | RO | 16'h0 | RRID translation not supported (no new RRID is forwarded to the target). |
| 15:0 | prio_entry | RO | 16'h0 | Priority-based address matching not supported. |

##### ENTRYOFFSET(0x0014)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | offset | RO | 32'hA000 | Offset of the Entry register array. |

##### MDLCK(0x0040)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:1 | md | W1SS | 31'h0 | Each bit md[j] locks the corresponding SRCMD_EN(i).md[j] field. <br>The number of valid bits depends on the configured number of MDs. |
| 0 | l | W1SS | 1'h0 | Lock bit for MDLCK and MDLCKH registers. |

##### MDLCKH(0x0044)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | mdh | W1SS | 32'h0 | Each bit mdh[j] locks the corresponding SRCMD_ENH(i).mdh[j] field. <br>The number of valid bits depends on the configured number of MDs. |

##### ENTRYLCK(0x004C)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:17 | rsv | RO | 15'h0 | Reserved. |
| 16:1 | f | RW | 16'h0 | Locks entries from entry(0) to entry(f-1). Only increasing values are allowed (write-once, monotonic increment). |
| 0 | l | W1SS | 1'h0 | Lock bit for the ENTRYLCK register. |

##### ERR_CFG(0x0060)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:19 | rsv2 | RO | 13'h0 | Reserved. |
| 18:8 | msidata | RO | 11'h0 | MSI interrupt not supported. |
| 7:4 | rsv1 | RO | 4'h0 | Reserved. |
| 3 | msi_en | RO | 1'h0 | MSI interrupt not supported. |
| 2 | rs | RO | 1'h0 | Bus error suppression not supported. |
| 1 | ie | RW | 1'h0 | IOPMP interrupt enable. |
| 0 | l | W1SS | 1'h0 | Lock bit for the ERR_CFG register. |

##### ERR_REQINFO(0x0064)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:8 | rsv2 | RO | 24'h0 | Reserved. |
| 7 | svc | RO | 1'h0 | Multiple Fault Recording (MFR) not supported. |
| 6:4 | etype | RO | 3'h0 | Error type: <br>0x0 = No error; <br>0x1 = Read error; <br>0x2 = Write error; <br>0x3 = Execution error; <br>0x4 = Reserved; <br>0x5 = No matching rule; <br>0x6 = Unknown SID; <br>0x7 = Reserved |
| 3 | rsv1 | RO | 1'h0 | Reserved. |
| 2:1 | ttype | RO | 2'h0 | Transaction type: <br>0x0 = Reserved; <br>0x1 = Read; <br>0x2 = Write; <br>0x3 = Execution |
| 0 | v | W1C | 1'h0 | Interrupt status bit. Write 1 to clear. Not affected by interrupt enable. Once set by hardware, error information is not updated until cleared. After clearing, error recording resumes. |

##### ERR_REQADDR(0x0068)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | addr | RO | 32'h0 | Bits [33:2] of the address where the error occurred. |

##### ERR_REQADDRH(0x006C)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | addrh | RO | 32'h0 | Bits [65:34] of the address where the error occurred. <br>The number of valid bits depends on the configured address width. |

##### ERR_REQID(0x0070)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:16 | eid | RO | 16'h0 | Entry ID where the error occurred. |
| 15:0 | rrid | RO | 16'h0 | RRID associated with the error. |

##### ERR_NUM_W(0x0100)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:16 | rsv | RO | 16'h0 | Reserved. |
| 15:0 | num | RO | 16'h0 | Accumulated error count on the write channel. Cleared when ERR_REQINFO.v is written with 1. |

##### ERR_NUM_R(0x0104)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:16 | rsv | RO | 16'h0 | Reserved. |
| 15:0 | num | RO | 16'h0 | Accumulated error count on the read channel. Cleared when ERR_REQINFO.v is written with 1. |

##### DEVICEIDCFG(0x0200)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:2 | rsv | RO | 30'h0 | Reserved. |
| 1 | l | W1SS | 1'h0 | Lock bit for the DEVICEIDCFG register. |
| 0 | id_sel | RW | 1'h0 | DeviceID selection: <br>0x0 = Use AxUSER signal as SID; DeviceID2SID registers are not used; <br>0x1 = Use Stream ID as SID; DeviceID2SID registers are used |

##### DFT_ADDR_W(0x0210)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:10 | addr | RW | CFG | Bits [33:12] of the default write address. The reset value is defined by configuration parameter IOPMP_DEFAULT_AWADDR. Not writable after enable is set to 1. |
| 9:0 | rsv | RO | 10'h0 | Reserved. |

##### DFT_ADDRH_W(0x0214)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | addrh | RW | CFG | Bits [65:34] of the default write address. <br>The number of valid bits depends on the configured address width. The reset value is defined by configuration parameter IOPMP_DEFAULT_AWADDR. Not writable after enable is set to 1. |

##### DFT_ADDR_R(0x0218)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:10 | addr | RW | CFG | Bits [33:12] of the default read address. The reset value is defined by configuration parameter IOPMP_DEFAULT_ARADDR. Not writable after enable is set to 1. |
| 9:0 | rsv | RO | 10'h0 | Reserved. |

##### DFT_ADDRH_R(0x021C)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | addrh | RW | CFG | Bits [65:34] of the default read address. <br>The number of valid bits depends on the configured address width. The reset value is defined by configuration parameter IOPMP_DEFAULT_ARADDR. Not writable after enable is set to 1. |

##### SRCMD_EN(0x1000 + (s)*32)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:1 | md | RW | 31'h0 | md[j] = 1 indicates that MD j is associated with SIDs. <br>The number of valid bits depends on the configured number of MDs. |
| 0 | l | W1SS | 1'h0 | Lock bit for SRCMD_EN(s) and SRCMD_ENH(s). |

##### SRCMD_ENH(s)(0x1004 + (s)*32)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | mdh | RW | 32'h0 | mdh[j] = 1 indicates that MD (j + 31) is associated with SIDs. <br>The number of valid bits depends on the configured number of MDs. |

##### DEVICEID(s)(0x9000 + (s)*4)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| [31:IOPMP_DEVICEID_WIDTH] | rsv | RO | (32-IOPMP_DEVICEID_WIDTH)'h0 | Reserved. |
| [IOPMP_DEVICEID_WIDTH-1:0] | deviceid | RW | (IOPMP_DEVICEID_WIDTH)'h0 | DeviceID mapped to SIDs. The bit width is defined by configuration parameter IOPMP_DEVICEID_WIDTH. |

##### ENTRY_ADDR(i)(0xA000 + (i)*16)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:10 | addr | RW | 22'h0 | Bits [33:12] of the physical address. |
| 9 | addr11 | RW | 1'h0 | Bit [11] of the physical address. Ignored when TOR mode is used. <br>In NAPOT mode, this bit determines the address range definition: <br>0x0 = 4 KB region defined by higher address bits; <br>0x1 = larger region defined by higher address bits. |
| 8:0 | rsv | RO | 9'h0 | Reserved. |

##### ENTRY_ADDRH(i)(0xA004 + (i)*16)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:0 | addrh | RW | 32'h0 | Bits [65:34] of the physical address. <br>The number of valid bits depends on the configured address width. |

##### ENTRY_CFG(i)(0xA008 + (i)*16)

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:11 | rsv | RO | 21'h0 | Reserved. |
| 10 | sexe | RO | 1'h0 | Per-entry bus error suppression for execution not supported. |
| 9 | sewe | RO | 1'h0 | Per-entry bus error suppression for write not supported. |
| 8 | sere | RO | 1'h0 | Per-entry bus error suppression for read not supported. |
| 7 | sixe | RO | 1'h0 | Per-entry interrupt suppression for execution not supported. |
| 6 | siwe | RO | 1'h0 | Per-entry interrupt suppression for write not supported. |
| 5 | sire | RO | 1'h0 | Per-entry interrupt suppression for read not supported. |
| 4:3 | a | RW | 2'h0 | Address matching mode: <br>0x0 = OFF; <br>0x1 = TOR; <br>0x2 = Reserved; <br>0x3 = NAPOT. |
| 2 | x | RW | 1'h0 | Execute (instruction fetch) access enable. |
| 1 | w | RW | 1'h0 | Write access enable. |
| 0 | r | RW | 1'h0 | Read access enable. |

> Note:
>
> - W1SS: Write 1 to set (bit can only transition from 0 to 1)
> - W1C: Write 1 to clear

### 15.4.5 Programming Guide

#### 15.4.5.1 Basic State and Security Constraints

- Reset and Enable Behavior
  - After power-on reset, the IOPMP operates in bypass mode, allowing all bus transactions without performing access permission checks.
  - Once enabled (enable = 1), the IOPMP continuously enforces access control on all bus transactions and cannot be disabled until the next reset.
- Security Domain Requirement
  - The IOPMP configuration registers reside in the secure domain and must only be accessed from a secure environment (e.g., Secure Boot or a Trusted Execution Environment, TEE).
- Clock Dependency
  - Before configuring IOPMP registers, software must ensure that both pclk and aclk are enabled.
- Lock Protection
  - Software should make appropriate use of the configuration protection mechanism to lock MDs and entries with higher security requirements.

#### 15.4.5.2 Configuration Rules and Address Mapping

- Entry Attributes
  - Each entry can be configured in either NAPOT or TOR addressing mode.
  - If the first entry of the first MD is configured as TOR, the starting address defaults to 0x0.
- Intra-SID Overlap Mechanism
  - Multiple entries mapped to the same SID are allowed to have overlapping address ranges.
  - When a bus transaction matches multiple entries (due to overlap):
    - If at least one entry grants the required access permission, the transaction is considered valid and no error is reported.
    - If none of the matched entries grant permission, the transaction is considered invalid and an error (etype = 0x5) is generated.
  - Software may leverage this mechanism to improve entry utilization, but care must be taken to avoid introducing security risks.
- Inter-SID Overlap Mechanism
  - Address overlap is also allowed among entries mapped to different SIDs, enabling different permission attributes for the same address space.
- SID Conflict Handling
  - If a transaction matches multiple SIDs (e.g., multiple DeviceID registers are configured with the same value), the hardware treats this as an error.
- Update Considerations
  - The hardware does not support stalling specific MDs or SIDs (i.e., there is no MDSTALL mechanism).
  - During entry or SID configuration updates, software must ensure that access rules remain complete and consistent, and must prevent peripherals from accessing address regions whose permissions are being modified.

#### 15.4.5.3 Error Detection and Recording

- Detection Methods
  - Software can detect access violations by:
    - Enabling interrupts; or
    - Polling the ERR_REQINFO.v bit.
- Recording Mechanism
  - The hardware records only the first error.
  - After clearing ERR_REQINFO.v, subsequent errors can be recorded.
  - Software can read ERR_NUM_W and ERR_NUM_R to obtain the total number of write and read errors, respectively.
- Concurrent Error Priority
  - If read and write channel errors occur in the same cycle, the hardware prioritizes recording the write error.
- Counting Rules
  - Write channel error → ERR_NUM_W increments by 1
  - Read channel error → ERR_NUM_R increments by 1

#### 15.4.5.4 Error Type Definition (etype)

- SID-related Errors (etype = 0x6)
  - No SID match
  - Multiple SID matches
  > Note: These two conditions share the same error code.
- Entry-related Errors (etype = 0x5)
  - No entry match
  - Multiple entry matches:
    - If permission is granted → no error is reported
    - If permission is not granted → etype = 0x5

#### 15.4.5.5 Error Information Register Validity

- ERR_REQID.sid Field
  - Source:
    - When DEVICEIDCFG.id_sel = 0, this field is assigned the AxUSER signal of the transaction that triggered the error.
    - Otherwise, it is assigned the SID corresponding to the stream ID of the transaction.
  - Validity:
    - This field is valid only when ERR_REQINFO.etype ≠ 0x6.
    - Otherwise, it is set to 0 and should be considered invalid.
- ERR_REQID.eid Field
  - Validity:
    - This field is valid only when ERR_REQINFO.etype = 0x1, 0x2, or 0x3.
    - It represents the entry index used for access permission checking.
    - Otherwise, it is set to 0 and should be considered invalid.

#### 15.4.5.6 Default Address Configuration Guidelines

##### Register Description

The reset values of the default address registers (DFT_ADDR/H_W, DFT_ADDR/H_R) are determined by the configuration parameters IOPMP_DEFAULT_AWADDR and IOPMP_DEFAULT_ARADDR.

- If the default configuration is used, software does not need to program these registers.
- To use a custom default address, software must:
  - Select a valid address within the chip address space.
  - Ensure the address is 4 KB aligned.
  - Program the address into DFT_ADDR/H_W and DFT_ADDR/H_R.

##### Configuration Recommendations

- IOPMP1/2/3
  - Upon a check failure, the response is handled by the Fabric Default Slave.
  - It is recommended to map the default address to a reserved region in the memory map.
- IOPMP2
  - Maximum default space: 16 × 8 Bytes = 128 Bytes (length × size)
  - Recommended address: 0x30000000
- DDR IOPMP 5/6/7/8/9
  - Maximum default space: 256 × 32 Bytes = 8192 Bytes (length × size)
- Other IOPMP instances
  - Software should configure these based on the specific application scenario, following platform guidelines.
