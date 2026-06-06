## EtherCAT Task Introduction

### Super Capacitor

#### Hardware preparation

Connect your capacitor controller board to any ``CAN`` port of your EtherCAT module.

> **Note:** the capacitor will be disabled before receiving any command.

CAN message definition as follows:

```c
struct ReportPacket {
    uint8_t cap_valid;
    uint8_t cap_status;
    uint8_t cap_remain_percentage;
    uint8_t chassis_power;
    uint8_t battery_volt;
    uint8_t chassis_only_power;
};

struct ControlPacket {
    uint8_t cap_enable;
    uint8_t do_charge;
    uint8_t max_charge_power;
    uint8_t allow_charge_power;
};
```

#### Configuration items

* CAN
    * The CAN port you connected to.
* Capacitor Control Packet ID
    * The packet id of control packet (bot → cap)
* Capacitor Report Packet ID
    * The packet id of report packet (cap → bot)

You can change the publisher topic name by inputting a new name in the ``Capacitor Feedback Publisher Topic Name`` input
box.

You can change the subscriber topic name by inputting a new name in the ``Capacitor Command Subscriber Topic Name`` input
box.

#### Related ROS2 Message Types

```c
/* Message type: custom_msgs/msg/ReadSuperCap */
std_msgs/Header header

uint8 online      // 0 or 1

uint8 cap_valid   // 0 or 1
// UNKNOWN = 255
// DISCHARGE = 0
// CHARGE = 1
// WAIT = 2
// SOFT_START_PROTECTION = 3
// OCP_PROTECTION = 4
// OVP_BAT_PROTECTION = 5
// UVP_BAT_PROTECTION = 6
// UVP_CAP_PROTECTION = 7
// OTP_PROTECTION = 8
uint8 cap_status
uint8 cap_remain_percentage // [0, 100]
uint8 chassis_power         // [0, 250], total power from the bat port
uint8 battery_voltage       
uint8 chassis_only_power    // total power - cap charge power (i.e. the power of chassis port)
```

```c
/* Message type: custom_msgs/msg/WriteSuperCap */

uint8 cap_enable          // 0 or 1
uint8 do_charge           // 0 or 1
uint8 max_charge_power    // max power draw limit from the bat port
uint8 allow_charge_power  // max capicator charge power
```