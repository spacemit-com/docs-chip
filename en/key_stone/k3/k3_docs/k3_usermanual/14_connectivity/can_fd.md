---
sidebar_position: 4
---

# 14.4 CAN-FD Interface

## 14.4.1 Overview

The FlexCAN Controller is a full implementation of the CAN protocol specification, the CAN with Flexible Data rate (CAN FD) protocol, and the CAN 2.0 Part B protocol.

## 14.4.2 Features

- Full implementation of the CAN FD protocol and CAN Specification 2.0, Part B
  - Standard data frames
  - Extended data frames
  - Zero to sixty-four bytes data length
  - Programmable bit rate
  - Content-related addressing
- Compliant with the ISO 11898-1 standard
- Silicon-proven implementation passing ISO 16845-1:2016 CAN conformance tests
- Flexible mailboxes configurable to store 0 to 8, 16, 32, or 64 bytes data length
- Each mailbox configurable as receive or transmit, all supporting standard and       extended messages
- Individual Rx Mask registers per mailbox
- Full-featured Rx FIFO with storage capacity for up to six frames and automatic
- internal pointer handling with MA support
- Transmission abort capability
- Flexible message buffers, totaling 128 message buffers of 8 bytes data length each,configurable as Rx or Tx
- Programmable clock source to the CAN Protocol Engine, either peripheral clock or oscillator clock
- RAM not used by reception or transmission structures can be used as general
- purpose RAM space
- Listen-Only mode capability
- Programmable Loop-Back mode supporting self-test operation
- Programmable transmission priority scheme: lowest ID, lowest buffer number, or
- highest priority
- Time stamp based on 16-bit free-running timer, with an optional external time tick
- Global network time, synchronized by a specific message
- Maskable interrupts
- Independence from the transmission medium (an external transceiver is assumed)
- Short latency time due to an arbitration scheme for high-priority messages
- Low-power modes, with programmable wakeup on bus activity or matching with
- received frames (Pretended Networking)
- Transceiver Delay Compensation feature when transmitting CAN FD messages at faster data rates
- Remote request frames may be managed automatically or by software
- CAN bit time settings and configuration bits can only be written in Freeze mode
- Tx mailbox status (lowest priority buffer or empty buffer)
- Identifier Acceptance Filter Hit Indicator (IDHIT) register for received frames
- SYNCH bit available in Error in Status 1 register to indicate that the FlexCAN is synchronous with CAN bus
- CRC status for transmitted message
- Rx FIFO Global Mask register
- Selectable priority between mailboxes and Rx FIFO during matching process
- Powerful Rx FIFO ID filtering, capable of matching incoming IDs against either 128 extended, 256 standard, or 512 partial (8 bit) IDs, with up to 32 ID Filter Table elements
- 100% backward compatibility with previous FlexCAN version
- Supports detection and correction of errors in memory read accesses. Each byte of FlexCAN memory is associated to 5 parity bits. The error correction mechanism ensures that in this 13-bit word, errors in one bit can be corrected (correctable errors) and errors in 2 bits can be detected but not corrected (non-correctable errors).
- Supports Pretended Networking functionality in low-power modes: Doze mode, Stop mode

## 14.4.3 Signal Descriptions

### 14.4.3.1 FlexCAN Controller Signal Descriptions

| Signal | Type | Description |
| --- | --- | --- |
| CAN-TX | Output | CAN Bus Transmit Data |
| CAN-RX | Input | CAN Bus Receive Data |

### 14.4.3.2 Mode of Operation

The FlexCAN module supports the following functional modes:

- Normal Mode (User or Supervisor)
  
  In Normal mode, the FlexCAN operates 
  - Receiving and/or transmitting message frames
  - Errors are managed normally
  - All CAN protocol functions are enabled

  User and Supervisor modes differ in the access to some restricted control registers.

- Loop-Back Mode
  The FlexCAN enters Loop-Back mode when CAN CTRL1 LPB is asserted.
  
  - In Loop-Back mode, the FlexCAN performs an internal loop back that can be used for self-test operation. The bit stream output of the transmitter is internally fed back to the receiver input. The Rx CAN input pin is ignored and the Tx CAN output goes to the recessive state (logic '1').
  
  - The FlexCAN behaves as it normally does when transmitting and treats its own transmitted message as a message received from a remote node.

  - In Loop-Back mode, the FlexCAN ignores the bit sent during the ACK slot in the CAN frame acknowledge field to ensure proper reception of its own message. Both transmit and receive interrupts are generated.

- CAN FD Active mode:
  
  - In CAN FD Active mode, the FlexCAN is capable of transmitting and receiving all messages formatted according to the CAN FD Protocol and CAN 2.0 Protocol in an interleaved fashion.
  
  - The CPU or MCU can set the FlexCAN into CAN FD Active mode by setting the MCR FDEN when the FlexCAN is in Freeze Mode.