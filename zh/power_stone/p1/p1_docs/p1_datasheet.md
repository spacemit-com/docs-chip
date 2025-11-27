# P1 数据手册
```
最新版本：2025/03/31
```

## 文档目的

本文档主要介绍 SpacemiT Power Stone® P1 芯片的基本规格和硬件特性，旨在帮助开发人员快速熟悉 P1 芯片规格，更准确高效地完成 P1 应用及产品开发。

## 1. 产品介绍

### 1.1 概述

SpacemiT Power Stone® P1 是一款高性能的多通道电源管理芯片（PMIC），专为满足各种应用的多样化电源需求而设计，为客户提供完整的电源解决方案。该芯片集成了以下功能模块：

- **6 个恒定导通时间（COT）控制模式降压转换器**
- **12 个低压差稳压器（LDO）**
- **1 个 I²C 接口**
- **多次可编程非易失性存储器（MTP）**

P1 芯片适用于多种移动设备和嵌入式系统，具备高度灵活的电源管理功能。其主要特点包括：

- **高效电源转换**：六个全集成降压转换器支持多种目标电压轨道，提供稳定电源。
- **快速动态响应**：恒定导通时间（COT）控制模式确保快速负载瞬态性能。
- **紧凑设计**：在连续导通模式（CCM）下，默认固定切换频率为 1.5MHz，可显著减少外部电感和电容值。
- **全面保护功能**：包括欠压锁定（UVLO）、过电流保护（OCP）、过压保护（OVP）和热关断。
- **动态电压控制（DVC）**：支持根据应用需求实时调整电源电压。

此外，P1 芯片的输出电压和启动/关闭顺序可通过多次可编程非易失性存储器（MTP）接口预设，并通过 I²C 总线进行控制。该芯片仅需最少的外部元件，采用紧凑的 QFN-60 封装（7mm×7mm），适合空间受限的应用场景。

### 1.2 关键特性

- 供电电压（VIN）：2.7V～ 5.5V
- 6 个高效降压转换器：

  - Buck1/2：0.5V～3.4V，4A，支持双相操作
  - Buck3/4：0.5V～3.4V，2.5A，支持双相操作
  - Buck5/6：0.5V～3.4V，2.5A
  - 可调输出电压：所有降压转换器支持两种电压调节范围，0.5V～1.35V（步进 5mV）或 1.375V～3.4V（步进 25mV）
  - 可调电流限制阈值：可根据不同应用的负载电流进行优化
  - 专用引脚：用于选择不同 DDR 颗粒的 VDDQ 电压
- 12 个可编程的 LDO 稳压器：

  - 1 个专用常开 LDO
  - 11 个低噪声 LDO
  - 输出电压范围：0.5V～3.4V，步进 25mV
  - 输出电流范围：0.3~0.5A
- 1 个负载开关：最大输出电流 1A
- 通信接口：I²C 接口。
- 用户可编程存储器：MTP
- 系统监控功能：

  - 看门狗定时器
  - 纽扣电池支持
  - 2μA 超低功耗 RTC，带警报功能
  - 12 位 ADC，8 个通道，可配置警报阈值
- 配置灵活性：

  - 输出电压和启动/关闭顺序：可通过 MTP 预设。
  - 6 个 GPIO 引脚：用于外围设备控制。
- 工作温度范围：-40℃ 至 125℃。
- 封装：QFN-60，7mm×7mm，引脚间距 0.4mm。

### 1.3 应用

P1 适用于多种高性能设备和系统，具体应用包括：

- 超级本
- 平板电脑
- 电子书
- 虚拟现实/增强现实设备
- 工业设备
- 导航设备
- 无人机

### 1.4 模块框图

![](static/CVgqbZypMo36kHx5vpEcOhPAnMg.png)

## 2. 封装信息

### 2.1 封装

![](static/YNjYbwpqRoi8CGxVRm2clLZQnRN.png)

![](static/QleTbkKomo7UoSxLulfcTeOtnAY.png)

### 2.2 Tray 盘

![](static/IQgfbtLlToY6CExeW0ncN709nK4.png)

![](static/EvxzbOvUgoYLonxfLBFcbGYOnlf.png)

## 3. 引脚封装图

P1 引脚封装图如下

![](static/LF0fbF5vZoXL6Mx8XdAcTghIncS.png)

P1 引脚类型定义如下表描述

<table>
<tbody>
<tr>
<td>引脚类型</td>
<td>描述</td>
<td>引脚类型</td>
<td>描述</td>
</tr>
<tr>
<td>DI</td>
<td>数字输入</td>
<td>AI</td>
<td>模拟输入</td>
</tr>
<tr>
<td>DO</td>
<td>数字输出</td>
<td>AO</td>
<td>模拟输出</td>
</tr>
<tr>
<td>DIO</td>
<td>数字输入/输出</td>
<td>AIO</td>
<td>模拟输入/输出</td>
</tr>
<tr>
<td>PWR</td>
<td>电源</td>
<td>GND</td>
<td>地</td>
</tr>
</tbody>
</table>

P1 引脚描述如下表描述

<table>
<tbody>
<tr>
<td>引脚</td>
<td>引脚名称</td>
<td>类型</td>
<td>描述</td>
<td>复用功能</td>
</tr>
<tr>
<td>1</td>
<td>ALDO3</td>
<td>AO</td>
<td>ALDO3电压输出</td>
<td> -</td>
</tr>
<tr>
<td>2</td>
<td>ALDOIN</td>
<td>PWR</td>
<td>ALDO1~4电源输入</td>
<td> -</td>
</tr>
<tr>
<td>3</td>
<td>ALDO1</td>
<td>AO</td>
<td>ALDO1电压输出</td>
<td>-</td>
</tr>
<tr>
<td>4</td>
<td>ALDO2</td>
<td>AO</td>
<td>ALDO2电压输出</td>
<td> -</td>
</tr>
<tr>
<td>5</td>
<td>FB3GND</td>
<td>GND</td>
<td>Buck3输出电压地端反馈</td>
<td> -</td>
</tr>
<tr>
<td>6</td>
<td>FB3</td>
<td>AIN</td>
<td>Buck3输出电压反馈</td>
<td> -</td>
</tr>
<tr>
<td>7</td>
<td>SW3</td>
<td>AIO</td>
<td>Buck3的开关节点</td>
<td> -</td>
</tr>
<tr>
<td>8</td>
<td>VIN3</td>
<td>PWR</td>
<td>Buck3的电源输入</td>
<td> -</td>
</tr>
<tr>
<td>9</td>
<td>VIN4</td>
<td>PWR</td>
<td>Buck4的电源输入</td>
<td> -</td>
</tr>
<tr>
<td>10</td>
<td>SW4</td>
<td>AIO</td>
<td>Buck4的开关节点</td>
<td> -</td>
</tr>
<tr>
<td>11</td>
<td>FB4</td>
<td>AIN</td>
<td>Buck4输出电压反馈</td>
<td> -</td>
</tr>
<tr>
<td>12</td>
<td>SWIN</td>
<td>AIN</td>
<td>负载开关输入端</td>
<td> -</td>
</tr>
<tr>
<td>13</td>
<td>SWOUT</td>
<td>AO</td>
<td>负载开关输出端</td>
<td> -</td>
</tr>
<tr>
<td>14</td>
<td>DLDO2</td>
<td>AO</td>
<td>DLDO2电压输出</td>
<td> -</td>
</tr>
<tr>
<td>15</td>
<td>DLDO1</td>
<td>AO</td>
<td>DLDO1电压输出</td>
<td> -</td>
</tr>
<tr>
<td>16</td>
<td>DLDO3</td>
<td>AO</td>
<td>DLDO3电压输出</td>
<td> -</td>
</tr>
<tr>
<td>17</td>
<td>DLDOIN1</td>
<td>PWR</td>
<td>DLDO1~4电源输入</td>
<td> -</td>
</tr>
<tr>
<td>18</td>
<td>DLDO4</td>
<td>AO</td>
<td>DLDO4电压输出</td>
<td> -</td>
</tr>
<tr>
<td>19</td>
<td>VSET6</td>
<td>AIN</td>
<td>Buck6默认 输出电压设定</td>
<td> -</td>
</tr>
<tr>
<td>20</td>
<td>FB6</td>
<td>AIN</td>
<td>Buck6输出电压反馈</td>
<td> -</td>
</tr>
<tr>
<td>21</td>
<td>SW6</td>
<td>AIN</td>
<td>Buck6的开关节点</td>
<td> -</td>
</tr>
<tr>
<td>22</td>
<td>VIN6</td>
<td>PWR</td>
<td>Buck6的电源输入</td>
<td> -</td>
</tr>
<tr>
<td>23</td>
<td>VIN5</td>
<td>PWR</td>
<td>Buck5的电源输入</td>
<td> -</td>
</tr>
<tr>
<td>24</td>
<td>SW5</td>
<td>AIO</td>
<td>Buck5的开关节点</td>
<td> -</td>
</tr>
<tr>
<td>25</td>
<td>FB5</td>
<td>AIN</td>
<td>Buck5输出电压反馈</td>
<td> -</td>
</tr>
<tr>
<td>26</td>
<td>VSET5</td>
<td>AIN</td>
<td>Buck5默认输出电压设定</td>
<td> -</td>
</tr>
<tr>
<td>27</td>
<td>DLDO5</td>
<td>AO</td>
<td>DLDO5电压输出</td>
<td> -</td>
</tr>
<tr>
<td>28</td>
<td>DLDO6</td>
<td>AO</td>
<td>DLDO6电压输出</td>
<td> -</td>
</tr>
<tr>
<td>29</td>
<td>DLDOIN2</td>
<td>PWR</td>
<td>DLDO5~7电源输入</td>
<td> -</td>
</tr>
<tr>
<td>30</td>
<td>DLDO7</td>
<td>AO</td>
<td>DLDO7电压输出</td>
<td> -</td>
</tr>
<tr>
<td>31</td>
<td>TEST2</td>
<td>DIO</td>
<td>测试引脚</td>
<td> -</td>
</tr>
<tr>
<td>32</td>
<td>TEST1</td>
<td>DIO</td>
<td>测试引脚</td>
<td> -</td>
</tr>
<tr>
<td>33</td>
<td>AGND</td>
<td>GND</td>
<td>模拟地</td>
<td> -</td>
</tr>
<tr>
<td>34</td>
<td>FB2</td>
<td>AIN</td>
<td>Buck2输出电压反馈</td>
<td> -</td>
</tr>
<tr>
<td>35</td>
<td>SW2</td>
<td>AIO</td>
<td>Buck2的开关节点</td>
<td> -</td>
</tr>
<tr>
<td>36</td>
<td>VIN2</td>
<td>PWR</td>
<td>Buck2的电源输入</td>
<td> -</td>
</tr>
<tr>
<td>37</td>
<td>VIN1</td>
<td>PWR</td>
<td>Buck1的电源输入</td>
<td> -</td>
</tr>
<tr>
<td>38</td>
<td>SW1</td>
<td>AIO</td>
<td>Buck1的开关节点</td>
<td> -</td>
</tr>
<tr>
<td>39</td>
<td>FB1</td>
<td>AIN</td>
<td>Buck1输出电压反馈</td>
<td> -</td>
</tr>
<tr>
<td>40</td>
<td>FB1GND</td>
<td>GND</td>
<td>Buck1输出电压地端反馈</td>
<td> -</td>
</tr>
<tr>
<td>41</td>
<td>VSYS</td>
<td>PWR</td>
<td>内部电路电源输入</td>
<td> -</td>
</tr>
<tr>
<td>42</td>
<td>GPIO5</td>
<td>DIO/AIN</td>
<td>多功能复用GPIO</td>
<td>EXT_EN/SLEEP_WKUP/PWRCTRL/nRESET/ADC input</td>
</tr>
<tr>
<td>43</td>
<td>GPIO4</td>
<td>DIO/AIN</td>
<td>多功能复用GPIO</td>
<td>EXT_EN/SLEEP_WKUP/PWRCTRL/nRESET/ADC input</td>
</tr>
<tr>
<td>44</td>
<td>SDA</td>
<td>DIO</td>
<td>I²C通信接口数据信号</td>
<td> -</td>
</tr>
<tr>
<td>45</td>
<td>SCL</td>
<td>DIN</td>
<td>I²C通信接口时钟信号</td>
<td> -</td>
</tr>
<tr>
<td>46</td>
<td>VCELL</td>
<td>AIN</td>
<td>纽扣电池电压输入端口</td>
<td> -</td>
</tr>
<tr>
<td>47</td>
<td>XTALOUT</td>
<td>AIN</td>
<td>外部晶振</td>
<td> -</td>
</tr>
<tr>
<td>48</td>
<td>XTALIN</td>
<td>AIN</td>
<td>外部晶振</td>
<td> -</td>
</tr>
<tr>
<td>49</td>
<td>GPIO3</td>
<td>DIO/AIN</td>
<td>多功能复用GPIO</td>
<td>EXT_EN/SLEEP_WKUP/PWRCTRL/nRESET/ADC input</td>
</tr>
<tr>
<td>50</td>
<td>32KOUT</td>
<td>DO</td>
<td>时钟输出</td>
<td> -</td>
</tr>
<tr>
<td>51</td>
<td>GPIO2</td>
<td>DIO/AIN</td>
<td>多功能复用GPIO</td>
<td>EXT_EN/SLEEP_WKUP/PWRCTRL/nRESET/ADC input</td>
</tr>
<tr>
<td>52</td>
<td>GPIO1</td>
<td>DIO/AIN</td>
<td>多功能复用GPIO</td>
<td>EXT_EN/SLEEP_WKUP/PWRCTRL/nRESET/ADC input</td>
</tr>
<tr>
<td>53</td>
<td>GPIO0</td>
<td>DIO/AIN</td>
<td>多功能复用GPIO</td>
<td>EXT_EN/SLEEP_WKUP/PWRCTRL/nRESET/ADC input</td>
</tr>
<tr>
<td>54</td>
<td>INT</td>
<td>DIO</td>
<td>中断输出</td>
<td> -</td>
</tr>
<tr>
<td>55</td>
<td>PWRKY</td>
<td>AIN</td>
<td>开机/关机/复位按键</td>
<td> -</td>
</tr>
<tr>
<td>56</td>
<td>PGOOD</td>
<td>DIO</td>
<td>Power good指示位/复位源</td>
<td> -</td>
</tr>
<tr>
<td>57</td>
<td>AGND</td>
<td>GND</td>
<td>模拟地</td>
<td> -</td>
</tr>
<tr>
<td>58</td>
<td>VREF</td>
<td>AO</td>
<td>芯片内部参考电压</td>
<td> -</td>
</tr>
<tr>
<td>59</td>
<td>AONLDO</td>
<td>AO</td>
<td>AONLDO电压输出</td>
<td> -</td>
</tr>
<tr>
<td>60</td>
<td>ALDO4</td>
<td>AO</td>
<td>ALDO4电压输出</td>
<td>-</td>
</tr>
</tbody>
</table>

## 4. 电气特性参数

### 4.1. 绝对最大额定值

绝对最大额定值如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>T(STG)</td>
<td>存储温度</td>
<td>- </td>
<td>-40</td>
<td> -</td>
<td>150</td>
<td>°C</td>
</tr>
<tr>
<td>T(J)</td>
<td>结温</td>
<td> -</td>
<td>-40</td>
<td> -</td>
<td>125</td>
<td>°C</td>
</tr>
<tr>
<td>V(SYS)</td>
<td>系统供电电压</td>
<td> -</td>
<td>-0.3</td>
<td> -</td>
<td>7.0</td>
<td>V</td>
</tr>
<tr>
<td>V(CELL)</td>
<td>纽扣电池供电电压</td>
<td> -</td>
<td>-0.3</td>
<td> -</td>
<td>7.0</td>
<td>V</td>
</tr>
<tr>
<td>V(ESD_HBM)</td>
<td>ESD保护-HBM</td>
<td> -</td>
<td>2</td>
<td> -</td>
<td>- </td>
<td>kV</td>
</tr>
<tr>
<td>V(ESD_CDM)</td>
<td>ESD保护-CDM</td>
<td> -</td>
<td>500</td>
<td> -</td>
<td> -</td>
<td>V</td>
</tr>
</tbody>
</table>

### 4.2 推荐工作条件

推荐工作条件如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>T(J)</td>
<td>结温</td>
<td> -</td>
<td>-40</td>
<td> -</td>
<td>125</td>
<td>℃</td>
</tr>
<tr>
<td>V(SYS)</td>
<td>系统供电电压</td>
<td> -</td>
<td>2.7</td>
<td> -</td>
<td>5.5</td>
<td>V</td>
</tr>
<tr>
<td>P(DIS)</td>
<td>芯片最大功耗</td>
<td> -</td>
<td>- </td>
<td> -</td>
<td>2</td>
<td>W</td>
</tr>
<tr>
<td>R(JA)</td>
<td>Junction到环境热阻</td>
<td> -</td>
<td> -</td>
<td>38</td>
<td> -</td>
<td>℃/W</td>
</tr>
<tr>
<td>R(JC)</td>
<td>Junction到芯片表面热阻</td>
<td> -</td>
<td> -</td>
<td>12</td>
<td> -</td>
<td>℃/W</td>
</tr>
<tr>
<td>R(JB)</td>
<td>Junction到PCB板热阻</td>
<td> -</td>
<td> -</td>
<td>9</td>
<td> -</td>
<td>℃/W</td>
</tr>
</tbody>
</table>

### 4.3 各模式功耗情况

各模式功耗情况如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td rowspan=5 colspan=1>功耗</td>
<td>RESET模式</td>
<td>-</td>
<td>- </td>
<td> -</td>
<td>- </td>
<td>μA</td>
</tr>
<tr>
<td>RTC模式</td>
<td>V(IN)=5V, Ta=25℃</td>
<td> -</td>
<td>1.5</td>
<td> -</td>
<td>μA</td>
</tr>
<tr>
<td>关机模式-SHUTDOWN</td>
<td>V(IN)=5V, Ta=25℃</td>
<td> -</td>
<td>35</td>
<td> -</td>
<td>μA</td>
</tr>
<tr>
<td>开机模式-ACTIVE</td>
<td>-</td>
<td> -</td>
<td>- </td>
<td> -</td>
<td>μA</td>
</tr>
<tr>
<td>睡眠模式-SLEEP</td>
<td>-</td>
<td> -</td>
<td> -</td>
<td> -</td>
<td>μA</td>
</tr>
</tbody>
</table>

### 4.4 数字引脚电气特性

数字引脚电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>V(IH)</td>
<td>高电平输入</td>
<td>2.7 ～ 5.5 V，-40 ~ 105 ℃</td>
<td> -</td>
<td> -</td>
<td>0.3 * AONLDO</td>
<td>V</td>
</tr>
<tr>
<td>V(IL)</td>
<td>低电平输入</td>
<td>2.7 ～ 5.5 V，-40 ~ 105 ℃</td>
<td>0.7 * AONLDO</td>
<td> -</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(OH)</td>
<td>高电平输出</td>
<td>5 V，25  ℃,<br/>AONLDO = 1.8 V，I(LOAD)=1 mA</td>
<td> -</td>
<td>AONLDO - 0.1</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(OL)</td>
<td>低电平输出</td>
<td>5V，25 ℃,<br/>AONLDO  = 1.8 V，I(LOAD)=1 mA</td>
<td> -</td>
<td>0.1</td>
<td> -</td>
<td>V<br/></td>
</tr>
<tr>
<td>I(DRIVE)</td>
<td>源电流驱动</td>
<td>5V，25 ℃,<br/>AONLDO = 1.8 V，PAD = 1.3 V</td>
<td> -</td>
<td>10</td>
<td> -</td>
<td>mA</td>
</tr>
<tr>
<td>I(SINK)</td>
<td>灌电流驱动</td>
<td>5V，25 ℃,<br/>AONLDO = 1.8 V，PAD = 0.5 V</td>
<td> -</td>
<td>25</td>
<td> -</td>
<td>mA</td>
</tr>
<tr>
<td>R(PU)</td>
<td>弱上拉电阻</td>
<td> -</td>
<td> -</td>
<td>20 k</td>
<td> -</td>
<td>Ω</td>
</tr>
<tr>
<td>R(PD)</td>
<td>弱下拉电阻</td>
<td> -</td>
<td> -</td>
<td>20 k</td>
<td> -</td>
<td>Ω</td>
</tr>
</tbody>
</table>

### 4.5 看门狗

看门狗数字引脚电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>T(WD_MIN)</td>
<td>最小看门狗时间</td>
<td> -</td>
<td>- </td>
<td>1</td>
<td> -</td>
<td>s</td>
</tr>
<tr>
<td>T(WD_MAX)</td>
<td>最大看门狗时间</td>
<td> -</td>
<td> -</td>
<td>16</td>
<td> -</td>
<td>s</td>
</tr>
</tbody>
</table>

## 4.6 LDO

### 4.6.1 AONLDO

AONLDO 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>V(DD)</td>
<td>输入电压范围</td>
<td>V(IN) = V(SYS)</td>
<td>2.7</td>
<td> -</td>
<td>5.5</td>
<td>V</td>
</tr>
<tr>
<td>V(LDO)</td>
<td>输出电压范围</td>
<td>- </td>
<td>0.5</td>
<td> -</td>
<td>3.4</td>
<td>V</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(LDO_ACC)</td>
<td rowspan=2 colspan=1>输出电压精度 </td>
<td>V(OUT) &gt; 1.2V</td>
<td>- </td>
<td> -</td>
<td>±1</td>
<td>%</td>
</tr>
<tr>
<td>V(OUT) &lt; 1.2V</td>
<td>-</td>
<td> -</td>
<td>±12</td>
<td>mV</td>
</tr>
<tr>
<td>I(OUT_MAX)</td>
<td>输出电流</td>
<td> -</td>
<td>- </td>
<td> -</td>
<td>0.2</td>
<td>A</td>
</tr>
<tr>
<td>I(OCP)</td>
<td>过流保护</td>
<td> -</td>
<td> -</td>
<td>0.3</td>
<td>- </td>
<td>A</td>
</tr>
<tr>
<td>I(SHORT)</td>
<td>短路电流</td>
<td> -</td>
<td> -</td>
<td>0.15</td>
<td> -</td>
<td>A</td>
</tr>
<tr>
<td>V(DROPOUT)</td>
<td>电压降</td>
<td>V(OUT) = 1.8 V, I(OUT_MAX)</td>
<td> -</td>
<td>0.3</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(S_LINE)</td>
<td>静态线性调整</td>
<td>V(IN) = 3 ~ 5 V</td>
<td> -</td>
<td>10</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>V(S_LOAD)</td>
<td>静态负载调整</td>
<td>I(LOAD) = 10 ~ 100 mA</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>PSRR</td>
<td>PSRR</td>
<td>I(OUT) = I(MAX) / 2, V(IN) - V(OUT) &gt; 1 V</td>
<td> -</td>
<td>60</td>
<td> -</td>
<td>dB</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Noise</td>
<td rowspan=2 colspan=1>输出噪声</td>
<td>V(OUT) = 1.8 V, I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>35</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>V(OUT ) = 2.5 V, I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>35</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>I(Q_ON)</td>
<td>开机模式静态电流</td>
<td>- </td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>μA</td>
</tr>
<tr>
<td>R(OFF)</td>
<td>关机模式下拉电阻</td>
<td>- </td>
<td> -</td>
<td>160</td>
<td> -</td>
<td>ohm</td>
</tr>
<tr>
<td>OV</td>
<td>过压</td>
<td>V(OUT)/V(OUT_TARGET)-1</td>
<td> -</td>
<td>20</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>UV</td>
<td>欠压</td>
<td>1- V(OUT)/V(OUT_TARGET)</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>%</td>
</tr>
</tbody>
</table>

### 4.6.2 ALDO1~4

ALDO1~4 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>V(DD)</td>
<td>输入电压范围</td>
<td>V(IN) = V(SYS)</td>
<td>2.7</td>
<td> -</td>
<td>5.5</td>
<td>V</td>
</tr>
<tr>
<td>V(LDO)</td>
<td>输出电压范围</td>
<td>- </td>
<td>0.5</td>
<td> -</td>
<td>3.4</td>
<td>V</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(LDO_ACC)</td>
<td rowspan=2 colspan=1>输出电压精度</td>
<td>V(OUT) &gt; 1.2 V</td>
<td> -</td>
<td> -</td>
<td>±1</td>
<td>%</td>
</tr>
<tr>
<td>V(OUT) &lt; 1.2 V</td>
<td> -</td>
<td> -</td>
<td>±12</td>
<td>mV</td>
</tr>
<tr>
<td>I(OUT_MAX)</td>
<td>输出电流</td>
<td> -</td>
<td> -</td>
<td> -</td>
<td>0.3</td>
<td>A</td>
</tr>
<tr>
<td>I(OCP)</td>
<td>过流保护</td>
<td> -</td>
<td> -</td>
<td>0.5</td>
<td>- </td>
<td>A</td>
</tr>
<tr>
<td>I(SHORT)</td>
<td>短路电流</td>
<td> -</td>
<td> -</td>
<td>0.25</td>
<td> -</td>
<td>A</td>
</tr>
<tr>
<td>V(DROPOUT)</td>
<td>电压降</td>
<td>V(IN)=2.0 V，I(OUT_MAX)</td>
<td> -</td>
<td>0.3</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(S_LINE)</td>
<td>静态线性调整</td>
<td>V(IN)= 3 ~ 5 V</td>
<td> -</td>
<td>10</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>V(S_LOAD)</td>
<td>静态负载调整</td>
<td>I(LOAD) = 10 ~ 100 mA</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>PSRR</td>
<td>PSRR</td>
<td>I(OUT)= I(MAX) / 2，V(IN ) - V(OUT ) &gt; 1 V</td>
<td> -</td>
<td>70</td>
<td> -</td>
<td>dB</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Noise</td>
<td rowspan=2 colspan=1>输出噪声</td>
<td>V(OUT) = 1.8 V，I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>30</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>V(OUT )= 2.5 V，I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>30</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>I(Q_ON)</td>
<td>开机模式静态电流</td>
<td> -</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>μA</td>
</tr>
<tr>
<td>R(OFF)</td>
<td>关机模式下拉电阻</td>
<td> -</td>
<td> -</td>
<td>160</td>
<td> -</td>
<td>Ω</td>
</tr>
<tr>
<td>OV</td>
<td>过压</td>
<td>V(OUT)/V(OUT_TARGET)-1</td>
<td> -</td>
<td>20</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>UV</td>
<td>欠压</td>
<td>1- V(OUT)/V(OUT_TARGET)</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>%</td>
</tr>
</tbody>
</table>

### 4.6.3 DLDO1/2/3/5/6

DLDO1/2/3/5/6 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(DD)</td>
<td rowspan=2 colspan=1>输入电压范围</td>
<td>V(IN) = V(SYS)</td>
<td>2.7</td>
<td> -</td>
<td>5.5</td>
<td>V</td>
</tr>
<tr>
<td>来自Buck的输入电压V(IN) </td>
<td>2.1</td>
<td> -</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(LDO)</td>
<td>输出电压范围</td>
<td>- </td>
<td>0.5</td>
<td> -</td>
<td>3.4</td>
<td>V</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(LDO_ACC)</td>
<td rowspan=2 colspan=1>输出电压精度</td>
<td>V(OUT) &gt; 1.2 V</td>
<td>  </td>
<td> -</td>
<td>±1</td>
<td>%</td>
</tr>
<tr>
<td>V(OUT) &lt; 1.2 V</td>
<td> -</td>
<td> -</td>
<td>±12</td>
<td>%</td>
</tr>
<tr>
<td>I(OUT_MAX)</td>
<td>输出电流</td>
<td>- </td>
<td> -</td>
<td> -</td>
<td>0.3</td>
<td>A</td>
</tr>
<tr>
<td>I(OCP)</td>
<td>过流保护</td>
<td>-</td>
<td> -</td>
<td>0.5</td>
<td>- </td>
<td>A</td>
</tr>
<tr>
<td>I(SHORT)</td>
<td>短路电流</td>
<td>-</td>
<td> -</td>
<td>0.25</td>
<td> -</td>
<td>A</td>
</tr>
<tr>
<td>V(DROPOUT)</td>
<td>电压降</td>
<td>V(IN) = 2.1 V，I(OUT_MAX)</td>
<td> -</td>
<td>0.3</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(S_LINE)</td>
<td>静态线性调整</td>
<td>V(IN) = 3 ~ 5 V</td>
<td> -</td>
<td>10</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>V(S_LOAD)</td>
<td>静态负载调整</td>
<td>I(LOAD) = 10 ~ 100 mA</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>PSRR</td>
<td>PSRR</td>
<td>I(OUT ) = I(MAX) / 2，<br/>V(IN )- V(OUT ) &gt; 1 V</td>
<td> -</td>
<td>60</td>
<td> -</td>
<td>dB</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Noise</td>
<td rowspan=2 colspan=1>输出噪声</td>
<td>V(OUT) = 1.8 V，<br/>I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>35</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>V(OUT) = 2.5 V，<br/>I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>35</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>I(Q_ON)</td>
<td>开机模式静态电流</td>
<td>- </td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>μA</td>
</tr>
<tr>
<td>R(OFF)</td>
<td>关机模式下拉电阻</td>
<td> -</td>
<td> -</td>
<td>160</td>
<td> -</td>
<td>Ω</td>
</tr>
<tr>
<td>OV</td>
<td>过压</td>
<td>V(OUT)/V(OUT_TARGET)-1</td>
<td> -</td>
<td>20</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>UV</td>
<td>欠压</td>
<td>1- V(OUT)/V(OUT_TARGET)</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>%</td>
</tr>
</tbody>
</table>

### 4.6.4 DLDO4/7

DLDO4/7 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(DD)</td>
<td rowspan=2 colspan=1>输入电压范围 </td>
<td>V(IN) = V(SYS)</td>
<td>2.7</td>
<td> -</td>
<td>5.5</td>
<td>V</td>
</tr>
<tr>
<td>来自Buck的输入电压V(IN)</td>
<td>2.1</td>
<td> -</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(LDO)</td>
<td>输出电压范围</td>
<td> -</td>
<td>0.5</td>
<td> -</td>
<td>3.4</td>
<td>V</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(LDO_ACC)</td>
<td rowspan=2 colspan=1>输出电压精度</td>
<td>V(OUT) &gt; 1.2 V</td>
<td> -</td>
<td> -</td>
<td>±1</td>
<td>%</td>
</tr>
<tr>
<td>V(OUT) &lt; 1.2 V</td>
<td> -</td>
<td> -</td>
<td>±12</td>
<td>%</td>
</tr>
<tr>
<td>I(OUT_MAX)</td>
<td>输出电流</td>
<td> -</td>
<td> -</td>
<td> -</td>
<td>0.5</td>
<td>A</td>
</tr>
<tr>
<td>I(OCP)</td>
<td>过流保护</td>
<td> -</td>
<td> -</td>
<td>0.8</td>
<td>- </td>
<td>A</td>
</tr>
<tr>
<td>I(SHORT)</td>
<td>短路电流</td>
<td> -</td>
<td> -</td>
<td>0.4</td>
<td>-</td>
<td>A</td>
</tr>
<tr>
<td>V(DROPOUT)</td>
<td>电压降</td>
<td>V(IN) = 2.1 V，I(OUT_MAX)</td>
<td> -</td>
<td>0.4</td>
<td>-</td>
<td>V</td>
</tr>
<tr>
<td>V(S_LINE)</td>
<td>静态线性调整</td>
<td>V(IN) = 3 ~ 5 V</td>
<td> -</td>
<td>10</td>
<td>- </td>
<td>mV</td>
</tr>
<tr>
<td>V(S_LOAD)</td>
<td>静态负载调整</td>
<td>I(LOAD) = 10 ~ 100 mA</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>PSRR</td>
<td>PSRR</td>
<td>I(OUT) = I(MAX) / 2，V(IN ) - V(OUT )&gt; 1 V</td>
<td> -</td>
<td>60</td>
<td> -</td>
<td>dB</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Noise</td>
<td rowspan=2 colspan=1>输出噪声</td>
<td>V(OUT) = 1.8 V，I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>35</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>V(OUT)= 2.5 V，I(OUT) = 5 mA - I(MAX)</td>
<td> -</td>
<td>35</td>
<td> -</td>
<td>μVrms</td>
</tr>
<tr>
<td>I(Q_ON)</td>
<td>开机模式静态电流</td>
<td> -</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>μA</td>
</tr>
<tr>
<td>R(OFF)</td>
<td>关机模式下拉电阻</td>
<td> -</td>
<td> -</td>
<td>160</td>
<td> -</td>
<td>Ω</td>
</tr>
<tr>
<td>OV</td>
<td>过压</td>
<td>V(OUT)/V(OUT_TARGET)-1</td>
<td> -</td>
<td>20</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>UV</td>
<td>欠压</td>
<td>1 - V(OUT)/V(OUT_TARGET)</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>%</td>
</tr>
</tbody>
</table>

### 4.7 BUCK1~6

BUCK1~6 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td rowspan=1 colspan=7><strong>Buck</strong><strong>的整体参数</strong></td>
</tr>
<tr>
<td>V(IN_MIN)</td>
<td>最小输入电压</td>
<td> -</td>
<td>- </td>
<td>2.7</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(IN_MAX)</td>
<td>最大输入电压</td>
<td> -</td>
<td> -</td>
<td>5.5</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(OUT_MIN)</td>
<td>最小输出电压</td>
<td> -</td>
<td> -</td>
<td>0.5</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>V(OUT_MAX)</td>
<td>最大输出电压</td>
<td> -</td>
<td> -</td>
<td>3.4</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(OUT_STEPS)</td>
<td rowspan=2 colspan=1>调压步幅</td>
<td>V(OUT) = 0.5 ~ 1.35 V</td>
<td> -</td>
<td>5</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>V(OUT) = 1.35 ~ 3.4 V</td>
<td> -</td>
<td>25</td>
<td> -</td>
<td>mV</td>
</tr>
<tr>
<td>V(SLEW)</td>
<td>DVS档位</td>
<td> -</td>
<td> -</td>
<td>5/10/25/50</td>
<td> -</td>
<td>mV/us</td>
</tr>
<tr>
<td>T(SFST)</td>
<td>软启动时间</td>
<td> -</td>
<td> -</td>
<td>1</td>
<td> -</td>
<td>ms</td>
</tr>
<tr>
<td>T(SFST_SET)</td>
<td>软启动档位设置</td>
<td> -</td>
<td> -</td>
<td>0.78/0.9/1.12</td>
<td> -</td>
<td>ms</td>
</tr>
<tr>
<td>R(DIDCHG)</td>
<td>泄放电阻</td>
<td> -</td>
<td> -</td>
<td>45</td>
<td> -</td>
<td>Ω</td>
</tr>
<tr>
<td>fsw</td>
<td>工作频率</td>
<td>CCM</td>
<td> -</td>
<td>1.5</td>
<td> -</td>
<td>MHz</td>
</tr>
<tr>
<td>OV</td>
<td>过压</td>
<td>V(OUT)/V(OUT_TARGET)-1</td>
<td> -</td>
<td>20</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>UV</td>
<td>欠压</td>
<td>1- V(OUT)/V(OUT_TARGET)</td>
<td> -</td>
<td>15</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(BUCK_ACC)</td>
<td rowspan=2 colspan=1>输出电压精度</td>
<td>（不含线性/负载调整）<br/>V(OUT) &gt; 1 V</td>
<td> -</td>
<td> -</td>
<td>±1</td>
<td>%</td>
</tr>
<tr>
<td>（不含线性/负载调整）<br/>V(OUT) &lt; 1 V</td>
<td> -</td>
<td>- </td>
<td>±10</td>
<td>mV</td>
</tr>
<tr>
<td>V(S_LOAD)</td>
<td>静态负载调整</td>
<td>I(OUT) = 0.1 ~ 2 A，V(OUT)= 1 V</td>
<td> -</td>
<td> -</td>
<td>±1</td>
<td>%</td>
</tr>
<tr>
<td>V(S_LINE)</td>
<td>静态线性调整</td>
<td>V(IN) = 3 ~ 5 V，V(OUT) = 1 V</td>
<td> -</td>
<td> -</td>
<td>±1</td>
<td>%</td>
</tr>
<tr>
<td rowspan=4 colspan=1>V(TR_LD)</td>
<td rowspan=4 colspan=1>负载瞬态响应<br/>(C(OUT)=44uF，I(OUT)=0.02 ~ 2.7 A) </td>
<td>undershoot，V(OUT)&lt; 1.2 V</td>
<td> -</td>
<td>30</td>
<td>60</td>
<td>mV</td>
</tr>
<tr>
<td>undershoot，V(OUT)&gt; 1.2 V</td>
<td> -</td>
<td>3</td>
<td>5</td>
<td>%</td>
</tr>
<tr>
<td>overshoot，V(OUT) &lt; 1.6 V</td>
<td> -</td>
<td>72</td>
<td>80</td>
<td>mV</td>
</tr>
<tr>
<td>overshoot，V(OUT) &gt; 1.6 V</td>
<td> -</td>
<td>- </td>
<td>5</td>
<td>%</td>
</tr>
<tr>
<td rowspan=2 colspan=1>V(RIPPLE)</td>
<td rowspan=2 colspan=1>输出纹波</td>
<td>I(OUT) = 0.1 A，V(OUT) = 1.1 V</td>
<td> -</td>
<td>13</td>
<td>25</td>
<td>mV</td>
</tr>
<tr>
<td>I(OUT) &gt; 1 A，V(OUT) = 1.1 V</td>
<td> -</td>
<td>7</td>
<td>20</td>
<td>mV</td>
</tr>
<tr>
<td rowspan=1 colspan=7><strong>Buck 1 ~ 2</strong></td>
</tr>
<tr>
<td>I(OUT_MAX)</td>
<td>输出电流 </td>
<td>OCP large=1</td>
<td>4.0</td>
<td>-</td>
<td> -</td>
<td>A</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Efficiency</td>
<td rowspan=2 colspan=1>效率</td>
<td>V(IN) = 4 V，V(OUT) = 0.9 V<br/>I(OUT) = 0.5 A</td>
<td>- </td>
<td>86.3<br/></td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>V(IN) = 4 V，V(OUT) = 0.9 V<br/>I(OUT) = 2.5 A</td>
<td> -<br/></td>
<td>78.2</td>
<td> -</td>
<td>% </td>
</tr>
<tr>
<td>D(ACC)</td>
<td>双相精度</td>
<td>I(OUT) = 6A</td>
<td> -</td>
<td>10.0</td>
<td>20.0</td>
<td>%</td>
</tr>
<tr>
<td>R(PU)</td>
<td>弱上拉电阻</td>
<td rowspan=2 colspan=1>V(IN) = 4 V</td>
<td> -</td>
<td>80</td>
<td>- </td>
<td>mΩ</td>
</tr>
<tr>
<td>R(PD)</td>
<td>弱下拉电阻</td>
<td> -</td>
<td>40</td>
<td>- </td>
<td>mΩ</td>
</tr>
<tr>
<td rowspan=1 colspan=7><strong>Buck 3 ~ 4</strong></td>
</tr>
<tr>
<td>I(OUT_MAX)</td>
<td>输出电流</td>
<td> </td>
<td>2.5</td>
<td>3.5</td>
<td> -</td>
<td>A</td>
</tr>
<tr>
<td>I(VALLEY_LIMIT)</td>
<td></td>
<td>正常电平</td>
<td>3.0</td>
<td>- </td>
<td>- </td>
<td>A</td>
</tr>
<tr>
<td rowspan=2 colspan=1>Efficiency</td>
<td rowspan=2 colspan=1>效率</td>
<td>V(IN) = 4 V，V(OUT) = 1.8 V<br/>I(OUT) = 0.5 A</td>
<td> -</td>
<td>90.6</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>V(IN) = 4 V，V(OUT) = 1.8 V<br/>I(OUT) = 2.5 A</td>
<td> -</td>
<td>83.4</td>
<td>-</td>
<td> %</td>
</tr>
<tr>
<td>D(ACC)</td>
<td>双相精度</td>
<td>I(OUT) = 5A</td>
<td> -</td>
<td>- </td>
<td>20.0</td>
<td>%</td>
</tr>
<tr>
<td>R(PU)</td>
<td>弱上拉电阻</td>
<td rowspan=2 colspan=1>V(IN) = 4 V </td>
<td> -</td>
<td>100</td>
<td> -</td>
<td>mΩ</td>
</tr>
<tr>
<td>R(PD)</td>
<td>弱下拉电阻</td>
<td>- </td>
<td>50</td>
<td> -</td>
<td>mΩ</td>
</tr>
<tr>
<td rowspan=1 colspan=7><strong>Buck 5 ~ 6</strong></td>
</tr>
<tr>
<td>I(OUT_MAX)</td>
<td>输出电流</td>
<td> </td>
<td>2.5</td>
<td> -</td>
<td>- </td>
<td>A</td>
</tr>
<tr>
<td>I(VALLEY_LIMIT)</td>
<td></td>
<td>正常电平</td>
<td>3.0</td>
<td> -</td>
<td> -</td>
<td>A</td>
</tr>
<tr>
<td rowspan=4 colspan=1>Efficiency</td>
<td rowspan=4 colspan=1>效率</td>
<td>V(IN) = 4 V，V(OUT) = 1.1 V<br/>I(OUT) = 0.5 A</td>
<td> -</td>
<td>87.7</td>
<td> -</td>
<td>%</td>
</tr>
<tr>
<td>V(IN) = 4 V，V(OUT) = 1.1 V<br/>I(OUT) = 2.5 A</td>
<td> -</td>
<td>79.9</td>
<td> -</td>
<td> %</td>
</tr>
<tr>
<td>V(IN) = 4 V，V(OUT) = 2.1 V<br/>I(OUT) = 0.5 A</td>
<td> -</td>
<td>91.6</td>
<td> -</td>
<td> %</td>
</tr>
<tr>
<td>V(IN) = 4 V，V(OUT) = 2.1 V<br/>I(OUT) = 2.5 A</td>
<td> -</td>
<td>86.8</td>
<td> -</td>
<td> %</td>
</tr>
<tr>
<td>R(PU)</td>
<td>弱上拉电阻</td>
<td rowspan=2 colspan=1>V(IN) = 4 V </td>
<td> -</td>
<td>100</td>
<td> -</td>
<td>mΩ</td>
</tr>
<tr>
<td>R(PD)</td>
<td>弱下拉电阻</td>
<td> -</td>
<td>50</td>
<td> -</td>
<td>mΩ</td>
</tr>
</tbody>
</table>

### 4.8 负载开关

负载开关电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>SW(IN-MIN)</td>
<td>最小输入电压</td>
<td>V(SYS) = 4V</td>
<td> -</td>
<td>2.7</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>SW(IN-MAX)</td>
<td>最大输入电压</td>
<td>V(SYS) = 4V</td>
<td> -</td>
<td>5.5</td>
<td> -</td>
<td>V</td>
</tr>
<tr>
<td>R(ON) </td>
<td>导通电阻</td>
<td>SWIN=5V</td>
<td> -</td>
<td>140</td>
<td> -</td>
<td>mohm</td>
</tr>
<tr>
<td>I_SC</td>
<td>短路电路</td>
<td> </td>
<td> -</td>
<td>0.5</td>
<td> -</td>
<td>A </td>
</tr>
<tr>
<td>I_MAX</td>
<td>最大电流</td>
<td> </td>
<td> -</td>
<td>1.6</td>
<td> -</td>
<td>A</td>
</tr>
</tbody>
</table>

### 4.9 ADC

ADC 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>Resolution</td>
<td>分辨率</td>
<td>- </td>
<td>- </td>
<td>12</td>
<td> -</td>
<td>Bits</td>
</tr>
<tr>
<td>VDD</td>
<td>供电电压</td>
<td> -</td>
<td>2.7</td>
<td> -</td>
<td>5.5</td>
<td>V</td>
</tr>
<tr>
<td>DNL</td>
<td>微分非线性</td>
<td>2.7 ~ 5.5 V<br/>-40 ~ 105 ℃</td>
<td>-3</td>
<td> -</td>
<td>3</td>
<td>LSB</td>
</tr>
<tr>
<td>INL</td>
<td>积分非线性</td>
<td>2.7 ~ 5.5 V<br/>-40 ~ 105 ℃</td>
<td>-4</td>
<td>- </td>
<td>4</td>
<td>LSB</td>
</tr>
<tr>
<td>Offset error</td>
<td>偏移误差</td>
<td>2.7 ~ 5.5 V<br/>-40 ~ 105 ℃</td>
<td>-4</td>
<td>- </td>
<td>4</td>
<td>LSB</td>
</tr>
<tr>
<td>Gain error</td>
<td>增益误差</td>
<td>2.7 ~ 5.5 V<br/>-40 ~ 105 ℃</td>
<td>-4</td>
<td> -</td>
<td>4</td>
<td>LSB</td>
</tr>
<tr>
<td>Sample rate</td>
<td>采样率</td>
<td>25 ℃</td>
<td>0.1</td>
<td> -</td>
<td>25</td>
<td>Ksps</td>
</tr>
<tr>
<td>I(WORK)</td>
<td>工作电流</td>
<td>5V，25 ℃</td>
<td>- </td>
<td>190</td>
<td> -</td>
<td>μA</td>
</tr>
</tbody>
</table>

### 4.10 ADC 内部基准电气

ADC 内部基准电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>V(REF_2V)</td>
<td>2V基准电压</td>
<td>2.7 ~ 5.5 V，25 ℃</td>
<td>1.995</td>
<td>2</td>
<td>2.005</td>
<td>V</td>
</tr>
<tr>
<td>V(REF_3V)</td>
<td>3V基准电压</td>
<td>3.5 ~ 5.5 V，25 ℃</td>
<td>2.995</td>
<td>3</td>
<td>3.005</td>
<td>V</td>
</tr>
<tr>
<td>I(WORK)</td>
<td>工作电流</td>
<td>5.0V，-40 ~ 105 ℃</td>
<td> -</td>
<td>400</td>
<td> -</td>
<td>μA</td>
</tr>
</tbody>
</table>

### 4.11 内部时钟（内部 LSI 电气）

内部 LSI 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>F(ACC)</td>
<td>频率精度</td>
<td>5 V，25 ℃</td>
<td>30</td>
<td>32</td>
<td>34</td>
<td>kHz</td>
</tr>
<tr>
<td>V(C)</td>
<td>电压系数</td>
<td>2.0 ~ 5.5 V，25 ℃</td>
<td>-7</td>
<td>- </td>
<td>7</td>
<td>%</td>
</tr>
<tr>
<td>T(C)</td>
<td>温度系数</td>
<td>5V，-40 ~ 105 ℃</td>
<td>-10</td>
<td> -</td>
<td>10</td>
<td>%</td>
</tr>
<tr>
<td>I(WORK)</td>
<td>工作电流</td>
<td>2.0 ~ 5.5 V，-40 ~ 105 ℃</td>
<td>0.4</td>
<td>0.9</td>
<td>1.5</td>
<td>μA</td>
</tr>
</tbody>
</table>

### 4.12 内部时钟（内部 HSI 电气）

内部 HSI 电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>F(ACC)</td>
<td>频率精度</td>
<td>5 V，25 ℃</td>
<td>1.98</td>
<td>2</td>
<td>2.02</td>
<td>MHz</td>
</tr>
<tr>
<td>V(C)</td>
<td>电压系数</td>
<td>2.0 ~ 5.5 V，25 ℃</td>
<td>-0.5</td>
<td> -</td>
<td>0.5</td>
<td>%</td>
</tr>
<tr>
<td>T(C)</td>
<td>温度系数</td>
<td>5V，-40 ~ 105 ℃</td>
<td>-3</td>
<td> -</td>
<td>3</td>
<td>%</td>
</tr>
<tr>
<td>I(WORK)</td>
<td>工作电流</td>
<td>2.0 ~ 5.5 V，-40 ~ 105 ℃</td>
<td>45</td>
<td>80</td>
<td>120</td>
<td>μA</td>
</tr>
</tbody>
</table>

### 4.13 32 kHz 晶振

晶体振荡器电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>C(LOAD)</td>
<td>外挂负载电容</td>
<td>2.7 ~ 5.5 V，-40 ~ 105 ℃</td>
<td>7</td>
<td>22.5</td>
<td>30</td>
<td>pF</td>
</tr>
<tr>
<td>I(WORK)</td>
<td>工作电流</td>
<td>5 V，25 ℃，C(LOAD) = 12.5 pF</td>
<td>- </td>
<td>1</td>
<td>- </td>
<td>μA</td>
</tr>
<tr>
<td>T(SETUP)</td>
<td>起振时间</td>
<td>5 V，25 ℃</td>
<td> -</td>
<td>0.6</td>
<td> -</td>
<td>s</td>
</tr>
</tbody>
</table>

### 4.14 POR/PDR

上电掉电复位电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>POR</td>
<td>上电复位电压</td>
<td>-40 ~ 105 ℃</td>
<td>1.75</td>
<td>2.0</td>
<td>2.25</td>
<td>V</td>
</tr>
<tr>
<td>PDR</td>
<td>掉电复位电压</td>
<td>-40 ~ 105 ℃</td>
<td>1.75</td>
<td>2.0</td>
<td>2.25</td>
<td>V</td>
</tr>
<tr>
<td>T(FILTER)</td>
<td>POR脉冲干扰滤波长度</td>
<td>25 ℃，3 V ~ 1.5 V</td>
<td>- </td>
<td>2.0</td>
<td>- </td>
<td>us</td>
</tr>
<tr>
<td>I(WORK)</td>
<td>工作电流</td>
<td>2.0 ~ 5.5 V，-40 ~ 105 ℃</td>
<td>0.1</td>
<td>0.3</td>
<td>1</td>
<td>μA</td>
</tr>
</tbody>
</table>

### 4.15 RTC 模块 POR/PDR

RTC 上电掉电复位电气特性如下表描述

<table>
<tbody>
<tr>
<td>参数</td>
<td>描述</td>
<td>条件</td>
<td>最小值</td>
<td>典型值</td>
<td>最大值</td>
<td>单位</td>
</tr>
<tr>
<td>POR</td>
<td>上电复位电压</td>
<td>-40 ~ 105 ℃</td>
<td>1.55</td>
<td>1.7</td>
<td>1.85</td>
<td>V</td>
</tr>
<tr>
<td>PDR</td>
<td>掉电复位电压</td>
<td>-40 ~ 105 ℃</td>
<td>1.55</td>
<td>1.7</td>
<td>1.85</td>
<td>V</td>
</tr>
<tr>
<td>I(WORK)</td>
<td>工作电流</td>
<td>2.0 ~ 5.5 V，-40 ~ 105 ℃</td>
<td>0.1</td>
<td>0.3</td>
<td>1</td>
<td>μA</td>
</tr>
</tbody>
</table>

## 5. 核心电源管理功能

P1 是一款低压多通道电源管理芯片（PMIC），专为满足不同 SoC 平台的电源需求而设计。它内部集成了 6 路快速瞬态响应的降压转换器（BUCK）和 12 路低噪声低压差稳压器（LDO），能够为多种应用提供高效的电源管理解决方案。

本章详细阐述 P1 PMIC 的核心电源管理功能，包括电压转换（BUCK/LDO）、动态电源时序控制及保护机制，确保系统获得稳定高效的电能供给。

### 5.1 电源管理引脚

电源管理引脚说明如下表描述

<table>
<tbody>
<tr>
<td>引脚</td>
<td>电源</td>
<td>描述</td>
</tr>
<tr>
<td><strong>PWRKY</strong></td>
<td>VSYS</td>
<td>开关机控制引脚，同时作为PMIC复位按键；<br/>支持关机、短按、长按、上升沿、下降沿中断功能。</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>OPEN DRAIN</td>
<td>中断引脚，支持INT下拉以开机。</td>
</tr>
<tr>
<td><strong>PGOOD</strong></td>
<td>OPEN DRAIN</td>
<td>- Input：检测PGOOD引脚释放，可作为复位源。<br/>- Output：PMIC关机或复位时下拉PGOOD，用于复位SoC。</td>
</tr>
<tr>
<td><strong>PWRCTRL</strong></td>
<td>AONLDO</td>
<td>GPIO复用输入功能，用于控制上下电、睡眠和唤醒流程。</td>
</tr>
<tr>
<td><strong>SLEEP/WKUP</strong></td>
<td>AONLDO</td>
<td>GPIO复用输入功能，用于控制睡眠或唤醒操作。</td>
</tr>
<tr>
<td><strong>nRESET</strong></td>
<td>AONLDO</td>
<td>GPIO复用输入功能，作为复位源（先关机再重启）。</td>
</tr>
<tr>
<td><strong>EXT_EN</strong></td>
<td>AONLDO</td>
<td>GPIO复用输出功能，可与其他PMIC配合使用。</td>
</tr>
<tr>
<td><strong>VSET5</strong></td>
<td>VSYS</td>
<td>用于BUCK5电压控制档位选择。</td>
</tr>
<tr>
<td><strong>VSET6</strong></td>
<td>VSYS</td>
<td>用于BUCK6电压控制档位选择。</td>
</tr>
<tr>
<td><strong>OUT_32K</strong></td>
<td>AONLDO</td>
<td>内部慢时钟或晶振时钟输出引脚。</td>
</tr>
</tbody>
</table>

#### 5.1.1 PWRKY 引脚

PWRKY 引脚内部上拉至 VSYS 电压，具备以下多功能性：

- **作为开机源、关机源、复位源**
- **生成多种中断事件**（包括关机、短按、长按、上升沿、下降沿中断）

1. **关机模式**下的 PWRKY 引脚行为

   - **开机功能**
     - PWRKY 引脚拉低一定时间后触发开机流程
     - 时间可配置为 **0.5s/1s/2s/3s**（参见表 7-91 PWR\_KEY\_TIME[1:0]）
   - **长按关机功能**
     - 若启用长按关机功能（表 7-126 SYS\_CFG1[0]=1），在关机模式下，PWRKY 引脚需持续拉低直至退出关机模式。
     - 如果退出关机模式后，PWRKY 引脚仍保持拉低状态，并且拉低时间超过 **4s/6s/8s/10s**（由表 7-91 PWR\_KEY\_TIME[3:2] 配置），则触发关机。
2. **非关机模式**下的 PWRKY 引脚行为

   - **关机功能**
     - PWRKY 引脚可作为关机源（表 7-88 PWR\_CTRL2[6]=0）
     - PWRKY 引脚拉低一定时间后触发关机，时间可配置为 **4s/6s/8s/10s**（参见表 7-91 PWR\_KEY\_TIME[3:2]）
   - **长按复位功能**
     - 若 PWRKY 引脚作为长按复位源（表 7-88 PWR\_CTRL2[6]=1），拉低 **12s** 将触发 PMIC 冷复位
     - 此复位操作会重置所有逻辑，包括所有模块的使能和配置（包括 RTC 模块），等效于冷启动
   - **长按复位结合关机模式**
     - 若启用长按复位功能（表 7-126 SYS\_CFG1[1]=1），在关机模式下 PWRKY 引脚持续拉低至退出关机模式
     - 如果退出关机模式后，PWRKY 引脚仍保持拉低状态，并且拉低时间超过 **12s**，将触发冷复位
3. **开机模式或睡眠模式**下的中断事件

   - **下降沿事件**
     - PWRKY 引脚拉低时产生下降沿事件
     - 若使能中断（表 7-120 IRQ\_PWRKY\_EN[4]），将触发 **下降沿中断**
   - **上升沿事件**
     - PWRKY 引脚拉低后释放时产生上升沿事件
     - 若使能中断（表 7-120 IRQ\_PWRKY\_EN[0]），将触发 **上升沿中断**
   - **短按事件**
     - PWRKY 引脚拉低再释放，且持续时间在短按时间范围内，产生短按事件
     - 若使能中断（表 7-120 IRQ\_PWRKY\_EN[2]），将触发 **短按中断**
     - 短按时间可配置为 **0.5s/1s/1.5s/2s**（表 7-91 PWR\_KEY\_TIME[5:4]）
   - **长按事件**
     - PWRKY 引脚拉低再释放，且持续时间介于短按和关机时间之间，产生长按事件
     - 若使能中断（表 7-120 IRQ\_PWRKY\_EN[3]），将触发 **长按中断**

PWRKY 按键开机模式相关事件触发示意图如下图所示

![](static/YA21bY2dBoZiMmx6lAhc69klnNc.png)

PWRKY 按键关机模式相关事件触发示意图如下图所示

![](static/ZpJkbaNCmorgpVxLrEScWBmznNf.png)

图 6-2 PWRKY 按键关机模式相关事件触发示意图

#### 5.1.2 INT 引脚

INT 引脚为开漏输出，内部施密特输入电路工作在 AONLDO 电压。

- **关机模式**

  - 若设置 INT 引脚作为开机源（表 7-86 PWR\_CTRL0[2]=1），当 INT 引脚拉低持续 16 ms 后，将触发开机流程。
- **开机模式**

  - 在开机状态下，当芯片内部事件触发且相应中断已使能时（例如按键中断事件），INT 引脚将被拉低，输出中断信号。

#### 5.1.3 PGOOD 引脚

PGOOD 引脚为开漏输出，内部施密特输入电路工作在 AONLDO 电压。

- **关机流程或关机模式**

  - 在关机流程或关机模式下，PMIC 将 PGOOD 引脚拉低以复位外部模块，且在关机模式中 PGOOD 引脚始终保持低电平。
- **开机流程结束**

  - 开机流程完成后，PMIC 立即释放 PGOOD 引脚。
  - 如果 PWR\_CTRL1[3]=0（表 7-87），芯片直接进入开机模式；
  - 如果 PWR\_CTRL1[3]=1，需等待 PGOOD 引脚变为高电平后才能进入开机模式。
  - 若等待时间超时，芯片将立即进入关机模式，已开启的电源轨也会随之关闭。
- **开机模式**

  - 在开机模式下，若 PGOOD 引脚被拉低超过 200 µs，且 PGOOD 下拉复位 已使能（PG\_RST\_EN），将触发复位流程（先关机再开机）。
- **睡眠模式和睡眠流程**

  - PGOOD 引脚状态可通过 PWR\_CTRL1[5]（表 7-87）进行配置，默认情况下，PGOOD 引脚保持高电平。
- **唤醒流程结束**

  - 唤醒流程完成后，PMIC 立即释放 PGOOD 引脚并进入开机模式。

#### 5.1.4 PWRCTRL 引脚

PWRCTRL 引脚具有 GPIO 复用输入功能，内部施密特触发器工作在 AONLDO 电压下。

PWRCTRL 引脚主要用于控制 **开机**、**关机**、**睡眠** 和 **唤醒** 流程：

- **开机事件**
  在关机模式下，若满足以下条件，则 PWRCTRL 引脚有效时触发开机流程：

  - 除 AONLDO 外，其他所有 BUCK 和 LDO 均绑定至 PWRCTRL 引脚；
  - PWRCTRL 全绑定开机 功能已使能（表 7-86 PWR\_CTRL0[4]=1）。
- **关机事件**
  在非关机模式下，若满足以下条件，则 PWRCTRL 引脚无效时触发关机流程：

  - 所有 BUCK 和 LDO 均绑定至 PWRCTRL 引脚；
  - PWRCTRL 全绑定关机 功能已使能（表 7-86 PWR\_CTRL0[5]=1）。
- **开机和唤醒流程**
  当某个 BUCK 或 LDO 绑定到 PWRCTRL 引脚时，以下规则适用：

  - PWRCTRL 引脚有效 时，开机和唤醒流程可继续执行对应 BUCK 或 LDO 的开启操作；
  - 若 PWRCTRL 引脚无效，流程将暂停并持续等待该引脚有效。
- **睡眠流程**
  当某个 BUCK 或 LDO 绑定到 PWRCTRL 引脚，且符合以下条件时，执行睡眠操作需等待 PWRCTRL 引脚无效：

  - 反序睡眠 已配置（表 7-87 PWR\_CTRL1[1]=1）；
  - 等待 PWRCTRL 引脚 已使能（表 7-88 PWR\_CTRL2[4]=1）。
    如果等待时间超过表 7-88 PWR\_CTRL2[5]，则强制执行对应 BUCK 和 LDO 的睡眠操作，并继续流程进入睡眠模式。
- **关机流程**
  当某个 BUCK 或 LDO 绑定到 PWRCTRL 引脚，且符合以下条件时，执行关机操作需等待 PWRCTRL 引脚无效：

  - 反序关机 已配置（表 7-87 PWR\_CTRL1[0]=0）；
  - 等待 PWRCTRL 引脚 已使能（表 7-88 PWR\_CTRL2[4]=1）。
    若等待时间超过表 7-88 PWR\_CTRL2[5]，则强制执行对应 BUCK 和 LDO 的关闭操作，并继续关机流程。
- **开机模式**

在开机模式下，若某个 BUCK 或 LDO 绑定到 PWRCTRL 引脚，遵循以下规则：

- PWRCTRL 引脚无效 时，相关 BUCK 和 LDO 将直接关闭；
- PWRCTRL 引脚有效 且对应 BUCK 和 LDO 的使能位有效时，相关 BUCK 和 LDO 将直接开启。

PWRCTRL 引脚的有效极性 可通过 GPIOx\_ODR 寄存器进行配置。

#### 5.1.5 SLEEP/WKUP 引脚

SLEEP/WKUP 引脚为 GPIO 复用输入功能，其内部施密特触发器电路工作在 **AONLDO 电压域**。

该引脚用于控制设备进入和退出 **睡眠模式**，具体行为如下：

1. 开机模式：SLEEP/WKUP 引脚有效时，执行睡眠流程并进入睡眠模式。
2. 睡眠模式：SLEEP/WKUP 引脚无效时，执行唤醒流程并进入开机模式。

SLEEP/WKUP 引脚有效极性可通过**表 7-5 **GPIO\_ODR 寄存器配置。

#### 5.1.6 nRESET 引脚

nRESET 引脚为 GPIO 复用输入功能，其内部施密特输入电路工作在 **AONLDO 电压****域**。

1. **非关机模式下**：

   - 若 **nRESET 引脚复位使能**（PWR\_CTRL0[6] = 1，见表 7-86），当 **nRESET 引脚从无效状态变为有效状态并持续超过 250 μs** 时，系统将触发复位流程（**先关机再开机**）。
   - 若 **GPIO 滤波使能开启**，则 nRESET 引脚的复位触发时间需额外增加滤波延迟，计算公式为：
     **250 μs +（表 7-8 **GPIO\_DEB\_EN[7:6]** 配置值）**。
2. **复位流程触发后**：

   - 若 **nRESET 引脚保持有效状态**，系统不会重复触发复位。
   - 仅当 **nRESET 引脚释放（恢复无效状态）** 后，才能响应下一次复位操作。

**nRESET 引脚的有效极性** 可通过 **GPIO\_ODR 寄存器**（见表 7-5）配置。

#### 5.1.7 EXT\_EN 引脚

**EXT\_EN** 引脚为复用的 **GPIO 输出功能**，其内部施密特触发器电路工作在 **AONLDO 电压域**。

该引脚的行为受 **开机、关机、睡眠、唤醒流程** 控制，（结合相关寄存器描述和上下电流程章节）具体逻辑如下：

1. **开机和唤醒流程**

- 当 **EXT\_EN** 通过 **PWR\_SLOT9 ~ PWR\_SLOT11**（表 7-102 ~ 表 7-104）绑定至某一 **时序槽（SLOT）** 时：
  - 仅当流程执行到该 SLOT 时，才会对 **EXT\_EN** 执行相应操作。

1. **睡眠流程**

- 当 **EXT\_EN** 绑定至某一 SLOT 时：
  - 仅当流程执行到该 SLOT **且** 配置为 **受睡眠时序控制**（PWR\_EXT\_CTRL[5:0]，表 7-106）时，才会关闭相应的 **EXT\_EN** 输出。

1. **关机流程**

- 当 **EXT\_EN** 通过 **PWR\_SLOT9 ~ PWR\_SLOT11**（表 7-102 ~ 表 7-104）绑定至某一 **时序槽（SLOT）** 时：
  - 仅当流程执行到该 SLOT 时，才会关闭相应的 **EXT\_EN** 输出。

1. **开机模式**

- 由**表 7-104 **PWR\_EXT\_EN 控制。

1. 睡眠模式

- EXT\_EN 受**表 7-104 **PWR\_EXT\_EN 和** 表 7-106 **PWR\_EXT\_CTRL 共同控制。

EXT\_EN 引脚有效极性可通过**表 7-5 **GPIO\_ODR 寄存器配置。

下表展示了 EXT\_EN 各模式状态控制

<table>
<tbody>
<tr>
<td>(x = 0 ~ 5)</td>
<td>开机流程</td>
<td>开机模式</td>
<td>睡眠流程</td>
<td>睡眠模式</td>
<td>唤醒流程</td>
<td>关机流程</td>
<td>关机模式</td>
</tr>
<tr>
<td>EXTx_EN</td>
<td>x</td>
<td>x</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>EXTx_EN_SLOT</td>
<td>x</td>
<td>-</td>
<td>x</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>-</td>
</tr>
<tr>
<td>EXTx_SLP_SD</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
</table>

#### 5.1.8 VSET5/VSET6 引脚

**VSET5/VSET6** 引脚通过其状态（**GND、VSYS 或 FLOAT**）配置 **BUCK5/BUCK6 的输出电压**，以满足不同应用场景需求。

**VSET 电压控制逻辑**

<table>
<tbody>
<tr>
<td>表 7-74 BUCK_LDO_CFG[2]</td>
<td>VDD</td>
<td>FLOAT</td>
<td>GND</td>
</tr>
<tr>
<td>0</td>
<td>1.1 V</td>
<td>VBUCKx_VOLT(x=5/6)</td>
<td>1.2 V</td>
</tr>
<tr>
<td>1</td>
<td>0.6 V</td>
<td>VBUCKx_VOLT(x=5/6)</td>
<td>1.5 V</td>
</tr>
</tbody>
</table>

#### 5.1.9 OUT\_32K 引脚

**OUT\_32K** 引脚可输出 **内部慢时钟** 或 **晶振时钟**，通过 **RTC\_CTRL[3]**（表 7-33）寄存器配置。

1. **时钟输出控制**：

   - 可通过 **MTP** 预先配置为时钟输出模式
   - 在开机流程前即可为外部模块提供时钟源
2. **电源状态影响**：

   - **正常工作模式**：保持时钟输出
   - **关机模式**：关闭时钟输出

### 5.2 工作模式

系统工作模式总共有 5 种：RESET 模式，RTC 模式，关机模式，开机模式和睡眠模式，会根据不同的事件进行模式切换，下图为**模式切换状态图**。对应的切换事件主要有：开机事件、关机事件、复位事件、睡眠事件、唤醒事件。

![](static/VZFIbb6v7oKNUhx7IwZcN8PTnig.png)

#### 5.2.1 复位模式

- 当 **VSYS \< 2.7V** 时，PMIC 处于复位模式，所有功能停止工作
- 仅当 **VSYS ≥ 2.7V** 后，系统才退出复位模式并开始正常工作
- 若运行中 **VSYS 跌落至 \< 2.55V**，系统立即重新进入复位模式

#### 5.2.2 RTC 模式

- PMIC 的超低功耗工作模式
- 仅维持 **RTC 模块**和**晶振电路**运行（保持计时功能）

**进入条件**：

- **VSYS \< 2.0V**（无主电源供电）
- **VBAT \> 2.0V**（电池供电正常）

**退出条件**：

- 与复位模式相同：**VSYS ≥ 2.7V**（上电复位释放）

#### 5.2.3 关机模式

该模式下大部分模块不工作，保持工作的模块有：AONLDO，Bandgap，VSYS 电压检测，RTC，晶振电路，按键检测等。

**关机模式下可进一步降低功耗（SHUTDOWN\_LP）：**

- 当**表 7-87 **PWR\_CTRL1[7] = 1，则进入关机模式时还会额外关闭 AONLDO 和 Bandgap。

**进入该模式：**

- PMIC 上电复位释放后（VSYS \> 2.7 V）。
- 开机流程过程中：所有的关机和复位事件会直接进入。
- 其他情况：所有的关机和复位事件会触发关机流程，才会回到关机模式。

**退出该模式：**

- **表 7-87** PWR\_CTRL1[7] = 0 时：所有开机事件。
- **表 7-87** PWR\_CTRL1[7] = 1 时：PWRKY 按键开机事件，RTC 闹钟和 TICK 事件。

**复位事件进入该模式时会停留一段时间（****表 7-88 **PWR\_CTRL2[7]**），在这段时间内所有开机源无效：**

- 当 PWRKY 引脚拉低 12s 强制复位时，PMIC 会从当前状态立即切换到关机模式，等待**表 7-88 **PWR\_CTRL2[7]时间后再进入复位模式。
- 其余复位事件进入关机模式后，等待**表 7-88 **PWR\_CTRL2[7]时间后并且此时 VSYS 电压高于设定开机阈值，则自动再执行开机流程。

#### 5.2.4 开机模式

该模式下所有模块都可正常工作，包括所有电源轨，负载开关，电池充电，电压检测，内部参考，电源轨过压/欠压/短路/开路检测，过温检测，内部时钟，晶振电路，ADC，RTC，通信接口，GPIO 模块，按键检测，中断等。

**进入该模式：**

- 开机流程执行完
- 睡眠模式下唤醒

**退出该模式：**

- 关机、复位、睡眠事件

#### 5.2.5 睡眠模式

该模式可以将部分电源轨做降压或关闭处理，还可以配置拉低 PGOOD 引脚来复位 SoC。

- 进入该模式：开机模式下睡眠事件。
- 退出该模式：关机、复位、唤醒事件。

#### 5.2.6 各模式工作状态

表 6-4 PMIC 模式管理

<table>
<tbody>
<tr>
<td>电源域</td>
<td>模块</td>
<td>RESET</td>
<td>RTC</td>
<td>SHUTDOWN-LP</td>
<td>SHUTDOWN</td>
<td>ACTIVE</td>
<td>SLEEP</td>
</tr>
<tr>
<td rowspan=15 colspan=1>VSYS</td>
<td>BUCK/LDO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
</tr>
<tr>
<td>SWITCH</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
</tr>
<tr>
<td>BCHG</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
</tr>
<tr>
<td>MTP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>AONLDO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>BG</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>VSYS DET</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>VREF</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>IREF</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>SOSC</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>FOSC</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>ADC</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
</tr>
<tr>
<td>TS</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>OT-P</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>KEY</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td rowspan=2 colspan=1>VSYS/<br/>VBAT<br/> </td>
<td>XTAL</td>
<td>-</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
</tr>
<tr>
<td>RTC</td>
<td>-</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
<td>x(if enable)</td>
</tr>
<tr>
<td>VSYS</td>
<td>DIGITAL</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td rowspan=3 colspan=1>AONLDO</td>
<td>GPIO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>INT</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>IIC</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>x</td>
<td>x</td>
</tr>
</tbody>
</table>

### 5.3 PMIC 相关事件及行为

表 6-5 为 PMIC 事件汇总，行为中的‘强制’行为是指 PMIC 会从当前状态立即强制切换到关机模式。

表 6-5 PMIC 事件汇总

<table>
<tbody>
<tr>
<td>类型</td>
<td>事件</td>
<td>作用区间</td>
<td>行为</td>
</tr>
<tr>
<td rowspan=5 colspan=1>开机事件<br/></td>
<td>VSYS超阈值</td>
<td rowspan=5 colspan=1>关机模式</td>
<td rowspan=5 colspan=1>开机唤醒</td>
</tr>
<tr>
<td>PWRKY开机</td>
</tr>
<tr>
<td>INT下拉16ms</td>
</tr>
<tr>
<td>ALARM/TICK</td>
</tr>
<tr>
<td>PWRCTRL全绑定开机</td>
</tr>
<tr>
<td rowspan=6 colspan=1>关机事件</td>
<td>PWRKY关机</td>
<td rowspan=4 colspan=1>小节5.2内图的 * 状态，# 状态</td>
<td rowspan=5 colspan=1>按配置关机</td>
</tr>
<tr>
<td>VSYS低阈值</td>
</tr>
<tr>
<td>PWRCTRL关机</td>
</tr>
<tr>
<td>电源轨异常</td>
</tr>
<tr>
<td>软件关机</td>
<td>小节5.2内图的 # 状态</td>
</tr>
<tr>
<td>芯片过温/VSYS过压</td>
<td>ALL</td>
<td>强制关机</td>
</tr>
<tr>
<td rowspan=2 colspan=1>睡眠事件</td>
<td>软件睡眠</td>
<td>开机模式</td>
<td rowspan=2 colspan=1>按配置进入睡眠</td>
</tr>
<tr>
<td>GPIO睡眠</td>
<td>开机模式</td>
</tr>
<tr>
<td rowspan=4 colspan=1>唤醒事件</td>
<td>软件唤醒</td>
<td>睡眠模式</td>
<td rowspan=4 colspan=1>按配置退出睡眠</td>
</tr>
<tr>
<td>GPIO唤醒</td>
<td>睡眠模式</td>
</tr>
<tr>
<td>PWRKY中断唤醒</td>
<td>睡眠模式</td>
</tr>
<tr>
<td>ALARM/TICK</td>
<td>睡眠模式</td>
</tr>
<tr>
<td rowspan=5 colspan=1>复位事件</td>
<td>PWRKY复位</td>
<td>ALL</td>
<td>强制冷复位</td>
</tr>
<tr>
<td>软件复位</td>
<td>小节5.2内图的 # 状态</td>
<td rowspan=4 colspan=1>按配置复位</td>
</tr>
<tr>
<td>nRESET无效</td>
<td rowspan=3 colspan=1>小节5.2内图的 * 状态，# 状态<br/></td>
</tr>
<tr>
<td>PGOOD拉低</td>
</tr>
<tr>
<td>看门狗超时</td>
</tr>
</tbody>
</table>

### 5.4 序列控制器

PMIC 电源轨（除了 AONLDO）的开机、关机、睡眠、唤醒流程都由一个可编程的序列控制器控制，该序列控制器包含了 **16** 个可编程的 SLOT，特性如下：

1. **电源轨控制**

   - 每个电源轨绑定一个 **SLOT ID**（可指向 16 个 SLOT 中的任意一个）
   - 电源轨开关受 **PWRCTRL** 控制（配置寄存器：
     - BUCK：表 7-75 BUCKx\_CTRL[5:3]
     - ALDO：表 7-80 ALDOx\_CTRL[3:1]
     - DLDO：表 7-83 DLDOx\_CTRL[3:1]
   - 进入 SLOT 后需等待 PWRCTRL 有效才能打开对应 BUCK 和 LDO 使能，或者等到 PWRCTRL 无效才关闭或调整对应 BUCK 和 LDO 电压。
2. **EXT\_EN 控制**

   - GPIO0~5 可配置为 **EXT\_EN** 输出功能
   - 每个 EXT\_EN 绑定独立 **SLOT ID**（配置寄存器：表 7-102 PWR\_SLOT9~表 7-104 PWR\_SLOT11）
3. **SLOT 计时规则**

   - 若电源轨受 PWRCTRL 控制，其 SLOT 计时需等待**所有绑定的 PWRCTRL 信号达到目标状态**（全部有效/无效）

序列控制器的 SLOT0~SLOT14 为有效控制序列，SLOT15 为无效控制序列：

- 在开机流程或唤醒流程中，

  - SLOT0~SLOT14 阶段相应的 BUCK 和 LDO 使能打开，并且 EXT\_EN 变有效，指向 SLOT15 的电源轨和 EXT\_EN 并不使能或变有效。
- 在睡眠过程中，

  - SLOT0~SLOT15 阶段相应的 BUCK 和 LDO 使能保持当前状态不变，但当电源轨的睡眠电压设置成 0，睡眠过程中相应电源轨使能关闭；
  - 当 EXT\_EN 配置为受睡眠时序控制（**表 7-106 **PWR\_EXT\_CTRL[5:0]），则在睡眠过程中 EXT\_EN 变无效，否则保持当前状态不变。
- 在关机流程中，

  - SLOT0~SLOT15 各阶段对应的 BUCK 和 LDO 使能关闭，EXT\_EN 变无效。

**控制规模**

- 最大支持 **23 个 SLOT ID**（6 个 EXT\_EN + 6 个 BUCK + 11 个 LDO）
- 典型应用示例：DLDO1/DLDO4 绑定至特定 PWRCTRL（见下图 序列控制器时序控制示意图）

![](static/B0DdbO3J4o7ua5xe5c9cd4JQnNh.png)

下表罗列各模式和流程下电源轨状态和输出电压表

<table>
<tbody>
<tr>
<td>模式</td>
<td>SLOT_ID</td>
<td>PWRCTRLx</td>
<td>软件</td>
<td>电源轨状态</td>
<td>电源轨输出电压</td>
</tr>
<tr>
<td>关机模式</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>关闭</td>
<td>-</td>
</tr>
<tr>
<td>开机流程</td>
<td>x</td>
<td>x（option）</td>
<td>x</td>
<td>使能</td>
<td>Normal</td>
</tr>
<tr>
<td>开机模式</td>
<td>-</td>
<td>x（option）</td>
<td>x</td>
<td>使能</td>
<td>Normal</td>
</tr>
<tr>
<td>睡眠流程</td>
<td>x</td>
<td>x（option）</td>
<td>x</td>
<td>使能</td>
<td>Normal –&gt;Sleep</td>
</tr>
<tr>
<td>睡眠模式</td>
<td>-</td>
<td>x（option）</td>
<td>x</td>
<td>使能</td>
<td>Sleep</td>
</tr>
<tr>
<td>唤醒流程</td>
<td>x</td>
<td>x（option）</td>
<td>x</td>
<td>使能</td>
<td>Sleep -&gt;Normal</td>
</tr>
<tr>
<td>关机流程</td>
<td>x</td>
<td>x（option）</td>
<td>-</td>
<td>关闭</td>
<td>-</td>
</tr>
</tbody>
</table>

#### 5.4.1 开机事件

PMIC 支持以下开机唤醒事件：

1. VSYS 超过开机阈值唤醒（可通过 MTP 屏蔽）
2. PWRKY 长按开机唤醒（常开）
3. INT 引脚下拉超 16ms 唤醒（可 MTP 屏蔽）
4. RTC 的 ALARM 和 TICK 事件唤醒（可 MTP 屏蔽）
5. PWRCTRL 全绑定开机事件唤醒（可 MTP 屏蔽）
6. 关机后的自动重启事件

> **触发条件**：除 VSYS 阈值事件外，其余事件均需 **VSYS 高于开机阈值**才会生效。

**唤醒要求**

- **VSYS 电压范围**：2.9V ~ 5.5V（需稳定）
- **开机阈值**：

  - 可通过 MTP 配置

PMIC 的开机阈值除了通过 MTP 配置外，硬件本身也会根据情况调整开机阈值，防止由于较弱供电导致的错误开关机流程，如下**图****（开机和关机阈值切换示意图）**所示。调整过程如下：

**开机阈值动态调整流程**

1. **初始状态**：

   - PMIC 复位释放后进入**关机模式**
   - 若 VSYS 事件未屏蔽，当 VSYS \> **默认开机阈值**时触发开机模式
2. **低电压保护机制**：

   - 若开机后 **16 秒内 VSYS \< 关机阈值**：
     - 执行关机流程并进入关机模式
     - **调整开机阈值**：
       - 若当前阈值未达最大值（3.6V），按 **0.1V/0.2V** 步进提升（由表 7-127 SYS\_CFG2[7]选择）
       - 若已达 3.6V，则**屏蔽 VSYS 开机事件**
3. **阈值恢复条件**：

   - 若开机后 **16 秒内 VSYS 持续正常**（即未低于关机阈值），阈值恢复为默认值
4. **功能关闭**：

   - 可通过置位表 7-127 SYS\_CFG2[6]禁用阈值调整

![](static/GNJUbF6SzooXCLxab3oc585PnAP.png)

#### 5.4.2 开机流程

**关机模式**下检测到**开机事件**时，按以下顺序执行开机流程：

1. 从 MTP **加载所需配置**，如各电源轨电压相关配置
2. 加载完配置后，PMIC 会启动一系列**开机前检测**，包括：

   - VSET 引脚状态
   - 异常事件（电源轨过压，欠压，短路和开路）
     检测完成并无异常发生时即启动**电源轨开机序列**；否则，立即回到关机模式。
3. 开机序列完成后，会经过一段**可编程控制的延时**（**表 7-92 **PWR\_SEQ\_TIME[5:4]），延时结束后，PMIC 主动释放 PGOOD 引脚：

   - 若配置为**无需等待 PGOOD 释放**（表 7-87 PWR\_CTRL1[3] = 0），则系统直接进入开机模式。
   - 若需**等待 PGOOD 释放**，则必须等 PGOOD 释放后才能进入开机模式。
   - 若 PGOOD 长时间未释放（表 7-87 PWR\_CTRL1[4]），PMIC 直接回到关机模式。

在进入开机模式前（见 6.2 小节**模式切换示意图**中带 \* 号的状态），若发生异常事件、关机或复位事件，PMIC 会立即终止开机流程并回到关机模式，等待下一次唤醒。

**SLOT 机制与电源轨控制**

- **电源轨管理**：所有 BUCK（BUCK1~6）、11 个 LDO 及所有 EXTx\_EN 具有各自独立的 SLOT ID，该 ID 由 MTP 配置决定。在关机模式下唤醒后，PMIC 从 MTP 读取相应配置。
- **SLOT 绑定**：多个电源轨或 EXTx\_EN 可绑定至同一 SLOT，即同一 SLOT 内的电源轨可同时打开。
- **DUMMY SLOT**：若某个 SLOT 未绑定任何电源轨或 EXT\_EN，则该 SLOT 被视为 DUMMY SLOT，序列控制器会跳过该 SLOT，仅持续一个内部慢时钟周期（约 32μs）。

**开机序列与 PWRCTRL 绑定情况**

开机过程中序列控制器从 SLOT0 开始，所有 SLOT 的计时是统一可编程的，有四个档位选择（**表 7-92 **PWR\_SEQ\_TIME[1:0]）。根据不同的 PWRCTRL 引脚绑定情况，有如下几种场景：

1. 假如 **SLOT0~14 无 PWRCTRL 绑定**

   - 进入该 SLOT 后，电源轨和 EXTx\_EN 会立即使能，并且立即开启并开始计时。
   - 计时完成后，进入下一个 SLOT。
2. 假如 **SLOT0~14 绑定了 PWRCTRL**，进入该 SLOT 后：

   - 其它无等待的电源轨和 EXTx\_EN 进入该 SLOT 后立即将其使能打开，但 SLOT 的计时不启动。
   - 对应 PWRCTRL 的电源轨在 PWRCTRL 有效后会直接使能。
   - 所有电源轨等待的 PWRCTRL 都有效后才开始计时，计时完成后即进入下一 SLOT。
   - 当计时未完成时，PWRCTRL 变无效，SLOT 计数停止并清零，对应 PWRCTRL 的电源轨关闭，直至所有 PWRCTRL 重新变有效后才开始重新计时并打开。
   - 当计时已完成并进入下一 SLOT 后，若 PWRCRTL 再变无效，则对应 PWRCTRL 的相关电源轨不再受影响。但进入开机模式时受 PWRCTRL 控制的电源轨会关闭，当 PWRCTRL 重新变有效时，相应电源轨重新打开。
3. 假如 SLOT15 绑定了 PWRCTRL，则进入该 SLOT 后：

   - 电源轨或 EXTx\_EN 使能不打开，即该 SLOT 下无操作。
   - 若电源轨绑定了 PWRCTRL，SLOT 计时也受 PWRCTRL 控制，即需等到 PWRCTRL 有效后才开始计时。

下图为**开机流程时序图**

![](static/T5TCbdx84oCR2rxAATncgOzonje.png)

#### 5.4.3 关机事件**类型**

PMIC 支持以下关机触发条件：

1. **硬件触发**

   - **PWRKY 长按关机**（PWR\_CTRL2[6]=0 时使能）
   - **VSYS 电压低于阈值**（硬件强制关机）
2. **软件触发**

   - **软件指令关机**（通过寄存器配置）
3. **电源管理事件**

   - **所有电源轨绑定的 PWRCTRL 均无效**（可 MTP 屏蔽）
4. **异常保护事件**（可软件/MTP 屏蔽）

   - 电源轨故障：**过压（OV）**、**欠压（UV）**、**短路（SC）**
   - **芯片过温**
   - **VSYS 过压**

#### 5.4.4 关机流程

**流程概述**

当 PMIC 在**开机模式**下触发**关机/复位事件**时，系统执行反向关机流程：

1. **时序控制**：

   - 从 **SLOT15** 开始，**反向执行**至 **SLOT0**
   - 各 SLOT 内行为逻辑与开机流程相同，但**触发条件及结果极性相反**（见图 6-4、图 6-7）
2. **异常中断处理**：

   - 若在**睡眠/唤醒过程**（图 6-3 标#状态）中触发关机事件：
     - 立即中断当前流程
     - 按 **PWR\_CTRL1[0]**（表 7-87）配置执行对应关机流程

反序走到某个 SLOT 时，与该 SLOT 绑定的电源轨关闭，EXT\_EN 变无效；当电源轨配置成等待 PWRCTRL（**表 7-88 **PWR\_CTRL2[4] = 1），则该 SLOT 的计时以及电源轨的关闭需等待 PWRCTRL 无效，若等待 PWRCTRL 超时（**表 7-88 **PWR\_CTRL2[5]），则启动 SLOT 计时并关闭相应电源轨。

**紧急事件处理**

- 触发条件（任一满足）：

  - **VSYS 过压**（表 7-113 PWRKY\_EVENT[5]）
  - **芯片过温**（表 7-109 EVENT2[6]）
- 响应动作：

  - 若使能保护（IRQ\_PWRKY\_EN[7:6]=1），**立即跳转至关机模式**
  - **强制关闭所有电源轨与 EXT\_EN**

关机流程时序图如下图所示

![](static/DvpJbqt17o1b6wxx4qIcpjiCn3e.png)

#### 5.4.5 睡眠事件

**图 6-3** 的睡眠事件即开机模式下进入睡眠模式的条件：

1. 软件进入睡眠（**表 7-88 **PWR\_CTRL2[0] = 1）
2. GPIO 复用输入功能（Sleep/Wake up）引脚有效事件

#### 5.4.6 睡眠流程

从开机模式进入睡眠模式的时序与开机流程时序一致，但具体行为不同。以下是睡眠流程的关键点：

1. **电源轨调节**
   各电源轨的使能状态保持不变。如果睡眠电压设置为 0，则电源轨会关闭；否则，电源轨会将其电压调节到设定的睡眠电压。
2. **EXT\_EN 控制**
   EXT\_EN 的状态仅受表 7-104（PWR\_EXT\_EN）和表 7-106（PWR\_EXT\_CTRL）的控制。只有当 EXTx\_SLP\_SD 设置为 1 时，EXT\_EN 才会在对应的 SLOT 阶段关闭；否则，EXT\_EN 保持不变。
3. **唤醒事件处理**
   在睡眠流程中，唤醒事件不会中断睡眠过程。如果进入睡眠模式后，唤醒条件仍然成立，则会启动唤醒流程。

   - 软件和 GPIO 引脚触发的睡眠条件采用电平方式，并仅在开机模式下生效。
4. **多 GPIO 配置**
   当多个 GPIO 被配置为 SLEEP/WKUP 引脚时，在开机模式下，只要任一引脚有效，系统就会进入睡眠流程。

#### 5.4.7 唤醒事件

如小节 5.2 图的唤醒事件即睡眠模式下退出的条件：

1. 软件唤醒
2. GPIO 复用输入功能（Sleep/Wake up）引脚无效事件
3. PWRKY 中断唤醒（短按/长按/上升/下降沿中断）
4. RTC ALARM 和 TICK（可 MTP 屏蔽）

#### 5.4.8 唤醒流程

从睡眠模式唤醒的行为与开机流程一致，但存在以下区别：

1. **电源轨电压调节**
   在唤醒流程中，电源轨的电压会从睡眠电压调节到正常电压。
2. **软件关闭的电源轨状态**
   如果在睡眠模式下，用户通过软件关闭了某电源轨，则进入唤醒流程时，该电源轨保持关闭状态。
3. **睡眠事件处理**
   在唤醒流程中，若遇到睡眠事件，不会中断当前流程。若进入开机模式后睡眠条件仍成立，则启动睡眠流程。
4. **软件触发条件清除**
   若通过软件进入睡眠，但通过其他方式退出睡眠，则其他唤醒源会清除软件触发条件，即清零相关寄存器。
5. **多 GPIO 配置要求**
   当多个 GPIO 被配置为 SLEEP/WKUP 引脚时，在睡眠模式下需所有 SLEEP/WKUP 引脚均无效，才能进入唤醒流程。
6. **特定唤醒源限制**
   若任一 SLEEP/WKUP 引脚有效，则 PWRKY 中断唤醒相关事件，RTC ALARM 和 TICK 事件无法唤醒 PMIC。

#### 5.4.9 复位事件

复位事件如下：

1. PWRKY 长按 12s 冷复位事件（**表 7-88 **`PWR_CTRL2[6]` = 1）
2. PWRKY 长按关机后自动重启（**表 7-88 **`PWR_CTRL2[6]` = 0 且**表 7-87 **`PWR_CTRL1[2]` = 1）
3. 软件复位事件
4. nRESET（GPIO 复用输入功能）无效事件（可软件屏蔽）
5. PGOOD 拉低（可软件或 MTP 屏蔽）
6. 看门狗超时复位事件（可软件屏蔽）

#### 5.4.10 复位流程

在开机模式和睡眠模式下，复位事件的行为一致，并根据配置执行下一步操作。所有复位流程均需经过关机流程。

1. **关机模式停留时间**
   经过关机流程进入关机模式后，PMIC 会在关机模式下停留一段时间（由表 7-88 PWR\_CTRL2[7] 配置），以确保足够的复位时间。计时完成后有两种可能的结果：
   - **进入 RESET 模式**
     当 PWRKY 按键配置为长按 12 秒复位且发生按键长按事件时，PMIC 将复位所有逻辑并进入 RESET 模式（如下图 **图复位流程** 所示）。

![](static/Kn0rb2ftHoLXCix6icrcFvAQnQe.png)

- **进入 MTP READ2 模式**
  对于其他复位事件，PMIC 将退出关机模式并进入 MTP READ2 模式（如下图 **冷复位流程** 所示）。

![](static/TT2rbFovKoUyN3xeGYhcEcH4nsh.png)

1. **复位源屏蔽行为**
   在复位源触发进入关机模式的 SD\_RST\_TIME 期间，所有开机源将被屏蔽，即开机源无效。

### 5.5 LDO

PMIC 内部集成了三种 LDO：**AONLDO**，**ALDO1~4** 和 **DLDO1~7**，其相关控制如下表所示：

表 6-7 LDO 控制参数

<table>
<tbody>
<tr>
<td>电源轨</td>
<td>Sequencer</td>
<td>PWRCTRL</td>
<td>软件</td>
<td>DVS</td>
<td>STEP</td>
<td>SLEEP Voltage</td>
</tr>
<tr>
<td>AONLDO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>25 mV</td>
<td>-</td>
</tr>
<tr>
<td>ALDO1~4</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>-</td>
<td>25 mV</td>
<td>x</td>
</tr>
<tr>
<td>DLDO1~7</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>-</td>
<td>25 mV</td>
<td>x</td>
</tr>
</tbody>
</table>

- **LDO 使能与电压调节**

  - **AONLDO**
    - 在 VSYS 上电（VSYS \> 2.7 V）后保持常开。
    - 无睡眠电压设置。
  - **ALDO1~4 和 DLDO1~7**
    - 使能和电压调节可通过软件修改（主机通过 IIC 访问 PMIC 内部寄存器）。
    - 所有 LDO 的电压调节步幅为 25 mV。
    - 支持两种电压配置：开机模式和睡眠模式下的电压。
- **硬件控制**
  ALDO1~4 和 DLDO1~7 可受以下硬件控制：

  - **序列控制器（Sequencer）**
    - 通过表 7-96（PWR\_SLOT3）至表 7-101（PWR\_SLOT8）配置 LDO 在 Sequencer 中的位置，以控制 LDO 的开启或关闭时序。
  - **PWRCTRL（GPIO 复用输入功能）**
    - 通过表 7-80（ALDOx\_CTRL[3:1]）和表 7-83（DLDOx\_CTRL[3:1]）配置，决定 LDO 是否受 PWRCTRL 信号控制。
    - 当 Sequencer 到达对应 SLOT 且绑定的 PWRCTRL 信号有效或无效时，对应 LDO 使能或关闭
- **下拉电阻控制**
  所有 LDO 输出端均有一个下拉电阻。

  - 当 LDO 使能打开时，下拉电阻关闭。
  - 当 LDO 关闭时，下拉电阻是否打开取决于 LDO\_PD\_DIS（详见寄存器描述）。

### 5.6 BUCK

PMIC 内部有 6 个 BUCK，其相关控制如下表所示：

表 6-8 BUCK 控制参数

<table>
<tbody>
<tr>
<td>电源轨</td>
<td>Sequencer</td>
<td>PWRCTRL</td>
<td>软件</td>
<td>DVS</td>
<td>STEP</td>
<td>SLEEP Voltage</td>
<td>软启</td>
<td>VSET</td>
<td>DUAL</td>
</tr>
<tr>
<td>BUCK1~2</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>5/25 mV</td>
<td>x</td>
<td>x</td>
<td>-</td>
<td>x</td>
</tr>
<tr>
<td>BUCK3~4</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>5/25 mV</td>
<td>x</td>
<td>x</td>
<td>-</td>
<td>x</td>
</tr>
<tr>
<td>BUCK5</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>5/25 mV</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>-</td>
</tr>
<tr>
<td>BUCK6</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>5/25 mV</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>-</td>
</tr>
</tbody>
</table>

- **软启动特性**
  所有 BUCK 在启动时均具备软启动功能，软启动时间为 1ms。
- **动态电压调节（DVS）**

  - 当 BUCK 使能且启用了 DVS 功能时，电压会按照设定的步幅（表 7-74 BUCK\_LDO\_CFG[4:3]）动态调节，直至达到目标电压。
  - **触发 DVS 的情况**：
    - 在开机模式下修改表 7-76（BUCKx\_VOLT）。
    - 在睡眠模式下修改表 7-77（BUCKx\_SLP\_VOLT）。
    - 在睡眠流程和唤醒流程中，由序列控制器切换电压。
- **双相模式配置**
  BUCK1 和 BUCK2、BUCK3 和 BUCK4 可配置为双相模式，以满足不同应用场景的需求。
- **下拉电阻控制**
  所有 BUCK 输出端均有一个下拉电阻。

  - 当 BUCK 使能打开时，下拉电阻关闭。
  - 当 BUCK 关闭时，下拉电阻是否打开取决于表 7-74（BUCK\_LDO\_CFG[6]）的配置
- **BUCK5 和 BUCK6 的特殊配置**

  - BUCK5 和 BUCK6 分别具有 VSET5 和 VSET6 引脚。
  - VSET5 和 VSET6 引脚的状态与 BUCK\_VSET\_CTRL 寄存器共同决定了这两个 BUCK 的输出电压状态。具体细节请参见相关寄存器描述和 VSET5/VSET6 引脚说明。

### 5.7 关机保护

PMIC 有以下保护操作：

1. 所有电源轨（BUCK 和 LDO）的过压，欠压，短路和开路保护。
2. 芯片过温保护；VSYS 过压保护；Switch 短路保护。

#### 5.7.1 电源轨异常保护

当使能电源轨的关机保护操作（表 7-121 PROT\_EN[5:0]）时，若任一电源轨发生异常，将触发关机流程。以下是电源轨异常保护的详细配置：

1. **欠压和过压检测事件**

   - **滤波时间配置**
     滤波时间通过 OVUV\_DELAY 配置，可选择以下选项：
     - 100 μs
     - 375 μs
     - 750 μs
     - 屏蔽滤波（表 7-127 SYS\_CFG2[4:3]）
   - **屏蔽时间配置**
     在某些特定时间范围内，PMIC 内部检测电路可能会产生异常的过压或欠压事件。如果不希望这些异常事件导致关机或中断，可通过设置屏蔽时间来屏蔽这些事件：
     - **特定时间范围**：
       - 电源轨开启后至其稳定阶段。
       - 电源轨电压改变阶段。
     - **屏蔽时间设置**：通过表 7-127 SYS\_CFG2[2:0] 配置。
2. **异常保护机制**

- 当检测到电源轨异常时，PMIC 会根据配置执行关机流程。
- 滤波时间和屏蔽时间的设置可以帮助用户根据实际需求灵活调整异常保护机制，以确保系统的稳定性和可靠性。

#### 5.7.2 其它异常保护

VSYS 过压保护，芯片过温保护和 Switch 短路保护分别有单独的使能位：**表 7-120 **IRQ\_PWRKY\_EN[7:6]，**表 7-121 **PROT\_EN[7:6]。

上述所有事件可通过寄存器**表 7-127 **SYS\_CFG2[5]设置滤波时间：100 us/屏蔽滤波功能。

过温保护的档位如下：

**表 6-9 过温保护档位及其行为**

<table>
<tbody>
<tr>
<td>表 7125 SYS_CFG0[7]</td>
<td>温度报警（warning）/ ℃</td>
<td>严重过温（severe）/ ℃</td>
<td>关机过温（critical）/ ℃</td>
</tr>
<tr>
<td>0</td>
<td>95</td>
<td>115</td>
<td>135</td>
</tr>
<tr>
<td>1</td>
<td>110</td>
<td>130</td>
<td>150</td>
</tr>
<tr>
<td>事件</td>
<td>表 7109 EVENT2[4]</td>
<td>表 7109 EVENT2[5]</td>
<td>表 7109 EVENT2[6]</td>
</tr>
<tr>
<td>使能</td>
<td>-</td>
<td>表 7121 PROT_EN[6]</td>
<td>表 7120 IRQ_PWRKY_EN[6]</td>
</tr>
<tr>
<td>行为</td>
<td>中断</td>
<td>关机</td>
<td>关机</td>
</tr>
</tbody>
</table>

### 5.8 负载开关

PMIC 内部的负载开关（SWITCH）受软件控制，其行为如下：

1. **下拉电阻控制**
   SWITCH 输出端有一个下拉电阻。

- 当 SWITCH 使能打开时，下拉电阻关闭。
- 当 SWITCH 关闭时，下拉电阻是否打开取决于表 7-78（SWITCH\_CTRL[1]）的配置。

2. **关机模式行为**

- 在关机模式下，SWITCH 不工作。

### 5.9 电池充电

主机配置好充电电压和充电电流，并打开使能（**表 7-73 **BBAT\_CTRL[0]=1）后，可给电池充电，行为如下：

1. 当电池充满电后，PMIC 内部计时 20 ms 后停止充电。
2. 当电池电压低于设定值时，PMIC 重新开始给电池充电，直至充满，重复步骤 1。
3. 充电使能关闭后（BCHG\_EN=0），充电即停止。

在关机模式下，电池充电电路关闭使能，重新进入开机模式后需重新配置使能。

## 6. 系统控制与接口功能

本章介绍 P1 PMIC 的系统级功能，涵盖通信接口（I²C/GPIO）、安全监控（看门狗/ADC）和实时时钟（RTC）等模块，实现与外部系统的无缝协同。

### 6.1 看门狗

在开机模式和睡眠模式下，主机可通过 IIC 通信接口使能看门狗并配置超时时间（**表 7-72 **WDT\_CTRL[2:1]）。

如果在设定超时时间内主机未进行喂狗操作（**表 7-72 **WDT\_CTRL[0]=1），则产生看门狗超时事件并置起相关标志位（**表 7-108 **EVENT1[3]）。

假如看门狗超时复位使能（**表 7-86 **PWR\_CTRL0[7]），则触发 PMIC 的复位流程。

假如看门狗中断使能打开（**表 7-115 **IRQ\_EN1[3]），则产生看门狗中断并拉低 INT 引脚。

看门狗进入关机模式后关闭使能并停止工作，重新进入开机模式需再次配置看门狗使能。

### 6.2 GPIO

PMIC 总共有 6 个 GPIO，既可作为通用 IO，也可配置成复用输入或输出功能，详见寄存器**表 7-12 **GPIO\_MODE0 ~ **表 7-13 **GPIO\_MODE1 和** 表 7-14 **GPIO\_AF01 ~ **表 7-16 **GPIO\_AF45。GPIO 其它特性如下：

1. 除了作为复用 ADC 输入功能外，GPIO 的极性、上下拉、开漏和滤波功能都有效。
2. 其中 GPIO 滤波时间为 100 us ~ 1.5 ms（**表 7-8 **GPIO\_DEB\_EN[7:6]），并且 GPIOx\_IDR 都可反映当前端口状态。
3. 作为 GPIO 输入功能时，**表 7-4 **GPIO\_IDR 和** 表 7-10 **GPIO\_ITYPE0，**表 7-11 **GPIO\_ITYPE1 相互配合可产生** 表 7-107 **EVENT0[5:0]事件。

GPIOx\_ODR 复用两种功能：

1. 作为 GPIO 输出时（GPIOx\_MODE=2’b01），GPIOx\_ODR 即为 GPIO 输出状态。
2. 作为复用功能时（GPIOx\_MODE=2’b1x），GPIOx\_ODR 即为相关复用功能的有效状态配置位。

### 6.3 IIC 通信接口

PMIC 的通信接口为 IIC，最大支持速度为 1MHz，此 PMIC 只作为从机使用。

在关机模式下 SCL 和 SDA 接口不工作，只有进入开机模式和睡眠模式后主机才能通过 IIC 接口操作 PMIC 寄存器。该 IIC 从机地址可通过 MTP 配置：**表 7-125 **SYS\_CFG0[6:0]。

### 6.4 ADC 控制电路

功能简介：

1. 12bit ADC，采样速率 100 Hz ~ 50 KHz，寄存器可配
2. 6 路外部扫描通道和 20 路内部扫描通道选择
3. ADC 参考电压寄存器可配置
4. 支持手动和自动扫描模式
5. 手动模式测量通道寄存器可配置，最多可测量 6 路外部扫描通道和 20 路内部扫描通道
6. 自动模式测量通道寄存器可配置，最多可测量 1 路内部通道（芯片结温 Tj）和 6 路外部扫描通道（6 路 GPIO 配置成 ADC 扫描输入模式），即 7 路自动扫描通道
7. 7 路独立的自动通道结果寄存器和一路复用手动通道结果寄存器
8. 7 路独立的自动扫描通道监控，高阈值和低阈值分别可配
9. 7 路自动扫描通道的高/低阈值标志位各自具备滤波功能（连续触发 ADC\_DEB\_NUM 次数后即置起）
10. 可屏蔽的 ADC 单次转换完成中断、序列转换完成中断、阈值比较中断

#### 6.4.1 通道选择

ADC 模块工作示意图如下图所示

![](static/ASrNbFEj9o2VABx3wLhc9ptmnMG.png)

ADC 各测量通道如下：

1. 通道 0：可选择测量 VSYS 电压，所有 BUCK 的电压和所有 LDO 电压；每路寄存器单独可配置；VSYS 电压是把 VSYS/4 作为 ADC 的输入并选用内部基准来测量
2. 通道 1：V(TJ)，芯片内部 Junction 温度
3. 通道 2：ADCIN0，GPIO0 配置成 ADC 模拟输入复用功能
4. 通道 3：ADCIN1，GPIO1 配置成 ADC 模拟输入复用功能
5. 通道 4：ADCIN2，GPIO2 配置成 ADC 模拟输入复用功能
6. 通道 5：ADCIN3，GPIO3 配置成 ADC 模拟输入复用功能
7. 通道 6：ADCIN4，GPIO4 配置成 ADC 模拟输入复用功能
8. 通道 7：ADCIN5，GPIO5 配置成 ADC 模拟输入复用功能

#### 6.4.2 手动模式

手动模式配置流程：

1. 复位 ADC\_AUTO 寄存器，禁止所有自动扫描通道使能，并使能 ADC（**表 7-34 **ADC\_CTRL[0]=1）。
2. 选择 ADC 转换通道，即配置**表 7-36 **ADC\_CFG1 [5:3]。
3. 若选择通道 0，则需选择通道 0 的手动通道，即**表 7-39 **ADC\_MAN\_EN0 ~ **表 7-41 **ADC\_MAN\_EN2。
4. 配置其它所需配置，如 ADC 结果滤波，采样频率，CHOP 功能，参考电压，和 ADC 各通道阈值等。
5. 置位 ADC\_GO 启动一次转换。

首次使能 ADC，其需要约\> 30 us 的稳定时间，ADC 稳定后 ADC 内部才真正开始工作。

手动模式下每完成一次转换：

1. 扫描通道 0 时 12 bit 结果存放在**表 7-42** ADC\_MAN\_RES\_H 和**表 7-43** ADC\_MAN\_RES\_L 里面；
2. 扫描其它通道时，12bit 结果放在对应的结果寄存器里（**表** **7-44** ADC\_TJ\_RES\_H ~ **表 7-57 **ADC\_IN5\_RES\_L）
3. ADC\_GO 被硬件清零
4. ADC 单次转换完成事件**表 7-108 **EVENT1[1]会被置位
5. 如果使能了中断（**表 7-115 **IRQ\_EN1[1]），会产生一个中断事件（拉低 INT 引脚）直至软件清除该事件或清零中断使能位。

手动模式下如果选择了通道 0：

1. 在配置完对应的通道使能后，每完成一次转换，ADC 内部通道选择自动切换到通道 0 下一次使能的通道，完成一轮扫描后，切换到最开始使能的通道，如下图** ADC 通道 0 扫描示意图 **所示。
2. 当需要切换扫描顺序，在下一次转换启动前配置好对应的通道使能即可
3. 如需要从头开始扫描，有两种方法：

   - ADC\_EN 关闭再打开；
   - 先切换自动模式，再切回手动模式：ADC\_AUTO 内任意寄存器配置成 1，然后再将其全清零。
4. **表 7-39 **ADC\_MAN\_EN0 ~ **表 7-41 **ADC\_MAN\_EN2 使能的通道全被扫描并转换完成后，会产生事件** 表 7-108 **EVENT1[2]，如果使能了中断（**表 7-115 **IRQ\_EN1[2]），会产生一个中断事件（拉低 INT 引脚）直至软件清除该事件或清零中断使能位。

> **注意****:** 通道转换过程中不可随意更改配置，如改变通道选择，采样频率和 ADC\_AUTO 等，否则不保证转换结果的正确性；若转换过程中软件清零 ADC\_GO，将会打断当前转换，结果不保存和更新，通道扫描从头开始。

![](static/EaBCbpxDKoe0YFx1T5wcebDXnad.png)

#### 6.4.3 自动模式

自动模式配置流程：

1. 配置所需自动扫描通道，ADC\_AUTO 对应的通道使能，并使能 ADC（**表 7-34 **ADC\_CTRL[0]=1）。
2. 配置好其它所需配置，如 ADC 结果滤波，采样频率，CHOP 功能，参考电压，高速模式和 ADC 各通道阈值等。
3. 置位 ADC\_GO 启动转换。

首次使能 ADC，其需要约\> 30 us 的稳定时间，ADC 稳定后 ADC 内部才真正开始工作。

自动模式下每完成一次转换：

1. 12bit 结果会存放在对应的结果寄存器里。
2. ADC\_GO 在自动扫描模式下不被清零。
3. ADC 单次转换完成事件**表 7-108 **EVENT1[1]会被置位。
4. 如果使能了中断（**表 7-115 **IRQ\_EN1[1]），会产生一个中断事件（拉低 INT 引脚）直至软件清除该事件或清零中断使能位。

每完成一个序列的扫描（ADC\_AUTO 使能的通道都被扫描完成），序列转换完成事件**表 7-108 **EVENT1[2]会被置位，如果使能了中断（**表 7-115 **IRQ\_EN1[2]），会产生一个中断事件（拉低 INT 引脚）直至软件清除该事件或清零中断使能位。

在配置完对应的通道使能后，每完成一次转换，ADC 内部通道选择自动切换到下一次使能的通道，完成一轮扫描后，切换到最开始使能的通道，如下图 **ADC 自动扫描示意图** 所示。

![](static/SVmFbhfUEoKnR1xVm5Zcy3LQnQu.png)

当需要切换扫描顺序或从头开始扫描，有两种方法：

1. ADC\_EN 关闭后重新按照自动模式配置流程重新配置，
2. 软件清零 ADC\_GO，当前转换将被打断，结果不保存和更新，下一次置位 ADC\_GO 后通道扫描从头开始。

注意，通道转换过程中不可随意更改配置，如改变通道选择，采样频率和 ADC\_AUTO 等，否则不保证转换结果的正确性。

#### 6.4.4 ADC 结果滤波

如果配置了通道 1~7 的阈值：

1. 在未开启结果滤波时（**表 7-35 **ADC\_CFG0 对应 bit 为 0），当本次转换结果超过或低于所设阈值，相应通道的事件（**表 7-107 **EVENT0[5:0]，**表 7-108 **EVENT1[0]）标志位将被置起。
2. 当开启了结果滤波时，只有连续遇到超阈值事件或低阈值事件达到**表 7-37 **ADC\_CFG2[6:4]设置的次数后才会置起相应标志位。

如果使能了对应的中断，会产生一个中断事件（拉低 INT 引脚）直至软件清除该事件或清零中断使能位。

下图为 **ADC 结果滤波示意图**

![](static/P1kvbSkWNof1hLx61SocDgBNn5d.png)

### 6.5 RTC 模块

RTC 模块有三个功能：

- 日历
- 闹钟
- 秒计数

RTC 供电由 2 个来源：VSYS 和 备用纽扣电池

- 当 VSYS 接入时，RTC 供电为 VSYS
- 当 VSYS 低于 2.0 V 时内部电路才会切换到纽扣电池供电

RTC 时钟源可选择内部慢时钟（LSI）或外部晶振，详见寄存器**表 7-33 **RTC\_CTRL[3]。

在开启上电流程前，可通过 MTP 使能寄存器**表 7-33 **RTC\_CTRL[1]输出内部慢时钟或者晶振时钟。

#### 6.5.1 RTC 日历

RTC 模块内部计时逻辑通过计数 32 kHz 时钟，分别提供秒，分，时，日，月和年，见寄存器**表 7-17 **RTC\_COUNT\_S ~ **表 7-22 **RTC\_COUNT\_Y。RTC\_COUNT\_Y=0 对应 2000 年，因此可计时的日历时间最高可至 2063 年。如需读取当前 PMIC 内部记录的日历值，则需先读 RTC\_COUNT\_S，与此同时该操作会锁存当前所有日历值分别至寄存器 RTC\_COUNT\_S ~ RTC\_COUNT\_Y。

如需要重新设置当前日历值，则需按顺序配置好各日历值（RTC\_COUNT\_S ~ RTC\_COUNT\_Y），最后写完寄存器 RTC\_COUNT\_Y 后，PMIC 会将当前用户配置好的日历值更新到 RTC 模块内部计时器当中，依此为基础开始新的计时。

#### 6.5.2 RTC 闹钟

RTC 模块提供**表 7-23 **RTC\_ALARM\_S ~ **表 7-28 **RTC\_ALARM\_Y 的闹钟值，当 RTC 内部当前日历值与 RTC\_ALARM\_S ~ RTC\_ALARM\_Y 都匹配时：

1. 若**表 7-33 **RTC\_CTRL[5]=1，此时产生一个闹钟事件** 表 7-108 **EVENT1[4]，如果**表 7-115 **IRQ\_EN1[4]=1，则也会产生一个中断，拉低 INT 引脚，直至主机清零 E\_ALARM 或 IRQ\_EN\_ALARM。
2. 若**表 7-33 **RTC\_CTRL[6]=1，此时产生一个 TICK 事件** 表 7-108 **EVENT1[5]，如果**表 7-115 **IRQ\_EN1[5] =1，则也会产生一个中断，拉低 INT 引脚，直至主机清零 E\_TICK 或 IRQ\_EN\_TICK。

TICK 的产生是周期性的，触发后可配置成 1s 或 1min（**表 7-33 **RTC\_CTRL[4]）周期内触发一次，因此当 TICK 事件触发后，主机只清零标志位（E\_TICK）并不会关闭周期性的触发事件，只有 TICK\_EN=0 才能关闭此周期性触发的事件。

当前日历值和设定闹钟值匹配还可以屏蔽对应的日历单位，以实现固定时间段产生闹钟和 TICK 事件：

1. MASK\_ALARM\_Y ~ MASK\_ALARM\_S 分别对应年月日时分秒屏蔽位。
2. 对应 bit 置 1 则屏蔽相应 RTC\_ALARM\_Y ~ RTC\_ALARM\_S 与当前日历值的匹配。

在关机模式下，RTC 闹钟和 TICK 事件都可作为开机源。

在睡眠模式下，RTC 闹钟和 TICK 事件都可作为唤醒源。

#### 6.5.3 秒计数

**表 7-29 **RTC\_SECOND\_A ~ **表 7-32 **RTC\_SECOND\_D 组成一个 32bit 秒计数器，RTC\_EN=1 后，秒计数开始计时，否则秒计数清零。

## 7. 寄存器

### 7.1 **表 7-1 **寄存器参数定义

表 7-1 Register Base Attributes

<table>
<tbody>
<tr>
<td>参数</td>
<td>简称</td>
<td>描述</td>
</tr>
<tr>
<td>Read Only</td>
<td>R</td>
<td>该bit可通过软件读，写无效。</td>
</tr>
<tr>
<td>Read/Write</td>
<td>RW</td>
<td>该bit可通过软件读写</td>
</tr>
<tr>
<td>Write Only</td>
<td>W</td>
<td>该bit只能软件写</td>
</tr>
<tr>
<td>Reserved</td>
<td>RV</td>
<td>该bit为保留位，软件不可修改。</td>
</tr>
</tbody>
</table>

## 7.2 **表 7-2 **寄存器特殊的参数定义

表 7-2 Register Attribute Modifier

<table>
<tbody>
<tr>
<td>参数</td>
<td>简称</td>
<td>描述</td>
</tr>
<tr>
<td>Write 1 Only</td>
<td>IO</td>
<td>该bit只能通过软件写1，写0无效。</td>
</tr>
<tr>
<td>Protected</td>
<td>P</td>
<td>该bit受解锁寄存器表 7128 MTP_KEY保护。<br/>当未向解锁寄存器写解锁序列时，该bit不能通过软件修改。</td>
</tr>
<tr>
<td>MTP Loaded</td>
<td>E</td>
<td>该bit可通过MTP修改。</td>
</tr>
</tbody>
</table>

## 7.3 表 7-3 寄存器映射表

表 7-3 Register Map

<table>
<tbody>
<tr>
<td>Module</td>
<td>Table Name</td>
<td>Register Address(hex)</td>
<td>Attribute</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=13 colspan=1><strong>GPIO</strong></td>
<td>表 7-4</td>
<td>0x00</td>
<td>R</td>
<td>GPIO端口输入值</td>
</tr>
<tr>
<td>表 7-5</td>
<td>0x01</td>
<td>RW</td>
<td>GPIO数据输出；<br/>有效电平配置</td>
</tr>
<tr>
<td>表 7-6</td>
<td>0x02</td>
<td>RWE</td>
<td>GPIO0 ~ 2上下拉配置</td>
</tr>
<tr>
<td>表 7-7</td>
<td>0x03</td>
<td>RWE</td>
<td>GPIO3 ~ 5上下拉配置</td>
</tr>
<tr>
<td>表 7-8</td>
<td>0x04</td>
<td>RW</td>
<td>GPIO滤波使能及滤波时间配置</td>
</tr>
<tr>
<td>表 7-9</td>
<td>0x05</td>
<td>RW</td>
<td>GPIO输出开漏配置</td>
</tr>
<tr>
<td>表 7-10</td>
<td>0x06</td>
<td>RWE</td>
<td>GPIO0 ~ 2中断类型配置</td>
</tr>
<tr>
<td>表 7-11</td>
<td>0x07</td>
<td>RWE</td>
<td>GPIO3 ~ 5中断类型配置</td>
</tr>
<tr>
<td>表 7-12</td>
<td>0x08</td>
<td>RWE</td>
<td>GPIO0 ~ 2模式配置</td>
</tr>
<tr>
<td>表 7-13</td>
<td>0x09</td>
<td>RWE</td>
<td>GPIO3 ~ 5模式配置</td>
</tr>
<tr>
<td>表 7-14</td>
<td>0x0A</td>
<td>RWE</td>
<td>GPIO0 ~ 1复用功能选择</td>
</tr>
<tr>
<td>表 7-15</td>
<td>0x0B</td>
<td>RWE</td>
<td>GPIO2 ~ 3复用功能选择</td>
</tr>
<tr>
<td>表 7-16</td>
<td>0x0C</td>
<td>RWE</td>
<td>GPIO4 ~ 5复用功能选择</td>
</tr>
<tr>
<td rowspan=17 colspan=1><strong>RTC</strong></td>
<td>表 7-17</td>
<td>0x0D</td>
<td>RW</td>
<td>RTC seconds 读出寄存器</td>
</tr>
<tr>
<td>表 7-18</td>
<td>0x0E</td>
<td>RW</td>
<td>RTC minutes 读出寄存器</td>
</tr>
<tr>
<td>表 7-19</td>
<td>0x0F</td>
<td>RW</td>
<td>RTC hours 读出寄存器</td>
</tr>
<tr>
<td>表 7-20</td>
<td>0x10</td>
<td>RW</td>
<td>RTC days 读出寄存器</td>
</tr>
<tr>
<td>表 7-21</td>
<td>0x11</td>
<td>RW</td>
<td>RTC months 读出寄存器</td>
</tr>
<tr>
<td>表 7-22</td>
<td>0x12</td>
<td>RW</td>
<td>RTC years 读出寄存器</td>
</tr>
<tr>
<td>表 7-23</td>
<td>0x13</td>
<td>RW</td>
<td>RTC_ALARM seconds 设置</td>
</tr>
<tr>
<td>表 7-24</td>
<td>0x14</td>
<td>RW</td>
<td>RTC_ALARM minutes 设置</td>
</tr>
<tr>
<td>表 7-25</td>
<td>0x15</td>
<td>RW</td>
<td>RTC_ALARM hours 设置</td>
</tr>
<tr>
<td>表 7-26</td>
<td>0x16</td>
<td>RW</td>
<td>RTC_ALARM days 设置</td>
</tr>
<tr>
<td>表 7-27</td>
<td>0x17</td>
<td>RW</td>
<td>RTC_ALARM months 设置</td>
</tr>
<tr>
<td>表 7-28</td>
<td>0x18</td>
<td>RW</td>
<td>RTC_ALARM years 设置</td>
</tr>
<tr>
<td>表 7-29</td>
<td>0x19</td>
<td>R</td>
<td>RTC 秒计数[7:0]</td>
</tr>
<tr>
<td>表 7-30</td>
<td>0x1A</td>
<td>R</td>
<td>RTC 秒计数[15:8]</td>
</tr>
<tr>
<td>表 7-31</td>
<td>0x1B</td>
<td>R</td>
<td>RTC 秒计数[23:16]</td>
</tr>
<tr>
<td>表 7-32</td>
<td>0X1C</td>
<td>R</td>
<td>RTC 秒计数[31:24]</td>
</tr>
<tr>
<td>表 7-33</td>
<td>0x1D</td>
<td>RWE</td>
<td>RTC 控制寄存器</td>
</tr>
<tr>
<td rowspan=38 colspan=1><strong>ADC</strong></td>
<td>表 7-34</td>
<td>0x1E</td>
<td>RW</td>
<td>ADC控制寄存器</td>
</tr>
<tr>
<td>表 7-35</td>
<td>0x1F</td>
<td>RW</td>
<td>ADC配置寄存器0</td>
</tr>
<tr>
<td>表 7-36</td>
<td>0x20</td>
<td>RW</td>
<td>ADC配置寄存器1</td>
</tr>
<tr>
<td>表 7-37</td>
<td>0x21</td>
<td>RW</td>
<td>ADC配置寄存器2</td>
</tr>
<tr>
<td>表 7-38</td>
<td>0x22</td>
<td>RW</td>
<td>ADC自动模式扫描通道选择</td>
</tr>
<tr>
<td>表 7-39</td>
<td>0x23</td>
<td>RW</td>
<td>ADC通道0手动扫描通道选择</td>
</tr>
<tr>
<td>表 7-40</td>
<td>0x24</td>
<td>RW</td>
<td>ADC通道0手动扫描通道选择</td>
</tr>
<tr>
<td>表 7-41</td>
<td>0x25</td>
<td>RW</td>
<td>ADC通道0手动扫描通道选择</td>
</tr>
<tr>
<td>表 7-42</td>
<td>0x26</td>
<td>R</td>
<td>ADC通道0转换结果高8位</td>
</tr>
<tr>
<td>表 7-43</td>
<td>0x27</td>
<td>R</td>
<td>ADC通道0转换结果低4位</td>
</tr>
<tr>
<td>表 7-44</td>
<td>0x28</td>
<td>R</td>
<td>Junction温度监控自动转换结果（8 MSBs）</td>
</tr>
<tr>
<td>表 7-45</td>
<td>0x29</td>
<td>R</td>
<td>Junction温度监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>表 7-46</td>
<td>0x2A</td>
<td>R</td>
<td>ADCIN0监控自动转换结果（8 MSBs）</td>
</tr>
<tr>
<td>表 7-47</td>
<td>0x2B</td>
<td>R</td>
<td>ADCIN0监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>表 7-48</td>
<td>0X2C</td>
<td>R</td>
<td>ADCIN1监控自动转换结果（8 MSBs）</td>
</tr>
<tr>
<td>表 7-49</td>
<td>0x2D</td>
<td>R</td>
<td>ADCIN1监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>表 7-50</td>
<td>0x2E</td>
<td>R</td>
<td>ADCIN2监控自动转换结果（8 MSBs）</td>
</tr>
<tr>
<td>表 7-51</td>
<td>0x2F</td>
<td>R</td>
<td>ADCIN2监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>表 7-52</td>
<td>0x30</td>
<td>R</td>
<td>ADCIN3监控自动转换结果（8 MSBs）</td>
</tr>
<tr>
<td>表 7-53</td>
<td>0x31</td>
<td>R</td>
<td>ADCIN3监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>表 7-54</td>
<td>0x32</td>
<td>R</td>
<td>ADCIN4监控自动转换结果（8 MSBs）</td>
</tr>
<tr>
<td>表 7-55</td>
<td>0x33</td>
<td>R</td>
<td>ADCIN4监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>表 7-56</td>
<td>0x34</td>
<td>R</td>
<td>ADCIN5监控自动转换结果（8 MSBs）</td>
</tr>
<tr>
<td>表 7-57</td>
<td>0x35</td>
<td>R</td>
<td>ADCIN5监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>表 7-58</td>
<td>0x36</td>
<td>RW</td>
<td>Junction温度监控上限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-59</td>
<td>0x37</td>
<td>RW</td>
<td>Junction温度监控下限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-60</td>
<td>0x38</td>
<td>RW</td>
<td>ADCIN0监控上限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-61</td>
<td>0x39</td>
<td>RW</td>
<td>ADCIN0监控下限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-62</td>
<td>0x3A</td>
<td>RW</td>
<td>ADCIN1监控上限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-63</td>
<td>0x3B</td>
<td>RW</td>
<td>ADCIN1监控下限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-64</td>
<td>0X3C</td>
<td>RW</td>
<td>ADCIN2监控上限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-65</td>
<td>0x3D</td>
<td>RW</td>
<td>ADCIN2监控下限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-66</td>
<td>0x3E</td>
<td>RW</td>
<td>ADCIN3监控上限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-67</td>
<td>0x3F</td>
<td>RW</td>
<td>ADCIN3监控下限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-68</td>
<td>0x40</td>
<td>RW</td>
<td>ADCIN4监控上限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-69</td>
<td>0x44</td>
<td>RW</td>
<td>ADCIN4监控下限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-70</td>
<td>0x42</td>
<td>RW</td>
<td>ADCIN5监控上限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td>表 7-71</td>
<td>0x43</td>
<td>RW</td>
<td>ADCIN5监控下限阈值设置（8 MSBs）</td>
</tr>
<tr>
<td><strong>WDT</strong></td>
<td>表 7-72</td>
<td>0x44</td>
<td>RW</td>
<td>看门狗控制寄存器</td>
</tr>
<tr>
<td><strong>Battery Charge</strong></td>
<td>表 7-73</td>
<td>0x45</td>
<td>RW</td>
<td>电池充电控制寄存器</td>
</tr>
<tr>
<td rowspan=33 colspan=1><strong>上下电控制 </strong></td>
<td>表 7-74</td>
<td>0x46</td>
<td>RWE</td>
<td>电源轨配置寄存器</td>
</tr>
<tr>
<td>表 7-75</td>
<td>0x47 + 3*n</td>
<td>RWE</td>
<td>BUCKn控制寄存器，n=0 ~ 5</td>
</tr>
<tr>
<td>表 7-76</td>
<td>0x48 + 3*n</td>
<td>RWE</td>
<td>BUCK电压设置</td>
</tr>
<tr>
<td>表 7-77</td>
<td>0x49 + 3*n</td>
<td>RWE</td>
<td>BUCK睡眠电压设置</td>
</tr>
<tr>
<td>表 7-78</td>
<td>0x59</td>
<td>RW</td>
<td>Switch控制寄存器</td>
</tr>
<tr>
<td>表 7-79</td>
<td>0x5A</td>
<td>RE</td>
<td>AONLDO控制寄存器</td>
</tr>
<tr>
<td>表 7-80</td>
<td>0x5B</td>
<td>RWE</td>
<td>ALDO控制寄存器</td>
</tr>
<tr>
<td>表 7-81</td>
<td>0x5C</td>
<td>RWE</td>
<td>ALDO电压设置</td>
</tr>
<tr>
<td>表 7-82</td>
<td>0x5D</td>
<td>RWE</td>
<td>ALDO睡眠电压设置</td>
</tr>
<tr>
<td>表 7-83</td>
<td>0x67</td>
<td>RWE</td>
<td>DLDO控制寄存器</td>
</tr>
<tr>
<td>表 7-84</td>
<td>0x68</td>
<td>RWE</td>
<td>DLDO电压设置</td>
</tr>
<tr>
<td>表 7-85</td>
<td>0x69</td>
<td>RWE</td>
<td>DLDO睡眠电压设置</td>
</tr>
<tr>
<td>表 7-86</td>
<td>0x7C</td>
<td>RWE</td>
<td>上下电控制寄存器0</td>
</tr>
<tr>
<td>表 7-87</td>
<td>0x7D</td>
<td>RWE</td>
<td>上下电控制寄存器1</td>
</tr>
<tr>
<td>表 7-88</td>
<td>0x7E</td>
<td>RWE</td>
<td>上下电控制寄存器2</td>
</tr>
<tr>
<td>表 7-89</td>
<td>0x7F</td>
<td>R</td>
<td>上下电状态寄存器0</td>
</tr>
<tr>
<td>表 7-90</td>
<td>0x80</td>
<td>R</td>
<td>上下电状态寄存器1</td>
</tr>
<tr>
<td>表 7-91</td>
<td>0x81</td>
<td>RWE</td>
<td>按键时间配置寄存器</td>
</tr>
<tr>
<td>表 7-92</td>
<td>0x82</td>
<td>RWE</td>
<td>上下电控制时间配置</td>
</tr>
<tr>
<td>表 7-93</td>
<td>0x88</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-94</td>
<td>0x84</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-95</td>
<td>0x85</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-96</td>
<td>0x86</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-97</td>
<td>0x87</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-98</td>
<td>0x88</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-99</td>
<td>0x89</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-100</td>
<td>0x8A</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-101</td>
<td>0x8B</td>
<td>RE</td>
<td>电源轨SLOT ID配置</td>
</tr>
<tr>
<td>表 7-102</td>
<td>0X8C</td>
<td>RE</td>
<td>EXT_EN  SLOT ID配置</td>
</tr>
<tr>
<td>表 7-103</td>
<td>0x8D</td>
<td>RE</td>
<td>EXT_EN  SLOT ID配置</td>
</tr>
<tr>
<td>表 7-104</td>
<td>0x8E</td>
<td>RE</td>
<td>EXT_EN  SLOT ID配置</td>
</tr>
<tr>
<td>表 7-105</td>
<td>0x8F</td>
<td>RWE</td>
<td>EXT_EN软件使能控制</td>
</tr>
<tr>
<td>表 7-106</td>
<td>0x90</td>
<td>RWE</td>
<td>EXT_EN睡眠流程控制</td>
</tr>
<tr>
<td rowspan=7 colspan=1><strong>事件</strong></td>
<td>表 7-107</td>
<td>0x91</td>
<td>RIO</td>
<td>PMIC系统事件</td>
</tr>
<tr>
<td>表 7-108</td>
<td>0x92</td>
<td>RIO</td>
<td>PMIC系统事件</td>
</tr>
<tr>
<td>表 7-109</td>
<td>0x99</td>
<td>RIO</td>
<td>PMIC系统事件</td>
</tr>
<tr>
<td>表 7-110</td>
<td>0x94</td>
<td>RIO</td>
<td>BUCK过压事件</td>
</tr>
<tr>
<td>表 7-111</td>
<td>0x95</td>
<td>RIO</td>
<td>BUCK欠压事件</td>
</tr>
<tr>
<td>表 7-112</td>
<td>0x96</td>
<td>RIO</td>
<td>BUCK短路/开路事件</td>
</tr>
<tr>
<td>表 7-113</td>
<td>0x97</td>
<td>RIO</td>
<td>PWRKY按键事件</td>
</tr>
<tr>
<td rowspan=7 colspan=1><strong>中断使能</strong></td>
<td>表 7-114</td>
<td>0x98</td>
<td>RW</td>
<td>PMIC系统事件中断使能</td>
</tr>
<tr>
<td>表 7-115</td>
<td>0x99</td>
<td>RW</td>
<td>PMIC系统事件中断使能</td>
</tr>
<tr>
<td>表 7-116</td>
<td>0x9A</td>
<td>RW</td>
<td>PMIC系统事件中断使能</td>
</tr>
<tr>
<td>表 7-117</td>
<td>0x9B</td>
<td>RW</td>
<td>BUCK过压事件中断使能</td>
</tr>
<tr>
<td>表 7-118</td>
<td>0X9C</td>
<td>RW</td>
<td>BUCK欠压事件中断使能</td>
</tr>
<tr>
<td>表 7-119</td>
<td>0x9D</td>
<td>RW</td>
<td>BUCK短路/开路事件中断使能</td>
</tr>
<tr>
<td>表 7-120</td>
<td>0x9E</td>
<td>RWE</td>
<td>PWRKY按键事件中断使能</td>
</tr>
<tr>
<td><strong>保护使能</strong></td>
<td>表 7-121</td>
<td>0x9F</td>
<td>RWE</td>
<td>系统异常事件保护使能</td>
</tr>
<tr>
<td rowspan=3 colspan=1><strong>ID</strong></td>
<td>表 7-122</td>
<td>0xA0</td>
<td>RE</td>
<td>设备ID</td>
</tr>
<tr>
<td>表 7-123</td>
<td>0xA1</td>
<td>RE</td>
<td>版本ID</td>
</tr>
<tr>
<td>表 7-124</td>
<td>0xA2</td>
<td>RE</td>
<td>用户ID</td>
</tr>
<tr>
<td rowspan=3 colspan=1><strong>系统配置</strong></td>
<td>表 7-125</td>
<td>0xAA</td>
<td>RE</td>
<td>系统配置寄存器0</td>
</tr>
<tr>
<td>表 7-126</td>
<td>0xA4</td>
<td>RE</td>
<td>系统配置寄存器1</td>
</tr>
<tr>
<td>表 7-127</td>
<td>0xA5</td>
<td>RE</td>
<td>系统配置寄存器2</td>
</tr>
<tr>
<td rowspan=5 colspan=1><strong>MTP</strong><br/> </td>
<td>表 7-128</td>
<td>0xA6</td>
<td>RW</td>
<td>MTP解锁寄存器</td>
</tr>
<tr>
<td>表 7-129</td>
<td>0xA7</td>
<td>RWP</td>
<td>MTP地址寄存器</td>
</tr>
<tr>
<td>表 7-130</td>
<td>0xA8</td>
<td>RWP</td>
<td>MTP读写数据寄存器</td>
</tr>
<tr>
<td>表 7-131</td>
<td>0xA9</td>
<td>RWP</td>
<td>MTP配置寄存器</td>
</tr>
<tr>
<td>表 7-132</td>
<td>0xAA</td>
<td>RWP</td>
<td>MTP控制寄存器</td>
</tr>
</tbody>
</table>

## 7.4 寄存器描述

### 表 7-4 GPIO\_IDR

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x0</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>GPIO5_IDR</td>
<td>R</td>
<td>0x0</td>
<td>GPIO5输入值</td>
</tr>
<tr>
<td>4</td>
<td>GPIO4_IDR</td>
<td>R</td>
<td>0x0</td>
<td>GPIO4输入值</td>
</tr>
<tr>
<td>3</td>
<td>GPIO3_IDR</td>
<td>R</td>
<td>0x0</td>
<td>GPIO3输入值</td>
</tr>
<tr>
<td>2</td>
<td>GPIO2_IDR</td>
<td>R</td>
<td>0x0</td>
<td>GPIO2输入值</td>
</tr>
<tr>
<td>1</td>
<td>GPIO1_IDR</td>
<td>R</td>
<td>0x0</td>
<td>GPIO1输入值</td>
</tr>
<tr>
<td>0</td>
<td>GPIO0_IDR</td>
<td>R</td>
<td>0x0</td>
<td>GPIO0输入值</td>
</tr>
</tbody>
</table>

### 表 7-5 GPIO\_ODR

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x1<br/></td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>GPIO5_ODR</td>
<td>RWE</td>
<td>0x0</td>
<td rowspan=6 colspan=1>作为GPIO输出时，为数据输出配置；<br/>作为复用功能时，为有效极性配置。<br/>- 0：输出低电平 / 有效极性为低电平<br/>- 1：输出高电平 / 有效极性为高电平<br/></td>
</tr>
<tr>
<td>4</td>
<td>GPIO4_ODR</td>
<td>RWE</td>
<td>0x0</td>
</tr>
<tr>
<td>3</td>
<td>GPIO3_ODR</td>
<td>RWE</td>
<td>0x0</td>
</tr>
<tr>
<td>2</td>
<td>GPIO2_ODR</td>
<td>RWE</td>
<td>0x0</td>
</tr>
<tr>
<td>1</td>
<td>GPIO1_ODR</td>
<td>RWE</td>
<td>0x0</td>
</tr>
<tr>
<td>0</td>
<td>GPIO0_ODR</td>
<td>RWE</td>
<td>0x0</td>
</tr>
</tbody>
</table>

### 表 7-6 GPIO\_PUPD0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x2</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>GPIO2_PUPD</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO2上下拉配置：<br/>00：无效操作<br/>01：上拉电阻使能<br/>10：下拉电阻使能<br/>1x：无效操作</td>
</tr>
<tr>
<td>3:2</td>
<td>GPIO1_PUPD</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO1上下拉配置：<br/>00：无效操作<br/>01：上拉电阻使能<br/>10：下拉电阻使能<br/>1x：无效操作</td>
</tr>
<tr>
<td>1:0</td>
<td>GPIO0_PUPD</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO0上下拉配置：<br/>00：无效操作<br/>01：上拉电阻使能<br/>10：下拉电阻使能<br/>1x：无效操作</td>
</tr>
</tbody>
</table>

### 表 7-7 GPIO\_PUPD1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x3</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>GPIO5_PUPD</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO5上下拉配置：<br/>00：无效操作<br/>01：上拉电阻使能<br/>10：下拉电阻使能<br/>1x：无效操作</td>
</tr>
<tr>
<td>3:2</td>
<td>GPIO4_PUPD</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO4上下拉配置：<br/>00：无效操作<br/>01：上拉电阻使能<br/>10：下拉电阻使能<br/>1x：无效操作</td>
</tr>
<tr>
<td>1:0</td>
<td>GPIO3_PUPD</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO3上下拉配置：<br/>00：无效操作<br/>01：上拉电阻使能<br/>10：下拉电阻使能<br/>1x：无效操作</td>
</tr>
</tbody>
</table>

### 表 7-8 GPIO\_DEB\_EN

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x4</td>
<td>7:6<br/></td>
<td>GPIO_DEB_TIME<br/></td>
<td>RW</td>
<td>0x0</td>
<td>GPIO0 ~ 5滤波时间选择<br/>00：100 us<br/>01：375 us<br/>10：750 us<br/>11：1.5 ms</td>
</tr>
<tr>
<td>5</td>
<td>GPIO5_DEB_EN</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO5滤波使能：<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>GPIO4_DEB_EN</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO4滤波使能：<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>GPIO3_DEB_EN</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO3滤波使能：<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>GPIO2_DEB_EN</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO2滤波使能：<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>GPIO1_DEB_EN</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO1滤波使能：<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>GPIO0_DEB_EN</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO0滤波使能：<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-9 GPIO\_OD

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x5 <br/> <br/></td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>GPIO5_OD</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO5输出开漏配置<br/>0：推挽输出<br/>1：开漏输出</td>
</tr>
<tr>
<td>4<br/></td>
<td>GPIO4_OD</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO4输出开漏配置<br/>0：推挽输出<br/>1：开漏输出</td>
</tr>
<tr>
<td>3</td>
<td>GPIO3_OD</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO3输出开漏配置<br/>0：推挽输出<br/>1：开漏输出</td>
</tr>
<tr>
<td>2</td>
<td>GPIO2_OD</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO2输出开漏配置<br/>0：推挽输出<br/>1：开漏输出</td>
</tr>
<tr>
<td>1</td>
<td>GPIO1_OD</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO1输出开漏配置<br/>0：推挽输出<br/>1：开漏输出</td>
</tr>
<tr>
<td>0</td>
<td>GPIO0_OD</td>
<td>RW</td>
<td>0x0</td>
<td>GPIO0输出开漏配置<br/>0：推挽输出<br/>1：开漏输出</td>
</tr>
</tbody>
</table>

### 表 7-10 GPIO\_ITYPE0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x6</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>GPIO2_ITYPE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO2中断类型<br/>00：上升沿中断<br/>01：下降沿中断<br/>10：高电平中断<br/>11：低电平中断</td>
</tr>
<tr>
<td>3:2</td>
<td>GPIO1_ITYPE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO1中断类型<br/>00：上升沿中断<br/>01：下降沿中断<br/>10：高电平中断<br/>11：低电平中断</td>
</tr>
<tr>
<td>1:0</td>
<td>GPIO0_ITYPE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO0中断类型<br/>00：上升沿中断<br/>01：下降沿中断<br/>10：高电平中断<br/>11：低电平中断</td>
</tr>
</tbody>
</table>

### 表 7-11 GPIO\_ITYPE1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x7</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>GPIO5_ITYPE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO5中断类型<br/>00：上升沿中断<br/>01：下降沿中断<br/>10：高电平中断<br/>11：低电平中断</td>
</tr>
<tr>
<td>3:2</td>
<td>GPIO4_ITYPE</td>
<td>RWE</td>
<td>0x0<br/></td>
<td>GPIO4中断类型<br/>00：上升沿中断<br/>01：下降沿中断<br/>10：高电平中断<br/>11：低电平中断</td>
</tr>
<tr>
<td>1:0</td>
<td>GPIO3_ITYPE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO3中断类型<br/>00：上升沿中断<br/>01：下降沿中断<br/>10：高电平中断<br/>11：低电平中断</td>
</tr>
</tbody>
</table>

### 表 7-12 GPIO\_MODE0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x8</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>GPIO2_MODE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO2模式选择<br/>00：输入模式<br/>01：输出模式<br/>1x：复用模式</td>
</tr>
<tr>
<td>3:2</td>
<td>GPIO1_MODE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO1模式选择<br/>00：输入模式<br/>01：输出模式<br/>1x：复用模式</td>
</tr>
<tr>
<td>1:0</td>
<td>GPIO0_MODE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO0模式选择<br/>00：输入模式<br/>01：输出模式<br/>1x：复用模式</td>
</tr>
</tbody>
</table>

### 表 7-13 GPIO\_MODE1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x9</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>GPIO5_MODE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO5模式选择<br/>00：输入模式<br/>01：输出模式<br/>1x：复用模式</td>
</tr>
<tr>
<td>3:2</td>
<td>GPIO4_MODE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO4模式选择<br/>00：输入模式<br/>01：输出模式<br/>1x：复用模式</td>
</tr>
<tr>
<td>1:0</td>
<td>GPIO3_MODE</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO3模式选择<br/>00：输入模式<br/>01：输出模式<br/>1x：复用模式</td>
</tr>
</tbody>
</table>

### 表 7-14 GPIO\_AF01

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0xA</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:3</td>
<td>GPIO1_AFR</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO1复用功能选择<br/>000：外部电源使能输出信号（EXT_EN）<br/>001：外部上电时序控制输入信号（PWRCTRL）<br/>010：外部休眠、唤醒控制输入信号（Sleep/Wakeup）<br/>011：外部复位控制输入信号（nReset）<br/>1xx：ADC输入信号（ADCIN）</td>
</tr>
<tr>
<td>2:0</td>
<td>GPIO0_AFR</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO0复用功能选择<br/>000：外部电源使能输出信号（EXT_EN）<br/>001：外部上电时序控制输入信号（PWRCTRL）<br/>010：外部休眠、唤醒控制输入信号（Sleep/Wakeup）<br/>011：外部复位控制输入信号（nReset）<br/>1xx：ADC输入信号（ADCIN）</td>
</tr>
</tbody>
</table>

### 表 7-15 GPIO\_AF23

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0xB<br/> <br/> </td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:3</td>
<td>GPIO3_AFR</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO3复用功能选择<br/>000：外部电源使能输出信号（EXT_EN）<br/>001：外部上电时序控制输入信号（PWRCTRL）<br/>010：外部休眠、唤醒控制输入信号（Sleep/Wakeup）<br/>011：外部复位控制输入信号（nReset）<br/>1xx：ADC输入信号（ADCIN）</td>
</tr>
<tr>
<td>2:0</td>
<td>GPIO2_AFR</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO2复用功能选择<br/>000：外部电源使能输出信号（EXT_EN）<br/>001：外部上电时序控制输入信号（PWRCTRL）<br/>010：外部休眠、唤醒控制输入信号（Sleep/Wakeup）<br/>011：外部复位控制输入信号（nReset）<br/>1xx：ADC输入信号（ADCIN）</td>
</tr>
</tbody>
</table>

### 表 7-16 GPIO\_AF45

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0xC<br/> <br/> </td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:3</td>
<td>GPIO5_AFR</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO5复用功能选择<br/>000：外部电源使能输出信号（EXT_EN）<br/>001：外部上电时序控制输入信号（PWRCTRL）<br/>010：外部休眠、唤醒控制输入信号（Sleep/Wakeup）<br/>011：外部复位控制输入信号（nReset）<br/>1xx：ADC输入信号（ADCIN）</td>
</tr>
<tr>
<td>2:0</td>
<td>GPIO4_AFR</td>
<td>RWE</td>
<td>0x0</td>
<td>GPIO4复用功能选择<br/>000：外部电源使能输出信号（EXT_EN）<br/>001：外部上电时序控制输入信号（PWRCTRL）<br/>010：外部休眠、唤醒控制输入信号（Sleep/Wakeup）<br/>011：外部复位控制输入信号（nReset）<br/>1xx：ADC输入信号（ADCIN）</td>
</tr>
</tbody>
</table>

### 表 7-17 RTC\_COUNT\_S

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0xD </td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:0</td>
<td>COUNT_S</td>
<td>RW</td>
<td>0x00</td>
<td>RTC seconds 读出寄存器。<br/>读此寄存器会将当前日历数据更新到COUNT_S ~ COUNT_Y</td>
</tr>
</tbody>
</table>

### 表 7-18 RTC\_COUNT\_MI

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0xE</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:0</td>
<td>COUNT_MI</td>
<td>RW</td>
<td>0x00</td>
<td>RTC minutes 读出寄存器</td>
</tr>
</tbody>
</table>

### 表 7-19 RTC\_COUNT\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0xF</td>
<td>7:5</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>4:0</td>
<td>COUNT_H</td>
<td>RW</td>
<td>0x00</td>
<td>RTC hours 读出寄存器</td>
</tr>
</tbody>
</table>

### 表 7-20 RTC\_COUNT\_D

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x10 </td>
<td>7:5</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>4:0</td>
<td>COUNT_D</td>
<td>RW</td>
<td>0x00</td>
<td>RTC days 读出寄存器</td>
</tr>
</tbody>
</table>

### 表 7-21 RTC\_COUNT\_MO

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x11</td>
<td>7:4</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>3:0</td>
<td>COUNT_MO</td>
<td>RW</td>
<td>0x00</td>
<td>RTC months 读出寄存器</td>
</tr>
</tbody>
</table>

### 表 7-22 RTC\_COUNT\_Y

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x12</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:0</td>
<td>COUNT_Y</td>
<td>RW</td>
<td>0x00</td>
<td>RTC years 读出寄存器。<br/>写此寄存器，会将当前COUNT_S ~ COUNT_Y更新到日历计数器；<br/>并且RTC_SECOND_A ~ RTC_SECOND_D复位。</td>
</tr>
</tbody>
</table>

### 表 7-23 RTC\_ALARM\_S

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x13</td>
<td>7</td>
<td>MASK_ALARM_S</td>
<td>RW</td>
<td>0x0</td>
<td>ALARM_S匹配屏蔽<br/>0：不屏蔽<br/>1：屏蔽</td>
</tr>
<tr>
<td>6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:0</td>
<td>ALARM_S</td>
<td>RW</td>
<td>0x00</td>
<td>RTC_ALARM seconds 设置，设置范围0x00 ~ 0x3B</td>
</tr>
</tbody>
</table>

### 表 7-24 RTC\_ALARM\_MI

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x14 </td>
<td>7</td>
<td>MASK_ALARM_MI</td>
<td>RW</td>
<td>0x0</td>
<td>ALARM_MI匹配屏蔽<br/>0：不屏蔽<br/>1：屏蔽</td>
</tr>
<tr>
<td>6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:0</td>
<td>ALARM_MI</td>
<td>RW</td>
<td>0x00</td>
<td>RTC_ALARM minutes 设置<br/>设置范围0x00 ~ 0x3B</td>
</tr>
</tbody>
</table>

### 表 7-25 RTC\_ALARM\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x15</td>
<td>7</td>
<td>MASK_ALARM_H</td>
<td>RW</td>
<td>0x0</td>
<td>ALARM_H匹配屏蔽<br/>0：不屏蔽<br/>1：屏蔽</td>
</tr>
<tr>
<td>6:5</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>4:0</td>
<td>ALARM_H</td>
<td>RW</td>
<td>0x00</td>
<td>RTC_ALARM hours 设置<br/>设置范围0x00 ~ 0x17</td>
</tr>
</tbody>
</table>

### 表 7-26 RTC\_ALARM\_D

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x16</td>
<td>7</td>
<td>MASK_ALARM_D</td>
<td>RW</td>
<td>0x0</td>
<td>ALARM_D匹配屏蔽<br/>0：不屏蔽<br/>1：屏蔽</td>
</tr>
<tr>
<td>6:5</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>4:0</td>
<td>ALARM_D</td>
<td>RW</td>
<td>0x00</td>
<td>RTC_ALARM days 设置<br/>设置范围0x00 ~ 0x1F</td>
</tr>
</tbody>
</table>

### 表 7-27 RTC\_ALARM\_MO

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x17<br/> <br/> </td>
<td>7</td>
<td>MASK_ALARM_MO</td>
<td>RW</td>
<td>0x0</td>
<td>ALARM_MO匹配屏蔽<br/>0：不屏蔽<br/>1：屏蔽</td>
</tr>
<tr>
<td>6:4</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>3:0</td>
<td>ALARM_MO</td>
<td>RW</td>
<td>0x00</td>
<td>RTC_ALARM months 设置<br/>设置范围0x00 ~ 0x0C</td>
</tr>
</tbody>
</table>

表 7-28 RTC\_ALARM\_Y

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x18</td>
<td>7</td>
<td>MASK_ALARM_Y</td>
<td>RW</td>
<td>0x0</td>
<td>ALARM_Y匹配屏蔽<br/>0：不屏蔽<br/>1：屏蔽</td>
</tr>
<tr>
<td>6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:0</td>
<td>ALARM_Y</td>
<td>RW</td>
<td>0x00</td>
<td>RTC_ALARM years 设置<br/>设置范围0x00 ~ 0x3F</td>
</tr>
</tbody>
</table>

### 表 7-29 RTC\_SECOND\_A

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x19</td>
<td>7:0</td>
<td>SECOND_A</td>
<td>R</td>
<td>0x00</td>
<td>RTC 秒计数[7:0]。<br/>读此寄存器会将当前32bit秒计数器数值更新到SECOND_A ~ SECOND_D</td>
</tr>
</tbody>
</table>

### 表 7-30 RTC\_SECOND\_B

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x1A</td>
<td>7:0</td>
<td>SECOND_B</td>
<td>R</td>
<td>0x00</td>
<td>RTC 秒计数[15:8]</td>
</tr>
</tbody>
</table>

### 表 7-31 RTC\_SECOND\_C

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x1B</td>
<td>7:0</td>
<td>SECOND_C</td>
<td>R</td>
<td>0x00</td>
<td>RTC 秒计数[23:16]</td>
</tr>
</tbody>
</table>

### 表 7-32 RTC\_SECOND\_D

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x1C</td>
<td>7:0</td>
<td>SECOND_D</td>
<td>R</td>
<td>0x00</td>
<td>RTC 秒计数[31:24]</td>
</tr>
</tbody>
</table>

### 表 7-33 RTC\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x1D<br/> <br/> <br/> <br/> <br/> <br/> <br/> </td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6</td>
<td>TICK_EN</td>
<td>RW</td>
<td>0x0</td>
<td>TICK使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>5</td>
<td>ALARM_EN</td>
<td>RW</td>
<td>0x0</td>
<td>ALARM使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4<br/></td>
<td>TICK_TYPE</td>
<td>RW</td>
<td>0x0</td>
<td>TICK周期选择：<br/>0：1s<br/>1：1min</td>
</tr>
<tr>
<td>3</td>
<td>RTC_CLK_SEL</td>
<td>RW</td>
<td>0x0</td>
<td>RTC时钟选择<br/>0：内部时钟（32 kHz）<br/>1：外部晶振时钟</td>
</tr>
<tr>
<td>2</td>
<td>RTC_EN</td>
<td>RW</td>
<td>0x0</td>
<td>RTC使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>OUT_32K_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>RTC时钟输出使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>CRYSTAL_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>外部晶振使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-34 ADC\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x1E<br/> <br/> </td>
<td>7:2</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>1</td>
<td>ADC_GO<strong>(1)</strong></td>
<td>RW</td>
<td>0</td>
<td>ADC转换启动位<br/>0：AD转换完成/未进行<br/>1：AD转换正在进行</td>
</tr>
<tr>
<td>0</td>
<td>ADC_EN</td>
<td>RW</td>
<td>0</td>
<td>ADC使能位<br/>0：禁止ADC<br/>1：使能ADC</td>
</tr>
</tbody>
</table>

### 表 7-35 ADC\_CFG0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x1F<br/> </td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6</td>
<td>ADCTJ_DEB_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADC结温超阈值中断标志滤波<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>5<br/></td>
<td>ADCIN5_DEB_EN(1)<br/></td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN5中断标志滤波<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>ADCIN4_DEB_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN4中断标志滤波<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>ADCIN3_DEB_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN3中断标志滤波<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>ADCIN2_DEB_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN2中断标志滤波<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>ADCIN1_DEB_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN1中断标志滤波<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>ADCIN0_DEB_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN0中断标志滤波<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

- 连续 ADC\_DEB\_NUM 次 ADC 转换结果超阈值或低阈值即置起相应标志位。

### 表 7-36 ADC\_CFG1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x20<br/> <br/> <br/> </td>
<td>7</td>
<td>ADC_CHOP_SEL</td>
<td>RW</td>
<td>0x0</td>
<td>ADC chop时钟选择<br/>0：31.25 kHz<br/>1：62.5 kHz</td>
</tr>
<tr>
<td>6</td>
<td>ADC_CHOP_EN</td>
<td>RW</td>
<td>0x0</td>
<td>ADC chop使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>5:3</td>
<td>ADC_CHNL_SEL</td>
<td>RW</td>
<td>0x0</td>
<td>ADC手动模式扫描通道选择<br/>000：通道0 – Vsys、BUCK、LDO电压<br/>001：通道1 - Tj，芯片内部Junction温度<br/>010：通道2 - GPIO0作为ADC输入（ADCIN0）<br/>011：通道3 - GPIO1作为ADC输入（ADCIN1）<br/>100：通道4 - GPIO2作为ADC输入（ADCIN2）<br/>101：通道5 - GPIO3作为ADC输入（ADCIN3）<br/>110：通道6 - GPIO4作为ADC输入（ADCIN4）<br/>111：通道7 - GPIO5作为ADC输入（ADCIN5）</td>
</tr>
<tr>
<td>2:0</td>
<td>ADC_SAMP_FREQ</td>
<td>RW</td>
<td>0x0</td>
<td>自动扫描的采样频率选择<br/>000：采样频率为100 Hz<br/>001：采样频率为781.25 Hz<br/>010：采样频率为1.5625 kHz<br/>011：采样频率为3.125 kHz<br/>100：采样频率为6.25 kHz<br/>101：采样频率为12.5 kHz<br/>110：采样频率为25 kHz<br/>111：采样频率为50 kHz</td>
</tr>
</tbody>
</table>

### 表 7-37 ADC\_CFG2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x21</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6:4</td>
<td>ADC_DEB_NUM<br/></td>
<td>RW</td>
<td>0x0</td>
<td>ADC结果滤波档位选择<br/>000：连续2次触发<br/>001：连续3次触发<br/>010：连续4次触发<br/>011：连续5次触发<br/>100：连续6次触发<br/>其它：连续7次触发</td>
</tr>
<tr>
<td>3:2</td>
<td>ADC_VREFH_SEL</td>
<td>RW</td>
<td>0x0</td>
<td>ADC正端参考电压选择<br/>00：Int<br/>01：VCC<br/>10：Ext<br/>11：Int + Cap</td>
</tr>
<tr>
<td>1:0</td>
<td>ADC_REF_SEL</td>
<td>RW</td>
<td>0x0</td>
<td>ADC参考电压选择<br/>01：2V内部参考电压<br/>10：3V内部参考电压<br/>其它：disalbe</td>
</tr>
</tbody>
</table>

### 表 7-38 ADC\_AUTO

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x22<br/></td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6</td>
<td>AUTO_IN5_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN5自动采样使能<br/>0：禁止自动采样<br/>1：使能自动采样</td>
</tr>
<tr>
<td>5</td>
<td>AUTO_IN4_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN4自动采样使能<br/>0：禁止自动采样<br/>1：使能自动采样</td>
</tr>
<tr>
<td>4</td>
<td>AUTO_IN3_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN3自动采样使能<br/>0：禁止自动采样<br/>1：使能自动采样</td>
</tr>
<tr>
<td>3</td>
<td>AUTO_IN2_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN2自动采样使能<br/>0：禁止自动采样<br/>1：使能自动采样</td>
</tr>
<tr>
<td>2</td>
<td>AUTO_IN1_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN1自动采样使能<br/>0：禁止自动采样<br/>1：使能自动采样</td>
</tr>
<tr>
<td>1</td>
<td>AUTO_IN0_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ADCIN0自动采样使能<br/>0：禁止自动采样<br/>1：使能自动采样</td>
</tr>
<tr>
<td>0</td>
<td>AUTO_TJ_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>Junction温度通道自动采样使能<br/>0：禁止自动采样<br/>1：使能自动采样</td>
</tr>
</tbody>
</table>

- 连 ADC\_AUTO[6:0]只要有任 1bit 使能，启动转换之后即进入自动扫描模式。

### 表 7-39 ADC\_MAN\_EN0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x23<br/></td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6</td>
<td>ADC_VSYS_EN</td>
<td>RW<br/></td>
<td>0x0</td>
<td>VSYS电压监控使能<br/>0： 禁止监控<br/>1： 使能监控</td>
</tr>
<tr>
<td>5</td>
<td>ADC_BUCK6_EN</td>
<td>RW</td>
<td>0x0</td>
<td>BUCK6输出电压监控使能<br/>0： 禁止监控<br/>1： 使能监控</td>
</tr>
<tr>
<td>4</td>
<td>ADC_BUCK5_EN</td>
<td>RW</td>
<td>0x0</td>
<td>BUCK5输出电压监控使能<br/>0： 禁止监控<br/>1： 使能监控</td>
</tr>
<tr>
<td>3</td>
<td>ADC_BUCK4_EN</td>
<td>RW</td>
<td>0x0</td>
<td>BUCK4输出电压监控使能<br/>0： 禁止监控<br/>1： 使能监控</td>
</tr>
<tr>
<td>2</td>
<td>ADC_BUCK3_EN</td>
<td>RW</td>
<td>0x0</td>
<td>BUCK3输出电压监控使能<br/>0： 禁止监控<br/>1： 使能监控</td>
</tr>
<tr>
<td>1</td>
<td>ADC_BUCK2_EN</td>
<td>RW</td>
<td>0x0</td>
<td>BUCK2输出电压监控使能<br/>0： 禁止监控<br/>1： 使能监控</td>
</tr>
<tr>
<td>0</td>
<td>ADC_BUCK1_EN</td>
<td>RW</td>
<td>0x0</td>
<td>BUCK1输出电压监控使能<br/>0： 禁止监控<br/>1： 使能监控</td>
</tr>
</tbody>
</table>

### 表 7-40 ADC\_MAN\_EN1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x24</td>
<td>7</td>
<td>ADC_DLDO3_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>DLDO3输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>6</td>
<td>ADC_DLDO2_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>DLDO2输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>5</td>
<td>ADC_DLDO1_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>DLDO1输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>4</td>
<td>ADC_ALDO4_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ALDO4输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>3</td>
<td>ADC_ALDO3_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ALDO3输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>2</td>
<td>ADC_ALDO2_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ALDO2输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>1</td>
<td>ADC_ALDO1_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>ALDO1输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>0</td>
<td>ADC_AONLDO_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>AONLDO输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
</tbody>
</table>

- ADC\_AUTO 无自动通道使能时，只要 ADC\_MAN\_EN0 ~ ADC\_MAN\_EN2 中任意手动通道使能后，启动转换之后即进入手动模式。

### 表 7-41 ADC\_MAN\_EN2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=5 colspan=1>0x25</td>
<td>7:4</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>3</td>
<td>ADC_DLDO_7_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>DLDO7输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>2</td>
<td>ADC_DLDO_6_EN(1)<br/></td>
<td>RW</td>
<td>0x0</td>
<td>DLDO6输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>1</td>
<td>ADC_DLDO_5_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>DLDO5输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
<tr>
<td>0</td>
<td>ADC_DLDO_4_EN(1)</td>
<td>RW</td>
<td>0x0</td>
<td>DLDO4输出电压监控使能<br/>0： 禁止<br/>1： 使能</td>
</tr>
</tbody>
</table>

- ADC\_AUTO 无自动通道使能时，只要 ADC\_MAN\_EN0 ~ ADC\_MAN\_EN2 中任意手动通道使能后，启动转换之后即进入手动模式。

### 表 7-42 ADC\_MAN\_RES\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x26</td>
<td>7:0</td>
<td>ADC_RES_H</td>
<td>R</td>
<td>0x00</td>
<td>12-bit ADC手动转换结果（8 MSBs）。<br/>读该寄存器，会将当前手动转换通道的12bit结果锁存到ADC_MAN_RES_H和DC_MAN_RES_L，防止后续读取低位结果时被新的转换结果给覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-43 ADC\_MAN\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x27</td>
<td>7:4</td>
<td>ADC_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>12-bit ADC手动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-44 ADC\_TJ\_RES\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x28</td>
<td>7:0</td>
<td>TJ_RES_H</td>
<td>R</td>
<td>0x00</td>
<td>Junction温度监控自动转换结果（8 MSBs）。<br/>读该寄存器，会将当前Junction寄存器结果锁存到ADC_TJ_RES_H和ADC_TJ_RES_L，防止后续读取低位结果时被新的转换结果覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-45 ADC\_TJ\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x29</td>
<td>7:4</td>
<td>TJ_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>Junction温度监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-46 ADC\_IN0\_RES\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x2A</td>
<td>7:0</td>
<td>ADCIN0_RES_H</td>
<td>R</td>
<td>0x00</td>
<td>ADCIN0监控自动转换结果（8 MSBs）<br/>读该寄存器，会将当前通道0结果锁存到ADC_IN0_RES_H和ADC_IN0_RES_L，防止后续读取低位结果时被新的转换结果覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-47 ADC\_IN0\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x2B</td>
<td>7:4</td>
<td>ADCIN0_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>ADCIN0监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-48 ADC\_IN1\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x2C</td>
<td>7:0</td>
<td>ADCIN1_RES_H</td>
<td>R</td>
<td>0x0</td>
<td>ADCIN2监控自动转换结果（8 MSBs）<br/>读该寄存器，会将当前通道2结果锁存到ADC_IN2_RES_H和ADC_IN2_RES_L，防止后续读取低位结果时被新的转换结果覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-49 ADC\_IN1\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x2D</td>
<td>7:4</td>
<td>ADCIN1_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>ADCIN1监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-50 ADC\_IN2\_RES\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x2E</td>
<td>7:0</td>
<td>ADCIN2_RES_H</td>
<td>R</td>
<td>0x00</td>
<td>ADCIN2监控自动转换结果（8 MSBs）<br/>读该寄存器，会将当前通道2结果锁存到ADC_IN2_RES_H和ADC_IN2_RES_L，防止后续读取低位结果时被新的转换结果覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-51 ADC\_IN2\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x2F</td>
<td>7:4</td>
<td>ADCIN2_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>ADCIN2监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-52 ADC\_IN3\_RES\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x30</td>
<td>7:0</td>
<td>ADCIN3_RES_H</td>
<td>R</td>
<td>0x00</td>
<td>ADCIN3监控自动转换结果（8 MSBs）<br/>读该寄存器，会将当前通道3结果锁存到ADC_IN3_RES_H和ADC_IN3_RES_L，防止后续读取低位结果时被新的转换结果覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-53 ADC\_IN3\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x31</td>
<td>7:4</td>
<td>ADCIN3_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>ADCIN3监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-54 ADC\_IN4\_RES\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x32</td>
<td>7:0</td>
<td>ADCIN4_RES_H</td>
<td>R</td>
<td>0x00</td>
<td>ADCIN4监控自动转换结果（8 MSBs）<br/>读该寄存器，会将当前通道4结果锁存到ADC_IN4_RES_H和ADC_IN4_RES_L，防止后续读取低位结果时被新的转换结果覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-55 ADC\_IN4\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x33</td>
<td>7:4</td>
<td>ADCIN4_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>ADCIN4监控自动转换结果（4 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-56 ADC\_IN5\_RES\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x34</td>
<td>7:0</td>
<td>ADCIN5_RES_H</td>
<td>R</td>
<td>0x00</td>
<td>ADCIN5监控自动转换结果（8 MSBs）<br/>读该寄存器，会将当前通道5结果锁存到ADC_IN5_RES_H和ADC_IN5_RES_L，防止后续读取低位结果时被新的转换结果覆盖，导致数据的不一致性。</td>
</tr>
</tbody>
</table>

### 表 7-57 ADC\_IN5\_RES\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x35</td>
<td>7:4</td>
<td>ADCIN5_RES_L</td>
<td>R</td>
<td>0x0</td>
<td>ADCIN5监控自动转换结果（5 LSBs）</td>
</tr>
<tr>
<td>3:0</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-58 ADC\_VTH\_TJ\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x36</td>
<td>7:0</td>
<td>VTH_TJ_H</td>
<td>RW</td>
<td>0x00</td>
<td>Junction温度监控上限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-59 ADC\_VTH\_TJ\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x37</td>
<td>7:0</td>
<td>VTH_TJ_L</td>
<td>RW</td>
<td>0x00</td>
<td>Junction温度监控下限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-60 ADC\_IN0\_VTH\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x38</td>
<td>7:0</td>
<td>ADCIN0_VTH_H</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN0监控上限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-61 ADC\_IN0\_VTH\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x39</td>
<td>7:0</td>
<td>ADCIN0_VTH_L</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN0监控下限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-62 ADC\_IN1\_VTH\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x3A</td>
<td>7:0</td>
<td>ADCIN1_VTH_H</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN1监控上限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-63 ADC\_IN1\_VTH\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x3B</td>
<td>7:0</td>
<td>ADCIN1_VTH_L</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN1监控下限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-64 ADC\_IN2\_VTH\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x3C</td>
<td>7:0</td>
<td>ADCIN2_VTH_H</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN2监控上限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-65 ADC\_IN2\_VTH\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x3D</td>
<td>7:0</td>
<td>ADCIN2_VTH_L</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN2监控下限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-66 ADC\_IN3\_VTH\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x3E</td>
<td>7:0</td>
<td>ADCIN3_VTH_H</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN3监控上限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-67 ADC\_IN3\_VTH\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x3F</td>
<td>7:0</td>
<td>ADCIN3_VTH_L</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN3监控下限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-68 ADC\_IN4\_VTH\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x40</td>
<td>7:0</td>
<td>ADCIN4_VTH_H</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN4监控上限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-69 ADC\_IN4\_VTH\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x41</td>
<td>7:0</td>
<td>ADCIN4_VTH_L</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN4监控下限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-70 ADC\_IN5\_VTH\_H

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x42</td>
<td>7:0</td>
<td>ADCIN5_VTH_H</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN5监控上限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-71 ADC\_IN5\_VTH\_L

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x43</td>
<td>7:0</td>
<td>ADCIN5_VTH_L</td>
<td>RW</td>
<td>0x00</td>
<td>ADCIN5监控下限阈值设置（8 MSBs）</td>
</tr>
</tbody>
</table>

### 表 7-72 WDT\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x44</td>
<td>7:4</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>3</td>
<td>WDT_EN</td>
<td>RW</td>
<td>0x0</td>
<td>看门狗使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2:1</td>
<td>WDT_SCALE</td>
<td>RW</td>
<td>0x0</td>
<td>看门狗超时时间配置<br/>00：1 s<br/>01：4 s<br/>10：8 s<br/>11：16 s</td>
</tr>
<tr>
<td>0</td>
<td>WDT_FEED</td>
<td>RW</td>
<td>0x0</td>
<td>看门狗计数清除<br/>置1，清零WDT计数器。硬件自动清0</td>
</tr>
</tbody>
</table>

### 表 7-73 BBAT\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x45</td>
<td>7:5</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>4:3</td>
<td>BCHG_ISET</td>
<td>RW</td>
<td>0x0</td>
<td>纽扣电池充电电流档位<br/>100：500uA<br/>101：1mA<br/>110：2mA<br/>111：4A</td>
</tr>
<tr>
<td>2:1</td>
<td>BCHG_VSET</td>
<td>RW</td>
<td>0x0</td>
<td>纽扣电池充电电压<br/>100：2.8 V<br/>101：2.9 V<br/>110：3 V<br/>111：3.1 V</td>
</tr>
<tr>
<td>0</td>
<td>BCHG_EN</td>
<td>RW</td>
<td>0x0</td>
<td>纽扣电池充电使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-74 BUCK\_LDO\_CFG

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x46</td>
<td>7</td>
<td>LDO_PD_EN</td>
<td>RWE</td>
<td>0</td>
<td>LDO下拉电阻使能<br/>0：禁止<br/>1：使能<br/>LDO使能时，该bit不起作用，即关闭下拉电阻；<br/>LDO关闭时，下拉电阻受此bit影响。</td>
</tr>
<tr>
<td>6</td>
<td>BUCK_PD_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK下拉电阻使能<br/>0：禁止<br/>1：使能<br/>BUCK使能时，该bit不起作用，即关闭下拉电阻；<br/>BUCK关闭时，下拉电阻受此bit影响。</td>
</tr>
<tr>
<td>5</td>
<td>BUCK_DVS_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK DVS使能<br/>0：禁止<br/>1：使能<br/>上电过程中，BUCK无DVS功能；在开机/关机模式，睡眠/唤醒流程中才有DVS。</td>
</tr>
<tr>
<td>4:3</td>
<td>BUCK_DVS_SEL</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK DVS斜率档位<br/>00：5 mV/us<br/>01：10 mV/us<br/>10：25 mV/us<br/>11：50 mV/us</td>
</tr>
<tr>
<td>2</td>
<td>BUCK_VSET_CTRL</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK5/6 VSET引脚的电压档位选择<br/>VSET     VDD       FLOATING        GND<br/>   <strong>0</strong>      1.1 V       BUCKx_VOLT    1.2 V<br/>   <strong>1</strong>      0.6 V       BUCKx_VOLT    1.5 V</td>
</tr>
<tr>
<td>1</td>
<td>BUCK_34_DUAL</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK3和BUCK4双相模式使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>BUCK_12_DUAL</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK1和BUCK2双相模式使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-75 BUCKx\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=5 colspan=1>0x47+3*N(1)</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:3</td>
<td>BUCKx_GPIO_SEL</td>
<td>RE</td>
<td>0x0</td>
<td>GPIO（PWRCTRL）控制BUCK使能<br/>000：不由GPIO控制<br/>001：GPIO0控制<br/>010： GPIO1控制<br/>011： GPIO2控制<br/>100： GPIO3控制<br/>101： GPIO4控制<br/>110： GPIO5控制<br/>111： 不由GPIO控制</td>
</tr>
<tr>
<td>2</td>
<td>BUCKx_MODE</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK工作模式<br/>0：PFM/PWM自动切换模式<br/>1：强制PWM模式</td>
</tr>
<tr>
<td>1</td>
<td>BUCKx_ILIM</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK限流档位<br/>0：BUCK1 ~ 2，5000 mA； BUCK3 ~ 6，3500 mA<br/>1：BUCK1 ~ 2，7500 mA； BUCK3 ~ 6，5000 mA</td>
</tr>
<tr>
<td>0</td>
<td>BUCKx_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>BUCK使能<br/>0：关闭<br/>1：使能</td>
</tr>
</tbody>
</table>

- N=0 ~ 5，x=1 ~ 6，依次对应 BUCK1 ~ BUCK6。

### 表 7-76 BUCKx\_VOLT

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x48+3*N(1)</td>
<td>7:0</td>
<td>BUCKx_VOLT</td>
<td>RWE</td>
<td>0x00</td>
<td>BUCK电压输出档位（8 MSBs）<br/>0.5V ~ 1.35V 5mV/step，1.375V ~ 3.45V 25mV/step<br/>00000000：0.500V<br/>00000001：0.505V<br/>00000010：0.510V<br/>...<br/>11111110：3.450V<br/>11111111：不允许写该档位</td>
</tr>
</tbody>
</table>

- N=0 ~ 5，x=1 ~ 6，依次对应 BUCK1 ~ BUCK6。

### 表 7-77 BUCKx\_SLP\_VOLT

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0x49+3*N(1)</td>
<td>7:0</td>
<td>BUCKx_SLP_VOLT</td>
<td>RWE</td>
<td>0x00</td>
<td>BUCK睡眠电压输出档位（8 MSBs）<br/>0.5V ~ 1.35V 5mV/step，1.375V ~ 3.45V 25mV/step<br/>00000000： 0.500V<br/>00000001： 0.505V<br/>00000010： 0.510V<br/>...<br/>11111110： 3.450V<br/>11111111： 0V（关闭BUCKx）</td>
</tr>
</tbody>
</table>

- N=0 ~ 5，x=1 ~ 6，依次对应 BUCK1 ~ BUCK6。

### 表 7-78 SWITCH\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x59</td>
<td>7:2</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>1<br/></td>
<td>SWITCH_PD_EN</td>
<td>RW</td>
<td>0x0</td>
<td>SWITCH下拉电阻使能<br/>0：禁止<br/>1：使能<br/>SWITCH_EN使能时，下拉电阻禁止，即该bit无效；仅当SWITCH_EN为0时下拉电阻才受该bit控制。</td>
</tr>
<tr>
<td>0</td>
<td>SWITCH_EN</td>
<td>RW</td>
<td>0x0</td>
<td>SWITCH使能<br/>0：关闭<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-79 AONLDO\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x5A</td>
<td>7:1</td>
<td>AONLDO_VOLT</td>
<td>RE</td>
<td>0x00</td>
<td>AONLDO电压输出档位（7 MSBs）<br/>0.5V ~ 3.4V 25mV/step<br/>0001011：0.500 V<br/>0001100：0.525 V<br/>0001101：0.550 V<br/>...<br/>1111111：3.400 V<br/>others：0.5V</td>
</tr>
<tr>
<td>0</td>
<td>Reserved</td>
<td>RV</td>
<td>1</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-80 ALDOx\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x5B+3*N(1)</td>
<td>7:4</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>3:1</td>
<td>ALDOx_GPIO_SEL</td>
<td>RE</td>
<td>0x0</td>
<td>GPIO（PWRCTRL）控制ALDOx使能<br/>000： 不由GPIO控制<br/>001： GPIO0控制<br/>010： GPIO1控制<br/>011： GPIO2控制<br/>100： GPIO3控制<br/>101： GPIO4控制<br/>110： GPIO5控制<br/>111： 不由GPIO控制</td>
</tr>
<tr>
<td>0</td>
<td>ALDOx_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>ALDOx使能<br/>0：关闭<br/>1：使能</td>
</tr>
</tbody>
</table>

- N=0 ~ 3，x=1 ~ 4，依次对应 ALDO1 ~ ALDO4。

### 表 7-81 ALDOx\_VOLT

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x5C+3*N(1)</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6:0</td>
<td>ALDOx_VOLT</td>
<td>RWE</td>
<td>0x0</td>
<td>ALDOx电压输出档位（7 MSBs）<br/>0.5V～3.4V 25mV/step<br/>0001011：0.500 V<br/>0001100：0.525 V<br/>0001101：0.550 V<br/>...<br/>1111111：3.400 V<br/>others：0.5 V</td>
</tr>
</tbody>
</table>

- N=0 ~ 3，x=1 ~ 4，依次对应 ALDO1 ~ ALDO4。

### 表 7-82 ALDOx\_SLP\_VOLT

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x5D+3*N(1)</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6:0</td>
<td>ALDOx_SLP_VOLT</td>
<td>RWE</td>
<td>0x0</td>
<td>ALDOx睡眠电压输出档位（7 MSBs）<br/>0.5V ~ 3.4V 25mV/step<br/>0001011：0.500 V<br/>0001100：0.525 V<br/>0001101：0.550 V<br/>...<br/>1111111：3.400 V<br/>others：0.5 V</td>
</tr>
</tbody>
</table>

- N=0 ~ 3，x=1 ~ 4，依次对应 ALDO1 ~ ALDO4。

### 表 7-83 DLDOx\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=3 colspan=1>0x67+3*N(1)</td>
<td>7:4</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>3:1</td>
<td>DLDOx_GPIO_SEL</td>
<td>RE</td>
<td>0x0</td>
<td>GPIO（PWRCTRL）控制DLDOx使能<br/>000： 不由GPIO控制<br/>001： GPIO0控制<br/>010： GPIO1控制<br/>011： GPIO2控制<br/>100： GPIO3控制<br/>101： GPIO4控制<br/>110： GPIO5控制<br/>111： 不由GPIO控制</td>
</tr>
<tr>
<td>0</td>
<td>DLDOx_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>DLDOx使能<br/>0：关闭<br/>1：使能</td>
</tr>
</tbody>
</table>

- N=0 ~ 6，x=1 ~ 7，依次对应 DLDO1 ~ DLDO7。

### 表 7-84 DLDOx\_VOLT

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x68+3*N(1)</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6:0</td>
<td>DLDOx_VOLT</td>
<td>RWE</td>
<td>0x0</td>
<td>DLDOx电压输出档位（7 MSBs）<br/>0.5V～3.4V 25mV/step<br/>0001011：0.500 V<br/>0001100：0.525 V<br/>0001101：0.550 V<br/>...<br/>1111111：3.400 V<br/>others：0.5 V</td>
</tr>
</tbody>
</table>

- N=0 ~ 6，x=1 ~ 7，依次对应 DLDO1 ~ DLDO7。

### 表 7-85 DLDOx\_SLP\_VOLT

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x69+3*N(1)</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6:0</td>
<td>DLDOx_SLP_VOLT</td>
<td>RWE</td>
<td>0x0</td>
<td>DLDOx睡眠电压输出档位（7 MSBs）<br/>0.5V ~ 3.4V 25mV/step<br/>0001011：0.500 V<br/>0001100：0.525 V<br/>0001101：0.550 V<br/>...<br/>1111111：3.400 V<br/>others：0.5 V</td>
</tr>
</tbody>
</table>

- N=0 ~ 6，x=1 ~ 7，依次对应 DLDO1 ~ DLDO7。

### 表 7-86 PWR\_CTRL0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x7C</td>
<td>7</td>
<td>WDT_RST_EN</td>
<td>RW</td>
<td>0x0</td>
<td>WDT超时触发复位使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>6</td>
<td>NRESET_RST_EN</td>
<td>RW</td>
<td>0x0</td>
<td>nRESET引脚下拉触发复位功能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>5</td>
<td>PWRCTRL_SHUT_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>PWRCTRL全绑定无效关机使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>PWRCTRL_STA_EN</td>
<td>RE</td>
<td>0x0</td>
<td>PWRCTRL全绑定有效开机使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>RTC_STA_EN</td>
<td>RE</td>
<td>0x0</td>
<td>RTC TICK、ALARM触发开机使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>INT_STA_EN</td>
<td>RE</td>
<td>0x0</td>
<td>INT引脚触发开机使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>VSYS_STA_EN</td>
<td>RE</td>
<td>0x0</td>
<td>Vsys上升沿触发开机使能<br/>0：禁止<br/>1：使能<br/>该bit使能后，初次上电后，VSYS电压超过设定阈值即开机</td>
</tr>
<tr>
<td>0</td>
<td>Reserved</td>
<td>RV</td>
<td>1</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

### 表 7-87 PWR\_CTRL1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x7D</td>
<td>7</td>
<td>SD_LOW_POWER</td>
<td>RW</td>
<td>0x0</td>
<td>关机模式下（SHUTDOWN）是否进入standby模式：<br/>0：不进入<br/>1：进入<br/>standby模式下，PMIC内部Bangap和AONLDO关闭，此时只有PWRKY按键和RTC唤醒</td>
</tr>
<tr>
<td>6</td>
<td>PG_RST_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>PGOOD引脚下拉触发复位功能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>5</td>
<td>PG_PD_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>进入睡眠时，PGOOD引脚下拉使能<br/>0：睡眠事件触发时，PGOOD引脚不下拉<br/>1：睡眠事件触发时，PGOOD引脚下拉</td>
</tr>
<tr>
<td>4</td>
<td>PG_WAIT_TO</td>
<td>RWE</td>
<td>0x0</td>
<td>上电等待PGOOD外部释放超时档位选择<br/>0：128 ms<br/>1：1 s</td>
</tr>
<tr>
<td>3</td>
<td>PG_WAIT_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>PMIC上电流程完成并释放PGOOD后，是否等待PGOOD被外部释放<br/>0：不等待<br/>1：等待</td>
</tr>
<tr>
<td>2</td>
<td>AUTO_BOOT_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>关机事件触发关机后重启使能位<br/>0：关机后不重启<br/>1：关机后重启</td>
</tr>
<tr>
<td>1</td>
<td>SLP_WKUP_SEQ</td>
<td>RWE</td>
<td>0x0</td>
<td>睡眠/唤醒时序<br/>0：直接进入/退出睡眠<br/>1：按照关机/开机的时序进入/退出睡眠</td>
</tr>
<tr>
<td>0</td>
<td>SD_SEQ</td>
<td>RWE</td>
<td>0x0</td>
<td>关机时序<br/>0：反序关机<br/>1：快速关机</td>
</tr>
</tbody>
</table>

### 表 7-88 PWR\_CTRL2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x7E</td>
<td>7</td>
<td>SD_RST_TIME</td>
<td>RE</td>
<td>0x0</td>
<td>复位进入关机模式时停留时间选择<br/>0：200 ms<br/>1：1 s</td>
</tr>
<tr>
<td>6</td>
<td>PWRKY_SD_DIS</td>
<td>RWE</td>
<td>0x0</td>
<td>PWRKY按键关机功能屏蔽位<br/>0：开启PWRKY按键关机功能（此时PWRKY按键12s长按复位失效）<br/>1：禁止PWRKY按键关机功能（此时PWRKY按键12s长按复位使能）</td>
</tr>
<tr>
<td>5</td>
<td>PWRCTRL_SDTO_TIME</td>
<td>RWE</td>
<td>0x0</td>
<td>关机和睡眠时序等待PWRCTRL超时档位选择<br/>0：128 ms<br/>1：1 s</td>
</tr>
<tr>
<td>4</td>
<td>PWRCTRL_WAIT_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>关机和睡眠时序等待是否等待PWRCTRL<br/>0：不等待<br/>1：等待</td>
</tr>
<tr>
<td>3</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>2</td>
<td>SW_SD</td>
<td>RW</td>
<td>0x0</td>
<td>软件关机<br/>0：无操作<br/>1：触发软件关机（软件触发，硬件清零）</td>
</tr>
<tr>
<td>1</td>
<td>SW_RST</td>
<td>RW</td>
<td>0x0</td>
<td>软件复位<br/>0：无操作<br/>1：触发软件复位（软件触发，硬件清零）</td>
</tr>
<tr>
<td>0</td>
<td>SW_SLP_WKUP</td>
<td>RW</td>
<td>0x0</td>
<td>软件睡眠/唤醒<br/>开机模式下：<br/>0：无操作<br/>1：触发软件睡眠（软件触发，硬件清零）<br/>关机模式下：<br/>0：触发软件唤醒（软件触发，硬件清零）<br/>1：无操作</td>
</tr>
</tbody>
</table>

### 表 7-89 PWR\_STS0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=6 colspan=1>0x7F</td>
<td>7:5</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>4</td>
<td>FLAG_PWRCTRL_WKUP</td>
<td>R，IO</td>
<td>0x0</td>
<td>开机源指示位（软件写1清零）<br/>0：非PWRCTRL全绑定开机唤醒<br/>1：PWRCTRL全绑定开机唤醒</td>
</tr>
<tr>
<td>3</td>
<td>FLAG_PWRKY_WKUP</td>
<td>R，IO</td>
<td>0x0</td>
<td>开机源指示位（软件写1清零）<br/>0：非PWRKY长按唤醒<br/>1：PWRKY长按开机唤醒</td>
</tr>
<tr>
<td>2</td>
<td>FLAG_VSYS_WKUP</td>
<td>R，IO</td>
<td>0x0</td>
<td>开机源指示位（软件写1清零）<br/>0：非VSYS超阈值唤醒<br/>1：VSYS超阈值开机唤醒</td>
</tr>
<tr>
<td>1</td>
<td>FLAG_INT_WKUP</td>
<td>R，IO</td>
<td>0x0</td>
<td>开机源指示位（软件写1清零）<br/>0：非INT引脚唤醒<br/>1：INT引脚开机唤醒</td>
</tr>
<tr>
<td>0</td>
<td>FLAG_RTC_WKUP</td>
<td>R，IO</td>
<td>0x0</td>
<td>开机源指示位（软件写1清零）<br/>0：非RTC唤醒<br/>1：RTC开机唤醒</td>
</tr>
</tbody>
</table>

### 表 7-90 PWR\_STS1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x80</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>WORK_STS</td>
<td>R</td>
<td>0x0</td>
<td>工作模式状态指示位<br/>0：开机模式<br/>1：关机模式</td>
</tr>
<tr>
<td>4</td>
<td>FLAG_PWRCTRL_SHUT</td>
<td>R，IO</td>
<td>0x0</td>
<td>关机源指示位（软件写1清零）<br/>0：非PWRCTRL无效关机<br/>1：PWRCTRL无效关机</td>
</tr>
<tr>
<td>3</td>
<td>FLAG_PWRKY_SHUT</td>
<td>R，IO</td>
<td>0x0</td>
<td>关机源指示位（软件写1清零）<br/>0：非PWRKY长按关机 <br/>1：PWRKY长按关机</td>
</tr>
<tr>
<td>2</td>
<td>FLAG_VSYS_SHUT</td>
<td>R，IO</td>
<td>0x0</td>
<td>关机源指示位（软件写1清零）<br/>0：非VSYS低阈值<br/>1：VSYS低阈值关机</td>
</tr>
<tr>
<td>1</td>
<td>FLAG_ERR_SHUT</td>
<td>R，IO</td>
<td>0x0</td>
<td>关机源指示位（软件写1清零）<br/>0：非异常关机 <br/>1：异常关机<br/>异常事件包括：VSYS过压，芯片过温，所有buck的过压/欠压/短路，所有LDO的过压/欠压/短路。</td>
</tr>
<tr>
<td>0</td>
<td>FLAG_SW_SHUT</td>
<td>R，IO</td>
<td>0x0</td>
<td>关机源指示位（软件写1清零）<br/>0：非软件挂机 <br/>1：软件关机</td>
</tr>
</tbody>
</table>

### 表 7-91 PWR\_KEY\_TIME

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x81</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>PWRKY_INT_TIME</td>
<td>RWE</td>
<td>0x0</td>
<td>PWRKY按键短按中断时间<br/>00： 0.5 s<br/>01： 1 s<br/>10： 1.5 s<br/>11： 2 s</td>
</tr>
<tr>
<td>3:2</td>
<td>PWRKY_SD_TIME</td>
<td>RWE</td>
<td>0x0</td>
<td>PWRKY按键关机时间<br/>00： 4 s<br/>01： 6 s<br/>10： 8 s<br/>11： 10 s</td>
</tr>
<tr>
<td>1:0</td>
<td>PWRKY_STA_TIME</td>
<td>RWE</td>
<td>0x0</td>
<td>PWRKY按键开机时间<br/>00： 0.5 s<br/>01： 1 s<br/>10： 2 s<br/>11： 3 s</td>
</tr>
</tbody>
</table>

### 表 7-92 PWR\_SEQ\_TIME

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0x82</td>
<td>7:6</td>
<td>PDN_SEQ_PG_DLY</td>
<td>RWE</td>
<td>0x0</td>
<td>PGOOD下拉到各路电源轨开始掉电的时间间隔<br/>00：4 ms<br/>01：16 ms<br/>10：64 ms<br/>11：128 ms</td>
</tr>
<tr>
<td>5:4</td>
<td>PUP_SEQ_PG_DLY</td>
<td>RWE</td>
<td>0x0</td>
<td>所有电源轨启动完成后与PGOOD信号释放的间隔时间<br/>00：4 ms<br/>01：16 ms<br/>10：64 ms<br/>11：128 ms</td>
</tr>
<tr>
<td>3:2</td>
<td>PDN_SEQ_SLOT_TIME</td>
<td>RWE</td>
<td>0x0</td>
<td>各路电源轨掉电间隔时间<br/>00：1 ms<br/>01：4 ms<br/>10：8 ms<br/>11：16 ms</td>
</tr>
<tr>
<td>1:0</td>
<td>PUP_SEQ_SLOT_TIME</td>
<td>RWE</td>
<td>0x0</td>
<td>各路电源轨上电间隔时间<br/>00：1 ms<br/>01：4 ms<br/>10：8 ms<br/>11：16 ms</td>
</tr>
</tbody>
</table>

### 表 7-93 PWR\_SLOT0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x83</td>
<td>7:4</td>
<td>BUCK2_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>BUCK2上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>BUCK1_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>BUCK1上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-94 PWR\_SLOT1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x84</td>
<td>7:4</td>
<td>BUCK4_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>BUCK4上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>BUCK3_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>BUCK3上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-95 PWR\_SLOT2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x85</td>
<td>7:4</td>
<td>BUCK6_SLOT<br/></td>
<td>RE</td>
<td>0x0</td>
<td>BUCK6上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>BUCK5_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>BUCK5上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-96 PWR\_SLOT3

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x86</td>
<td>7:4</td>
<td>ALDO2_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>ALDO2上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>ALDO1_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>ALDO1上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-97 PWR\_SLOT4

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x87</td>
<td>7:4</td>
<td>ALDO4_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>ALDO4上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>ALDO3_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>ALDO3上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-98 PWR\_SLOT5

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x88</td>
<td>7:4</td>
<td>DLDO2_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>DLDO2上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>DLDO1_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>DLDO1上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-99 PWR\_SLOT6

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x89</td>
<td>7:4</td>
<td>DLDO4_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>DLDO4上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>DLDO3_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>DLDO3上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-100 PWR\_SLOT7

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x8A</td>
<td>7:4<br/></td>
<td>DLDO6_SLOT<br/></td>
<td>RE</td>
<td>0x0</td>
<td>DLDO6上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>DLDO5_SLOT<br/></td>
<td>RE</td>
<td>0x0</td>
<td>DLDO5上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-101 PWR\_SLOT8

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x8B</td>
<td>7:4</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>3:0</td>
<td>DLDO7_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>DLDO7上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-102 PWR\_SLOT9

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x8C</td>
<td>7:4</td>
<td>EXT1_EN_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>EXT1上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>EXT0_EN_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>EXT0上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-103 PWR\_SLOT10

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x8D</td>
<td>7:4</td>
<td>EXT3_EN_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>EXT3上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>EXT2_EN_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>EXT2上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-104 PWR\_SLOT11

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0x8E</td>
<td>7:4</td>
<td>EXT5_EN_SLOT<br/></td>
<td>RE</td>
<td>0x0</td>
<td>EXT5上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
<tr>
<td>3:0</td>
<td>EXT4_EN_SLOT</td>
<td>RE</td>
<td>0x0</td>
<td>EXT4上电掉电时序槽<br/>0000： 第1个时序槽<br/>0001： 第2个时序槽<br/>. . .<br/>1101： 第14个时序槽<br/>1110： 第15个时序槽<br/>1111： 不参与上下电流程</td>
</tr>
</tbody>
</table>

### 表 7-105 PWR\_EXT\_EN

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x8F</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>EXT5_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN5软件使能位<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>EXT4_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN4软件使能位<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>EXT3_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN3软件使能位<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>EXT2_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN2软件使能位<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>EXT1_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN1软件使能位<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>EXT0_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN0软件使能位<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-106 PWR\_EXT\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x90</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>EXT5_SLP_SD</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN5是否在睡眠模式和睡眠流程关闭<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>EXT4_SLP_SD</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN4是否在睡眠模式和睡眠流程关闭<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>EXT3_SLP_SD</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN3是否在睡眠模式和睡眠流程关闭<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>EXT2_SLP_SD</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN2是否在睡眠模式和睡眠流程关闭<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>EXT1_SLP_SD</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN1是否在睡眠模式和睡眠流程关闭<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>EXT0_SLP_SD</td>
<td>RWE</td>
<td>0x0</td>
<td>EXT_EN0是否在睡眠模式和睡眠流程关闭<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-107 EVENT0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x91</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>E_GPI5</td>
<td>R，IO</td>
<td>0x0</td>
<td>根据有效电平设置，产生GPI5输入有效事件或ADCIN5超/低阈值事件<br/>0：无事件发生<br/>1：有事件发生（软件写1清零）</td>
</tr>
<tr>
<td>4</td>
<td>E_GPI4</td>
<td>R，IO</td>
<td>0x0</td>
<td>根据有效电平设置，产生GPI4输入有效事件或ADCIN4超/低阈值事件<br/>0：无事件发生<br/>1：有事件发生（软件写1清零）</td>
</tr>
<tr>
<td>3</td>
<td>E_GPI3</td>
<td>R，IO</td>
<td>0x0</td>
<td>根据有效电平设置，产生GPI3输入有效事件或ADCIN3超/低阈值事件<br/>0：无事件发生<br/>1：有事件发生（软件写1清零）</td>
</tr>
<tr>
<td>2</td>
<td>E_GPI2</td>
<td>R，IO</td>
<td>0x0</td>
<td>根据有效电平设置，产生GPI2输入有效事件或ADCIN2超/低阈值事件<br/>0：无事件发生<br/>1：有事件发生（软件写1清零）</td>
</tr>
<tr>
<td>1</td>
<td>E_GPI1</td>
<td>R，IO</td>
<td>0x0</td>
<td>根据有效电平设置，产生GPI1输入有效事件或ADCIN1超/低阈值事件<br/>0：无事件发生<br/>1：有事件发生（软件写1清零）</td>
</tr>
<tr>
<td>0</td>
<td>E_GPI0</td>
<td>R，IO</td>
<td>0x0</td>
<td>根据有效电平设置，产生GPI0输入有效事件或ADCIN0超/低阈值事件<br/>0：无事件发生<br/>1：有事件发生（软件写1清零）</td>
</tr>
</tbody>
</table>

### 表 7-108 EVENT1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x92<br/></td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>E_TICK</td>
<td>R，IO<br/></td>
<td>0x0</td>
<td>RTC TICK事件<br/>0：RTC闹钟未达设定值<br/>1：RTC闹钟已达设定值，并按照设定周期触发该事件<br/>软件写1清零，但下一周期tick事件仍会置起该bit，关闭周期tick事件需清零TICK_EN。</td>
</tr>
<tr>
<td>4</td>
<td>E_ALARM</td>
<td>R，IO</td>
<td>0x0</td>
<td>RTC闹钟事件<br/>0：RTC闹钟未达设定值<br/>1：RTC闹钟已达设定值（软件写1清零）</td>
</tr>
<tr>
<td>3</td>
<td>E_WDT_TO</td>
<td>R，IO</td>
<td>0x0</td>
<td>看门狗超时事件<br/>0：看门狗未超时<br/>1：看门狗超时（软件写1清零）</td>
</tr>
<tr>
<td>2</td>
<td>E_ADC_EOS</td>
<td>R，IO</td>
<td>0x0</td>
<td>ADC自动模式序列转换完成事件<br/>0：未完成一次序列转换<br/>1：已完成一次序列转换（软件写1清零）</td>
</tr>
<tr>
<td>1</td>
<td>E_ADC_EOC</td>
<td>R，IO</td>
<td>0x0</td>
<td>ADC转换完成事件<br/>0：未转换完成<br/>1：已转换完成一次（软件写1清零）</td>
</tr>
<tr>
<td>0</td>
<td>E_ADC_TEMP</td>
<td>R，IO</td>
<td>0x0</td>
<td>ADC通道1（Junction结温）超/低阈值事件<br/>0：无过温事件发生<br/>1：ADC通道1超/低阈值事件（软件写1清零）</td>
</tr>
</tbody>
</table>

### 表 7-109 EVENT2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x93</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6</td>
<td>E_TEMP_CRIT</td>
<td>R，IO</td>
<td>0x0</td>
<td>芯片触发关机过温报警事件<br/>0：未发生关机过温报警<br/>1：已发生关机过温报警（软件写1清零）</td>
</tr>
<tr>
<td>5</td>
<td>E_TEMP_SEVERE</td>
<td>R，IO</td>
<td>0x0</td>
<td>芯片严重过温报警事件<br/>0：未发生严重过温报警<br/>1：已发生严重过温报警（软件写1清零）</td>
</tr>
<tr>
<td>4</td>
<td>E_TEMP_WARN</td>
<td>R，IO</td>
<td>0x0</td>
<td>芯片过温报警事件<br/>0：未发生过温报警<br/>1：已发生过温报警（软件写1清零）</td>
</tr>
<tr>
<td>3</td>
<td>E_SW_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>SWITCH短路事件<br/>0：未发生短路/开路<br/>1：SWITCH发生了短路（软件写1清零）</td>
</tr>
<tr>
<td>2</td>
<td>E_LDO_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>LDO短路/开路事件<br/>0：未发生短路/开路<br/>1：任意一个LDO发生了短路/开路（软件写1清零）</td>
</tr>
<tr>
<td>1</td>
<td>E_LDO_UV</td>
<td>R，IO</td>
<td>0x0</td>
<td>LDO欠压事件<br/>0：未发生欠压<br/>1：任意一个LDO发生了欠压（软件写1清零）</td>
</tr>
<tr>
<td>0</td>
<td>E_LDO_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>LDO过压事件<br/>0：未发生过压<br/>1：任意一个LDO发生了过压（软件写1清零）</td>
</tr>
</tbody>
</table>

### 表 7-110 BUCK\_EVNET0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x94</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>E_BUCK6_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK6过压事件<br/>0：BUCK6未发生过压<br/>1：BUCK6发生过压</td>
</tr>
<tr>
<td>4</td>
<td>E_BUCK5_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK5过压事件<br/>0：BUCK5未发生过压<br/>1：BUCK5发生过压</td>
</tr>
<tr>
<td>3</td>
<td>E_BUCK4_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK4过压事件<br/>0：BUCK4未发生过压<br/>1：BUCK4发生过压</td>
</tr>
<tr>
<td>2</td>
<td>E_BUCK3_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK3过压事件<br/>0：BUCK3未发生过压<br/>1：BUCK3发生过压</td>
</tr>
<tr>
<td>1</td>
<td>E_BUCK2_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK2过压事件<br/>0：BUCK2未发生过压<br/>1：BUCK2发生过压</td>
</tr>
<tr>
<td>0</td>
<td>E_BUCK1_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK1过压事件<br/>0：BUCK1未发生过压<br/>1：BUCK1发生过压</td>
</tr>
</tbody>
</table>

### 表 7-111 BUCK\_EVNET1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x95</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>E_BUCK6_UV<br/></td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK6欠压事件<br/>0：BUCK6未发生欠压<br/>1：BUCK6发生欠压</td>
</tr>
<tr>
<td>4</td>
<td>E_BUCK5_UV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK5欠压事件<br/>0：BUCK5未发生欠压<br/>1：BUCK5发生欠压</td>
</tr>
<tr>
<td>3</td>
<td>E_BUCK4_UV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK4欠压事件<br/>0：BUCK4未发生欠压<br/>1：BUCK4发生欠压</td>
</tr>
<tr>
<td>2</td>
<td>E_BUCK3_UV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK3欠压事件<br/>0：BUCK3未发生欠压<br/>1：BUCK3发生欠压</td>
</tr>
<tr>
<td>1</td>
<td>E_BUCK2_UV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK2欠压事件<br/>0：BUCK2未发生欠压<br/>1：BUCK2发生欠压</td>
</tr>
<tr>
<td>0</td>
<td>E_BUCK1_UV</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK1欠压事件<br/>0：BUCK1未发生欠压<br/>1：BUCK1发生欠压</td>
</tr>
</tbody>
</table>

### 表 7-112 BUCK\_EVNET2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x96</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>E_BUCK6_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK6短路/开路事件<br/>0：BUCK6未发生短路/开路<br/>1：BUCK6发生短路/开路</td>
</tr>
<tr>
<td>4</td>
<td>E_BUCK5_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK5短路/开路事件<br/>0：BUCK5未发生短路/开路<br/>1：BUCK5发生短路/开路</td>
</tr>
<tr>
<td>3</td>
<td>E_BUCK4_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK4短路/开路事件<br/>0：BUCK4未发生短路/开路<br/>1：BUCK4发生短路/开路</td>
</tr>
<tr>
<td>2</td>
<td>E_BUCK3_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK3短路/开路事件<br/>0：BUCK3未发生短路/开路<br/>1：BUCK3发生短路/开路</td>
</tr>
<tr>
<td>1</td>
<td>E_BUCK2_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK2短路/开路事件<br/>0：BUCK2未发生短路/开路<br/>1：BUCK2发生短路/开路</td>
</tr>
<tr>
<td>0</td>
<td>E_BUCK1_SC</td>
<td>R，IO</td>
<td>0x0</td>
<td>BUCK1短路/开路事件<br/>0：BUCK1未发生短路/开路<br/>1：BUCK1发生短路/开路</td>
</tr>
</tbody>
</table>

### 表 7-113 PWRKY\_EVNET

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x97</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>E_VSYS_OV</td>
<td>R，IO</td>
<td>0x0</td>
<td>VSYS过压事件<br/>0：VSYS未过压<br/>1：VSYS过压（VSYS &gt; 5.9 V）</td>
</tr>
<tr>
<td>4</td>
<td>E_PWRKY_SDINTR</td>
<td>R，IO</td>
<td>0x0</td>
<td>PRWKY关机事件<br/>0：按键未检测到关机事件<br/>1：按键检测到关机事件</td>
</tr>
<tr>
<td>3</td>
<td>E_PWRKY_LINTR</td>
<td>R，IO</td>
<td>0x0</td>
<td>PRWKY按键长按事件<br/>0：按键未检测到长按<br/>1：按键检测到长按</td>
</tr>
<tr>
<td>2</td>
<td>E_PWRKY_SINTR</td>
<td>R，IO</td>
<td>0x0</td>
<td>PRWKY按键短按事件<br/>0：按键未检测到短按<br/>1：按键检测到短按</td>
</tr>
<tr>
<td>1</td>
<td>E_PWRKY_FINTR</td>
<td>R，IO</td>
<td>0x0</td>
<td>PRWKY按键下降沿事件<br/>0：按键未检测到下降沿<br/>1：按键检测到下降沿</td>
</tr>
<tr>
<td>0</td>
<td>E_PWRKY_RINTR</td>
<td>R，IO</td>
<td>0x0</td>
<td>PRWKY按键上升沿事件<br/>0：按键未检测到上升沿<br/>1：按键检测到上升沿</td>
</tr>
</tbody>
</table>

### 表 7-114 IRQ\_EN0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x98</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>IRQ_EN_GPI5</td>
<td>RW</td>
<td>0x0</td>
<td>E_GPI5事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>IRQ_EN_GPI4</td>
<td>RW</td>
<td>0x0</td>
<td>E_GPI4事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>IRQ_EN_GPI3</td>
<td>RW</td>
<td>0x0</td>
<td>E_GPI3事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>IRQ_EN_GPI2</td>
<td>RW</td>
<td>0x0</td>
<td>E_GPI2事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>IRQ_EN_GPI1</td>
<td>RW</td>
<td>0x0</td>
<td>E_GPI1事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>IRQ_EN_GPI0</td>
<td>RW</td>
<td>0x0</td>
<td>E_GPI0事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-115 IRQ\_EN1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x99</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>IRQ_EN_TICK</td>
<td>RW</td>
<td>0x0</td>
<td>E_TICK事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>IRQ_EN_ALARM</td>
<td>RW</td>
<td>0x0</td>
<td>E_ALARM事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>IRQ_EN_WDT_TO</td>
<td>RW</td>
<td>0x0</td>
<td>E_WDT_TO事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>IRQ_EN_ADC_EOS</td>
<td>RW</td>
<td>0x0</td>
<td>E_ADC_EOS事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>IRQ_EN_ADC_EOC</td>
<td>RW</td>
<td>0x0</td>
<td>E_ADC_EOC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>IRQ_EN_ADC_TEMP</td>
<td>RW</td>
<td>0x0</td>
<td>E_ADC_TEMP事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-116 IRQ\_EN2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x9A</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6</td>
<td>IRQ_EN_TEMP_CRIT<br/></td>
<td>RW</td>
<td>0x0</td>
<td>E_TEMP_CRIT事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>5</td>
<td>IRQ_EN_TEMP_SEVERE</td>
<td>RW</td>
<td>0x0</td>
<td>E_TEMP_SEVERE事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>IRQ_EN_TEMP_WARN</td>
<td>RW</td>
<td>0x0</td>
<td>E_TEMP_WARN事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>IRQ_EN_SW_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_SW_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>IRQ_EN_LDO_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_LDO_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>IRQ_EN_LDO_UV</td>
<td>RW</td>
<td>0x0</td>
<td>E_LDO_UV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>IRQ_EN_LDO_OV</td>
<td>RW</td>
<td>0x0</td>
<td>E_LDO_OV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-117 IRQ\_BUCK\_EN0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x9B</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>IRQ_EN_BUCK6_OV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK6_OV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>IRQ_EN_BUCK5_OV</td>
<td>RW</td>
<td>0x0<br/></td>
<td>E_BUCK5_OV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>IRQ_EN_BUCK4_OV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK4_OV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>IRQ_EN_BUCK3_OV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK3_OV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>IRQ_EN_BUCK2_OV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK2_OV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>IRQ_EN_BUCK1_OV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK1_OV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-118 IRQ\_BUCK\_EN1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x9C</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>IRQ_EN_BUCK6_UV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK6_UV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>IRQ_EN_BUCK5_UV</td>
<td>RW</td>
<td>0x0<br/></td>
<td>E_BUCK5_UV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>IRQ_EN_BUCK4_UV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK4_UV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>IRQ_EN_BUCK3_UV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK3_UV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>IRQ_EN_BUCK2_UV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK2_UV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>IRQ_EN_BUCK1_UV</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK1_UV事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-119 IRQ\_BUCK\_EN1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=7 colspan=1>0x9D</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5</td>
<td>IRQ_EN_BUCK6_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK6_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>IRQ_EN_BUCK5_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK5_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>IRQ_EN_BUCK4_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK4_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>IRQ_EN_BUCK3_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK3_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>IRQ_EN_BUCK2_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK2_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>IRQ_EN_BUCK1_SC</td>
<td>RW</td>
<td>0x0</td>
<td>E_BUCK1_SC事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-120 IRQ\_PWRKY\_EN

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x9E</td>
<td>7</td>
<td>VSYS_OVP_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>VSYS过压（5.9V）关机保护使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>6</td>
<td>TEMP_CRIT_PROT</td>
<td>RWE</td>
<td>0x0</td>
<td>过温（135℃/150℃）关机保护使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>5</td>
<td>IRQ_EN_VSYS_OV</td>
<td>RW</td>
<td>0x0</td>
<td>VSYS过压事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>4</td>
<td>IRQ_EN_PWRKY_SDINTR</td>
<td>RW</td>
<td>0x0</td>
<td>E_PWRKY_SDINTR事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>3</td>
<td>IRQ_EN_PWRKY_LINTR</td>
<td>RW</td>
<td>0x0</td>
<td>E_PWRKY_LINTR事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>2</td>
<td>IRQ_EN_PWRKY_SINTR</td>
<td>RW</td>
<td>0x0</td>
<td>E_PWRKY_SINTR事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>IRQ_EN_PWRKY_FINTR</td>
<td>RW</td>
<td>0x0</td>
<td>E_PWRKY_FINTR事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>IRQ_EN_PWRKY_RINTR</td>
<td>RW</td>
<td>0x0</td>
<td>E_PWRKY_RINTR事件中断使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>

### 表 7-121 PROT\_EN

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=8 colspan=1>0x9F</td>
<td>7</td>
<td>SW_SCP_DIS<br/></td>
<td>RWE<br/></td>
<td>0x0</td>
<td>Switch短路保护禁止<br/>0： 使能<br/>1： 禁止</td>
</tr>
<tr>
<td>6</td>
<td>TEMP_SEVERE_PROT</td>
<td>RWE</td>
<td>0x0</td>
<td>严重过温保护功能（进行关机保护）<br/>0： 禁止严重过温保护<br/>1： 使能严重过温保护</td>
</tr>
<tr>
<td>5</td>
<td>BUCK_SCP_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>任一BUCK短路/开路保护（进行关机保护）<br/>0： 禁止保护<br/>1： 使能保护</td>
</tr>
<tr>
<td>4</td>
<td>BUCK_UVP_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>任一BUCK输出欠压保护（进行关机保护）<br/>0： 禁止保护<br/>1： 使能保护</td>
</tr>
<tr>
<td>3</td>
<td>BUCK_OVP_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>任一BUCK输出过压保护（进行关机保护）<br/>0： 禁止保护<br/>1： 使能保护</td>
</tr>
<tr>
<td>2</td>
<td>LDO_SCP_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>任一LDO输出短路/开路保护（进行关机保护）<br/>0： 禁止保护<br/>1： 使能保护</td>
</tr>
<tr>
<td>1</td>
<td>LDO_UVP_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>任一LDO输出过压保护（进行关机保护）<br/>0： 禁止保护<br/>1： 使能保护</td>
</tr>
<tr>
<td>0</td>
<td>LDO_OVP_EN</td>
<td>RWE</td>
<td>0x0</td>
<td>任一LDO过流、短路保护（进行关机保护）<br/>0： 禁止保护<br/>1： 使能保护</td>
</tr>
</tbody>
</table>

### 表 7-122 DEVICE\_ID

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0xA0</td>
<td>7:0</td>
<td>DEVICE_ID</td>
<td>RE</td>
<td>0x00</td>
<td>设备ID号</td>
</tr>
</tbody>
</table>

### 表 7-123 VERSION\_ID

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0xA1</td>
<td>7:0</td>
<td>VERSION_ID</td>
<td>RE</td>
<td>0x00</td>
<td>版本ID号</td>
</tr>
</tbody>
</table>

### 表 7-124 CUSTOMER\_ID

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0xA2</td>
<td>7:0</td>
<td>CUSTOMER_ID</td>
<td>RE</td>
<td>0x00</td>
<td>用户ID号</td>
</tr>
</tbody>
</table>

### 表 7-125 SYS\_CFG0

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0xA3</td>
<td>7</td>
<td>TEMP_LEVEL</td>
<td>RE</td>
<td>0x0</td>
<td>温度档位选择<br/>温度报警（warn） 严重过温（severe）   关机过温（critical）<br/>0：   95 ℃            115 ℃                    135℃<br/>1：  110 ℃            130 ℃                    150℃</td>
</tr>
<tr>
<td>6:0</td>
<td>IF_ADDR</td>
<td>RE</td>
<td>0x55</td>
<td>IIC从机地址配置</td>
</tr>
</tbody>
</table>

### 表 7-126 SYS\_CFG1

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0xA4</td>
<td>7:5</td>
<td>VSYS_STA_VTH</td>
<td>RE</td>
<td>0x0</td>
<td>开机阈值<br/>000：Vsys&gt;2.9V，启动开机流程<br/>001：Vsys&gt;3.0V，启动开机流程<br/>010：Vsys&gt;3.1V，启动开机流程<br/>011：Vsys&gt;3.2V，启动开机流程<br/>100：Vsys&gt;3.3V，启动开机流程<br/>101：Vsys&gt;3.4V，启动开机流程<br/>110：Vsys&gt;3.5V，启动开机流程<br/>111：Vsys&gt;3.6V，启动开机流程</td>
</tr>
<tr>
<td>4:2</td>
<td>VSYS_SHUT_VTH</td>
<td>RE</td>
<td>0x0</td>
<td>关机阈值<br/>000：Vsys&lt;2.6V，启动关机流程<br/>001：Vsys&lt;2.7V，启动关机流程<br/>010：Vsys&lt;2.8V，启动关机流程<br/>011：Vsys&lt;2.9V，启动关机流程<br/>100：Vsys&lt;3.0V，启动关机流程<br/>101：Vsys&lt;3.1V，启动关机流程<br/>110：Vsys&lt;3.2V，启动关机流程<br/>111：Vsys&lt;3.3V，启动关机流程</td>
</tr>
<tr>
<td>1</td>
<td>KEY_RST_EN</td>
<td>RE</td>
<td>0x0</td>
<td>关机模式下长按PWRKY按键触发开机后，继续长按是否触发复位<br/>0：不触发<br/>1：触发（当PWRKY_SD_DIS=1）</td>
</tr>
<tr>
<td>0</td>
<td>KEY_SD_EN</td>
<td>RE</td>
<td>0x0</td>
<td>关机模式下长按PWRKY按键触发开机后，继续长按是否触发关机<br/>0：不触发<br/>1：触发（当PWRKY_SD_DIS=0）</td>
</tr>
</tbody>
</table>

### 表 7-127 SYS\_CFG2

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=5 colspan=1>0xA5</td>
<td>7</td>
<td>VSYS_STEP</td>
<td>RE<br/></td>
<td>0x0</td>
<td>热插拔开机阈值提升步幅<br/>0：0.1 V<br/>1：0.2 V</td>
</tr>
<tr>
<td>6</td>
<td>HOT_SWAP_DIS</td>
<td>RE</td>
<td>0x0</td>
<td>热插拔抬高开机阈值控制<br/>0：使能<br/>1：禁止<br/>禁止后，当发生热插拔后，开机阈值不会提高</td>
</tr>
<tr>
<td>5</td>
<td>EVENT_DELAY</td>
<td>RE</td>
<td>0x0</td>
<td>过温，vsys过压，buck和ldo短路事件滤波<br/>0：100 us<br/>1：disable</td>
</tr>
<tr>
<td>4:3</td>
<td>OVUV_DELAY</td>
<td>RE</td>
<td>0x0</td>
<td>异常事件（buck和ldo的uv，ov）滤波时间<br/>00：100 us<br/>01：375 us<br/>10：750 us<br/>11: disable this function</td>
</tr>
<tr>
<td>2:0</td>
<td>OVUV_MASK_DELAY</td>
<td>RE</td>
<td>0x0</td>
<td>BUCK和LDO的过压欠压事件屏蔽时间<br/>000：125 us<br/>001：250 us<br/>010：1 ms<br/>011：8 ms<br/>100：64 ms<br/>101：256 ms<br/>110：512 ms<br/>111: disable this function<br/>BUCK和LDO开启时，或者BUCK和LDO电压发生改变时，在UVOV_MASK_DELAY的时间内，将屏蔽BUCK和LDO的过压欠压事件</td>
</tr>
</tbody>
</table>

### 表 7-128 MTP\_KEY

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0xA6</td>
<td>7:0</td>
<td>MTP_KEY</td>
<td>RW</td>
<td>0x00</td>
<td>MTP寄存器（MTP_ADDR，MTP_DATA，MTP_CFG，MTP_CTRL）解锁。<br/>解锁操作为：向该寄存器写0xAA。<br/>解锁后该寄存器读出为0x1。</td>
</tr>
</tbody>
</table>

### 表 7-129 MTP\_ADDR

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=2 colspan=1>0xA7</td>
<td>7</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>6:0</td>
<td>MTP_ADDR</td>
<td>RW，P</td>
<td>0x0</td>
<td>MTP地址寄存器（读，编程，擦除）</td>
</tr>
</tbody>
</table>

### 表 7-130 MTP\_DATA

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td>0xA8</td>
<td>7:0</td>
<td>MTP_DATA</td>
<td>RW，P</td>
<td>0x0</td>
<td>MTP数据寄存器（读取数据存放在此寄存器，编程前将数据提前准备在此寄存器）</td>
</tr>
</tbody>
</table>

### 表 7-131 MTP\_CFG

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=5 colspan=1>0xA9</td>
<td>7:6</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>5:4</td>
<td>MTP_PG_TIME_SEL</td>
<td>RW，P</td>
<td>0x0</td>
<td>MTP编程时间选择<br/>00：30 us<br/>01：20 us<br/>1x：40 us</td>
</tr>
<tr>
<td>3</td>
<td>MTP_PDN</td>
<td>RW，P</td>
<td>0x0</td>
<td>MTP低功耗模式选择<br/>0：关闭MTP<br/>1：打开MTP<br/>MTP的读操作，编程和擦除操作都需将此位置1</td>
</tr>
<tr>
<td>2:1</td>
<td>MTP_TRIM</td>
<td>RW，P</td>
<td>0x2</td>
<td>配置MTP内部的电源模块的输出电压值<br/>01： 用于编程和擦除<br/>10：用于MTP读</td>
</tr>
<tr>
<td>0</td>
<td>MTP_VRFCG_SEL</td>
<td>RW，P</td>
<td>0x1</td>
<td>配置MTP内部CG电压<br/>0：CG = 0<br/>1：CG = 1.2 V</td>
</tr>
</tbody>
</table>

### 表 7-132 MTP\_CTRL

<table>
<tbody>
<tr>
<td>Addr</td>
<td>Bits</td>
<td>Field Name</td>
<td>Attr</td>
<td>Default</td>
<td>Description</td>
</tr>
<tr>
<td rowspan=4 colspan=1>0xAA</td>
<td>7:3</td>
<td>Reserved</td>
<td>RV</td>
<td>0</td>
<td>Reserved</td>
</tr>
<tr>
<td>2</td>
<td>MTP_ER</td>
<td>RW，P</td>
<td>0x0</td>
<td>MTP擦除使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>1</td>
<td>MTP_PG</td>
<td>RW，P</td>
<td>0x0</td>
<td>MTP编程使能<br/>0：禁止<br/>1：使能</td>
</tr>
<tr>
<td>0</td>
<td>MTP_RD</td>
<td>RW，P</td>
<td>0x0</td>
<td>MTP读使能<br/>0：禁止<br/>1：使能</td>
</tr>
</tbody>
</table>
