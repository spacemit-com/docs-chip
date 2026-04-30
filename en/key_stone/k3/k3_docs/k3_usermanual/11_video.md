---
sidebar_position: 12
---

# 11. Video Subsystem

## 11.1 Overview

The Video Processing Unit (VPU) is a quad-core video accelerator designed to handle both decoding and encoding of multiple video standards. It includes a host CPU that runs firmware to control the hardware engine, managing tasks such as bitstream parsing, sub-block control, and error resilience.

The VPU can operate at up to 1 GHz and supports a wide range of video standards, including H.265, H.264, VP8, VP9, MPEG-4, MPEG-2, and H.263. It allows simultaneous operations such as:

- Encoding and decoding at 4K@60 fps.
- H.264/H.265 encoding at 4K@60 fps.
- H.264/H.265 decoding at 4K@120 fps.

The video codec core performs the actual decoding and encoding for each standard using dedicated hardware logic. The Macroblock Sequencer serves as the main controller, scheduling the process flows of sub-blocks to reduce the load on the processor and simplify firmware complexity.

Additionally, several standard-independent blocks share common logic during operation, ensuring high efficiency and streamlined performance across different video standards.

## 11.2 Video Encoder

### 11.2.1 Encoding Features

- Configurable Arm Frame Buffer Compression (AFBC) 1.0 or 1.2 for input.
- Supports YUV422 and YUV420 AFBC block splitting (16 × 16).
- Supports stride (not applicable to AFBC input formats).
- Horizontal and vertical mirroring (not applicable to AFBC input formats).
- Optional source-frame rotation in 90° steps before encoding (not applicable to AFBC input formats).

> Note: If YUV422 is rotated by 90° or 270° without conversion to YUV420, the output is converted to YUV440.

### 11.2.2 Supported Source-Frame Input Formats

- 1-plane YUV422, scan-line format, interleaved in YUYV or UYVY order.
  - Note: YUV422 input can be converted to YUV420.
- 1-plane RGB (8-bit), byte-address order: RGBA, BGRA, ARGB, ABGR.
- 2-plane YUV420, scan-line format, with chroma interleaved in UV or VU order.
- 3-plane YUV420, scan-line format.
  > Note: Supported for testing purposes only; not recommended for optimal performance.
- AFBC YUV422.
- AFBC YUV420.

### 11.2.3 Supported Encoding Formats

- HEVC (H.265) Main Profile.
- HEVC (H.265) Main 10 Profile.
- H.264 Baseline Profile (BP).
- H.264 Main Profile (MP).
- H.264 High Profile (HP).
- VP8
- VP9 Profile 0
- JPEG, baseline sequential.

#### 11.2.3.1 HEVC (H.265)

- Encoded bitstream compliant with HEVC (H.265) Main Profile.
  - Encoded: up to 4K@60 fps.
- Maximum frame dimensions: 4096 × 4096 pixels.
- Bit depth: 8-bit encoding with I, P, and B frames.
- Supports tiled mode with up to 4 tiles (horizontal splits only).
- Motion Estimation (ME):
  - Search window: ±128 pixels horizontally, ±64 pixels vertically.
  - Precision: down to Quarter Pixel (QPEL) resolution.
- Intra prediction modes:
  - Luma: 8×8, 16×16, 32×32.
  - Chroma: 4×4, 8×8, 16×16.
- Inter prediction modes: 8×8, 16×16, 32×32.
- Transform sizes:
  - Luma: 8×8, 16×16, 32×32.
  - Chroma: 4×4, 8×8, 16×16.
  - Supports Skipped CUs and Merge modes.
- Deblocking filter.
- Quantization: Fixed QP or rate-controlled operation.
  - Rate control uses a leaky bucket model based on bitrate and buffer size.
- Long-term reference frame support.
- Slice insertion at CTU row granularity.
- Encoder does not prevent output from exceeding maximum bits per CTU.

#### 11.2.3.2 H.264

- Encoded bitstream compliant with Baseline, Main, and High Profiles.
- Encoded: up to 4K@60 fps.
- Maximum frame dimensions: 4096 × 4096 pixels.
- Frame types: Supports I, P, and B frames.
- Progressive encoding supported.
- Entropy coding: CABAC or CAVLC.
  > Note: B frames are not supported by CAVLC.
- Motion Estimation (ME):
  - Search window: ±128 pixels horizontally, ±64 pixels vertically.
  - Precision: down to Quarter Pixel (QPEL) resolution.
- Intra prediction modes:
  - Luma: 4×4, 8×8, 16×16.
  - Chroma: 8×8.
- Inter prediction modes: 8×8, 16×16.
- Transform sizes: 4×4, 8×8.
- Deblocking filter.
- Quantization: Fixed QP or rate-controlled operation.
  - Rate control uses a leaky bucket model based on bitrate and buffer size.
- Long-term reference frame support.
- Slice insertion granularity: 32-pixel-high rows.
  > Notes:
  > - For further details, refer to ITU-T H.264 Annex B.
  > - Encoder does not prevent output from exceeding the maximum bits per macroblock.

#### 11.2.3.3 VP8

- Encoded: up to 4K@60 fps.
- Maximum frame dimensions: 2048 × 2048 pixels.
- Frame types: Supports I and P frames.
- Motion Estimation (ME):
  - Search window: ±128 pixels horizontally, ±64 pixels vertically.
  - Precision: down to Quarter Pixel (QPEL) resolution.
- Intra prediction modes:
  - Luma: 4×4, 8×8, 16×16.
  - Chroma: 8×8.
- Inter prediction modes: 8×8, 16×16.
- Deblocking filter.
- Quantization: Fixed QP or rate-controlled operation.
  - Rate control uses a leaky bucket model based on bitrate and buffer size.

#### 11.2.3.4 VP9

- Encoded: up to 4K@60 fps.
- Encoded bitstream compliant with VP9 Profile 0 at 8-bit depth.
- Maximum frame dimensions: 4096 × 4096 pixels.
- Sample depth: 8-bit.
- Frame types: Supports I and P frames.
- Motion Estimation (ME):
  - Search window: ±128 pixels horizontally, ±64 pixels vertically.
  - Precision: down to Quarter Pixel (QPEL) resolution.
- Intra prediction modes:
  - Luma: 8×8, 16×16, 32×32.
  - Chroma: 4×4, 8×8, 16×16.
- Inter prediction modes: 8×8, 16×16, 32×32.
- Transform sizes:
  - Luma: 8×8, 16×16, 32×32.
  - Chroma: 4×4, 8×8, 16×16.
- Deblocking filter.
- Quantization: Fixed QP or rate-controlled operation.
  - Rate control uses a leaky bucket model based on bitrate and buffer size.

## 11.3 Video Decoder

### 11.3.1 Decoding Features

- Supports the following output frame formats:
  - 2-plane YUV420, scan-line format, chroma interleaved in UV or VU order.
  - 3-plane YUV420, scan-line format.
    > Note: The 3-plane format is for testing purposes only and is not recommended for maximum performance in normal applications.
- Ensure correct YUV buffer alignment and stride for optimal performance.
- Supports YUV420 AFBC format, 8-bit color depth.
  - Configurable for AFBC 1.0 or AFBC 1.2 output.
- Stride support for scan-line formats only.
- Supports decoded-frame rotation in 90-degree increments before output.
  > Note: Not applicable to AFBC output formats.
- Supports reporting average luminance (brightness) and chrominance (color) values for each 32×32 pixel block in every displayed output frame.

### 11.3.2 Supported Decoding Formats

- HEVC (H.265): Main Profile.
- H.264: Baseline, Main, High Profiles.
- VP8.
- VP9: Profile 0 and Profile 2 at 10-bit.
- VC-1: Simple Profile (SP), Main Profile (MP), Advanced Profile (AP).
- MPEG-4: Simple Profile (SP), Advanced Simple Profile (ASP).
- MPEG-2: Main Profile (MP).
- H.263: Profile 0.

#### 11.3.2.1 HEVC (H.265)

- Full compliance with Main Profiles.
- Decoded: up to 4K@120 fps.
- Maximum frame dimensions: 4096 × 4096 pixels.

#### 11.3.2.2 H.264

- Decoded: up to 4K@120 fps.
- Fully compliant with Baseline, Main, High, and High 10 progressive profiles.
- Maximum frame dimensions: 4096 × 4096 pixels.
- Note: For further details, refer to ITU-T H.264 Annex B.

#### 11.3.2.3 VP8

- Decoded: up to 4K@120 fps.
- Fully compliant with the VP8 specification.
- Maximum frame dimensions: 2048 × 2048 pixels.

#### 11.3.2.4 VP9

- Decoded: up to 4K@120 fps.
- Fully compliant with Profile 0.
- Maximum frame dimensions: 4096 × 4096 pixels.

#### 11.3.2.5 VC-1

- Decoded: up to 4K@120 fps.
- Fully compliant with VC-1 Simple, Main, and Advanced Profiles.
- Maximum frame dimensions: Width 2048 pixels, Height 4096 pixels.

#### 11.3.2.6 MPEG-4

- Decoded: up to 4K@120 fps.
- Compliant with MPEG-4 Simple Profile (SP) and Advanced Simple Profile (ASP).
- Supports Global Motion Compensation (GMC) with a limitation of one warp point.
- Maximum frame dimensions: Width 2048 pixels, Height 2048 pixels.

#### 11.3.2.7 MPEG-2

- Decoded: up to 4K@120 fps.
- Compliant with MPEG-2 Main Profile.
- Maximum frame dimensions:
  - Progressive streams: Width up to 4096 pixels.
  - Interlaced streams: Width up to 2048 pixels.
  - Height up to 4096 pixels.

#### 11.3.2.8 H.263

- Decoded: up to 4K@120 fps.
- Compliant with H.263 Profile 0.
- Maximum frame dimensions: Width and height up to 2048 pixels.

## 11.4 Block Diagram

<img src="/k3_docs/static/k3_video.png" alt="" width="600">
