---
sidebar_position: 3
---

# 14.3 Ethernet GMAC

## 14.3.1 Overview

The K3 SoC integrates four GMAC interfaces for Ethernet communication.

**Controller Architecture:**

- Based on Synopsys DesignWare Ethernet QoS controller
- Complies with IEEE 802.3-2015 standard
- Consists of three modules: MAC, MTL, and DMA

**Interface Support:**

- Application side: AXI interface
- PHY side: MII, RMII, and RGMII
- Link speeds: 10/100/1000 Mbps

**Key Capabilities:**

- Packet filtering
- Hardware offload functions
- Flow control
- PTP time synchronization
- Energy Efficient Ethernet (EEE)
- Time-Sensitive Networking (TSN)

**Applications:**

- AV bridges and nodes
- Network switches
- Network interface cards
- Data center bridges and nodes

## 14.3.2 Features

### 14.3.2.1 MAC Features

- Supports MII, RMII, and RGMII interface modes
- Supports 10/100/1000 Mbps link speeds
- Supports automatic CRC generation and stripping
- Supports standard Ethernet frames
- Supports jumbo frames
- Supports source address insertion and replacement
- Supports VLAN tag insertion, replacement, and removal
- Supports VLAN filtering on received packets
- Supports destination address filtering
- Supports source address filtering
- Supports perfect match filtering
- Supports hash filtering
- Supports promiscuous mode
- Supports Layer 3 filtering
- Supports Layer 4 filtering
- Supports IPv4 packet filtering
- Supports IPv6 packet filtering
- Supports TCP packet filtering
- Supports UDP packet filtering
- Supports IEEE 802.3x Pause frame flow control
- Supports Priority Flow Control (PFC)
- Supports half-duplex backpressure flow control
- Supports transmit and receive timestamping
- Supports one-step timestamping
- Supports two-step timestamping
- Supports one PPS output
- Supports Wake-on-LAN (WoL)
- Supports MAC loopback mode

### 14.3.2.2 MTL Features

- Supports programmable burst length
- Supports up to four Tx/Rx queues
- Supports Store-and-Forward mode
- Supports Threshold mode
- Supports Strict Priority (SP) scheduling
- Supports Weighted Round Robin (WRR) scheduling
- Supports Deficit Weighted Round Robin (DWRR) scheduling
- Supports Weighted Fair Queuing (WFQ) scheduling
- Supports Credit Based Shaper (CBS)
- Supports Enhancements for Scheduled Traffic (EST)
- Supports frame preemption
- Supports Time Based Scheduling (TBS)

### 14.3.2.3 DMA Features

- Supports up to four Tx/Rx DMA channels
- Supports TCP Segmentation Offload (TSO)
- Supports checksum insertion on transmit packets
- Supports checksum checking on received packets
- Supports IPv4 checksum offload
- Supports TCP checksum offload
- Supports UDP checksum offload
- Supports ICMP checksum offload
- Supports header/payload split storage
- Supports ARP offload
- Supports packet routing to different channels based on priority
- Supports packet routing to different channels based on VLAN priority

## 14.3.3 Signal Descriptions

| Signal | Description |
| --- | --- |
| RXDV | Receive control signal. In MII mode, this pin is used as RXDV. In RMII mode, it is multiplexed as CRS_DV. In RGMII mode, it is multiplexed as RX_CTL. |
| RX_D0 | Receive data bit 0. Used in MII, RMII, and RGMII modes. |
| RX_D1 | Receive data bit 1. Used in MII, RMII, and RGMII modes. |
| RX_CLK | Receive/reference clock signal. In MII mode, this pin is used as RX_CLK. In RMII mode, this pin is unused and should be left unconnected. In RGMII mode, it is used as RX_CLK. |
| RX_D2 | Receive data bit 2. Used in RGMII mode only. |
| RX_D3 | Receive data bit 3. Used in RGMII mode only. |
| TX_D0 | Transmit data bit 0. Used in MII, RMII, and RGMII modes. |
| TX_D1 | Transmit data bit 1. Used in MII, RMII, and RGMII modes. |
| TX_CLK | Transmit/reference clock signal. In RGMII mode, this pin is used as TX_CLK and may operate as either an input or output depending on the clock configuration. In RMII mode, it is used as REF_CLK and receives the reference clock from the PHY. |
| TX_D2 | Transmit data bit 2. Used in RGMII mode only. |
| TX_D3 | Transmit data bit 3. Used in RGMII mode only. |
| TX_EN | Transmit control signal. In MII and RMII modes, this pin is used as TX_EN. In RGMII mode, it is multiplexed as TX_CTL. |
| MDC | Management Data Clock for the MDIO interface. Used to drive PHY management transactions. |
| MDIO | Management Data Input/Output for the MDIO interface. Used to access PHY registers. |
| INT_N | Interrupt input from the PHY, active low. |
| RXER | Receive error indication signal. Used in MII mode only. |
| TXER | Transmit error indication signal. Used in MII mode only. |
| CRS | Carrier sense signal. Used in MII mode only. |
| COL | Collision detect signal. Used in MII mode only. |
| PPS | Pulse Per Second output. |
| CLK_REF | Optional reference clock output for the external PHY. It can be used as the PHY reference clock source in place of an external 25 MHz crystal. |

## 14.3.4 Register Description

All four GMAC controllers each have two platform registers: a control register (CTRL) and a delay line register (DLINE). Their base addresses and offsets are as follows:

- **GMAC0**
  - CTRL register: base = 0xd4282be4, offset = 0x3e4
  - DLINE register: base = 0xd4282be4, offset = 0x3e8
- **GMAC1**
  - CTRL register: base = 0xd4282be4, offset = 0x3ec
  - DLINE register: base = 0xd4282be4, offset = 0x3f0
- **GMAC2**
  - CTRL register: base = 0xd4282be4, offset = 0x248
  - DLINE register: base = 0xd4282be4, offset = 0x24c
- **GMAC3**
  - CTRL register: base = 0xc0880000, offset = 0x0e4
  - DLINE register: base = 0xc0880000, offset = 0x0e8

Below, the descriptions of these two registers are provided for GMAC0 as an example; the bit definitions for the corresponding registers in the other GMAC controllers are identical.

### 14.3.4.1 GMAC0 CTRL Register

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0 | Reserved for future use |
| 15 | EMAC0_1588_CLK_MUX | RW | 0x0 | 1 = PLL 125 MHz/25 MHz/2.5 MHz (matches the current speed mode: 1000M/100M/10M)<br>0 = 24M |
| 14 | EMAC0_CLK_REF_GATE | RW | 0x0 | 1 = tx 25M refclk disable<br>0 = tx 25M refclk enable |
| 13 | EMAC0_AXI_MST_ID | RW | 0x0 | 1 = EMAC0 AXI MST interface uses a single ID to issue transfers<br>0 = EMAC0 AXI MST interface uses multiple IDs to issue transfers |
| 12 | EMAC0_PHY_INTR_EN | RW | 0x0 | 1 = EMAC0 PHY PMT Intr MASK enable<br>0 = EMAC0 PHY PMT Intr MASK disable |
| 11:10 | RSVD | RO | 0 | Reserved for future use |
| 9 | EMAC0_LPI_INTR_EN | RW | 0x0 | 1 = EMAC0 LPI Intr MASK enable<br>0 = EMAC0 LPI Intr MASK disable |
| 8 | EMAC0_RGMII_TXC_SRC_SEL | RW | 0x0 | This bit is only valid in RGMII mode.<br>1 = tx clock source from SoC<br>0 = tx clock source from RX clock |
| 7 | EMAC_RX_REFCLK_PHASE_SEL | RW | 0x0 | EMAC0 RX REFCLK PHASE SEL<br>1 = REFCLK inv<br>0 = REFCLK |
| 6 | EMAC_RMII_TX_REFCLK_PHASE_SEL | RW | 0x0 | EMAC0 RMII TX REFCLK PHASE SEL<br>1 = RMII REFCLK inv<br>0 = RMII REFCLK |
| 5 | RSVD | RO | 0 | Reserved for future use |
| 4:3 | EMAC0_PHY_SELECT | RW | 0x0 | EMAC0 PHY SELECT<br>2'b11 = MII<br>2'b01 = RGMII<br>2'b00 = RMII |
| 2 | RSVD | RO | 0 | Reserved for future use |
| 1 | EMAC0_BUS_RST | RW | 0x0 | EMAC0 AXI Bus Reset<br>1 = Reset Release (deasserted)<br>0 = Reset |
| 0 | EMAC0_BUS_EN | RW | 0x0 | EMAC0 AXI Bus Clock Enable<br>1 = AXI clock enabled<br>0 = AXI clock disabled |

### 14.3.4.2 GMAC0 DLINE Register

| Bits | Field (Code) | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | EMAC0_RGMII_TXC_DLINE_ADJ | RW | 0x0 | Delay code |
| 23:22 | RSVD | RO | 0 | Reserved for future use |
| 21:20 | EMAC0_RGMII_TXC_DLINE_STEP | RW | 0x0 | Delay step:<br>2'b00: 15.6 ps,<br>2'b01: 24.4 ps,<br>2'b10: 29.7 ps,<br>2'b11: 35.1 ps |
| 19:17 | RSVD | RO | 0 | Reserved for future use |
| 16 | EMAC0_RGMII_TXC_DLINE_PU | RW | 0x0 | Delay line enable |
| 15:8 | EMAC0_RGMII_RXC_DLINE_ADJ | RW | 0x0 | Delay code |
| 7:6 | RSVD | RO | 0 | Reserved for future use |
| 5:4 | EMAC0_RGMII_RXC_DLINE_STEP | RW | 0x0 | Delay step:<br>2'b00: 15.6 ps,<br>2'b01: 24.4 ps,<br>2'b10: 29.7 ps,<br>2'b11: 35.1 ps |
| 3:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | EMAC0_RGMII_RXC_DLINE_PU | RW | 0x0 | Delay line enable |

