---
sidebar_position: 5
---

# Hardware FAQ

## Development & Debugging

1. **How to get the user guides for the K1 MUSE Pi development board?**

   - Development documentation is published on SpacemiT Developer Community. You can access the guide via the link:
     [K1 MUSE Pi User Guide](https://spacemit.com/community/document/info?lang=en&nodepath=hardware/eco/k1_muse_pi/pi_user_guide.md)

2. **How should the serial port and JTAG be connected for debugging on K1 MUSE Pi?**

   - **Serial port location**:
       The serial is a single-row 3-pin header, located between the Wi-Fi module and the 26-pin expansion header.
   - **Connection Method**:
       Connect the board's TX pin (as labeled on the silkscreen) to the RX pin of the serial cable, and connect the board's RX pin to the TX pin of the serial cable.
   - **Serial Debugging Requirements**:
      A 3.3 V serial cable is required.
      Baud rate: 115200 (serial port debugging tools should be set to this rate.)
   - **PRI JTAG Debugging**
     - PRI JTAG location:
          The PRI JTAG is located at pins 7, 11, 13, 15 of the 26 Pin, corresponding to PRI\_TDI, PRI\_TMS, PRI\_TCK and PRI\_TDO respectively.
     - PRI JTAG connection method:
          Wire pins 7, 11, 13, and 15 of the 26-pin header to the corresponding pins on your J-Link probe, matching the signal names. Connect pin 1 of the header to the VREF power pin on the J-Link.
   - **SEC JTAG Debugging**
     - SEC JTAG location:
          The SEC JTAG interface is located at the SD card slot, multiplexed with the SD card CLK and DATA0~3 pins. These correspond to SEC\_TCK, SEC\_TRSTn, SEC\_TDO, SEC\_TDI and SEC\_TMS respectively.
     - SEC JTAG connection method:
          Due to the SD card slot package design, these pins are not routed to external headers. It is recommended that you either fabricate a custom adapter board, or remove the SD card slot and make flying wire connections according to the board's schematic/position diagram.
     - SEC JTAG usage requirements:
       Before using the SEC JTAG interface, you must first configure the hardware as described in the [K1 MUSE Pi User Guide](https://spacemit.com/community/document/info?lang=en&nodepath=hardware/eco/k1_muse_pi/pi_user_guide.md) → Hardware Overview → Boot Download Sel & JTAG Sel section.

3. **Can components annotated "for test" in the schematic be removed?**

   - Yes. These components are generally not required for product functionality, and are only intended to provide convenience during the development and debugging.

4. **Is there any description of K1 PCB fabrication for trace impedance design?**

   - Yes, you can refer to [K1 Hardware Design Guide](https://spacemit.com/community/document/info?lang=en&nodepath=hardware/key_stone/k1/k1_hw/k1_hw_design_guide.md) for detailed specifications for impedance design and routing rules.

5. **What is the JTAG interface on the K1 used to debug?**

   - It is used for CPU debugging, supporting program download, as well as single-step debugging and breakpoint debugging.

## Power System

This section answers common questions about the power system, including DCIN, P1 (the multi-channel power management IC), power domains, DCDC, battery, charger, and fuel gauge.

1. **What is the accuracy of the RTC integrated in P1?**

   - The RTC in P1 has an accuracy of 20 ppm.

2. **Which power rails remain powered during sleep and shutdown?**

   - In sleep mode, the following powers are turned off:
     - Buck4, Buck3
     - ALDO0, ALDO1, ALDO2, ALDO3
     - DLDO0, DLDO1, DLDO2
   - When the device is in shutdown state with external power still connected, the AONLDO (Always-On LDO) remains powered to maintain the power button functionality.

3. **Can the ferrite beads in the K1 power supply design be removed?**

   - No. Ferrite beads are used to isolate the analog PHY power supply from the digital power supply, helping maintain power integrity and stability. Removing them may introduce power noise and reduce chip performance.

4. **Can unused LDOs on P1 be reassigned to other functions?**

   - Yes, but the following points should be verified:
     - Confirm that the default LDO output voltage meets the application requirements.
     - Confirm that the target peripheral can tolerate the LDO output voltage.

5. **Can the PMIC automatically power on the system at a scheduled time while the system is powered off?**

   - Yes,
     - The PMIC supports RTC alarm wake-up.
     - When the scheduled time is reached, P1 starts directly without any additional interrupt output signal.

6. **Does P1 support automatic power-on when an adapter is connected?**

   - In the current design, P1 powers up automatically when the adapter is connected, and no manual action is required.

7. **If P1 does not use a dedicated adapter detection circuit, how is adapter insertion detected?**

   - Detection is handled by the internal detection mechanism integrated into P1.
   - P1 detects the VIN input through its internal circuitry and then triggers power-on.

8. **If the battery still has charge and the system is powered off, will connecting the adapter automatically power on the system?**

   - No. In this case, connecting the adapter will not automatically start the system. Manual power-on through the button is required.

9. **Can P1 be powered directly from a 3.7 V battery?**

   - Yes. P1 can be powered directly from a 3.7 V battery.

10. **Is the on/off timing of the integrated SW switch in P1 configurable?**

    - No. The on/off timing of the integrated switch in P1 is fixed and cannot be adjusted.

11. **Why does the integrated SW switch in P1 still conduct even when it is off?**

    - This is a known design characteristic. When SW is off, current can still flow through the body diode of the MOSFET integrated in the P1 SW path, but the current capability is very limited.
    - Recommendation: To ensure normal operation and expected performance, SW should be enabled during standard use.

12. **Does P1 provide an always-on LDO that becomes active immediately after power is applied?**

    - Yes. P1 includes an always-on LDO called AONLDO. It begins outputting as soon as P1 is powered, and its default output voltage is 1.8 V.

13. **Can all ALDO-series LDOs be configured to 3.3 V, switched quickly to 3.3 V during startup, and kept enabled during sleep to provide continuous power?**

    - Yes, all ALDO-series LDOs can be configured for 3.3 V output.
    - During system startup, ALDO can be set to 3.3 V in the SPL stage through rapid configuration. This takes about 490 ms.
    - ALDO can also be kept enabled during sleep so that critical circuits remain powered.

14. **Can the output voltage of every LDO on P1 be adjusted?**

    - Yes. The output voltage can be customized as needed, but the default enable state and default voltage setting of each LDO must be taken into account.

15. **Can 8-core CPU support independent power off for each core**

    - No, but it supports independent power off for each cluster.

## Storage System

This section answers common questions about the storage system, including DRAM, eMMC, TF card, SSD, SPI Flash, and EEPROM.

1. **What is the purpose of adding an EEPROM?**
   - It is used to identify different hardware configurations, allowing a single firmware image to support multiple hardware variants.

## Clock System

This section answers common questions about the clock system, including DCXO and PLL.

## Reset System

This section answers common questions about the reset system.

## Display System

This section answers common questions about the display system, including MIPI DSI and HDMI.

1. **If DSI is not used, does the DSI block still need power?**
   - Yes. Even when the DSI module is not used, it still requires power.

## Audio System

This section answers common questions about the audio system, including codec, speaker, PA, and MIC.

## Camera System

This section answers common questions about the camera system, including MIPI CSI and USB.

1. **If CSI is not used, does the CSI block still need power?**
   - Yes. Even when the CSI module is not used, it still requires power.

## Networking System

This section answers common questions about the networking system, including Ethernet, Wi-Fi, BT, 4G, and 5G.

1. **If 100M Ethernet is used and the PHY supply voltage is only 3.3 V, how should the connection be made?**

   - Our GMAC does not support 100M PHYs, and only supports 1000M PHYs.
   - Recommendation: Use a 1000M PHY for connection.

2. **In a single-port Ethernet application, does selecting GMAC0 or GMAC1 affect software behavior?**

   - No. In a single-port application, using GMAC0 or GMAC1 does not affect software functionality.

## Peripherals and Interfaces

This section answers common questions about peripherals and interfaces, including USB, SPI, I2C, I2S, UART, PCIe, ADC, PWM, CAN, GPIO, Key, CTP, Sensor and LED.

1. **Do all K1 IOs support interrupt input?**

   - No. Only IOs multiplexed to GPIO functions support interrupt input.

2. **Is GPIO90 only used for detection during boot, and can it be used as a general-purpose I/O pin afterwards?**

   - Yes, GPIO90 is used for detection functions during the boot sequence, and can be repurposed as a general-purpose I/O pin after boot completion.

3. **Does K1 provides SATA interface?**

   - K1 does not provide a native SATA interface. However, SATA can be added through a PCIe-to-SATA bridge, and ASM1061 and JMB582 adapter cards are already supported.

4. **Does USB2 support OTG?**

   - Yes, USB2 supports OTG functionality. It can act as an OTG interface, but does not support firmware download.

5. **Does USB0 default to device mode at power-up? Besides firmware download, can it also operate in host mode?**

   - USB0 defaults to device mode at power-up for firmware download.
   - It also supports host mode for connecting other USB devices.

6. **After a PCIe-to-SD card interface is used, is TF-card-based firmware download still supported?**

   - No. TF-card-based firmware download is not supported when a PCIe-to-SD card interface is used.

7. **Does K1 support ADC functionality?**

   - K1 does not support ADC functionality, but P1 does.

8. **How to get the description and pin location of the can?**

   - The CAN functionality can be configured via the following pins:
   - GPIO75 & GPIO76 (Located at Pin 23 and Pin 24 of the 26-Pin)
   - GPIO47 & GPIO48 (Located at Pin 8 and Pin 10 of the 26-Pin)

9. **What is the on-chip consumption (in dB) of K1 high-speed interfaces (such as USB, PCIe)?**

   - The on-chip consumption of the K1 is less than 1 dB.
   - Please refer to the specifications of each interface protocol for detailed board-level consumption control requirements.

10. **Why is an additional diode required for MOSFET level shifting circuits?**

    - The purpose of adding the diode is to reduce the voltage drop from the 1.8 V side to the 3.3 V side when the 3.3 V side is pulled low, and to prevent potential reliability issues.
    - Based on practical field experience, this diode is not mandatory. It has been omitted from all subsequent mass-production products.

11. **For a PCIe 2.1 x2 interface with 2 lanes, if I only use 1 lane, can I select it arbitrarily?**

     - No. When the PCIe 2.1 x2 interface is configured for 1-lane operation, you must use the TX0N/P and RX0N/P lane pair.

12. **For the GPIOs (GPIO98 ~ GPIO103) assigned to the QSPI interface, are there any design considerations if they are repurposed to connect UART devices?**  

     - UART5 on GPIO102/103 is the preferred option.  The UART on GPIO98~GPIO101 should only be used when its initial state is fully confirmed. This is because GPIO98~GPIO101 function as strap pins, whose initial power-up state determines the chip's boot order, download mode, and download interface configuration.

13. **Is it necessary to add a diode to the level-shifting circuit?**

      - No, it is not required.

## Reliability

This section answers common questions about reliability, including ESD, high and low temperature operation, humidity, lifetime, and EMI.

## Product Certification

This section answers common questions about product certification, including RoHS, CE, CCC, and FCC.

## Other

This section answers miscellaneous questions that do not fall into the categories above, including PCB, mechanical structure, power consumption, thermal design measures, and surface temperature.

1. **What is the power consumption of K1 in sleep mode?**

   - 28 mW.

2. **What are the impedance control requirements for K1 single-ended and differential traces?**

   - For single-ended traces, the impedance target is 50Ω.
   - For differential traces, the impedance target is 90Ω.

3. **Is 90 Ω differential impedance control mandatory for the K1?**

   - The differential lines for the DDR interface must be controlled to 90 Ω.
   - For all other differential lines, the impedance can be set to either 90 Ω or 100 Ω.

4. **The K1 MUSE N1 has many capacitors placed under the CPU, while the K1 MUSE Pi has very few.**

   - The K1 MUSE N1 layout is optimized for the actual fanout area of the SoC. With fewer fanout signals, there is more space on the backside to place capacitors, allowing for a higher capacitor count.
   - In contrast, the K1 MUSE Pi routes out all signals, leaving limited backside space for additional components. This design has been validated through simulation and testing, and is both robust and reliable.
