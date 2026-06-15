---
sidebar_position: 1
---

# K3 Thermal Design Reference

## PDF Version

Click to download [K3 Thermal Design Reference (PDF)](#)
> Coming soon ... 

## Revision History

| Version | Date | Description |
| --- | --- | --- |
| V1.0 | 2026.06.xx | Initial release |

## Glossary

| Term (Abbreviation) | Definition |
| --- | --- |
| Thermal Design Power (TDP) | The average heat dissipated by the CPU under maximum sustained workload at the highest operating frequency. |
| Package Long Term Power Limit (PL1) | The sustained power consumption threshold for the CPU during extended operation; approximately equal to TDP. |
| Single-root (SR) | A standalone product form factor built around a single CPU. |
| System on Chip (SoC) | An integrated circuit that consolidates a complete computer system onto a single die, including processing cores, peripheral interfaces, and functional modules. |

## 1. Scope

This reference guide provides system-level thermal requirements for the K3 SoC. It is intended for customers designing new K3-based boards or complete systems built on the K3 platform, offering reference thermal dissipation solutions. The heatsink parameters, fan performance data, and thermal interface material properties listed herein are provided as design references.

In their respective projects, customers are required to:

- Review this guide and understand the safe operating temperature conditions required by the K3 SoC under maximum load.
- Identify the environmental requirements of their own products, assess the differences from this reference design, and perform appropriate design adjustments along with any necessary thermal simulation.
- Take responsibility for designing and implementing a thermal solution that maintains the K3 junction temperature within the specified safe operating range.
- Validate the thermal solution through system-level thermal testing, verify actual temperature rise against design targets, and debug any deviations to ensure reliable and stable system operation.