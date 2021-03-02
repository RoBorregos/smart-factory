// Auto-generated. Do not edit!

// (in-package occupancy_grid_utils.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let nav_msgs = _finder('nav_msgs');

//-----------------------------------------------------------

class NavigationFunction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.info = null;
      this.source = null;
      this.valid = null;
      this.back_pointers = null;
      this.potential = null;
    }
    else {
      if (initObj.hasOwnProperty('info')) {
        this.info = initObj.info
      }
      else {
        this.info = new nav_msgs.msg.MapMetaData();
      }
      if (initObj.hasOwnProperty('source')) {
        this.source = initObj.source
      }
      else {
        this.source = 0;
      }
      if (initObj.hasOwnProperty('valid')) {
        this.valid = initObj.valid
      }
      else {
        this.valid = [];
      }
      if (initObj.hasOwnProperty('back_pointers')) {
        this.back_pointers = initObj.back_pointers
      }
      else {
        this.back_pointers = [];
      }
      if (initObj.hasOwnProperty('potential')) {
        this.potential = initObj.potential
      }
      else {
        this.potential = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NavigationFunction
    // Serialize message field [info]
    bufferOffset = nav_msgs.msg.MapMetaData.serialize(obj.info, buffer, bufferOffset);
    // Serialize message field [source]
    bufferOffset = _serializer.uint32(obj.source, buffer, bufferOffset);
    // Serialize message field [valid]
    bufferOffset = _arraySerializer.bool(obj.valid, buffer, bufferOffset, null);
    // Serialize message field [back_pointers]
    bufferOffset = _arraySerializer.uint32(obj.back_pointers, buffer, bufferOffset, null);
    // Serialize message field [potential]
    bufferOffset = _arraySerializer.float32(obj.potential, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NavigationFunction
    let len;
    let data = new NavigationFunction(null);
    // Deserialize message field [info]
    data.info = nav_msgs.msg.MapMetaData.deserialize(buffer, bufferOffset);
    // Deserialize message field [source]
    data.source = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [valid]
    data.valid = _arrayDeserializer.bool(buffer, bufferOffset, null)
    // Deserialize message field [back_pointers]
    data.back_pointers = _arrayDeserializer.uint32(buffer, bufferOffset, null)
    // Deserialize message field [potential]
    data.potential = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.valid.length;
    length += 4 * object.back_pointers.length;
    length += 4 * object.potential.length;
    return length + 92;
  }

  static datatype() {
    // Returns string type for a message object
    return 'occupancy_grid_utils/NavigationFunction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c75461ff4f50ec30d6191b0a4430e7ee';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    nav_msgs/MapMetaData info
    uint32 source
    bool[] valid
    uint32[] back_pointers
    float32[] potential
    ================================================================================
    MSG: nav_msgs/MapMetaData
    # This hold basic information about the characterists of the OccupancyGrid
    
    # The time at which the map was loaded
    time map_load_time
    # The map resolution [m/cell]
    float32 resolution
    # Map width [cells]
    uint32 width
    # Map height [cells]
    uint32 height
    # The origin of the map [m, m, rad].  This is the real-world pose of the
    # cell (0,0) in the map.
    geometry_msgs/Pose origin
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NavigationFunction(null);
    if (msg.info !== undefined) {
      resolved.info = nav_msgs.msg.MapMetaData.Resolve(msg.info)
    }
    else {
      resolved.info = new nav_msgs.msg.MapMetaData()
    }

    if (msg.source !== undefined) {
      resolved.source = msg.source;
    }
    else {
      resolved.source = 0
    }

    if (msg.valid !== undefined) {
      resolved.valid = msg.valid;
    }
    else {
      resolved.valid = []
    }

    if (msg.back_pointers !== undefined) {
      resolved.back_pointers = msg.back_pointers;
    }
    else {
      resolved.back_pointers = []
    }

    if (msg.potential !== undefined) {
      resolved.potential = msg.potential;
    }
    else {
      resolved.potential = []
    }

    return resolved;
    }
};

module.exports = NavigationFunction;
