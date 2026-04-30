---
sidebar_position: 11
---

# 10. Image Subsystem

## 10.1 MIPI Camera IN Interface

### 10.1.1 Overview

The MIPI Camera IN interface integrates four MIPI-CSI2 v1.1 controllers, each equipped with four data lanes and supporting a maximum transfer rate of 1.5 Gbps per lane.

### 10.1.2 Features

- Configurable data lanes per controller: 1, 2, or 4.
- Independent D-PHY Resources:
  - CSI0 and CSI1 each have a dedicated D-PHY interface
- Shared D-PHY Resource:
  - CSI2 and CSI3 share one 4-lane D-PHY interface. Each supports up to 4 lanes when used independently, or up to 2 lanes per controller when operating simultaneously.
- Supported input data formats:
  - Legacy YUV420 8-bit
  - YUV420 8-bit
  - RAW8
  - RAW10
  - RAW12
  - Embedded data type
- Supported data interleaving types:
  - Data-type interleaving
  - Virtual-channel interleaving

### 10.1.3 Block Diagram

<img src="/k3_docs/static/k3_mipi.png" alt="" width="800">

## 10.2 GPU

### 10.2.1 Overview

The GPU engine processes a number of different workload types, namely:

- 3D Graphics Workload, which involves processing vertex data and pixel data for rendering 3D scenes. The GPU architecture is based on tile-based deferred rendering (TBDR) and processes data in two phases:
  - Geometry Processing Phase - This involves vertex operations such as transformation and vertex lighting, as well as dividing a 3D scene into tiles.
  - Fragment Processing Phase - This involves pixel operations such as rasterisation, texturing and shading of pixels.
- Compute Workload (GP-GPU), which involves general-purpose data processing.

3D Graphics and Compute (General-Purpose GPU) workloads with memory barriers cannot execute concurrently.

The GPU architecture provides full compliance with OpenGL ES 1.1, 2.0 and 3.2, EGL 1.5, OpenCL 3.0, and Vulkan 1.3 specifications.

The GPU has a 128-bit AXI bus to access SoC DDR memory, and the core frequency is up to 1228 MHz.

### 10.2.2 Features

#### 10.2.2.1 GPU Key Features

The graphics processors are built around multi-threaded Unified Shading Clusters (USCs) which feature an ALU architecture with high SIMD efficiency, and support tile-based deferred rendering with concurrent processing of multiple tiles.

This core has the following features:

- Base architecture, fully compliant with the following APIs:
  - OpenGL ES 1.1/2.0/3.2
  - EGL 1.5
  - OpenCL 3.0
  - Vulkan 1.3
- Tile-based deferred rendering architecture for 3D graphics workloads, with concurrent processing of multiple tiles.
- Programmable high-quality image anti-aliasing
- Fine-grain triangle culling
- Support for DRM security
- Support for GPU virtualization
  - up to 8 virtual GPUs
  - Support for IMG hyperlane technology, with 8 hyperlanes available
  - Separate IRQs per OSI
- Multi-threaded Unified Shading Cluster (USC) engine incorporating pixel shader, vertex shader and GP-GPU (compute shader) functionality
- USC incorporates an ALU architecture with high SIMD efficiency
- Fully virtualized memory addressing (up to 64 GB address space), supporting unified memory architecture
- Fine-grained task switching, workload balancing, and power management
- Advanced DMA-driven operation for minimum host CPU interaction
- System Level Cache (SLC)
  - The size of the SLC can be configured by the customer
- Specialized Texture Cache Unit (TCU)
- Compressed Texture Decoding
- Lossless and/or visually lossless low area image compression - the Imagination frame buffer compression and decompression (TFBC) algorithm
- Dedicated processor for B-Series core firmware execution
  - Single-threaded firmware processor with a 2KB instruction cache and a 2KB data cache.
- Separate power island for the firmware processor
- On-Chip Performance, Power and Statistics Registers.

#### 10.2.2.2 Unified Shading Cluster Features

- Number of ALU pipelines: 2
- 8 parallel instances per clock
- Local data, texture and instruction caches
- Variable length instruction set encoding
- Full support for OpenCL™ atomic operations
- Scalar and vector SIMD execution model
- USC F16 Sum-of-Products Multiply-Add (SOPMAD) Arithmetic Logic Unit (ALU)

#### 10.2.2.3 3D Graphics Features

##### Rasterization

- Deferred Pixel Shading
- On-chip tile floating point depth buffer
- 8-bit stencil with on-chip tile stencil buffer
- Maximum tiles in flight (per ISP): 2
- 16 parallel depth/stencil tests per clock
- 1 fixed-function rasterisation pipeline(s)

##### Texture Lookups

- Load from source instruction support
- Texture writes enabled through the Texture Processing Unit

##### Filtering

- Point, bilinear and trilinear filtering
- Anisotropic filtering
- Corner filtering support for Cube Environment Mapped textures and filtering across faces

##### Texture Formats

- ASTC LDR compressed texture format support
- TFBC lossless and/or lossy compression format support for non-compressed textures and YUV textures
- ETC
- YUV planar support

##### Resolution Support

- Frame buffer max size = 8K × 8K
- Texture max size = 8K × 8K

##### Anti-aliasing

- Maximum 4× multisampling

##### Primitive Assembly

- Early hidden object removal
- Tile acceleration.

##### Render to Buffers

- Twiddled format support
- Multiple on-chip render targets (MRT)
- Lossless and/or lossy Frame Buffer Compression (and Decompression)
- Programmable Geometry Shader Support
- Direct Geometry Stream Out (Transform Feedback)

##### Compute Features

- 1, 2 and 3 dimensional compute primitives
- Block DMA to/from USC Common Store (for local data)
- Per task input data DMA (to USC Unified Store)
- Conditional execution
- Execution fences
- Compute workload can be overlapped with any other workload
- Round to nearest even

## 10.3 V2D

### 10.3.1 Overview

The V2D (2D Video Processor) in the K3 SoC is a hardware accelerator for video processing tasks such as format conversion, scaling, color-space transformation, and layer composition. It is designed for video playback and post-processing pipelines.

### 10.3.2 Features

- Support for scaling up/down: maximum scale-up factor of 16×, maximum scale-down factor of 1/16×
- Support for rotation: 0°, 90°, 180°, 270°, mirror, and flip operations
- Supports simple blending of layers and backgrounds
- Supports cropping.
- Supports fetching solid colors.
- Supports color-space conversion among RGB, BT601, and BT709 (narrow and full range).
- Maximum RGBA8888 size: 4096 x 2304
- Supports dithering
- Supports MMU

### 10.3.3 Supported Formats

#### 10.3.3.1 Input Format

- RGB888 (RB can swap)
- RGBX8888 (RB can swap)
- RGBA8888 (RB can swap)
- ARGB8888 (RB can swap)
- RGB565 (RB can swap)
- RGBA5658 (RB can swap)
- ARGB8565 (RB can swap)
- A8 (8-bit alpha image)
- Y8 (8-bit grayscale image)
- YUV420 semi-planar (UV can swap)
- AFBC 16×16 RGBA8888 layout 0 (split and non-split modes)
- AFBC 16×16 NV12 layout 1 (split and non-split modes)

#### 10.3.3.2 Output Format
- RGB888 (RB can swap)
- RGBX8888 (RB can swap)
- RGBA8888 (RB can swap)
- ARGB8888 (RB can swap)
- RGB565 (RB can swap)
- RGBA5658 (RB can swap)
- ARGB8565 (RB can swap)
- A8 (8-bit alpha image)
- Y8 (8-bit grayscale image)
- YUV420 semi-planar (UV can swap)
- AFBC 16×16 RGBA8888 layout 0 (split and non-split modes)
- AFBC 16×16 NV12 layout 1 (split and non-split modes)

### 10.3.4 Subsystem Description

<img src="/k3_docs/static/k3_v2d.png" alt="" width="800">

The work scenario is shown in the following figure.
<img src="/k3_docs/static/k3_v2dx00.png" alt="" width="600">

### 10.3.5 Functional Description

#### 10.3.5.1 Fetch Data

The process of fetching a 16×16 block of data from a source frame (src frame) and mapping it to the destination superblock (dst superblock) is shown below, where:

- AFBC: fetch rectangle left, top, width, and height are 4-byte aligned
- Non-AFBC: fetch rectangle left, top, width, and height are 1-byte aligned

<img src="/k3_docs/static/k3_fetch.png" alt="" width="400">

The code for fetching data for display is listed below.

```
Input param: Rect_left, Rect_top, Rect_width, Rect_height
Rect_width = Rect_left % 4 + Rect_width;
Rect_height = Rect_top % 4 + Rect_height;
Rect_left = (Rect_left / 4) * 4;
Rect_top = (Rect_top / 4) * 4;

if LayerX_format == YUV420
{
  Rect_width = ALIGN((Rect_left % 2) + Rect_width, 2);
  Rect_height = ALIGN((Rect_top % 2) + Rect_height, 2);
  Rect_left = (Rect_left / 2) * 2;
  Rect_top = (Rect_top / 2) * 2;
}

Take the data in the Rect
Loop every pixel in Rect
{
  if LayerX_format == YUV420 
  {
    upsample YUV420 to YUV444
    c0 = channel0 //Y
    c1 = channel1 //U
    c2 = channel2 //V
    c3 = 0xff
  }
  if LayerX_format == RGB888
  {
    c0 = channel0 //R
    c1 = channel1 //G
    c2 = channel2 //B
    c3 = 0xff //A
  }
  if LayerX_format == RGBX8888
  {
    c0 = channel0
    c1 = channel1
    c2 = channel2
    c3 = 0xff
  }
  if LayerX_format == RGBA8888
  {
    c0 = channel0 //R
    c1 = channel1 //G
    c2 = channel2 //B
    c3 = channel3 //A
  }
  if LayerX_format == ARGB8888
  {
    c0 = channel1
    c1 = channel2
    c2 = channel3
    c3 = channel0
  }
  if LayerX_format == RGB565
  {
    c0 = byte_low&0x1f
    c1 = ((byte_high<<3)|(byte_low>>5))&0x3f;
    c2 = (byte_high>>3)&0x1f;
    c0 = (c0<<3)|(c0>>2);
    c1 = (c1<<2)|(c1>>4);
    c2 = (c2<<3)|(c2>>2);
    c3 = 0xff
  }
  if LayerX_format == YUV420 && LayerX_swap==1
    Swap(c1,c2)
  else if LayerX_swap==1
    Swap(c0,c2)

  Index = Rect_y%16 * 16 + Rect_x
  data[0][index] = c0
  data[1][index] = c1
  data[2][index] = c2
  data[3][index] = c3
}
```

**Variables:**

| Variable | Bits | Comment |
| :--- | :--- | :--- |
| Rect_left, Rect_top | 16-bit unsigned | Range [0,65535] |
| Rect_width, Rect_height | 5-bit unsigned | Range [1/16,16] |
| Rect_x, Rect_y | 16-bit unsigned | Range [0,65535]; pixel global position |
| c0, c1, c2, c3 | 8-bit unsigned | Range [0,255] |
| byte_low, byte_high | 8-bit unsigned | Range [0,255]; `byte_low`: lower byte in RGB565; `byte_high`: higher byte in RGB565 |
| data[4][256] | 8-bit unsigned x4x256 | Range [0,255] |
| index | 8-bit unsigned | Range [0,255] |

**Registers:**

| Register Name | Comment |
| :--- | :--- |
| LayerX_format | X is 0 or 1; refer to the module register |
| LayerX_swap | X is 0 or 1; refer to the module register |

#### 10.3.5.2 Solid Color

The code for applying a solid color within a specific rectangle is listed below.

If `LayerX_solid` is enabled, the fetched data is set to solid R, G, B, and A values.

```
Input param: Rect_left, Rect_top, Rect_width, Rect_height
If LayerX_solid_enable == 1
{
  c0 = layerX_solid_R
  c1 = layerX_solid_G
  c2 = layerX_solid_B
  c3 = layerX_solid_A

  Loop all pixel in Rect
  {
    Index = (Rect_y % 16) * 16 + Rect_x
    data[0][index] = c0
    data[1][index] = c1
    data[2][index] = c2
    data[3][index] = c3
  }
  Skip fetch data from DDR
}
```

The coordinates of the fetch rect and solid rect are updated after rotation.

**Variables:**

| Variable | Bits | Comment |
| :--- | :--- | :--- |
| Rect_left, Rect_top | 16-bit unsigned | Range [0,65535] |
| Rect_width, Rect_height | 5-bit unsigned | Range [1/16,16] |
| Rect_x, Rect_y | 16-bit unsigned | Range [0,65535]; pixel global position |
| c0, c1, c2, c3 | 8-bit unsigned | Range [0,255] |
| byte_low, byte_high | 8-bit unsigned | Range [0,255]; `byte_low`: lower byte in RGB565; `byte_high`: higher byte in RGB565 |
| data[4][256] | 8-bit unsigned x4x256 | Range [0,255] |
| index | 8-bit unsigned | Range [0,255] |

**Registers:**

| Register Name | Comment |
| :--- | :--- |
| LayerX_solid_enable | X is 0 or 1; refer to the module register |
| layerX_solid_R | X is 0 or 1; refer to the module register |
| layerX_solid_G | X is 0 or 1; refer to the module register |
| layerX_solid_B | X is 0 or 1; refer to the module register |
| layerX_solid_A | X is 0 or 1; refer to the module register |

#### 10.3.5.3 Rotation

Supports 0°, 90°, 180°, and 270° rotation (performed clockwise), as well as mirror and flip options, as shown in the example below.

<img src="/k3_docs/static/k3_rotat.png" alt="" width="200">

The code for rotating, mirroring, and flipping graphical content is listed below.

```
Input param: Rect_left, Rect_top, Rect_width, Rect_height
Output: Block_rect_left, Block_rect_top, Block_rect_width, Block_rect_height, data_out[4][256]
Block_rect_left = Rect_left
Block_rect_top = Rect_top
Block_rect_width = Rect_width
Block_rect_height = Rect_height

If LayerX_degree == ROT_0 {
  Org_rect_left = Rect_left
  Org_rect_top = Rect_top
  Org_rect_width = Rect_width
  Org_rect_height = Rect_height
}
If LayerX_degree == ROT_90 {
  Org_rect_left = Rect_top
  Org_rect_top = ALIGN(LayerX_height, 16) - Rect_left - Rect_width
  Org_rect_width = Rect_height
  Org_rect_height = Rect_width
}
If LayerX_degree == ROT_180 {
  Org_rect_left = ALIGN(LayerX_width, 16) - Rect_left - Rect_width
  Org_rect_top = ALIGN(LayerX_height, 16) - Rect_top - Rect_height
  Org_rect_width = Rect_width
  Org_rect_height = Rect_height
}
If LayerX_degree == ROT_270 {
  Org_rect_left = ALIGN(LayerX_width, 16) - Rect_top - Rect_height
  Org_rect_top = Rect_left
  Org_rect_width = Rect_height
  Org_rect_height = Rect_width
}
If LayerX_degree == ROT_MIRROR {
  Org_rect_left = ALIGN(LayerX_width, 16) - Rect_left - Rect_width
  Org_rect_top = Rect_top
  Org_rect_width = Rect_width
  Org_rect_height = Rect_height
}
If LayerX_degree == ROT_FLIP {
  Org_rect_left = Rect_left
  Org_rect_top = ALIGN(LayerX_height, 16) - Rect_top - Rect_height
  Org_rect_width = Rect_width
  Org_rect_height = Rect_height
}

//fetch data in Org_rect
Fetch_data(Org_rect, &data_in[4][256])

Loop all pixels in data_in{
  dst_index=j*16 + i
  If LayerX_degree == ROT_0
    src_index=j*16 + i
  If LayerX_degree == ROT_90
    src_index=(15-i)*16 + j
  If LayerX_degree == ROT_180
    src_index = (15 - j) * 16 + (15 - i)
  If LayerX_degree == ROT_270
    src_index = i * 16 + (15 - j);
  If LayerX_degree == ROT_MIRROR
    src_index = j * 16 + (15 - i);
  If LayerX_degree == ROT_FLIP
    src_index = (15 - j) * 16 + i;

  data_out[0][dst_index] = data_out[0][src_index]
  data_out[1][dst_index] = data_out[1][src_index]
  data_out[2][dst_index] = data_out[2][src_index]
  data_out[3][dst_index] = data_out[3][src_index]
}
```

**Variables:**

| Variable | Bits | Comment |
| :--- | :--- | :--- |
| Rect_left, Rect_top | 16-bit unsigned | Range [0,65535] |
| Rect_width, Rect_height | 5-bit unsigned | Range [1,16] |
| Block_rect_left, Block_rect_top | 16-bit unsigned | Range [0,65535] |
| Block_rect_width, Block_rect_height | 5-bit unsigned | Range [1,16] |
| data_in[4][256], data_out[4][256] | 8-bit unsigned x4x256 | Range [0,255] |

**Registers:**

| Register Name | Bits | Comment |
| :--- | :--- | :--- |
| LayerX_degree | 3-bit unsigned | X is 0 or 1; refer to the module register |
| LayerX_width, LayerX_height | 16-bit unsigned | X is 0 or 1; refer to the module register |

#### 10.3.5.4 CSC

Color Space Conversion (CSC) supports format conversion as follows:

- BT601 and BT709: conversion between narrow and full range
- RGB to YUV
- YUV to RGB

The conversion process transforms input channels into output channels using a transformation matrix with clamping to ensure valid output values, that is, within the range [0, 255].

For that purpose, the formulas below are implemented, and the details of the specific variables and registers involved are listed immediately after.

Firstly, compute the intermediate channel values:

$$
C0_{inter} = (Layer\_matrix[0][0] \times C0_{in} + Layer\_matrix[0][1] \times C1_{in} + Layer\_matrix[0][2] \times C2_{in} + 512) \gg 10 + Layer\_matrix[0][3]
$$


$$
C1_{inter} = (Layer\_matrix[1][0] \times C0_{in} + Layer\_matrix[1][1] \times C1_{in} + Layer\_matrix[1][2] \times C2_{in} + 512) \gg 10 + Layer\_matrix[1][3]
$$

$$
C2_{inter} = (Layer\_matrix[2][0] \times C0_{in} + Layer\_matrix[2][1] \times C1_{in} + Layer\_matrix[2][2] \times C2_{in} + 512) \gg 10 + Layer\_matrix[2][3]
$$

Then clamp to ensure valid output values:

$$
\begin{aligned}
C0_{out} & = clamp(C0_{inter}, 0, 255) \\
C1_{out} & = clamp(C1_{inter}, 0, 255) \\
C2_{out} & = clamp(C2_{inter}, 0, 255) \\
C3_{out} & = clamp(C3_{in}, 0, 255)
\end{aligned}
$$

Note: If `LayerX_CSC_enable == 0`, skip the CSC function.

**Registers:**

| Register Name | Index | Bits | Comment |
| :--- | :--- | :--- | :--- |
| LayerX_CSC_enable | - | 1-bit unsigned | 0: disable; 1: enable |
| Layer_matrix | 0-11 | 13-bit signed | Range [-4096,4095]; refer to `LayerX_matrix` or `Layer1_matrix` |

**Variables:**

| Variables | Bits | Comment |
| :--- | :--- | :--- |
| $C0_{in}, C1_{in}, C2_{in}, C3_{in}$ | 8-bit unsigned | Input channels |
| $C0_{inter}, C1_{inter}, C2_{inter}$ | 10-bit signed | - |
| $C0_{out}, C1_{out}, C2_{out}, C3_{out}$ | 8-bit unsigned | Output channels |

#### 10.3.5.5 Scaling

The scaling operation follows a systematic superblock-based approach, where:

- The first four superblocks are output horizontally, then vertically
- After the vertical output is completed, the process restarts from the first row of superblocks

#### 10.3.5.6 Pack

A 16×16 image block can be stored in DDR memory; however, only the portion that falls within the output crop region is stored and converted to the specified output color format, such as YUV or RGB.

The code for storing an image block is listed below.

```
Input param: Rect_left, Rect_top, Rect_width, Rect_height, data_in[4][256]

if output_format == YUV420 
{
  s0=0
  s1=1
  s2=2
  If(output_swap){
    Swap(s1, s2)
  }
  Loop all pixels by 2x2{
    If(pixel in output_crop_rect){
      Y00=data_in[s0][pixel_index00]
      Y01=data_in[s0][pixel_index01]
      Y10=data_in[s0][pixel_index10]
      Y11=data_in[s0][pixel_index11]
      U00=data_in[s1][pixel_index00]
      U01=data_in[s1][pixel_index01]
      U10=data_in[s1][pixel_index10]
      U11=data_in[s1][pixel_index11]
      V00=data_in[s2][pixel_index00]
      V01=data_in[s2][pixel_index01]
      V10=data_in[s2][pixel_index10]
      V11=data_in[s2][pixel_index11]
      Downsample and store to output frame
      U=(U00+U01+U10+U11+2)>>2
      V=(V00+V01+V10+V11+2)>>2
    }
  }
}
if output_format == RGB888 
{
  s0=0
  s1=1
  s2=2
  If(output_swap){
    Swap(s0, s2)
  }
  Loop all pixels{
    If(pixel in output_crop_rect){
      R=data_in[s0][pixel_index]
      G=data_in[s1][pixel_index]
      B=data_in[s2][pixel_index]
      store to output frame
    }
  }
}
if output_format == RGBX8888 || output_format == RGBA8888
{
  s0=0
  s1=1
  s2=2
  s3=3
  If(output_swap){
    Swap(s0, s2)
  }
  Loop all pixels{
    If(pixel in output_crop_rect){
      R=data_in[s0][pixel_index]
      G=data_in[s1][pixel_index]
      B=data_in[s2][pixel_index]
      A=data_in[s3][pixel_index]
      store to output frame
    }
  }
}
if output_format == ARGB8888 
{
  s0=3
  s1=0
  s2=1
  s3=2
  If(output_swap){
    Swap(s1, s3)
  }
  Loop all pixels{
    If(pixel in output_crop_rect){
      R=data_in[s0][pixel_index]
      G=data_in[s1][pixel_index]
      B=data_in[s2][pixel_index]
      A=data_in[s3][pixel_index]
      store to output frame
    }
  }
}
```

**Variables:**

| Variable | Bits | Comment |
| :--- | :--- | :--- |
| Rect_left, Rect_top | 16-bit unsigned | Range [0,65535] |
| Rect_width, Rect_height | 5-bit unsigned | Range [1,16] |
| pixel_index | 8-bit unsigned | Range [0,255] |
| s0, s1, s2, s3 | 8-bit unsigned | Range [0,255] |
| Y00, Y01, Y10, Y11, U00, U01, U10, U11, V00, V01, V10, V11, U, V, R, G, B, A | 8-bit unsigned | Range [0,255] |
| data_in[4][256] | 8-bit unsigned x 4 x 256 | Range [0,255] |

**Registers:**

| Register Name | Bits | Comment |
| :--- | :--- | :--- |
| Output_format | 3-bit unsigned | 0: RGB888 (R at low address, B at high address); 1: RGBX8888; 2: RGBA8888; 3: ARGB8888 (A at low address, B at high address); 5: YUVs420sp (U at low address, V at high address) |
| Output_swap | 1-bit unsigned | 0: No swap; 1: RGB swap RB, YUV swap UY |
| Output_layout | 1-bit unsigned | 1: FBC compressed; 0: Linear |
| Output_crop_left | 16-bit unsigned | Range [0, 65534]; `crop_left < output_left + output_width` |
| Output_crop_top | 16-bit unsigned | Range [0, 65534]; `crop_top < output_top + output_height` |
| Output_crop_width | 16-bit unsigned | Range [1, 65535]; `crop_left + crop_wdith ≤ output_left + output_width` |
| Output_crop_height | 16-bit unsigned | Range [1, 65535]; `crop_top + crop_height ≤ output_top + output_height` |

### 10.3.6 Register Description

The base address: 0xC010_0000.

#### V2D_V2_REG_0

Offset:0x0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:16 | R_RDMA_BURST_LEN | RW | 16 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:8 | R_WDMA_BURST_LEN | RW | 16 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_TRIGGER | RW | 0 | NO |

#### V2D_V2_REG_1

Offset:0x4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF1 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF0 | RW | 0 | NO |

#### V2D_V2_REG_2

Offset:0x8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF3 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF2 | RW | 0 | NO |

#### V2D_V2_REG_3

Offset:0xC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF5 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF4 | RW | 0 | NO |

#### V2D_V2_REG_4

Offset:0x10

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF7 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF6 | RW | 0 | NO |

#### V2D_V2_REG_5

Offset:0x14

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF9 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF8 | RW | 0 | NO |

#### V2D_V2_REG_6

Offset:0x18

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF11 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF10 | RW | 0 | NO |


#### V2D_V2_REG_7

Offset:0x1C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF13 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF12 | RW | 0 | NO |

#### V2D_V2_REG_8

Offset:0x20

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF15 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF14 | RW | 0 | NO |

#### V2D_V2_REG_9

Offset:0x24

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF17 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF16 | RW | 0 | NO |

#### V2D_V2_REG_10

Offset:0x28

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF19 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF18 | RW | 0 | NO |

#### V2D_V2_REG_11

Offset:0x2C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF21 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF20 | RW | 0 | NO |

#### V2D_V2_REG_12

Offset:0x30

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF23 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF22 | RW | 0 | NO |

#### V2D_V2_REG_13

Offset:0x34

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF25 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF24 | RW | 0 | NO |

#### V2D_V2_REG_14

Offset:0x38

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF27 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF26 | RW | 0 | NO |

#### V2D_V2_REG_15

Offset:0x3C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF29 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF28 | RW | 0 | NO |

#### V2D_V2_REG_16

Offset:0x40

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF31 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF30 | RW | 0 | NO |

#### V2D_V2_REG_17

Offset:0x44

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF33 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF32 | RW | 0 | NO |

#### V2D_V2_REG_18

Offset:0x48

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF35 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF34 | RW | 0 | NO |

#### V2D_V2_REG_19

Offset:0x4C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF37 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF36 | RW | 0 | NO |

#### V2D_V2_REG_20

Offset:0x50

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF39 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF38 | RW | 0 | NO |

#### V2D_V2_REG_21

Offset:0x54

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF41 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF40 | RW | 0 | NO |

#### V2D_V2_REG_22

Offset:0x58

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF43 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF42 | RW | 0 | NO |

#### V2D_V2_REG_23

Offset:0x5C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF45 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF44 | RW | 0 | NO |

#### V2D_V2_REG_24

Offset:0x60

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:28 | RSVD | RO | 0 | Reserved for future use |
| 27:16 | R_SCALER_COEF47 | RW | 0 | NO |
| 15:12 | RSVD | RO | 0 | Reserved for future use |
| 11:0 | R_SCALER_COEF46 | RW | 0 | NO |

#### V2D_V2_REG_25

Offset:0x64

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_BLD_BG_B | RW | 0 | NO |
| 23:16 | R_BLD_BG_G | RW | 0 | NO |
| 15:8 | R_BLD_BG_R | RW | 0 | NO |
| 7:2 | RSVD | RO | 0 | Reserved for future use |
| 1 | R_BLD_BG_ENABLE | RW | 0 | NO |
| 0 | R_BLD_MODE | RW | 0 | NO |

#### V2D_V2_REG_26

Offset:0x68

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:8 | RSVD | RO | 0 | Reserved for future use |
| 7:0 | R_BLD_BG_A | RW | 0 | NO |

#### V2D_V2_REG_27

Offset:0x6C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | R_BLD_MASK_RECT_LTOP_X | RW | 0 | NO |
| 7:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_BLD_MASK_ENABLE | RW | 0 | NO |

#### V2D_V2_REG_28

Offset:0x70

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_BLD_MASK_RECT_WIDTH | RW | 0 | NO |
| 15:0 | R_BLD_MASK_RECT_LTOP_Y | RW | 0 | NO |

#### V2D_V2_REG_29

Offset:0x74

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0 | Reserved for future use |
| 15:0 | R_BLD_MASK_RECT_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_30

Offset:0x78

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_OUT_ADDR_Y_31_0 | RW | 0 | NO |

#### V2D_V2_REG_31

Offset:0x7C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_OUT_ADDR_Y_33_32 | RW | 0 | NO |

#### V2D_V2_REG_32

Offset:0x80

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_OUT_ADDR_UV_31_0 | RW | 0 | NO |

#### V2D_V2_REG_33

Offset:0x84

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | R_OUT_ORI_WIDTH | RW | 0 | NO |
| 7:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_OUT_ADDR_UV_33_32 | RW | 0 | NO |

#### V2D_V2_REG_34

Offset:0x88

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_OUT_STRIDE | RW | 0 | NO |
| 15:0 | R_OUT_ORI_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_35

Offset:0x8C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_OUT_CROP_LTOP_X | RW | 0 | NO |
| 15:9 | RSVD | RO | 0 | Reserved for future use |
| 8 | R_OUT_FBC_EN | RW | 0 | NO |
| 7 | R_OUT_SWAP | RW | 0 | NO |
| 6:5 | R_OUT_DITHER | RW | 0 | NO |
| 4 | R_OUT_RANGE | RW | 0 | NO |
| 3:0 | R_OUT_FORMAT | RW | 0 | NO |

#### V2D_V2_REG_36

Offset:0x90

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_OUT_CROP_WIDTH | RW | 0 | NO |
| 15:0 | R_OUT_CROP_LTOP_Y | RW | 0 | NO |

#### V2D_V2_REG_37

Offset:0x94

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0 | Reserved for future use |
| 15:0 | R_OUT_CROP_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_38

Offset:0x98

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_MASK_BASE_ADDR_31_0 | RW | 0 | NO |

#### V2D_V2_REG_39

Offset:0x9C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | R_MASK_IN_ORI_WIDTH | RW | 0 | NO |
| 7:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_MASK_BASE_ADDR_33_32 | RW | 0 | NO |

#### V2D_V2_REG_40

Offset:0xA0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_MASK_IN_STRIDE | RW | 0 | NO |
| 15:0 | R_MASK_IN_ORI_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_41

Offset:0xA4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_MASK_IN_CROP_LTOP_Y | RW | 0 | NO |
| 15:0 | R_MASK_IN_CROP_LTOP_X | RW | 0 | NO |

#### V2D_V2_REG_42

Offset:0xA8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_MASK_IN_CROP_HEIGHT | RW | 0 | NO |
| 15:0 | R_MASK_IN_CROP_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_43

Offset:0xAC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L0_IN_ADDR_Y_31_0 | RW | 0 | NO |

#### V2D_V2_REG_44

Offset:0xB0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_L0_IN_ADDR_Y_33_32 | RW | 0 | NO |

#### V2D_V2_REG_45

Offset:0xB4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L0_IN_ADDR_UV_31_0 | RW | 0 | NO |

#### V2D_V2_REG_46

Offset:0xB8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:20 | R_L0_BLD_ALPHA_ROP2_CODE | RW | 0 | NO |
| 19:16 | R_L0_BLD_COLOR_ROP2_CODE | RW | 0 | NO |
| 15:14 | RSVD | RO | 0 | Reserved for future use |
| 13:11 | R_L0_BLD_DST_ALPHA_FACTOR | RW | 0 | NO |
| 10:8 | R_L0_BLD_SRC_ALPHA_FACTOR | RW | 0 | NO |
| 7:5 | R_L0_BLD_DST_COLOR_FACTOR | RW | 0 | NO |
| 4:2 | R_L0_BLD_SRC_COLOR_FACTOR | RW | 0 | NO |
| 1:0 | R_L0_IN_ADDR_UV_33_32 | RW | 0 | NO |

#### V2D_V2_REG_47

Offset:0xBC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L0_IN_ORI_HEIGHT | RW | 0 | NO |
| 15:0 | R_L0_IN_ORI_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_48

Offset:0xC0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:25 | RSVD | RO | 0 | Reserved for future use |
| 24 | R_L0_IN_FBC_EN | RW | 0 | NO |
| 23 | R_L0_IN_SWAP | RW | 0 | NO |
| 22:20 | R_L0_RT_DEGREE | RW | 0 | NO |
| 19:16 | R_L0_IN_FORMAT | RW | 0 | NO |
| 15:0 | R_L0_IN_STRIDE | RW | 0 | NO |

#### V2D_V2_REG_49

Offset:0xC4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L0_IN_CROP_LTOP_Y | RW | 0 | NO |
| 15:0 | R_L0_IN_CROP_LTOP_X | RW | 0 | NO |

#### V2D_V2_REG_50

Offset:0xC8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L0_IN_CROP_HEIGHT | RW | 0 | NO |
| 15:0 | R_L0_IN_CROP_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_51

Offset:0xCC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L0_SOLID_B | RW | 0 | NO |
| 23:16 | R_L0_SOLID_G | RW | 0 | NO |
| 15:8 | R_L0_SOLID_R | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L0_SOLID_EN | RW | 0 | NO |

#### V2D_V2_REG_52

Offset:0xD0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L0_CSC_MATRIX0 | RW | 0 | NO |
| 15:9 | RSVD | RO | 0 | Reserved for future use |
| 8 | R_L0_CSC_EN | RW | 0 | NO |
| 7:0 | R_L0_SOLID_A | RW | 0 | NO |

#### V2D_V2_REG_53

Offset:0xD4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L0_CSC_MATRIX2 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L0_CSC_MATRIX1 | RW | 0 | NO |

#### V2D_V2_REG_54

Offset:0xD8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L0_CSC_MATRIX4 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L0_CSC_MATRIX3 | RW | 0 | NO |

#### V2D_V2_REG_55

Offset:0xDC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L0_CSC_MATRIX6 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L0_CSC_MATRIX5 | RW | 0 | NO |

#### V2D_V2_REG_56

Offset:0xE0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L0_CSC_MATRIX8 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L0_CSC_MATRIX7 | RW | 0 | NO |

#### V2D_V2_REG_57

Offset:0xE4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L0_CSC_MATRIX10 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L0_CSC_MATRIX9 | RW | 0 | NO |

#### V2D_V2_REG_58

Offset:0xE8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:15 | RSVD | RO | 0 | Reserved for future use |
| 14:13 | R_L0_SCL_MODE | RW | 0 | NO |
| 12:0 | R_L0_CSC_MATRIX11 | RW | 0 | NO |

#### V2D_V2_REG_59

Offset:0xEC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:20 | RSVD | RO | 0 | Reserved for future use |
| 19:0 | R_L0_SCL_DELTA_X | RW | 0 | NO |

#### V2D_V2_REG_60

Offset:0xF0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L0_BLD_GLB_ALP | RW | 0 | NO |
| 23:22 | R_L0_BLD_PRE_ALP_FUNC | RW | 0 | NO |
| 21:20 | R_L0_BLD_ALPHA_SOURCE | RW | 0 | NO |
| 19:0 | R_L0_SCL_DELTA_Y | RW | 0 | NO |

#### V2D_V2_REG_61

Offset:0xF4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | R_L0_BLD_RECT_LTOP_X | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L0_BLEND_EN | RW | 0 | NO |

#### V2D_V2_REG_62

Offset:0xF8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L0_BLD_RECT_WIDTH | RW | 0 | NO |
| 15:0 | R_L0_BLD_RECT_LTOP_Y | RW | 0 | NO |

#### V2D_V2_REG_63

Offset:0xFC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0 | Reserved for future use |
| 15:0 | R_L0_BLD_RECT_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_64

Offset:0x100

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L1_IN_ADDR_Y_31_0 | RW | 0 | NO |

#### V2D_V2_REG_65

Offset:0x104

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_L1_IN_ADDR_Y_33_32 | RW | 0 | NO |

#### V2D_V2_REG_66

Offset:0x108

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L1_IN_ADDR_UV_31_0 | RW | 0 | NO |

#### V2D_V2_REG_67

Offset:0x10C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:20 | R_L1_BLD_ALPHA_ROP2_CODE | RW | 0 | NO |
| 19:16 | R_L1_BLD_COLOR_ROP2_CODE | RW | 0 | NO |
| 15:14 | RSVD | RO | 0 | Reserved for future use |
| 13:11 | R_L1_BLD_DST_ALPHA_FACTOR | RW | 0 | NO |
| 10:8 | R_L1_BLD_SRC_ALPHA_FACTOR | RW | 0 | NO |
| 7:5 | R_L1_BLD_DST_COLOR_FACTOR | RW | 0 | NO |
| 4:2 | R_L1_BLD_SRC_COLOR_FACTOR | RW | 0 | NO |
| 1:0 | R_L1_IN_ADDR_UV_33_32 | RW | 0 | NO |

#### V2D_V2_REG_68

Offset:0x110

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L1_IN_ORI_HEIGHT | RW | 0 | NO |
| 15:0 | R_L1_IN_ORI_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_69

Offset:0x114

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:25 | RSVD | RO | 0 | Reserved for future use |
| 24 | R_L1_IN_FBC_EN | RW | 0 | NO |
| 23 | R_L1_IN_SWAP | RW | 0 | NO |
| 22:20 | R_L1_RT_DEGREE | RW | 0 | NO |
| 19:16 | R_L1_IN_FORMAT | RW | 0 | NO |
| 15:0 | R_L1_IN_STRIDE | RW | 0 | NO |

#### V2D_V2_REG_70

Offset:0x118

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L1_IN_CROP_LTOP_Y | RW | 0 | NO |
| 15:0 | R_L1_IN_CROP_LTOP_X | RW | 0 | NO |

#### V2D_V2_REG_71

Offset:0x11C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L1_IN_CROP_HEIGHT | RW | 0 | NO |
| 15:0 | R_L1_IN_CROP_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_72

Offset:0x120

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L1_SOLID_B | RW | 0 | NO |
| 23:16 | R_L1_SOLID_G | RW | 0 | NO |
| 15:8 | R_L1_SOLID_R | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L1_SOLID_EN | RW | 0 | NO |

#### V2D_V2_REG_73
Offset:0x124

| Bits     | Field     | Type | Reset | Description             |
| :--- | :--- | :--- | :--- | :--- |
| 31:29    | RSVD               | RO   | 0     | Reserved for future use |
| 28:16    | R_L1_CSC_MATRIX0   | RW   | 0     | NO                      |
| 15:9     | RSVD               | RO   | 0     | Reserved for future use |
| 8        | R_L1_CSC_EN        | RW   | 0     | NO                      |
| 7:0      | R_L1_SOLID_A       | RW   | 0     | NO                      |

#### V2D_V2_REG_74

Offset:0x128

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L1_CSC_MATRIX2 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L1_CSC_MATRIX1 | RW | 0 | NO |

#### V2D_V2_REG_75

Offset:0x12C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L1_CSC_MATRIX4 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L1_CSC_MATRIX3 | RW | 0 | NO |

#### V2D_V2_REG_76

Offset:0x130

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L1_CSC_MATRIX6 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L1_CSC_MATRIX5 | RW | 0 | NO |

#### V2D_V2_REG_77

Offset:0x134

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L1_CSC_MATRIX8 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L1_CSC_MATRIX7 | RW | 0 | NO |

#### V2D_V2_REG_78

Offset:0x138

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L1_CSC_MATRIX10 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L1_CSC_MATRIX9 | RW | 0 | NO |

#### V2D_V2_REG_79

Offset:0x13C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:15 | RSVD | RO | 0 | Reserved for future use |
| 14:13 | R_L1_SCL_MODE | RW | 0 | NO |
| 12:0 | R_L1_CSC_MATRIX11 | RW | 0 | NO |

#### V2D_V2_REG_80

Offset:0x140

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:20 | RSVD | RO | 0 | Reserved for future use |
| 19:0 | R_L1_SCL_DELTA_X | RW | 0 | NO |

#### V2D_V2_REG_81

Offset:0x144

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L1_BLD_GLB_ALP | RW | 0 | NO |
| 23:22 | R_L1_BLD_PRE_ALP_FUNC | RW | 0 | NO |
| 21:20 | R_L1_BLD_ALPHA_SOURCE | RW | 0 | NO |
| 19:0 | R_L1_SCL_DELTA_Y | RW | 0 | NO |

#### V2D_V2_REG_82

Offset:0x148

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | R_L1_BLD_RECT_LTOP_X | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L1_BLEND_EN | RW | 0 | NO |

#### V2D_V2_REG_83

Offset:0x14C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L1_BLD_RECT_WIDTH | RW | 0 | NO |
| 15:0 | R_L1_BLD_RECT_LTOP_Y | RW | 0 | NO |

#### V2D_V2_REG_84

Offset:0x150

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0 | Reserved for future use |
| 15:0 | R_L1_BLD_RECT_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_85

Offset:0x154

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L2_IN_ADDR_Y_31_0 | RW | 0 | NO |

#### V2D_V2_REG_86

Offset:0x158

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_L2_IN_ADDR_Y_33_32 | RW | 0 | NO |

#### V2D_V2_REG_87

Offset:0x15C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L2_IN_ADDR_UV_31_0 | RW | 0 | NO |

#### V2D_V2_REG_88

Offset:0x160

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:20 | R_L2_BLD_ALPHA_ROP2_CODE | RW | 0 | NO |
| 19:16 | R_L2_BLD_COLOR_ROP2_CODE | RW | 0 | NO |
| 15:14 | RSVD | RO | 0 | Reserved for future use |
| 13:11 | R_L2_BLD_DST_ALPHA_FACTOR | RW | 0 | NO |
| 10:8 | R_L2_BLD_SRC_ALPHA_FACTOR | RW | 0 | NO |
| 7:5 | R_L2_BLD_DST_COLOR_FACTOR | RW | 0 | NO |
| 4:2 | R_L2_BLD_SRC_COLOR_FACTOR | RW | 0 | NO |
| 1:0 | R_L2_IN_ADDR_UV_33_32 | RW | 0 | NO |

#### V2D_V2_REG_89

Offset:0x164

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L2_IN_ORI_HEIGHT | RW | 0 | NO |
| 15:0 | R_L2_IN_ORI_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_90

Offset:0x168

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:25 | RSVD | RO | 0 | Reserved for future use |
| 24 | R_L2_IN_FBC_EN | RW | 0 | NO |
| 23 | R_L2_IN_SWAP | RW | 0 | NO |
| 22:20 | R_L2_RT_DEGREE | RW | 0 | NO |
| 19:16 | R_L2_IN_FORMAT | RW | 0 | NO |
| 15:0 | R_L2_IN_STRIDE | RW | 0 | NO |

#### V2D_V2_REG_91

Offset:0x16C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L2_IN_CROP_LTOP_Y | RW | 0 | NO |
| 15:0 | R_L2_IN_CROP_LTOP_X | RW | 0 | NO |

#### V2D_V2_REG_92

Offset:0x170

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L2_IN_CROP_HEIGHT | RW | 0 | NO |
| 15:0 | R_L2_IN_CROP_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_93

Offset:0x174

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L2_SOLID_B | RW | 0 | NO |
| 23:16 | R_L2_SOLID_G | RW | 0 | NO |
| 15:8 | R_L2_SOLID_R | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L2_SOLID_EN | RW | 0 | NO |

#### V2D_V2_REG_94
No Comments
Offset:0x178

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L2_CSC_MATRIX0 | RW | 0 | NO |
| 15:9 | RSVD | RO | 0 | Reserved for future use |
| 8 | R_L2_CSC_EN | RW | 0 | NO |
| 7:0 | R_L2_SOLID_A | RW | 0 | NO |

#### V2D_V2_REG_95

Offset:0x17C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L2_CSC_MATRIX2 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L2_CSC_MATRIX1 | RW | 0 | NO |

#### V2D_V2_REG_96

Offset:0x180

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L2_CSC_MATRIX4 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L2_CSC_MATRIX3 | RW | 0 | NO |

#### V2D_V2_REG_97

Offset:0x184

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L2_CSC_MATRIX6 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L2_CSC_MATRIX5 | RW | 0 | NO |

#### V2D_V2_REG_98

Offset:0x188

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L2_CSC_MATRIX8 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L2_CSC_MATRIX7 | RW | 0 | NO |

#### V2D_V2_REG_99

Offset:0x18C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L2_CSC_MATRIX10 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L2_CSC_MATRIX9 | RW | 0 | NO |

#### V2D_V2_REG_100

Offset:0x190

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:15 | RSVD | RO | 0 | Reserved for future use |
| 14:13 | R_L2_SCL_MODE | RW | 0 | NO |
| 12:0 | R_L2_CSC_MATRIX11 | RW | 0 | NO |

#### V2D_V2_REG_101

Offset:0x194

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:20 | RSVD | RO | 0 | Reserved for future use |
| 19:0 | R_L2_SCL_DELTA_X | RW | 0 | NO |

#### V2D_V2_REG_102

Offset:0x198

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L2_BLD_GLB_ALP | RW | 0 | NO |
| 23:22 | R_L2_BLD_PRE_ALP_FUNC | RW | 0 | NO |
| 21:20 | R_L2_BLD_ALPHA_SOURCE | RW | 0 | NO |
| 19:0 | R_L2_SCL_DELTA_Y | RW | 0 | NO |

#### V2D_V2_REG_103

Offset:0x19C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | R_L2_BLD_RECT_LTOP_X | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L2_BLEND_EN | RW | 0 | NO |

#### V2D_V2_REG_104

Offset:0x1A0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L2_BLD_RECT_WIDTH | RW | 0 | NO |
| 15:0 | R_L2_BLD_RECT_LTOP_Y | RW | 0 | NO |

#### V2D_V2_REG_105

Offset:0x1A4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0 | Reserved for future use |
| 15:0 | R_L2_BLD_RECT_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_106

Offset:0x1A8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L3_IN_ADDR_Y_31_0 | RW | 0 | NO |

#### V2D_V2_REG_107

Offset:0x1AC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:2 | RSVD | RO | 0 | Reserved for future use |
| 1:0 | R_L3_IN_ADDR_Y_33_32 | RW | 0 | NO |

#### V2D_V2_REG_108

Offset:0x1B0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_L3_IN_ADDR_UV_31_0 | RW | 0 | NO |

#### V2D_V2_REG_109

Offset:0x1B4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:20 | R_L3_BLD_ALPHA_ROP2_CODE | RW | 0 | NO |
| 19:16 | R_L3_BLD_COLOR_ROP2_CODE | RW | 0 | NO |
| 15:14 | RSVD | RO | 0 | Reserved for future use |
| 13:11 | R_L3_BLD_DST_ALPHA_FACTOR | RW | 0 | NO |
| 10:8 | R_L3_BLD_SRC_ALPHA_FACTOR | RW | 0 | NO |
| 7:5 | R_L3_BLD_DST_COLOR_FACTOR | RW | 0 | NO |
| 4:2 | R_L3_BLD_SRC_COLOR_FACTOR | RW | 0 | NO |
| 1:0 | R_L3_IN_ADDR_UV_33_32 | RW | 0 | NO |

#### V2D_V2_REG_110

Offset:0x1B8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L3_IN_ORI_HEIGHT | RW | 0 | NO |
| 15:0 | R_L3_IN_ORI_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_111

Offset:0x1BC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:25 | RSVD | RO | 0 | Reserved for future use |
| 24 | R_L3_IN_FBC_EN | RW | 0 | NO |
| 23 | R_L3_IN_SWAP | RW | 0 | NO |
| 22:20 | R_L3_RT_DEGREE | RW | 0 | NO |
| 19:16 | R_L3_IN_FORMAT | RW | 0 | NO |
| 15:0 | R_L3_IN_STRIDE | RW | 0 | NO |

#### V2D_V2_REG_112

Offset:0x1C0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L3_IN_CROP_LTOP_Y | RW | 0 | NO |
| 15:0 | R_L3_IN_CROP_LTOP_X | RW | 0 | NO |

#### V2D_V2_REG_113

Offset:0x1C4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L3_IN_CROP_HEIGHT | RW | 0 | NO |
| 15:0 | R_L3_IN_CROP_WIDTH | RW | 0 | NO |

#### V2D_V2_REG_114

Offset:0x1C8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L3_SOLID_B | RW | 0 | NO |
| 23:16 | R_L3_SOLID_G | RW | 0 | NO |
| 15:8 | R_L3_SOLID_R | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L3_SOLID_EN | RW | 0 | NO |

#### V2D_V2_REG_115

Offset:0x1CC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L3_CSC_MATRIX0 | RW | 0 | NO |
| 15:9 | RSVD | RO | 0 | Reserved for future use |
| 8 | R_L3_CSC_EN | RW | 0 | NO |
| 7:0 | R_L3_SOLID_A | RW | 0 | NO |

#### V2D_V2_REG_116

Offset:0x1D0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L3_CSC_MATRIX2 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L3_CSC_MATRIX1 | RW | 0 | NO |

#### V2D_V2_REG_117

Offset:0x1D4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L3_CSC_MATRIX4 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L3_CSC_MATRIX3 | RW | 0 | NO |

#### V2D_V2_REG_118

Offset:0x1D8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L3_CSC_MATRIX6 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L3_CSC_MATRIX5 | RW | 0 | NO |

#### V2D_V2_REG_119

Offset:0x1DC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L3_CSC_MATRIX8 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L3_CSC_MATRIX7 | RW | 0 | NO |

#### V2D_V2_REG_120

Offset:0x1E0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:29 | RSVD | RO | 0 | Reserved for future use |
| 28:16 | R_L3_CSC_MATRIX10 | RW | 0 | NO |
| 15:13 | RSVD | RO | 0 | Reserved for future use |
| 12:0 | R_L3_CSC_MATRIX9 | RW | 0 | NO |

#### V2D_V2_REG_121

Offset:0x1E4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:15 | RSVD | RO | 0 | Reserved for future use |
| 14:13 | R_L3_SCL_MODE | RW | 0 | NO |
| 12:0 | R_L3_CSC_MATRIX11 | RW | 0 | NO |

#### V2D_V2_REG_122

Offset:0x1E8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:20 | RSVD | RO | 0 | Reserved for future use |
| 19:0 | R_L3_SCL_DELTA_X | RW | 0 | NO |

#### V2D_V2_REG_123

Offset:0x1EC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | R_L3_BLD_GLB_ALP | RW | 0 | NO |
| 23:22 | R_L3_BLD_PRE_ALP_FUNC | RW | 0 | NO |
| 21:20 | R_L3_BLD_ALPHA_SOURCE | RW | 0 | NO |
| 19:0 | R_L3_SCL_DELTA_Y | RW | 0 | NO |

#### V2D_V2_REG_124

Offset:0x1F0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | R_L3_BLD_RECT_LTOP_X | RW | 0 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_L3_BLEND_EN | RW | 0 | NO |

#### V2D_V2_REG_125

Offset:0x1F4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | R_L3_BLD_RECT_WIDTH | RW | 0 | NO |
| 15:0 | R_L3_BLD_RECT_LTOP_Y | RW | 0 | NO |

#### V2D_V2_REG_126

Offset:0x1F8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | RSVD | RO | 0 | Reserved for future use |
| 15:0 | R_L3_BLD_RECT_HEIGHT | RW | 0 | NO |

#### V2D_V2_REG_127

Offset:0x1FC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:24 | RSVD | RO | 0 | Reserved for future use |
| 23:8 | DMA_TIMEOUT_NUM | RW | 65535 | NO |
| 7:1 | RSVD | RO | 0 | Reserved for future use |
| 0 | R_DEBUG_MODE | RW | 0 | NO |

#### V2D_V2_REG_128

Offset:0x200

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:16 | LAYER_TIMEOUT_NUM | RW | 65535 | NO |
| 15:0 | FBC_TIMEOUT_NUM | RW | 65535 | NO |

#### V2D_V2_REG_129

Offset:0x204

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31 | R_DAMC_WR_INT_CLR | RW | 0 | NO |
| 30 | R_DAMC_RD_INT_CLR | RW | 0 | NO |
| 29:26 | R_DMAC_USER_ID | RW | 0 | NO |
| 25 | R_DMAC_RST_REQ | RW | 0 | NO |
| 24 | R_DMAC_RST_N_PWR | RW | 1 | NO |
| 23:16 | R_DMAC_POSTWR_EN | RW | 255 | NO |
| 15:13 | R_DMAC_MAX_REQ_NUM | RW | 7 | NO |
| 12 | R_DMAC_AXI_SEC | RW | 0 | NO |
| 11:8 | R_DMAC_AWQOS | RW | 0 | NO |
| 7:6 | RSVD | RO | 0 | Reserved for future use |
| 5:2 | R_DMAC_ARQOS | RW | 0 | NO |
| 1:0 | R_DMAC_ARB_MODE | RW | 2 | NO |

#### V2D_V2_REG_130

Offset:0x208

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE0 | RW | 0 | NO |

#### V2D_V2_REG_131

Offset:0x20C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE1 | RW | 0 | NO |

#### V2D_V2_REG_132

Offset:0x210

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE2 | RW | 0 | NO |

#### V2D_V2_REG_133

Offset:0x214

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE3 | RW | 0 | NO |

#### V2D_V2_REG_134

Offset:0x218

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE4 | RW | 0 | NO |

#### V2D_V2_REG_135

Offset:0x21C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE5 | RW | 0 | NO |

#### V2D_V2_REG_136

Offset:0x220

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE6 | RW | 0 | NO |

#### V2D_V2_REG_137

Offset:0x224

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE7 | RW | 0 | NO |

#### V2D_V2_REG_138

Offset:0x228

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE8 | RW | 0 | NO |

#### V2D_V2_REG_139

Offset:0x22C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE9 | RW | 0 | NO |

#### V2D_V2_REG_140

Offset:0x230

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE10 | RW | 0 | NO |

#### V2D_V2_REG_141

Offset:0x234

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE11 | RW | 0 | NO |

#### V2D_V2_REG_142

Offset:0x238

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE12 | RW | 0 | NO |

#### V2D_V2_REG_143

Offset:0x23C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE13 | RW | 0 | NO |

#### V2D_V2_REG_144

Offset:0x240

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE14 | RW | 0 | NO |

#### V2D_V2_REG_145

Offset:0x244

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE15 | RW | 0 | NO |

#### V2D_V2_REG_146

Offset:0x248

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE16 | RW | 0 | NO |

#### V2D_V2_REG_147

Offset:0x24C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE17 | RW | 0 | NO |

#### V2D_V2_REG_148

Offset:0x250

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE18 | RW | 0 | NO |

#### V2D_V2_REG_149

Offset:0x254

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE19 | RW | 0 | NO |

#### V2D_V2_REG_150

Offset:0x258

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE20 | RW | 0 | NO |

#### V2D_V2_REG_151

Offset:0x25C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE21 | RW | 0 | NO |

#### V2D_V2_REG_152

Offset:0x260

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE22 | RW | 0 | NO |

#### V2D_V2_REG_153

Offset:0x264

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE23 | RW | 0 | NO |

#### V2D_V2_REG_154

Offset:0x268

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE24 | RW | 0 | NO |

#### V2D_V2_REG_155

Offset:0x26C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE25 | RW | 0 | NO |

#### V2D_V2_REG_156

Offset:0x270

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE26 | RW | 0 | NO |

#### V2D_V2_REG_157

Offset:0x274

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE27 | RW | 0 | NO |

#### V2D_V2_REG_158

Offset:0x278

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE28 | RW | 0 | NO |

#### V2D_V2_REG_159

Offset:0x27C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE29 | RW | 0 | NO |

#### V2D_V2_REG_160

Offset:0x280

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE30 | RW | 0 | NO |

#### V2D_V2_REG_161

Offset:0x284

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE31 | RW | 0 | NO |

#### V2D_V2_REG_162

Offset:0x288

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE32 | RW | 0 | NO |

#### V2D_V2_REG_163

Offset:0x28C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE33 | RW | 0 | NO |

#### V2D_V2_REG_164

Offset:0x290

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE34 | RW | 0 | NO |

#### V2D_V2_REG_165

Offset:0x294

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE35 | RW | 0 | NO |

#### V2D_V2_REG_166

Offset:0x298

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE36 | RW | 0 | NO |

#### V2D_V2_REG_167

Offset:0x29C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE37 | RW | 0 | NO |

#### V2D_V2_REG_168

Offset:0x2A0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE38 | RW | 0 | NO |

#### V2D_V2_REG_169

Offset:0x2A4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE39 | RW | 0 | NO |

#### V2D_V2_REG_170

Offset:0x2A8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE40 | RW | 0 | NO |

#### V2D_V2_REG_171

Offset:0x2AC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE41 | RW | 0 | NO |

#### V2D_V2_REG_172

Offset:0x2B0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE42 | RW | 0 | NO |

#### V2D_V2_REG_173

Offset:0x2B4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE43 | RW | 0 | NO |

#### V2D_V2_REG_174

Offset:0x2B8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE44 | RW | 0 | NO |

#### V2D_V2_REG_175

Offset:0x2BC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE45 | RW | 0 | NO |

#### V2D_V2_REG_176

Offset:0x2C0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE46 | RW | 0 | NO |

#### V2D_V2_REG_177

Offset:0x2C4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE47 | RW | 0 | NO |

#### V2D_V2_REG_178

Offset:0x2C8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE48 | RW | 0 | NO |

#### V2D_V2_REG_179

Offset:0x2CC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE49 | RW | 0 | NO |

#### V2D_V2_REG_180

Offset:0x2D0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE50 | RW | 0 | NO |

#### V2D_V2_REG_181

Offset:0x2D4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE51 | RW | 0 | NO |

#### V2D_V2_REG_182

Offset:0x2D8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE52 | RW | 0 | NO |

#### V2D_V2_REG_183

Offset:0x2DC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE53 | RW | 0 | NO |

#### V2D_V2_REG_184

Offset:0x2E0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE54 | RW | 0 | NO |

#### V2D_V2_REG_185

Offset:0x2E4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE55 | RW | 0 | NO |

#### V2D_V2_REG_186

Offset:0x2E8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE56 | RW | 0 | NO |

#### V2D_V2_REG_187

Offset:0x2EC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE57 | RW | 0 | NO |

#### V2D_V2_REG_188

Offset:0x2F0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE58 | RW | 0 | NO |

#### V2D_V2_REG_189

Offset:0x2F4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE59 | RW | 0 | NO |

#### V2D_V2_REG_190

Offset:0x2F8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE60 | RW | 0 | NO |

#### V2D_V2_REG_191

Offset:0x2FC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE61 | RW | 0 | NO |

#### V2D_V2_REG_192

Offset:0x300

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE62 | RW | 0 | NO |

#### V2D_V2_REG_193

Offset:0x304

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE63 | RW | 0 | NO |

#### V2D_V2_REG_194

Offset:0x308

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE64 | RW | 0 | NO |

#### V2D_V2_REG_195

Offset:0x30C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE65 | RW | 0 | NO |

#### V2D_V2_REG_196

Offset:0x310

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE66 | RW | 0 | NO |

#### V2D_V2_REG_197

Offset:0x314

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE67 | RW | 0 | NO |

#### V2D_V2_REG_198

Offset:0x318

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE68 | RW | 0 | NO |

#### V2D_V2_REG_199

Offset:0x31C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE69 | RW | 0 | NO |

#### V2D_V2_REG_200

Offset:0x320

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE70 | RW | 0 | NO |

#### V2D_V2_REG_201

Offset:0x324

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE71 | RW | 0 | NO |

#### V2D_V2_REG_202

Offset:0x328

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE72 | RW | 0 | NO |

#### V2D_V2_REG_203

Offset:0x32C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE73 | RW | 0 | NO |

#### V2D_V2_REG_204

Offset:0x330

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE74 | RW | 0 | NO |

#### V2D_V2_REG_205

Offset:0x334

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE75 | RW | 0 | NO |

#### V2D_V2_REG_206

Offset:0x338

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE76 | RW | 0 | NO |

#### V2D_V2_REG_207

Offset:0x33C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE77 | RW | 0 | NO |

#### V2D_V2_REG_208

Offset:0x340

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE78 | RW | 0 | NO |

#### V2D_V2_REG_209

Offset:0x344

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE79 | RW | 0 | NO |

#### V2D_V2_REG_210

Offset:0x348

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE80 | RW | 0 | NO |

#### V2D_V2_REG_211

Offset:0x34C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE81 | RW | 0 | NO |

#### V2D_V2_REG_212

Offset:0x350

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE82 | RW | 0 | NO |

#### V2D_V2_REG_213

Offset:0x354

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE83 | RW | 0 | NO |

#### V2D_V2_REG_214

Offset:0x358

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE84 | RW | 0 | NO |

#### V2D_V2_REG_215

Offset:0x35C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE85 | RW | 0 | NO |

#### V2D_V2_REG_216

Offset:0x360

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE86 | RW | 0 | NO |

#### V2D_V2_REG_217

Offset:0x364

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE87 | RW | 0 | NO |

#### V2D_V2_REG_218

Offset:0x368

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE88 | RW | 0 | NO |

#### V2D_V2_REG_219

Offset:0x36C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE89 | RW | 0 | NO |

#### V2D_V2_REG_220

Offset:0x370

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE90 | RW | 0 | NO |

#### V2D_V2_REG_221

Offset:0x374

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE91 | RW | 0 | NO |

#### V2D_V2_REG_222

Offset:0x378

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE92 | RW | 0 | NO |

#### V2D_V2_REG_223

Offset:0x37C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE93 | RW | 0 | NO |

#### V2D_V2_REG_224

Offset:0x380

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE94 | RW | 0 | NO |

#### V2D_V2_REG_225

Offset:0x384

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE95 | RW | 0 | NO |

#### V2D_V2_REG_226

Offset:0x388

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE96 | RW | 0 | NO |

#### V2D_V2_REG_227

Offset:0x38C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE97 | RW | 0 | NO |

#### V2D_V2_REG_228

Offset:0x390

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE98 | RW | 0 | NO |

#### V2D_V2_REG_229

Offset:0x394

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE99 | RW | 0 | NO |

#### V2D_V2_REG_230

Offset:0x398

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE100 | RW | 0 | NO |

#### V2D_V2_REG_231

Offset:0x39C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE101 | RW | 0 | NO |

#### V2D_V2_REG_232

Offset:0x3A0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE102 | RW | 0 | NO |

#### V2D_V2_REG_233

Offset:0x3A4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE103 | RW | 0 | NO |

#### V2D_V2_REG_234

Offset:0x3A8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE104 | RW | 0 | NO |

#### V2D_V2_REG_235

Offset:0x3AC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE105 | RW | 0 | NO |

#### V2D_V2_REG_236

Offset:0x3B0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE106 | RW | 0 | NO |

#### V2D_V2_REG_237

Offset:0x3B4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE107 | RW | 0 | NO |

#### V2D_V2_REG_238

Offset:0x3B8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE108 | RW | 0 | NO |

#### V2D_V2_REG_239

Offset:0x3BC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE109 | RW | 0 | NO |

#### V2D_V2_REG_240

Offset:0x3C0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE110 | RW | 0 | NO |

#### V2D_V2_REG_241

Offset:0x3C4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE111 | RW | 0 | NO |

#### V2D_V2_REG_242

Offset:0x3C8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE112 | RW | 0 | NO |

#### V2D_V2_REG_243

Offset:0x3CC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE113 | RW | 0 | NO |

#### V2D_V2_REG_244

Offset:0x3D0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE114 | RW | 0 | NO |

#### V2D_V2_REG_245

Offset:0x3D4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE115 | RW | 0 | NO |

#### V2D_V2_REG_246

Offset:0x3D8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE116 | RW | 0 | NO |

#### V2D_V2_REG_247

Offset:0x3DC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE117 | RW | 0 | NO |

#### V2D_V2_REG_248

Offset:0x3E0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE118 | RW | 0 | NO |

#### V2D_V2_REG_249

Offset:0x3E4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE119 | RW | 0 | NO |

#### V2D_V2_REG_250

Offset:0x3E8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE120 | RW | 0 | NO |

#### V2D_V2_REG_251

Offset:0x3EC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE121 | RW | 0 | NO |

#### V2D_V2_REG_252

Offset:0x3F0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE122 | RW | 0 | NO |

#### V2D_V2_REG_253

Offset:0x3F4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE123 | RW | 0 | NO |

#### V2D_V2_REG_254

Offset:0x3F8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE124 | RW | 0 | NO |

#### V2D_V2_REG_255

Offset:0x3FC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE125 | RW | 0 | NO |

#### V2D_V2_REG_256

Offset:0x400

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE126 | RW | 0 | NO |

#### V2D_V2_REG_257

Offset:0x404

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE127 | RW | 0 | NO |

#### V2D_V2_REG_258

Offset:0x408

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE128 | RW | 0 | NO |

#### V2D_V2_REG_259

Offset:0x40C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE129 | RW | 0 | NO |

#### V2D_V2_REG_260

Offset:0x410

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE130 | RW | 0 | NO |

#### V2D_V2_REG_261

Offset:0x414

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE131 | RW | 0 | NO |

#### V2D_V2_REG_262

Offset:0x418

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE132 | RW | 0 | NO |

#### V2D_V2_REG_263

Offset:0x41C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE133 | RW | 0 | NO |

#### V2D_V2_REG_264

Offset:0x420

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE134 | RW | 0 | NO |

#### V2D_V2_REG_265

Offset:0x424

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE135 | RW | 0 | NO |

#### V2D_V2_REG_266

Offset:0x428

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE136 | RW | 0 | NO |

#### V2D_V2_REG_267

Offset:0x42C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE137 | RW | 0 | NO |

#### V2D_V2_REG_268

Offset:0x430

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE138 | RW | 0 | NO |

#### V2D_V2_REG_269

Offset:0x434

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE139 | RW | 0 | NO |

#### V2D_V2_REG_270

Offset:0x438

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE140 | RW | 0 | NO |

#### V2D_V2_REG_271

Offset:0x43C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE141 | RW | 0 | NO |

#### V2D_V2_REG_272

Offset:0x440

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE142 | RW | 0 | NO |

#### V2D_V2_REG_273

Offset:0x444

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE143 | RW | 0 | NO |

#### V2D_V2_REG_274

Offset:0x448

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE144 | RW | 0 | NO |

#### V2D_V2_REG_275

Offset:0x44C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE145 | RW | 0 | NO |

#### V2D_V2_REG_276

Offset:0x450

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE146 | RW | 0 | NO |

#### V2D_V2_REG_277

Offset:0x454

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE147 | RW | 0 | NO |

#### V2D_V2_REG_278

Offset:0x458

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE148 | RW | 0 | NO |

#### V2D_V2_REG_279

Offset:0x45C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE149 | RW | 0 | NO |

#### V2D_V2_REG_280

Offset:0x460

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE150 | RW | 0 | NO |

#### V2D_V2_REG_281

Offset:0x464

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE151 | RW | 0 | NO |

#### V2D_V2_REG_282

Offset:0x468

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE152 | RW | 0 | NO |

#### V2D_V2_REG_283

Offset:0x46C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE153 | RW | 0 | NO |

#### V2D_V2_REG_284

Offset:0x470

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE154 | RW | 0 | NO |

#### V2D_V2_REG_285

Offset:0x474

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE155 | RW | 0 | NO |

#### V2D_V2_REG_286

Offset:0x478

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE156 | RW | 0 | NO |

#### V2D_V2_REG_287

Offset:0x47C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE157 | RW | 0 | NO |

#### V2D_V2_REG_288

Offset:0x480

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE158 | RW | 0 | NO |

#### V2D_V2_REG_289

Offset:0x484

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE159 | RW | 0 | NO |

#### V2D_V2_REG_290

Offset:0x488

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE160 | RW | 0 | NO |

#### V2D_V2_REG_291

Offset:0x48C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE161 | RW | 0 | NO |

#### V2D_V2_REG_292

Offset:0x490

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE162 | RW | 0 | NO |

#### V2D_V2_REG_293

Offset:0x494

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE163 | RW | 0 | NO |

#### V2D_V2_REG_294

Offset:0x498

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE164 | RW | 0 | NO |

#### V2D_V2_REG_295

Offset:0x49C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE165 | RW | 0 | NO |

#### V2D_V2_REG_296

Offset:0x4A0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE166 | RW | 0 | NO |

#### V2D_V2_REG_297

Offset:0x4A4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE167 | RW | 0 | NO |

#### V2D_V2_REG_298

Offset:0x4A8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE168 | RW | 0 | NO |

#### V2D_V2_REG_299

Offset:0x4AC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE169 | RW | 0 | NO |

#### V2D_V2_REG_300

Offset:0x4B0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE170 | RW | 0 | NO |

#### V2D_V2_REG_301

Offset:0x4B4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE171 | RW | 0 | NO |

#### V2D_V2_REG_302

Offset:0x4B8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE172 | RW | 0 | NO |

#### V2D_V2_REG_303

Offset:0x4BC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE173 | RW | 0 | NO |

#### V2D_V2_REG_304

Offset:0x4C0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE174 | RW | 0 | NO |

#### V2D_V2_REG_305

Offset:0x4C4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE175 | RW | 0 | NO |

#### V2D_V2_REG_306

Offset:0x4C8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE176 | RW | 0 | NO |

#### V2D_V2_REG_307

Offset:0x4CC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE177 | RW | 0 | NO |

#### V2D_V2_REG_308

Offset:0x4D0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE178 | RW | 0 | NO |

#### V2D_V2_REG_309

Offset:0x4D4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE179 | RW | 0 | NO |

#### V2D_V2_REG_310

Offset:0x4D8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE180 | RW | 0 | NO |

#### V2D_V2_REG_311

Offset:0x4DC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE181 | RW | 0 | NO |

#### V2D_V2_REG_312

Offset:0x4E0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE182 | RW | 0 | NO |

#### V2D_V2_REG_313

Offset:0x4E4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE183 | RW | 0 | NO |

#### V2D_V2_REG_314

Offset:0x4E8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE184 | RW | 0 | NO |

#### V2D_V2_REG_315

Offset:0x4EC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE185 | RW | 0 | NO |

#### V2D_V2_REG_316

Offset:0x4F0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE186 | RW | 0 | NO |

#### V2D_V2_REG_317

Offset:0x4F4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE187 | RW | 0 | NO |

#### V2D_V2_REG_318

Offset:0x4F8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE188 | RW | 0 | NO |

#### V2D_V2_REG_319

Offset:0x4FC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE189 | RW | 0 | NO |

#### V2D_V2_REG_320

Offset:0x500

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE190 | RW | 0 | NO |

#### V2D_V2_REG_321

Offset:0x504

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE191 | RW | 0 | NO |

#### V2D_V2_REG_322

Offset:0x508

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE192 | RW | 0 | NO |

#### V2D_V2_REG_323

Offset:0x50C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE193 | RW | 0 | NO |

#### V2D_V2_REG_324

Offset:0x510

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE194 | RW | 0 | NO |

#### V2D_V2_REG_325

Offset:0x514

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE195 | RW | 0 | NO |

#### V2D_V2_REG_326

Offset:0x518

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE196 | RW | 0 | NO |

#### V2D_V2_REG_327

Offset:0x51C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE197 | RW | 0 | NO |

#### V2D_V2_REG_328

Offset:0x520

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE198 | RW | 0 | NO |

#### V2D_V2_REG_329

Offset:0x524

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE199 | RW | 0 | NO |

#### V2D_V2_REG_330

Offset:0x528

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE200 | RW | 0 | NO |

#### V2D_V2_REG_331

Offset:0x52C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE201 | RW | 0 | NO |

#### V2D_V2_REG_332

Offset:0x530

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE202 | RW | 0 | NO |

#### V2D_V2_REG_333

Offset:0x534

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE203 | RW | 0 | NO |

#### V2D_V2_REG_334

Offset:0x538

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE204 | RW | 0 | NO |

#### V2D_V2_REG_335

Offset:0x53C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE205 | RW | 0 | NO |

#### V2D_V2_REG_336

Offset:0x540

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE206 | RW | 0 | NO |

#### V2D_V2_REG_337

Offset:0x544

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE207 | RW | 0 | NO |

#### V2D_V2_REG_338

Offset:0x548

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE208 | RW | 0 | NO |

#### V2D_V2_REG_339

Offset:0x54C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE209 | RW | 0 | NO |

#### V2D_V2_REG_340

Offset:0x550

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE210 | RW | 0 | NO |

#### V2D_V2_REG_341

Offset:0x554

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE211 | RW | 0 | NO |

#### V2D_V2_REG_342

Offset:0x558

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE212 | RW | 0 | NO |

#### V2D_V2_REG_343

Offset:0x55C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE213 | RW | 0 | NO |

#### V2D_V2_REG_344

Offset:0x560

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE214 | RW | 0 | NO |

#### V2D_V2_REG_345

Offset:0x564

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE215 | RW | 0 | NO |

#### V2D_V2_REG_346

Offset:0x568

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE216 | RW | 0 | NO |

#### V2D_V2_REG_347

Offset:0x56C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE217 | RW | 0 | NO |

#### V2D_V2_REG_348

Offset:0x570

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE218 | RW | 0 | NO |

#### V2D_V2_REG_349

Offset:0x574

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE219 | RW | 0 | NO |

#### V2D_V2_REG_350

Offset:0x578

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE220 | RW | 0 | NO |

#### V2D_V2_REG_351

Offset:0x57C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE221 | RW | 0 | NO |

#### V2D_V2_REG_352

Offset:0x580

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE222 | RW | 0 | NO |

#### V2D_V2_REG_353

Offset:0x584

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE223 | RW | 0 | NO |

#### V2D_V2_REG_354

Offset:0x588

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE224 | RW | 0 | NO |

#### V2D_V2_REG_355

Offset:0x58C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE225 | RW | 0 | NO |

#### V2D_V2_REG_356

Offset:0x590

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE226 | RW | 0 | NO |

#### V2D_V2_REG_357

Offset:0x594

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE227 | RW | 0 | NO |

#### V2D_V2_REG_358

Offset:0x598

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE228 | RW | 0 | NO |

#### V2D_V2_REG_359

Offset:0x59C

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE229 | RW | 0 | NO |

#### V2D_V2_REG_360

Offset:0x5A0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE230 | RW | 0 | NO |

#### V2D_V2_REG_361

Offset:0x5A4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE231 | RW | 0 | NO |

#### V2D_V2_REG_362

Offset:0x5A8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE232 | RW | 0 | NO |

#### V2D_V2_REG_363

Offset:0x5AC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE233 | RW | 0 | NO |

#### V2D_V2_REG_364

Offset:0x5B0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE234 | RW | 0 | NO |

#### V2D_V2_REG_365

Offset:0x5B4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE235 | RW | 0 | NO |

#### V2D_V2_REG_366

Offset:0x5B8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE236 | RW | 0 | NO |

#### V2D_V2_REG_367

Offset:0x5BC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE237 | RW | 0 | NO |

#### V2D_V2_REG_368

Offset:0x5C0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE238 | RW | 0 | NO |

#### V2D_V2_REG_369

Offset:0x5C4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE239 | RW | 0 | NO |

#### V2D_V2_REG_370

Offset:0x5C8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE240 | RW | 0 | NO |

#### V2D_V2_REG_371

Offset:0x5CC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE241 | RW | 0 | NO |

#### V2D_V2_REG_372

Offset:0x5D0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE242 | RW | 0 | NO |

#### V2D_V2_REG_373

Offset:0x5D4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE243 | RW | 0 | NO |

#### V2D_V2_REG_374

Offset:0x5D8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE244 | RW | 0 | NO |

#### V2D_V2_REG_375

Offset:0x5DC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE245 | RW | 0 | NO |

#### V2D_V2_REG_376

Offset:0x5E0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE246 | RW | 0 | NO |

#### V2D_V2_REG_377

Offset:0x5E4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE247 | RW | 0 | NO |

#### V2D_V2_REG_378

Offset:0x5E8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE248 | RW | 0 | NO |

#### V2D_V2_REG_379

Offset:0x5EC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE249 | RW | 0 | NO |

#### V2D_V2_REG_380

Offset:0x5F0

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE250 | RW | 0 | NO |

#### V2D_V2_REG_381

Offset:0x5F4

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE251 | RW | 0 | NO |

#### V2D_V2_REG_382

Offset:0x5F8

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE252 | RW | 0 | NO |

#### V2D_V2_REG_383

Offset:0x5FC

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE253 | RW | 0 | NO |

#### V2D_V2_REG_384

Offset:0x600

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE254 | RW | 0 | NO |

#### V2D_V2_REG_385

Offset:0x604

| Bits | Field | Type | Reset | Description |
| :--- | :--- | :--- | :--- | :--- |
| 31:0 | R_PALETTE_TABLE255 | RW | 0 | NO |

