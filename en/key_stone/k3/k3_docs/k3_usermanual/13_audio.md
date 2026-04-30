---
sidebar_position: 14
---

# 13. Audio Subsystem

## 13.1 Overview

The K3 SoC integrates a comprehensive audio subsystem designed to deliver high-quality, low-latency audio performance. It incorporates multiple I²S and DisplayPort audio interfaces to support diverse playback and recording scenarios across multimedia and communication applications.

The subsystem includes the following primary interfaces:

- 6 × Full-Duplex I²S Interfaces
- 4 × Half-Duplex I²S Interfaces (two connected to the DP/eDP controller), using dedicated DMA for data transfer
- 2 × DP/eDP Audio Interfaces

## 13.2 Full-Duplex I²S Interfaces

The controller directly supports the following protocols:

- Motorola* Serial Peripheral Interface (SPI)
- Inter-IC Sound (I²S)

### 13.2.1 Features

- Supports full-duplex operation with simultaneous playback and recording
- Supports master mode
- Complies with the standard I²S audio format
- Fixed audio parameters:
  - Sampling rate: 48 kHz
  - Data depth: 16 bits
  - Channels: 2 (stereo)
  - TX/RX FIFO depth: 32 words
- Supports DMA burst transfer
- Configurable system clock (sysclk) modes: 64fs, 128fs, or 256fs

### 13.2.2 Registers

#### 13.2.2.1 Module Base Address

| Module Name | Base Address |
|-------------|--------------|
| I2S0 | 0xD4026000 |
| I2S1 | 0xD4026800 |
| I2S2 | 0xD4027000 |
| I2S3 | 0xD4027800 |
| I2S4 | 0xD4041000 |
| I2S5 | 0xD4041800 |

#### 13.2.2.2 Register Description

Refer to [SPI](./14_connectivity/spi.md) for details.

## 13.3 Half-Duplex I²S Interfaces

### 13.3.1 Features

- Supports playback or recording in half-duplex mode
- Supports master mode
- Complies with standard I²S, left-justified, and right-justified formats
- Audio parameters:
  - Sampling rate: 48 kHz
  - Data depth: 16 bits
  - Channels: 2 (stereo)
  - TX/RX FIFO depth: 64 words
- Supports TDM (Time-Division Multiplexing) mode:
  - DSP_A / DSP_B modes
  - Sampling rate: 48 kHz
  - Data depth: 16-bit / 32-bit
  - TX/RX FIFO depth: 64 words
  - Up to 4 channels
- Supports DMA burst transfer
  - Uses dedicated DMA: ADMA

### 13.3.2 Registers

#### 13.3.2.1 Module Base Address

| Module Name | Base Address |
|-------------|--------------|
| RI2S0 | 0xC0883100 |
| RI2S1 | 0xC0883500 |
| RI2S2 | 0xC0883900 |
| RI2S3 | 0xC0883D00 |

#### 13.3.2.2 Register Description

##### DATA RECEIVE REGISTER

SSPA_RX_DATA

Offset: 0x0

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | AUD_SAM | RO | 0x0 | Audio Sample<br><br>The data format in this register depends on the sample size.<br><br>Independently of the serial data justification, audio samples that have fewer than 32 bits should have their MSB in bit 31.<br><br>This is not a CPU access path. This address is used as the source address for the Audio DMA channel 1 to transfer data from SSPA to Audio SRAM memory. |

##### CHANNEL RECEIVE IDENTIFICATION REGISTER

SSPA_RX_ID

Offset: 0x4

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:7 | RSVD | RO | 0x0 | Reserved for future use. |
| 6:0 | CHAN_ID | RO | 0x0 | Channel identification. |

##### RECEIVE CONTROL REGISTER

SSPA_RX_CTRL

Offset: 0x8

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31 | RPH | RW | 0x0 | Read Phase<br>0x0 = Single-phase frame<br>0x1 = Dual-phase frame |
| 30:24 | RFRLEN2 | RW | 0x0 | Receive Frame Length in Phase 2 (RFRLEN2 + 1)<br><br>This field specifies the receive frame length (number of words) for phase 2.<br>0x0 = 1 word in phase 2<br>0x1 = 2 words in phase 2<br>0x3F = 64 words in phase 2<br>0x40 = Reserved<br>...<br>0x7F = Reserved |
| 23:21 | RWDLEN2 | RW | 0x0 | Receive Word Length in Phase 2<br><br>This field specifies the receive word length (number of bits) for phase 2.<br>0x0 = Receive word length is 8 bits<br>0x1 = Receive word length is 12 bits<br>0x2 = Receive word length is 16 bits<br>0x3 = Receive word length is 20 bits<br>0x4 = Receive word length is 24 bits<br>0x5 = Receive word length is 32 bits<br>0x6 = Reserved<br>0x7 = Reserved |
| 20:19 | RDATDLY | RW | 0x0 | Receive Data Delay Bit<br>0x0 = 0-bit data delay<br>0x1 = 1-bit data delay<br>0x2 = 2-bit data delay<br>0x3 = Reserved |
| 18:16 | RSSZ2 | RW | 0x0 | Receive Sample Audio Size in Phase 2<br>0x0 = Audio sample word length is 8 bits<br>0x1 = Audio sample word length is 12 bits<br>0x2 = Audio sample word length is 16 bits<br>0x3 = Audio sample word length is 20 bits<br>0x4 = Audio sample word length is 24 bits<br>0x5 = Audio sample word length is 32 bits<br>0x6 = Reserved<br>0x7 = Reserved |
| 15 | RFIG | RW | 0x0 | Receive Frame Ignore<br>0x0 = Receive frame-synchronization pulses after the first pulse restarts the transfer<br>0x1 = Receive frame-synchronization pulses after the first pulse are ignored |
| 14:8 | RFRLEN1 | RW | 0x0 | Receive Frame Length in Phase 1 (RFRLEN1 + 1)<br><br>This field specifies the receive frame length (number of words) for phase 1.<br>0x0 = 1 word in phase 1<br>0x1 = 2 words in phase 1<br>0x3F = 64 words in phase 1<br>0x40 = Reserved<br>...<br>0x7F = Reserved |
| 7:5 | RWDLEN1 | RW | 0x0 | Receive Word Length in Phase 1<br><br>This field specifies the receive word length (number of bits) for phase 1.<br>0x0 = Receive word length is 8 bits<br>0x1 = Receive word length is 12 bits<br>0x2 = Receive word length is 16 bits<br>0x3 = Receive word length is 20 bits<br>0x4 = Receive word length is 24 bits<br>0x5 = Receive word length is 32 bits<br>0x6 = Reserved<br>0x7 = Reserved |
| 4 | RSVD | RO | 0x0 | Reserved for future use. |
| 3 | JST | RW | 0x0 | Audio Sample Justification<br>0x0 = Left justified<br>0x1 = Right justified |
| 2:0 | RSSZ1 | RW | 0x0 | Receive Sample Audio Size in Phase 1<br>0x0 = Audio sample word length is 8 bits<br>0x1 = Audio sample word length is 12 bits<br>0x2 = Audio sample word length is 16 bits<br>0x3 = Audio sample word length is 20 bits<br>0x4 = Audio sample word length is 24 bits<br>0x5 = Audio sample word length is 32 bits<br>0x6 = Reserved<br>0x7 = Reserved |

##### SERIAL PORT CONTROL REGISTER

SSPA_RX_SP_CTRL

Offset: 0xC

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31 | WEN | RW | 0 | Write Configuration Enable:<br>0x0 = Disable writes to bits 27-4<br>0x1 = Enable writes to bits 27-4 |
| 30:28 | RSVD | RO | 0 | Reserved for future use. |
| 27:20 | FWD | RW | 0x0 | Frame-Sync Width:<br>Actual Width = (FWD + 1).<br>Specifies the width of the frame-sync signal pulse during its active period.<br>Valid values: 0x0 to 0xFF. |
| 19 | RSVD | RO | 0 | Reserved for future use. |
| 18 | MSL | RW | 0x0 | Master/Slave Configuration:<br>0x0 = External Clock (sclk and fsync provided externally)<br>0x1 = Internal Clock (sclk and fsync generated by IP core) |
| 17 | CLKP | RW | 0x0 | CLKP Polarity / Clock Edge Select:<br>0x0 = sdata sampled at rising edge of sclk<br>0x1 = sdata sampled at falling edge of sclk |
| 16 | FSP | RW | 0x0 | FSP Polarity / Frame-Sync Edge Select:<br>0x0 = Active high fsync<br>0x1 = Active low fsync |
| 15:4 | FPER | RW | 0x0 | Frame-Sync Period:<br>Actual Period = (FPER + 1).<br>Specifies when the next frame-sync signal becomes active.<br>Valid values: 0x0 to 0xFFF. |
| 3 | RSVD | RO | 0 | Reserved for future use |
| 2 | FFLUSH | RW | 0x0 | FIFO Flush:<br>0x0 = Do nothing<br>0x1 = Writing 1 flushes the FIFO |
| 1 | S_RST | RW | 0x0 | Serial Domain Reset (Active High):<br>0x0 = Do nothing<br>0x1 = Writing 1 resets registers in the serial clock domain |
| 0 | S_EN | RW | 0x0 | Serial Clock Domain Enable:<br>0x0 = Disable reception of audio streaming<br>0x1 = Enable reception of audio stream per current configuration |

##### FIFO UPPER LIMIT REGISTER

SSPA_RX_FIFO_UL

Offset: 0x10

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:15 | RSVD | RO | 0x0 | Reserved for future use. |
| 14:0 | UPPER_LIMIT | RW | 0x7FFF | FIFO Upper Limit<br>Sets the FIFO upper limit. When the number of samples in the FIFO exceeds this limit, a request is sent to DMA. |

##### INTERRUPT MASK REGISTER

SSPA_RX_INT_MSK

Offset: 0x14

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:17 | RSVD | RO | 0x0 | Reserved for future use. |
| 16 | FFI | RW | 0x0 | FIFO Interrupt<br>0x0 = Nothing to signal<br>0x1 = The number of samples in the FIFO is greater than the configured upper FIFO limit |
| 15:1 | RSVD | RO | 0x0 | Reserved for future use. |
| 0 | FFM | RW | 0x0 | FIFO Interrupt Mask<br>0x0 = FFI is ignored<br>0x1 = FFI drives IRQ |

##### DATA TRANSMIT REGISTER

SSPA_TX_DATA

Offset: 0x80

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | AUD_SAM | RO | 0x0 | Audio Sample<br><br>The data format in this register depends on the sample size.<br><br>Independently of the serial data justification, audio samples that have fewer than 32 bits should have their MSB in bit 31.<br><br>This is not a CPU access path. This address is used as the destination address for the Audio DMA channel 0 to transfer data from Audio SRAM memory to SSPA. |

##### CHANNEL TRANSMIT IDENTIFICATION REGISTER

SSPA_TX_ID

Offset: 0x84

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:7 | RSVD | RO | 0x0 | Reserved for future use. |
| 6:0 | CHAN_ID | RO | 0x0 | Channel identification. |

##### TRANSMIT CONTROL REGISTER

SSPA_TX_CTRL

Offset: 0x88

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31 | XPH | RW | 0x0 | Read Phase<br>0x0 = Single-phase frame<br>0x1 = Dual-phase frame |
| 30:24 | XFRLEN2 | RW | 0x0 | Transmit Frame Length in Phase 2 (XFRLEN2 + 1)<br>Specifies the transmit frame length (number of words) for phase 2.<br>0x0 = 1 word in phase 2<br>0x1 = 2 words in phase 2<br>0x3F = 64 words in phase 2<br>0x40 - 0x7F = Reserved |
| 23:21 | XWDLEN2 | RW | 0x0 | Transmit Word Length in Phase 2<br>This field specifies the transmit word length (number of bits) for phase 2.<br>0x0 = 8 bits<br>0x1 = 12 bits<br>0x2 = 16 bits<br>0x3 = 20 bits<br>0x4 = 24 bits<br>0x5 = 32 bits<br>0x6 - 0x7 = Reserved |
| 20:19 | XDATDLY | RW | 0x0 | Transmit Data Delay<br>0x0 = 0-bit data delay<br>0x1 = 1-bit data delay<br>0x2 = 2-bit data delay<br>0x3 = Reserved |
| 18:16 | XSSZ2 | RW | 0x0 | Transmit Sample Audio Size in Phase 2<br>0x0 = 8 bits<br>0x1 = 12 bits<br>0x2 = 16 bits<br>0x3 = 20 bits<br>0x4 = 24 bits<br>0x5 = 32 bits |
| 15 | XFIG | RW | 0x0 | Transmit Zeros When FIFO Empty<br>0x0 = Transmit zeros when the FIFO is empty<br>0x1 = Repeat the last sample/sample-pair present in the FIFO |
| 14:8 | XFRLEN1 | RW | 0x0 | Transmit Frame Length in Phase 1 (XFRLEN1 + 1)<br>Specifies the transmit frame length (number of words) for phase 1.<br>0x0 = 1 word in phase 1<br>0x1 = 2 words in phase 1<br>0x3F = 64 words in phase 1<br>0x40 - 0x7F = Reserved |
| 7:5 | XWDLEN1 | RW | 0x0 | Transmit Word Length in Phase 1<br>This field specifies the transmit word length (number of bits) for phase 1.<br>0x0 = 8 bits<br>0x1 = 12 bits<br>0x2 = 16 bits<br>0x3 = 20 bits<br>0x4 = 24 bits<br>0x5 = 32 bits<br>0x6 - 0x7 = Reserved |
| 4 | RSVD | RO | 0x0 | Reserved for future use |
| 3 | JST | RW | 0x0 | Audio Sample Justification<br>0x0 = Left justified<br>0x1 = Right justified |
| 2:0 | XSSZ1 | RW | 0x0 | Transmit Sample Audio Size in Phase 1<br>0x0 = 8 bits<br>0x1 = 12 bits<br>0x2 = 16 bits<br>0x3 = 20 bits<br>0x4 = 24 bits<br>0x5 = 32 bits<br>0x6 - 0x7 = Reserved |

##### SERIAL PORT CONTROL REGISTER

SSPA_TX_SP_CTRL

Offset: 0x8C

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31 | WEN | RW | 0x0 | Write Configuration Enable<br>0x0 = Disable writes to bits 27-4<br>0x1 = Enable writes to bits 27-4 |
| 30:28 | RSVD | RO | 0x0 | Reserved for future use |
| 27:20 | FWD | RW | 0x0 | Frame-Sync Width (FWID+1)<br>This field specifies the width of the frame-sync signal pulse during its active period.<br>Valid values are 0x0 to 0xFF. |
| 19 | RSVD | RO | 0x0 | Reserved for future use |
| 18 | MSL | RW | 0x0 | Master/Slave Configuration<br>0x0 = External clock (sclk and fsync must be provided externally)<br>0x1 = Internal clock (sclk and fsync are generated by the IP core) |
| 17 | CLKP | RW | 0x0 | CLKP Polarity / Clock Edge Select<br>0x0 = sdata must be sampled at the rising edge of sclk<br>0x1 = sdata must be sampled at the falling edge of sclk |
| 16 | FSP | RW | 0x0 | FSP Polarity / Clock Edge Select<br>0x0 = Active high fsync<br>0x1 = Active low fsync |
| 15:4 | FPER | RW | 0x0 | Frame-Sync Active (FPER+1)<br>This field specifies when the next frame-sync signal becomes active.<br>Valid values are 0x0 to 0xFFF. |
| 3 | RSVD | RO | 0x0 | Reserved for future use |
| 2 | FFLUSH | RW | 0x0 | FIFO Flush<br>0x0 = Do nothing<br>0x1 = Writing 1 to this bit flushes the FIFO |
| 1 | S_RST | RW | 0x0 | Active High Reset Signal<br>0x0 = Do nothing<br>0x1 = Writing 1 to this bit resets the registers in the serial clock domain |
| 0 | S_EN | RW | 0x0 | Serial Clock Domain Enable<br>0x0 = Disable reception of any audio streaming<br>0x1 = Enable reception of an audio stream according to the current configuration |

##### FIFO LOW LIMIT REGISTER

SSPA_TX_FIFO_UL

Offset: 0x90

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:15 | RSVD | RO | 0x0 | Reserved for future use |
| 14:0 | LOW_LIMIT | RW | 0x7FFF | FIFO Lower Limit<br>Sets the FIFO lower limit.<br> When the number of samples in the FIFO goes below this limit, a request is sent to DMA. |

##### INTERRUPT MASK REGISTER

SSPA_TX_INT_MSK

Offset: 0x94

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:17 | RSVD | RO | 0x0 | Reserved for future use |
| 16 | FFI | RW | 0x0 | FIFO Interrupt<br>0x0 = Nothing to signal<br>0x1 = The number of samples in the FIFO is greater than the configured upper FIFO limit |
| 15:1 | RSVD | RO | 0x0 | Reserved for future use |
| 0 | FFM | RW | 0x0 | FIFO Interrupt Mask<br>0x0 = FFI is ignored<br>0x1 = FFI drives IRQ |

## 13.4 DP/eDP Audio Interfaces

- Supports audio playback over DisplayPort or Embedded DisplayPort links
- Supports slave mode
- Complies with standard I²S, left-justified, and right-justified formats
- Audio parameters:
  - Sampling rate: up to 192 kHz
  - Data depth: 16-bit / 20-bit / 24-bit
  - Channels: 2 (stereo)
- Limitation: BCLK requires 64fs, and SYSCLK requires 512fs

## 13.5 ADMA

### 13.5.1 Features
- Four instances of the ADMA controller, each for an RI2S, handle audio data transfers
- Supports two DMA channels: channel 0 for RI2S TX and channel 1 for RI2S RX
- Supports programmable data-burst sizes (1, 2, 4, 8, 16, or 32 bytes) and configurable peripheral device data widths (8, 12, 16, 20, 24, or 32 bits)
- Supports up to 65535 bytes of data transfer per descriptor; larger transfers can be performed by chaining multiple descriptors

### 13.5.2 Registers

#### 13.5.2.1 Module Base Address

| Module Name | Base Address |
|-------------|--------------|
| ADMA0 | 0xC0883000 |
| ADMA1 | 0xC0883400 |
| ADMA2 | 0xC0883800 |
| ADMA3 | 0xC0883C00 |

#### 13.5.2.2 Register Description

**Byte Count**
This register is programmed with a 16-bit value that contains the number of data bytes that this channel must transfer. The maximum number of bytes that the DMA channel can be configured to transfer is 64 KB.

This register will decrement at the end of every data transfer when data is transferred from source to destination. When the byte count reaches 0, the DMA transaction is finished.

##### CHANNEL 0 BYTE COUNT REGISTER
ADMA_CHAN_0_BYTE_CNT
Offset:0x0

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:16 | Reserved | RO | 0x0 | Reserved for future use |
| 15:0 | BYTECNT0 | RW | 0x0 | Channel 0 Byte Count<br>Number of data bytes that this DMA channel must transfer. |

##### CHANNEL 1 BYTE COUNT REGISTER
ADMA_CHAN_1_BYTE_CNT
Offset:0x4

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:16 | Reserved | RO | 0x0 | Reserved for future use |
| 15:0 | BYTECNT1 | RW | 0x0 | Channel 1 Byte Count<br>Number of data bytes that this DMA channel must transfer. |

##### CHANNEL 0 SOURCE ADDRESS REGISTER
ADMA_CHAN_0_SRC_ADDR
Offset:0x10

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | SRCADD0 | RW | 0x0 | Channel 0 Source Address |

##### CHANNEL 1 SOURCE ADDRESS REGISTER
ADMA_CHAN_1_SRC_ADDR
Offset:0x14

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | SRCADD1 | RW | 0x0 | Channel 1 Source Address |

##### CHANNEL 0 DESTINATION ADDRESS REGISTER
ADMA_CHAN_0_DEST_ADDR
Offset:0x20

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | DESTADD0 | RW | 0x0 | Channel 0 Destination Address |

##### CHANNEL 1 DESTINATION ADDRESS REGISTER
ADMA_CHAN_1_DEST_ADDR
Offset:0x24

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | DESTADD1 | RW | 0x0 | Channel 1 Destination Address |

##### CHANNEL 0 NEXT DESCRIPTOR POINTER REGISTER
ADMA_CHAN_0_NEXT_DESC_PTR
Offset:0x30

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | NDPTR0 | RW | 0x0 | Channel 0 Next Descriptor Pointer Address<br>This must be 16-byte aligned. |

##### CHANNEL 1 NEXT DESCRIPTOR POINTER REGISTER
ADMA_CHAN_1_NEXT_DESC_PTR
Offset:0x34

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | NDPTR1 | RW | 0x0 | Channel 1 Next Descriptor Pointer Address<br>This must be 16-byte aligned. |

##### CHANNEL 0 CONTROL REGISTER
ADMA_CHAN_0_CTRL
Offset:0x40

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:25 | RSVD | RO | 0x0 | Reserved for future use |
| 24:22 | XSSZ | RW | 0x0 | Transmit Audio Sample Size (Word Length)<br>0x0 = Audio sample word length is 8 bits<br>0x1 = Audio sample word length is 12 bits<br>0x2 = Audio sample word length is 16 bits<br>0x3 = Audio sample word length is 20 bits<br>0x4 = Audio sample word length is 24 bits<br>0x5 = Audio sample word length is 32 bits<br>0x6 = Reserved<br>0x7 = Reserved |
| 21 | SSPMOD | RW | 0x0 | SSPMod<br>0 = Non-SSP FIFO access<br>1 = SSP FIFO access |
| 20 | ABR | RW | 0x0 | Channel Abort<br>When software sets this bit to 1, the DMA aborts the transfer. This field is cleared by the DMA hardware. |
| 19:18 | RSVD | RO | 0x0 | Reserved for future use |
| 17 | CDE | RW | 0x0 | Close Descriptor Enable<br>If enabled, the DMA writes the remainder byte count into bits[31:16] of the byte count field.<br>0 = Disable<br>1 = Enable |
| 16 | RSVD | RO | 0x0 | Reserved for future use |
| 15 | SDA | RW | 0x0 | Source/Destination Address Alignment<br>0 = Alignment is towards the source. After the DMA's first read, all reads will be to 32-bit word aligned address.<br>1 = Alignment is towards the destination. After the first write, the following writes will be with all Byte Enables asserted. |
| 14 | CHANACT | RO | 0x0 | DMA Channel Active<br>0 = Channel is not active<br>1 = Channel is active |
| 13 | FETCHND | RW | 0x0 | Fetch Next Descriptor<br>0 = Does not force a fetch of the next descriptor<br>1 = Forces a fetch of the next descriptor<br>This field is automatically cleared after the fetch completes. |
| 12 | CHANEN | RW | 0x0 | Channel Enable<br>0 = Disable<br>1 = Enable<br>When software sets this field to 1, it activates the channel. This bit is automatically cleared after the DMA transfer is done.<br>Setting it to 0 causes the channel to suspend.<br>Re-setting this field to 1 allows the channel to continue the DMA transfer.<br>CHIP recommends setting this field at the same time as the other control bits in this register, or after the other control bits in this register have been set. |
| 11 | TRANSMOD | RW | 0x0 | TransMod<br>0 = External DMA_REQ access mode |
| 10 | INTMODE | RW | 0x0 | Interrupt Mode<br>0 = Interrupt asserted every time the DMA byte count reaches 0<br>1 = Interrupt asserted when the Next Descriptor Pointer value is NULL and the DMA byte count reaches 0 |
| 9 | CHAINMOD | RW | 0x0 | Chain Mode<br>0 = Chain mode<br>1 = Non-Chain mode |
| 8:6 | BURSTLIMIT | RW | 0x0 | Burst Limit in each DMA Access<br>0x5 = 1 byte<br>0x6 = 2 bytes<br>0x0 = 4 bytes<br>0x1 = 8 bytes<br>0x3 = 16 bytes<br>0x7 = 32 bytes |
| 5:4 | DESTDIR | RW | 0x0 | Destination Direction<br>0x0 = Increment destination address<br>0x1 = Decrement destination address<br>0x2 = Hold the same value<br>0x3 = Reserved |
| 3:2 | SRCDIR | RW | 0x0 | Source Direction<br>0x0 = Increment source address<br>0x1 = Decrement source address<br>0x2 = Hold the same value<br>0x3 = Reserved |
| 1:0 | RSVD | RO | 0x0 | Reserved for future use |

##### CHANNEL 1 CONTROL REGISTER
ADMA_CHAN_1_CTRL
Offset:0x44

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:25 | RSVD | RO | 0x0 | Reserved for future use |
| 24:22 | RSSZ | RW | 0x0 | Receive Audio Sample Size (Word Length)<br>0x0 = Audio sample word length is 8 bits<br>0x1 = Audio sample word length is 12 bits<br>0x2 = Audio sample word length is 16 bits<br>0x3 = Audio sample word length is 20 bits<br>0x4 = Audio sample word length is 24 bits<br>0x5 = Audio sample word length is 32 bits<br>0x6 = Reserved<br>0x7 = Reserved |
| 21 | SSPMOD | RW | 0x0 | SSPMod<br>0 = Non-SSP FIFO access<br>1 = SSP FIFO access |
| 20 | ABR | RW | 0x0 | Channel Abort<br>When software sets this bit to 1, the DMA aborts the transfer. This field is cleared by the DMA hardware. |
| 19:18 | RSVD | RO | 0x0 | Reserved for future use |
| 17 | CDE | RW | 0x0 | Close Descriptor Enable<br>If enabled, the DMA writes the remainder byte count into bits[31:16] of the byte count field.<br>0 = Disable<br>1 = Enable |
| 16:15 | RSVD | RO | 0x0 | Reserved for future use |
| 14 | CHANACT | RO | 0x0 | DMA Channel Active<br>0 = Channel is not active<br>1 = Channel is active |
| 13 | FETCHND | RW | 0x0 | Fetch Next Descriptor<br>0 = Does not force a fetch of the next descriptor<br>1 = Forces a fetch of the next descriptor<br>This field is automatically cleared after the fetch completes. |
| 12 | CHANEN | RW | 0x0 | Channel Enable<br>0 = Disable<br>1 = Enable<br>When software sets this field to 1, it activates the channel. This bit is automatically cleared after the DMA transfer is done.<br>Setting it to 0 causes the channel to suspend.<br>Re-setting this field to 1 allows the channel to continue the DMA transfer.<br>CHIP recommends setting this field at the same time as the other control bits in this register, or after the other control bits in this register have been set. |
| 11 | TRANSMOD | RW | 0x0 | TransMod<br>0 = External DMA_REQ access mode |
| 10 | INTMODE | RW | 0x0 | Interrupt Mode<br>0 = Interrupt asserted every time the DMA byte count reaches 0<br>1 = Interrupt asserted when the Next Descriptor Pointer value is NULL and the DMA byte count reaches 0 |
| 9 | CHAINMOD | RW | 0x0 | Chain Mode<br>0 = Chain mode<br>1 = Non-Chain mode |
| 8:6 | BURSTLIMIT | RW | 0x0 | Burst Limit in each DMA Access<br>0x5 = 1 byte<br>0x6 = 2 bytes<br>0x0 = 4 bytes<br>0x1 = 8 bytes<br>0x3 = 16 bytes<br>0x7 = 32 bytes |
| 5:4 | DESTDIR | RW | 0x0 | Destination Direction<br>0x0 = Increment destination address<br>0x1 = Decrement destination address<br>0x2 = Hold the same value<br>0x3 = Reserved |
| 3:2 | SRCDIR | RW | 0x0 | Source Direction<br>0x0 = Increment source address<br>0x1 = Decrement source address<br>0x2 = Hold the same value<br>0x3 = Reserved |
| 1:0 | RSVD | RO | 0x0 | Reserved for future use |

##### CHANNEL PRIORITY REGISTER
ADMA_CHAN_PRI
Offset:0x60

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31 | REVERSE_MEMORY_COPY | RW | 0x0 | Reverse Memory Copy<br>0x1 = When &lt;SRCDIR&gt;/&lt;DESTDIR&gt; is 2'b01 and the current remaining size in the channel is less than or equal to the burst limit in each DMA access, the current DMA source/destination address = (channel source/destination address - current remaining size) |
| 30:2 | RSVD | RO | 0x0 | Reserved for future use |
| 1:0 | PRIOCHAN10 | RW | 0x0 | Channels 0 and 1 Priority<br>0x0 = Round Robin<br>0x1 = Priority to channel 1 over channel 0<br>0x2 = Priority to channel 0 over channel 1<br>0x3 = Reserved |


##### CHANNEL ID FILTER REGISTER
CHANNEL_ID_FILTER
Offset:0x64

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:8 | RSVD | RO | 0x00 | Reserved for future use |
| 7:0 | EN_ACCESS | RW | 0x0D | Enable Access |

##### CHANNEL 0 CURRENT DESCRIPTOR POINTER REGISTER
CHAN_0_CURR_DESC_PTR
Offset:0x70

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | CDPTR0 | RW | 0x0 | Channel 0 Current Descriptor Pointer Address |

##### CHANNEL 1 CURRENT DESCRIPTOR POINTER REGISTER
CHAN_1_CURR_DESC_PTR
Offset:0x74

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:0 | CDPTR1 | RW | 0x0 | Channel 1 Current Descriptor Pointer Address |

##### CHANNEL 0 INTERRUPT MASK REGISTER
ADMA_CHAN_0_INT_MASK
Offset:0x80

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:2 | RSVD | RO | 0x0 | Reserved for future use |
| 1 | DMA_ABORT_INT | RW | 0x0 | Channel 0 DMA Aborted Interrupt Mask<br>1 = Channel 0 DMA Aborted interrupt is enabled<br>0 = Channel 0 DMA Aborted interrupt is disabled |
| 0 | COMP | RW | 0x0 | Channel 0 Completion Interrupt Mask<br>1 = Channel 0 Completion interrupt is enabled<br>0 = Channel 0 Completion interrupt is disabled |

##### CHANNEL 1 INTERRUPT MASK REGISTER
ADMA_CHAN_1_INT_MASK
Offset:0x84

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:2 | RSVD | RO | 0x0 | Reserved for future use |
| 1 | DMA_ABORT_INT | RW | 0x0 | Channel 0 DMA Aborted Interrupt Mask<br>1 = Channel 1 DMA aborted interrupt is enabled<br>0 = Channel 1 DMA aborted interrupt is disabled |
| 0 | COMP | RW | 0x0 | Channel 1 Completion Interrupt Mask<br>1 = Channel 1 completion interrupt is enabled<br>0 = Channel 1 completion interrupt is disabled |

##### CHANNEL 0 RESET SELECT REGISTER
CHAN_0_RSR
Offset:0x90

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:2 | RSVD | RO | 0x0 | Reserved for future use |
| 1:0 | RSR0 | RW | 0x0 | Channel 0 Reset Select Address<br>The bits in this register correspond to the bits in the CHAN_0_INT_STATUS register.<br> Setting a bit to 1 enables the read-clear function of the corresponding CHAN_0_INT_STATUS bit.<br>0 = Disable<br>1 = Enable |

##### CHANNEL 1 RESET SELECT REGISTER
ADMA_CHAN_1_RSR
Offset:0x94

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:2 | RSVD | RO | 0x0 | Reserved for future use |
| 1:0 | RSR1 | RW | 0x0 | Channel 1 Reset Select Address<br>The bits in this register correspond to the bits in the CHAN_1_INT_STATUS register.<br> Setting a bit to 1 enables the read-clear function of the corresponding CHAN_1_INT_STATUS bit.<br>0 = Disable<br>1 = Enable |

##### CHANNEL 0 INTERRUPT STATUS REGISTER
ADMA_CHAN_0_INT_STATUS
Offset:0xA0

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:2 | RSVD | RO | 0x0 | Reserved for future use |
| 1 | DMA_ABORT | RW | 0x0 | DMA Abort Interrupt Status and Clear (Channel 0)<br>Read-clear functionality for this field is enabled via the corresponding RSR bit in the CHAN_0_RSR register. |
| 0 | INT_DONE | RW | 0x0 | Interrupt Done Status and Clear (Channel 0)<br>Read-clear functionality for this field is enabled via the corresponding RSR bit in the CHAN_0_RSR register. |

##### CHANNEL 1 INTERRUPT STATUS REGISTER
ADMA_CHAN_1_INT_STATUS
Offset:0xA4

| Bits | Field | Type | Reset | Description |
|------|-------|------|-------|-------------|
| 31:2 | RSVD | RO | 0x0 | Reserved for future use |
| 1 | DMA_ABORT | RW | 0x0 | DMA Abort Interrupt Status and Clear (Channel 1)<br>Read-clear functionality for this field is enabled via the corresponding RSR bit in the CHAN_1_RSR register. |
| 0 | INT_DONE | RW | 0x0 | Interrupt Done Status and Clear (Channel 1)<br>Read-clear functionality for this field is enabled via the corresponding RSR bit in the CHAN_1_RSR register. |

