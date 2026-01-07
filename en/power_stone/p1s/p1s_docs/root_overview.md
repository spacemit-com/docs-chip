sidebar_position: 1

# P1S Brief

## Overview

P1S is a high-performance multi-channel power management chip (PMIC), designed to provide customized power solutions for complex computing systems and meet the differentiated and high-demanding power requirements of customers.

P1S is mainly used for AR/VR, industrial devices, AI Robots and drone.

- **Highly Flexible Power Management Capabilities**
It features 6 channels of COT (Constant On-Time) control buck converters, 12 Low Drop-Out (LDO) regulators, and an I2C interface, providing highly flexible power management capabilities for a range of mobile devices and embedded systems.

- **Provide Safe and Stable Power**
Six integrated buck converters power a variety of target rails. Constant-on-time (COT) control offers fast transient performance. The 1.5MHz, default, fixed switching frequency during continuous conduction mode (CCM) reduces the external inductor and capacitor values greatly. Full protection features include UVLO, OCP, OVP and thermal shutdown. Dynamic voltage control (DVC) enables supply voltage controllability based on the application requirements. The output voltage and start up/shutdown sequence can be  preset by the multiple-time programmable (MTP) interface and controlled via the I2C bus. 

- **Compact Package**
The P1S requires a minimal number of external components, and is available in a compact QFN-60 (7mmx7mm) package.

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

- **5 Programmable LDO regulators** 
  - 1 Dedicated always on LDO
  - 5 Low-Noise LDOs 
  - VOUT: 0.5V ~ 3.4V, 25mV step
  - IOUT: 0.3A max

- **I2C communication interface**

- **System monitor with watchdog timer**

- **12-bits ADC with 8 channels and configurable alarm thresholds**

- **Output voltage and start up/shutdown sequence can be  preset by MTP**

- **6 GPIO pins for peirpheral control**

- **-40℃ ~ 125℃ junction temperature**

- **Package: QFN-60 7mm * 7mm, 0.4mm pitch**

## Block Diagram

![](static/G8rTbP4A8oDQ2rxA4X5czogpnmc.png)
