---
sidebar_position: 5
---

# 4. Electrical Characteristics

## 4.1 Pin AC/DC Operating Conditions

The following table describes the recommended operating conditions.

| Module        | Symbol/Pin                   | Min               | Typ             | Max               |
|---------------|------------------------------|-------------------|-----------------|-------------------|
| **CPU**           | VDD08_X100                   | 0.72V             | 0.8V            | 1.05V             |
|               | VDD08_M1A100                 | 0.72V             | 0.8V            | 0.88V             |
| **PLL**           | AVDD08_PLL1                  | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD08_PLL234                | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD08_PLL567                | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD18_PLL1                  | 1.71V             | 1.8V            | 1.96V             |
|               | AVDD18_PLL234                | 1.71V             | 1.8V            | 1.96V             |
|               | AVDD18_PLL567                | 1.71V             | 1.8V            | 1.96V             |
| **PLL-DDR**       | AVDD08_PLL_DDR0              | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD08_PLL_DDR1              | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD1V8_PLL_DDR0             | 1.71V             | 1.8V            | 1.96V             |
|               | AVDD1V8_PLL_DDR1             | 1.71V             | 1.8V            | 1.96V             |
| **CSI**           | AVDD08_CSI0                  | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD08_CSI1                  | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD08_CSI2                  | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD18_CSI0                  | 1.71V             | 1.8V            | 1.96V             |
|               | AVDD18_CSI1                  | 1.71V             | 1.8V            | 1.96V             |
|               | AVDD18_CSI2                  | 1.71V             | 1.8V            | 1.96V             |
| **DDR**           | VAA1V8_VDD2H_DDR             | 1.674V            | 1.8V            | 1.98V             |
|               | VDD2H_DDR                    | 1.01V/1.045V (LP5/LP4x) | 1.05V/1.1V (LP5/LP4x) | 1.12V/1.155V (LP5/LP4x) |
|               | VDDQ_DDR                     | 0.47V/0.57V (LP5/LP4x)  | 0.5V/0.6V (LP5/LP4x)  | 0.57V/0.63V (LP5/LP4x)  |
|               | VDD0V8_DDR                   | 0.744V            | 0.8V            | 0.88V             |
| **DSI**           | AVDD08_DSI                   | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD12_DSI                   | 1.14V             | 1.2V            | 1.32V             |
|               | AVDD18_DSI                   | 1.71V             | 1.8V            | 1.96V             |
| **EDP**           | AVDD18_EDP0                  | 1.674V            | 1.8V            | 1.98V             |
|               | DVDD08_EDP0                  | 0.744V            | 0.8V            | 0.88V             |
| **EDP1**          | AVDD18_EDP1                  | 1.674V            | 1.8V            | 1.98V             |
|               | DVDD08_EDP1                  | 0.744V            | 0.8V            | 0.88V             |
| **EMMC**          | AVDD08_EMMC                  | 0.744V            | 0.8V            | 0.88V             |
|               | VCC18_EMMC                   | 1.674V            | 1.8V            | 1.98V             |
| **FUSE**          | FUSE_AVDD18                  | 1.71V             | 1.8V            | 1.96V             |
| **GPIO**          | VCC18_GPIO1                  | 1.674V            | 1.8V            | 1.98V             |
|               | VCC18_GPIO2                  | 1.674V            | 1.8V            | 1.98V             |
|               | VCC18_GPIO3                  | 1.674V            | 1.8V            | 1.98V             |
|               | VCC18_GPIO4                  | 1.674V            | 1.8V            | 1.98V             |
|               | VCC18_GPIO5                  | 1.674V            | 1.8V            | 1.98V             |
|               | VCC18_PMIC                   | 1.674V            | 1.8V            | 1.98V             |
|               | VCC1833_GPIO1                | 1.674V/2.97V      | 1.8V/3.3V       | 1.98V/3.63V       |
|               | VCC1833_GPIO2                | 1.674V/2.97V      | 1.8V/3.3V       | 1.98V/3.63V       |
|               | VCC1833_GPIO4                | 1.674V/2.97V      | 1.8V/3.3V       | 1.98V/3.63V       |
|               | VCC1833_GPIO5                | 1.674V/2.97V      | 1.8V/3.3V       | 1.98V/3.63V       |
|               | VCC1833_QSPI                 | 1.674V/2.97V      | 1.8V/3.3V       | 1.98V/3.63V       |
|               | VCC1833_MMC1                 | 1.674V/2.97V      | 1.8V/3.3V       | 1.98V/3.63V       |
| **OSC**           | AVDD08_OSC                   | 0.76V             | 0.8V            | 0.88V             |
|               | AVDD18_OSC                   | 1.71V             | 1.8V            | 1.96V             |
| **PICE PHY0**     | AVDD08_PCIeA                 | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_PCIeA                 | 1.674V            | 1.8V            | 1.98V             |
| **PICE PHY**1     | AVDD08_PCIeB                 | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_PCIeB                 | 1.674V            | 1.8V            | 1.98V             |
| **PICE PHY2**     | AVDD08_PCIeC/USB3-B          | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_PCIeC/USB3-B          | 1.674V            | 1.8V            | 1.98V             |
| **PICE PHY3**     | AVDD08_PCIeD/USB3-C          | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_PCIeD/USB3-C          | 1.674V            | 1.8V            | 1.98V             |
| **PICE PHY4**     | AVDD08_PCIeE/USB3-D          | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_PCIeE/USB3-D          | 1.674V            | 1.8V            | 1.98V             |
| **PICE PHY5**     | AVDD08_PCIe5                 | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_PCIe5                 | 1.674V            | 1.8V            | 1.98V             |
| **UCIE**          | UCIE_VCCAON_0V8              | 0.76V             | 0.8V            | 0.84V             |
|               | UCIE_VCCIO_0V8               | 0.76V             | 0.8V            | 0.84V             |
|               | UCIE_VCCPLL_1P2V             | 1.116V            | 1.2V            | 1.236V            |
|               | UCIE_VDD_0V8                 | 0.76V             | 0.8V            | 0.84V             |
|               | UCIE_VDDBH_0V9               | 0.855V            | 0.9V            | 0.945V            |
|               | UCIE_VDDVPH0_0V9             | 0.855V            | 0.9V            | 0.945V            |
| **UFS**           | UFS_VCC_1V8                  | 1.71V             | 1.8V            | 1.96V             |
|               | UFS_VCCQ_1V2                 | 1.14V             | 1.2V            | 1.32V             |
|               | UFS_VDDU_0V8                 | 0.76              | 0.8V            | 0.88V             |
| **USB2**          | AVDD08_B_USB20               | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD08_C_USB20               | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD08_D_USB20               | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD08_USB20_Host            | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_B_USB20               | 1.674V            | 1.8V            | 1.98V             |
|               | AVDD18_C_USB20               | 1.674V            | 1.8V            | 1.98V             |
|               | AVDD18_D_USB20               | 1.674V            | 1.8V            | 1.98V             |
|               | AVDD18_USB20_Host            | 1.674V            | 1.8V            | 1.98V             |
|               | AVDD33_B_USB20               | 3.069V            | 3.3V            | 3.63V             |
|               | AVDD33_C_USB20               | 3.069V            | 3.3V            | 3.63V             |
|               | AVDD33_D_USB20               | 3.069V            | 3.3V            | 3.63V             |
|               | AVDD33_DRD_USB               | 3.069V            | 3.3V            | 3.63V             |
|               | AVDD33_USB20_Host            | 3.069V            | 3.3V            | 3.63V             |
| **USB3-DRD**      | AVDD08_DRD_USB               | 0.744V            | 0.8V            | 0.88V             |
|               | AVDD18_DRD_USB               | 1.674V            | 1.8V            | 1.98V             |

## 4.2 Absolute Maximum DC Ratings

### 4.2.1 For Pins

| Module        | Symbol/Pin                   | Min    | Max               |
|---------------|------------------------------|--------|-------------------|
| **CPU**           | VDD08_X100                   | -0.3V  | 1.05V             |
|               | VDD08_M1A100                 | -0.3V  | 0.88V             |
| **Digital Power** | VCC_M1                       | -0.3V  | 0.88V             |
| **PLL**           | AVDD08_PLL1                  | -0.3V  | 0.88V             |
|               | AVDD08_PLL234                | -0.3V  | 0.88V             |
|               | AVDD08_PLL567                | -0.3V  | 0.88V             |
|               | AVDD18_PLL1                  | -0.3V  | 1.96V             |
|               | AVDD18_PLL234                | -0.3V  | 1.96V             |
|               | AVDD18_PLL567                | -0.3V  | 1.96V             |
| **PLL-DDR**       | AVDD08_PLL_DDR0              | -0.3V  | 0.88V             |
|               | AVDD08_PLL_DDR1              | -0.3V  | 0.88V             |
|               | AVDD1V8_PLL_DDR0             | -0.3V  | 1.96V             |
|               | AVDD1V8_PLL_DDR1             | -0.3V  | 1.96V             |
| **CSI**           | AVDD08_CSI0                  | -0.3V  | 0.88V             |
|               | AVDD08_CSI1                  | -0.3V  | 0.88V             |
|               | AVDD08_CSI2                  | -0.3V  | 0.88V             |
|               | AVDD18_CSI0                  | -0.3V  | 1.96V             |
|               | AVDD18_CSI1                  | -0.3V  | 1.96V             |
|               | AVDD18_CSI2                  | -0.3V  | 1.96V             |
| **DDR**           | VAA1V8_VDD2H_DDR             | -0.3V  | 1.98V             |
|               | VDD2H_DDR                    | -0.3V  | 1.12V             |
|               | VDDQ_DDR                     | -0.3V  | 0.57V             |
|               | VDD0V8_DDR                   | -0.3V  | 0.88V             |
| **DSI**           | AVDD08_DSI                   | -0.3V  | 0.88V             |
|               | AVDD12_DSI                   | -0.3V  | 1.32V             |
|               | AVDD18_DSI                   | -0.3V  | 1.96V             |
| **EDP**           | AVDD18_EDP0                  | -0.3V  | 1.98V             |
|               | DVDD08_EDP0                  | -0.3V  | 0.88V             |
| **EDP1**          | AVDD18_EDP1                  | -0.3V  | 1.98V             |
|               | DVDD08_EDP1                  | -0.3V  | 0.88V             |
| **EMMC**          | AVDD08_EMMC                  | -0.3V  | 0.88V             |
|               | VCC18_EMMC                   | -0.3V  | 1.98V             |
| **FUSE**          | FUSE_AVDD18                  | -0.3V  | 1.96V             |
| **GPIO**          | VCC18_GPIO1                  | -0.3V  | 1.98V             |
|               | VCC18_GPIO2                  | -0.3V  | 1.98V             |
|               | VCC18_GPIO3                  | -0.3V  | 1.98V             |
|               | VCC18_GPIO4                  | -0.3V  | 1.98V             |
|               | VCC18_GPIO5                  | -0.3V  | 1.98V             |
|               | VCC18_PMIC                   | -0.3V  | 1.98V             |
|               | VCC1833_GPIO1                | -0.3V  | 1.98V/3.63V       |
|               | VCC1833_GPIO2                | -0.3V  | 1.98V/3.63V       |
|               | VCC1833_GPIO4                | -0.3V  | 1.98V/3.63V       |
|               | VCC1833_GPIO5                | -0.3V  | 1.98V/3.63V       |
|               | VCC1833_QSPI                 | -0.3V  | 1.98V/3.63V       |
|               | VCC1833_MMC1                 | -0.3V  | 1.98V/3.63V       |
| **OSC**           | AVDD08_OSC                   | -0.3V  | 0.88V             |
|               | AVDD18_OSC                   | -0.3V  | 1.96V             |
| **PICE PHY0**     | AVDD08_PCIeA                 | -0.3V  | 0.88V             |
|               | AVDD18_PCIeA                 | -0.3V  | 1.98V             |
| **PICE PHY1**     | AVDD08_PCIeB                 | -0.3V  | 0.88V             |
|               | AVDD18_PCIeB                 | -0.3V  | 1.98V             |
| **PICE PHY2**     | AVDD08_PCIeC/USB3-B          | -0.3V  | 0.88V             |
|               | AVDD18_PCIeC/USB3-B          | -0.3V  | 1.98V             |
| **PICE PHY3**     | AVDD08_PCIeD/USB3-C          | -0.3V  | 0.88V             |
|               | AVDD18_PCIeD/USB3-C          | -0.3V  | 1.98V             |
| **PICE PHY4**     | AVDD08_PCIeE/USB3-D          | -0.3V  | 0.88V             |
|               | AVDD18_PCIeE/USB3-D          | -0.3V  | 1.98V             |
| **PICE PHY5**     | AVDD08_PCIe5                 | -0.3V  | 0.88V             |
|               | AVDD18_PCIe5                 | -0.3V  | 1.98V             |
| **UCIE**          | UCIE_VCCAON_0V8              | -0.3V  | 0.84V             |
|               | UCIE_VCCIO_0V8               | -0.3V  | 0.84V             |
|               | UCIE_VCCPLL_1P2V             | -0.3V  | 1.236V            |
|               | UCIE_VDD_0V8                 | -0.3V  | 0.84V             |
|               | UCIE_VDDBH_0V9               | -0.3V  | 0.945V            |
|               | UCIE_VDDVPH0_0V9             | -0.3V  | 0.945V            |
| **UFS**           | UFS_VCC_1V8                  | -0.3V  | 1.96V             |
|               | UFS_VCCQ_1V2                 | -0.3V  | 1.32V             |
|               | UFS_VDDU_0V8                 | -0.3V  | 0.88V             |
| **USB2**          | AVDD08_B_USB20               | -0.3V  | 0.88V             |
|               | AVDD08_C_USB20               | -0.3V  | 0.88V             |
|               | AVDD08_D_USB20               | -0.3V  | 0.88V             |
|               | AVDD08_USB20_Host            | -0.3V  | 0.88V             |
|               | AVDD18_B_USB20               | -0.3V  | 1.98V             |
|               | AVDD18_C_USB20               | -0.3V  | 1.98V             |
|               | AVDD18_D_USB20               | -0.3V  | 1.98V             |
|               | AVDD18_USB20_Host            | -0.3V  | 1.98V             |
|               | AVDD33_B_USB20               | -0.3V  | 3.63V             |
|               | AVDD33_C_USB20               | -0.3V  | 3.63V             |
|               | AVDD33_D_USB20               | -0.3V  | 3.63V             |
|               | AVDD33_DRD_USB               | -0.3V  | 3.63V             |
|               | AVDD33_USB20_Host            | -0.3V  | 3.63V             |
| **USB3-DRD**      | AVDD08_DRD_USB               | -0.3V  | 0.88V             |
|               | AVDD18_DRD_USB               | -0.3V  | 1.98V             |

### 4.2.2 For Packages

| Item                                    | Symbol | Min     | Max     |
|-----------------------------------------|--------|---------|---------|
| Operating Temperature (Industrial Standard) | Ta     | -40°C   | 85°C    |
| Junction Temperature                    | Tj     | N/A     | 125°C   |
| Storage Temperature                     | Tstg   | -40°C   | 125°C   |

## 4.3 Thermal Characteristics

Thermal Resistance (Junction-to-Case): 0.23°C/W (with integrated heat spreader)

## 4.4 Pin Maximum Currents

TBD

## 4.5 Power On/Off Sequence

TBD

