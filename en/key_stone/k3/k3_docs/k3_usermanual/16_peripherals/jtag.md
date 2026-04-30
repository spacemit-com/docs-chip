---
sidebar_position: 11
---

# 16.11 JTAG

## 16.11.1 Overview

JTAG provides a way to observe internal states and access chip resources, including processors and peripherals.
The JTAG logic consists of:

- Test Access Port (TAP) controller
- TAP pins
- Instruction register
- Test Data Registers (TDRs)

The registers include:
- Boundary Scan Register (BSR) to control the IO pins directly
- Bypass register
- Device Identification (ID) register
- Data-specific registers

Data is shifted into all registers serially, most significant bit (MSB) first.

The JTAG interface is controlled through five dedicated TAP controller pins:
- TDI
- TMS
- TCK
- TRSTn
- TDO

## 16.11.2 Features

- Provides access through the JTAG port to IEEE Std. 1149.1-compatible registers such as IDCODE, BYPASS, and EXTEST
- Supports hardware and software debugging through the core TAP controller in concatenation mode

> Note: For detailed explanations of these terms and TAP controller states, refer to IEEE Std. 1149.1

## 16.11.3 Functional Description

The JTAG can be selected and configured to connect to either the CPU processors (X100™/A100™) or the RCPU, as follows:

- `jtag tap_ctl(0x98) = 0xa`: Primary JTAG routes to X100™/A100™
- `jtag tap_ctl(0x98) = 0xe`: Primary JTAG routes to RCPU

After the chip is powered on, a TAP can be detected on the JTAG chain, and it can be configured to determine whether it is routed to the CPU or the RCPU. Once the configuration is complete, the JTAG chain changes, and three TAPs can be scanned, with the middle TAP used to debug the CPU.
