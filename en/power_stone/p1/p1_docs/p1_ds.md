sidebar_position: 2

# P1 Datasheet

## PDF Version

Click to download [P1 Datasheet (PDF)](https://cdn-resource.spacemit.com/file/chip/P1/P1_Datasheet_en.pdf)

## Revision History

| Version | Date       | Notes                                                                                              |
|---------|------------|----------------------------------------------------------------------------------------------------|
| V2.0    | 2025.03.31 | Restructured and improved the quality of all content of the whole document                         |
| V1.3    | 2025.03.28 | Quick revision of all content of the whole document                                                |
| V1.2    | 2024.09.11 | Update parameters                                                                                |
| V1.1    | 2024.05.04 | Update parameters                                                                                |
| V1.0    | 2024.02.08 | Initial version                                                                                  |

## 1. Product Overview

### 1.1 General Description

SpacemiT® Power Stone™ P1 is a highly integrated multi-channel Power Management IC (PMIC) designed to meet diverse power requirements across a wide range of applications, providing customers with a complete power solution.  
It integrates six Constant On-Time (COT) controlled buck converters, twelve Low Dropout Regulators (LDOs), an I²C interface, and multi-time programmable non-volatile memory (MTP), enabling highly flexible and programmable power management for mobile devices and embedded systems.

The six fully integrated buck converters provide stable power for multiple target voltage rails. The COT control architecture delivers fast load transient response. Operating in Continuous Conduction Mode (CCM), the default 1.5 MHz fixed switching frequency significantly reduces the required external inductance and capacitance. Comprehensive protection features include Undervoltage Lockout (UVLO), Overcurrent Protection (OCP), Overvoltage Protection (OVP), and Thermal Shutdown.  
Dynamic Voltage Control (DVC) enables real-time voltage adjustment to match application requirements.

All output voltages as well as power-up and power-down sequencing can be preconfigured via the MTP interface and controlled through the I²C bus. The P1 requires only a minimal number of external components and is available in a compact QFN-60 (7 mm × 7 mm) package.

### 1.2 Key Features

- Input Supply Voltage (VIN): 2.7 V to 5.5 V  

- 6 High-Efficiency Buck Converters
  - Buck1 / Buck2: 0.5 V to 3.4 V, up to 4 A, supports dual-phase operation  
  - Buck3 / Buck4: 0.5 V to 3.4 V, up to 3 A, supports dual-phase operation  
  - Buck5 / Buck6: 0.5 V to 3.4 V, up to 2.5 A  
  - Selectable output voltage ranges for all buck converters:  
    - 0.5 V to 1.35 V, 5 mV steps  
    - 1.375 V to 3.4 V, 25 mV steps  
  - Adjustable current limit thresholds to optimize for different load requirements  
  - Dedicated pins for selecting VDDQ voltages for different DDR memory devices  

- 12 Programmable LDO Regulators
  - 1 dedicated always-on LDO  
  - 11 low-noise LDOs  
  - Output voltage: 0.5 V to 3.4 V, 25 mV steps  
  - Output current: 0.3 A to 0.5 A  

- 1 Load Switch with up to 1 A output current  

- I²C Communication Interface

- User-Programmable MTP (Multi-Time Programmable Memory)

- System Monitor with Watchdog Timer

- Coin-Cell Battery Support

- Ultra-Low-Power RTC
  - 2 µA typical current consumption  
  - Alarm function supported  

- 12-bit ADC
  - 8 channels  
  - Configurable alarm thresholds  

- Output Voltage Levels and Power-Up / Power-Down Sequences
  - Preconfigured via MTP  

- 6 GPIO Pins for peripheral control  

- Junction Temperature Range: –40 °C to +125 °C  

- Package
  - QFN-60  
  - 7 mm × 7 mm  
  - 0.4 mm pitch  

### 1.3 Applications

- Ultrabooks  
- Tablets  
- E-books
- Virtual Reality (VR) / Augmented Reality (AR) devices  
- Industrial equipment  
- Navigation devices  
- Drones  

## 2. Block Diagram

![](static/CVgqbZypMo36kHx5vpEcOhPAnMg.png)

## 3. Pin Configuration Diagram

The pin configuration of the P1 device is shown below:

![](static/LF0fbF5vZoXL6Mx8XdAcTghIncS.png)

Pin Type Definitions are defined in the table below:

| Pin Type | Description            | Pin Type | Description            |
|---------:|------------------------|---------:|------------------------|
| DI       | Digital Input          | AI       | Analog Input           |
| DO       | Digital Output         | AO       | Analog Output          |
| DIO      | Digital Input / Output | AIO      | Analog Input / Output  |
| PWR      | Power Supply           | GND      | Ground                 |

Pin Descriptions

| Pin No. | Pin Name | Type      | Description   | Multiplexed Function   |
|-------:|----------|-----------|-----------------|-----------|
| 1  | ALDO3   | AO        | ALDO3 voltage output                     | – |
| 2  | ALDOIN  | PWR       | Power input for ALDO1–4                  | – |
| 3  | ALDO1   | AO        | ALDO1 voltage output                     | – |
| 4  | ALDO2   | AO        | ALDO2 voltage output                     | – |
| 5  | FB3GND  | GND       | Buck3 output voltage ground feedback     | – |
| 6  | FB3     | AI        | Buck3 output voltage feedback            | – |
| 7  | SW3     | AIO       | Buck3 switching node                     | – |
| 8  | VIN3    | PWR       | Buck3 power input                        | – |
| 9  | VIN4    | PWR       | Buck4 power input                        | – |
| 10 | SW4     | AIO       | Buck4 switching node                     | – |
| 11 | FB4     | AIN        | Buck4 output voltage feedback            | – |
| 12 | SWIN    | AIN       | Load switch input                        | – |
| 13 | SWOUT   | AO        | Load switch output                       | – |
| 14 | DLDO2   | AO        | DLDO2 voltage output                     | – |
| 15 | DLDO1   | AO        | DLDO1 voltage output                     | – |
| 16 | DLDO3   | AO        | DLDO3 voltage output                     | – |
| 17 | DLDOIN1 | PWR       | Power input for DLDO1–4                  | – |
| 18 | DLDO4   | AO        | DLDO4 voltage output                     | – |
| 19 | VSET6   | AIN        | Buck6 default output voltage setting     | – |
| 20 | FB6     | AIN        | Buck6 output voltage feedback            | – |
| 21 | SW6     | AIN       | Buck6 switching node                     | – |
| 22 | VIN6    | PWR       | Buck6 power input                        | – |
| 23 | VIN5    | PWR       | Buck5 power input                        | – |
| 24 | SW5     | AIO       | Buck5 switching node                     | – |
| 25 | FB5     | AI        | Buck5 output voltage feedback            | – |
| 26 | VSET5   | AI        | Buck5 default output voltage setting     | – |
| 27 | DLDO5   | AO        | DLDO5 voltage output                     | – |
| 28 | DLDO6   | AO        | DLDO6 voltage output                     | – |
| 29 | DLDOIN2 | PWR       | Power input for DLDO5–7                  | – |
| 30 | DLDO7   | AO        | DLDO7 voltage output                     | – |
| 31 | TEST2   | DIO       | Test pin                                | – |
| 32 | TEST1   | DIO       | Test pin                                | – |
| 33 | AGND    | GND       | Analog ground                            | – |
| 34 | FB2     | AI        | Buck2 output voltage feedback            | – |
| 35 | SW2     | AIO       | Buck2 switching node                     | – |
| 36 | VIN2    | PWR       | Buck2 power input                        | – |
| 37 | VIN1    | PWR       | Buck1 power input                        | – |
| 38 | SW1     | AIO       | Buck1 switching node                     | – |
| 39 | FB1     | AI        | Buck1 output voltage feedback            | – |
| 40 | FB1GND  | GND       | Buck1 output voltage ground feedback     | – |
| 41 | VSYS    | PWR       | Internal circuit power input             | – |
| 42 | GPIO5   | DIO / AI  | Multifunction GPIO                      | EXT_EN / SLEEP_WKUP / PWRCTRL / nRESET / ADC input |
| 43 | GPIO4   | DIO / AI  | Multifunction GPIO                      | EXT_EN / SLEEP_WKUP / PWRCTRL / nRESET / ADC input |
| 44 | SDA     | DIO       | I²C data line                            | – |
| 45 | SCL     | DI        | I²C clock line                           | – |
| 46 | VCELL   | AI        | Coin-cell battery voltage input          | – |
| 47 | XTALOUT | AI        | External crystal output                 | – |
| 48 | XTALIN  | AI        | External crystal input                  | – |
| 49 | GPIO3   | DIO / AI  | Multifunction GPIO                      | EXT_EN / SLEEP_WKUP / PWRCTRL / nRESET / ADC input |
| 50 | 32KOUT  | DO        | Clock output                             | – |
| 51 | GPIO2   | DIO / AI  | Multifunction GPIO                      | EXT_EN / SLEEP_WKUP / PWRCTRL / nRESET / ADC input |
| 52 | GPIO1   | DIO / AI  | Multifunction GPIO                      | EXT_EN / SLEEP_WKUP / PWRCTRL / nRESET / ADC input |
| 53 | GPIO0   | DIO / AI  | Multifunction GPIO                      | EXT_EN / SLEEP_WKUP / PWRCTRL / nRESET / ADC input |
| 54 | INT     | DIO       | Interrupt output                        | – |
| 55 | PWRKY   | AI        | Power-on / Power-off / Reset key input  | – |
| 56 | PGOOD   | DIO       | Power-good indicator / Reset source     | – |
| 57 | AGND    | GND       | Analog ground                            | – |
| 58 | VREF    | AO        | Internal reference voltage               | – |
| 59 | AONLDO  | AO        | AON LDO voltage output                  | – |
| 60 | ALDO4   | AO        | ALDO4 voltage output                    | – |

## 4. Absolute Maximum Ratings

The absolute maximum ratings are listed in the table below.  

| Parameter     | Description                     | Conditions | Min   | Typ | Max   | Unit |
|---------------|----------------------------------|------------|-------|-----|-------|------|
| T(STG) | Storage temperature              | –          | -40   | –   | 150   | °C   |
| T(J)   | Junction temperature             | –          | -40   | –   | 125   | °C   |
| V(SYS) | System supply voltage            | –          | -0.3  | –   | 7.0   | V    |
| V(CELL)| Coin-cell battery supply voltage | –          | -0.3  | –   | 7.0   | V    |
| V(ESD_HBM) | ESD protection (HBM)         | –          | 2     | –   | –     | kV   |
| V(ESD_CDM) | ESD protection (CDM)         | –          | 500   | –   | –     | V    |

## 5. Electrical Characteristics

### 5.1 Recommended Operating Conditions

The recommended operating conditions are listed in the table below.

| Parameter | Description                              | Conditions | Min  | Typ | Max | Unit |
|----------|------------------------------------------|------------|------|-----|-----|------|
| T(J) | Junction temperature                   | –          | -40  | –   | 125 | °C   |
| V(SYS) | System supply voltage                | –          | 2.7  | –   | 5.5 | V    |
| P(DIS) | Maximum chip power dissipation       | –          | –    | –   | 2   | W    |
| R(JA) | Junction-to-ambient thermal resistance | –        | –    | 38  | –   | °C/W |
| R(JC) | Junction-to-case thermal resistance    | –        | –    | 12  | –   | °C/W |
| R(JB) | Junction-to-board thermal resistance   | –        | –    | 9   | –   | °C/W |

### 5.2 Power Consumption in Different Modes

The power consumption in different operating modes is shown below.

| Description        | Conditions             | Min | Typ | Max | Unit |
|--------------------|------------------------|-----|-----|-----|------|
| RESET mode         | –                      | –   | –   | –   | μA   |
| RTC mode           | V(IN)=5 V, T(A)=25 °C | – | 2 | – | μA |
| Shutdown mode      | V(IN)=5 V, T(A)=25 °C | – | 40 | – | μA |
| Active mode        | –                      | –   | –   | –   | μA   |
| Sleep mode         | –                      | –   | –   | –   | μA   |

### 5.3 Digital I/O Electrical Characteristics

The digital I/O electrical characteristics are listed below.

| Parameter | Description          | Conditions                                                                 | Min              | Typ              | Max             | Unit |
|----------|----------------------|----------------------------------------------------------------------------|------------------|------------------|------------------|------|
| V(IH) | Input high voltage | 2.7–5.5 V, -40 to 105 °C                                                    | –                | –                | 0.3 × AONLDO     | V    |
| V(IL) | Input low voltage  | 2.7–5.5 V, -40 to 105 °C                                                    | 0.7 × AONLDO     | –                | –                | V    |
| V(OH) | Output high voltage | 5 V, 25 °C<br/>AONLDO = 1.8 V, I(LOAD) = 1 mA                      | –                | AONLDO − 0.1     | –                | V    |
| V(OL) | Output low voltage  | 5 V, 25 °C<br/>AONLDO = 1.8 V, I(LOAD) = 1 mA                      | –                | 0.1              | –                | V    |
| I(DRIVE) | Source drive current | 5 V, 25 °C<br/>AONLDO = 1.8 V, PAD = 1.3 V                                | –                | 10               | –                | mA   |
| I(SINK)  | Sink drive current   | 5 V, 25 °C<br/>AONLDO = 1.8 V, PAD = 0.5 V                                | –                | 25               | –                | mA   |
| R(PU) | Weak pull-up resistor   | –                                                                          | –                | 20 k             | –                | Ω    |
| R(PD) | Weak pull-down resistor | –                                                                          | –                | 20 k             | –                | Ω    |

### 5.4 Watchdog Timer

The watchdog timer characteristics are listed below.

| Parameter | Description                   | Conditions | Min | Typ | Max | Unit |
|----------|-------------------------------|------------|-----|-----|-----|------|
| T(WD_MIN) | Minimum watchdog timeout | –          | –   | 1   | –   | s    |
| T(WD_MAX) | Maximum watchdog timeout | –          | –   | 16  | –   | s    |

### 5.5 LDO Characteristics

#### 5.5.1 AONLDO

The electrical characteristics of the AONLDO are listed in the table below.

| Parameter | Description | Conditions | Min | Typ | Max | Unit |
|----------|-------------|------------|-----|-----|-----|------|
| V(DD) | Input voltage range | V(IN) = V(SYS) | 2.7 | – | 5.5 | V |
| V(LDO) | Output voltage range | – | 0.5 | – | 3.4 | V |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) > 1.2 V) | – | – | – | ±1 | % |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) < 1.2 V) | – | – | – | ±12 | mV |
| I(OUT_MAX) | Output current | – | – | – | 0.2 | A |
| I(OCP) | Overcurrent protection | – | – | 0.3 | – | A |
| I(SHORT) | Short-circuit current | – | – | 0.15 | – | A |
| V(DROPOUT) | Dropout voltage | V(OUT) = 1.8 V, I(OUT) = I(OUT_MAX) | – | 0.3 | – | V |
| V(S_LINE) | Line regulation | V(IN) = 3 to 5 V | – | 10 | – | mV |
| V(S_LOAD) | Load regulation | I(LOAD) = 10 to 100 mA | – | 15 | – | mV |
| PSRR | Power supply rejection ratio | I(OUT) = I(MAX)/2, V(IN) − V(OUT) > 1 V | – | 60 | – | dB |
| Noise | Output noise (V(OUT) = 1.8 V) | V(OUT) = 1.8 V, I(OUT) = 5 mA to I(MAX) | – | 35 | – | µV(RMS) |
| Noise | Output noise (V(OUT) = 2.5 V) | V(OUT) = 2.5 V, I(OUT) = 5 mA to I(MAX) | – | 35 | – | µV(RMS) |
| I(Q_ON) | Quiescent current (ON mode) | – | – | 15 | – | µA |
| R(OFF) | Pull-down resistance (OFF mode) | – | – | 160 | – | Ω |
| OV | Overvoltage threshold | V(OUT)/V(OUT_TARGET) − 1 | – | 20 | – | % |
| UV | Undervoltage threshold | 1 − V(OUT)/V(OUT_TARGET) | – | 15 | – | % |

#### 5.5.2 ALDO1 ~ ALDO4

The electrical characteristics of ALDO1 ~ ALDO4 are listed below.

| Parameter | Description | Conditions | Min | Typ | Max | Unit |
|----------|-------------|------------|-----|-----|-----|------|
| V(DD) | Input voltage range | V(IN) = V(SYS) | 2.7 | – | 5.5 | V |
| V(LDO) | Output voltage range | – | 0.5 | – | 3.4 | V |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) > 1.2 V) | V(OUT) > 1.2 V | – | – | ±1 | % |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) < 1.2 V) | V(OUT) < 1.2 V | – | – | ±12 | mV |
| I(OUT_MAX) | Output current | – | – | – | 0.3 | A |
| I(OCP) | Overcurrent protection | – | – | 0.5 | – | A |
| I(SHORT) | Short-circuit current | – | – | 0.25 | – | A |
| V(DROPOUT) | Dropout voltage | V(IN) = 2.0 V, I(OUT) = I(OUT_MAX) | – | 0.3 | – | V |
| V(S_LINE) | Line regulation | V(IN) = 3 to 5 V | – | 10 | – | mV |
| V(S_LOAD) | Load regulation | I(LOAD) = 10 to 100 mA | – | 15 | – | mV |
| PSRR | Power supply rejection ratio | I(OUT) = I(MAX)/2, V(IN) − V(OUT) > 1 V | – | 70 | – | dB |
| Noise | Output noise (V(OUT) = 1.8 V) | V(OUT) = 1.8 V, I(OUT) = 5 mA to I(MAX) | – | 30 | – | µV(RMS) |
| Noise | Output noise (V(OUT) = 2.5 V) | V(OUT) = 2.5 V, I(OUT) = 5 mA to I(MAX) | – | 30 | – | µV(RMS) |
| I(Q_ON) | Quiescent current (ON mode) | – | – | 15 | – | µA |
| R(OFF) | Pull-down resistance (OFF mode) | – | – | 160 | – | Ω |
| OV | Overvoltage threshold | V(OUT)/V(OUT_TARGET) − 1 | – | 20 | – | % |
| UV | Undervoltage threshold | 1 − V(OUT)/V(OUT_TARGET) | – | 15 | – | % |

#### 5.5.3 DLDO1/2/3/5/6

The electrical characteristics of DLDO1/2/3/5/6 (i.e., DLDO1, DLDO2, DLDO3, DLDO5, and DLDO6) are shown below.

| Parameter | Description | Conditions | Min | Typ | Max | Unit |
|----------|-------------|------------|-----|-----|-----|------|
| V(DD) | Input voltage range (V(IN) = V(SYS)) | V(IN) = V(SYS) | 2.7 | – | 5.5 | V |
| V(DD) | Input voltage range (buck-supplied) | Buck output used as V(IN) | 2.1 | – | – | V |
| V(LDO) | Output voltage range | – | 0.5 | – | 3.4 | V |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) > 1.2 V) | V(OUT) > 1.2 V | – | – | ±1 | % |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) < 1.2 V) | V(OUT) < 1.2 V | – | – | ±12 | % |
| I(OUT_MAX) | Output current | – | – | – | 0.3 | A |
| I(OCP) | Overcurrent protection | – | – | 0.5 | – | A |
| I(SHORT) | Short-circuit current | – | – | 0.25 | – | A |
| V(DROPOUT) | Dropout voltage | V(IN) = 2.1 V, I(OUT) = I(OUT_MAX) | – | 0.3 | – | V |
| V(S_LINE) | Line regulation | V(IN) = 3 to 5 V | – | 10 | – | mV |
| V(S_LOAD) | Load regulation | I(LOAD) = 10 to 100 mA | – | 15 | – | mV |
| PSRR | Power supply rejection ratio | I(OUT) = I(MAX)/2, V(IN) − V(OUT) > 1 V | – | 60 | – | dB |
| Noise | Output noise (V(OUT) = 1.8 V) | V(OUT) = 1.8 V, I(OUT) = 5 mA to I(MAX) | – | 35 | – | µV(RMS) |
| Noise | Output noise (V(OUT) = 2.5 V) | V(OUT) = 2.5 V, I(OUT) = 5 mA to I(MAX) | – | 35 | – | µV(RMS) |
| I(Q_ON) | Quiescent current (ON mode) | – | – | 15 | – | µA |
| R(OFF) | Pull-down resistance (OFF mode) | – | – | 160 | – | Ω |
| OV | Overvoltage threshold | V(OUT)/V(OUT_TARGET) − 1 | – | 20 | – | % |
| UV | Undervoltage threshold | 1 − V(OUT)/V(OUT_TARGET) | – | 15 | – | % |

#### 5.5.4 DLDO4 / DLDO7

The electrical characteristics of DLDO4 / DLDO7 are listed below.

| Parameter | Description | Conditions | Min | Typ | Max | Unit |
|----------|-------------|------------|-----|-----|-----|------|
| V(DD) | Input voltage range (V(IN) = V(SYS)) | V(IN) = V(SYS) | 2.7 | – | 5.5 | V |
| V(DD) | Input Voltage Range (from Buck input voltage V(IN)) | Buck output used as V(IN) | 2.1 | – | – | V |
| V(LDO) | Output voltage range | – | 0.5 | – | 3.4 | V |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) > 1.2 V) | V(OUT) > 1.2 V | – | – | ±1 | % |
| V(LDO_ACC) | Output voltage accuracy (V(OUT) < 1.2 V) | V(OUT) < 1.2 V | – | – | ±12 | % |
| I(OUT_MAX) | Output current | – | – | – | 0.5 | A |
| I(OCP) | Overcurrent protection | – | – | 0.8 | – | A |
| I(SHORT) | Short-circuit current | – | – | 0.4 | – | A |
| V(DROPOUT) | Dropout voltage | V(IN) = 2.1 V, I(OUT) = I(OUT_MAX) | – | 0.4 | – | V |
| V(S_LINE) | Line regulation | V(IN) = 3 to 5 V | – | 10 | – | mV |
| V(S_LOAD) | Load regulation | I(LOAD) = 10 to 100 mA | – | 15 | – | mV |
| PSRR | Power supply rejection ratio | I(OUT) = I(MAX)/2, V(IN) − V(OUT) > 1 V | – | 60 | – | dB |
| Noise | Output noise (V(OUT) = 1.8 V) | V(OUT) = 1.8 V, I(OUT) = 5 mA to I(MAX) | – | 35 | – | µV(RMS) |
| Noise | Output noise (V(OUT) = 2.5 V) | V(OUT) = 2.5 V, I(OUT) = 5 mA to I(MAX) | – | 35 | – | µV(RMS) |
| I(Q_ON) | Quiescent current (ON mode) | – | – | 15 | – | µA |
| R(OFF) | Pull-down resistance (OFF mode) | – | – | 160 | – | Ω |
| OV | Overvoltage threshold | V(OUT)/V(OUT_TARGET) − 1 | – | 20 | – | % |
| UV | Undervoltage threshold | 1 − V(OUT)/V(OUT_TARGET) | – | 15 | – | % |

### 5.6 BUCK 1 ~ 6

The electrical characteristics of BUCK1–BUCK6 are listed in the tables below.

#### General Buck Parameters

| Parameter        | Description                         | Conditions                                              | Min | Typ             | Max | Unit  |
|------------------|-------------------------------------|----------------------------------------------------------|-----|------------------|-----|-------|
| V(IN_MIN)  | Minimum input voltage               | –                                                        | –   | 2.7              | –   | V     |
| V(IN_MAX)  | Maximum input voltage               | –                                                        | –   | 5.5              | –   | V     |
| V(OUT_MIN) | Minimum output voltage              | –                                                        | –   | 0.5              | –   | V     |
| V(OUT_MAX) | Maximum output voltage              | –                                                        | –   | 3.4              | –   | V     |
| V(OUT_STEPS) | Output voltage step size           | V(OUT) = 0.5 ~ 1.35 V                            | –   | 5                | –   | mV    |
| V(OUT_STEPS) | Output voltage step size           | V(OUT) = 1.35 ~ 3.4 V                            | –   | 25               | –   | mV    |
| V(SLEW)     | DVS slew rate options               | –                                                        | –   | 5 / 10 / 25 / 50 | –   | mV/µs |
| T(SFST)     | Soft-start time                     | –                                                        | –   | 1                | –   | ms    |
| T(SFST_SET) | Soft-start time setting options     | –                                                        | –   | 0.78 / 0.9 / 1.12| –   | ms    |
| R(DIDCHG)   | Discharge resistor                  | –                                                        | –   | 45               | –   | Ω     |
| f(SW)       | Switching frequency                 | CCM                                                      | –   | 1.5              | –   | MHz   |
| OV               | Over-voltage threshold               | V(OUT)/V(OUT_TARGET) − 1               | –   | 20               | –   | %     |
| UV               | Under-voltage threshold              | 1 − V(OUT)/V(OUT_TARGET)               | –   | 15               | –   | %     |
| V(BUCK_ACC) | Output voltage accuracy             | Excluding line/load regulation, V(OUT) > 1 V   | –   | –                | ±1  | %     |
| V(BUCK_ACC) | Output voltage accuracy             | Excluding line/load regulation, V(OUT) < 1 V   | –   | –                | ±10 | mV    |
| V(S_LOAD)   | Static load regulation              | I(OUT) = 0.1 ~ 2 A, V(OUT) = 1 V       | –   | –                | ±1  | %     |
| V(S_LINE)   | Static line regulation              | V(IN) = 3 ~ 5 V, V(OUT) = 1 V         | –   | –                | ±1  | %     |
| V(TR_LD)    | Load transient response; C(OUT)=44uF, I(OUT)=0.02 ~ 2.7 A | (undershoot，V(OUT)< 1.2 V) | –   | 30               | 60  | mV    |
|             | Undershoot                           | (undershoot，V(OUT)< 1.2 V) V                                  | –   | 3                | 5   | %     |
|             | Overshoot                            | (overshoot，V(OUT) < 1.6 V)                                  | –   | 72               | 80  | mV    |
|             | Overshoot                            | (overshoot，V(OUT) < 1.6 V)                                  | –   | –                | 5   | %     |
| V(RIPPLE)   | Output ripple; I(OUT) = 0.1 A, V(OUT) = 1.1 V |   –     | –   | 13               | 25  | mV    |
| V(RIPPLE)   | Output ripple; I(OUT) > 1 A, V(OUT) = 1.1 V   |   –    | –   | 7                | 20  | mV    |

#### Buck 1 ~ 2 (Single Buck)

| Parameter      | Description              | Conditions                                           | Min | Typ  | Max  | Unit |
|----------------|--------------------------|------------------------------------------------------|-----|------|------|------|
| I(OUT_MAX) | Output current          | OCP large = 1                                       | –   | 4.0  | –    | A    |
| Efficiency     | Efficiency               | V(IN) = 4 V, V(OUT) = 0.9 V, I(OUT) = 0.5 A | – | 86.3 | – | % |
| Efficiency     | Efficiency               | V(IN) = 4 V, V(OUT) = 0.9 V, I(OUT) = 2.5 A | – | 78.2 | – | % |
| D(ACC)     | Dual-phase current accuracy | I(OUT) = 6 A                               | –   | 10.0 | 20.0 | %    |
| R(PU)      | Pull-up resistance      | V(IN) = 4 V                                 | –   | 80   | –    | mΩ   |
| R(PD)      | Pull-down resistance    | V(IN) = 4 V                                 | –   | 40   | –    | mΩ   |

#### Buck 3 ~ 4

| Parameter           | Description              | Conditions                                           | Min | Typ  | Max  | Unit |
|---------------------|--------------------------|------------------------------------------------------|-----|------|------|------|
| I(OUT_MAX)| Output current           | –                                                    | 2.5 | 3.5  | –    | A    |
| I(VALLEY_LIMIT) | Valley current limit     | –                                                    | 3.0 | –    | –    | A    |
| Efficiency          | Efficiency               | V(IN) = 4 V, V(OUT) = 1.8 V, I(OUT) = 0.5 A | – | 90.6 | – | % |
| Efficiency          | Efficiency               | V(IN) = 4 V, V(OUT) = 1.8 V, I(OUT) = 2.5 A | – | 83.4 | – | % |
| D(ACC)          | Dual-phase current accuracy | I(OUT) = 5 A                               | –   | –    | 20.0 | %    |
| R(PU)           | Pull-up resistance      | V(IN) = 4 V                                 | –   | 100  | –    | mΩ   |
| R(PD)           | Pull-down resistance    | V(IN) = 4 V                                 | –   | 50   | –    | mΩ   |

#### Buck 5 ~ 6

| Parameter           | Description              | Conditions                                           | Min | Typ  | Max | Unit |
|---------------------|--------------------------|------------------------------------------------------|-----|------|-----|------|
| I(OUT_MAX)| Output current           | –                                                    | 2.5 | –    | –   | A    |
| I(VALLEY_LIMIT) | Valley current limit     | –                                                    | 3.0 | –    | –   | A    |
| Efficiency          | Efficiency               | V(IN) = 4 V, V(OUT) = 1.1 V, I(OUT) = 0.5 A | – | 87.7 | – | % |
| Efficiency          | Efficiency               | V(IN) = 4 V, V(OUT) = 1.1 V, I(OUT) = 2.5 A | – | 79.9 | – | % |
| Efficiency          | Efficiency               | V(IN) = 4 V, V(OUT) = 2.1 V, I(OUT) = 0.5 A | – | 91.6 | – | % |
| Efficiency          | Efficiency               | V(IN) = 4 V, V(OUT) = 2.1 V, I(OUT) = 2.5 A | – | 86.8 | – | % |
| R(PU)           | Pull-up resistance      | V(IN) = 4 V                                 | –   | 100  | –   | mΩ   |
| R(PD)           | Pull-down resistance    | V(IN) = 4 V                                 | –   | 50   | –   | mΩ   |

### 5.7 Load Switch

The electrical characteristics of the load switch are listed in the table below.

| Parameter      | Description               | Conditions        | Min | Typ | Max | Unit |
|----------------|---------------------------|-------------------|-----|-----|-----|------|
| SW(IN_MIN) | Minimum input voltage    | V(SYS) = 4 V | –   | 2.7 | –   | V    |
| SW(IN_MAX) | Maximum input voltage    | V(SYS) = 4 V | –   | 5.5 | –   | V    |
| R(ON)      | On-resistance            | SWIN = 5 V        | –   | 140 | –   | mΩ   |
| I_SC       | Short-circuit current    | –                 | –   | 0.5 | –   | A    |
| I_MAX      | Maximum output current   | –                 | –   | 1.6 | –   | A    |

### 5.8 ADC

#### ADC Electrical Characteristics

| Parameter        | Description            | Conditions                     | Min | Typ | Max | Unit |
|------------------|------------------------|--------------------------------|-----|-----|-----|------|
| Resolution       | Resolution             | –                              | –   | 12  | –   | Bits |
| V(DD)   | Supply voltage         | –                              | 2.7 | –   | 5.5 | V    |
| DNL              | Differential nonlinearity | 2.7 ~ 5.5 V, −40 ~ 105 °C     | −3  | –   | 3   | LSB  |
| INL              | Integral nonlinearity   | 2.7 ~ 5.5 V, −40 ~ 105 °C     | −4  | –   | 4   | LSB  |
| Offset error     | Offset error            | 2.7 ~ 5.5 V, −40 ~ 105 °C     | −4  | –   | 4   | LSB  |
| Gain error       | Gain error              | 2.7 ~ 5.5 V, −40 ~ 105 °C     | −4  | –   | 4   | LSB  |
| Sample rate      | Sampling rate           | 25 °C                          | 0.1 | –   | 25  | kSPS |
| I(WORK) | Operating current       | 5 V, 25 °C                    | –   | 190 | –   | µA   |

#### ADC Internal Reference Electrical Characteristics

| Parameter        | Description              | Conditions                 | Min   | Typ | Max   | Unit |
|------------------|--------------------------|----------------------------|-------|-----|-------|------|
| V(REF_2V) | 2 V reference voltage    | 2.7 ~ 5.5 V, 25 °C         | 1.995 | 2.0 | 2.005 | V    |
| V(REF_3V) | 3 V reference voltage    | 3.5 ~ 5.5 V, 25 °C         | 2.995 | 3.0 | 3.005 | V    |
| I(WORK)   | Operating current        | 5.0 V, −40 ~ 105 °C       | –     | 400 | –     | µA   |

### 5.9 Internal Clocks

#### Internal LSI Electrical Characteristics

| Parameter     | Description              | Conditions                    | Min | Typ | Max | Unit |
|---------------|--------------------------|-------------------------------|-----|-----|-----|------|
| F(ACC) | Frequency accuracy       | 5 V, 25 °C                   | 30  | 32  | 34  | kHz  |
| V(C)   | Voltage coefficient      | 2.0 ~ 5.5 V, 25 °C           | −5  | –   | 2   | %    |
| T(C)   | Temperature coefficient  | 5 V, −40 ~ 105 °C            | 0   | –   | 5   | %    |
| I(WORK) | Operating current        | 2.0 ~ 5.5 V, −40 ~ 105 °C    | 0.4 | 0.9 | 1.5 | µA   |

#### Internal HSI Electrical Characteristics

| Parameter     | Description              | Conditions                    | Min | Typ | Max | Unit |
|---------------|--------------------------|-------------------------------|-----|-----|-----|------|
| F(ACC) | Frequency accuracy       | 5 V, 25 °C                   | 1.98 | 2.00 | 2.02 | MHz  |
| V(C)   | Voltage coefficient      | 2.0 ~ 5.5 V, 25 °C           | −0.2 | –   | 0.2 | %    |
| T(C)   | Temperature coefficient  | 5 V, −40 ~ 105 °C            | −2  | –   | 2   | %    |
| I(WORK) | Operating current        | 2.0 ~ 5.5 V, −40 ~ 105 °C    | 45  | 80  | 120 | µA   |

### 5.10 32 kHz Crystal Oscillator

The electrical characteristics of the 32 kHz crystal oscillator are listed in the table below.

| Parameter     | Description                | Conditions                         | Min | Typ  | Max | Unit |
|---------------|----------------------------|------------------------------------|-----|------|-----|------|
| C(LOAD) | External load capacitance | 2.7 ~ 5.5 V, −40 ~ 105 °C          | 7   | 22.5 | 30  | pF   |
| I(WORK) | Operating current         | 5 V, 25 °C, C(LOAD) = 12.5 pF | –   | 1    | –   | µA   |
| T(SETUP) | Startup time             | 5 V, 25 °C                         | –   | 0.6  | –   | s    |

### 5.11 POR / PDR

The electrical characteristics of the Power-On Reset (POR) and Power-Down Reset (PDR) are listed below.

| Parameter        | Description                         | Conditions                   | Min  | Typ | Max  | Unit |
|------------------|-------------------------------------|------------------------------|------|-----|------|------|
| POR              | Power-on reset voltage              | −40 ~ 105 °C                 | 1.75 | 2.0 | 2.25 | V    |
| PDR              | Power-down reset voltage            | −40 ~ 105 °C                 | 1.75 | 2.0 | 2.25 | V    |
| T(FILTER) | POR glitch filter duration          | 25 °C, 3 V → 1.5 V           | –    | 2.0 | –    | µs   |
| I(WORK)   | Operating current                   | 2.0 ~ 5.5 V, −40 ~ 105 °C    | 0.1  | 0.3 | 1.0  | µA   |

### 5.12 RTC Module POR / PDR

The electrical characteristics of the RTC power-on and power-down reset are listed below.

| Parameter     | Description                | Conditions                   | Min  | Typ | Max  | Unit |
|---------------|----------------------------|------------------------------|------|-----|------|------|
| POR           | Power-on reset voltage     | −40 ~ 105 °C                 | 1.55 | 1.7 | 1.85 | V    |
| PDR           | Power-down reset voltage   | −40 ~ 105 °C                 | 1.55 | 1.7 | 1.85 | V    |
| I(WORK) | Operating current          | 2.0 ~ 5.5 V, −40 ~ 105 °C    | 0.1  | 0.3 | 1.0  | µA   |

## 6. Functional Description

P1 is a low-voltage, multi-channel Power Management IC (PMIC). It integrates six fast transient-response BUCK converters and twelve low-noise LDO regulators. An internal MTP (Multi-Time Programmable) memory is provided, allowing flexible configuration of default output voltages and power-up/power-down sequencing for each rail. This enables the PMIC to meet the power sequencing requirements of different SoC platforms and application scenarios.

### 6.1 Power Management Pins

The power management pins are described in the table below.

| Pin            | Power Domain | Description |
|----------------|--------------|-------------|
| PWRKY      | VSYS         | Power key control pin. Also functions as a PMIC reset button. Supports shutdown, short-press, long-press, rising-edge, and falling-edge interrupt functions. |
| INT        | Open-Drain   | Interrupt output pin. Supports pull-down on INT to power on the PMIC. |
| PGOOD      | Open-Drain   | - Input: Detects release of the PGOOD pin and can be used as a reset source.<br>- Output: Pulled low during PMIC shutdown or reset to reset the SoC. |
| PWRCTRL    | AONLDO       | GPIO-multiplexed input used to control power-on/power-off, sleep, and wake-up sequences. |
| SLEEP/WKUP | AONLDO       | GPIO-multiplexed input used to control sleep or wake-up operations. |
| nRESET     | AONLDO       | GPIO-multiplexed input used as a reset source (power-off followed by restart). |
| EXT_EN     | AONLDO       | GPIO-multiplexed output used for coordination with external PMICs or power devices. |
| VSET5      | VSYS         | Voltage selection control pin for BUCK5 output levels. |
| VSET6      | VSYS         | Voltage selection control pin for BUCK6 output levels. |
| OUT_32K    | AONLDO       | Output pin for the internal low-speed clock or external crystal clock. |

#### 6.1.1 PWRKY Pin

The PWRKY pin is internally pulled up to VSYS and provides multiple functions:

- Acts as power-on, power-off, and reset source
- Generates multiple interrupt events including shutdown, short press, long press, rising edge, and falling edge interrupts

1. PWRKY Behavior in Shutdown Mode

   - Power-on Function
     - Pulling the PWRKY pin low for a specified time triggers the power-on sequence.
   - Duration is configurable to 0.5s / 1s / 2s / 3s (see Table 7-91 PWR_KEY_TIME[1:0]).

   - Long-Press Shutdown Function
     - If long-press shutdown is enabled (SYS_CFG1[0]=1, Table 7-126), PWRKY must be held low until exiting shutdown mode.
   - After exiting shutdown mode, if PWRKY remains low longer than 4s / 6s / 8s / 10s (configured via PWR_KEY_TIME[3:2] in Table 7-91), a shutdown is triggered.

2. PWRKY Behavior in Non-Shutdown Mode

   - Power-off Function
     - PWRKY can act as a shutdown source (PWR_CTRL2[6]=0, Table 7-88).
   - Pulling low for a configured duration triggers shutdown. Time configurable to 4s / 6s / 8s / 10s (Table 7-91 PWR_KEY_TIME[3:2]).

    - Long-Press Reset Function
       - When configured as a long-press reset source (PWR_CTRL2[6]=1), holding PWRKY low for 12s triggers a PMIC cold reset.
     - Cold reset clears all logic and module configurations (including RTC), equivalent to a power-on reset.

   - Long-Press Reset Combined with Shutdown
     - If long-press reset is enabled (SYS_CFG1[1]=1, Table 7-126), PWRKY held low in shutdown mode continues until exit.
   - After exiting shutdown, if still low for over 12s, a cold reset is triggered.

3. Interrupt Events in Power-On or Sleep Mode

   - Falling Edge Event
     - Pulling PWRKY low generates a falling edge event.
   - If enabled (IRQ_PWRKY_EN[4], Table 7-120), triggers a falling edge interrupt.

   - Rising Edge Event
      - Releasing PWRKY after a low pulse generates a rising edge event.
         - If enabled (IRQ_PWRKY_EN[0]), triggers a rising edge interrupt.

   - Short Press Event
     - Pulling low then releasing within the short-press time generates a short press event.
   - If enabled (IRQ_PWRKY_EN[2]), triggers a short-press interrupt.
   - Duration configurable to 0.5s / 1s / 1.5s / 2s (Table 7-91 PWR_KEY_TIME[5:4]).

   - Long Press Event
     - Pulling low then releasing with duration between short-press and shutdown triggers a long press event.
   - If enabled (IRQ_PWRKY_EN[3]), triggers a long-press interrupt.

PWRKY Event Timing Diagrams

   - Power-On Mode Events
   ![](static/YA21bY2dBoZiMmx6lAhc69klnNc.png)

   - Shutdown Mode Events
   ![](static/ZpJkbaNCmorgpVxLrEScWBmznNf.png)


#### 6.1.2 INT Pin

The INT pin is an open-drain output with an internal Schmitt-trigger input operating at AONLDO voltage.

- Shutdown Mode
   - When configured as a power-on source (PWR_CTRL0[2]=1, Table 7-86), pulling the INT pin low for 16 ms triggers the power-on sequence.

- Power-On Mode
  - During normal operation, when an internal event occurs and the corresponding interrupt is enabled (e.g., key press event), the INT pin is pulled low to output the interrupt signal.

#### 6.1.3 PGOOD Pin

The PGOOD pin is an open-drain output with an internal Schmitt-trigger input operating at AONLDO voltage.

- Shutdown Process or Shutdown Mode
  - During shutdown or shutdown mode, the PMIC pulls the PGOOD pin low to reset external modules.
  - In shutdown mode, PGOOD remains low at all times.

- End of Power-On Sequence
  - Once the power-on sequence completes, the PMIC immediately releases the PGOOD pin.
  - If PWR_CTRL1[3]=0 (Table 7-87), the chip enters power-on mode directly.
  - If PWR_CTRL1[3]=1, the chip waits until PGOOD goes high before entering power-on mode.
  - If this wait times out, the chip immediately enters shutdown, and all powered rails are turned off.

- Power-On Mode
   - In normal operation, if PGOOD is pulled low for more than 200 µs and PGOOD pull-down reset is enabled (`PG_RST_EN`), a reset sequence is triggered (shutdown followed by power-on).

- Sleep Mode and Sleep Sequence
  - The PGOOD state during sleep can be configured via PWR_CTRL1[5] (Table 7-87). By default, PGOOD remains high.

- End of Wake-Up Sequence
  - After wake-up, the PMIC immediately releases PGOOD and enters power-on mode.

#### 6.1.4 PWRCTRL Pin

The PWRCTRL pin features a GPIO-multiplexed input function with an internal Schmitt-trigger operating at AONLDO voltage.

The PWRCTRL pin is primarily used to control power-on, power-off, sleep, and wake-up sequences:

- Power-On Event
  - In shutdown mode, the power-on sequence is triggered by the PWRCTRL pin when the following conditions are met:
   - All BUCKs and LDOs, except AONLDO, are bound to the PWRCTRL pin.
    - Full binding power-on functionality is enabled (PWR_CTRL0[4]=1, Table 7-86).

- Power-Off Event
   - In non-shutdown mode, the power-off sequence is triggered when the PWRCTRL pin is inactive, if the following conditions are met:
    - All BUCKs and LDOs are bound to the PWRCTRL pin.
    - Full binding power-off functionality is enabled (PWR_CTRL0[5]=1, Table 7-86).

- Power-On and Wake-Up Sequences
  - When a BUCK or LDO is bound to the PWRCTRL pin:
   - If the PWRCTRL pin is active, the power-on or wake-up sequence proceeds to enable the corresponding BUCK or LDO.
   - If the PWRCTRL pin is inactive, the sequence pauses until the pin becomes active.

- Sleep Sequence
  - When a BUCK or LDO is bound to PWRCTRL:
    - If reverse sleep is configured (PWR_CTRL1[1]=1, Table 7-87) and wait-for-PWRCTRL is enabled (PWR_CTRL2[4]=1, Table 7-88), the sleep operation waits until PWRCTRL is inactive.
    - If the wait time exceeds PWR_CTRL2[5] (Table 7-88), the BUCK or LDO is forced into sleep, and the sequence continues into sleep mode.

- Power-Off Sequence
  - When a BUCK or LDO is bound to PWRCTRL:
    - If reverse power-off is configured (PWR_CTRL1[0]=0, Table 7-87) and wait-for-PWRCTRL is enabled (PWR_CTRL2[4]=1, Table 7-88), the shutdown waits for the PWRCTRL pin to become inactive.
    - If the wait time exceeds PWR_CTRL2[5], the BUCK or LDO is forced off, and the shutdown sequence continues.

- Power-On Mode
  - If a BUCK or LDO is bound to PWRCTRL:
    - When PWRCTRL is inactive, the associated BUCK or LDO is turned off.
    - When PWRCTRL is active and the BUCK or LDO enable bit is set, the corresponding BUCK or LDO is turned on.

The active polarity of the PWRCTRL pin can be configured via the `GPIOx_ODR` register.

#### 6.1.5 SLEEP/WKUP Pin

The SLEEP/WKUP pin features a GPIO-multiplexed input function with an internal Schmitt-trigger operating in the AONLDO voltage domain.

This pin is used to control entering and exiting sleep mode with the following behavior:

1. Power-On Mode: When the SLEEP/WKUP pin is active, the sleep sequence is executed, and the device enters sleep mode.
2. Sleep Mode: When the SLEEP/WKUP pin is inactive, the wake-up sequence is executed, and the device returns to power-on mode.

The active polarity of the SLEEP/WKUP pin can be configured via the GPIO_ODR register (Table 7-5).

#### 6.1.6 nRESET Pin

The nRESET pin is a GPIO-multiplexed input with an internal Schmitt-trigger operating in the AONLDO voltage domain.

1. In Non-Shutdown Mode:

    - If nRESET reset is enabled (PWR_CTRL0[6]=1, Table 7-86), a transition of the nRESET pin from inactive to active lasting longer than 250 μs triggers the reset sequence (power-off followed by power-on).
    - If GPIO filtering is enabled, the nRESET reset trigger time is extended by the filter delay as follows:  
       250 μs + (filter configuration value from Table 7-8 GPIO_DEB_EN[7:6]).

2. After Reset Sequence Triggered:

   - If the nRESET pin remains active, the system will not re-trigger a reset.
   - A new reset can only be triggered after the nRESET pin is released (returns to inactive).

The active polarity of the nRESET pin can be configured via the GPIO_ODR register (Table 7-5).

#### 6.1.7 EXT_EN Pin

The EXT_EN pin is a multiplexed GPIO output with an internal Schmitt-trigger operating in the AONLDO voltage domain.

Its behavior is controlled by the power-on, power-off, sleep, and wake-up sequences, as described in the corresponding registers and power sequence sections. The detailed logic is as follows:

1. Power-On and Wake-Up Sequences

    - When EXT_EN is bound to a specific timing slot (SLOT) via PWR_SLOT9 ~ PWR_SLOT11 (Tables 7-102 ~ 7-104):  
       - The corresponding EXT_EN output operates only when the sequence reaches that SLOT.

2. Sleep Sequence

    - When EXT_EN is bound to a SLOT:  
       - The output is disabled only when the sequence reaches that SLOT and it is configured as controlled by sleep timing (PWR_EXT_CTRL[5:0], Table 7-106).

3. Power-Off Sequence

    - When EXT_EN is bound to a SLOT via PWR_SLOT9 ~ PWR_SLOT11 (Tables 7-102 ~ 7-104):  
     - The output is disabled only when the sequence reaches that SLOT.

4. Power-On Mode

   - Controlled by PWR_EXT_EN (Table 7-104).

5. Sleep Mode

   - Controlled jointly by PWR_EXT_EN (Table 7-104) and PWR_EXT_CTRL (Table 7-106).

The active polarity of the EXT_EN pin can be configured via the GPIO_ODR register (Table 7-5).

The table below summarizes EXT_EN output control across different modes:

| (x = 0 ~ 5)     | Power-On Sequence | Power-On Mode | Sleep Sequence | Sleep Mode | Wake-Up Sequence | Power-Off Sequence | Power-Off Mode |
|-----------------|-----------------|---------------|----------------|------------|-----------------|------------------|----------------|
| EXTx_EN         | x               | x             | -              | x          | x               | -                | -              |
| EXTx_EN_SLOT    | x               | -             | x              | -          | x               | x                | -              |
| EXTx_SLP_SD     | -               | -             | x              | x          | -               | -                | -              |

#### 6.1.8 VSET5 / VSET6 Pins

The VSET5 and VSET6 pins configure the output voltage of BUCK5 and BUCK6, respectively, based on their state (GND, VSYS, or FLOAT) to support different application scenarios.

VSET Voltage Control Logic

| BUCK_LDO_CFG[2] (Table 7-74) | VDD   | FLOAT                     | GND   |
|-------------------------------|-------|---------------------------|-------|
| 0                             | 1.1 V | VBUCKx_VOLT (x=5/6)       | 1.2 V |
| 1                             | 0.6 V | VBUCKx_VOLT (x=5/6)       | 1.5 V |

#### 6.1.9 OUT_32K Pin

The OUT_32K pin provides an output of the internal slow clock or crystal oscillator clock, configurable via the RTC_CTRL[3] register (Table 7-33).

1. Clock Output Control:

   - Can be pre-configured via MTP to operate in clock output mode.
   - Provides a clock source to external modules even before the power-on sequence begins.

2. Impact of Power States:

   - Normal Operating Mode: Clock output remains active.
   - Power-Off Mode: Clock output is disabled.


### 6.2 Operating Modes

The system supports five operating modes: RESET, RTC, Shutdown, Active, and Sleep. Mode transitions are triggered by various events including power-on, power-off, reset, sleep, and wake-up events. The following diagram illustrates the mode transition states:

![](static/VZFIbb6v7oKNUhx7IwZcN8PTnig.png)

#### 6.2.1 Reset Mode

- When VSYS < 2.7V, the PMIC enters Reset Mode and all functions are halted.
- The system exits Reset Mode and starts normal operation only when VSYS ≥ 2.7V.
- If VSYS drops below 2.55V during operation, the system immediately returns to Reset Mode.

#### 6.2.2 RTC Mode

Ultra-low power mode, maintaining only the RTC module and oscillator to preserve timekeeping.

Entry Conditions:

- VSYS < 2.0V (no main power)
- VBAT > 2.0V (battery supply available)

Exit Conditions:

- Same as Reset Mode: VSYS ≥ 2.7V (power-on reset released)

#### 6.2.3 Shutdown Mode

Most modules are powered down. Active modules include: AONLDO, Bandgap, VSYS voltage detection, RTC, oscillator, and key detection.

Low-Power Shutdown (SHUTDOWN_LP):

- If PWR_CTRL1[7] = 1 (Table 7-87), AONLDO and Bandgap are additionally disabled in Shutdown Mode.

Entry Conditions:

- After PMIC power-on reset release (VSYS > 2.7V)
- During power-on sequence: all shutdown and reset events directly trigger this mode
- Other scenarios: shutdown or reset events trigger the shutdown sequence

Exit Conditions:

- PWR_CTRL1[7] = 0: any power-on event
- PWR_CTRL1[7] = 1: PWRKY key power-on, RTC alarm, or TICK events

Reset events entering Shutdown Mode:

- When a PWRKY forced reset occurs (>12s), PMIC switches immediately to Shutdown Mode, waits PWR_CTRL2[7], then enters Reset Mode.
- For other reset events, PMIC waits PWR_CTRL2[7]; if VSYS exceeds the power-on threshold, it automatically executes the power-on sequence.

#### 6.2.4 Active Mode

All modules are operational: power rails, load switches, battery charging, voltage detection, internal references, OV/UV/SC/OL detection, thermal monitoring, internal clocks, oscillators, ADC, RTC, communication interfaces, GPIO, keys, and interrupts.

Entry Conditions:

- Completion of power-on sequence
- Wake-up from Sleep Mode

Exit Conditions:

- Power-off, reset, or sleep events

#### 6.2.5 Sleep Mode

- Certain power rails can be reduced or turned off; PGOOD pin can be pulled low to reset SoC.

Entry Condition: sleep event from Active Mode  
Exit Conditions: power-off, reset, or wake-up events

#### 6.2.6 Mode Status Overview

Table 6-4: PMIC Mode Management

| Power Domain    | Module      | RESET | RTC             | SHUTDOWN-LP     | SHUTDOWN        | ACTIVE          | SLEEP           |
|-----------------|------------|-------|-----------------|-----------------|-----------------|-----------------|-----------------|
| VSYS            | BUCK/LDO    | -     | -               | -               | -               | x <br>(if enabled)  | x <br> (if enabled)  |
|                 | SWITCH      | -     | -               | -               | -               | x <br>(if enabled)  | x <br>(if enabled)  |
|                 | BCHG        | -     | -               | -               | -               | x <br>(if enabled)  | x <br>(if enabled)  |
|                 | MTP         | -     | -               | -               | -               | x               | x               |
|                 | AONLDO      | -     | -               | -               | x               | x               | x               |
|                 | BG          | -     | -               | -               | x               | x               | x               |
|                 | VSYS DET    | -     | -               | x               | x               | x               | x               |
|                 | VREF        | -     | -               | -               | -               | x               | x               |
|                 | IREF        | -     | -               | -               | -               | x               | x               |
|                 | SOSC        | -     | -               | x               | x               | x               | x               |
|                 | FOSC        | -     | -               | -               | -               | x               | x               |
|                 | ADC         | -     | -               | -               | -               | x <br>(if enabled)  | x <br>(if enabled)  |
|                 | TS          | -     | -               | -               | -               | x               | x               |
|                 | OT-P        | -     | -               | -               | -               | x               | x               |
|                 | KEY         | -     | -               | x               | x               | x               | x               |
| VSYS / VBAT     | XTAL        | -     | x <br>(if enabled)  | x <br>(if enabled)  | x <br>(if enabled)  | x <br>(if enabled)  | x <br>(if enabled)  |
|                 | RTC         | -     | x <br>(if enabled)  | x <br>(if enabled)  | x <br>(if enabled)  | x <br>(if enabled)  | x <br>(if enabled)  |
| VSYS            | DIGITAL     | -     | -               | x               | x               | x               | x               |
| AONLDO          | GPIO        | -     | -               | -               | -               | x               | x               |
|                 | INT         | -     | -               | -               | -               | x               | x               |
|                 | IIC         | -     | -               | -               | -               | x               | x               |

### 6.3 PMIC Events and Behaviors

Table 6-5 summarizes the PMIC events and corresponding behaviors. The term “Forced” indicates that the PMIC will immediately switch from its current state to Shutdown Mode.

| Type        | Event                   | Applicable Mode/Domain                        | Behavior                    |
|------------|-------------------------|-----------------------------------------------|-----------------------------|
| Power-On   | VSYS over-threshold     | Shutdown Mode                                 | Power-On / Wake-Up          |
|            | PWRKY Power-On          |                                               |                             |
|            | INT Pulldown 16 ms      |                                               |                             |
|            | ALARM / TICK            |                                               |                             |
|            | PWRCTRL Fully Bound On  |                                               |                             |
| Power-Off  | PWRKY Power-Off         | See Section 5.2 diagram (* state, # state)   | Configured Power-Off        |
|            | VSYS under-threshold    |                                               |                             |
|            | PWRCTRL Power-Off       |                                               |                             |
|            | Power Rail Abnormal     |                                               |                             |
|            | Software Power-Off      | See Section 5.2 diagram (# state)            |                             |
|            | Chip Over-Temperature / VSYS Over-Voltage | ALL                         | Forced Shutdown             |
| Sleep      | Software Sleep          | Active Mode                                   | Configured Sleep Entry      |
|            | GPIO Sleep              | Active Mode                                   |                             |
| Wake-Up    | Software Wake           | Sleep Mode                                    | Configured Sleep Exit       |
|            | GPIO Wake               | Sleep Mode                                    |                             |
|            | PWRKY Interrupt Wake    | Sleep Mode                                    |                             |
|            | ALARM / TICK            | Sleep Mode                                    |                             |
| Reset      | PWRKY Reset             | ALL                                           | Forced Cold Reset           |
|            | Software Reset          | See Section 5.2 diagram (# state)            | Configured Reset            |
|            | nRESET Inactive         | See Section 5.2 diagram (* state, # state)   |                             |
|            | PGOOD Pulldown          |                                               |                             |
|            | Watchdog Timeout        |                                               |                             |

### 6.4 Sequence Controller

The PMIC's power rails (except AONLDO) are managed by a programmable sequence controller, which handles Power-On, Power-Off, Sleep, and Wake-Up flows. The controller features 16 programmable SLOTs with the following characteristics:

1. Power Rail Control

   - Each power rail is assigned a SLOT ID, which can point to any of the 16 SLOTs.
   - Power rail enable/disable is controlled by PWRCTRL (register configuration):
     - BUCK: BUCKx_CTRL[5:3] (Table 7-75)
     - ALDO: ALDOx_CTRL[3:1] (Table 7-80)
     - DLDO: DLDOx_CTRL[3:1] (Table 7-83)
   - During a SLOT, the rail will only enable if PWRCTRL is valid; conversely, the rail will disable or adjust voltage when PWRCTRL becomes invalid.

2. EXT_EN Control

   - GPIO0~5 can be configured as EXT_EN outputs.
   - Each EXT_EN is assigned a SLOT ID (register configuration: Tables 7-102 to 7-104).

3. SLOT Timing Rules

   - If a power rail is controlled by PWRCTRL, the SLOT timing waits until all bound PWRCTRL signals reach their target states (all valid/invalid).

SLOT Functions

- SLOT0~SLOT14: Active control sequence.
- SLOT15: Inactive control sequence.

Behavior by Mode:

- Power-On / Wake-Up Flows
  - BUCK and LDO enables are activated according to SLOT0~SLOT14.
  - EXT_EN becomes active.
  - Power rails and EXT_EN pointing to SLOT15 remain inactive.

- Sleep Flow
  - BUCK and LDO enable states remain unchanged for SLOT0~SLOT15.
  - Rails with sleep voltage set to 0 are disabled.
  - EXT_EN controlled by sleep timing (PWR_EXT_CTRL[5:0], Table 7-106) becomes inactive; otherwise, it remains unchanged.

- Power-Off Flow
  - BUCK and LDO enables are disabled for SLOT0~SLOT15.
  - EXT_EN becomes inactive.

Controller Scale

- Supports up to 23 SLOT IDs (6 EXT_EN + 6 BUCK + 11 LDO)
- Example: DLDO1/DLDO4 bound to a specific PWRCTRL (see sequence controller timing diagram below).

![](static/B0DdbO3J4o7ua5xe5c9cd4JQnNh.png)

Power Rail State & Output by Mode

| Mode        | SLOT_ID | PWRCTRLx      | Software | Rail State | Rail Output Voltage    |
|------------|---------|---------------|----------|------------|-----------------------|
| Shutdown    | -       | -             | -        | Disabled   | -                     |
| Power-On Flow | x     | x (optional)  | x        | Enabled    | Normal                |
| Active Mode | -       | x (optional)  | x        | Enabled    | Normal                |
| Sleep Flow  | x       | x (optional)  | x        | Enabled    | Normal -> Sleep       |
| Sleep Mode  | -       | x (optional)  | x        | Enabled    | Sleep                 |
| Wake-Up Flow| x       | x (optional)  | x        | Enabled    | Sleep -> Normal       |
| Power-Off Flow | x    | x (optional)  | -        | Disabled   | -                     |

#### 6.4.1 Power-On Events

The PMIC supports the following Power-On / Wake-Up events:

1. VSYS exceeds the Power-On threshold (maskable via MTP)
2. PWRKY long-press Power-On (normally open)
3. INT pin pulled low for >16 ms (maskable via MTP)
4. RTC ALARM or TICK events (maskable via MTP)
5. PWRCTRL full-bind Power-On event (maskable via MTP)
6. Auto-restart event after shutdown

> Trigger Condition: Except for VSYS threshold events, all other events require VSYS above the Power-On threshold to be valid.

Wake-Up Requirements

- VSYS Voltage Range: 2.9V ~ 5.5V (must be stable)
- Power-On Threshold:
  - Configurable via MTP

In addition to MTP configuration, the PMIC dynamically adjusts the Power-On threshold in hardware to prevent false Power-On/Off events under weak supply conditions. The Power-On/Off threshold switching diagram is shown below. Adjustment procedure:

Dynamic Power-On Threshold Adjustment

1. Initial State
   - After PMIC reset release, the device enters Shutdown Mode.
   - If VSYS event is not masked, Power-On occurs when VSYS > default Power-On threshold.

2. Low-Voltage Protection
    - If VSYS < Shutdown threshold within 16 seconds after Power-On:
     - Execute Power-Off flow and enter Shutdown Mode.
       - Adjust Power-On Threshold:
          - If the current threshold < maximum (3.6V), increase in 0.1V or 0.2V steps (selected via SYS_CFG2[7], Table 7-127)
          - If already at 3.6V, mask the VSYS Power-On event

3. Threshold Recovery
   - If VSYS remains stable above the Shutdown threshold for 16 seconds after Power-On, restore the threshold to default.

4. Disable Feature
   - Threshold adjustment can be disabled via SYS_CFG2[6] (Table 7-127).

![](static/GNJUbF6SzooXCLxab3oc585PnAP.png)

#### 6.4.2 Power-On Sequence

When a Power-On event is detected in Shutdown Mode, the PMIC executes the Power-On sequence as follows:

1. Load Configuration from MTP
   - Includes voltage settings and other required configurations for all power rails.

2. Pre-Power-On Checks
   - Checks VSET pin status.
   - Monitors abnormal events (OVP/UVP, short-circuit, open-circuit) on all power rails.
   - If no abnormal events are detected, the Power Rail On Sequence is initiated; otherwise, the PMIC immediately returns to Shutdown Mode.

3. Power-On Sequence Completion
    - After the sequence, a programmable delay is applied (PWR_SEQ_TIME[5:4], Table 7-92), then the PMIC releases the PGOOD pin:
       - If configured to not wait for PGOOD release (PWR_CTRL1[3]=0, Table 7-87), the system enters Power-On mode immediately.
       - If waiting for PGOOD release, the system enters Power-On mode only after PGOOD is released.
     - If PGOOD is not released within the configured timeout (PWR_CTRL1[4], Table 7-87), the PMIC returns to Shutdown Mode.

> Note: Before entering Power-On mode (see 6.2 [Mode Transition Diagram](#62-operating-modes), * state), if an abnormal, shutdown, or reset event occurs, the PMIC aborts the Power-On sequence and returns to Shutdown Mode, awaiting the next wake-up event.

SLOT Mechanism and Power Rail Control

- Power Rail Management: All BUCKs (BUCK1~6), 11 LDOs, and all EXTx_EN signals have independent SLOT IDs, configured via MTP. After waking from Shutdown Mode, PMIC reads the configuration from MTP.
- SLOT Binding: Multiple power rails or EXTx_EN signals can be bound to the same SLOT, enabling simultaneous activation.
- DUMMY SLOT: If a SLOT has no bound power rail or EXT_EN, it is treated as a DUMMY SLOT. The sequence controller skips it, holding for one internal slow clock cycle (~32 μs).

Power-On Sequence and PWRCTRL Binding

The sequence controller starts from SLOT0, with programmable timing (four levels available, PWR_SEQ_TIME[1:0], Table 7-92). Behavior depends on PWRCTRL bindings:

1. SLOT0~14 without PWRCTRL Binding
   - Upon entering the SLOT, power rails and EXTx_EN are enabled immediately and timing starts.
   - After timing completes, the next SLOT is executed.

2. SLOT0~14 with PWRCTRL Binding
   - Rails/EXT_EN without PWRCTRL are enabled immediately; SLOT timing does not start until all bound PWRCTRL signals are valid.
   - Rails bound to PWRCTRL are enabled only when the corresponding PWRCTRL signal is valid.
   - Once all bound PWRCTRL signals are valid, timing begins; after timing completes, the next SLOT executes.
   - If a PWRCTRL signal becomes invalid during timing, the timer stops and resets, the corresponding rails are disabled, and timing restarts only after PWRCTRL signals are valid again.
   - Once timing completes and the next SLOT starts, any subsequent PWRCTRL changes do not affect already activated rails. In Power-On mode, rails controlled by PWRCTRL will disable if PWRCTRL becomes invalid and re-enable when PWRCTRL becomes valid.

3. SLOT15 with PWRCTRL Binding
   - Rails or EXTx_EN are not enabled; this SLOT performs no action.
   - If rails are bound to PWRCTRL, SLOT timing waits until PWRCTRL is valid before starting.

![](static/T5TCbdx84oCR2rxAATncgOzonje.png)

#### 6.4.3 Shutdown Event Types

The PMIC supports the following conditions for triggering a shutdown:

1. Hardware-Triggered Events
   - PWRKY Long-Press Shutdown (enabled when PWR_CTRL2[6]=0)
   - VSYS below threshold (forces hardware shutdown)

2. Software-Triggered Events
   - Software-Initiated Shutdown via register configuration

3. Power Management Events
   - All power rails bound to PWRCTRL are invalid (can be masked via MTP)

4. Protection and Fault Events (maskable via software/MTP)
   - Power rail faults: Over-Voltage (OV), Under-Voltage (UV), Short-Circuit (SC)
   - Chip Over-Temperature
   - VSYS Over-Voltage

#### 6.4.4 Shutdown Sequence

Overview

When the PMIC triggers a shutdown or reset event while in Active Mode, the system executes a reverse shutdown sequence:

1. Sequence Control
   - Starts from SLOT15 and executes in reverse order down to SLOT0.
   - The behavior within each SLOT follows the same logic as the startup sequence, but trigger conditions and output polarity are inverted (see Figures 6-4 and 6-7).

2. Fault and Interrupt Handling
   - If a shutdown event occurs during sleep/wake processes (see Figure 6-3, marked #):
     - The current sequence is immediately interrupted.
     - The shutdown sequence corresponding to PWR_CTRL1[0] (Table 7-87) is executed.

For each SLOT in the reverse sequence:

- Power rails bound to that SLOT are disabled and EXT_EN outputs are deactivated.
- If the power rail is configured to wait for PWRCTRL (PWR_CTRL2[4]=1, Table 7-88), the SLOT timing and power rail shutdown will wait until PWRCTRL becomes inactive.
- If the PWRCTRL wait exceeds the configured timeout (PWR_CTRL2[5], Table 7-88), the SLOT timing proceeds and the corresponding power rails are forced to shutdown.

Emergency Event Handling

- Trigger Conditions (any of the following):
   - VSYS Over-Voltage (PWRKY_EVENT[5], Table 7-113)
   - Chip Over-Temperature (EVENT2[6], Table 7-109)
- Response Actions:
   - If protection is enabled (IRQ_PWRKY_EN[7:6]=1), the system immediately jumps to Shutdown Mode.
   - All power rails and EXT_EN outputs are forcibly disabled.

The shutdown sequence timing diagram is shown below:

![](static/DvpJbqt17o1b6wxx4qIcpjiCn3e.png)

#### 6.4.5 Sleep Events

The sleep events in Figure 6-3 represent the conditions for entering Sleep Mode from Active Mode:

1. Software-Initiated Sleep (PWR_CTRL2[0]=1, Table 7-88)
2. GPIO Input Event via the Sleep/Wake-up (SLEEP/WKUP) pin

#### 6.4.6 Sleep Sequence

The timing sequence for entering Sleep Mode from Active Mode follows the same SLOT-based structure as the startup sequence, but with different behaviors. Key points of the sleep sequence:

1. Power Rail Adjustment
   - The enable state of each power rail remains unchanged.
   - If the sleep voltage for a rail is set to 0, the rail is disabled.
   - Otherwise, the rail adjusts to its configured sleep voltage.

2. EXT_EN Control
   - The state of EXT_EN outputs is controlled by Table 7-104 (PWR_EXT_EN) and Table 7-106 (PWR_EXT_CTRL).
   - EXT_EN outputs will only be deactivated in their respective SLOT stages if EXTx_SLP_SD is set to 1; otherwise, the outputs remain unchanged.

3. Wake-up Event Handling
   - Wake-up events do not interrupt the sleep sequence.
   - If wake-up conditions are met after entering Sleep Mode, the wake-up sequence is initiated.
   - Sleep conditions triggered by software or GPIO are level-sensitive and only valid in Active Mode.

4. Multiple GPIO Configuration
   - When multiple GPIOs are configured as SLEEP/WKUP pins, the system enters Sleep Mode if any one of the pins becomes active during Active Mode.

#### 6.4.7 Wake-up Events

The wake-up events (see Figure in Section 5.2) define the conditions for exiting Sleep Mode:

1. Software-initiated wake-up
2. GPIO input event via Sleep/Wake-up (SLEEP/WKUP) pins becoming inactive
3. PWRKY interrupt wake-up (short press, long press, rising/falling edge)
4. RTC ALARM and TICK events (maskable via MTP)

#### 6.4.8 Wake-up Sequence

The wake-up behavior from Sleep Mode follows the same SLOT-based sequence as the power-on sequence, with the following distinctions:

1. Power Rail Voltage Adjustment
   - During wake-up, the voltage of each power rail is adjusted from its sleep voltage to the normal operating voltage.

2. Software-Disabled Power Rails
   - Any power rail disabled via software during Sleep Mode remains off during the wake-up sequence.

3. Sleep Event Handling
   - Sleep events do not interrupt the wake-up sequence.
   - If Sleep conditions are still met after entering Active Mode, the system will initiate a sleep sequence.

4. Clearing Software Triggered Sleep Conditions
   - If sleep was entered via software but exited through another wake-up source, other wake-up sources will clear the software-triggered sleep conditions by resetting the corresponding registers.

5. Multiple GPIO Configuration
   - When multiple GPIOs are configured as SLEEP/WKUP pins, all SLEEP/WKUP pins must be inactive to initiate the wake-up sequence.

6. Specific Wake-up Source Restrictions
   - If any SLEEP/WKUP pin is active, wake-up via PWRKY interrupts, RTC ALARM, or TICK events is inhibited.

#### 6.4.9 Reset Events

The PMIC supports the following reset events:

1. PWRKY long-press 12s cold reset event (Table 7-88 PWR_CTRL2[6] = 1)
2. PWRKY long-press shutdown followed by automatic restart (Table 7-88 PWR_CTRL2[6] = 0 and Table 7-87 PWR_CTRL1[2] = 1)
3. Software-initiated reset
4. nRESET (GPIO input multiplexed function) invalid event (maskable via software)
5. PGOOD pull-down (maskable via software or MTP)
6. Watchdog timeout reset (maskable via software)

#### 6.4.10 Reset Sequence

Reset events behave identically in Active Mode and Sleep Mode. All reset sequences execute through the shutdown sequence before completing.

1. Shutdown Mode Hold Time
   - After executing the shutdown sequence, the PMIC remains in Shutdown Mode for a configurable duration (Table 7-88 PWR_CTRL2[7]) to ensure sufficient reset timing.
   - Upon completion of this period, two outcomes are possible:
       - Enter RESET Mode
          - If PWRKY is configured for 12s long-press reset and the key event occurs, the PMIC resets all logic and enters RESET Mode (see Reset Sequence Diagram).

       ![](static/Kn0rb2ftHoLXCix6icrcFvAQnQe.png)

       - Enter MTP READ2 Mode
          - For other reset events, the PMIC exits Shutdown Mode and enters MTP READ2 Mode (see Cold Reset Sequence Diagram).

       ![](static/TT2rbFovKoUyN3xeGYhcEcH4nsh.png)

2. Reset Source Masking
   - During the SD_RST_TIME period while in Shutdown Mode triggered by a reset source, all power-on sources are masked and remain inactive.

### 6.5 Watchdog

In Active Mode and Sleep Mode, the host can enable the watchdog and configure its timeout via the I²C interface (Table 7-72 WDT_CTRL[2:1]).

- If the host fails to feed the watchdog within the configured timeout period (WDT_CTRL[0]=1), a watchdog timeout event is generated and the corresponding flag is set (Table 7-108 EVENT1[3]).
- If watchdog reset is enabled (Table 7-86 PWR_CTRL0[7]), the PMIC will initiate the reset sequence upon timeout.
- If watchdog interrupt is enabled (Table 7-115 IRQ_EN1[3]), a watchdog interrupt is triggered and the INT pin is pulled low.

The watchdog is automatically disabled and stops functioning when the PMIC enters Shutdown Mode. To re-enable it, configuration must be performed again after returning to Active Mode.

### 6.6 GPIO

The PMIC provides 6 GPIOs, which can function as general-purpose IO or be configured for multiplexed input/output. Configuration details are available in Table 7-12 GPIO_MODE0 ~ Table 7-13 GPIO_MODE1 and Table 7-14 GPIO_AF01 ~ Table 7-16 GPIO_AF45. Additional GPIO features include:

1. All GPIOs support polarity control, pull-up/down, open-drain, and filtering, except when used as multiplexed ADC inputs.
2. GPIO debounce/filter time ranges from 100 μs to 1.5 ms (Table 7-8 GPIO_DEB_EN[7:6]), and the GPIOx_IDR reflects the current port state.
3. When configured as GPIO inputs, GPIO_IDR (Table 7-4) together with GPIO_ITYPE0 (Table 7-10) and GPIO_ITYPE1 (Table 7-11) can generate EVENT0[5:0] (Table 7-107).

The GPIOx_ODR register serves dual purposes:

1. When configured as GPIO output (GPIOx_MODE=2’b01), GPIOx_ODR reflects the GPIO output state.
2. When configured for multiplexed functionality (GPIOx_MODE=2’b1x), GPIOx_ODR represents the active state configuration of the associated multiplexed function.

### 6.7 I²C Communication Interface

The PMIC supports an I²C interface with a maximum speed of 1 MHz and operates only as a slave device.

- In Shutdown Mode, the SCL and SDA lines are inactive.  
- The host can access PMIC registers via I²C only in Active Mode or Sleep Mode.  
- The I²C slave address is configurable via MTP: Table 7-125 SYS_CFG0[6:0].

### 6.8 LDO

The PMIC integrates three types of LDOs: AONLDO, ALDO1~4, and DLDO1~7. Their control parameters are summarized below:

| Power Rail  | Sequencer | PWRCTRL | Software | DVS | STEP | SLEEP Voltage |
|------------|-----------|---------|---------|-----|------|---------------|
| AONLDO     | -         | -       | -       | -   | 25 mV| -             |
| ALDO1~4    | x         | x       | x       | -   | 25 mV| x             |
| DLDO1~7    | x         | x       | x       | -   | 25 mV| x             |

LDO Enable and Voltage Control

- AONLDO
  - Always enabled after VSYS powers up (VSYS > 2.7 V).  
  - No sleep voltage configuration.
- ALDO1~4 and DLDO1~7
   - Enable and voltage can be configured via software (host I²C access to PMIC registers).  
   - Voltage step size is 25 mV.  
   - Supports two voltage settings: Active Mode and Sleep Mode.

Hardware Control

- Sequencer
   - LDOs can be assigned to sequencer slots via Table 7-96 (PWR_SLOT3) to Table 7-101 (PWR_SLOT8), controlling on/off timing.  
- PWRCTRL (GPIO Multiplexed Input Function)
   - Configured via ALDOx_CTRL[3:1] (Table 7-80) and DLDOx_CTRL[3:1] (Table 7-83).  
  - LDO is enabled or disabled when the sequencer reaches the corresponding slot and the bound PWRCTRL signal is valid or invalid.

Pull-Down Control

- All LDO outputs include a pull-down resistor.  
- When LDO is enabled, the pull-down is disabled.  
- When LDO is disabled, the pull-down status is controlled by LDO_PD_DIS (see register description).

### 6.9 BUCK

The PMIC integrates 6 BUCK regulators with the following control parameters:

| Power Rail | Sequencer | PWRCTRL | Software | DVS | STEP     | SLEEP Voltage | Soft-Start | VSET | DUAL |
|------------|-----------|---------|---------|-----|----------|---------------|------------|------|------|
| BUCK1~2    | x         | x       | x       | x   | 5/25 mV | x             | x          | -    | x    |
| BUCK3~4    | x         | x       | x       | x   | 5/25 mV | x             | x          | -    | x    |
| BUCK5      | x         | x       | x       | x   | 5/25 mV | x             | x          | x    | -    |
| BUCK6      | x         | x       | x       | x   | 5/25 mV | x             | x          | x    | -    |

Soft-Start Feature

- All BUCK regulators support soft-start with a typical start-up time of 1 ms.

Dynamic Voltage Scaling (DVS)

- When a BUCK is enabled and DVS is active, the output voltage ramps dynamically in steps (configured in Table 7-74 BUCK_LDO_CFG[4:3]) until the target voltage is reached.
- DVS triggers:
   - Modifying BUCKx_VOLT (Table 7-76) in Active Mode.
   - Modifying BUCKx_SLP_VOLT (Table 7-77) in Sleep Mode.
   - Voltage switching by the sequencer during Sleep and Wake-Up sequences.

Dual-Phase Mode

- BUCK1 & BUCK2 and BUCK3 & BUCK4 can be configured in dual-phase mode to support higher current or improved efficiency.

Pull-Down Control

- All BUCK outputs include a pull-down resistor.
- Enabled BUCK: pull-down disabled.
- Disabled BUCK: pull-down status is determined by BUCK_LDO_CFG[6] (Table 7-74).

Special Configuration for BUCK5 and BUCK6

- BUCK5 and BUCK6 have dedicated VSET5 and VSET6 pins.
- The output voltage is determined by the pin state and the BUCK_VSET_CTRL register.  
- Refer to the corresponding register descriptions and VSET5/VSET6 pin details for full configuration information.

### 6.10 Shutdown Protection

The PMIC implements the following protection mechanisms:

1. Power Rail Protection: Over-voltage (OV), under-voltage (UV), short-circuit (SC), and open-circuit (OC) protection for all BUCK and LDO regulators.
2. Chip-Level Protection: Over-temperature, VSYS over-voltage, and switch short-circuit protection.

#### 6.10.1 Power Rail Fault Protection

When the shutdown protection for a power rail is enabled (PROT_EN[5:0], Table 7-121), any detected abnormality on the rail triggers the shutdown sequence. Configuration details are as follows:

1. Under-Voltage and Over-Voltage Detection

    - Filter Time Configuration  
       Filter time is configurable via OVUV_DELAY and supports:
     - 100 μs
     - 375 μs
     - 750 μs
     - Filter bypass (Table 7-127 SYS_CFG2[4:3])
     
   - Mask Time Configuration  
     Certain intervals may generate spurious OV/UV events. To avoid false shutdown or interrupts, mask time can be configured:
   - Applicable Intervals:
       - During power rail startup until stabilization
       - During voltage transition phases
   - Configuration: Table 7-127 SYS_CFG2[2:0]

2. Fault Response Mechanism

   - When a rail fault is detected, the PMIC executes the shutdown sequence according to the configured settings.
   - Filter and mask times allow flexible adjustment of protection behavior to ensure system stability and reliability.

#### 6.10.2 Other Fault Protection

- VSYS Over-Voltage, Chip Over-Temperature, and Switch Short-Circuit protections have separate enable bits:  
   - IRQ_PWRKY_EN[7:6], Table 7-120  
   - PROT_EN[7:6], Table 7-121
- All events support filter configuration via SYS_CFG2[5], Table 7-127 (100 μs or filter bypass).

Over-Temperature Protection Levels

| SYS_CFG0[7] (Table 7-125) | Warning Temp (℃) | Severe Temp (℃) | Critical Temp (℃) |
|----------------------------|-----------------|----------------|------------------|
| 0                          | 95              | 115            | 135              |
| 1                          | 110             | 130            | 150              |
| Event                      | EVENT2[4], Table 7-109 | EVENT2[5], Table 7-109 | EVENT2[6], Table 7-109 |
| Enable                     | -               | PROT_EN[6], Table 7-121 | IRQ_PWRKY_EN[6], Table 7-120 |
| Action                     | Interrupt       | Shutdown       | Shutdown          |

### 6.11 Load Switch

The PMIC integrates a software-controlled load switch (SWITCH) with the following behavior:

1. Pull-Down Resistor Control  

   - The SWITCH output has an internal pull-down resistor.
   - When the SWITCH is enabled, the pull-down resistor is disabled.
   - When the SWITCH is disabled, the pull-down resistor state is determined by SWITCH_CTRL[1], Table 7-78.

2. Behavior in Shutdown Mode  

   - The SWITCH is inactive in shutdown mode.

### 6.12 Battery Charging

The host can configure the charging voltage and current, and enable charging via BBAT_CTRL[0] = 1, Table 7-73. Charging behavior is as follows:

1. Full Charge Detection  
   - Once the battery reaches full charge, the PMIC waits 20 ms internally before stopping the charge.
2. Recharge on Voltage Drop  
   - If the battery voltage drops below the configured threshold, the PMIC resumes charging until full, repeating step 1.
3. Charging Disable  
   - Disabling charging (BCHG_EN = 0) stops the charging process immediately.

- In shutdown mode, the battery charging circuit is disabled. After re-entering power-on mode, charging must be re-enabled by the host.

### 6.13 ADC Control Circuit

The PMIC integrates a 12-bit ADC with the following features:

1. Sampling Rate: Configurable from 100 Hz to 50 kHz via registers.
2. Channels: 6 external scan channels and 20 internal scan channels selectable.
3. Reference Voltage: Configurable via ADC reference voltage register.
4. Scan Modes: Supports manual and automatic scan modes.
5. Manual Mode: Measurement channels are configurable; supports up to 6 external channels and 20 internal channels.
6. Automatic Mode: Measurement channels are configurable; supports 1 internal channel (chip junction temperature Tj) and 6 external scan channels (6 GPIOs configured as ADC scan input mode), totaling 7 automatic scan channels.
7. Result Registers: 7 independent automatic channel result registers and 1 multiplexed manual channel result register.
8. Threshold Monitoring: Each of the 7 automatic scan channels supports high and low threshold monitoring.
9. Threshold Flags with Filtering: Each high/low threshold flag is filtered and triggered after ADC_DEB_NUM consecutive events.
10. Interrupts: Supports maskable single conversion complete interrupt, sequence conversion complete interrupt, and threshold comparison interrupt.

#### 6.13.1 Channel Selection

The ADC module operation is illustrated below:

![](static/ASrNbFEj9o2VABx3wLhc9ptmnMG.png)

ADC Measurement Channels

| Channel | Description |
|---------|-------------|
| 0       | Measures VSYS voltage, all BUCK voltages, and all LDO voltages. Each channel is individually configurable. VSYS input is divided by 4 and measured using the internal reference. |
| 1       | V(TJ), internal junction temperature of the chip. |
| 2       | ADCIN0, GPIO0 configured as ADC analog input multiplexed function. |
| 3       | ADCIN1, GPIO1 configured as ADC analog input multiplexed function. |
| 4       | ADCIN2, GPIO2 configured as ADC analog input multiplexed function. |
| 5       | ADCIN3, GPIO3 configured as ADC analog input multiplexed function. |
| 6       | ADCIN4, GPIO4 configured as ADC analog input multiplexed function. |
| 7       | ADCIN5, GPIO5 configured as ADC analog input multiplexed function. |

#### 6.13.2 Manual Mode

The manual mode configuration procedure is as follows:

1. Reset the ADC_AUTO registers, disable all automatic scan channels, and enable the ADC (Table 7-34 ADC_CTRL[0]=1).
2. Select the ADC conversion channel by configuring Table 7-36 ADC_CFG1[5:3].
3. If channel 0 is selected, select the manual sub-channels for channel 0 via Table 7-39 ADC_MAN_EN0 ~ Table 7-41 ADC_MAN_EN2.
4. Configure other required settings, including ADC result filtering, sampling frequency, CHOP function, reference voltage, and per-channel threshold values.
5. Set ADC_GO to start a single conversion.

When the ADC is first enabled, it requires approximately >30 μs to stabilize. The ADC only begins normal operation after this stabilization period.

For each conversion in manual mode:

1. When scanning channel 0, the 12-bit result is stored in Table 7-42 ADC_MAN_RES_H and Table 7-43 ADC_MAN_RES_L.
2. When scanning other channels, the 12-bit results are stored in the corresponding result registers (Table 7-44 ADC_TJ_RES_H ~ Table 7-57 ADC_IN5_RES_L).
3. ADC_GO is automatically cleared by hardware.
4. The single conversion complete event (Table 7-108 EVENT1[1]) is set.
5. If interrupts are enabled (Table 7-115 IRQ_EN1[1]), an interrupt is triggered (INT pin pulled low) until cleared by software or the interrupt enable bit is reset.

Behavior when channel 0 is selected:

1. After configuring the enabled channels, each completed conversion automatically switches to the next enabled sub-channel of channel 0. After completing a full scan cycle, it returns to the first enabled channel, as illustrated in the ADC Channel 0 Scan Diagram below.
2. To change the scan sequence, configure the enabled channels before starting the next conversion.
3. To restart scanning from the beginning, use one of the following methods:
   - Disable and then re-enable ADC_EN.
   - Switch to automatic mode and back to manual mode: set any register in ADC_AUTO to 1, then clear all registers.
4. After all channels enabled via Table 7-39 ADC_MAN_EN0 ~ Table 7-41 ADC_MAN_EN2 are scanned and converted, the event Table 7-108 EVENT1[2] is set. If interrupts are enabled (Table 7-115 IRQ_EN1[2]), an interrupt is generated (INT pin pulled low) until cleared by software or the interrupt enable bit is reset.

> Note: Do not modify configuration (e.g., channel selection, sampling frequency, ADC_AUTO) during conversion. Doing so may invalidate conversion results. Clearing ADC_GO during conversion interrupts the current conversion; results are not saved, and channel scanning restarts from the beginning.

![](static/EaBCbpxDKoe0YFx1T5wcebDXnad.png)

#### 6.13.3 Automatic Mode

The automatic mode configuration procedure is as follows:

1. Configure the desired automatic scan channels by enabling the corresponding ADC_AUTO channels, and enable the ADC (Table 7-34 ADC_CTRL[0]=1).
2. Configure other required settings, including ADC result filtering, sampling frequency, CHOP function, reference voltage, high-speed mode, and per-channel thresholds.
3. Set ADC_GO to start conversion.

When the ADC is first enabled, it requires approximately >30 μs to stabilize. Normal operation begins only after stabilization.

For each conversion in automatic mode:

1. The 12-bit result is stored in the corresponding result register.
2. ADC_GO is not cleared in automatic scan mode.
3. The single conversion complete event (Table 7-108 EVENT1[1]) is set.
4. If interrupts are enabled (Table 7-115 IRQ_EN1[1]), an interrupt is triggered (INT pin pulled low) until cleared by software or the interrupt enable bit is reset.

After completing a full scan sequence (all channels enabled in ADC_AUTO are scanned):

1. The sequence conversion complete event (Table 7-108 EVENT1[2]) is set.
2. If interrupts are enabled (Table 7-115 IRQ_EN1[2]), an interrupt is generated (INT pin pulled low) until cleared by software or the interrupt enable bit is reset.

Behavior of channel selection:

- After configuring the enabled channels, each completed conversion automatically switches to the next enabled channel. After a full scan cycle, it returns to the first enabled channel, as illustrated in the ADC Automatic Scan Diagram below.

![](static/SVmFbhfUEoKnR1xVm5Zcy3LQnQu.png)

To change the scan sequence or restart scanning from the beginning:

1. Disable ADC_EN and reconfigure according to the automatic mode procedure.
2. Clear ADC_GO in software. The current conversion is interrupted, results are not saved, and scanning restarts from the beginning upon the next ADC_GO set.

> Note: Do not modify configuration during conversions (e.g., channel selection, sampling frequency, ADC_AUTO), as doing so may invalidate conversion results.

#### 6.13.4 ADC Result Filtering

For channels 1–7 with configured thresholds:

1. Without result filtering (ADC_CFG0 corresponding bits in Table 7-35 = 0):  
   If the conversion result exceeds or falls below the configured threshold, the corresponding channel event flags (Table 7-107 EVENT0[5:0], Table 7-108 EVENT1[0]) are set immediately.
2. With result filtering enabled:  
   The event flags are set only after consecutive over-threshold or under-threshold events reach the count configured in Table 7-37 ADC_CFG2[6:4].

If the corresponding interrupt is enabled, an interrupt event is generated (INT pin pulled low) until cleared by software or the interrupt enable bit is reset.

The figure below illustrates ADC result filtering:

![](static/P1kvbSkWNof1hLx61SocDgBNn5d.png)

### 6.14 RTC Module

The RTC module provides three main functions:

- Calendar
- Alarm
- Second counting

RTC power is supplied from two sources: VSYS and a backup coin cell battery.

- When VSYS is present, RTC is powered by VSYS.
- When VSYS drops below 2.0 V, the internal circuit switches to coin cell battery power.

The RTC clock source can be selected from the internal slow clock (LSI) or an external crystal, as configured in Table 7-33 RTC_CTRL[3].

Before starting the power-on sequence, the internal slow clock or crystal clock output can be enabled via the MTP register Table 7-33 RTC_CTRL[1].

#### 6.14.1 RTC Calendar

The RTC internal timing logic counts the 32 kHz clock to provide seconds, minutes, hours, day, month, and year, stored in Table 7-17 RTC_COUNT_S through Table 7-22 RTC_COUNT_Y.  
RTC_COUNT_Y = 0 corresponds to the year 2000, allowing calendar time up to 2063.  

To read the current internal calendar value, read RTC_COUNT_S first. This operation latches all calendar values into RTC_COUNT_S through RTC_COUNT_Y.

To update the calendar, configure all calendar registers in order (RTC_COUNT_S through RTC_COUNT_Y). After writing RTC_COUNT_Y, the PMIC updates the internal RTC timer with the new user-defined calendar value and starts counting from this point.

#### 6.14.2 RTC Alarm

The RTC module provides alarm registers Table 7-23 RTC_ALARM_S through Table 7-28 RTC_ALARM_Y. When the current RTC calendar value matches all RTC_ALARM_S through RTC_ALARM_Y:

1. If Table 7-33 RTC_CTRL[5]=1, an alarm event (Table 7-108 EVENT1[4]) is generated. If Table 7-115 IRQ_EN1[4]=1, an interrupt is also triggered (INT pin pulled low) until the host clears E_ALARM or IRQ_EN_ALARM.
2. If Table 7-33 RTC_CTRL[6]=1, a TICK event (Table 7-108 EVENT1[5]) is generated. If Table 7-115 IRQ_EN1[5]=1, an interrupt is also triggered (INT pin pulled low) until the host clears E_TICK or IRQ_EN_TICK.

TICK events are periodic and can be configured to trigger every 1 s or 1 min (Table 7-33 RTC_CTRL[4]). Clearing E_TICK does not stop the periodic trigger; only setting TICK_EN=0 disables the periodic event.

Alarm and TICK events can be masked for specific calendar units to generate events only during selected time periods:

1. MASK_ALARM_Y through MASK_ALARM_S correspond to year, month, day, hour, minute, and second mask bits.
2. Setting a mask bit to 1 disables matching of the corresponding RTC_ALARM_Y through RTC_ALARM_S unit.

In shutdown mode, RTC alarm and TICK events can serve as power-on sources.

In sleep mode, RTC alarm and TICK events can serve as wake-up sources.

#### 6.14.3 Second Counting

Registers Table 7-29 RTC_SECOND_A through Table 7-32 RTC_SECOND_D form a 32-bit second counter. When RTC_EN=1, the counter starts; otherwise, the second counter is cleared.

## 7. Registers

### 7.1 Register Attribute Definitions

The basic attributes of registers are defined in [Table 7-1](#table-7-1-register-base-attributes). Special attribute modifiers for certain registers are defined in [Table 7-2](#table-7-2-register-attribute-modifier).

#### Table 7-1 Register Base Attributes

| Attribute      | Abbreviation | Description                                         |
|----------------|-------------|-----------------------------------------------------|
| Read Only      | R           | Bit can be read by software, write has no effect. |
| Read/Write     | RW          | Bit can be read and written by software.          |
| Write Only     | W           | Bit can only be written by software.              |
| Reserved       | RV          | Bit is reserved and cannot be modified by software.|

#### Table 7-2 Register Attribute Modifiers

| Attribute        | Abbreviation | Description                                                                                     |
|-----------------|-------------|-------------------------------------------------------------------------------------------------|
| Write 1 Only     | IO          | Bit can only be written with 1 by software; writing 0 has no effect.                           |
| Protected        | P           | Bit is protected by the unlock register Table 7-128 MTP_KEY. Without writing the unlock sequence to the register, this bit cannot be modified by software. |
| MTP Loaded       | E           | Bit can be modified through MTP.                                                               |

### 7.2 Register Map

#### 7.2.1 Register Map Overview

##### Table 7-3 Register Map

| Module              | Table Name | Register Address (hex) | Attribute | Description |
|---------------------|------------|-------------------------|-----------|-------------|
| GPIO | [Table 7-4](#table-7-4-gpio_idr) | 0x00 | R | GPIO input data register |
| GPIO | [Table 7-5](#table-7-5-gpio_odr) | 0x01 | RW | GPIO output data register; active level configuration |
| GPIO | [Table 7-6](#table-7-6-gpio_pupd0) | 0x02 | RWE | GPIO0–GPIO2 pull-up / pull-down configuration |
| GPIO | [Table 7-7](#table-7-7-gpio_pupd1) | 0x03 | RWE | GPIO3–GPIO5 pull-up / pull-down configuration |
| GPIO | [Table 7-8](#table-7-8-gpio_deb_en) | 0x04 | RW | GPIO debounce enable and debounce time configuration |
| GPIO | [Table 7-9](#table-7-9-gpio_od) | 0x05 | RW | GPIO open-drain configuration |
| GPIO | [Table 7-10](#table-7-10-gpio_itype0) | 0x06 | RWE | GPIO0–GPIO2 interrupt type configuration |
| GPIO | [Table 7-11](#table-7-11-gpio_itype1) | 0x07 | RWE | GPIO3–GPIO5 interrupt type configuration |
| GPIO | [Table 7-12](#table-7-12-gpio_mode0) | 0x08 | RWE | GPIO0–GPIO2 mode configuration |
| GPIO | [Table 7-13](#table-7-13-gpio_mode1) | 0x09 | RWE | GPIO3–GPIO5 mode configuration |
| GPIO | [Table 7-14](#table-7-14-gpio_af01) | 0x0A | RWE | GPIO0–GPIO1 alternate function selection |
| GPIO | [Table 7-15](#table-7-15-gpio_af23) | 0x0B | RWE | GPIO2–GPIO3 alternate function selection |
| GPIO | [Table 7-16](#table-7-16-gpio_af45) | 0x0C | RWE | GPIO4–GPIO5 alternate function selection |
| RTC | [Table 7-17](#table-7-17-rtc_count_s) | 0x0D | RW | RTC seconds counter register |
| RTC | [Table 7-18](#table-7-18-rtc_count_mi) | 0x0E | RW | RTC minutes counter register |
| RTC | [Table 7-19](#table-7-19-rtc_count_h) | 0x0F | RW | RTC hours counter register |
| RTC | [Table 7-20](#table-7-20-rtc_count_d) | 0x10 | RW | RTC days counter register |
| RTC | [Table 7-21](#table-7-21-rtc_count_mo) | 0x11 | RW | RTC months counter register |
| RTC | [Table 7-22](#table-7-22-rtc_count_y) | 0x12 | RW | RTC years counter register |
| RTC | [Table 7-23](#table-7-23-rtc_alarm_s) | 0x13 | RW | RTC alarm seconds setting |
| RTC | [Table 7-24](#table-7-24-rtc_alarm_mi) | 0x14 | RW | RTC alarm minutes setting |
| RTC | [Table 7-25](#table-7-25-rtc_alarm_h) | 0x15 | RW | RTC alarm hours setting |
| RTC | [Table 7-26](#table-7-26-rtc_alarm_d) | 0x16 | RW | RTC alarm days setting |
| RTC | [Table 7-27](#table-7-27-rtc_alarm_mo) | 0x17 | RW | RTC alarm months setting |
| RTC | [Table 7-28](#table-7-28-rtc_alarm_y) | 0x18 | RW | RTC alarm years setting |
| RTC | [Table 7-29](#table-7-29-rtc_second_a) | 0x19 | R | RTC second counter [7:0] |
| RTC | [Table 7-30](#table-7-30-rtc_second_b) | 0x1A | R | RTC second counter [15:8] |
| RTC | [Table 7-31](#table-7-31-rtc_second_c) | 0x1B | R | RTC second counter [23:16] |
| RTC | [Table 7-32](#table-7-32-rtc_second_d) | 0x1C | R | RTC second counter [31:24] |
| RTC | [Table 7-33](#table-7-33-rtc_ctrl) | 0x1D | RWE | RTC control register |
| ADC | [Table 7-34](#table-7-34-adc_ctrl1) | 0x1E | RW | ADC control register |
| ADC | [Table 7-35](#table-7-35-adc_cfg01) | 0x1F | RW | ADC configuration register 0 |
| ADC | [Table 7-36](#table-7-36-adc_cfg11) | 0x20 | RW | ADC configuration register 1 |
| ADC | [Table 7-37](#table-7-37-adc_cfg21) | 0x21 | RW | ADC configuration register 2 |
| ADC | [Table 7-38](#table-7-38-adc_auto1) | 0x22 | RW | ADC automatic scan channel selection |
| ADC | [Table 7-39](#table-7-39-adc_man_en01) | 0x23 | RW | Manual scan channel selection for ADC channel 0 |
| ADC | [Table 7-40](#table-7-40-adc_man_en11) | 0x24 | RW | Manual scan channel selection for ADC channel 0 |
| ADC | [Table 7-41](#table-7-41-adc_man_en21) | 0x25 | RW | Manual scan channel selection for ADC channel 0 |
| ADC | [Table 7-42](#table-7-42-adc_man_res_h1) | 0x26 | R | ADC channel 0 manual conversion result [11:4] |
| ADC | [Table 7-43](#table-7-43-adc_man_res_l1) | 0x27 | R | ADC channel 0 manual conversion result [3:0] |
| ADC | [Table 7-44](#table-7-44-adc_tj_res_h1) | 0x28 | R | Junction temperature auto conversion result (8 MSBs) |
| ADC | [Table 7-45](#table-7-45-adc_tj_res_l1) | 0x29 | R | Junction temperature auto conversion result (4 LSBs) |
| ADC | [Table 7-46](#table-7-46-adc_in0_res_h1) | 0x2A | R | ADCIN0 auto conversion result (8 MSBs) |
| ADC | [Table 7-47](#table-7-47-adc_in0_res_l1) | 0x2B | R | ADCIN0 auto conversion result (4 LSBs) |
| ADC | [Table 7-48](#table-7-48-adc_in1_res_h1) | 0x2C | R | ADCIN1 auto conversion result (8 MSBs) |
| ADC | [Table 7-49](#table-7-49-adc_in1_res_l1) | 0x2D | R | ADCIN1 auto conversion result (4 LSBs) |
| ADC | [Table 7-50](#table-7-50-adc_in2_res_h1) | 0x2E | R | ADCIN2 auto conversion result (8 MSBs) |
| ADC | [Table 7-51](#table-7-51-adc_in2_res_l1) | 0x2F | R | ADCIN2 auto conversion result (4 LSBs) |
| ADC | [Table 7-52](#table-7-52-adc_in3_res_h1) | 0x30 | R | ADCIN3 auto conversion result (8 MSBs) |
| ADC | [Table 7-53](#table-7-53-adc_in3_res_l1) | 0x31 | R | ADCIN3 auto conversion result (4 LSBs) |
| ADC | [Table 7-54](#table-7-54-adc_in4_res_h1) | 0x32 | R | ADCIN4 auto conversion result (8 MSBs) |
| ADC | [Table 7-55](#table-7-55-adc_in4_res_l1) | 0x33 | R | ADCIN4 auto conversion result (4 LSBs) |
| ADC | [Table 7-56](#table-7-56-adc_in5_res_h1) | 0x34 | R | ADCIN5 auto conversion result (8 MSBs) |
| ADC | [Table 7-57](#table-7-57-adc_in5_res_l1) | 0x35 | R | ADCIN5 auto conversion result (4 LSBs) |
| ADC | [Table 7-58](#table-7-58-adc_vth_tj_h1) | 0x36 | RW | Junction temperature high threshold (8 MSBs) |
| ADC | [Table 7-59](#table-7-59-adc_vth_tj_l1) | 0x37 | RW | Junction temperature low threshold (8 MSBs) |
| ADC | [Table 7-60](#table-7-60-adc_in0_vth_h1) | 0x38 | RW | ADCIN0 high threshold (8 MSBs) |
| ADC | [Table 7-61](#table-7-61-adc_in0_vth_l1) | 0x39 | RW | ADCIN0 low threshold (8 MSBs) |
| ADC | [Table 7-62](#table-7-62-adc_in1_vth_h1) | 0x3A | RW | ADCIN1 high threshold (8 MSBs) |
| ADC | [Table 7-63](#table-7-63-adc_in1_vth_l1) | 0x3B | RW | ADCIN1 low threshold (8 MSBs) |
| ADC | [Table 7-64](#table-7-64-adc_in2_vth_h1) | 0x3C | RW | ADCIN2 high threshold (8 MSBs) |
| ADC | [Table 7-65](#table-7-65-adc_in2_vth_l1) | 0x3D | RW | ADCIN2 low threshold (8 MSBs) |
| ADC | [Table 7-66](#table-7-66-adc_in3_vth_h1) | 0x3E | RW | ADCIN3 high threshold (8 MSBs) |
| ADC | [Table 7-67](#table-7-67-adc_in3_vth_l1) | 0x3F | RW | ADCIN3 low threshold (8 MSBs) |
| ADC | [Table 7-68](#table-7-68-adc_in4_vth_h1) | 0x40 | RW | ADCIN4 high threshold (8 MSBs) |
| ADC | [Table 7-69](#table-7-69-adc_in4_vth_l1) | 0x44 | RW | ADCIN4 low threshold (8 MSBs) |
| ADC | [Table 7-70](#table-7-70-adc_in5_vth_h1) | 0x42 | RW | ADCIN5 high threshold (8 MSBs) |
| ADC | [Table 7-71](#table-7-71-adc_in5_vth_l1) | 0x43 | RW | ADCIN5 low threshold (8 MSBs) |
| WDT | [Table 7-72](#table-7-72-wdt_ctrl1) | 0x44 | RW | Watchdog control register |
| Battery Charge | [Table 7-73](#table-7-73-bbat_ctrl1) | 0x45 | RW | Battery charging control register |
| Power Control | [Table 7-74](#table-7-74-buck_ldo_cfg1) | 0x46 | RWE | Power rail configuration register |
| Power Control | [Table 7-75](#table-7-75-buckx_ctrl1) | 0x47 + 3×n | RWE | BUCKn control register, n = 0–5 |
| Power Control | [Table 7-76](#table-7-76-buckx_volt1) | 0x48 + 3×n | RWE | BUCK output voltage setting |
| Power Control | [Table 7-77](#table-7-77-buckx_slp_volt1) | 0x49 + 3×n | RWE | BUCK sleep voltage setting |
| Power Control | [Table 7-78](#table-7-78-switch_ctrl1) | 0x59 | RW | Load switch control register |
| Power Control | [Table 7-79](#table-7-79-aonldo_ctrl1) | 0x5A | RE | AON LDO control register |
| Power Control | [Table 7-80](#table-7-80-aldox_ctrl1) | 0x5B | RWE | ALDO control register |
| Power Control | [Table 7-81](#table-7-81-aldox_volt1) | 0x5C | RWE | ALDO voltage setting |
| Power Control | [Table 7-82](#table-7-82-aldox_slp_volt1) | 0x5D | RWE | ALDO sleep voltage setting |
| Power Control | [Table 7-83](#table-7-83-dldox_ctrl) | 0x67 | RWE | DLDO control register |
| Power Control | [Table 7-84](#table-7-84-dldox_volt) | 0x68 | RWE | DLDO voltage setting |
| Power Control | [Table 7-85](#table-7-85-dldox_slp_volt) | 0x69 | RWE | DLDO sleep voltage setting |
| Power Control | [Table 7-86](#table-7-86-pwr_ctrl0) | 0x7C | RWE | Power control register 0 |
| Power Control | [Table 7-87](#table-7-87-pwr_ctrl1) | 0x7D | RWE | Power control register 1 |
| Power Control | [Table 7-88](#table-7-88-pwr_ctrl2) | 0x7E | RWE | Power control register 2 |
| Power Control | [Table 7-89](#table-7-89-pwr_sts0) | 0x7F | R | Power status register 0 |
| Power Control | [Table 7-90](#table-7-90-pwr_sts1) | 0x80 | R | Power status register 1 |
| Power Control | [Table 7-91](#table-7-91-pwr_key_time) | 0x81 | RWE | Power key timing configuration |
| Power Control | [Table 7-92](#table-7-92-pwr_seq_time) | 0x82 | RWE | Power sequencing timing configuration |
| Power Control | [Table 7-93](#table-7-93-pwr_slot0) | 0x83 | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-94](#table-7-94-pwr_slot1) | 0x84 | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-95](#table-7-95-pwr_slot2) | 0x85 | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-96](#table-7-96-pwr_slot3) | 0x86 | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-97](#table-7-97-pwr_slot4) | 0x87 | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-98](#table-7-98-pwr_slot5) | 0x88 | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-99](#table-7-99-pwr_slot6) | 0x89 | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-100](#table-7-100-buck_event0) | 0x8A | RIO | BUCK over-voltage event |
| Power Control | [Table 7-101](#table-7-101-pwr_slot8) | 0x8B | RE | Power rail SLOT ID configuration |
| Power Control | [Table 7-102](#table-7-102-pwr_slot9) | 0x8C | RE | EXT_EN SLOT ID configuration |
| Power Control | [Table 7-103](#table-7-103-pwr_slot10) | 0x8D | RE | EXT_EN SLOT ID configuration |
| Power Control | [Table 7-104](#table-7-104-pwr_slot11) | 0x8E | RE | EXT_EN SLOT ID configuration |
| Power Control | [Table 7-105](#table-7-105-pwr_ext_en) | 0x8F | RWE | EXT_EN software enable control |
| Power Control | [Table 7-106](#table-7-106-pwr_ext_ctrl) | 0x90 | RWE | EXT_EN sleep sequence control |
| Event | [Table 7-107](#table-7-107-event0) | 0x91 | RIO | PMIC system events |
| Event | [Table 7-108](#table-7-108-event1) | 0x92 | RIO | PMIC system events |
| Event | [Table 7-109](#table-7-109-event2) | 0x93 | RIO | PMIC system events |
| Event | [Table 7-110](#table-7-110-buck_event0) | 0x94 | RIO | BUCK over-voltage event |
| Event | [Table 7-111](#table-7-111-buck_event1) | 0x95 | RIO | BUCK under-voltage event |
| Event | [Table 7-112](#table-7-112-buck_event2) | 0x96 | RIO | BUCK short/open-circuit event |
| Event | [Table 7-113](#table-7-113-pwrky_event) | 0x97 | RIO | Power key event |
| Interrupt Enable | [Table 7-114](#table-7-114-irq_en0) | 0x98 | RW | PMIC system interrupt enable |
| Interrupt Enable | [Table 7-115](#table-7-115-irq_en1) | 0x99 | RW | PMIC system interrupt enable |
| Interrupt Enable | [Table 7-116](#table-7-116-irq_en2) | 0x9A | RW | PMIC system interrupt enable |
| Interrupt Enable | [Table 7-117](#table-7-117-irq_buck_en0) | 0x9B | RW | BUCK over-voltage interrupt enable |
| Interrupt Enable | [Table 7-118](#table-7-118-irq_buck_en1) | 0x9C | RW | BUCK under-voltage interrupt enable |
| Interrupt Enable | [Table 7-119](#table-7-119-irq_buck_en2) | 0x9D | RW | BUCK short/open-circuit interrupt enable |
| Interrupt Enable | [Table 7-120](#table-7-120-irq_pwrky_en) | 0x9E | RWE | Power key interrupt enable |
| Protection Enable | [Table 7-121](#table-7-121-prot_en) | 0x9F | RWE | System fault protection enable |
| ID | [Table 7-122](#table-7-122-device_id) | 0xA0 | RE | Device ID |
| ID | [Table 7-123](#table-7-123-version_id) | 0xA1 | RE | Version ID |
| ID | [Table 7-124](#table-7-124-customer_id) | 0xA2 | RE | Customer ID |
| System Configuration | [Table 7-125](#table-7-125-sys_cfg0) | 0xA3 | RE | System configuration register 0 |
| System Configuration | [Table 7-126](#table-7-126-sys_cfg1) | 0xA4 | RE | System configuration register 1 |
| System Configuration | [Table 7-127](#table-7-127-sys_cfg2) | 0xA5 | RE | System configuration register 2 |
| MTP | [Table 7-128](#table-7-128-mtp_key) | 0xA6 | RW | MTP unlock register |
| MTP | [Table 7-129](#table-7-129-mtp_addr) | 0xA7 | RWP | MTP address register |
| MTP | [Table 7-130](#table-7-130-mtp_data) | 0xA8 | RWP | MTP read/write data register |
| MTP | [Table 7-131](#table-7-131-mtp_cfg) | 0xA9 | RWP | MTP configuration register |
| MTP | [Table 7-132](#table-7-132-mtp_ctrl) | 0xAA | RWP | MTP control register |

#### 7.2.2 Register Description

##### Table 7-4 GPIO_IDR

| Addr | Bits | Field Name | Attr | Default | Description       |
| ---- | ---- | ---------- | ---- | ------- | ----------------- |
| 0x00 | 7:6  | Reserved   | RV   | 0       | Reserved          |
| 0x00 | 5    | GPIO5_IDR  | R    | 0x0     | GPIO5 input value |
| 0x00 | 4    | GPIO4_IDR  | R    | 0x0     | GPIO4 input value |
| 0x00 | 3    | GPIO3_IDR  | R    | 0x0     | GPIO3 input value |
| 0x00 | 2    | GPIO2_IDR  | R    | 0x0     | GPIO2 input value |
| 0x00 | 1    | GPIO1_IDR  | R    | 0x0     | GPIO1 input value |
| 0x00 | 0    | GPIO0_IDR  | R    | 0x0     | GPIO0 input value |

##### Table 7-5 GPIO_ODR

| Addr | Bits | Field Name | Attr | Default | Description   |
| ---- | ---- | ---------- | ---- | ------- | ------------------- |
| 0x01 | 7:6  | Reserved   | RV   | 0       | Reserved   |
| 0x01 | 5    | GPIO5_ODR  | RWE  | 0x0     | When configured as GPIO output, this bit defines the output data.<br>When configured for an alternate function, this bit defines the active polarity.<br><b>`0`</b>: Output low level / Active polarity is low<br><b>`1`</b>: Output high level / Active polarity is high |
| 0x01 | 4    | GPIO4_ODR  | RWE  | 0x0     | Same as GPIO5_ODR  |
| 0x01 | 3    | GPIO3_ODR  | RWE  | 0x0     | Same as GPIO5_ODR |
| 0x01 | 2    | GPIO2_ODR  | RWE  | 0x0     | Same as GPIO5_ODR |
| 0x01 | 1    | GPIO1_ODR  | RWE  | 0x0     | Same as GPIO5_ODR  |
| 0x01 | 0    | GPIO0_ODR  | RWE  | 0x0     | Same as GPIO5_ODR  |

##### Table 7-6 GPIO_PUPD0

| Addr | Bits | Field Name | Attr | Default | Description   |
| ---- | ---- | ---------- | ---- | ------- | ----- |
| 0x02 | 7:6  | Reserved   | RV   | 0       | Reserved   |
| 0x02 | 5:4  | GPIO2_PUPD | RWE  | 0x0     | GPIO2 pull-up / pull-down configuration:<br>- `00`: No operation<br>- `01`: Pull-up enabled<br>- `10`: Pull-down enabled<br>- `1x`: Invalid |
| 0x02 | 3:2  | GPIO1_PUPD | RWE  | 0x0     | GPIO1 pull-up / pull-down configuration:<br>- `00`: No operation<br>- `01`: Pull-up enabled<br>- `10`: Pull-down enabled<br>- `1x`: Invalid |
| 0x02 | 1:0  | GPIO0_PUPD | RWE  | 0x0     | GPIO0 pull-up / pull-down configuration:<br>- `00`: No operation<br>- `01`: Pull-up enabled<br>- `10`: Pull-down enabled<br>- `1x`: Invalid |

##### Table 7-7 GPIO_PUPD1

| Addr | Bits | Field Name | Attr | Default | Description   |
| ---- | ---- | ---------- | ---- | ------- | ----------- |
| 0x03 | 7:6  | Reserved   | RV   | 0       | Reserved     |
| 0x03 | 5:4  | GPIO5_PUPD | RWE  | 0x0     | GPIO5 pull-up / pull-down configuration:<br>- `00`: No operation<br>- `01`: Pull-up enabled<br>- `10`: Pull-down enabled<br>- `1x`: Invalid |
| 0x03 | 3:2  | GPIO4_PUPD | RWE  | 0x0     | GPIO4 pull-up / pull-down configuration:<br>- `00`: No operation<br>- `01`: Pull-up enabled<br>- `10`: Pull-down enabled<br>- `1x`: Invalid |
| 0x03 | 1:0  | GPIO3_PUPD | RWE  | 0x0     | GPIO3 pull-up / pull-down configuration:<br>- `00`: No operation<br>- `01`: Pull-up enabled<br>- `10`: Pull-down enabled<br>- `1x`: Invalid |

##### Table 7-8 GPIO_DEB_EN

| Addr | Bits | Field Name    | Attr | Default | Description     |
| ---- | ---- | ------------- | ---- | ------- | --------------- |
| 0x04 | 7:6  | GPIO_DEB_TIME | RW   | 0x0     | GPIO0–GPIO5 debounce time selection:<br>- `00`: 100 µs<br>- `01`: 375 µs<br>- `10`: 750 µs<br>- `11`: 1.5 ms |
| 0x04 | 5    | GPIO5_DEB_EN  | RW   | 0x0     | GPIO5 debounce enable:<br>- `0`: Disabled<br>- `1`: Enabled  |
| 0x04 | 4    | GPIO4_DEB_EN  | RW   | 0x0     | GPIO4 debounce enable:<br>- `0`: Disabled<br>- `1`: Enabled   |
| 0x04 | 3    | GPIO3_DEB_EN  | RW   | 0x0     | GPIO3 debounce enable:<br>- `0`: Disabled<br>- `1`: Enabled  |
| 0x04 | 2    | GPIO2_DEB_EN  | RW   | 0x0     | GPIO2 debounce enable:<br>- `0`: Disabled<br>- `1`: Enabled   |
| 0x04 | 1    | GPIO1_DEB_EN  | RW   | 0x0     | GPIO1 debounce enable:<br>- `0`: Disabled<br>- `1`: Enabled  |
| 0x04 | 0    | GPIO0_DEB_EN  | RW   | 0x0     | GPIO0 debounce enable:<br>- `0`: Disabled<br>- `1`: Enabled   |

##### Table 7-9 GPIO_OD

| Addr | Bits | Field Name | Attr | Default | Description    |
| ---- | ---- | ---------- | ---- | ------- | --------|
| 0x05 | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                      |
| 0x05 | 5    | GPIO5_OD   | RW   | 0x0     | GPIO5 open-drain output configuration:<br>- `0`: Push-pull output<br>- `1`: Open-drain output |
| 0x05 | 4    | GPIO4_OD   | RW   | 0x0     | GPIO4 open-drain output configuration:<br>- `0`: Push-pull output<br>- `1`: Open-drain output |
| 0x05 | 3    | GPIO3_OD   | RW   | 0x0     | GPIO3 open-drain output configuration:<br>- `0`: Push-pull output<br>- `1`: Open-drain output |
| 0x05 | 2    | GPIO2_OD   | RW   | 0x0     | GPIO2 open-drain output configuration:<br>- `0`: Push-pull output<br>- `1`: Open-drain output |
| 0x05 | 1    | GPIO1_OD   | RW   | 0x0     | GPIO1 open-drain output configuration:<br>- `0`: Push-pull output<br>- `1`: Open-drain output |
| 0x05 | 0    | GPIO0_OD   | RW   | 0x0     | GPIO0 open-drain output configuration:<br>- `0`: Push-pull output<br>- `1`: Open-drain output |

##### Table 7-10 GPIO_ITYPE0

| Addr | Bits | Field Name  | Attr | Default | Description    |
| ---- | ---- | ----------- | ---- | ------- | --------------|
| 0x06 | 7:6  | Reserved    | RV   | 0       | Reserved    |
| 0x06 | 5:4  | GPIO2_ITYPE | RWE  | 0x0     | GPIO2 interrupt type:<br>`00`: Rising-edge triggered<br>`01`: Falling-edge triggered<br>`10`: High-level triggered<br>`11`: Low-level triggered |
| 0x06 | 3:2  | GPIO1_ITYPE | RWE  | 0x0     | GPIO1 interrupt type:<br>`00`: Rising-edge triggered<br>`01`: Falling-edge triggered<br>`10`: High-level triggered<br>`11`: Low-level triggered |
| 0x06 | 1:0  | GPIO0_ITYPE | RWE  | 0x0     | GPIO0 interrupt type:<br>`00`: Rising-edge triggered<br>`01`: Falling-edge triggered<br>`10`: High-level triggered<br>`11`: Low-level triggered |

##### Table 7-11 GPIO_ITYPE1

| Addr | Bits | Field Name  | Attr | Default | Description   |
| ---- | ---- | ----------- | ---- | ------- | ------- |
| 0x07 | 7:6  | Reserved    | RV   | 0       | Reserved                                                                                                                                        |
| 0x07 | 5:4  | GPIO5_ITYPE | RWE  | 0x0     | GPIO5 interrupt type:<br>`00`: Rising-edge triggered<br>`01`: Falling-edge triggered<br>`10`: High-level triggered<br>`11`: Low-level triggered |
| 0x07 | 3:2  | GPIO4_ITYPE | RWE  | 0x0     | GPIO4 interrupt type:<br>`00`: Rising-edge triggered<br>`01`: Falling-edge triggered<br>`10`: High-level triggered<br>`11`: Low-level triggered |
| 0x07 | 1:0  | GPIO3_ITYPE | RWE  | 0x0     | GPIO3 interrupt type:<br>`00`: Rising-edge triggered<br>`01`: Falling-edge triggered<br>`10`: High-level triggered<br>`11`: Low-level triggered |

##### Table 7-12 GPIO_MODE0

| Addr | Bits | Field Name | Attr | Default | Description    |
| ---- | ---- | ---------- | ---- | ------- | --------- |
| 0x08 | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                                      |
| 0x08 | 5:4  | GPIO2_MODE | RWE  | 0x0     | GPIO2 mode selection:<br>`00`: Input mode<br>`01`: Output mode<br>`1x`: Alternate (multiplexed) function mode |
| 0x08 | 3:2  | GPIO1_MODE | RWE  | 0x0     | GPIO1 mode selection:<br>`00`: Input mode<br>`01`: Output mode<br>`1x`: Alternate (multiplexed) function mode |
| 0x08 | 1:0  | GPIO0_MODE | RWE  | 0x0     | GPIO0 mode selection:<br>`00`: Input mode<br>`01`: Output mode<br>`1x`: Alternate (multiplexed) function mode |

##### Table 7-13 GPIO_MODE1

| Addr | Bits | Field Name | Attr | Default | Description  |
| ---- | ---- | ---------- | ---- | ------- | ---------|
| 0x09 | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                                      |
| 0x09 | 5:4  | GPIO5_MODE | RWE  | 0x0     | GPIO5 mode selection:<br>`00`: Input mode<br>`01`: Output mode<br>`1x`: Alternate (multiplexed) function mode |
| 0x09 | 3:2  | GPIO4_MODE | RWE  | 0x0     | GPIO4 mode selection:<br>`00`: Input mode<br>`01`: Output mode<br>`1x`: Alternate (multiplexed) function mode |
| 0x09 | 1:0  | GPIO3_MODE | RWE  | 0x0     | GPIO3 mode selection:<br>`00`: Input mode<br>`01`: Output mode<br>`1x`: Alternate (multiplexed) function mode |

##### Table 7-14 GPIO_AF01

| Addr | Bits | Field Name | Attr | Default | Description   |
| ---- | ---- | ---------- | ---- | ------- | -------------- |
| 0x0A | 7:6  | Reserved   | RV   | 0       | Reserved |
| 0x0A | 5:3  | GPIO1_AFR  | RWE  | 0x0     | GPIO1 alternate function selection:<br>`000`: External power enable output (EXT_EN)<br>`001`: External power-up sequence control input (PWRCTRL)<br>`010`: External sleep / wake-up control input (Sleep/Wakeup)<br>`011`: External reset control input (nReset)<br>`1xx`: ADC input (ADCIN) |
| 0x0A | 2:0  | GPIO0_AFR  | RWE  | 0x0     | GPIO0 alternate function selection:<br>`000`: External power enable output (EXT_EN)<br>`001`: External power-up sequence control input (PWRCTRL)<br>`010`: External sleep / wake-up control input (Sleep/Wakeup)<br>`011`: External reset control input (nReset)<br>`1xx`: ADC input (ADCIN) |

##### Table 7-15 GPIO_AF23

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                                                                                                                                                  |
| ---- | ---- | ---------- | ---- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0B | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                                                                                                                                                                                                                     |
| 0x0B | 5:3  | GPIO3_AFR  | RWE  | 0x0     | GPIO3 alternate function selection:<br>`000`: External power enable output (EXT_EN)<br>`001`: External power-up sequence control input (PWRCTRL)<br>`010`: External sleep / wake-up control input (Sleep/Wakeup)<br>`011`: External reset control input (nReset)<br>`1xx`: ADC input (ADCIN) |
| 0x0B | 2:0  | GPIO2_AFR  | RWE  | 0x0     | GPIO2 alternate function selection:<br>`000`: External power enable output (EXT_EN)<br>`001`: External power-up sequence control input (PWRCTRL)<br>`010`: External sleep / wake-up control input (Sleep/Wakeup)<br>`011`: External reset control input (nReset)<br>`1xx`: ADC input (ADCIN) |


##### Table 7-16 GPIO_AF45

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                                                                                                                                                  |
| ---- | ---- | ---------- | ---- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0C | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                                                                                                                                                                                                                     |
| 0x0C | 5:3  | GPIO5_AFR  | RWE  | 0x0     | GPIO5 alternate function selection:<br>`000`: External power enable output (EXT_EN)<br>`001`: External power-up sequence control input (PWRCTRL)<br>`010`: External sleep / wake-up control input (Sleep/Wakeup)<br>`011`: External reset control input (nReset)<br>`1xx`: ADC input (ADCIN) |
| 0x0C | 2:0  | GPIO4_AFR  | RWE  | 0x0     | GPIO4 alternate function selection:<br>`000`: External power enable output (EXT_EN)<br>`001`: External power-up sequence control input (PWRCTRL)<br>`010`: External sleep / wake-up control input (Sleep/Wakeup)<br>`011`: External reset control input (nReset)<br>`1xx`: ADC input (ADCIN) |

##### Table 7-17 RTC_COUNT_S

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                               |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| 0x0D | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                                                  |
| 0x0D | 5:0  | COUNT_S    | RW   | 0x00    | RTC seconds read register.<br>Reading this register latches the current calendar values into `COUNT_S` through `COUNT_Y`. |


##### Table 7-18 RTC_COUNT_MI

| Addr | Bits | Field Name | Attr | Default | Description                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ----------------------------------------------------------------------------------- |
| 0x0E | 7:6  | Reserved   | RV   | 0       | Reserved                                                                            |
| 0x0E | 5:0  | COUNT_MI   | RW   | 0x00    | RTC minutes read register. Reading this register returns the current minutes value. |

##### Table 7-19 RTC_COUNT_H

| Addr | Bits | Field Name | Attr | Default | Description                                                                    |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------ |
| 0xF  | 7:5  | Reserved   | RV   | 0       | Reserved                                                                       |
| 0xF  | 4:0  | COUNT_H    | RW   | 0x00    | RTC hours read register. Reading this register returns the current hour value. |


##### Table 7-20 RTC_COUNT_D

| Addr | Bits | Field Name | Attr | Default | Description                                                                  |
| ---- | ---- | ---------- | ---- | ------- | ---------------------------------------------------------------------------- |
| 0x10 | 7:5  | Reserved   | RV   | 0       | Reserved                                                                     |
| 0x10 | 4:0  | COUNT_D    | RW   | 0x00    | RTC days read register. Reading this register returns the current day value. |


##### Table 7-21 RTC_COUNT_MO

| Addr | Bits | Field Name | Attr | Default | Description                                                                      |
| ---- | ---- | ---------- | ---- | ------- | -------------------------------------------------------------------------------- |
| 0x11 | 7:4  | Reserved   | RV   | 0       | Reserved                                                                         |
| 0x11 | 3:0  | COUNT_MO   | RW   | 0x00    | RTC months read register. Reading this register returns the current month value. |


##### Table 7-22 RTC_COUNT_Y

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                             |
| ---- | ---- | ---------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x12 | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                                                                                                |
| 0x12 | 5:0  | COUNT_Y    | RW   | 0x00    | RTC years read/write register. Writing to this register updates the calendar counter with the current COUNT_S ~ COUNT_Y values, and resets RTC_SECOND_A ~ RTC_SECOND_D. |

##### Table 7-23 RTC_ALARM_S

| Addr | Bits | Field Name   | Attr | Default | Description                                    |
| ---- | ---- | ------------ | ---- | ------- | ---------------------------------------------- |
| 0x13 | 7    | MASK_ALARM_S | RW   | 0x0     | ALARM_S match mask: <br>`0`: not masked <br> `1`: masked |
| 0x13 | 6    | Reserved     | RV   | 0       | Reserved                                       |
| 0x13 | 5:0  | ALARM_S      | RW   | 0x00    | RTC_ALARM seconds setting, range 0x00 ~ 0x3B   |

##### Table 7-24 RTC_ALARM_MI

| Addr | Bits | Field Name    | Attr | Default | Description                                     |
| ---- | ---- | ------------- | ---- | ------- | ----------------------------------------------- |
| 0x14 | 7    | MASK_ALARM_MI | RW   | 0x0     | ALARM_MI match mask: <br>`0`:not masked <br>`1`: masked |
| 0x14 | 6    | Reserved      | RV   | 0       | Reserved                                        |
| 0x14 | 5:0  | ALARM_MI      | RW   | 0x00    | RTC_ALARM minutes setting, range 0x00 ~ 0x3B    |


##### Table 7-25 RTC_ALARM_H

| Addr | Bits | Field Name   | Attr | Default | Description                                    |
| ---- | ---- | ------------ | ---- | ------- | ---------------------------------------------- |
| 0x15 | 7    | MASK_ALARM_H | RW   | 0x0     | ALARM_H match mask: <br>`0`: not masked <br>`1`: masked |
| 0x15 | 6:5  | Reserved     | RV   | 0       | Reserved                                       |
| 0x15 | 4:0  | ALARM_H      | RW   | 0x00    | RTC_ALARM hours setting, range 0x00 ~ 0x17     |

##### Table 7-26 RTC_ALARM_D

| Addr | Bits | Field Name   | Attr | Default | Description                                    |
| ---- | ---- | ------------ | ---- | ------- | ---------------------------------------------- |
| 0x16 | 7    | MASK_ALARM_D | RW   | 0x0     | ALARM_D match mask: <br>`0`: not masked <br>``1`: masked |
| 0x16 | 6:5  | Reserved     | RV   | 0       | Reserved                                       |
| 0x16 | 4:0  | ALARM_D      | RW   | 0x00    | RTC_ALARM days setting, range 0x00 ~ 0x1F      |


##### Table 7-27 RTC_ALARM_MO

| Addr | Bits | Field Name    | Attr | Default | Description                                     |
| ---- | ---- | ------------- | ---- | ------- | ----------------------------------------------- |
| 0x17 | 7    | MASK_ALARM_MO | RW   | 0x0     | ALARM_MO match mask: <br>`0`: not masked <br>`1`: masked |
| 0x17 | 6:4  | Reserved      | RV   | 0       | Reserved                                        |
| 0x17 | 3:0  | ALARM_MO      | RW   | 0x00    | RTC_ALARM months setting, range 0x00 ~ 0x0C     |


##### Table 7-28 RTC_ALARM_Y

| Addr | Bits | Field Name   | Attr | Default | Description                                    |
| ---- | ---- | ------------ | ---- | ------- | ---------------------------------------------- |
| 0x18 | 7    | MASK_ALARM_Y | RW   | 0x0     | ALARM_Y match mask: <br>`0`: not masked <br> `1`: masked |
| 0x18 | 6    | Reserved     | RV   | 0       | Reserved                                       |
| 0x18 | 5:0  | ALARM_Y      | RW   | 0x00    | RTC_ALARM years setting, range 0x00 ~ 0x3F     |

##### Table 7-29 RTC_SECOND_A

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                 |
| ---- | ---- | ---------- | ---- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| 0x19 | 7:0  | SECOND_A   | R    | 0x00    | RTC seconds counter [7:0]. Reading this register updates the current 32-bit seconds counter value into SECOND_A ~ SECOND_D. |


##### Table 7-30 RTC_SECOND_B

| Addr | Bits | Field Name | Attr | Default | Description                 |
| ---- | ---- | ---------- | ---- | ------- | --------------------------- |
| 0x1A | 7:0  | SECOND_B   | R    | 0x00    | RTC seconds counter [15:8]. |


##### Table 7-31 RTC_SECOND_C

| Addr | Bits | Field Name | Attr | Default | Description                  |
| ---- | ---- | ---------- | ---- | ------- | ---------------------------- |
| 0x1B | 7:0  | SECOND_C   | R    | 0x00    | RTC seconds counter [23:16]. |


##### Table 7-32 RTC_SECOND_D

| Addr | Bits | Field Name | Attr | Default | Description                  |
| ---- | ---- | ---------- | ---- | ------- | ---------------------------- |
| 0x1C | 7:0  | SECOND_D   | R    | 0x00    | RTC seconds counter [31:24]. |

##### Table 7-33 RTC_CTRL

| Addr | Bits | Field Name      | Attr | Default | Description                                                |
| ---- | ---- | --------------- | ---- | ------- | ---------------------------------------------------------- |
| 0x1D | 7    | Reserved        | RV   | 0       | Reserved                                                   |
|      | 6    | TICK_EN(*1)     | RW   | 0x0     | TICK enable:<br><b>`0`</b>: disable<br><b>`1`</b>: enable                       |
|      | 5    | ALARM_EN(*1)    | RW   | 0x0     | ALARM enable:<br><b>`0`</b>: disable<br><b>`1`</b>: enable                      |
|      | 4    | TICK_TYPE(*1)   | RW   | 0x0     | TICK period select:<br><b>`0`</b>: 1s<br><b>`1`</b>: 1min                       |
|      | 3    | RTC_CLK_SEL(*1) | RW   | 0x0     | RTC clock select:<br><b>`0`</b>: internal 32kHz<br><b>`1`</b>: external crystal |
|      | 2    | RTC_EN(*1)      | RW   | 0x0     | RTC enable:<br><b>`0`</b>: disable<br><b>`1`</b>: enable                        |
|      | 1    | OUT_32K_EN(*2)  | RWE  | 0x0     | RTC clock output enable:<br><b>`0`</b>: disable<br><b>`1`</b>: enable           |
|      | 0    | CRYSTAL_EN(*3)  | RWE  | 0x0     | External crystal enable:<br><b>`0`</b>: disable<br><b>`1`</b>: enable           |

> Notes:
> (*1) Values remain unchanged in shutdown mode
> (*2) On entering shutdown mode = 0, restored from MTP on boot event
> (*3) On entering shutdown mode, restored from MTP on boot event

##### Table 7-34 ADC_CTRL(*1)

| Addr | Bits | Field Name | Attr | Default | Description    |
| ---- | ---- | ---------- | ---- | ------- | ---------------------- |
| 0x1E | 7:2  | Reserved   | RV   | 0       | Reserved  |
|      | 1    | ADC_GO(*2) | RW   | 0       | ADC conversion start bit:<br><b>`0`</b>: conversion done/not started<br><b>`1`</b>: conversion in progress.<br>In manual mode, set to `1` and cleared by hardware after each conversion; in auto mode, software clears to stop conversions; clearing during conversion stops it immediately. |
|      | 0    | ADC_EN     | RW   | 0       | ADC enable:<br><b>`0`</b>: disable<br><b>`1`</b>: enable       |
> Notes:
> (*1) Default restored on entering shutdown mode
> (*2) Behavior of ADC_GO as described above

##### Table 7-35 ADC_CFG0(*1)

| Addr | Bits | Field Name        | Attr | Default | Description  |
| ---- | ---- | ----------------- | ---- | ------- | --- |
| 0x1F | 7    | Reserved          | RV   | 0       | Reserved     |
|      | 6    | ADCTJ_DEB_EN(*1)  | RW   | 0x0     | ADC junction temperature threshold interrupt debounce: <br>`0` = disable <br>`1` = enable |
|      | 5    | ADCIN5_DEB_EN(*1) | RW   | 0x0     | ADCIN5 interrupt debounce: <br>`0`: disable <br>`1`: enable                             |
|      | 4    | ADCIN4_DEB_EN(*1) | RW   | 0x0     | ADCIN4 interrupt debounce: <br>`0`: disable <br>`1`: enable                             |
|      | 3    | ADCIN3_DEB_EN(*1) | RW   | 0x0     | ADCIN3 interrupt debounce: <br>`0`: disable <br>`1`: enable                             |
|      | 2    | ADCIN2_DEB_EN(*1) | RW   | 0x0     | ADCIN2 interrupt debounce: <br>`0`: disable <br>`1`: enable                             |
|      | 1    | ADCIN1_DEB_EN(*1) | RW   | 0x0     | ADCIN1 interrupt debounce: <br>`0`: disable <br>`1`: enable                             |
|      | 0    | ADCIN0_DEB_EN(*1) | RW   | 0x0     | ADCIN0 interrupt debounce: <br>`0`: disable <br>`1`: enable                             |

> Notes:
> (*1) Defaults restored on entering shutdown mode
> (*2) After `ADC_DEB_NUM` consecutive conversions exceed or fall below threshold, corresponding flag is set

##### Table 7-36 ADC_CFG1 (*1)

| Addr | Bits | Field Name    | Attr | Default | Description   |
| ---- | ---- | ------------- | ---- | ------- | ----------- |
| 0x20 | 7    | ADC_CHOP_SEL  | RW   | 0x0     | ADC chop clock selection:<br>`0`: 31.25 kHz<br>`1`: 62.5 kHz    |
|      | 6    | ADC_CHOP_EN   | RW   | 0x0     | ADC chop enable:<br>`0`: disable<br>`1`: enable   |
|      | 5:3  | ADC_CHNL_SEL  | RW   | 0x0     | ADC manual mode channel select:<br>`000`: Channel 0 – Vsys / BUCK / LDO voltage<br>`001`: Channel 1 – Tj (internal junction temperature)<br>`010`: Channel 2 – GPIO0 as ADC input (ADCIN0)<br>`011`: Channel 3 – GPIO1 as ADC input (ADCIN1)<br>`100`: Channel 4 – GPIO2 as ADC input (ADCIN2)<br>`101`: Channel 5 – GPIO3 as ADC input (ADCIN3)<br>`110`: Channel 6 – GPIO4 as ADC input (ADCIN4)<br>`111`: Channel 7 – GPIO5 as ADC input (ADCIN5) |
|      | 2:0  | ADC_SAMP_FREQ | RW   | 0x0     | Auto-scan sampling frequency selection:<br>`000`: 100 Hz<br>`001`: 781.25 Hz<br>`010`: 1.5625 kHz<br>`011`: 3.125 kHz<br>`100`: 6.25 kHz<br>`101`: 12.5 kHz<br>`110`: 25 kHz<br>`111`: 50 kHz  |

> Notes:
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-37 ADC_CFG2 (*1)

| Addr | Bits | Field Name    | Attr | Default | Description    |
| ---- | ---- | ------------- | ---- | ------- | ------------- |
| 0x21 | 7    | Reserved      | RV   | 0       | Reserved     |
|      | 6:4  | ADC_DEB_NUM   | RW   | 0x0     | ADC debounce count selection:<br>`000`: 2 consecutive triggers<br>`001`: 3 consecutive triggers<br>`010`: 4 consecutive triggers<br>`011`: 5 consecutive triggers<br>`100`: 6 consecutive triggers<br>Others: 7 consecutive triggers |
|      | 3:2  | ADC_VREFH_SEL | RW   | 0x0     | ADC positive reference selection:<br>`00`: Internal<br>`01`: VCC<br>`10`: External<br>`11`: Internal + capacitor     |
|      | 1:0  | ADC_REF_SEL   | RW   | 0x0     | ADC reference voltage selection:<br>`01`: 2 V internal reference<br>`10`: 3 V internal reference<br>Others: disable       |

> Notes:
> (*1) Restored to default value when entering shutdown mode.


##### Table 7-38 ADC_AUTO (*1)

| Addr | Bits | Field Name       | Attr | Default | Description        |
| ---- | ---- | ---------------- | ---- | ------- | ---- |
| 0x22 | 7    | Reserved         | RV   | 0       | Reserved   |
|      | 6    | AUTO_IN5_EN (*2) | RW   | 0x0     | ADCIN5 auto-sampling enable:<br>`0`: disable<br>`1`: enable                       |
|      | 5    | AUTO_IN4_EN (*2) | RW   | 0x0     | ADCIN4 auto-sampling enable:<br>`0`: disable<br>`1`: enable                       |
|      | 4    | AUTO_IN3_EN (*2) | RW   | 0x0     | ADCIN3 auto-sampling enable:<br>`0`: disable<br>`1`: enable                       |
|      | 3    | AUTO_IN2_EN (*2) | RW   | 0x0     | ADCIN2 auto-sampling enable:<br>`0`: disable<br>`1`: enable                       |
|      | 2    | AUTO_IN1_EN (*2) | RW   | 0x0     | ADCIN1 auto-sampling enable:<br>`0`: disable<br>`1`: enable                       |
|      | 1    | AUTO_IN0_EN (*2) | RW   | 0x0     | ADCIN0 auto-sampling enable:<br>`0`: disable<br>`1`: enable                       |
|      | 0    | AUTO_TJ_EN (*2)  | RW   | 0x0     | Junction temperature channel auto-sampling enable:<br>`0`: disable<br>`1`: enable |

> Notes:
> (*1) Restored to default value when entering shutdown mode.
> (*2) If any bit in `ADC_AUTO[6:0]` is set, the ADC enters automatic scan mode after conversion is started.


##### Table 7-39 ADC_MAN_EN0 (*1)

| Addr | Bits | Field Name   | Attr | Default | Description  |
| ---- | ---- | ------------ | ---- | ------- | --------|
| 0x23 | 7    | Reserved     | RV   | 0       | Reserved   |
| 0x23 | 6    | ADC_VSYS_EN  | RW   | 0x0     | VSYS voltage monitoring enable:<br>`0`: Monitoring disabled<br>`1`: Monitoring enabled |
| 0x23 | 5    | ADC_BUCK6_EN | RW   | 0x0     | BUCK6 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled               |
| 0x23 | 4    | ADC_BUCK5_EN | RW   | 0x0     | BUCK5 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled               |
| 0x23 | 3    | ADC_BUCK4_EN | RW   | 0x0     | BUCK4 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled               |
| 0x23 | 2    | ADC_BUCK3_EN | RW   | 0x0     | BUCK3 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled               |
| 0x23 | 1    | ADC_BUCK2_EN | RW   | 0x0     | BUCK2 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled               |
| 0x23 | 0    | ADC_BUCK1_EN | RW   | 0x0     | BUCK1 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled               |

> Note:
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-40 ADC_MAN_EN1 (*1)

| Addr | Bits | Field Name         | Attr | Default | Description                                                               |
| ---- | ---- | ------------------ | ---- | ------- | ------------------------------------------------------------------------- |
| 0x24 | 7    | ADC_DLDO3_EN (*2)  | RW   | 0x0     | DLDO3 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled  |
| 0x24 | 6    | ADC_DLDO2_EN (*2)  | RW   | 0x0     | DLDO2 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled  |
| 0x24 | 5    | ADC_DLDO1_EN (*2)  | RW   | 0x0     | DLDO1 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled  |
| 0x24 | 4    | ADC_ALDO4_EN (*2)  | RW   | 0x0     | ALDO4 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled  |
| 0x24 | 3    | ADC_ALDO3_EN (*2)  | RW   | 0x0     | ALDO3 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled  |
| 0x24 | 2    | ADC_ALDO2_EN (*2)  | RW   | 0x0     | ALDO2 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled  |
| 0x24 | 1    | ADC_ALDO1_EN (*2)  | RW   | 0x0     | ALDO1 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled  |
| 0x24 | 0    | ADC_AONLDO_EN (*2) | RW   | 0x0     | AONLDO output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled |

> Notes:
> (*1) Restored to default value when entering shutdown mode.
> (*2) When no automatic channel is enabled in `ADC_AUTO`, enabling any channel in `ADC_MAN_EN0`–`ADC_MAN_EN2` causes the ADC to enter manual mode after conversion is started.

##### Table 7-41 ADC_MAN_EN2 (*1)

| Addr | Bits | Field Name        | Attr | Default | Description                                                              |
| ---- | ---- | ----------------- | ---- | ------- | ------------------------------------------------------------------------ |
| 0x25 | 7:4  | Reserved          | RV   | 0       | Reserved                                                                 |
| 0x25 | 3    | ADC_DLDO7_EN (*2) | RW   | 0x0     | DLDO7 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled |
| 0x25 | 2    | ADC_DLDO6_EN (*2) | RW   | 0x0     | DLDO6 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled |
| 0x25 | 1    | ADC_DLDO5_EN (*2) | RW   | 0x0     | DLDO5 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled |
| 0x25 | 0    | ADC_DLDO4_EN (*2) | RW   | 0x0     | DLDO4 output voltage monitoring enable:<br>`0`: Disabled<br>`1`: Enabled |

> Notes:
> (*1) Restored to default value when entering shutdown mode.
> (*2) When no automatic channel is enabled in `ADC_AUTO`, enabling any channel in `ADC_MAN_EN0`–`ADC_MAN_EN2` causes the ADC to enter manual mode after conversion is started.

##### Table 7-42 ADC_MAN_RES_H (*1)

| Addr | Bits | Field Name | Attr | Default | Description        |
| ---- | ---- | ---------- | ---- | ------- | ----------------- |
| 0x26 | 7:0  | ADC_RES_H  | R    | 0x00    | 12-bit ADC manual conversion result (8 MSBs).<br>Reading this register latches the current 12-bit result of the selected manual conversion channel into `ADC_MAN_RES_H` and `ADC_MAN_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-43 ADC_MAN_RES_L (*1)

| Addr | Bits | Field Name | Attr | Default | Description                                   |
| ---- | ---- | ---------- | ---- | ------- | --------------------------------------------- |
| 0x27 | 7:4  | ADC_RES_L  | R    | 0x0     | 12-bit ADC manual conversion result (4 LSBs). |
| 0x27 | 3:0  | Reserved   | RV   | 0       | Reserved.                                     |

> Notes:
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-44 ADC_TJ_RES_H (*1)

| Addr | Bits | Field Name | Attr | Default | Description   |
| ---- | ---- | ---------- | ---- | ------- | ------------------- |
| 0x28 | 7:0  | TJ_RES_H   | R    | 0x00    | Junction temperature automatic conversion result (8 MSBs).<br>Reading this register latches the current junction temperature result into `ADC_TJ_RES_H` and `ADC_TJ_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-45 ADC_TJ_RES_L (*1)

| Addr | Bits | Field Name | Attr | Default | Description |
| ---- | ---- | ---------- | ---- | ------- | ----------- |
| 0x29 | 7:4  | TJ_RES_L   | R    | 0x0     | Junction temperature automatic conversion result (4 LSBs). |
| 0x29 | 3:0  | Reserved   | RV   | 0       | Reserved. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-46 ADC_IN0_RES_H (*1)

| Addr | Bits | Field Name   | Attr | Default | Description |
| ---- | ---- | ------------ | ---- | ------- | ----------- |
| 0x2A | 7:0  | ADCIN0_RES_H | R    | 0x00    | ADCIN0 automatic conversion result (8 MSBs).<br>Reading this register latches the current Channel 0 result into `ADC_IN0_RES_H` and `ADC_IN0_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-47 ADC_IN0_RES_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description |
| ---- | ---- | ------------ | ---- | ------- | ----------- |
| 0x2B | 7:4  | ADCIN0_RES_L | R    | 0x0     | ADCIN0 automatic conversion result (4 LSBs). |
| 0x2B | 3:0  | Reserved     | RV   | 0       | Reserved. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.


##### Table 7-48 ADC_IN1_RES_H (*1)

| Addr | Bits | Field Name   | Attr | Default | Description |
| ---- | ---- | ------------ | ---- | ------- | ----------- |
| 0x2C | 7:0  | ADCIN1_RES_H | R    | 0x0     | ADCIN1 automatic conversion result (8 MSBs).<br>Reading this register latches the current Channel 1 result into `ADC_IN1_RES_H` and `ADC_IN1_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-49 ADC_IN1_RES_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description |
| ---- | ---- | ------------ | ---- | ------- | ----------- |
| 0x2D | 7:4  | ADCIN1_RES_L | R    | 0x0     | ADCIN1 automatic conversion result (4 LSBs). |
| 0x2D | 3:0  | Reserved     | RV   | 0       | Reserved. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-50 ADC_IN2_RES_H (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x2E | 7:0  | ADCIN2_RES_H   | R    | 0x00    | ADCIN2 automatic conversion result (8 MSBs).<br>Reading this register latches the current Channel 2 result into `ADC_IN2_RES_H` and `ADC_IN2_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-51 ADC_IN2_RES_L (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x2F | 7:4  | ADCIN2_RES_L   | R    | 0x0     | ADCIN2 automatic conversion result (4 LSBs). |
| 0x2F | 3:0  | Reserved       | RV   | 0       | Reserved. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-52 ADC_IN3_RES_H (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x30 | 7:0  | ADCIN3_RES_H   | R    | 0x00    | ADCIN3 automatic conversion result (8 MSBs).<br>Reading this register latches the current Channel 3 result into `ADC_IN3_RES_H` and `ADC_IN3_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-53 ADC_IN3_RES_L (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x31 | 7:4  | ADCIN3_RES_L   | R    | 0x0     | ADCIN3 automatic conversion result (4 LSBs). |
| 0x31 | 3:0  | Reserved       | RV   | 0       | Reserved. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-54 ADC_IN4_RES_H (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x32 | 7:0  | ADCIN4_RES_H   | R    | 0x00    | ADCIN4 automatic conversion result (8 MSBs).<br>Reading this register latches the current Channel 4 result into `ADC_IN4_RES_H` and `ADC_IN4_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-55 ADC_IN4_RES_L (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x33 | 7:4  | ADCIN4_RES_L   | R    | 0x0     | ADCIN4 automatic conversion result (4 LSBs). |
| 0x33 | 3:0  | Reserved       | RV   | 0       | Reserved. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-56 ADC_IN5_RES_H (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x34 | 7:0  | ADCIN5_RES_H   | R    | 0x00    | ADCIN5 automatic conversion result (8 MSBs).<br>Reading this register latches the current Channel 5 result into `ADC_IN5_RES_H` and `ADC_IN5_RES_L`, preventing the lower bits from being overwritten by a new conversion and ensuring data consistency. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-57 ADC_IN5_RES_L (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x35 | 7:4  | ADCIN5_RES_L   | R    | 0x0     | ADCIN5 automatic conversion result (4 LSBs). |
| 0x35 | 3:0  | Reserved       | RV   | 0       | Reserved. |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-58 ADC_VTH_TJ_H (*1)

| Addr | Bits | Field Name | Attr | Default | Description |
| ---- | ---- | ---------- | ---- | ------- | ----------- |
| 0x36 | 7:0  | VTH_TJ_H   | RW   | 0x00    | Junction temperature monitoring upper threshold setting (8 MSBs). |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-59 ADC_VTH_TJ_L (*1)

| Addr | Bits | Field Name | Attr | Default | Description |
| ---- | ---- | ---------- | ---- | ------- | ----------- |
| 0x37 | 7:0  | VTH_TJ_L   | RW   | 0x00    | Junction temperature monitoring lower threshold setting (8 MSBs). |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-60 ADC_IN0_VTH_H (*1)

| Addr | Bits | Field Name     | Attr | Default | Description |
| ---- | ---- | -------------- | ---- | ------- | ----------- |
| 0x38 | 7:0  | ADCIN0_VTH_H   | RW   | 0x00    | ADCIN0 monitoring upper threshold setting (8 MSBs). |

> Notes:  
> (*1) Restored to default value when entering shutdown mode.

##### Table 7-61 ADC_IN0_VTH_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x39 | 7:0  | ADCIN0_VTH_L | RW   | 0x00    | ADCIN0 lower threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-62 ADC_IN1_VTH_H (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x3A | 7:0  | ADCIN1_VTH_H | RW   | 0x00    | ADCIN1 upper threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-63 ADC_IN1_VTH_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x3B | 7:0  | ADCIN1_VTH_L | RW   | 0x00    | ADCIN1 lower threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-64 ADC_IN2_VTH_H (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x3C | 7:0  | ADCIN2_VTH_H | RW   | 0x00    | ADCIN2 upper threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-65 ADC_IN2_VTH_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x3D | 7:0  | ADCIN2_VTH_L | RW   | 0x00    | ADCIN2 lower threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-66 ADC_IN3_VTH_H (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x3E | 7:0  | ADCIN3_VTH_H | RW   | 0x00    | ADCIN3 upper threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-67 ADC_IN3_VTH_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x3F | 7:0  | ADCIN3_VTH_L | RW   | 0x00    | ADCIN3 lower threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-68 ADC_IN4_VTH_H (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x40 | 7:0  | ADCIN4_VTH_H | RW   | 0x00    | ADCIN4 upper threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-69 ADC_IN4_VTH_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x41 | 7:0  | ADCIN4_VTH_L | RW   | 0x00    | ADCIN4 lower threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-70 ADC_IN5_VTH_H (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x42 | 7:0  | ADCIN5_VTH_H | RW   | 0x00    | ADCIN5 upper threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-71 ADC_IN5_VTH_L (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                             |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------- |
| 0x43 | 7:0  | ADCIN5_VTH_L | RW   | 0x00    | ADCIN5 lower threshold setting (8 MSBs) |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-72 WDT_CTRL (*1)

| Addr | Bits | Field Name | Attr | Default | Description                                                                                     |
| ---- | ---- | ---------- | ---- | ------- | ----------------------------------------------------------------------------------------------- |
| 0x44 | 7:4  | Reserved   | RV   | 0       | Reserved                                                                                        |
| 0x44 | 3    | WDT_EN     | RW   | 0x0     | Watchdog enable:<br>`0`: Disabled<br>`1`: Enabled                                               |
| 0x44 | 2:1  | WDT_SCALE  | RW   | 0x0     | Watchdog timeout configuration:<br>`00`: 1 s<br>`01`: 4 s<br>`10`: 8 s<br>`11`: 16 s            |
| 0x44 | 0    | WDT_FEED   | RW   | 0x0     | Watchdog counter clear:<br>Write `1`: Clear WDT counter<br>Hardware automatically clears to `0` |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-73 BBAT_CTRL (*1)

| Addr | Bits | Field Name | Attr | Default | Description                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | --------------------------------------------------------------------------------------------------- |
| 0x45 | 7:5  | Reserved   | RV   | 0       | Reserved                                                                                            |
| 0x45 | 4:3  | BCHG_ISET  | RW   | 0x0     | Coin-cell charging current setting:<br>`100`: 500 µA<br>`101`: 1 mA<br>`110`: 2 mA<br>`111`: 4 mA   |
| 0x45 | 2:1  | BCHG_VSET  | RW   | 0x0     | Coin-cell charging voltage setting:<br>`100`: 2.8 V<br>`101`: 2.9 V<br>`110`: 3.0 V<br>`111`: 3.1 V |
| 0x45 | 0    | BCHG_EN    | RW   | 0x0     | Coin-cell charging enable:<br>`0`: Disabled<br>`1`: Enabled                                         |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-74 BUCK_LDO_CFG (*1)

| Addr | Bits | Field Name     | Attr | Default | Description                                                                                                                                                                                                  |
| ---- | ---- | -------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x46 | 7    | LDO_PD_EN      | RWE  | 0       | LDO pull-down resistor enable:<br>`0`: Disabled<br>`1`: Enabled<br>When LDO is enabled, this bit has no effect (pull-down disabled); when LDO is disabled, the pull-down resistor is controlled by this bit. |
| 0x46 | 6    | BUCK_PD_EN     | RWE  | 0x0     | BUCK pull-down resistor enable:<br>`0`: Disabled<br>`1`: Enabled<br>When BUCK is enabled, this bit has no effect; when BUCK is disabled, the pull-down resistor is controlled by this bit.                   |
| 0x46 | 5    | BUCK_DVS_EN    | RWE  | 0x0     | BUCK DVS enable:<br>`0`: Disabled<br>`1`: Enabled<br>DVS is not active during power-up; DVS is applied only during power-on/off and sleep/wake transitions.                                                  |
| 0x46 | 4:3  | BUCK_DVS_SEL   | RWE  | 0x0     | BUCK DVS slew rate selection:<br>`00`: 5 mV/µs<br>`01`: 10 mV/µs<br>`10`: 25 mV/µs<br>`11`: 50 mV/µs                                                                                                         |
| 0x46 | 2    | BUCK_VSET_CTRL | RWE  | 0x0     | BUCK5/6 VSET pin voltage selection:<br>`0`: VSET=VDD: 1.1 V, FLOATING: BUCKx_VOLT, GND: 1.2 V<br>`1`: VSET=VDD: 0.6 V, FLOATING: BUCKx_VOLT, GND: 1.5 V                                                      |
| 0x46 | 1    | BUCK_34_DUAL   | RWE  | 0x0     | BUCK3 and BUCK4 dual-phase mode enable:<br>`0`: Disabled<br>`1`: Enabled                                                                                                                                     |
| 0x46 | 0    | BUCK_12_DUAL   | RWE  | 0x0     | BUCK1 and BUCK2 dual-phase mode enable:<br>`0`: Disabled<br>`1`: Enabled                                                                                                                                     |

> Note:
> (*1) Value is retained in power-down mode and restored from MTP after a power-on event.

##### Table 7-75 BUCKx_CTRL (*1)

| Addr          | Bits | Field Name     | Attr | Default | Description                                                                                                                                                                                        |
| ------------- | ---- | -------------- | ---- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x47+3xN (*2) | 7:6  | Reserved       | RV   | 0       | Reserved                                                                                                                                                                                           |
| 0x47+3xN (*2) | 5:3  | BUCKx_GPIO_SEL | RE   | 0x0     | GPIO (PWRCTRL) control of BUCK enable:<br>`000`: Not GPIO-controlled<br>`001`: GPIO0<br>`010`: GPIO1<br>`011`: GPIO2<br>`100`: GPIO3<br>`101`: GPIO4<br>`110`: GPIO5<br>`111`: Not GPIO-controlled |
| 0x47+3xN (*2) | 2    | BUCKx_MODE     | RWE  | 0x0     | BUCK operating mode:<br>`0`: PFM/PWM auto-switch<br>`1`: Forced PWM                                                                                                                                |
| 0x47+3xN (*2) | 1    | BUCKx_ILIM     | RWE  | 0x0     | BUCK current limit selection:<br>`0`: BUCK1–2: 5000 mA; BUCK3–6: 3500 mA<br>`1`: BUCK1–2: 7500 mA; BUCK3–6: 5000 mA                                                                                |
| 0x47+3xN (*2) | 0    | BUCKx_EN       | RWE  | 0x0     | BUCK enable:<br>`0`: Disabled<br>`1`: Enabled                                                                                                                                                      |

> Note:
> (*1) Value is retained in power-down mode and restored from MTP after a power-on event.
> (*2) N = 0–5, x = 1–6, corresponding to BUCK1–BUCK6.

##### Table 7-76 BUCKx_VOLT (*1)

| Addr          | Bits | Field Name | Attr | Default | Description                                                                                                                                                                                                                        |
| ------------- | ---- | ---------- | ---- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x48+3xN (*2) | 7:0  | BUCKx_VOLT | RWE  | 0x00    | BUCK output voltage setting (8 MSBs):<br>0.5 V–1.35 V: 5 mV/step<br>1.375 V–3.45 V: 25 mV/step<br>`00000000`: 0.500 V<br>`00000001`: 0.505 V<br>`00000010`: 0.510 V<br>...<br>`11111110`: 3.450 V<br>`11111111`: Write not allowed |

> Note:
> (*1) Value is retained in power-down mode and restored from MTP after a power-on event.
> (*2) N = 0–5, x = 1–6, corresponding to BUCK1–BUCK6.

##### Table 7-77 BUCKx_SLP_VOLT (*1)

| Addr          | Bits | Field Name     | Attr | Default | Description                                                                                                                                                                                                                                 |
| ------------- | ---- | -------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x49+3xN (*2) | 7:0  | BUCKx_SLP_VOLT | RWE  | 0x00    | BUCK sleep-mode output voltage setting (8 MSBs):<br>0.5 V–1.35 V: 5 mV/step<br>1.375 V–3.45 V: 25 mV/step<br>`00000000`: 0.500 V<br>`00000001`: 0.505 V<br>`00000010`: 0.510 V<br>...<br>`11111110`: 3.450 V<br>`11111111`: 0 V (BUCKx off) |

> Note:
> (*1) Value is retained in power-down mode and restored from MTP after a power-on event.
> (*2) N = 0–5, x = 1–6, corresponding to BUCK1–BUCK6.

##### Table 7-78 SWITCH_CTRL (*1)

| Addr | Bits | Field Name   | Attr | Default | Description                                                                                                                                                                                                                               |
| ---- | ---- | ------------ | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x59 | 7:2  | Reserved     | RV   | 0       | Reserved                                                                                                                                                                                                                                  |
| 0x59 | 1    | SWITCH_PD_EN | RW   | 0x0     | SWITCH pull-down resistor enable:<br>`0`: Disabled<br>`1`: Enabled<br>When SWITCH_EN is enabled, the pull-down resistor is disabled and this bit has no effect; the pull-down resistor is controlled by this bit only when SWITCH_EN = 0. |
| 0x59 | 0    | SWITCH_EN    | RW   | 0x0     | SWITCH enable:<br>`0`: Disabled<br>`1`: Enabled                                                                                                                                                                                           |

> Note:
> (*1) Default value is restored when entering power-down mode.

##### Table 7-79 AONLDO_CTRL (*1)

| Addr | Bits | Field Name  | Attr | Default | Description                                                                                                                                                                        |
| ---- | ---- | ----------- | ---- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x5A | 7:1  | AONLDO_VOLT | RE   | 0x00    | AONLDO output voltage setting (7 MSBs):<br>0.5 V–3.4 V: 25 mV/step<br>`0001011`: 0.500 V<br>`0001100`: 0.525 V<br>`0001101`: 0.550 V<br>...<br>`1111111`: 3.400 V<br>Others: 0.5 V |
| 0x5A | 0    | Reserved    | RV   | 1       | Reserved                                                                                                                                                                           |

> Note:
> (*1) Value is retained in power-down mode and restored from MTP after a power-on event.

##### Table 7-80 ALDOx_CTRL (*1)

| Addr          | Bits | Field Name     | Attr | Default | Description                                                                                                                                                                                         |
| ------------- | ---- | -------------- | ---- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x5B+3xN (*2) | 7:4  | Reserved       | RV   | 0       | Reserved                                                                                                                                                                                            |
| 0x5B+3xN (*2) | 3:1  | ALDOx_GPIO_SEL | RE   | 0x0     | GPIO (PWRCTRL) control of ALDOx enable:<br>`000`: Not GPIO-controlled<br>`001`: GPIO0<br>`010`: GPIO1<br>`011`: GPIO2<br>`100`: GPIO3<br>`101`: GPIO4<br>`110`: GPIO5<br>`111`: Not GPIO-controlled |
| 0x5B+3xN (*2) | 0    | ALDOx_EN       | RWE  | 0x0     | ALDOx enable:<br>`0`: Disabled<br>`1`: Enabled                                                                                                                                                      |

> Note:
> (*1) Value is retained in power-down mode and restored from MTP after a power-on event.
> (*2) N = 0–3, x = 1–4, corresponding to ALDO1–ALDO4.

##### Table 7-81 ALDOx_VOLT (*1)

| Addr          | Bits | Field Name | Attr | Default | Description                                                                                                                                                              |
| ------------- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x5C+3xN (*2) | 7    | Reserved   | RV   | 0       | Reserved                                                                                                                                                                 |
| 0x5C+3xN (*2) | 6:0  | ALDOx_VOLT | RWE  | 0x0     | ALDOx voltage output level (7 MSBs)<br>0.5 V ~ 3.4 V, 25 mV/step<br>`0001011`: 0.500 V<br>`0001100`: 0.525 V<br>`0001101`: 0.550 V<br>...<br>`1111111`: 3.400 V<br>others: 0.5 V |

> Note:
> (*1) Value remains unchanged when entering shutdown mode and is restored to the value stored in MTP after a power-on event.
> (*2) N: 0 ~ 3, x: 1 ~ 4, corresponding to ALDO1 ~ ALDO4.

##### Table 7-82 ALDOx_SLP_VOLT (*1)

| Addr          | Bits | Field Name     | Attr | Default | Description                                                                                                                                                                         |
| ------------- | ---- | -------------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x5D+3xN (*2) | 7    | Reserved       | RV   | 0       | Reserved                                                                                                                                                                            |
| 0x5D+3xN (*2) | 6:0  | ALDOx_SLP_VOLT | RWE  | 0x0     | ALDOx sleep-mode voltage output level (7 MSBs)<br>0.5 V ~ 3.4 V, 25 mV/step<br>`0001011`: 0.500 V<br>`0001100`: 0.525 V<br>`0001101`: 0.550 V<br>...<br>`1111111`: 3.400 V<br>others: 0.5 V |

> Note:
> (*1) Value remains unchanged when entering shutdown mode and is restored to the value stored in MTP after a power-on event.
> (*2) N: 0 ~ 3, x: 1 ~ 4, corresponding to ALDO1 ~ ALDO4.

##### Table 7-83 DLDOx_CTRL

| Addr          | Bits | Field Name     | Attr | Default | Description                                                                                                                                                                                                                                                                  |
| ------------- | ---- | -------------- | ---- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x67+3xN (*1) | 7:4  | Reserved       | RV   | 0       | Reserved                                                                                                                                                                                                                                                                     |
| 0x67+3xN (*1) | 3:1  | DLDOx_GPIO_SEL | RE   | 0x0     | GPIO (PWRCTRL) control of DLDOx enable<br>`000`: Not controlled by GPIO<br>`001`: Controlled by GPIO0<br>`010`: Controlled by GPIO1<br>`011`: Controlled by GPIO2<br>`100`: Controlled by GPIO3<br>`101`: Controlled by GPIO4<br>`110`: Controlled by GPIO5<br>`111`: Not controlled by GPIO |
| 0x67+3xN (*1) | 0    | DLDOx_EN       | RWE  | 0x0     | DLDOx enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                                                                                                                                                      |

> Note:
> (*1) N: 0 ~ 6, x: 1 ~ 7, corresponding to DLDO1 ~ DLDO7.

##### Table 7-84 DLDOx_VOLT

| Addr          | Bits | Field Name | Attr | Default | Description                                                                                                                                                              |
| ------------- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x68+3xN (*1) | 7    | Reserved   | RV   | 0       | Reserved                                                                                                                                                                 |
| 0x68+3xN (*1) | 6:0  | DLDOx_VOLT | RWE  | 0x0     | DLDOx voltage output level (7 MSBs)<br>0.5 V ~ 3.4 V, 25 mV/step<br>`0001011`: 0.500 V<br>`0001100`: 0.525 V<br>`0001101`: 0.550 V<br>...<br>`1111111`: 3.400 V<br>others: 0.5 V |

> Note:
> (*1) N: 0 ~ 6, x: 1 ~ 7, corresponding to DLDO1 ~ DLDO7.

##### Table 7-85 DLDOx_SLP_VOLT

| Addr          | Bits | Field Name     | Attr | Default | Description                                                                                                                                                                         |
| ------------- | ---- | -------------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x69+3xN (*1) | 7    | Reserved       | RV   | 0       | Reserved                                                                                                                                                                            |
| 0x69+3xN (*1) | 6:0  | DLDOx_SLP_VOLT | RWE  | 0x0     | DLDOx sleep-mode voltage output level (7 MSBs)<br>0.5 V ~ 3.4 V, 25 mV/step<br>`0001011`: 0.500 V<br>`0001100`: 0.525 V<br>`0001101`: 0.550 V<br>...<br>`1111111`: 3.400 V<br>others: 0.5 V |

> Note:
> (*1) N: 0 ~ 6, x: 1 ~ 7, corresponding to DLDO1 ~ DLDO7.

##### Table 7-86 PWR_CTRL0

| Addr | Bits | Field Name      | Attr | Default | Description                                                                                                                                                                   |
| ---- | ---- | --------------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x7C | 7    | WDT_RST_EN      | RW   | 0x0     | WDT timeout reset enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                                           |
| 0x7C | 6    | NRESET_RST_EN   | RW   | 0x0     | nRESET pin pull-down triggered reset enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                        |
| 0x7C | 5    | PWRCTRL_SHUT_EN | RWE  | 0x0     | PWRCTRL all-bound invalid shutdown enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                          |
| 0x7C | 4    | PWRCTRL_STA_EN  | RE   | 0x0     | PWRCTRL all-bound valid power-on enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                            |
| 0x7C | 3    | RTC_STA_EN      | RE   | 0x0     | RTC TICK / ALARM triggered power-on enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                         |
| 0x7C | 2    | INT_STA_EN      | RE   | 0x0     | INT pin triggered power-on enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                                  |
| 0x7C | 1    | VSYS_STA_EN     | RE   | 0x0     | VSYS rising-edge triggered power-on enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable<br>When enabled, the device powers on once VSYS exceeds the configured threshold after initial power-up |
| 0x7C | 0    | Reserved        | RV   | 1       | Reserved                                                                                                                                                                      |

##### Table 7-87 PWR_CTRL1

| Addr | Bits | Field Name   | Attr | Default | Description                                                                                                                                                                 |
| ---- | ---- | ------------ | ---- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x7D | 7    | SD_LOW_POWER | RW   | 0x0     | Enter standby mode in shutdown state<br><b>`0`</b>: Do not enter<br><b>`1`</b>: Enter<br>In standby mode, internal bandgap and AON LDO are disabled; only PWRKY and RTC wake-up are available |
| 0x7D | 6    | PG_RST_EN    | RWE  | 0x0     | PGOOD pin pull-down triggered reset enable<br><b>`0`</b>: Disable<br><b>`1`</b>: Enable                                                                                                       |
| 0x7D | 5    | PG_PD_EN     | RWE  | 0x0     | PGOOD pin pull-down enable during sleep<br><b>`0`</b>: PGOOD not pulled down on sleep event<br><b>`1`</b>: PGOOD pulled down on sleep event                                                   |
| 0x7D | 4    | PG_WAIT_TO   | RWE  | 0x0     | Timeout selection for waiting external PGOOD release after power-on<br><b>`0`</b>: 128 ms<br><b>`1`</b>: 1 s                                                                                  |
| 0x7D | 3    | PG_WAIT_EN   | RWE  | 0x0     | Wait for external PGOOD release after PMIC power-on sequence completes<br><b>`0`</b>: Do not wait<br><b>`1`</b>: Wait                                                                         |
| 0x7D | 2    | AUTO_BOOT_EN | RWE  | 0x0     | Auto reboot enable after shutdown event<br><b>`0`</b>: No reboot after shutdown<br><b>`1`</b>: Reboot after shutdown                                                                          |
| 0x7D | 1    | SLP_WKUP_SEQ | RWE  | 0x0     | Sleep / wake-up sequence selection<br><b>`0`</b>: Direct enter / exit sleep<br><b>`1`</b>: Follow shutdown / power-on sequence                                                                |
| 0x7D | 0    | SD_SEQ       | RWE  | 0x0     | Shutdown sequence selection<br><b>`0`</b>: Reverse-order shutdown<br><b>`1`</b>: Fast shutdown                                                                                                |

##### Table 7-88 PWR_CTRL2

| Addr | Bits | Field Name        | Attr | Default | Description                                                                                                                                                                                                                                  |
| ---- | ---- | ----------------- | ---- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x7E | 7    | SD_RST_TIME       | RE   | 0x0     | Dwell time selection when reset enters shutdown mode<br><b>`0`</b>: 200 ms<br><b>`1`</b>: 1 s                                                                                                                                                                  |
| 0x7E | 6    | PWRKY_SD_DIS      | RWE  | 0x0     | PWRKY shutdown function mask<br><b>`0`</b>: Enable PWRKY shutdown (12 s long-press reset disabled)<br><b>`1`</b>: Disable PWRKY shutdown (12 s long-press reset enabled)                                                                                       |
| 0x7E | 5    | PWRCTRL_SDTO_TIME | RWE  | 0x0     | PWRCTRL timeout selection for shutdown and sleep sequences<br><b>`0`</b>: 128 ms<br><b>`1`</b>: 1 s                                                                                                                                                            |
| 0x7E | 4    | PWRCTRL_WAIT_EN   | RWE  | 0x0     | Wait for PWRCTRL during shutdown and sleep sequences<br><b>`0`</b>: Do not wait<br><b>`1`</b>: Wait                                                                                                                                                            |
| 0x7E | 3    | Reserved          | RV   | 0       | Reserved                                                                                                                                                                                                                                     |
| 0x7E | 2    | SW_SD             | RW   | 0x0     | Software shutdown<br><b>`0`</b>: No operation<br><b>`1`</b>: Trigger software shutdown (software-triggered, hardware-cleared)                                                                                                                                  |
| 0x7E | 1    | SW_RST            | RW   | 0x0     | Software reset<br><b>`0`</b>: No operation<br><b>`1`</b>: Trigger software reset (software-triggered, hardware-cleared)                                                                                                                                        |
| 0x7E | 0    | SW_SLP_WKUP       | RW   | 0x0     | Software sleep / wake-up<br>Power-on mode:<br><b>`0`</b>: No operation<br><b>`1`</b>: Trigger software sleep (software-triggered, hardware-cleared)<br>Shutdown mode:<br><b>`0`</b>: Trigger software wake-up (software-triggered, hardware-cleared)<br><b>`1`</b>: No operation |

##### Table 7-89 PWR_STS0

| Addr | Bits | Field Name        | Attr  | Default | Description                                                                                                                       |
| ---- | ---- | ----------------- | ----- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 0x7F | 7:5  | Reserved          | RV    | 0       | Reserved                                                                                                                          |
| 0x7F | 4    | FLAG_PWRCTRL_WKUP | R, IO | 0x0     | Power-on source indicator (cleared by writing 1)<br><b>`0`</b>: Not PWRCTRL all-bound wake-up<br><b>`1`</b>: PWRCTRL all-bound wake-up              |
| 0x7F | 3    | FLAG_PWRKY_WKUP   | R, IO | 0x0     | Power-on source indicator (cleared by writing 1)<br><b>`0`</b>: Not PWRKY long-press wake-up<br><b>`1`</b>: PWRKY long-press power-on wake-up       |
| 0x7F | 2    | FLAG_VSYS_WKUP    | R, IO | 0x0     | Power-on source indicator (cleared by writing 1)<br><b>`0`</b>: Not VSYS over-threshold wake-up<br><b>`1`</b>: VSYS over-threshold power-on wake-up |
| 0x7F | 1    | FLAG_INT_WKUP     | R, IO | 0x0     | Power-on source indicator (cleared by writing 1)<br><b>`0`</b>: Not INT pin wake-up<br><b>`1`</b>: INT pin power-on wake-up                         |
| 0x7F | 0    | FLAG_RTC_WKUP     | R, IO | 0x0     | Power-on source indicator (cleared by writing 1)<br><b>`0`</b>: Not RTC wake-up<br><b>`1`</b>: RTC power-on wake-up                                 |

##### Table 7-90 PWR_STS1

| Addr | Bits | Field Name        | Attr  | Default | Description                                                                                                                                                                                                                                                                            |
| ---- | ---- | ----------------- | ----- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x80 | 7:6  | Reserved          | RV    | 0       | Reserved                                                                                                                                                                                                                                                                               |
| 0x80 | 5    | WORK_STS          | R     | 0x0     | Operating mode status<br><b>`0`</b>: Power-on mode<br><b>`1`</b>: Shutdown mode                                                                                                                                                                                                                          |
| 0x80 | 4    | FLAG_PWRCTRL_SHUT | R, IO | 0x0     | Shutdown source indicator (cleared by writing 1)<br><b>`0`</b>: Not PWRCTRL invalid shutdown<br><b>`1`</b>: PWRCTRL invalid shutdown                                                                                                                                                                     |
| 0x80 | 3    | FLAG_PWRKY_SHUT   | R, IO | 0x0     | Shutdown source indicator (cleared by writing 1)<br><b>`0`</b>: Not PWRKY long-press shutdown<br><b>`1`</b>: PWRKY long-press shutdown                                                                                                                                                                   |
| 0x80 | 2    | FLAG_VSYS_SHUT    | R, IO | 0x0     | Shutdown source indicator (cleared by writing 1)<br><b>`0`</b>: Not VSYS low-threshold shutdown<br><b>`1`</b>: VSYS low-threshold shutdown                                                                                                                                                               |
| 0x80 | 1    | FLAG_ERR_SHUT     | R, IO | 0x0     | Shutdown source indicator (cleared by writing 1)<br><b>`0`</b>: Not abnormal shutdown<br><b>`1`</b>: Abnormal shutdown<br>Abnormal events include: VSYS over-voltage, chip over-temperature, all buck over-voltage / under-voltage / short-circuit, all LDO over-voltage / under-voltage / short-circuit |
| 0x80 | 0    | FLAG_SW_SHUT      | R, IO | 0x0     | Shutdown source indicator (cleared by writing 1)<br><b>`0`</b>: Not software shutdown<br><b>`1`</b>: Software shutdown                                                                                                                                                                                   |


##### Table 7-91 PWR_KEY_TIME

| Addr | Bits | Field Name     | Attr | Default | Description                                                                                 |
| ---- | ---- | -------------- | ---- | ------- | ------------------------------------------------------------------------------------------- |
| 0x81 | 7:6  | Reserved       | RV   | 0       | Reserved                                                                                    |
| 0x81 | 5:4  | PWRKY_INT_TIME | RWE  | 0x0     | PWR key short-press interrupt time:<br>`00`: 0.5 s<br>`01`: 1 s<br>`10`: 1.5 s<br>`11`: 2 s |
| 0x81 | 3:2  | PWRKY_SD_TIME  | RWE  | 0x0     | PWR key shutdown time:<br>`00`: 4 s<br>`01`: 6 s<br>`10`: 8 s<br>`11`: 10 s                 |
| 0x81 | 1:0  | PWRKY_STA_TIME | RWE  | 0x0     | PWR key power-on time:<br>`00`: 0.5 s<br>`01`: 1 s<br>`10`: 2 s<br>`11`: 3 s                |

##### Table 7-92 PWR_SEQ_TIME

| Addr | Bits | Field Name        | Attr | Default | Description                                                                                                                           |
| ---- | ---- | ----------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 0x82 | 7:6  | PDN_SEQ_PG_DLY    | RWE  | 0x0     | Delay from PGOOD deassertion to start of power rail power-down:<br>`00`: 4 ms<br>`01`: 16 ms<br>`10`: 64 ms<br>`11`: 128 ms           |
| 0x82 | 5:4  | PUP_SEQ_PG_DLY    | RWE  | 0x0     | Delay between completion of all power rails power-up and PGOOD assertion:<br>`00`: 4 ms<br>`01`: 16 ms<br>`10`: 64 ms<br>`11`: 128 ms |
| 0x82 | 3:2  | PDN_SEQ_SLOT_TIME | RWE  | 0x0     | Power-down interval between power rails:<br>`00`: 1 ms<br>`01`: 4 ms<br>`10`: 8 ms<br>`11`: 16 ms                                     |
| 0x82 | 1:0  | PUP_SEQ_SLOT_TIME | RWE  | 0x0     | Power-up interval between power rails:<br>`00`: 1 ms<br>`01`: 4 ms<br>`10`: 8 ms<br>`11`: 16 ms                                       |

##### Table 7-93 PWR_SLOT0

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x83 | 7:4  | BUCK2_SLOT | RE   | 0x0     | BUCK2 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x83 | 3:0  | BUCK1_SLOT | RE   | 0x0     | BUCK1 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |

##### Table 7-94 PWR_SLOT1

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x84 | 7:4  | BUCK4_SLOT | RE   | 0x0     | BUCK4 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x84 | 3:0  | BUCK3_SLOT | RE   | 0x0     | BUCK3 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |

##### Table 7-95 PWR_SLOT2

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x85 | 7:4  | BUCK6_SLOT | RE   | 0x0     | BUCK6 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x85 | 3:0  | BUCK5_SLOT | RE   | 0x0     | BUCK5 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |

##### Table 7-96 PWR_SLOT3

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x86 | 7:4  | ALDO2_SLOT | RE   | 0x0     | ALDO2 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x86 | 3:0  | ALDO1_SLOT | RE   | 0x0     | ALDO1 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |

##### Table 7-97 PWR_SLOT4

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x87 | 7:4  | ALDO4_SLOT | RE   | 0x0     | ALDO4 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x87 | 3:0  | ALDO3_SLOT | RE   | 0x0     | ALDO3 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |

##### Table 7-98 PWR_SLOT5

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x88 | 7:4  | DLDO2_SLOT | RE   | 0x0     | DLDO2 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x88 | 3:0  | DLDO1_SLOT | RE   | 0x0     | DLDO1 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |

##### Table 7-99 PWR_SLOT6

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x89 | 7:4  | DLDO4_SLOT | RE   | 0x0     | DLDO4 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x89 | 3:0  | DLDO3_SLOT | RE   | 0x0     | DLDO3 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |

##### Table 7-100 PWR_SLOT7

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                         |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x8A | 7:4  | DLDO6_SLOT | RE   | 0x0     | DLDO6 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |
| 0x8A | 3:0  | DLDO5_SLOT | RE   | 0x0     | DLDO5 power-up/power-down sequence slot:<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not included in power sequence |


##### Table 7-101 PWR_SLOT8

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                                            |
| ---- | ---- | ---------- | ---- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x8B | 7:4  | Reserved   | RV   | 0       | Reserved                                                                                                                                                                               |
| 0x8B | 3:0  | DLDO7_SLOT | RE   | 0x0     | DLDO7 power-on and power-off sequence slot<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not involved in power-up or power-down sequence |

##### Table 7-102 PWR_SLOT9

| Addr | Bits | Field Name   | Attr | Default | Description                                                                                                                                                                           |
| ---- | ---- | ------------ | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x8C | 7:4  | EXT1_EN_SLOT | RE   | 0x0     | EXT1 power-on and power-off sequence slot<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not involved in power-up or power-down sequence |
| 0x8C | 3:0  | EXT0_EN_SLOT | RE   | 0x0     | EXT0 power-on and power-off sequence slot<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not involved in power-up or power-down sequence |

##### Table 7-103 PWR_SLOT10

| Addr | Bits | Field Name   | Attr | Default | Description                                                                                                                                                                           |
| ---- | ---- | ------------ | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x8D | 7:4  | EXT3_EN_SLOT | RE   | 0x0     | EXT3 power-on and power-off sequence slot<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not involved in power-up or power-down sequence |
| 0x8D | 3:0  | EXT2_EN_SLOT | RE   | 0x0     | EXT2 power-on and power-off sequence slot<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not involved in power-up or power-down sequence |

##### Table 7-104 PWR_SLOT11

| Addr | Bits | Field Name   | Attr | Default | Description                                                                                                                                                                           |
| ---- | ---- | ------------ | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x8E | 7:4  | EXT5_EN_SLOT | RE   | 0x0     | EXT5 power-on and power-off sequence slot<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not involved in power-up or power-down sequence |
| 0x8E | 3:0  | EXT4_EN_SLOT | RE   | 0x0     | EXT4 power-on and power-off sequence slot<br>`0000`: Slot 1<br>`0001`: Slot 2<br>...<br>`1101`: Slot 14<br>`1110`: Slot 15<br>`1111`: Not involved in power-up or power-down sequence |

##### Table 7-105 PWR_EXT_EN

| Addr | Bits | Field Name | Attr | Default | Description                                             |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------- |
| 0x8F | 7:6  | Reserved   | RV   | 0       | Reserved                                                |
| 0x8F | 5    | EXT5_EN    | RWE  | 0x0     | EXT5 software enable bit<br>`0`: disable<br>`1`: enable |
| 0x8F | 4    | EXT4_EN    | RWE  | 0x0     | EXT4 software enable bit<br>`0`: disable<br>`1`: enable |
| 0x8F | 3    | EXT3_EN    | RWE  | 0x0     | EXT3 software enable bit<br>`0`: disable<br>`1`: enable |
| 0x8F | 2    | EXT2_EN    | RWE  | 0x0     | EXT2 software enable bit<br>`0`: disable<br>`1`: enable |
| 0x8F | 1    | EXT1_EN    | RWE  | 0x0     | EXT1 software enable bit<br>`0`: disable<br>`1`: enable |
| 0x8F | 0    | EXT0_EN    | RWE  | 0x0     | EXT0 software enable bit<br>`0`: disable<br>`1`: enable |

##### Table 7-106 PWR_EXT_CTRL

| Addr | Bits | Field Name  | Attr | Default | Description                                                                               |
| ---- | ---- | ----------- | ---- | ------- | ----------------------------------------------------------------------------------------- |
| 0x90 | 7:6  | Reserved    | RV   | 0       | Reserved                                                                                  |
| 0x90 | 5    | EXT5_SLP_SD | RWE  | 0x0     | EXT5 shutdown control during sleep mode and sleep sequence<br>`0`: disable<br>`1`: enable |
| 0x90 | 4    | EXT4_SLP_SD | RWE  | 0x0     | EXT4 shutdown control during sleep mode and sleep sequence<br>`0`: disable<br>`1`: enable |
| 0x90 | 3    | EXT3_SLP_SD | RWE  | 0x0     | EXT3 shutdown control during sleep mode and sleep sequence<br>`0`: disable<br>`1`: enable |
| 0x90 | 2    | EXT2_SLP_SD | RWE  | 0x0     | EXT2 shutdown control during sleep mode and sleep sequence<br>`0`: disable<br>`1`: enable |
| 0x90 | 1    | EXT1_SLP_SD | RWE  | 0x0     | EXT1 shutdown control during sleep mode and sleep sequence<br>`0`: disable<br>`1`: enable |
| 0x90 | 0    | EXT0_SLP_SD | RWE  | 0x0     | EXT0 shutdown control during sleep mode and sleep sequence<br>`0`: disable<br>`1`: enable |

##### Table 7-107 EVENT0

| Addr | Bits | Field Name | Attr  | Default | Description                                                                                                                    |
| ---- | ---- | ---------- | ----- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 0x91 | 7:6  | Reserved   | RV    | 0       | Reserved                                                                                                                       |
| 0x91 | 5    | E_GPI5     | R, IO | 0x0     | GPI5 valid-level input event or ADCIN5 over/under-threshold event<br>`0`: no event<br>`1`: event occurred (write `1` to clear) |
| 0x91 | 4    | E_GPI4     | R, IO | 0x0     | GPI4 valid-level input event or ADCIN4 over/under-threshold event<br>`0`: no event<br>`1`: event occurred (write `1` to clear) |
| 0x91 | 3    | E_GPI3     | R, IO | 0x0     | GPI3 valid-level input event or ADCIN3 over/under-threshold event<br>`0`: no event<br>`1`: event occurred (write `1` to clear) |
| 0x91 | 2    | E_GPI2     | R, IO | 0x0     | GPI2 valid-level input event or ADCIN2 over/under-threshold event<br>`0`: no event<br>`1`: event occurred (write `1` to clear) |
| 0x91 | 1    | E_GPI1     | R, IO | 0x0     | GPI1 valid-level input event or ADCIN1 over/under-threshold event<br>`0`: no event<br>`1`: event occurred (write `1` to clear) |
| 0x91 | 0    | E_GPI0     | R, IO | 0x0     | GPI0 valid-level input event or ADCIN0 over/under-threshold event<br>`0`: no event<br>`1`: event occurred (write `1` to clear) |

##### Table 7-108 EVENT1

| Addr | Bits | Field Name | Attr  | Default | Description                                                                                                                                                                                   |
| ---- | ---- | ---------- | ----- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x92 | 7:6  | Reserved   | RV    | 0       | Reserved                                                                                                                                                                                      |
| 0x92 | 5    | E_TICK     | R, IO | 0x0     | RTC tick event<br>`0`: RTC alarm not reached<br>`1`: RTC alarm reached and triggers periodically<br>Write `1` to clear; the next tick event will set this bit again unless TICK_EN is cleared |
| 0x92 | 4    | E_ALARM    | R, IO | 0x0     | RTC alarm event<br>`0`: alarm not reached<br>`1`: alarm reached (write `1` to clear)                                                                                                          |
| 0x92 | 3    | E_WDT_TO   | R, IO | 0x0     | Watchdog timeout event<br>`0`: no timeout<br>`1`: timeout occurred (write `1` to clear)                                                                                                       |
| 0x92 | 2    | E_ADC_EOS  | R, IO | 0x0     | ADC auto-sampling sequence complete event<br>`0`: sequence not complete<br>`1`: sequence completed (write `1` to clear)                                                                       |
| 0x92 | 1    | E_ADC_EOC  | R, IO | 0x0     | ADC conversion complete event<br>`0`: conversion not complete<br>`1`: conversion completed (write `1` to clear)                                                                               |
| 0x92 | 0    | E_ADC_TEMP | R, IO | 0x0     | ADC channel 1 (junction temperature) over/under-threshold event<br>`0`: no event<br>`1`: event occurred (write `1` to clear)                                                                  |

##### Table 7-109 EVENT2

| Addr | Bits | Field Name    | Attr  | Default | Description                                                                                                                           |
| ---- | ---- | ------------- | ----- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 0x93 | 7    | Reserved      | RV    | 0       | Reserved                                                                                                                              |
| 0x93 | 6    | E_TEMP_CRIT   | R, IO | 0x0     | Chip critical over-temperature shutdown event<br>`0`: no critical event<br>`1`: critical shutdown event occurred (write `1` to clear) |
| 0x93 | 5    | E_TEMP_SEVERE | R, IO | 0x0     | Chip severe over-temperature warning event<br>`0`: no severe warning<br>`1`: severe warning occurred (write `1` to clear)             |
| 0x93 | 4    | E_TEMP_WARN   | R, IO | 0x0     | Chip over-temperature warning event<br>`0`: no warning<br>`1`: warning occurred (write `1` to clear)                                  |
| 0x93 | 3    | E_SW_SC       | R, IO | 0x0     | SWITCH short-circuit event<br>`0`: no short/open circuit<br>`1`: short circuit detected (write `1` to clear)                          |
| 0x93 | 2    | E_LDO_SC      | R, IO | 0x0     | LDO short/open-circuit event<br>`0`: no fault<br>`1`: at least one LDO fault occurred (write `1` to clear)                            |
| 0x93 | 1    | E_LDO_UV      | R, IO | 0x0     | LDO undervoltage event<br>`0`: no undervoltage<br>`1`: undervoltage occurred (write `1` to clear)                                     |
| 0x93 | 0    | E_LDO_OV      | R, IO | 0x0     | LDO overvoltage event<br>`0`: no overvoltage<br>`1`: overvoltage occurred (write `1` to clear)                                        |

##### Table 7-110 BUCK_EVENT0

| Addr | Bits | Field Name | Attr  | Default | Description                                                                 |
| ---- | ---- | ---------- | ----- | ------- | --------------------------------------------------------------------------- |
| 0x94 | 7:6  | Reserved   | RV    | 0       | Reserved                                                                    |
| 0x94 | 5    | E_BUCK6_OV | R, IO | 0x0     | BUCK6 overvoltage event<br>`0`: no overvoltage<br>`1`: overvoltage occurred |
| 0x94 | 4    | E_BUCK5_OV | R, IO | 0x0     | BUCK5 overvoltage event<br>`0`: no overvoltage<br>`1`: overvoltage occurred |
| 0x94 | 3    | E_BUCK4_OV | R, IO | 0x0     | BUCK4 overvoltage event<br>`0`: no overvoltage<br>`1`: overvoltage occurred |
| 0x94 | 2    | E_BUCK3_OV | R, IO | 0x0     | BUCK3 overvoltage event<br>`0`: no overvoltage<br>`1`: overvoltage occurred |
| 0x94 | 1    | E_BUCK2_OV | R, IO | 0x0     | BUCK2 overvoltage event<br>`0`: no overvoltage<br>`1`: overvoltage occurred |
| 0x94 | 0    | E_BUCK1_OV | R, IO | 0x0     | BUCK1 overvoltage event<br>`0`: no overvoltage<br>`1`: overvoltage occurred |

##### Table 7-111 BUCK_EVNET1

| Addr | Bits | Field Name | Attr | Default | Description                                                                                          |
| ---- | ---- | ---------- | ---- | ------- | ---------------------------------------------------------------------------------------------------- |
| 0x95 | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                             |
| 0x95 | 5    | E_BUCK6_UV | R，IO | 0x0     | BUCK6 undervoltage event<br>`0`: BUCK6 undervoltage not detected<br>`1`: BUCK6 undervoltage detected |
| 0x95 | 4    | E_BUCK5_UV | R，IO | 0x0     | BUCK5 undervoltage event<br>`0`: BUCK5 undervoltage not detected<br>`1`: BUCK5 undervoltage detected |
| 0x95 | 3    | E_BUCK4_UV | R，IO | 0x0     | BUCK4 undervoltage event<br>`0`: BUCK4 undervoltage not detected<br>`1`: BUCK4 undervoltage detected |
| 0x95 | 2    | E_BUCK3_UV | R，IO | 0x0     | BUCK3 undervoltage event<br>`0`: BUCK3 undervoltage not detected<br>`1`: BUCK3 undervoltage detected |
| 0x95 | 1    | E_BUCK2_UV | R，IO | 0x0     | BUCK2 undervoltage event<br>`0`: BUCK2 undervoltage not detected<br>`1`: BUCK2 undervoltage detected |
| 0x95 | 0    | E_BUCK1_UV | R，IO | 0x0     | BUCK1 undervoltage event<br>`0`: BUCK1 undervoltage not detected<br>`1`: BUCK1 undervoltage detected |

##### Table 7-112 BUCK_EVNET2

| Addr | Bits | Field Name | Attr | Default | Description                                                                                            |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------------------------------------------------------------ |
| 0x96 | 7:6  | Reserved   | RV   | 0       | Reserved                                                                                               |
| 0x96 | 5    | E_BUCK6_SC | R，IO | 0x0     | BUCK6 short/open circuit event<br>`0`: BUCK6 short/open not detected<br>`1`: BUCK6 short/open detected |
| 0x96 | 4    | E_BUCK5_SC | R，IO | 0x0     | BUCK5 short/open circuit event<br>`0`: BUCK5 short/open not detected<br>`1`: BUCK5 short/open detected |
| 0x96 | 3    | E_BUCK4_SC | R，IO | 0x0     | BUCK4 short/open circuit event<br>`0`: BUCK4 short/open not detected<br>`1`: BUCK4 short/open detected |
| 0x96 | 2    | E_BUCK3_SC | R，IO | 0x0     | BUCK3 short/open circuit event<br>`0`: BUCK3 short/open not detected<br>`1`: BUCK3 short/open detected |
| 0x96 | 1    | E_BUCK2_SC | R，IO | 0x0     | BUCK2 short/open circuit event<br>`0`: BUCK2 short/open not detected<br>`1`: BUCK2 short/open detected |
| 0x96 | 0    | E_BUCK1_SC | R，IO | 0x0     | BUCK1 short/open circuit event<br>`0`: BUCK1 short/open not detected<br>`1`: BUCK1 short/open detected |

##### Table 7-113 PWRKY_EVNET

| Addr | Bits | Field Name     | Attr | Default | Description                                                                                                   |
| ---- | ---- | -------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------- |
| 0x97 | 7:6  | Reserved       | RV   | 0       | Reserved                                                                                                      |
| 0x97 | 5    | E_VSYS_OV      | R，IO | 0x0     | VSYS overvoltage event<br>`0`: VSYS overvoltage not detected<br>`1`: VSYS overvoltage detected (VSYS > 5.9 V) |
| 0x97 | 4    | E_PWRKY_SDINTR | R，IO | 0x0     | PWRKY shutdown event<br>`0`: Shutdown event not detected<br>`1`: Shutdown event detected                      |
| 0x97 | 3    | E_PWRKY_LINTR  | R，IO | 0x0     | PWRKY long-press event<br>`0`: Long press not detected<br>`1`: Long press detected                            |
| 0x97 | 2    | E_PWRKY_SINTR  | R，IO | 0x0     | PWRKY short-press event<br>`0`: Short press not detected<br>`1`: Short press detected                         |
| 0x97 | 1    | E_PWRKY_FINTR  | R，IO | 0x0     | PWRKY falling-edge event<br>`0`: Falling edge not detected<br>`1`: Falling edge detected                      |
| 0x97 | 0    | E_PWRKY_RINTR  | R，IO | 0x0     | PWRKY rising-edge event<br>`0`: Rising edge not detected<br>`1`: Rising edge detected                         |

##### Table 7-114 IRQ_EN0

| Addr | Bits | Field Name  | Attr | Default | Description                                                  |
| ---- | ---- | ----------- | ---- | ------- | ------------------------------------------------------------ |
| 0x98 | 7:6  | Reserved    | RV   | 0       | Reserved                                                     |
| 0x98 | 5    | IRQ_EN_GPI5 | RW   | 0x0     | E_GPI5 event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x98 | 4    | IRQ_EN_GPI4 | RW   | 0x0     | E_GPI4 event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x98 | 3    | IRQ_EN_GPI3 | RW   | 0x0     | E_GPI3 event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x98 | 2    | IRQ_EN_GPI2 | RW   | 0x0     | E_GPI2 event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x98 | 1    | IRQ_EN_GPI1 | RW   | 0x0     | E_GPI1 event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x98 | 0    | IRQ_EN_GPI0 | RW   | 0x0     | E_GPI0 event interrupt enable<br>`0`: disable<br>`1`: enable |

##### Table 7-115 IRQ_EN1

| Addr | Bits | Field Name      | Attr | Default | Description                                                      |
| ---- | ---- | --------------- | ---- | ------- | ---------------------------------------------------------------- |
| 0x99 | 7:6  | Reserved        | RV   | 0       | Reserved                                                         |
| 0x99 | 5    | IRQ_EN_TICK     | RW   | 0x0     | E_TICK event interrupt enable<br>`0`: disable<br>`1`: enable     |
| 0x99 | 4    | IRQ_EN_ALARM    | RW   | 0x0     | E_ALARM event interrupt enable<br>`0`: disable<br>`1`: enable    |
| 0x99 | 3    | IRQ_EN_WDT_TO   | RW   | 0x0     | E_WDT_TO event interrupt enable<br>`0`: disable<br>`1`: enable   |
| 0x99 | 2    | IRQ_EN_ADC_EOS  | RW   | 0x0     | E_ADC_EOS event interrupt enable<br>`0`: disable<br>`1`: enable  |
| 0x99 | 1    | IRQ_EN_ADC_EOC  | RW   | 0x0     | E_ADC_EOC event interrupt enable<br>`0`: disable<br>`1`: enable  |
| 0x99 | 0    | IRQ_EN_ADC_TEMP | RW   | 0x0     | E_ADC_TEMP event interrupt enable<br>`0`: disable<br>`1`: enable |

##### Table 7-116 IRQ_EN2

| Addr | Bits | Field Name         | Attr | Default | Description                                                         |
| ---- | ---- | ------------------ | ---- | ------- | ------------------------------------------------------------------- |
| 0x9A | 7    | Reserved           | RV   | 0       | Reserved                                                            |
| 0x9A | 6    | IRQ_EN_TEMP_CRIT   | RW   | 0x0     | E_TEMP_CRIT event interrupt enable<br>`0`: disable<br>`1`: enable   |
| 0x9A | 5    | IRQ_EN_TEMP_SEVERE | RW   | 0x0     | E_TEMP_SEVERE event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9A | 4    | IRQ_EN_TEMP_WARN   | RW   | 0x0     | E_TEMP_WARN event interrupt enable<br>`0`: disable<br>`1`: enable   |
| 0x9A | 3    | IRQ_EN_SW_SC       | RW   | 0x0     | E_SW_SC event interrupt enable<br>`0`: disable<br>`1`: enable       |
| 0x9A | 2    | IRQ_EN_LDO_SC      | RW   | 0x0     | E_LDO_SC event interrupt enable<br>`0`: disable<br>`1`: enable      |
| 0x9A | 1    | IRQ_EN_LDO_UV      | RW   | 0x0     | E_LDO_UV event interrupt enable<br>`0`: disable<br>`1`: enable      |
| 0x9A | 0    | IRQ_EN_LDO_OV      | RW   | 0x0     | E_LDO_OV event interrupt enable<br>`0`: disable<br>`1`: enable      |

##### Table 7-117 IRQ_BUCK_EN0

| Addr | Bits | Field Name      | Attr | Default | Description                                                      |
| ---- | ---- | --------------- | ---- | ------- | ---------------------------------------------------------------- |
| 0x9B | 7:6  | Reserved        | RV   | 0       | Reserved                                                         |
| 0x9B | 5    | IRQ_EN_BUCK6_OV | RW   | 0x0     | E_BUCK6_OV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9B | 4    | IRQ_EN_BUCK5_OV | RW   | 0x0     | E_BUCK5_OV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9B | 3    | IRQ_EN_BUCK4_OV | RW   | 0x0     | E_BUCK4_OV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9B | 2    | IRQ_EN_BUCK3_OV | RW   | 0x0     | E_BUCK3_OV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9B | 1    | IRQ_EN_BUCK2_OV | RW   | 0x0     | E_BUCK2_OV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9B | 0    | IRQ_EN_BUCK1_OV | RW   | 0x0     | E_BUCK1_OV event interrupt enable<br>`0`: disable<br>`1`: enable |

##### Table 7-118 IRQ_BUCK_EN1

| Addr | Bits | Field Name      | Attr | Default | Description                                                      |
| ---- | ---- | --------------- | ---- | ------- | ---------------------------------------------------------------- |
| 0x9C | 7:6  | Reserved        | RV   | 0       | Reserved                                                         |
| 0x9C | 5    | IRQ_EN_BUCK6_UV | RW   | 0x0     | E_BUCK6_UV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9C | 4    | IRQ_EN_BUCK5_UV | RW   | 0x0     | E_BUCK5_UV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9C | 3    | IRQ_EN_BUCK4_UV | RW   | 0x0     | E_BUCK4_UV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9C | 2    | IRQ_EN_BUCK3_UV | RW   | 0x0     | E_BUCK3_UV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9C | 1    | IRQ_EN_BUCK2_UV | RW   | 0x0     | E_BUCK2_UV event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9C | 0    | IRQ_EN_BUCK1_UV | RW   | 0x0     | E_BUCK1_UV event interrupt enable<br>`0`: disable<br>`1`: enable |

##### Table 7-119 IRQ_BUCK_EN2

| Addr | Bits | Field Name      | Attr | Default | Description                                                      |
| ---- | ---- | --------------- | ---- | ------- | ---------------------------------------------------------------- |
| 0x9D | 7:6  | Reserved        | RV   | 0       | Reserved                                                         |
| 0x9D | 5    | IRQ_EN_BUCK6_SC | RW   | 0x0     | E_BUCK6_SC event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9D | 4    | IRQ_EN_BUCK5_SC | RW   | 0x0     | E_BUCK5_SC event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9D | 3    | IRQ_EN_BUCK4_SC | RW   | 0x0     | E_BUCK4_SC event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9D | 2    | IRQ_EN_BUCK3_SC | RW   | 0x0     | E_BUCK3_SC event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9D | 1    | IRQ_EN_BUCK2_SC | RW   | 0x0     | E_BUCK2_SC event interrupt enable<br>`0`: disable<br>`1`: enable |
| 0x9D | 0    | IRQ_EN_BUCK1_SC | RW   | 0x0     | E_BUCK1_SC event interrupt enable<br>`0`: disable<br>`1`: enable |

##### Table 7-120 IRQ_PWRKY_EN

| Addr | Bits | Field Name          | Attr | Default | Description                                                                                  |
| ---- | ---- | ------------------- | ---- | ------- | -------------------------------------------------------------------------------------------- |
| 0x9E | 7    | VSYS_OVP_EN         | RWE  | 0x0     | VSYS overvoltage (5.9 V) shutdown protection enable<br>`0`: disable<br>`1`: enable           |
| 0x9E | 6    | TEMP_CRIT_PROT      | RWE  | 0x0     | Over-temperature (135 °C / 150 °C) shutdown protection enable<br>`0`: disable<br>`1`: enable |
| 0x9E | 5    | IRQ_EN_VSYS_OV      | RW   | 0x0     | VSYS overvoltage event interrupt enable<br>`0`: disable<br>`1`: enable                       |
| 0x9E | 4    | IRQ_EN_PWRKY_SDINTR | RW   | 0x0     | E_PWRKY_SDINTR event interrupt enable<br>`0`: disable<br>`1`: enable                         |
| 0x9E | 3    | IRQ_EN_PWRKY_LINTR  | RW   | 0x0     | E_PWRKY_LINTR event interrupt enable<br>`0`: disable<br>`1`: enable                          |
| 0x9E | 2    | IRQ_EN_PWRKY_SINTR  | RW   | 0x0     | E_PWRKY_SINTR event interrupt enable<br>`0`: disable<br>`1`: enable                          |
| 0x9E | 1    | IRQ_EN_PWRKY_FINTR  | RW   | 0x0     | E_PWRKY_FINTR event interrupt enable<br>`0`: disable<br>`1`: enable                          |
| 0x9E | 0    | IRQ_EN_PWRKY_RINTR  | RW   | 0x0     | E_PWRKY_RINTR event interrupt enable<br>`0`: disable<br>`1`: enable                          |

##### Table 7-121 PROT_EN

| Addr | Bits | Field Name       | Attr | Default | Description                                                                                                                                                   |
| ---- | ---- | ---------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x9F | 7    | SW_SCP_DIS       | RWE  | 0x0     | Switch short-circuit protection disable<br>`0`: enable<br>`1`: disable                                                                                        |
| 0x9F | 6    | TEMP_SEVERE_PROT | RWE  | 0x0     | Severe over-temperature protection (shutdown protection)<br>`0`: disable severe over-temperature protection<br>`1`: enable severe over-temperature protection |
| 0x9F | 5    | BUCK_SCP_EN      | RWE  | 0x0     | Any BUCK short-circuit / open-circuit protection (shutdown protection)<br>`0`: disable protection<br>`1`: enable protection                                   |
| 0x9F | 4    | BUCK_UVP_EN      | RWE  | 0x0     | Any BUCK output undervoltage protection (shutdown protection)<br>`0`: disable protection<br>`1`: enable protection                                            |
| 0x9F | 3    | BUCK_OVP_EN      | RWE  | 0x0     | Any BUCK output overvoltage protection (shutdown protection)<br>`0`: disable protection<br>`1`: enable protection                                             |
| 0x9F | 2    | LDO_SCP_EN       | RWE  | 0x0     | Any LDO output short-circuit / open-circuit protection (shutdown protection)<br>`0`: disable protection<br>`1`: enable protection                             |
| 0x9F | 1    | LDO_UVP_EN       | RWE  | 0x0     | Any LDO output undervoltage protection (shutdown protection)<br>`0`: disable protection<br>`1`: enable protection                                             |
| 0x9F | 0    | LDO_OVP_EN       | RWE  | 0x0     | Any LDO overcurrent / short-circuit protection (shutdown protection)<br>`0`: disable protection<br>`1`: enable protection                                     |

##### Table 7-122 DEVICE_ID

| Addr | Bits | Field Name | Attr | Default | Description |
| ---- | ---- | ---------- | ---- | ------- | ----------- |
| 0xA0 | 7:0  | DEVICE_ID  | RE   | 0x00    | Device ID   |

##### Table 7-123 VERSION_ID

| Addr | Bits | Field Name | Attr | Default | Description |
| ---- | ---- | ---------- | ---- | ------- | ----------- |
| 0xA1 | 7:0  | VERSION_ID | RE   | 0x00    | Version ID  |

##### Table 7-124 CUSTOMER_ID

| Addr | Bits | Field Name  | Attr | Default | Description |
| ---- | ---- | ----------- | ---- | ------- | ----------- |
| 0xA2 | 7:0  | CUSTOMER_ID | RE   | 0x00    | Customer ID |

##### Table 7-125 SYS_CFG0

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                             |
| ---- | ---- | ---------- | ---- | ------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 0xA3 | 7    | TEMP_LEVEL | RE   | 0x0     | Temperature level selection<br>Temperature warning / severe / critical<br>`0`: 95 °C / 115 °C / 135 °C<br>`1`: 110 °C / 130 °C / 150 °C |
| 0xA3 | 6:0  | IF_ADDR    | RE   | 0x55    | I²C slave address configuration                                                                                                         |

##### Table 7-126 SYS_CFG1

| Addr | Bits | Field Name    | Attr | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---- | ---- | ------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0xA4 | 7:5  | VSYS_STA_VTH  | RE   | 0x0     | Power-on threshold<br>`000`: Vsys > 2.9 V, start power-on sequence<br>`001`: Vsys > 3.0 V, start power-on sequence<br>`010`: Vsys > 3.1 V, start power-on sequence<br>`011`: Vsys > 3.2 V, start power-on sequence<br>`100`: Vsys > 3.3 V, start power-on sequence<br>`101`: Vsys > 3.4 V, start power-on sequence<br>`110`: Vsys > 3.5 V, start power-on sequence<br>`111`: Vsys > 3.6 V, start power-on sequence |
| 0xA4 | 4:2  | VSYS_SHUT_VTH | RE   | 0x0     | Shutdown threshold<br>`000`: Vsys < 2.6 V, start shutdown sequence<br>`001`: Vsys < 2.7 V, start shutdown sequence<br>`010`: Vsys < 2.8 V, start shutdown sequence<br>`011`: Vsys < 2.9 V, start shutdown sequence<br>`100`: Vsys < 3.0 V, start shutdown sequence<br>`101`: Vsys < 3.1 V, start shutdown sequence<br>`110`: Vsys < 3.2 V, start shutdown sequence<br>`111`: Vsys < 3.3 V, start shutdown sequence |
| 0xA4 | 1    | KEY_RST_EN    | RE   | 0x0     | In shutdown mode, after long-press PWRKY triggers power-on, continue pressing to trigger reset<br>`0`: do not trigger<br>`1`: trigger (when PWRKY_SD_DIS = `1`)                                                                                                                                                                                                                                                    |
| 0xA4 | 0    | KEY_SD_EN     | RE   | 0x0     | In shutdown mode, after long-press PWRKY triggers power-on, continue pressing to trigger shutdown<br>`0`: do not trigger<br>`1`: trigger (when PWRKY_SD_DIS = `0`)                                                                                                                                                                                                                                                 |
##### Table 7-127 SYS_CFG2

| Addr | Bits | Field Name      | Attr | Default | Description   |
| ---- | ---- | --------------- | ---- | ------- | --------------- |
| 0xA5 | 7    | VSYS_STEP       | RE   | 0x0     | Hot-swap power-on threshold step<br>`0`: 0.1 V<br>`1`: 0.2 V   |
| 0xA5 | 6    | HOT_SWAP_DIS    | RE   | 0x0     | Hot-swap power-on threshold increase control<br>`0`: enable<br>`1`: disable<br>When disabled, the power-on threshold is not increased after hot-swap    |
| 0xA5 | 5    | EVENT_DELAY     | RE   | 0x0     | Event filtering for over-temperature, VSYS overvoltage, BUCK and LDO short-circuit events<br>`0`: 100 µs<br>`1`: disable     |
| 0xA5 | 4:3  | OVUV_DELAY      | RE   | 0x0     | Abnormal event (BUCK and LDO UV/OV) filtering time<br>`00`: 100 µs<br>`01`: 375 µs<br>`10`: 750 µs<br>`11`: disable    |
| 0xA5 | 2:0  | OVUV_MASK_DELAY | RE   | 0x0     | BUCK and LDO overvoltage/undervoltage event mask duration<br>`000`: 125 µs<br>`001`: 250 µs<br>`010`: 1 ms<br>`011`: 8 ms<br>`100`: 64 ms<br>`101`: 256 ms<br>`110`: 512 ms<br>`111`: disable<br>When the BUCK and LDO are enabled, or when the output voltage of the BUCK or LDO changes, over-voltage and under-voltage events for the BUCK and LDO are masked for the duration defined by UVOV_MASK_DELAY. |

##### Table 7-128 MTP_KEY

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                                                 |
| ---- | ---- | ---------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0xA6 | 7:0  | MTP_KEY    | RW   | 0x00    | MTP register unlock key (MTP_ADDR, MTP_DATA, MTP_CFG, MTP_CTRL)<br>Unlock operation: write `0xAA` to this register<br>After unlock, readback value is `0x1` |

##### Table 7-129 MTP_ADDR

| Addr | Bits | Field Name | Attr | Default | Description                                 |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------- |
| 0xA7 | 7    | Reserved   | RV   | 0       | Reserved                                    |
| 0xA7 | 6:0  | MTP_ADDR   | RW，P | 0x0     | MTP address register (read, program, erase) |


##### Table 7-130 MTP_DATA

| Addr | Bits | Field Name | Attr | Default | Description                                                                                                                  |
| ---- | ---- | ---------- | ---- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 0xA8 | 7:0  | MTP_DATA   | RW，P | 0x0     | MTP data register<br>Read data is stored in this register<br>Write data must be prepared in this register before programming |

##### Table 7-131 MTP_CFG

| Addr | Bits | Field Name      | Attr | Default | Description                                                                                                             |
| ---- | ---- | --------------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------- |
| 0xA9 | 7:6  | Reserved        | RV   | 0       | Reserved                                                                                                                |
| 0xA9 | 5:4  | MTP_PG_TIME_SEL | RW，P | 0x0     | MTP programming time selection<br>`00`: 30 µs<br>`01`: 20 µs<br>`1x`: 40 µs                                             |
| 0xA9 | 3    | MTP_PDN         | RW，P | 0x0     | MTP power control<br>`0`: MTP off<br>`1`: MTP on<br>MTP read, program, and erase operations require this bit set to `1` |
| 0xA9 | 2:1  | MTP_TRIM        | RW，P | 0x2     | Internal MTP power module output voltage selection<br>`01`: for program and erase<br>`10`: for MTP read                 |
| 0xA9 | 0    | MTP_VRFCG_SEL   | RW，P | 0x1     | MTP internal CG voltage selection<br>`0`: CG = 0<br>`1`: CG = 1.2 V                                                     |

##### Table 7-132 MTP_CTRL

| Addr | Bits | Field Name | Attr | Default | Description                                       |
| ---- | ---- | ---------- | ---- | ------- | ------------------------------------------------- |
| 0xAA | 7:3  | Reserved   | RV   | 0       | Reserved                                          |
| 0xAA | 2    | MTP_ER     | RW，P | 0x0     | MTP erase enable<br>`0`: disable<br>`1`: enable   |
| 0xAA | 1    | MTP_PG     | RW，P | 0x0     | MTP program enable<br>`0`: disable<br>`1`: enable |
| 0xAA | 0    | MTP_RD     | RW，P | 0x0     | MTP read enable<br>`0`: disable<br>`1`: enable    |


## 8. Package Information

![](./static/YNjYbwpqRoi8CGxVRm2clLZQnRN.png)
![](./static/QleTbkKomo7UoSxLulfcTeOtnAY.png)

## 9. Tray Information

![](./static/IQgfbtLlToY6CExeW0ncN709nK4.png)
![](./static/EvxzbOvUgoYLonxfLBFcbGYOnlf.png)
