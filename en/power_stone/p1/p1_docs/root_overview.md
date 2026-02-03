sidebar_position: 1

# P1 Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/chip/P1/P1_brief_en.pdf)**

## Overview

P1 is a high-performance multi-channel power management chip (PMIC), designed to provide customized power solutions for complex computing systems and meet the differentiated and high-demanding power requirements of customers.

P1 is mainly used for AR/VR, industrial devices, AI Robots and drone.

- **Highly Integrated Power Management Solution**
   Integrates 6 constant on-time (COT) buck converters, 12 low-dropout regulators (LDOs), an I²C interface, and multiple-time programmable (MTP) non-volatile memory, providing highly flexible power management for a wide range of mobile and embedded systems.

- **Comprehensive and Reliable Protection Mechanisms**
   Includes a full set of protection features such as undervoltage lockout (UVLO), overvoltage protection (OVP), overcurrent protection (OCP), and thermal shutdown.

- **Industrial-Grade Operating Range**
   Operates stably and reliably over an ambient temperature range of –40°C to +85°C, meeting the demanding requirements of industrial applications.

- **Compact Package**
   Requires only a minimal number of external components and is offered in a compact QFN-60 (7 mm × 7 mm) package.

## Key Features

- **Power supply voltage (VIN)**
  - 2.6V ~ 5.5V

- **6 High-Efficiency Buck Converters**
  - Buck1/2: 0.5V ~ 3.4V, 4A , can dual phase operation
  - Buck3/4: 0.5V ~ 3.4V, 2.5A , can dual phase operation
  - Buck5/6: 0.5V ~ 3.4V, 2.5A
  - Selectable output voltage range for all bucks: 0.5V ~ 1.35V, 5mV step or 1.375V ~ 3.4V, 25mV step
  - Adjustable current-limit threshold allowing optimization for different applications with different load currents 
  - Dedicated pins for VDDQ voltage select for DDR support 

- **12 Programmable LDO regulators** 
  - 1 Dedicated always on LDO
  - 11 Low-Noise LDOs 
  - VOUT: 0.5V ~ 3.4V, 25mV step
  - IOUT: 0.3A max

- **1 Load Switch, 1A max**

- **I2C communication interface**

- **System monitor with watchdog timer**

- **Coin cell/super-capacitor backup charger**

- **Ultra-low power, 2 µA RTC with alarm**

- **12-bits ADC with 8 channels and configurable alarm thresholds**

- **Output voltage and start up/shutdown sequence can be  preset by MTP**

- **6 GPIO pins for peirpheral control**

- **-40℃ ~ 125℃ junction temperature**

- **Package: QFN-60 7mm * 7mm, 0.4mm pitch**

## Block Diagram

![](static/CVgqbZypMo36kHx5vpEcOhPAnMg.png)
