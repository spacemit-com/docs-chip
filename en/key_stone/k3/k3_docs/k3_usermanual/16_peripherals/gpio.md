---
sidebar_position: 8
---

# 16.8 GPIO

## 16.8.1 Overview

The K3 provides General-Purpose Input/Output (GPIO) ports for generating and capturing application-specific input and output. These ports are accessed through the alternate function muxing, and the GPIO unit manages their control and status.

## 16.8.2 Features

- A GPIO port configured as an input can also serve as an interrupt source  
- At system reset, by default all GPIO ports are configured as inputs until changed by the boot process or user software  
- Each GPIO port has a dedicated control signal  
- Supports separate interrupts on either the leading edge, the trailing edge, or both  
- The GPIO port output can be individually set or cleared  
- The GPIO port input can be individually read  

## 16.8.3 Registers

### 16.8.3.1 Base Addresses

| GPIO Block | Base Address |
|------------|----------------|
| AUD_GPIO_BASE | 0xC088_9400 |
| GPIO0_BASE     | 0xD401_9000 |
| GPIO1_BASE     | 0xD401_9040 |
| GPIO2_BASE     | 0xD401_9080 |
| GPIO3_BASE     | 0xD401_9100 |
| SEC_GPIO0_BASE | 0xF061_9000 |
| SEC_GPIO1_BASE | 0xF061_9040 |
| SEC_GPIO2_BASE | 0xF061_9080 |
| SEC_GPIO3_BASE | 0xF061_9100 |

> Note: GPIO0–GPIO3 base addresses are listed above for reference.

### 16.8.3.2 Register Overview

The GPIO control block contains a total of 52 32-bit registers, organized into six functional groups. Each GPIO port implements an identical set of registers, supporting up to 128 GPIOs.

1. Port State Monitoring (4 registers, read-only, one per port)

   - GPIO Pin-Level Registers (GPIO_PLRx) – Reflect current pin state.

2. Port Direction Control (12 registers)

   - 4x GPIO Pin Direction Registers (GPIO_PDRx) – Read/write. Set pin direction.
   - 4x Bit-wise Set of GPIO Direction Registers (GPIO_SDRx) – Write-only. Modifies GPIO_PDRx.
   - 4x Bit-wise Clear of GPIO Direction Registers (GPIO_CDRx) – Write-only. Modifies GPIO_PDRx.

3. Port State Control (8 registers, write-only)

   - 4x GPIO Pin Output Set Register (GPIO_PSRx) – Sets GPIO output port.
   - 4x GPIO Pin Output Clear Register (GPIO_PCRx) – Clears GPIO output port.

4. Rising Edge Detection (12 registers)

   - 4x GPIO Rising-Edge Detect Enable Registers (GPIO_RERx) – Read/write.
   - 4x Bit-wise Set of GPIO Rising Edge Detect Enable Registers (GPIO_SRERx) – Write-only. Modifies GPIO_RERx.
   - 4x Bit-wise Clear of GPIO Rising Edge Detect Enable Registers (GPIO_CRERx) – Write-only. Modifies GPIO_RERx.

5. Falling Edge Detection (12 registers)

   - 4x GPIO Falling-Edge Detect Enable Registers (GPIO_GFERx) – Read/write.
   - 4x Bit-wise Set of GPIO Falling Edge Detect Enable Registers (GPIO_SFERx) – Write-only. Modifies GPIO_FERx.
   - 4x Bit-wise Clear of GPIO Falling Edge Detect Enable Registers (GPIO_CFERx) – Write-only. Modifies GPIO_FERx.

6. Edge Detect Status (4 registers)

   - GPIO Edge Detect Status Register (GPIO_EDRx) – Indicates when specified edge types have been detected on ports.

**Reset Behavior**

- **GPIO_PDRx** is initialized on reset, configuring all GPIO pins as inputs.
- All other GPIO registers reset to `0x0000_0000`.

### 16.8.3.3 Register Description

#### GPIO PIN-LEVEL REGISTER

GPIO_PLR

The state of each of the GPIO ports is visible through this register. Each bit corresponds to the port number.

GPIO_PLR0[31:0] corresponds to GPIO[31:0]
GPIO_PLR1[31:0] corresponds to GPIO[63:32]
GPIO_PLR2[31:0] corresponds to GPIO[95:64]
GPIO_PLR3[31:0] corresponds to GPIO[127:96]

These read-only registers determine the current value of a particular port (regardless of the programmed port direction).

The 32 port-level bits are shown in the GPIO Pin-Level Registers.

Offset:0x0

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | PLX | RO | 0x0 | GPIO port level n (where n = 0 through 31)<br>0 = Port state is low<br>1 = Port state is high |

#### GPIO PIN DIRECTION REGISTER

GPIO_PDR

Users control port direction by programming the GPIO Pin Direction registers (GPIO_PDR0, GPIO_PDR1, GPIO_PDR2, and GPIO_PDR3). They contain one direction control bit for each of the 128 ports.

GPIO_PDR0[31:0] corresponds to GPIO[31:0]
GPIO_PDR1[31:0] corresponds to GPIO[63:32]
GPIO_PDR2[31:0] corresponds to GPIO[95:64]
GPIO_PDR3[31:0] corresponds to GPIO[127:96]

If a direction bit is programmed to 1, the GPIO function is an output. If it is programmed to 0, it is an input. 

A pair of set/clear registers (GPIO_SDRx and GPIO_CDRx) is also provided to enable the setting and clearing of individual bits in this register. 

At reset, all bits in this register are cleared, configuring all GPIO ports as inputs. 

The location of each port direction bit is shown in the GPIO Pin Direction Register (GPIO_PDR0).

Offset:0x4

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | PDX | RW | 0x0 | GPIO port direction n (where n = 0 through 31)<br>0 = Port configured as an input<br>1 = Port configured as an output |

#### GPIO PIN OUTPUT SET REGISTER

GPIO_PSR
Offset:0x8

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | PSX | WO | 0x0 | GPIO output port set n (where n = 0 through 31)<br>0 = Port level unaffected<br>1 = If port configured as an output, set port level logic high |

#### GPIO PIN OUTPUT CLEAR REGISTER

GPIO_PCR
Offset:0xC

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | PCX | WO | 0x0 | GPIO output port clear n (where n = 0 through 31)<br>0 = Port level unaffected<br>1 = If port configured as an output, clear port level logic low |

#### GPIO RISING-EDGE DETECT ENABLE REGISTER

GPIO_RER

The GPIO Edge Detect functionality described in this section is independent of, and in addition to, the Pin Control Unit edge-detect logic and is functional only when the GPIO alternate function is selected on the multi-function I/O pin. In addition, GPIO Edge Detect is used as an interrupt, while the Pin Control Unit edge-detect logic is mainly used as a wakeup event.

Each GPIO can be programmed to detect a rising edge, falling edge, or either transition on a port. When an edge is detected that matches the type of edge programmed for the port, a status bit is set.

The GPIO Rising-Edge Detect Enable and GPIO Falling-Edge Detect Enable Registers (GPIO_RERx and GPIO_FERx, respectively) select the type of transition on a GPIO port that causes a bit within the GPIO Edge-Detect Status Register (GPIO_EDRx) to be set. For a given GPIO port, its corresponding GPIO Rising-Edge Detect Enable Register bit is set to cause a GPIO Edge-Detect Status Register status bit to be set when the port transitions from logic level low to logic level high. Likewise, the GPIO Falling-Edge Detect Enable Register is used to set the corresponding GPIO Edge-Detect Status Register status bit when a transition from logic level high to logic level low occurs. When the corresponding bits are set in both registers, either a falling- or a rising-edge transition causes the corresponding GPIO Edge-Detect Status Register status bit to be set.

These registers contain one rising-edge detect control bit for each of the 128 ports.

GPIO_RER0[31:0] corresponds to GPIO[31:0]
GPIO_RER1[31:0] corresponds to GPIO[63:32]
GPIO_RER2[31:0] corresponds to GPIO[95:64]
GPIO_RER3[31:0] corresponds to GPIO[127:96]

These registers show the rising-edge enable bit locations corresponding to all 32 ports of GPIO_RER0. 

A pair of set/clear registers are also provided to enable the setting and clearing of individual bits of the GPIO Rising-Edge Detect Enable Registers. 

Offset:0x10

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | REX | RW | 0x0 | GPIO port n rising-edge detect enable (where n = 0 through 31)<br>0 = Disable rising-edge detect enable<br>1 = Set corresponding GPIO Edge Detect Status Register status bit when a rising edge is detected on the GPIO port |

#### GPIO FALLING-EDGE DETECT ENABLE REGISTER

GPIO_FERX

The GPIO Edge Detect functionality described in this section is independent of and in addition to the Pin Control Unit edge-detect logic and is only functional when the GPIO alternate function is selected on the multi-function I/O pin. In addition, the GPIO Edge Detect is used as an interrupt while the Pin Control Unit edge-detect logic is mainly used as a wakeup event.

Each GPIO can be programmed to detect a rising edge, falling edge, or either transition on a port. When an edge is detected that matches the type of edge programmed for the port, a status bit is set.

The GPIO Rising-Edge Detect Enable and GPIO Falling-Edge Detect Enable Registers (GPIO_RERx and GFERx, respectively) select the type of transition on a GPIO port that causes a bit within the GPIO Edge Detect Status Register (GPIO_EDRx) to be set. For a given GPIO port, its corresponding GPIO Falling-Edge Detect Enable Register bit is set to cause a GPIO Edge Detect Status Register status bit to be set when the port transitions from logic level high to logic level low. Likewise, the GPIO Rising-Edge Detect Enable Register is used to set the corresponding GPIO Edge Detect Status Register status bit when a transition from logic level low to logic level high occurs. When the corresponding bits are set in both registers, either a falling- or a rising-edge transition causes the corresponding GPIO Edge Detect Status Register status bit to be set.
This register shows the falling-edge enable bit locations corresponding to all 32 ports of GPIO_FERx.

A pair of set/clear registers are also provided to enable the setting and clearing of individual bits of the GPIO_FERx registers. 

Offset:0x14

| Offset | Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0x14 | 31:0 | FEX | RW | 0x0 | GPIO port falling-edge detect enable n (where n = 0 through 31)<br>0 = Disable falling-edge detect enable<br>1 = Set corresponding GPIO Edge Detect Status Register status bit when a falling edge is detected on the GPIO port |

#### GPIO EDGE DETECT STATUS REGISTER

GPIO_EDR

The GPIO Edge Detect Status Registers (GPIO_EDR0, GPIO_EDR1, GPIO_EDR2, and GPIO_EDR3) contain a total of 128 status bits that correspond to the 128 GPIO ports.

These registers contain one edge detect status bit for each of the 128 ports.

GPIO_EDR0[31:0] corresponds to GPIO[31:0]
GPIO_EDR1[31:0] corresponds to GPIO[63:32]
GPIO_EDR2[31:0] corresponds to GPIO[95:64]
GPIO_EDR3[31:0] corresponds to GPIO[127:96]

When an edge-detect occurs on a port that matches the type of edge programmed in the GPIO Rising-Edge Detect Enable and/or GPIO Falling-Edge Detect Enable Registers, the corresponding status bit is set in this register. Once a bit is set in this register, the CPU must clear it. Status bits in this register are cleared by writing a 1 to them. Writing a 0 has no effect.

Each edge detect that sets the corresponding status bit in this register for GPIO ports 0–127 can trigger an interrupt request. Ports 2–127 together form a group that can generate a single interrupt request when any of the status bits 2–127 in this register is set. GPIO ports 0 and 1 each generate their own independent first-level interrupt. This register shows the GPIO_EDR0 bit locations.

Offset:0x18

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | EDX | RWC | 0x0 | GPIO edge detect status n (where n = 0 through 31)<br>0 = No edge detect has occurred on the port as specified in GPIO Rising-Edge Detect Enable and/or GPIO Falling-Edge Detect Enable Registers<br>1 = Edge detect has occurred on the port as specified in the GPIO Rising-Edge Detect Enable and/or GPIO Falling-Edge Detect Enable Registers |

#### BIT-WISE SET OF GPIO DIRECTION REGISTER

GPIO_SDR

Users control port direction by programming the GPIO pin Bit-wise Set of GPIO Direction Registers (GPIO_SDR0, GPIO_SDR1, GPIO_SDR2, and GPIO_SDR3). These registers contain one direction control bit for each of the 128 ports.

GPIO_SDR0[31:0] corresponds to GPIO[31:0]
GPIO_SDR1[31:0] corresponds to GPIO[63:32]
GPIO_SDR2[31:0] corresponds to GPIO[95:64]
GPIO_SDR3[31:0] corresponds to GPIO[127:96]

If a direction bit is programmed to a 1, the corresponding bit in the GPIO Pin Direction Register is set and the GPIO function is configured as an output. If it is programmed to a 0, no change in the GPIO functionality or the GPIO Pin Direction Register occurs. 

At reset, all bits in this register are cleared. 

The location of each port direction bit is shown in the GPIO Pin Direction Register, GPIO_SDR0.

Offset:0x1C

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | PDX | WO | 0x0 | Set GPIO port direction n (where n = 0 through 31)<br>0 = GPIO Pin Direction Register bit not affected<br>1 = GPIO Pin Direction Register bit is set and GPIOx function is set to OUTPUT |

#### BIT-WISE CLEAR OF GPIO DIRECTION REGISTER

GPIO_CDR

Users control pin direction by programming the GPIO pin Bit-wise Clear of GPIO Direction Registers (GPIO_CDR0, GPIO_CDR1, GPIO_CDR2, and GPIO_CDR3). These registers contain one direction control bit for each of the 128 pins.

GPIO_CDR0[31:0] corresponds to GPIO[31:0]
GPIO_CDR1[31:0] corresponds to GPIO[63:32]
GPIO_CDR2[31:0] corresponds to GPIO[95:64]
GPIO_CDR3[31:0] corresponds to GPIO[127:96]

If a direction bit is programmed to a 1, the corresponding bit in GPIO Pin Direction Register is cleared and the GPIO function is configured as an input. If it is programmed to a 0, no change in the GPIO functionality or the GPIO Pin Direction Register occurs. 

At reset, all bits in this register are cleared. 

Refer to this register for the location of each port direction bit.

Offset:0x20

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | PDCX | WO | 0x0 | Set GPIO port direction n (where n = 0 through 31)<br>0 = GPIO Pin Direction Register bit not affected<br>1 = GPIO Pin Direction Register bit is cleared and GPIO n function is set to INPUT |

#### BIT-WISE SET OF GPIO RISING-EDGE DETECT ENABLE REGISTER

GPIO_SRERX

Offset:0x24

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | RESX | WO | 0x0 | Set GPIO rising-edge detect enable n (where n = 0 through 31)<br>0 = GPIO Rising-Edge Detect Enable Register bit is not affected<br>1 = GPIO Rising-Edge Detect Enable Register bit is set |

#### BIT-WISE SET OF GPIO FALLING-EDGE DETECT ENABLE REGISTER
GPIO_SFER
Offset:0x2C

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | FESX | WO | 0x0 | Set GPIO falling-edge detect enable n (where n = 0 through 31)<br>0 = GPIO Falling-Edge Detect Enable Register bit not affected<br>1 = GPIO Falling-Edge Detect Enable Register bit is set |

#### BIT-WISE CLEAR OF GPIO FALLING-EDGE DETECT ENABLE REGISTER
GPIO_CFER
Offset:0x30

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | FECX | WO | 0x0 | Clear GPIO falling-edge detect enable n (where n = 0 through 31)<br>0 = GPIO Falling-Edge Detect Enable Register bit not affected<br>1 = GPIO Falling-Edge Detect Enable Register bit is cleared |

#### BIT-WISE MASK OF GPIO EDGE DETECT REGISTER
APMASK_REG
Offset:0x34

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | EDMX | RW | 0x0 | Mask GPIO edge detect n (where n = 0 through 31)<br>0 = GPIO edge detects are masked<br>1 = GPIO edge detects are not masked |

#### BIT-WISE MASK OF GPIO EDGE DETECT REGISTER
CPMASK_REG
Offset:0x38

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | EDMX | RW | 0x0 | Mask GPIO edge detect n (where n = 0 through 31)<br>0 = GPIO edge detects are masked<br>1 = GPIO edge detects are not masked |