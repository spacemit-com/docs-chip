---
sidebar_position: 10
---

# 16.10 Power Management and Low-Power Mode Control

## 16.10.1 Overview

The PMU module is a hardware unit within the SoC and is primarily responsible for managing CPU core power-on and power-off functions.

## 16.10.2 Features

- Manage CPU core and cluster power on/off
- Capture external wake-up sources to wake up the CPU
- Support system suspend management

## 16.10.3 Registers

### Core Power-Down Voting Register

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:22 | Reserved | RO | 0 | Reserved for future use. |
| 21:20 | Power switch mode | RW | 0 | Power switch mode.<br>The core has both a large macro power switch and distributed power switches. This field selects the power switch mode.<br>`0` = Both the large macro switches and distributed switches are used. |
| 19 | Disable L1 sleep | RW | 0 | Disable L1 sleep.<br>This field disables core L1 SRAM power-switch power-down during core power-down mode.<br>`1` = Disable core L1 SRAM switch sleep. |
| 18 | Disable core sleep | RW | 0 | Disable core sleep.<br>This field disables core switch sleep power-down during core power-down mode.<br>`1` = Disable core power-switch sleep. |
| 17:12 | Reserved | RO | 0 | Reserved for future use. |
| 11 | Mask core clock off state check | RW | 0 | Mask core clock-off state check.<br>Masks the core clock-off check during the core idle process. |
| 10 | Mask core clock stable state check | RW | 0 | Mask core clock stable-state check.<br>Masks the core clock stable check during core wake-up. |
| 9 | Mask JTAG idle state check | RW | 0 | Mask JTAG idle-state check.<br>Masks the JTAG idle check during MP idle entry.<br>`1` = Mask the JTAG idle check. |
| 8 | Mask core WFI idle state check | RW | 0 | Mask core WFI idle-state check.<br>Debug only. |
| 7:5 | Reserved | RO | 0 | Reserved for future use. |
| 4 | GIC nFIQ global mask | RW | 0 | GIC nFIQ global mask.<br>Masks nFIQ generated in the GIC for the core. Software can set this bit before the core enters power-down mode. APMU hardware automatically clears this bit when the core enters power-down mode. |
| 3 | GIC nIRQ global mask | RW | 0 | GIC nIRQ global mask.<br>Masks nIRQ generated in the GIC for the core. Software can set this bit before the core enters power-down mode. APMU hardware automatically clears this bit when the core enters power-down mode. |
| 2 | Core L1 SRAM power down | RW | 0 | Core L1 SRAM power down.<br>Not used. |
| 1 | Core power down | RW | 0 | Core power down.<br>This bit has no effect if bit `[0]` is `0`.<br>`1` = When the core enters WFI idle, the core enters deep-sleep mode and power is turned off. |
| 0 | Core idle | RW | 0 | Core idle.<br>`1` = When the core enters WFI idle, the core clock is gated externally. |

### Cluster Power-Down Voting Register

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:20 | Reserved | RO | 0 | Reserved for future use. |
| 19 | Disable Application MP L2 power switch | RW | 0 | Disable Application MP L2 power switch.<br>This field disables Application MP L2 power-switch sleep power-down during Application MP power-down mode.<br>`1` = Disable. |
| 18 | Disable Application MP power switch mode | RW | 0 | Disable Application MP power switch.<br>This field disables Application MP power-switch sleep power-down during MP subsystem power-down mode.<br>`1` = Disable MP power-switch sleep mode. |
| 17 | Reserved | RO | 0 | Reserved. |
| 16 | FRC L2 SRAM off | RW | 0 | Force L2 SRAM off.<br>`1` = L2 cache power is off. |
| 15:14 | Reserved | RO | 0 | Reserved. |
| 13 | L2 hardware cache flush enable | RW | 0 | L2 hardware cache flush enable.<br>`1` = Enable. |
| 12 | Mask SRAM repair done check | RW | 0 | Mask SRAM repair-done check.<br>`1` = Mask the SRAM repair-done check. |
| 11 | Mask core clock off state check | RW | 0 | Mask MP clock-off stable check.<br>This field masks the MP clock-off stable check during the MP idle process. |
| 10 | Mask core clock stable state check | RW | 0 | Mask MP clock stable check.<br>This field masks the MP clock stable check during MP wake-up. |
| 9 | Mask JTAG idle state check | RW | 0 | Mask the JTAG idle check during MP idle entry.<br>`1` = Mask the JTAG idle check. |
| 8 | Mask idle state check | RW | 0 | Mask Application MP idle-state check. Debug only.<br>This field should be `0` during normal operation.<br>`1` = Status check masked<br>`0` = Status check not masked |
| 7 | ACINACTM hardware control | RW | 0 | ACINACTM hardware control.<br>`0` = The low-power state machine does not control the ACINACTM port.<br>`1` = The low-power state machine controls the Application MP ACINACTM port.<br>When M2/M1 low-power mode is entered, the ACINACTM port is high. |
| 6 | Reserved | RO | 0 | Reserved. |
| 5 | Disable memory controller software REQ | RW | 0 | Disable memory controller software request.<br>This field disables memory controller entry into idle mode through the memory controller sleep request bits. |
| 4 | Application MP wake MC enable | RW | 0 | Application MP wake memory controller enable.<br>Wakes up the memory controller when the Application MP wakes up from idle mode.<br>The memory controller is woken up before the interrupt to the core is released. |
| 3 | SCU SRAM Power Down | RW | 0 | Not used. |
| 2 | L2 cache SRAM power down | RW | 0 | L2 cache SRAM power down.<br>This field has no effect if bit `[1]` is `0`.<br>`1` = When Application MP is idle, L2 SRAM power is turned off.<br>`0` = When Application MP is idle, L2 SRAM remains in retention mode. |
| 1 | Application MP power down | RW | 0 | Application MP power down.<br>This bit has no effect if bit `[0]` is `0`.<br>`1` = When Application MP is idle, Application MP enters deep-sleep mode and power is turned off. |
| 0 | Application MP idle | RW | 0 | Application MP idle.<br>`1` = When Application MP is idle, the Application MP clocks are gated externally. |

### Core Wake-Up Register

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | Reserved | RO | 0 | Reserved for future use. |
| 15 | Wakeup Core15 | RO | 0 | Wake up Core15.<br>If software writes `1` to this field, core 15 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 15 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 15 exits `C1/C2` mode. |
| 14 | Wakeup Core14 | RW | 0 | Wake up Core14.<br>If software writes `1` to this field, core 14 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 14 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 14 exits `C1/C2` mode. |
| 13 | Wakeup Core13 | RW | 0 | Wake up Core13.<br>If software writes `1` to this field, core 13 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 13 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 13 exits `C1/C2` mode. |
| 12 | Wakeup Core12 | RW | 0 | Wake up Core12.<br>If software writes `1` to this field, core 12 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 12 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 12 exits `C1/C2` mode. |
| 11 | Wakeup Core11 | RW | 0 | Wake up Core11.<br>If software writes `1` to this field, core 11 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 11 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 11 exits `C1/C2` mode. |
| 10 | Wakeup Core10 | RW | 0 | Wake up Core10.<br>If software writes `1` to this field, core 10 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 10 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 10 exits `C1/C2` mode. |
| 9 | Wakeup Core9 | RW | 0 | Wake up Core9.<br>If software writes `1` to this field, core 9 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 9 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 9 exits `C1/C2` mode. |
| 8 | Wakeup Core8 | RW | 0 | Wake up Core8.<br>If software writes `1` to this field, core 8 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 8 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 8 exits `C1/C2` mode. |
| 7 | Wakeup Core7 | RW | 0 | Wake up Core7.<br>If software writes `1` to this field, core 7 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 7 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 7 exits `C1/C2` mode. |
| 6 | Wakeup Core6 | RO | 0 | Wake up Core6.<br>If software writes `1` to this field, core 6 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 6 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 6 exits `C1/C2` mode. |
| 5 | Wakeup Core5 | RW | 0 | Wake up Core5.<br>If software writes `1` to this field, core 5 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 5 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 5 exits `C1/C2` mode. |
| 4 | Wakeup Core4 | RW | 0 | Wake up Core4.<br>If software writes `1` to this field, core 4 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 4 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 4 exits `C1/C2` mode. |
| 3 | Wakeup Core3 | RW | 0 | Wake up Core3.<br>If software writes `1` to this field, core 3 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 3 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 3 exits `C1/C2` mode. |
| 2 | Wakeup Core2 | RW | 0 | Wake up Core2.<br>If software writes `1` to this field, core 2 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 2 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 2 exits `C1/C2` mode. |
| 1 | Wakeup Core1 | RW | 0 | Wake up Core1.<br>If software writes `1` to this field, core 1 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 1 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 1 exits `C1/C2` mode. |
| 0 | Wakeup Core0 | RW | 0 | Wake up Core0.<br>If software writes `1` to this field, core 0 is woken up.<br>Writes of `0` to this bit, and writes to this bit when core 0 is in `C0 (WFI)` mode, are ignored.<br>This bit is cleared by PMU hardware when core 0 exits `C1/C2` mode. |

### APCR_COREX Voting Register

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31 | AXISD | RW | 0 | AXISD<br>Allows AXI buses and agents to be shut down after the Application MP cores enter idle states.<br>`0` = AXI shutdown is not allowed.<br>`1` = AXI shutdown is allowed. |
| 30 | DSPSD | RW | 0 | Not used |
| 29 | SLPEN | RW | 0 | SLPEN<br>Allows the PMU to switch the system to sleep mode after the system reaches idle mode.<br>`0` = Sleep mode is not allowed.<br>`1` = Sleep mode is allowed. |
| 28 | Reserved | RO | 0 | Reserved for future use. |
| 27 | DDRCORSD | RW | 0 | DDRCORSD<br>Allows Application MP core clocks and TC DDR clocks to shut down. The clocks are halted when `CPCR[DDRCORSD]`, `APCR[DDRCORSD]`, and `DPCR[DDRCORSD]` are set and the Application MP core is in idle mode.<br>`0` = Application MP core and TC DDR clock shutdown is not allowed.<br>`1` = Application MP core and TC DDR clock shutdown is allowed. |
| 26 | APBSD | RW | 0 | APBSD<br>Allows the PMU to shut down APB clocks to all recipients, overriding other per-mode fields. The APB clock is actually shut down once the cores are idle and `CPCR[APBSD]`, `APCR[APBSD]`, and `DPCR[APBSD]` are set.<br>`0` = APB clock shutdown is not allowed.<br>`1` = APB clock shutdown is allowed. |
| 25 | BBSD | RW | 0 | BBSD<br>Allows the PMU to shut down all clocks provided to the baseband logic except the `32.768 kHz` clock.<br>The baseband logic clocks are halted as soon as `CPCR[BBSD]`, `APCR[BBSD]`, and `DPCR[BBSD]` are set and the `pm_bb_clkres` port is negated.<br>`0` = Baseband clock shutdown is not allowed.<br>`1` = Baseband clock shutdown is allowed. |
| 24:20 | Reserved | RO | 0 | Reserved for future use. |
| 19 | VCTCXOSD | RW | 0 | VCTCXOSD<br>Allows VCTCXO shutdown when the system is in sleep mode.<br>VCTCXO is shut down when `CPCR[VCTCXOSD]`, `APCR[VCTCXOSD]`, and `DPCR[VCTCXOSD]` are set and the system enters sleep mode.<br>`0` = VCTCXO shutdown is not allowed.<br>`1` = VCTCXO shutdown is allowed. |
| 18:15 | Reserved | RO | 0 | Reserved for future use. |
| 14 | MASSLPEN | RW | 0 | MASSLPEN<br>Allows the MSA subsystem to enter sleep mode after it reaches subsystem idle mode.<br>Sleep mode is allowed when `CPCR[MASSLPEN]`, `APCR[MASSLPEN]`, and `DPCR[MASSLPEN]` are set.<br>`0` = MSA sleep mode is not allowed.<br>`1` = MSA sleep mode is allowed. |
| 13 | STBYEN | RW | 1 | STBYEN<br>Allows the Apps subsystem to shut down and enter UDR mode when the AP subsystem is in sleep mode.<br>UDR is enabled when `CPCR[STBYEN]` and `APCR[STBYEN]` are both set and the AP subsystem enters AP sleep. |
| 12:4 | Reserved | RO | 0 | Reserved for future use. |
| 3 | C0_VOTE_AP_SLPEN | RW | 1 | C0 vote APMU sleep enable. |
| 2:0 | Reserved | RO | 0 | Reserved for future use |

### APCR_PER Voting Register

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31 | AXISD | RW | 0 | AXISD<br>Allows AXI buses and agents to be shut down after the Application MP cores enter idle states.<br>`0` = AXI shutdown is not allowed.<br>`1` = AXI shutdown is allowed. |
| 30 | DSPSD | RW | 0 | Not used |
| 29 | SLPEN | RW | 0 | SLPEN<br>Allows the PMU to switch the system to sleep mode after the system reaches idle mode.<br>`0` = Sleep mode is not allowed.<br>`1` = Sleep mode is allowed. |
| 28 | Reserved | RO | 0 | Reserved for future use. |
| 27 | DDRCORSD | RW | 0 | DDRCORSD<br>Allows Application MP core clocks and TC DDR clocks to shut down. The clocks are halted when `CPCR[DDRCORSD]`, `APCR[DDRCORSD]`, and `DPCR[DDRCORSD]` are set and the Application MP core is in idle mode.<br>`0` = Application MP core and TC DDR clock shutdown is not allowed.<br>`1` = Application MP core and TC DDR clock shutdown is allowed. |
| 26 | APBSD | RW | 0 | APBSD<br>Allows the PMU to shut down APB clocks to all recipients, overriding other per-mode fields. The APB clock is actually shut down once the cores are idle and `CPCR[APBSD]`, `APCR[APBSD]`, and `DPCR[APBSD]` are set.<br>`0` = APB clock shutdown is not allowed.<br>`1` = APB clock shutdown is allowed. |
| 25 | BBSD | RW | 0 | BBSD<br>Allows the PMU to shut down all clocks provided to the baseband logic except the `32.768 kHz` clock.<br>The baseband logic clocks are halted as soon as `CPCR[BBSD]`, `APCR[BBSD]`, and `DPCR[BBSD]` are set and the `pm_bb_clkres` port is negated.<br>`0` = Baseband clock shutdown is not allowed.<br>`1` = Baseband clock shutdown is allowed. |
| 24:20 | Reserved | RO | 0 | Reserved for future use. |
| 19 | VCTCXOSD | RW | 0 | VCTCXOSD<br>Allows VCTCXO shutdown when the system is in sleep mode.<br>VCTCXO is shut down when `CPCR[VCTCXOSD]`, `APCR[VCTCXOSD]`, and `DPCR[VCTCXOSD]` are set and the system enters sleep mode.<br>`0` = VCTCXO shutdown is not allowed.<br>`1` = VCTCXO shutdown is allowed. |
| 18:15 | Reserved | RO | 0 | Reserved for future use. |
| 14 | MSASLPEN | RW | 0 | MSASLPEN<br>Allows the MSA subsystem to enter sleep mode after it reaches subsystem idle mode.<br>Sleep mode is allowed when `CPCR[MASSLPEN]`, `APCR[MASSLPEN]`, and `DPCR[MASSLPEN]` are set.<br>`0` = MSA sleep mode is not allowed.<br>`1` = MSA sleep mode is allowed. |
| 13 | STBYEN | RW | 1 | STBYEN<br>Allows the Apps subsystem to shut down and enter UDR mode when the AP subsystem is in sleep mode.<br>UDR is enabled when `CPCR[STBYEN]` and `APCR[STBYEN]` are both set and the AP subsystem enters AP sleep. |
| 12:4 | Reserved | RO | 0 | Reserved for future use. |
| 3 | PER_VOTE_AP_SLPEN | RW | 1 | Peripheral vote APMU sleep enable. |
| 2:0 | Reserved | RO | 0 | Reserved for future use |
