---
sidebar_position: 5
---

# 16.5 PWM

## 16.5.1 Overview

K3 contains 20 Pulse-Width Modulation (PWM) channels labeled as PWMx where x=[0,19].

Each PWM channel operates independently, with its own configuration registers, and generates a PWM output signal on a multifunction pin.

Each PWM channel allows control of both the leading-edge timing and the trailing-edge timing of its output signal.

The timing of each PWM channel can be configured to run continuously or be adjusted dynamically to meet changing requirements.

The power-saving mode allows the internal clock of a PWM channel (PSCLK_PWM) to be stopped, forcing the corresponding output signal (PWM_OUT) to remain at a constant high or low level. This saves power when the output signal is not required.

## 16.5.2 Features

- Supports a 50% duty cycle from 198.4 Hz to 6.5 MHz (additional duty-cycle options depend on the selected frequency)
- Supports enhanced period control through a 6-bit clock divider and a 10-bit period counter
- Supports 15-bit pulse-counter control

## 16.5.3 Register Description

> Note: The base address of the PWMn registers (`n = 1, 2, ..., 20`) is `0xD401A000`, with a stride of `0x400`.

### PWM_CRX Register

PWM control registers. 

These registers configure the PWM shutdown behavior and the divider applied to the input clock of the PWM control unit, which determines the frequency of the scaled counter clock.

Offset: 0x0 + (n - 1) * 0x400

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:9 | Reserved | RO | 0x0 | Reserved for future use. |
| 8 | PWM_OUTCNTen | RW | 0x0 | PWM output counter register enable. <br>`0`: Disable. <br>`1`: Enable. |
| 7 | Reserved | RO | 0x0 | Reserved for future use. |
| 6 | PWM shutdown mode | RW | 0x0 | `0`: Graceful shutdown of the PWM when the SoC stops the clock to the PWM. <br>`1`: Abrupt shutdown of the PWM when the SoC stops the clocks to the PWM. |
| 5:0 | Prescale | RW | 0x0 | The scaled counter clock frequency is `PSCLK_PWM / (PRESCALE + 1)`. |

### PWM_DCR Register

PWM duty-cycle registers.

These registers configure the duty cycle of the corresponding PWM_OUT signals.

Offset: 0x4 + (n - 1) * 0x400

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:11 | Reserved | RO | 0x0 | Reserved for future use. |
| 10 | Full duty cycle | RW | 0x0 | `0`: `PWM_OUT` is determined by the `<Duty Cycle of PWM_OUT>` value. `1`: `PWM_OUT` is continuously asserted. |
| 9:0 | Duty cycle of PWM_OUT | RW | 0x0 | `0`: `PWM_OUT` is continuously deasserted. <br>`1`: `PWM_OUT` is high for a number of 12 MHz clock periods equal to this field (`<PRESCALE>` in the PWM control registers + 1). <br>If `<Full Duty Cycle>` is set, this field has no effect on the PWM output. |

### PWM_PCR Register

PWM period control registers.

These registers configure the cycle time of the corresponding PWM_OUT signals.

If this register is cleared, the `PWM_OUT` signal remains in a high state.

Offset: 0x8 + (n - 1) * 0x400

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:10 | Reserved | RO | 0x0 | Reserved for future use. |
| 9:0 | Period value | RW | 0x4 | The number of scaled clock cycles per `PWM_OUT` cycle, plus one. <br>If all zeros are written to this register, the signal remains high. |

### PWM_OUTCNT Register

PWM output counter registers.

Offset: 0x10 + (n - 1) * 0x400

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:16 | Reserved | RO | 0x0 | Reserved for future use. |
| 15:0 | Counter value | RW | 0x0 | The number of `PWM_OUT` pulses. |
