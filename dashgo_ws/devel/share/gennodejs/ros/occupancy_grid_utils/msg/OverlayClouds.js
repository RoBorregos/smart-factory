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

class OverlayClouds {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.grid = null;
      this.frame_id = null;
      this.occupancy_threshold = null;
      this.max_distance = null;
      this.min_pass_through = null;
      this.hit_counts = null;
      this.pass_through_counts = null;
    }
    else {
      if (initObj.hasOwnProperty('grid')) {
        this.grid = initObj.grid
      }
      else {
        this.grid = new nav_msgs.msg.OccupancyGrid();
      }
      if (initObj.hasOwnProperty('frame_id')) {
        this.frame_id = initObj.frame_id
      }
      else {
        this.frame_id = '';
      }
      if (initObj.hasOwnProperty('occupancy_threshold')) {
        this.occupancy_threshold = initObj.occupancy_threshold
      }
      else {
        this.occupancy_threshold = 0.0;
      }
      if (initObj.hasOwnProperty('max_distance')) {
        this.max_distance = initObj.max_distance
      }
      else {
        this.max_distance = 0.0;
      }
      if (initObj.hasOwnProperty('min_pass_through')) {
        this.min_pass_through = initObj.min_pass_through
      }
      else {
        this.min_pass_through = 0.0;
      }
      if (initObj.hasOwnProperty('hit_counts')) {
        this.hit_counts = initObj.hit_counts
      }
      else {
        this.hit_counts = [];
      }
      if (initObj.hasOwnProperty('pass_through_counts')) {
        this.pass_through_counts = initObj.pass_through_counts
      }
      else {
        this.pass_through_counts = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OverlayClouds
    // Serialize message field [grid]
    bufferOffset = nav_msgs.msg.OccupancyGrid.serialize(obj.grid, buffer, bufferOffset);
    // Serialize message field [frame_id]
    bufferOffset = _serializer.string(obj.frame_id, buffer, bufferOffset);
    // Serialize message field [occupancy_threshold]
    bufferOffset = _serializer.float32(obj.occupancy_threshold, buffer, bufferOffset);
    // Serialize message field [max_distance]
    bufferOffset = _serializer.float32(obj.max_distance, buffer, bufferOffset);
    // Serialize message field [min_pass_through]
    bufferOffset = _serializer.float32(obj.min_pass_through, buffer, bufferOffset);
    // Serialize message field [hit_counts]
    bufferOffset = _arraySerializer.int32(obj.hit_counts, buffer, bufferOffset, null);
    // Serialize message field [pass_through_counts]
    bufferOffset = _arraySerializer.int32(obj.pass_through_counts, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OverlayClouds
    let len;
    let data = new OverlayClouds(null);
    // Deserialize message field [grid]
    data.grid = nav_msgs.msg.OccupancyGrid.deserialize(buffer, bufferOffset);
    // Deserialize message field [frame_id]
    data.frame_id = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [occupancy_threshold]
    data.occupancy_threshold = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [max_distance]
    data.max_distance = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [min_pass_through]
    data.min_pass_through = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [hit_counts]
    data.hit_counts = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [pass_through_counts]
    data.pass_through_counts = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += nav_msgs.msg.OccupancyGrid.getMessageSize(object.grid);
    length += object.frame_id.length;
    length += 4 * object.hit_counts.length;
    length += 4 * object.pass_through_counts.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'occupancy_grid_utils/OverlayClouds';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a1dfac662600ca9b91b434a76485a5d9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    nav_msgs/OccupancyGrid grid
    string frame_id
    float32 occupancy_threshold
    float32 max_distance
    float32 min_pass_through
    int32[] hit_counts
    int32[] pass_through_counts
    ================================================================================
    MSG: nav_msgs/OccupancyGrid
    # This represents a 2-D grid map, in which each cell represents the probability of
    # occupancy.
    
    Header header 
    
    #MetaData for the map
    MapMetaData info
    
    # The map data, in row-major order, starting with (0,0).  Occupancy
    # probabilities are in the range [0,100].  Unknown is -1.
    int8[] data
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
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
    const resolved = new OverlayClouds(null);
    if (msg.grid !== undefined) {
      resolved.grid = nav_msgs.msg.OccupancyGrid.Resolve(msg.grid)
    }
    else {
      resolved.grid = new nav_msgs.msg.OccupancyGrid()
    }

    if (msg.frame_id !== undefined) {
      resolved.frame_id = msg.frame_id;
    }
    else {
      resolved.frame_id = ''
    }

    if (msg.occupancy_threshold !== undefined) {
      resolved.occupancy_threshold = msg.occupancy_threshold;
    }
    else {
      resolved.occupancy_threshold = 0.0
    }

    if (msg.max_distance !== undefined) {
      resolved.max_distance = msg.max_distance;
    }
    else {
      resolved.max_distance = 0.0
    }

    if (msg.min_pass_through !== undefined) {
      resolved.min_pass_through = msg.min_pass_through;
    }
    else {
      resolved.min_pass_through = 0.0
    }

    if (msg.hit_counts !== undefined) {
      resolved.hit_counts = msg.hit_counts;
    }
    else {
      resolved.hit_counts = []
    }

    if (msg.pass_through_counts !== undefined) {
      resolved.pass_through_counts = msg.pass_through_counts;
    }
    else {
      resolved.pass_through_counts = []
    }

    return resolved;
    }
};

module.exports = OverlayClouds;
