---
sidebar_position: 6
---

# 16.6 Mailbox

## 16.6.1 Overview

The Mailbox module provides an inter-OS communication mechanism on the chip.
The module is implemented with multi-channel FIFOs and interrupts. The sender writes data into the FIFO of a mailbox channel, and an interrupt notifies the receiver to read the data. Each channel has an independent FIFO and configurable threshold, and the transfer direction of each channel can be configured flexibly.

## 16.6.2 Features

The Mailbox module provides the following features:
- 16 channels for mailbox_ns and 8 channels for mailbox_s, with each channel providing an 8 × 32-bit FIFO
- Each channel supports empty and not-full interrupt events
- Independent empty and not-full interrupt thresholds for each channel
- Configurable transfer direction for each channel

## 16.6.3 Functional Description

The Mailbox module enables point-to-point communication between different operating systems running on the chip. The design is parameterizable and supports up to 16 mailbox instances and 8 users.
In the current chip configuration, two users are supported, corresponding to the Secure and Non-secure domains, with 16 mailbox channels for the Non-secure domain and 8 mailbox channels for the Secure domain.
Each mailbox channel provides a FIFO with a depth of 8 × 32-bit words. The mapping between mailbox channels and users is defined by software.
Using the default configuration as an example:
- Channel 0 and Channel 1 are used for messages from User0 to User1.
- Channel 2 and Channel 3 are conventionally used for messages from User1 to User0.

There are no hardware restrictions on channel assignment. If message traffic is asymmetric between users, software can allocate mailbox channels accordingly.

<img src="/k3_docs/static/mailbox.png" alt="" width="500">

## 16.6.4 Registers

| Register Name | Type | Register Width (Bits) | Address Offset |
| :--- | :--- | :--- | :--- |
| MAILBOX_REVISION | R | 32 | 0x000 |
| MAILBOX_SYSCONFIG | R/W1C | 32 | 0x010 |
| MAILBOX_MESSAGE_m | R/W | 32 | 0x040 + (0x4 * m) |
| MAILBOX_FIFOSTATUS_m | R/W1C | 32 | 0x080 + (0x4 * m) |
| MAILBOX_MSGSTATUS_m | R/W1C | 32 | 0x0C0 + (0x4 * m) |
| MAILBOX_IRQSTATUS_RAW_u | R/W1S | 32 | 0x100 + (0x10 * u) |
| MAILBOX_IRQSTATUS_CLR_u | R/W1C | 32 | 0x104 + (0x10 * u) |
| MAILBOX_IRQENABLE_SET_u | R/W1S | 32 | 0x108 + (0x10 * u) |
| MAILBOX_IRQENABLE_CLR_u | R/W1C | 32 | 0x10C + (0x10 * u) |
| MAILBOX_IRQTHR0_u | R/W | 32 | 0x180 + (0x10 * u) |
| MAILBOX_IRQTHR1_u | R/W | 32 | 0x184 + (0x10 * u) |
| MAILBOX_IRQTHR2_u | R/W | 32 | 0x188 + (0x10 * u) |
| MAILBOX_IRQTHR3_u | R/W | 32 | 0x18C + (0x10 * u) |

### 16.6.4.1 Register Description

#### MAILBOX_REVISION

Offset: 0x0000

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | REVISION | R | 0xAAAA_5555 | Mailbox version, used to verify that the bus is connected correctly |

#### MAILBOX_SYSCONFIG

Each bit represents one mailbox instance. Writing `1` to the corresponding bit clears the FIFO of that mailbox instance.

Offset: 0x0010

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0x0 | Reserved for future use. |
| 15 | FIFO_CLR_15 | R/W1C | 0x0 | Mailbox 15 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 14 | FIFO_CLR_14 | R/W1C | 0x0 | Mailbox 14 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 13 | FIFO_CLR_13 | R/W1C | 0x0 | Mailbox 13 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 12 | FIFO_CLR_12 | R/W1C | 0x0 | Mailbox 12 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 11 | FIFO_CLR_11 | R/W1C | 0x0 | Mailbox 11 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 10 | FIFO_CLR_10 | R/W1C | 0x0 | Mailbox 10 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 9 | FIFO_CLR_9 | R/W1C | 0x0 | Mailbox 9 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 8 | FIFO_CLR_8 | R/W1C | 0x0 | Mailbox 8 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 7 | FIFO_CLR_7 | R/W1C | 0x0 | Mailbox 7 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 6 | FIFO_CLR_6 | R/W1C | 0x0 | Mailbox 6 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 5 | FIFO_CLEAR_5 | R/W1C | 0x0 | Mailbox 5 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 4 | FIFO_CLEAR_4 | R/W1C | 0x0 | Mailbox 4 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 3 | FIFO_CLEAR_3 | R/W1C | 0x0 | Mailbox 3 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 2 | FIFO_CLEAR_2 | R/W1C | 0x0 | Mailbox 2 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 1 | FIFO_CLEAR_1 | R/W1C | 0x0 | Mailbox 1 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |
| 0 | FIFO_CLEAR_0 | R/W1C | 0x0 | Mailbox 0 FIFO clear<br>Read 0: FIFO clear is complete<br>Write 0: No action<br>Read 1: FIFO clear is not complete<br>Write 1: Perform FIFO clear |

#### MAILBOX_MESSAGE_m

Offset: 0x0040 + (0x4 * m)

This register stores messages and operates on the FIFO. `m` ranges from `0` to `15`. Before accessing this register, software must confirm the FIFO status through `MAILBOX_FIFOSTATUS_m` or `MAILBOX_MSGSTATUS_m`.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | MESSAGE | R/W | 0x0 | Message data in mailbox `m` |

#### MAILBOX_FIFOSTATUS_m

Offset: 0x0080 + (0x4 * m)

This register provides FIFO status flags. Bit `[28]` records a previous write-full event, and bit `[29]` records a previous read-empty event. These flags are cleared by writing `1`.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:30 | RSVD | R | 0x0 | Reserved |
| 29 | RD_EMPTY_FLAG | R/W1C | 0x0 | Mailbox `m` read-empty flag<br>This bit is set when mailbox `m` is read while empty |
| 28 | WR_FULL_FLAG | R/W1C | 0x0 | Mailbox `m` write-full flag<br>This bit is set when mailbox `m` is written while full |
| 27:2 | RSVD | R | 0x0 | Reserved |
| 1 | EMPTY_STATUS | R | 0x1 | Mailbox `m` empty status<br>`1`: Empty<br>`0`: Not empty |
| 0 | FULL_STATUS | R | 0x0 | Mailbox `m` full status<br>`1`: Full<br>`0`: Not full |

#### MAILBOX_MSGSTATUS_m

Offset: 0x00C0 + (0x4 * m)

This register records the number of data words currently stored in the FIFO. Bits `[29:28]` have the same function as in `MAILBOX_FIFOSTATUS_m` and are set and cleared in the same manner.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:30 | RSVD | R | 0x0 | Reserved |
| 29 | RD_EMPTY_FLAG | R/W1C | 0x0 | Mailbox `m` read-empty flag<br>This bit is set when mailbox `m` is read while empty |
| 28 | WR_FULL_FLAG | R/W1C | 0x0 | Mailbox `m` write-full flag<br>This bit is set when mailbox `m` is written while full |
| 27:4 | RSVD | R | 0x0 | Reserved |
| 3:0 | MSG_COUNT | R | 0x0 | Number of messages in mailbox `m` (`0` to `8`) |

#### MAILBOX_IRQSTATUS_RAW_u

Offset: 0x0100 + (0x10 * u)

Interrupt status register, including Not Full interrupt status and New Message interrupt status.
The Not Full interrupt indicates that the FIFO is not full; that is, under the current configuration, the number of data words in the FIFO is less than 8.
The New Message interrupt indicates that the FIFO is not empty; that is, the number of data words in the FIFO is between 1 and 7.
This register cannot be cleared by software. It can be set manually to `1` for debugging purposes.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31 | NOT_FULL_15 | R/W1S | 0x0 | Not full status of mailbox 15<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 30 | NEW_MSG_15 | R/W1S | 0x0 | New message status of mailbox 15<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 29 | NOT_FULL_14 | R/W1S | 0x0 | Not full status of mailbox 14<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 28 | NEW_MSG_14 | R/W1S | 0x0 | New message status of mailbox 14<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 27 | NOT_FULL_13 | R/W1S | 0x0 | Not full status of mailbox 13<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 26 | NEW_MSG_13 | R/W1S | 0x0 | New message status of mailbox 13<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 25 | NOT_FULL_12 | R/W1S | 0x0 | Not full status of mailbox 12<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 24 | NEW_MSG_12 | R/W1S | 0x0 | New message status of mailbox 12<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 23 | NOT_FULL_11 | R/W1S | 0x0 | Not full status of mailbox 11<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 22 | NEW_MSG_11 | R/W1S | 0x0 | New message status of mailbox 11<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 21 | NOT_FULL_10 | R/W1S | 0x0 | Not full status of mailbox 10<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 20 | NEW_MSG_10 | R/W1S | 0x0 | New message status of mailbox 10<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 19 | NOT_FULL_9 | R/W1S | 0x0 | Not full status of mailbox 9<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 18 | NEW_MSG_9 | R/W1S | 0x0 | New message status of mailbox 9<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 17 | NOT_FULL_8 | R/W1S | 0x0 | Not full status of mailbox 8<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 16 | NEW_MSG_8 | R/W1S | 0x0 | New message status of mailbox 8<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 15 | NOT_FULL_7 | R/W1S | 0x0 | Not full status of mailbox 7<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 14 | NEW_MSG_7 | R/W1S | 0x0 | New message status of mailbox 7<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 13 | NOT_FULL_6 | R/W1S | 0x0 | Not full status of mailbox 6<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 12 | NEW_MSG_6 | R/W1S | 0x0 | New message status of mailbox 6<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 11 | NOT_FULL_5 | R/W1S | 0x0 | Not full status of mailbox 5<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 10 | NEW_MSG_5 | R/W1S | 0x0 | New message status of mailbox 5<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 9 | NOT_FULL_4 | R/W1S | 0x0 | Not full status of mailbox 4<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 8 | NEW_MSG_4 | R/W1S | 0x0 | New message status of mailbox 4<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 7 | NOT_FULL_3 | R/W1S | 0x0 | Not full status of mailbox 3<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 6 | NEW_MSG_3 | R/W1S | 0x0 | New message status of mailbox 3<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 5 | NOT_FULL_2 | R/W1S | 0x0 | Not full status of mailbox 2<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 4 | NEW_MSG_2 | R/W1S | 0x0 | New message status of mailbox 2<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 3 | NOT_FULL_1 | R/W1S | 0x0 | Not full status of mailbox 1<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 2 | NEW_MSG_1 | R/W1S | 0x0 | New message status of mailbox 1<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 1 | NOT_FULL_0 | R/W1S | 0x0 | Not full status of mailbox 0<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 0 | NEW_MSG_0 | R/W1S | 0x0 | New message status of mailbox 0<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |

#### MAILBOX_IRQSTATUS_CLR_u

Offset: 0x0104 + (0x10 * u)

Interrupt status clear register.
Writing `1` to a bit in this register clears the corresponding interrupt status.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31 | NOT_FULL_15 | R/W1C | 0x0 | Not full status of mailbox 15<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 30 | NEW_MSG_15 | R/W1C | 0x0 | New message status of mailbox 15<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 29 | NOT_FULL_14 | R/W1C | 0x0 | Not full status of mailbox 14<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 28 | NEW_MSG_14 | R/W1C | 0x0 | New message status of mailbox 14<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 27 | NOT_FULL_13 | R/W1C | 0x0 | Not full status of mailbox 13<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 26 | NEW_MSG_13 | R/W1C | 0x0 | New message status of mailbox 13<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 25 | NOT_FULL_12 | R/W1C | 0x0 | Not full status of mailbox 12<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 24 | NEW_MSG_12 | R/W1C | 0x0 | New message status of mailbox 12<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 23 | NOT_FULL_11 | R/W1C | 0x0 | Not full status of mailbox 11<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 22 | NEW_MSG_11 | R/W1C | 0x0 | New message status of mailbox 11<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 21 | NOT_FULL_10 | R/W1C | 0x0 | Not full status of mailbox 10<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 20 | NEW_MSG_10 | R/W1C | 0x0 | New message status of mailbox 10<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 19 | NOT_FULL_9 | R/W1C | 0x0 | Not full status of mailbox 9<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 18 | NEW_MSG_9 | R/W1C | 0x0 | New message status of mailbox 9<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 17 | NOT_FULL_8 | R/W1C | 0x0 | Not full status of mailbox 8<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 16 | NEW_MSG_8 | R/W1C | 0x0 | New message status of mailbox 8<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 15 | NOT_FULL_7 | R/W1C | 0x0 | Not full status of mailbox 7<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 14 | NEW_MSG_7 | R/W1C | 0x0 | New message status of mailbox 7<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 13 | NOT_FULL_6 | R/W1C | 0x0 | Not full status of mailbox 6<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 12 | NEW_MSG_6 | R/W1C | 0x0 | New message status of mailbox 6<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 11 | NOT_FULL_5 | R/W1C | 0x0 | Not full status of mailbox 5<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 10 | NEW_MSG_5 | R/W1C | 0x0 | New message status of mailbox 5<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 9 | NOT_FULL_4 | R/W1C | 0x0 | Not full status of mailbox 4<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 8 | NEW_MSG_4 | R/W1C | 0x0 | New message status of mailbox 4<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 7 | NOT_FULL_3 | R/W1C | 0x0 | Not full status of mailbox 3<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 6 | NEW_MSG_3 | R/W1C | 0x0 | New message status of mailbox 3<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 5 | NOT_FULL_2 | R/W1C | 0x0 | Not full status of mailbox 2<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 4 | NEW_MSG_2 | R/W1C | 0x0 | New message status of mailbox 2<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |
| 3 | NOT_FULL_1 | R/W1C | 0x0 | Not full status of mailbox 1<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: clear the event (for debug) |
| 2 | NEW_MSG_1 | R/W1C | 0x0 | New message status of mailbox 1<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: set the event (for debug) |
| 1 | NOT_FULL_0 | R/W1C | 0x0 | Not full status of mailbox 0<br>• Read 0: No event (message queue full)<br>• Write 0: no action<br>• Read 1: event pending (message queue not full)<br>• Write 1: set the event (for debug) |
| 0 | NEW_MSG_0 | R/W1C | 0x0 | New message status of mailbox 0<br>• Read 0: No event (Message)<br>• Write 0: no action<br>• Read 1: Event (message) pending<br>• Write 1: clear the event (for debug) |

#### MAILBOX_IRQENABLE_SET_u

Offset: 0x0108 + (0x10 * u)

Interrupt enable register. It specifies which mailbox interrupts are received by the corresponding user. Writing `1` sets the corresponding enable bit.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31 | NOT_FULL_EN_15 | R/W1S | 0x0 | Not full interrupt enable of mailbox 15<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 30 | NEW_MSG_EN_15 | R/W1S | 0x0 | New message interrupt enable of mailbox 15<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 29 | NOT_FULL_EN_14 | R/W1S | 0x0 | Not full interrupt enable of mailbox 14<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 28 | NEW_MSG_EN_14 | R/W1S | 0x0 | New message interrupt enable of mailbox 14<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 27 | NOT_FULL_EN_13 | R/W1S | 0x0 | Not full interrupt enable of mailbox 13<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 26 | NEW_MSG_EN_13 | R/W1S | 0x0 | New message interrupt enable of mailbox 13<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 25 | NOT_FULL_EN_12 | R/W1S | 0x0 | Not full interrupt enable of mailbox 12<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 24 | NEW_MSG_EN_12 | R/W1S | 0x0 | New message interrupt enable of mailbox 12<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 23 | NOT_FULL_EN_11 | R/W1S | 0x0 | Not full interrupt enable of mailbox 11<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 22 | NEW_MSG_EN_11 | R/W1S | 0x0 | New message interrupt enable of mailbox 11<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 21 | NOT_FULL_IE_10 | R/W1S | 0x0 | Not full interrupt enable of mailbox 10<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 20 | NEW_MSG_IE_10 | R/W1S | 0x0 | New message interrupt enable of mailbox 10<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 19 | NOT_FULL_IE_9 | R/W1S | 0x0 | Not full interrupt enable of mailbox 9<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 18 | NEW_MSG_IE_9 | R/W1S | 0x0 | New message interrupt enable of mailbox 9<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 17 | NOT_FULL_IE_8 | R/W1S | 0x0 | Not full interrupt enable of mailbox 8<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 16 | NEW_MSG_IE_8 | R/W1S | 0x0 | New message interrupt enable of mailbox 8<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 15 | NOT_FULL_IE_7 | R/W1S | 0x0 | Not full interrupt enable of mailbox 7<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 14 | NEW_MSG_IE_7 | R/W1S | 0x0 | New message interrupt enable of mailbox 7<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 13 | NOT_FULL_IE_6 | R/W1S | 0x0 | Not full interrupt enable of mailbox 6<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 12 | NEW_MSG_IE_6 | R/W1S | 0x0 | New message interrupt enable of mailbox 6<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 11 | NOT_FULL_IE_5 | R/W1S | 0x0 | Not full interrupt enable of mailbox 5<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 10 | NEW_MSG_IE_5 | R/W1S | 0x0 | New message interrupt enable of mailbox 5<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 9 | NOT_FULL_IE_4 | R/W1S | 0x0 | Not full interrupt enable of mailbox 4<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 8 | NEW_MSG_IE_4 | R/W1S | 0x0 | New message interrupt enable of mailbox 4<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 7 | NOT_FULL_IE_3 | R/W1S | 0x0 | Not full interrupt enable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 6 | NEW_MSG_IE_3 | R/W1S | 0x0 | New message interrupt enable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 5 | NOT_FULL_IE_2 | R/W1S | 0x0 | Not full interrupt enable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 4 | NEW_MSG_IE_2 | R/W1S | 0x0 | New message interrupt enable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 3 | NOT_FULL_IE_1 | R/W1S | 0x0 | Not full interrupt enable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 2 | NEW_MSG_IE_1 | R/W1S | 0x0 | New message interrupt enable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: enable interrupt |
| 1 | NOT_FULL_IE_0 | R/W1S | 0x0 | Not full interrupt enable of mailbox 0 <br>• Read 0: Interrupt disabled <br>• Write 0: no action <br>• Read 1: interrupt enabled <br>• Write 1: enable interrupt |
| 0 | NEW_MSG_IE_0 | R/W1S | 0x0 | New message interrupt enable of mailbox 0 <br>• Read 0: Interrupt disabled <br>• Write 0: no action <br>• Read 1: interrupt enabled <br>• Write 1: enable interrupt

#### MAILBOX_IRQENABLE_CLR_u

Offset: 0x010C + (0x10 * u)

This register clears interrupt enables. Writing `1` clears the corresponding enable bit.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31 | NOT_FULL_DIS_3 | R/W1C | 0x0 | Not full interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 30 | NEW_MSG_DIS_3 | R/W1C | 0x0 | New message interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 29 | NOT_FULL_DIS_2 | R/W1C | 0x0 | Not full interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 28 | NEW_MSG_DIS_2 | R/W1C | 0x0 | New message interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 27 | NOT_FULL_DIS_1 | R/W1C | 0x0 | Not full interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 26 | NEW_MSG_DIS_1 | R/W1C | 0x0 | New message interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 25 | NOT_FULL_DIS_0 | R/W1C | 0x0 | Not full interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 24 | NEW_MSG_DIS_0 | R/W1C | 0x0 | New message interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 23 | NOT_FULL_DIS_3_2 | R/W1C | 0x0 | Not full interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 22 | NEW_MSG_DIS_3_2 | R/W1C | 0x0 | New message interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 21 | NOT_FULL_DIS_2 | R/W1C | 0x0 | Not full interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 20 | NEW_MSG_DIS_2 | R/W1C | 0x0 | New message interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 19 | NOT_FULL_DIS_1 | R/W1C | 0x0 | Not full interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 18 | NEW_MSG_DIS_1 | R/W1C | 0x0 | New message interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 17 | NOT_FULL_DIS_0 | R/W1C | 0x0 | Not full interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 16 | NEW_MSG_DIS_0 | R/W1C | 0x0 | New message interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 15 | NOT_FULL_DIS_3 | R/W1C | 0x0 | Not full interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 14 | NEW_MSG_DIS_3 | R/W1C | 0x0 | New message interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 13 | NOT_FULL_DIS_2 | R/W1C | 0x0 | Not full interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 12 | NEW_MSG_DIS_2 | R/W1C | 0x0 | New message interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 11 | NOT_FULL_DIS_1 | R/W1C | 0x0 | Not full interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action　<br>• Read 1: interrupt enabled　<br>• Write 1: disable interrupt
| 10 | NEW_MSG_DIS_1 | R/W1C | 0x0 | New message interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 9 | NOT_FULL_DIS_0 | R/W1C | 0x0 | Not full interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 8 | NEW_MSG_DIS_0 | R/W1C | 0x0 | New message interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 7 | NOT_FULL_DIS_3 | R/W1C | 0x0 | Not full interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 6 | NEW_MSG_DIS_3 | R/W1C | 0x0 | New message interrupt disable of mailbox 3<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 5 | NOT_FULL_DIS_2 | R/W1C | 0x0 | Not full interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 4 | NEW_MSG_DIS_2 | R/W1C | 0x0 | New message interrupt disable of mailbox 2<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 3 | NOT_FULL_DIS_1 | R/W1C | 0x0 | Not full interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 2 | NEW_MSG_DIS_1 | R/W1C | 0x0 | New message interrupt disable of mailbox 1<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 1 | NOT_FULL_DIS_0 | R/W1C | 0x0 | Not full interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action<br>• Read 1: interrupt enabled<br>• Write 1: disable interrupt |
| 0 | NEW_MSG_DIS_0 | R/W1C | 0x0 | New message interrupt disable of mailbox 0<br>• Read 0: Interrupt disabled<br>• Write 0: no action　<br>• Read 1: interrupt enabled　<br>• Write 1: disable interrupt　｜


#### MAILBOX_IRQTHR0_u

Offset: 0x0180 + (0x10 * u)

Interrupt threshold register.
A Not Full interrupt is generated when the Not Full interrupt is enabled and the number of data words in the FIFO is less than the configured Not Full threshold.
A New Message interrupt is generated when the New Message interrupt is enabled and the number of data words in the FIFO is greater than the configured New Message threshold.
The threshold mechanism is provided to avoid excessive interrupt generation.

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | M3_NOT_FULL_TH | R/W | 0x8 | Mailbox 3 not full interrupt threshold of user u<br>m3 not full is generated, only when num of messages in m3 < [31:28] |
| 27:24 | M3_NEW_MSG_TH | R/W | 0x0 | Mailbox 3 new message interrupt threshold of user u<br>m3 new message is generated, only when num of messages in m3 > [27:24] |
| 23:20 | M2_NOT_FULL_TH | R/W | 0x8 | Mailbox 2 not full interrupt threshold of user u<br>m2 not full is generated, only when num of messages in m2 < [23:20] |
| 19:16 | M2_NEW_MSG_TH | R/W | 0x0 | Mailbox 2 new message interrupt threshold of user u<br>m2 new message is generated, only when num of messages in m2 > [19:16] |
| 15:12 | M1_NOT_FULL_TH | R/W | 0x8 | Mailbox 1 not full interrupt threshold of user u<br>m1 not full is generated, only when num of messages in m1 < [15:12] |
| 11:8 | M1_NEW_MSG_TH | R/W | 0x0 | Mailbox 1 new message interrupt threshold of user u<br>m1 new message is generated, only when num of messages in m1 > [11:8] |
| 7:4 | M0_NOT_FULL_TH | R/W | 0x8 | Mailbox 0 not full interrupt threshold of user u<br>m0 not full is generated, only when num of messages in m0 < [7:4] |
| 3:0 | M0_NEW_MSG_TH | R/W | 0x0 | Mailbox 0 new message interrupt threshold of user u<br>m0 new message is generated, only when num of messages in m0 > [3:0] |

#### MAILBOX_IRQTHR1_u

Offset: 0x0184 + (0x10 * u)

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | M7_NOT_FULL_TH | R/W | 0x8 | Mailbox 7 not full interrupt threshold of user u<br>m7 not full is generated, only when num of messages in m7 < [31:28] |
| 27:24 | M7_NEW_MSG_TH | R/W | 0x0 | Mailbox 7 new message interrupt threshold of user u<br>m7 new message is generated, only when num of messages in m7 > [27:24] |
| 23:20 | M6_NOT_FULL_TH | R/W | 0x8 | Mailbox 6 not full interrupt threshold of user u<br>m6 not full is generated, only when num of messages in m6 < [23:20] |
| 19:16 | M6_NEW_MSG_TH | R/W | 0x0 | Mailbox 6 new message interrupt threshold of user u<br>m6 new message is generated, only when num of messages in m6 > [19:16] |
| 15:12 | M5_NOT_FULL_TH | R/W | 0x8 | Mailbox 5 not full interrupt threshold of user u<br>m5 not full is generated, only when num of messages in m5 < [15:12] |
| 11:8 | M5_NEW_MSG_TH | R/W | 0x0 | Mailbox 5 new message interrupt threshold of user u<br>m5 new message is generated, only when num of messages in m5 > [11:8] |
| 7:4 | M4_NOT_FULL_TH | R/W | 0x8 | Mailbox 4 not full interrupt threshold of user u<br>m4 not full is generated, only when num of messages in m4 < [7:4] |
| 3:0 | M4_NEW_MSG_TH | R/W | 0x0 | Mailbox 4 new message interrupt threshold of user u<br>m4 new message is generated, only when num of messages in m4 > [3:0] |

#### MAILBOX_IRQTHR2_u

Offset: 0x0188 + (0x10 * u)

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | M11_NOT_FULL_TH | R/W | 0x8 | Mailbox 11 not full interrupt threshold of user u<br>m11 not full is generated, only when num of messages in m11 < [31:28] |
| 27:24 | M11_NEW_MSG_TH | R/W | 0x0 | Mailbox 11 new message interrupt threshold of user u<br>m11 new message is generated, only when num of messages in m11 > [27:24] |
| 23:20 | M10_NOT_FULL_TH | R/W | 0x8 | Mailbox 10 not full interrupt threshold of user u<br>m10 not full is generated, only when num of messages in m10 < [23:20] |
| 19:16 | M10_NEW_MSG_TH | R/W | 0x0 | Mailbox 10 new message interrupt threshold of user u<br>m10 new message is generated, only when num of messages in m10 > [19:16] |
| 15:12 | M9_NOT_FULL_TH | R/W | 0x8 | Mailbox 9 not full interrupt threshold of user u<br>m9 not full is generated, only when num of messages in m9 < [15:12] |
| 11:8 | M9_NEW_MSG_TH | R/W | 0x0 | Mailbox 9 new message interrupt threshold of user u<br>m9 new message is generated, only when num of messages in m9 > [11:8] |
| 7:4 | M8_NOT_FULL_TH | R/W | 0x8 | Mailbox 8 not full interrupt threshold of user u<br>m8 not full is generated, only when num of messages in m8 < [7:4] |
| 3:0 | M8_NEW_MSG_TH | R/W | 0x0 | Mailbox 8 new message interrupt threshold of user u<br>m8 new message is generated, only when num of messages in m8 > [3:0] |

#### MAILBOX_IRQTHR3_u

Offset: 0x018C + (0x10 * u)

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | M15_NOT_FULL_TH | R/W | 0x8 | Mailbox 15 not full interrupt threshold of user u<br>m15 not full is generated, only when num of messages in m15 < [31:28] |
| 27:24 | M15_NEW_MSG_TH | R/W | 0x0 | Mailbox 15 new message interrupt threshold of user u<br>m15 new message is generated, only when num of messages in m15 > [27:24] |
| 23:20 | M14_NOT_FULL_TH | R/W | 0x8 | Mailbox 14 not full interrupt threshold of user u<br>m14 not full is generated, only when num of messages in m14 < [23:20] |
| 19:16 | M14_NEW_MSG_TH | R/W | 0x0 | Mailbox 14 new message interrupt threshold of user u<br>m14 new message is generated, only when num of messages in m14 > [19:16] |
| 15:12 | M13_NOT_FULL_TH | R/W | 0x8 | Mailbox 13 not full interrupt threshold of user u<br>m13 not full is generated, only when num of messages in m13 < [15:12] |
| 11:8 | M13_NEW_MSG_TH | R/W | 0x0 | Mailbox 13 new message interrupt threshold of user u<br>m13 new message is generated, only when num of messages in m13 > [11:8] |
| 7:4 | M12_NOT_FULL_TH | R/W | 0x8 | Mailbox 12 not full interrupt threshold of user u<br>m12 not full is generated, only when num of messages in m12 < [7:4] |
| 3:0 | M12_NEW_MSG_TH | R/W | 0x0 | Mailbox 12 new message interrupt threshold of user u<br>m12 new message is generated, only when num of messages in m12 > [3:0] |

## 16.6.5 Programming Model

### 16.6.5.1 Mailbox New Message Interrupt

[User0 sends messages to User1]
  1. User1 enables the New Message interrupt for Mailbox0 by writing `0x1` to `MAILBOX_IRQENABLE_SET_1[1:0]`, and then waits for the interrupt.
  2. Before sending messages, User0 checks the status of Mailbox0:
      - `MAILBOX_FIFOSTATUS_0[0] != 1`, or
      - `MAILBOX_MSGSTATUS_0[3:0] < 0x8`.
  3. User0 writes one or more messages to `MAILBOX_MESSAGE_0`, ensuring that the FIFO does not overflow.
  4. After the first message is written, the FIFO contains data. If no interrupt threshold is configured, User1 receives an interrupt (`MAILBOX_IRQSTATUS_RAW_1[0] = 1`).
  5. In the interrupt service routine:
      - Clear the New Message interrupt enable and interrupt status for Mailbox0.
      - Read `MAILBOX_MSGSTATUS_0[3:0]` to obtain the number of messages in the FIFO.
      - Repeatedly read `MAILBOX_MESSAGE_0` until all messages have been retrieved.
  6. After all messages have been processed, re-enable the interrupt. The message transfer is then complete.

[User1 sends messages to User0]

The procedure is the same as in [User0 sends messages to User1], except that the corresponding registers are different.

### 16.6.5.2 Mailbox Not Full Interrupt

[User0 sends multiple messages to User1]

When the message length exceeds `8 × 32-bit` words, the FIFO may become full. In this case, User0 waits for a Not Full interrupt, which is triggered after User1 reads data, before continuing to send messages.
  1. According to the channel assignment, User0 uses Mailbox1 to send messages to User1. Before writing, User0 checks `MAILBOX_MSGSTATUS_1[3:0]` to ensure that the Mailbox1 FIFO is not full. User0 then writes multiple messages to `MAILBOX_MESSAGE_1` until the FIFO becomes full.
  2. If User1 is slow to read messages or is busy with other tasks, User0 may perform other operations while waiting for User1 to read data from the FIFO. Once space becomes available, a Not Full interrupt is generated. To receive this interrupt, User0 writes `2'b10` to `MAILBOX_IRQENABLE_SET_0[3:2]` to enable the Not Full interrupt from Mailbox1. After the interrupt occurs, User0 can resume sending messages.
  3. After User1 reads messages from the FIFO, User0 receives the interrupt. User0 checks `MAILBOX_IRQSTATUS_RAW_0` to confirm that the interrupt is the Not Full event from Mailbox1, and then continues sending messages to the mailbox.

The procedure for testing Not Full interrupts between other CPUs is similar.

### 16.6.5.3 Mailbox Interrupt Thresholds

[Not Full Interrupt Threshold]

Due to possible performance differences between User0 and User1, for example, User0 running at 2 GHz and User1 at 200 MHz, when User0 sends a large amount of data to User1, the slower read rate of User1 may cause frequent Not Full interrupts on User0. To mitigate this issue, a Not Full interrupt threshold register is provided.
  1. According to the channel assignment, User0 can use Mailbox0 to send messages to User1. Before writing, User0 reads `MAILBOX_MSGSTATUS_0[3:0]` to ensure that the Mailbox0 FIFO is not full, and then writes multiple messages to `MAILBOX_MESSAGE_0` until the FIFO becomes full.
  2. User0 writes `0x4` to `MAILBOX_IRQTHR_0[7:4]`, which means a Not Full interrupt is triggered only when the number of entries in Mailbox0 drops below `4 × 32-bit` words. User0 then writes `2'b10` to `MAILBOX_IRQENABLE_SET_0[1:0]` to enable the Not Full interrupt from Mailbox0 to User0.
  3. When User1 reads messages, if the number of entries in Mailbox0 becomes smaller than the configured threshold, User0 receives the interrupt. User0 checks `MAILBOX_IRQSTATUS_RAW_0` to confirm that the interrupt is the Not Full interrupt from Mailbox0, and then continues sending messages to the mailbox.

[New Message Interrupt Threshold]

Similarly, when User1 sends messages to User0, User1 may write messages relatively slowly while User0 reads them quickly. In this case, a New Message interrupt may be triggered immediately after each write, causing frequent interrupts and allowing User0 to read only one message at a time. To avoid this issue, a New Message interrupt threshold register is provided.
  1. User0 writes `0x4` to `MAILBOX_IRQTHR_0[19:16]`, which means a New Message interrupt is generated only when Mailbox2 contains at least `5 × 32-bit` words. User0 then writes `2'b01` to `MAILBOX_IRQENABLE_SET_0[5:4]` to enable the New Message interrupt from Mailbox2 to User0.
  2. According to the channel assignment, User1 can use Mailbox2 to send messages to User0. Before writing, User1 reads `MAILBOX_MSGSTATUS_2[3:0]` to ensure that the Mailbox2 FIFO is not full, and then writes multiple messages to `MAILBOX_MESSAGE_2` until the FIFO becomes full.
  3. User1 continues writing messages until the number of entries in Mailbox2 exceeds the configured threshold. At this point, User0 receives the New Message interrupt, checks `MAILBOX_IRQSTATUS_RAW_0` to confirm that the interrupt originates from Mailbox2, and reads `MAILBOX_MESSAGE_2` to retrieve the messages.

