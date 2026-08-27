---
sidebar_position: 7
---

# 6. Address Mapping

K3 includes:
- One SpacemiT K3 RISC-V Main CPU Domain
- One RISC-V Real-Time CPU Domain

The SoC address maps from each CPU perspective are provided in the following sections.

## 6.1 Main CPU Domain Address Mapping

| Memory Mapping | Address | Size | Note | S/NS |
| --- | --- | --- | --- | --- |
| RISCV TCM (64MB) | 0x0000_0000 | 0x0400_0000 |  |  |
| Reserved | 0x0400_0000 | 0x7C00_0000 |  |  |
| PCIe_USB Subsys MGMT (64MB) | 0x8000_0000 | 0x0400_0000 |  |  |
| espi_slv_mem | 0x8400_0000 | 0x0200_0000 |  |  |
| espi_slv_io | 0x8600_0000 | 0x0200_0000 |  |  |
| Reserved | 0x8800_0000 | 0x3000_0000 |  |  |
| QSPI (128MB) | 0xB800_0000 | 0x0800_0000 |  |  |
| Reserved | 0xC000_0000 | 0x0010_0000 |  |  |
| V2D | 0xC010_0000 | 0x0020_0000 |  |  |
| DPU0 | 0xC034_0000 | 0x0005_4000 |  |  |
| Reserved  | 0xC039_4000 | 0x0006_C000 |  |  |
| FBC-Dec0 | 0xC040_0000 | 0x0000_0100 |  |  |
| FBC-Dec1 | 0xC040_0100 | 0x0000_0100 |  |  |
| ASTC-Dec | 0xC040_0200 | 0x0000_0100 |  |  |
| LCD_TOP | 0xC040_0300 | 0x0000_0100 |  |  |
| LCD_MMU | 0xC040_0400 | 0x0000_0100 |  |  |
| LCD_DSI | 0xC040_0500 | 0x0000_0200 |  |  |
| Reserved | 0xC040_0700 | 0x0003_F900 |  |  |
| DPU1 | 0xC044_0000 | 0x0005_4000 |  |  |
| Reserved  | 0xC049_4000 | 0x0006_C000 |  |  |
| VPU | 0xC050_0000 | 0x0020_0000 |  |  |
| Audio Peripherals2 | 0xC070_0000 | 0x0010_0000 |  |  |
| Audio SRAM (512KB) | 0xC080_0000 | 0x0008_0000 |  | Secure |
| Audio Peripherals | 0xC088_0000 | 0x0018_0000 |  |  |
| USB OTG | 0xC0A0_0000 | 0x0010_0000 |  |  |
| UCIE IP | 0xC0B0_0000 | 0x0010_0000 |  |  |
| UCIE BGR | 0xC0C0_0000 | 0x0010_0000 |  |  |
| UCIE Monitor | 0xC0D0_0000 | 0x0010_0000 |  |  |
| UFS | 0xC0E0_0000 | 0x0010_0000 |  |  |
| IOMMU | 0xC0F0_0000 | 0x09D0_0000 |  |  |
| GPU (512KB) | 0xCAC0_0000 | 0x0008_0000 |  |  |
| GMAC0 (8KB) | 0xCAC8_0000 | 0x0000_2000 |  |  |
| GMAC1 (8KB) | 0xCAC8_2000 | 0x0000_2000 |  |  |
| DP0 (16KB) | 0xCAC8_4000 | 0x0000_4000 |  |  |
| DP1 (16KB) | 0xCAC8_8000 | 0x0000_4000 |  |  |
| ESPI (4KB) | 0xCAC8_C000 | 0x0000_1000 |  |  |
| Reserved | 0xCAC8_D000 | 0x0000_1000 |  |  |
| GMAC2 (8KB) | 0xCAC8_E000 | 0x0000_2000 |  |  |
| Mailbox0 | 0xCAC9_0000 | 0x0000_0400 |  |  |
| Mailbox1 | 0xCAC9_0400 | 0x0000_0400 |  |  |
| Mailbox2 | 0xCAC9_0800 | 0x0000_0400 |  |  |
| Mailbox3 | 0xCAC9_0C00 | 0x0000_0400 |  |  |
| Mailbox4 | 0xCAC9_1000 | 0x0000_0400 |  |  |
| Mailbox5 | 0xCAC9_1400 | 0x0000_0400 |  |  |
| Mailbox6 | 0xCAC9_1800 | 0x0000_0400 |  |  |
| Spinlock | 0xCAC9_1C00 | 0x0000_0400 |  |  |
| Reserved | 0xCAC9_2000 | 0x0006_E000 |  |  |
| USB3 (1MB) | 0xCAD0_0000 | 0x0010_0000 |  |  |
| Reserved | 0xCAE0_0000 | 0x0020_0000 |  |  |
| SNPS DDRC0 (16MB) | 0xCB00_0000 | 0x0100_0000 |  |  |
| SNPS DDRC1 (16MB) | 0xCC00_0000 | 0x0100_0000 |  |  |
| Reserved | 0xCD00_0000 | 0x0700_0000 |  |  |
| PDMA Controller Config | 0xD400_0000 | 0x0001_0000 |  |  |
| RTC | 0xD401_0000 | 0x0000_0800 |  |  |
| IIC0 | 0xD401_0800 | 0x0000_0800 |  |  |
| IIC1 | 0xD401_1000 | 0x0000_0800 |  |  |
| reserved | 0xD401_1800 | 0x0000_0800 |  |  |
| IIC2 | 0xD401_2000 | 0x0000_0800 |  |  |
| IIC4 | 0xD401_2800 | 0x0000_0800 |  |  |
| DRO | 0xD401_3000 | 0x0000_0400 |  |  |
| IPCADSP2AP (Audio-to-RISCV) | 0xD401_3400 | 0x0000_0400 |  |  |
| IIC5 | 0xD401_3800 | 0x0000_0800 |  |  |
| Timer0 (WDT0) | 0xD401_4000 | 0x0000_1000 |  |  |
| APB Bus Clock Unit | 0xD401_5000 | 0x0000_1000 |  |  |
| Timer1 (WDT1) | 0xD401_6000 | 0x0000_1000 |  |  |
| UART0 | 0xD401_7000 | 0x0000_0100 |  |  |
| UART2 | 0xD401_7100 | 0x0000_0100 |  |  |
| UART3 | 0xD401_7200 | 0x0000_0100 |  |  |
| UART4 | 0xD401_7300 | 0x0000_0100 |  |  |
| UART5 | 0xD401_7400 | 0x0000_0100 |  |  |
| UART6 | 0xD401_7500 | 0x0000_0100 |  |  |
| UART7 | 0xD401_7600 | 0x0000_0100 |  |  |
| UART8 | 0xD401_7700 | 0x0000_0100 |  |  |
| UART9 | 0xD401_7800 | 0x0000_0100 |  |  |
| Reserved | 0xD401_7900 | 0x0000_0600 |  |  |
| IR | 0xD401_7E00 | 0x0000_0100 |  |  |
| IR1 | 0xD401_7F00 | 0x0000_0100 |  |  |
| Tsensor | 0xD401_8000 | 0x0000_0800 |  |  |
| IIC6 | 0xD401_8800 | 0x0000_0800 |  |  |
| GPIO | 0xD401_9000 | 0x0000_0800 |  |  |
| GPIO Edge | 0xD401_9800 | 0x0000_0800 |  |  |
| PWM0 | 0xD401_A000 | 0x0000_0400 |  |  |
| PWM1 | 0xD401_A400 | 0x0000_0400 |  |  |
| PWM2 | 0xD401_A800 | 0x0000_0400 |  |  |
| PWM3 | 0xD401_AC00 | 0x0000_0400 |  |  |
| PWM4 | 0xD401_B000 | 0x0000_0400 |  |  |
| PWM5 | 0xD401_B400 | 0x0000_0400 |  |  |
| PWM6 | 0xD401_B800 | 0x0000_0400 |  |  |
| PWM7 | 0xD401_BC00 | 0x0000_0400 |  |  |
| SSP3 | 0xD401_C000 | 0x0000_1800 |  |  |
| IIC8 (PWR_IIC) | 0xD401_D800 | 0x0000_0800 |  |  |
| Pad Configuration | 0xD401_E000 | 0x0000_1000 |  |  |
| UART10 | 0xD401_F000 | 0x0000_1000 |  |  |
| PWM8 | 0xD402_0000 | 0x0000_0400 |  |  |
| PWM9 | 0xD402_0400 | 0x0000_0400 |  |  |
| PWM10 | 0xD402_0800 | 0x0000_0400 |  |  |
| PWM11 | 0xD402_0C00 | 0x0000_0400 |  |  |
| PWM12 | 0xD402_1000 | 0x0000_0400 |  |  |
| PWM13 | 0xD402_1400 | 0x0000_0400 |  |  |
| PWM14 | 0xD402_1800 | 0x0000_0400 |  |  |
| PWM15 | 0xD402_1C00 | 0x0000_0400 |  |  |
| PWM16 | 0xD402_2000 | 0x0000_0400 |  |  |
| PWM17 | 0xD402_2400 | 0x0000_0400 |  |  |
| PWM18 | 0xD402_2800 | 0x0000_0400 |  |  |
| PWM19 | 0xD402_2C00 | 0x0000_0400 |  |  |
| Reserved | 0xD402_3000 | 0x0000_3000 |  |  |
| SSPA0 (l2S0) | 0xD402_6000 | 0x0000_0800 |  |  |
| SSPA1 (l2S1) | 0xD402_6800 | 0x0000_0800 |  |  |
| SSPA2 (l2S2) | 0xD402_7000 | 0x0000_0800 |  |  |
| SSPA3 (l2S3) | 0xD402_7800 | 0x0000_0800 |  |  |
| CAN0 | 0xD402_8000 | 0x0000_4000 |  |  |
| CAN1 | 0xD402_C000 | 0x0000_4000 |  |  |
| Reserved | 0xD403_0000 | 0x0000_1800 |  |  |
| Timer2 (WDT2) | 0xD403_1800 | 0x0000_0400 |  |  |
| Timer3 (WDT3) | 0xD403_1C00 | 0x0000_0400 |  |  |
| Timer4 | 0xD403_2000 | 0x0000_0400 |  |  |
| Timer5 | 0xD403_2400 | 0x0000_0400 |  |  |
| Timer6 | 0xD403_2800 | 0x0000_0400 |  |  |
| Timer7 | 0xD403_2C00 | 0x0000_0400 |  |  |
| reserved | 0xD403_3000 | 0x0000_1000 |  |  |
| CAN2 | 0xD403_4000 | 0x0000_4000 |  |  |
| CAN3 | 0xD403_8000 | 0x0000_4000 |  |  |
| CAN4 | 0xD403_C000 | 0x0000_4000 |  |  |
| SSP0 | 0xD404_0000 | 0x0000_0800 |  |  |
| SSP1 | 0xD404_0800 | 0x0000_0800 |  |  |
| SSPA4 (l2S4) | 0xD404_1000 | 0x0000_0800 |  |  |
| SSPA5 (l2S5) | 0xD404_1800 | 0x0000_0800 |  |  |
| Reserved | 0xD404_2000 | 0x0000_E000 |  |  |
| Main PMU (NDR) | 0xD405_0000 | 0x0001_0000 |  |  |
| Reserved | 0xD406_0000 | 0x0002_0000 |  |  |
| PMU Timer&WDT (NDR) | 0xD408_0000 | 0x0001_0000 |  |  |
| Extra Logic (NDR) | 0xD409_0000 | 0x0001_0000 |  |  |
| Reserved | 0xD40A_0000 | 0x0001_0000 |  |  |
| Resource IPC (NDR) | 0xD40B_0000 | 0x0001_0000 |  |  |
| Reserved | 0xD40C_0000 | 0x0004_0000 |  |  |
| Reserved | 0xD410_0000 | 0x0010_6000 |  |  |
| IPE3 | 0xD420_6000 | 0x0000_4000 |  |  |
| IPE1 | 0xD420_A000 | 0x0000_0800 |  |  |
| IPE2 | 0xD420_A800 | 0x0000_1800 |  |  |
| QSPI_reg | 0xD420_C000 | 0x0000_3000 |  |  |
| CAM_CCIC | 0xD420_F000 | 0x0000_B800 |  |  |
| LCD_DSI | 0xD421_A800 | 0x0006_5800 |  |  |
| SDH | 0xD428_0000 | 0x0000_2000 |  |  |
| ICU | 0xD428_2000 | 0x0000_0800 |  |  |
| AP PMU | 0xD428_2800 | 0x0000_0100 |  | Secure |
| Reserved | 0xD428_2900 | 0x0000_0300 |  |  |
| CPU Config Unit | 0xD428_2C00 | 0x0000_0400 | The CPU warm boot entry point is located in this region. | Secure |
| Reserved | 0xD428_3000 | 0x041B_D000 |  |  |
| CIU Dragon | 0xD844_0000 | 0x000C_0000 |  | Secure |
| CCI550 | 0xD850_0000 | 0x0010_0000 |  | Secure |
| HSDMA | 0xD870_0000 | 0x0010_0000 |  |  |
| DMA350_0 | 0xD880_0000 | 0x0000_2000 |  |  |
| DMA350_1 | 0xD880_2000 | 0x0000_2000 |  |  |
| AIDMA_0 | 0xD880_4000 | 0x0000_1000 |  |  |
| AIDMA_1 | 0xD880_5000 | 0x0000_1000 |  |  |
| AIDMA_2 | 0xD880_6000 | 0x0000_1000 |  |  |
| AIDMA_3 | 0xD880_7000 | 0x0000_1000 |  |  |
| AIDMA_4 | 0xD880_8000 | 0x0000_1000 |  |  |
| AIDMA_5 | 0xD880_9000 | 0x0000_1000 |  |  |
| AIDMA_6 | 0xD880_A000 | 0x0000_1000 |  |  |
| AIDMA_7 | 0xD880_B000 | 0x0000_1000 |  |  |
| Reserved | 0xD880_C000 | 0x077F_4000 |  |  |
| RISCV_APB (Non-Secure) | 0xE000_0000 | 0x1000_0000 | AIA Non-Secure |  |
| Reserved | 0xF000_0000 | 0x0030_0000 |  |  |
| Secure DPU0 | 0xF030_0000 | 0x0010_0000 |  | Secure |
| Secure DPU1 | 0xF040_0000 | 0x0010_0000 |  | Secure |
| Secure VPU | 0xF050_0000 | 0x0008_0000 |  | Secure |
| Secure Configuration unit | 0xF058_0000 | 0x0008_0000 |  | Secure |
| Secure DMA Controller Config | 0xF060_0000 | 0x0001_0000 |  | Secure |
| SEC APB Bus Clock Unit | 0xF061_0000 | 0x0000_2000 |  | Secure |
| SEC UART1 | 0xF061_2000 | 0x0000_1000 |  | Secure |
| SEC SSP2 | 0xF061_3000 | 0x0000_1000 |  | Secure |
| SEC IIC3 | 0xF061_4000 | 0x0000_1000 |  | Secure |
| SEC RTC | 0xF061_5000 | 0x0000_1000 |  | Secure |
| SEC_Timer 8 | 0xF061_6000 | 0x0000_1000 |  | Secure |
| SEC_Keypad Controller | 0xF061_7000 | 0x0000_1000 |  | Secure |
| SEC_JTAG Software | 0xF061_8000 | 0x0000_1000 |  | Secure |
| SEC_GPIO | 0xF061_9000 | 0x000E_7000 |  | Secure |
| Secure BCM config | 0xF070_0000 | 0x0010_0000 | Secure-domain Crypto Engine (eFuse, TE200) | Secure |
| IOPMP config | 0xF080_0000 | 0x0080_0000 |  | Secure |
| RISCV_APB (Secure) | 0xF100_0000 | 0x0700_0000 | AIA Secure | Secure |
| Reserved | 0xF800_0000 | 0x07E0_0000 |  |  |
| ROM Memory | 0xFFE0_0000 | 0x0020_0000 |  | Secure |
| DDR DRAM (64GB) | 0x1_0000_0000 | 0x10_0000_0000 |  |  |
| PCIE0 x8（DEV 2GB） | 0x11_0000_0000 | 0x00_8000_0000 |  |  |
| PCIE1 x2（DEV 2GB） | 0x11_8000_0000 | 0x00_8000_0000 |  |  |
| PCIE2 x2（DEV 2GB） | 0x12_0000_0000 | 0x00_8000_0000 |  |  |
| PCIE3 x1（DEV 1GB） | 0x12_8000_0000 | 0x00_4000_0000 |  |  |
| PCIE4 x1（DEV 1GB） | 0x12_C000_0000 | 0x00_4000_0000 |  |  |
| PCIE4 x1（MEM 4GB） | 0x13_0000_0000 | 0x01_0000_0000 |  |  |
| PCIE3 x1（MEM 4GB） | 0x14_0000_0000 | 0x01_0000_0000 |  |  |
| PCIE2 x2（MEM 4GB） | 0x15_0000_0000 | 0x01_0000_0000 |  |  |
| PCIE1 x2（MEM 8GB） | 0x16_0000_0000 | 0x02_0000_0000 |  |  |
| PCIE0 x8（MEM 32GB） | 0x18_0000_0000 | 0x08_0000_0000 |  |  |
| UCIE (IO 4GB) | 0x20_0000_0000 | 0x01_0000_0000 |  |  |
| UCIE (DDR 64GB) | 0x21_0000_0000 | 0x10_0000_0000 |  |  |
| UCIE (PCIe 60GB) | 0x31_0000_0000 | 0x0F_0000_0000 |  |  |

## 6.2 RCPU Domain Address Mapping
| Module | Address | Size | Note |
| --- | --- | --- | --- |
| SRAM(512KB) | 0x0000_0000 | 0x0008_0000 | 512 KB, shared with the SRAM at 0xC080_0000 |
| Reserved | 0x0008_0000 | 0x0FF8_0000 |  |
| espi_slv_mem | 0x1000_0000 | 0x0200_0000 | The ACPU accesses this I/O space at address 0x9000_0000 |
| espi_slv_io | 0x1200_0000 | 0x0200_0000 |  |
| Reserved | 0x1400_0000 | 0x0C00_0000 |  |
| r_gmac_slv | 0x2000_0000 | 0x1000_0000 |  |
| Reserved | 0x3000_0000 | 0x5000_0000 |  |
| X100 Domain Device | 0x8000_0000 | 0x4060_0000 | The rCPU accesses devices in the X100 domain. |
| Reserved | 0xC060_0000 | 0x0010_0000 |  |
| r_espi_apb | 0xC070_0000 | 0x0001_0000 |  |
| r_can0 | 0xC071_0000 | 0x0001_0000 |  |
| r_can1 | 0xC072_0000 | 0x0001_0000 |  |
| r_can2 | 0xC073_0000 | 0x0001_0000 |  |
| r_can3 | 0xC074_0000 | 0x0001_0000 |  |
| r_can4 | 0xC075_0000 | 0x0001_0000 |  |
| r_mailbox | 0xC076_0000 | 0x0001_0000 |  |
| Reserved | 0xC077_0000 | 0x0009_0000 |  |
| SRAM RMAP(512KB) | 0xC080_0000 | 0x0008_0000 | 512KB |
| sys_ctrl regs | 0xC088_0000 | 0x0000_1000 |  |
| R_UART0 | 0xC088_1000 | 0x0000_0100 |  |
| R_UART1 | 0xC088_1100 | 0x0000_0100 |  |
| R_UART2 | 0xC088_1200 | 0x0000_0100 |  |
| R_UART3 | 0xC088_1300 | 0x0000_0100 |  |
| R_UART4 | 0xC088_1400 | 0x0000_0100 |  |
| R_UART5 | 0xC088_1500 | 0x0000_0100 |  |
| Reserved | 0xC088_1600 | 0x0000_0900 |  |
| RURT_CLK_RES | 0xC088_1F00 | 0x0000_0100 |  |
| Audio_ctrl_reg | 0xC088_2000 | 0x0000_1000 |  |
| I2S0_ADMA | 0xC088_3000 | 0x0000_0100 |  |
| I2S0_SSPA | 0xC088_3100 | 0x0000_0300 |  |
| I2S1 ADMA | 0xC088_3400 | 0x0000_0100 |  |
| I2S1 SSPA | 0xC088_3500 | 0x0000_0300 |  |
| I2S2_ADMA | 0xC088_3800 | 0x0000_0100 |  |
| I2S2_SSPA | 0xC088_3900 | 0x0000_0300 |  |
| I2S3 ADMA | 0xC088_3C00 | 0x0000_0100 |  |
| I2S3 SSPA | 0xC088_3D00 | 0x0000_0300 |  |
| AHBDMA | 0xC088_4000 | 0x0000_1000 |  |
| R_SSP0 | 0xC088_5000 | 0x0000_0100 |  |
| R_SSP1 | 0xC088_5100 | 0x0000_0100 |  |
| R_SSP2 | 0xC088_5200 | 0x0000_0100 |  |
| Reserved | 0xC088_5300 | 0x0000_0C00 |  |
| RSSP_CLK_RES | 0xC088_5F00 | 0x0000_0100 |  |
| R_I2C0 | 0xC088_6000 | 0x0000_0100 |  |
| R_I2C1 | 0xC088_6100 | 0x0000_0100 |  |
| R_PWR_I2C | 0xC088_6200 | 0x0000_0D00 |  |
| R_I2C_CLK_RES | 0xC088_6F00 | 0x0000_0100 |  |
| R_IRC0 | 0xC088_7000 | 0x0000_1000 |  |
| Reserved | 0xC088_8000 | 0x0000_1000 |  |
| AON_TIMER1 | 0xC088_9000 | 0x0000_0400 |  |
| R_GPIO | 0xC088_9400 | 0x0000_0400 |  |
| R_GPIO_EDGE | 0xC088_9800 | 0x0000_0800 |  |
| AON_IPC2AP | 0xC088_A000 | 0x0000_1000 |  |
| Reserved | 0xC088_B000 | 0x0000_1000 |  |
| AON_PMU_REG | 0xC088_C000 | 0x0000_0800 |  |
| AON_TIMER2 | 0xC088_C800 | 0x0000_0100 |  |
| AON_TIMER3 | 0xC088_C900 | 0x0000_0100 |  |
| AON_TIMER4 | 0xC088_CA00 | 0x0000_0100 |  |
| Reserved | 0xC088_CB00 | 0x0000_0500 |  |
| PWM_CLK_RES | 0xC088_D000 | 0x0000_0100 |  |
| PWM0 | 0xC088_D100 | 0x0000_0100 |  |
| PWM1 | 0xC088_D200 | 0x0000_0100 |  |
| PWM2 | 0xC088_D300 | 0x0000_0100 |  |
| PWM3 | 0xC088_D400 | 0x0000_0100 |  |
| PWM4 | 0xC088_D500 | 0x0000_0100 |  |
| PWM5 | 0xC088_D600 | 0x0000_0100 |  |
| PWM6 | 0xC088_D700 | 0x0000_0100 |  |
| PWM7 | 0xC088_D800 | 0x0000_0100 |  |
| PWM8 | 0xC088_D900 | 0x0000_0100 |  |
| PWM9 | 0xC088_DA00 | 0x0000_0100 |  |
| Reserved | 0xC088_DB00 | 0x0000_0500 |  |
| R_IRC1 | 0xC088_E000 | 0x0000_2000 |  |
| Reserved | 0xC089_0000 | 0x0004_0000 |  |
| Audio Buf(65KB) | 0xC08D_0000 | 0x0001_0400 |  |
| Reserved | 0xC08E_0400 | 0x1371_FC00 |  |
| To AP APB | 0xD400_0000 | 0x0040_0000 |  |
| X100 Domain Device | 0xD440_0000 | 0x2BC0_0000 |  |
| DDR_DRAM(64GB) | 0x01_0000_0000 | 0x10_0000_0000 |  |