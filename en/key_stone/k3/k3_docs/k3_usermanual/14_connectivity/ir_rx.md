---
sidebar_position: 8
---

# 14.8 IR-RX

## 14.8.1 Overview

The IR-RX module is capable of receiving infrared signals and transforming the received signals into digital format. Received data can be accessed through FIFO by checking status or configuring interrupt.

## 14.8.2 Features

- Infrared input signals are transformed into the Run-Length-Code (RLC) format
- Configurable signal width threshold for noise detecting
- 32 Bytes FIFO for received data storage

## 14.8.3 Functional Description

The IR-RX module receives infrared signals and transforms the received information into digital format. The input infrared signals are filtered depending on a configurable noise detecting threshold. The transformed data is written into FIFO as the Run-Length-Code (RLC). Software may read the data from FIFO by checking status or configuring interrupt.

The block diagram of IR-RX is depicted below.

<img src="./static/ir_rx.png" alt="" width="400">

The input clock signal (CLK) is divided by a configurable parameter to generate the internal working clock (WCLK) which is used to measure the duration or transition time of the input infrared signal.

When IR_EN=1, the 7-bit width RLC_COUNT counts under the working clock. The RLC_COUNT is cleared to be 0 either if IR_RX changes or if it counts to 127.

When IR_RX changes or RLC_COUNT counts to 127, 1 byte data is written into FIFO.

If RLC_COUNT > NOISETHR at the data sampling moment, the current IR_RX value and the current RLC_COUNT value are stored, which is {IR_RX, RLC_COUNT[6:0]}.

If RLC_COUNT <= NOISETHR at the data sampling moment, the previously stored IR_RX value and the current RLC_COUNT value are stored, which is {IR_RX_old, RLC_COUNT[6:0]}.

For example, the following data in RLC format implies that:

- 0x98 --> Logic '1' has sustained for 0x18 working clock cycles.
- 0x7F --> Logic '0' has sustained for 0x7F working clock cycles.
- 0x06 --> Logic '0' has sustained for 0x06 working clock cycles.
- 0xFF --> Logic '1' has sustained for 0x7F working clock cycles.

## 14.8.4 Register Description

The base address of two IR-RX registers in the X100™ field are 
- 0xD401_7E00 
- 0xD401_7F00

The base address of two IR-RX registers in the RT_24 field are 
- 0xC088_7000 
- 0xC088_E000

### IRC_EN REGISTER

Offset: 0x0

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:1 | Reserved | RO | 0x0 | Reserved |
| 0 | IRC_EN | RW | 0x0 | This is the global enable bit for the IR-RX.<br>0x0: Disabled<br>0x1: Enabled |

### CLKDIV REGISTER

Offset: 0x4

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:24 | Reserved | RO | 0x0 | Reserved |
| 23:0 | CLKDIV | RW | 0x0 | Frequency dividing parameter for generating the internal working clock (WCLK). The generated WCLK frequency is:<br>Freq_of_WCLK = Freq_of_CLK / (CLKDIV +1) |

### NOISETHR REGISTER

Offset: 0x8

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:8 | Reserved | RO | 0x0 | Reserved |
| 7:0 | NOISETHR | RW | 0x0 | Noise detection threshold. |

### IDLE_STATE REGISTER

Offset: 0xC

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:1 | Reserved | RO | 0x0 | Reserved |
| 0 | IDLE_STATE | RW | 0x1 | This is the IDLE status bit.<br>0x0: Not IDLE<br>0x1: IDLE<br>It is cleared by hardware at the change of input infrared signal. Software could set this bit to 0x1. |

### FIFO_OUT REGISTER

Offset: 0x10

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:8 | Reserved | RO | 0x0 | Reserved |
| 7:0 | FIFO_OUT | RO | 0x0 | This is the data output of FIFO. |

### FIFO_STS REGISTER

Offset: 0x14

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31 | FIFO_full | RO | 0x0 | Flag bit of FIFO full. |
| 30 | FIFO_empty | RO | 0x1 | Flag bit of FIFO empty. |
| 29:6 | Reserved | RO | 0x0 | Reserved |
| 5:0 | FIFO_CNT | RO | 0x0 | This is the number of unread data in FIFO. |

### FIFO_CMP REGISTER

Offset: 0x18

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:6 | Reserved | RO | 0x0 | Reserved |
| 5:0 | FIFO_CMP | RW | 0x0 | Comparison value for the number of unread data in FIFO. It is used to generate interruption. |

### INT_EN REGISTER

Offset: 0x1C

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:4 | Reserved | RO | 0x0 | Reserved |
| 3 | CMP_INT_EN | RW | 0x0 | Interrupt enable bit for comparison between FIFO_CMP and the number of unread data in FIFO. |
| 2 | CNT_INT_EN | RW | 0x0 | Interrupt enable bit for RLC_COUNT counts to 127. |
| 1 | PEDGE_INT_EN | RW | 0x0 | Interrupt enable bit for the positive edge of the input infrared signal. |
| 0 | NEDGE_INT_EN | RW | 0x0 | Interrupt enable bit for the negative edge of the input infrared signal. |

### INT_FLAG REGISTER

Offset: 0x20

| Bits | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 31:4 | Reserved | RO | 0x0 | Reserved |
| 3 | CMP_INT_FLAG | RW1C | 0x0 | This bit is set to 1 if the number of unread data in FIFO equals to FIFO_CMP. Interrupt is generated if CMP_INT_EN=1. It can be cleared by writing 0x1 to this bit. |
| 2 | CNT_INT_FLAG | RW1C | 0x0 | This bit is set to 1 if RLC_COUNT=127. Interrupt is generated if CNT_INT_EN=1. It can be cleared by writing 0x1 to this bit. |
| 1 | PEDGE_INT_FLAG | RW1C | 0x0 | This bit is set to 1 if positive edge of the input infrared signal is detected. Interrupt is generated if PEDGE_INT_EN=1. It can be cleared by writing 0x1 to this bit. |
| 0 | NEDGE_INT_FLAG | RW1C | 0x0 | This bit is set to 1 if negative edge of the input infrared signal is detected. Interrupt is generated if NEDGE_INT_EN=1. It can be cleared by writing 0x1 to this bit. |