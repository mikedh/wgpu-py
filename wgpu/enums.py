"""
Enums are choices; exactly one field must be selected.
These enums are also available in the root wgpu namespace.
"""

# THIS CODE IS AUTOGENERATED - DO NOT EDIT

_use_sphinx_repr = False


class Enum:
    def __init__(self, name, **kwargs):
        self._name = name
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __iter__(self):
        return iter(
            [getattr(self, key) for key in dir(self) if not key.startswith("_")]
        )

    def __repr__(self):
        if _use_sphinx_repr:  # no-cover
            return ""
        options = ", ".join(f"'{x}'" for x in self)
        return f"<{self.__class__.__name__} {self._name}: {options}>"


# There are 35 enums

#: * "low_power"
#: * "high_performance"
PowerPreference = Enum(
    "PowerPreference",
    low_power="low-power",
    high_performance="high-performance",
)

#: * "depth_clip_control"
#: * "depth32float_stencil8"
#: * "texture_compression_bc"
#: * "texture_compression_etc2"
#: * "texture_compression_astc"
#: * "timestamp_query"
#: * "indirect_first_instance"
#: * "shader_f16"
#: * "rg11b10ufloat_renderable"
FeatureName = Enum(
    "FeatureName",
    depth_clip_control="depth-clip-control",
    depth32float_stencil8="depth32float-stencil8",
    texture_compression_bc="texture-compression-bc",
    texture_compression_etc2="texture-compression-etc2",
    texture_compression_astc="texture-compression-astc",
    timestamp_query="timestamp-query",
    indirect_first_instance="indirect-first-instance",
    shader_f16="shader-f16",
    rg11b10ufloat_renderable="rg11b10ufloat-renderable",
)

#: * "unmapped"
#: * "pending"
#: * "mapped"
BufferMapState = Enum(
    "BufferMapState",
    unmapped="unmapped",
    pending="pending",
    mapped="mapped",
)

#: * "d1"
#: * "d2"
#: * "d3"
TextureDimension = Enum(
    "TextureDimension",
    d1="1d",
    d2="2d",
    d3="3d",
)

#: * "d1"
#: * "d2"
#: * "d2_array"
#: * "cube"
#: * "cube_array"
#: * "d3"
TextureViewDimension = Enum(
    "TextureViewDimension",
    d1="1d",
    d2="2d",
    d2_array="2d-array",
    cube="cube",
    cube_array="cube-array",
    d3="3d",
)

#: * "all"
#: * "stencil_only"
#: * "depth_only"
TextureAspect = Enum(
    "TextureAspect",
    all="all",
    stencil_only="stencil-only",
    depth_only="depth-only",
)

#: * "r8unorm"
#: * "r8snorm"
#: * "r8uint"
#: * "r8sint"
#: * "r16uint"
#: * "r16sint"
#: * "r16float"
#: * "rg8unorm"
#: * "rg8snorm"
#: * "rg8uint"
#: * "rg8sint"
#: * "r32uint"
#: * "r32sint"
#: * "r32float"
#: * "rg16uint"
#: * "rg16sint"
#: * "rg16float"
#: * "rgba8unorm"
#: * "rgba8unorm_srgb"
#: * "rgba8snorm"
#: * "rgba8uint"
#: * "rgba8sint"
#: * "bgra8unorm"
#: * "bgra8unorm_srgb"
#: * "rgb9e5ufloat"
#: * "rgb10a2unorm"
#: * "rg11b10ufloat"
#: * "rg32uint"
#: * "rg32sint"
#: * "rg32float"
#: * "rgba16uint"
#: * "rgba16sint"
#: * "rgba16float"
#: * "rgba32uint"
#: * "rgba32sint"
#: * "rgba32float"
#: * "stencil8"
#: * "depth16unorm"
#: * "depth24plus"
#: * "depth24plus_stencil8"
#: * "depth32float"
#: * "depth32float_stencil8"
#: * "bc1_rgba_unorm"
#: * "bc1_rgba_unorm_srgb"
#: * "bc2_rgba_unorm"
#: * "bc2_rgba_unorm_srgb"
#: * "bc3_rgba_unorm"
#: * "bc3_rgba_unorm_srgb"
#: * "bc4_r_unorm"
#: * "bc4_r_snorm"
#: * "bc5_rg_unorm"
#: * "bc5_rg_snorm"
#: * "bc6h_rgb_ufloat"
#: * "bc6h_rgb_float"
#: * "bc7_rgba_unorm"
#: * "bc7_rgba_unorm_srgb"
#: * "etc2_rgb8unorm"
#: * "etc2_rgb8unorm_srgb"
#: * "etc2_rgb8a1unorm"
#: * "etc2_rgb8a1unorm_srgb"
#: * "etc2_rgba8unorm"
#: * "etc2_rgba8unorm_srgb"
#: * "eac_r11unorm"
#: * "eac_r11snorm"
#: * "eac_rg11unorm"
#: * "eac_rg11snorm"
#: * "astc_4x4_unorm"
#: * "astc_4x4_unorm_srgb"
#: * "astc_5x4_unorm"
#: * "astc_5x4_unorm_srgb"
#: * "astc_5x5_unorm"
#: * "astc_5x5_unorm_srgb"
#: * "astc_6x5_unorm"
#: * "astc_6x5_unorm_srgb"
#: * "astc_6x6_unorm"
#: * "astc_6x6_unorm_srgb"
#: * "astc_8x5_unorm"
#: * "astc_8x5_unorm_srgb"
#: * "astc_8x6_unorm"
#: * "astc_8x6_unorm_srgb"
#: * "astc_8x8_unorm"
#: * "astc_8x8_unorm_srgb"
#: * "astc_10x5_unorm"
#: * "astc_10x5_unorm_srgb"
#: * "astc_10x6_unorm"
#: * "astc_10x6_unorm_srgb"
#: * "astc_10x8_unorm"
#: * "astc_10x8_unorm_srgb"
#: * "astc_10x10_unorm"
#: * "astc_10x10_unorm_srgb"
#: * "astc_12x10_unorm"
#: * "astc_12x10_unorm_srgb"
#: * "astc_12x12_unorm"
#: * "astc_12x12_unorm_srgb"
TextureFormat = Enum(
    "TextureFormat",
    r8unorm="r8unorm",
    r8snorm="r8snorm",
    r8uint="r8uint",
    r8sint="r8sint",
    r16uint="r16uint",
    r16sint="r16sint",
    r16float="r16float",
    rg8unorm="rg8unorm",
    rg8snorm="rg8snorm",
    rg8uint="rg8uint",
    rg8sint="rg8sint",
    r32uint="r32uint",
    r32sint="r32sint",
    r32float="r32float",
    rg16uint="rg16uint",
    rg16sint="rg16sint",
    rg16float="rg16float",
    rgba8unorm="rgba8unorm",
    rgba8unorm_srgb="rgba8unorm-srgb",
    rgba8snorm="rgba8snorm",
    rgba8uint="rgba8uint",
    rgba8sint="rgba8sint",
    bgra8unorm="bgra8unorm",
    bgra8unorm_srgb="bgra8unorm-srgb",
    rgb9e5ufloat="rgb9e5ufloat",
    rgb10a2unorm="rgb10a2unorm",
    rg11b10ufloat="rg11b10ufloat",
    rg32uint="rg32uint",
    rg32sint="rg32sint",
    rg32float="rg32float",
    rgba16uint="rgba16uint",
    rgba16sint="rgba16sint",
    rgba16float="rgba16float",
    rgba32uint="rgba32uint",
    rgba32sint="rgba32sint",
    rgba32float="rgba32float",
    stencil8="stencil8",
    depth16unorm="depth16unorm",
    depth24plus="depth24plus",
    depth24plus_stencil8="depth24plus-stencil8",
    depth32float="depth32float",
    depth32float_stencil8="depth32float-stencil8",
    bc1_rgba_unorm="bc1-rgba-unorm",
    bc1_rgba_unorm_srgb="bc1-rgba-unorm-srgb",
    bc2_rgba_unorm="bc2-rgba-unorm",
    bc2_rgba_unorm_srgb="bc2-rgba-unorm-srgb",
    bc3_rgba_unorm="bc3-rgba-unorm",
    bc3_rgba_unorm_srgb="bc3-rgba-unorm-srgb",
    bc4_r_unorm="bc4-r-unorm",
    bc4_r_snorm="bc4-r-snorm",
    bc5_rg_unorm="bc5-rg-unorm",
    bc5_rg_snorm="bc5-rg-snorm",
    bc6h_rgb_ufloat="bc6h-rgb-ufloat",
    bc6h_rgb_float="bc6h-rgb-float",
    bc7_rgba_unorm="bc7-rgba-unorm",
    bc7_rgba_unorm_srgb="bc7-rgba-unorm-srgb",
    etc2_rgb8unorm="etc2-rgb8unorm",
    etc2_rgb8unorm_srgb="etc2-rgb8unorm-srgb",
    etc2_rgb8a1unorm="etc2-rgb8a1unorm",
    etc2_rgb8a1unorm_srgb="etc2-rgb8a1unorm-srgb",
    etc2_rgba8unorm="etc2-rgba8unorm",
    etc2_rgba8unorm_srgb="etc2-rgba8unorm-srgb",
    eac_r11unorm="eac-r11unorm",
    eac_r11snorm="eac-r11snorm",
    eac_rg11unorm="eac-rg11unorm",
    eac_rg11snorm="eac-rg11snorm",
    astc_4x4_unorm="astc-4x4-unorm",
    astc_4x4_unorm_srgb="astc-4x4-unorm-srgb",
    astc_5x4_unorm="astc-5x4-unorm",
    astc_5x4_unorm_srgb="astc-5x4-unorm-srgb",
    astc_5x5_unorm="astc-5x5-unorm",
    astc_5x5_unorm_srgb="astc-5x5-unorm-srgb",
    astc_6x5_unorm="astc-6x5-unorm",
    astc_6x5_unorm_srgb="astc-6x5-unorm-srgb",
    astc_6x6_unorm="astc-6x6-unorm",
    astc_6x6_unorm_srgb="astc-6x6-unorm-srgb",
    astc_8x5_unorm="astc-8x5-unorm",
    astc_8x5_unorm_srgb="astc-8x5-unorm-srgb",
    astc_8x6_unorm="astc-8x6-unorm",
    astc_8x6_unorm_srgb="astc-8x6-unorm-srgb",
    astc_8x8_unorm="astc-8x8-unorm",
    astc_8x8_unorm_srgb="astc-8x8-unorm-srgb",
    astc_10x5_unorm="astc-10x5-unorm",
    astc_10x5_unorm_srgb="astc-10x5-unorm-srgb",
    astc_10x6_unorm="astc-10x6-unorm",
    astc_10x6_unorm_srgb="astc-10x6-unorm-srgb",
    astc_10x8_unorm="astc-10x8-unorm",
    astc_10x8_unorm_srgb="astc-10x8-unorm-srgb",
    astc_10x10_unorm="astc-10x10-unorm",
    astc_10x10_unorm_srgb="astc-10x10-unorm-srgb",
    astc_12x10_unorm="astc-12x10-unorm",
    astc_12x10_unorm_srgb="astc-12x10-unorm-srgb",
    astc_12x12_unorm="astc-12x12-unorm",
    astc_12x12_unorm_srgb="astc-12x12-unorm-srgb",
)

#: * "clamp_to_edge"
#: * "repeat"
#: * "mirror_repeat"
AddressMode = Enum(
    "AddressMode",
    clamp_to_edge="clamp-to-edge",
    repeat="repeat",
    mirror_repeat="mirror-repeat",
)

#: * "nearest"
#: * "linear"
FilterMode = Enum(
    "FilterMode",
    nearest="nearest",
    linear="linear",
)

#: * "nearest"
#: * "linear"
MipmapFilterMode = Enum(
    "MipmapFilterMode",
    nearest="nearest",
    linear="linear",
)

#: * "never"
#: * "less"
#: * "equal"
#: * "less_equal"
#: * "greater"
#: * "not_equal"
#: * "greater_equal"
#: * "always"
CompareFunction = Enum(
    "CompareFunction",
    never="never",
    less="less",
    equal="equal",
    less_equal="less-equal",
    greater="greater",
    not_equal="not-equal",
    greater_equal="greater-equal",
    always="always",
)

#: * "uniform"
#: * "storage"
#: * "read_only_storage"
BufferBindingType = Enum(
    "BufferBindingType",
    uniform="uniform",
    storage="storage",
    read_only_storage="read-only-storage",
)

#: * "filtering"
#: * "non_filtering"
#: * "comparison"
SamplerBindingType = Enum(
    "SamplerBindingType",
    filtering="filtering",
    non_filtering="non-filtering",
    comparison="comparison",
)

#: * "float"
#: * "unfilterable_float"
#: * "depth"
#: * "sint"
#: * "uint"
TextureSampleType = Enum(
    "TextureSampleType",
    float="float",
    unfilterable_float="unfilterable-float",
    depth="depth",
    sint="sint",
    uint="uint",
)

#: * "write_only"
StorageTextureAccess = Enum(
    "StorageTextureAccess",
    write_only="write-only",
)

#: * "error"
#: * "warning"
#: * "info"
CompilationMessageType = Enum(
    "CompilationMessageType",
    error="error",
    warning="warning",
    info="info",
)

#: * "validation"
#: * "internal"
PipelineErrorReason = Enum(
    "PipelineErrorReason",
    validation="validation",
    internal="internal",
)

#: * "auto"
AutoLayoutMode = Enum(
    "AutoLayoutMode",
    auto="auto",
)

#: * "point_list"
#: * "line_list"
#: * "line_strip"
#: * "triangle_list"
#: * "triangle_strip"
PrimitiveTopology = Enum(
    "PrimitiveTopology",
    point_list="point-list",
    line_list="line-list",
    line_strip="line-strip",
    triangle_list="triangle-list",
    triangle_strip="triangle-strip",
)

#: * "ccw"
#: * "cw"
FrontFace = Enum(
    "FrontFace",
    ccw="ccw",
    cw="cw",
)

#: * "none"
#: * "front"
#: * "back"
CullMode = Enum(
    "CullMode",
    none="none",
    front="front",
    back="back",
)

#: * "zero"
#: * "one"
#: * "src"
#: * "one_minus_src"
#: * "src_alpha"
#: * "one_minus_src_alpha"
#: * "dst"
#: * "one_minus_dst"
#: * "dst_alpha"
#: * "one_minus_dst_alpha"
#: * "src_alpha_saturated"
#: * "constant"
#: * "one_minus_constant"
BlendFactor = Enum(
    "BlendFactor",
    zero="zero",
    one="one",
    src="src",
    one_minus_src="one-minus-src",
    src_alpha="src-alpha",
    one_minus_src_alpha="one-minus-src-alpha",
    dst="dst",
    one_minus_dst="one-minus-dst",
    dst_alpha="dst-alpha",
    one_minus_dst_alpha="one-minus-dst-alpha",
    src_alpha_saturated="src-alpha-saturated",
    constant="constant",
    one_minus_constant="one-minus-constant",
)

#: * "add"
#: * "subtract"
#: * "reverse_subtract"
#: * "min"
#: * "max"
BlendOperation = Enum(
    "BlendOperation",
    add="add",
    subtract="subtract",
    reverse_subtract="reverse-subtract",
    min="min",
    max="max",
)

#: * "keep"
#: * "zero"
#: * "replace"
#: * "invert"
#: * "increment_clamp"
#: * "decrement_clamp"
#: * "increment_wrap"
#: * "decrement_wrap"
StencilOperation = Enum(
    "StencilOperation",
    keep="keep",
    zero="zero",
    replace="replace",
    invert="invert",
    increment_clamp="increment-clamp",
    decrement_clamp="decrement-clamp",
    increment_wrap="increment-wrap",
    decrement_wrap="decrement-wrap",
)

#: * "uint16"
#: * "uint32"
IndexFormat = Enum(
    "IndexFormat",
    uint16="uint16",
    uint32="uint32",
)

#: * "uint8x2"
#: * "uint8x4"
#: * "sint8x2"
#: * "sint8x4"
#: * "unorm8x2"
#: * "unorm8x4"
#: * "snorm8x2"
#: * "snorm8x4"
#: * "uint16x2"
#: * "uint16x4"
#: * "sint16x2"
#: * "sint16x4"
#: * "unorm16x2"
#: * "unorm16x4"
#: * "snorm16x2"
#: * "snorm16x4"
#: * "float16x2"
#: * "float16x4"
#: * "float32"
#: * "float32x2"
#: * "float32x3"
#: * "float32x4"
#: * "uint32"
#: * "uint32x2"
#: * "uint32x3"
#: * "uint32x4"
#: * "sint32"
#: * "sint32x2"
#: * "sint32x3"
#: * "sint32x4"
VertexFormat = Enum(
    "VertexFormat",
    uint8x2="uint8x2",
    uint8x4="uint8x4",
    sint8x2="sint8x2",
    sint8x4="sint8x4",
    unorm8x2="unorm8x2",
    unorm8x4="unorm8x4",
    snorm8x2="snorm8x2",
    snorm8x4="snorm8x4",
    uint16x2="uint16x2",
    uint16x4="uint16x4",
    sint16x2="sint16x2",
    sint16x4="sint16x4",
    unorm16x2="unorm16x2",
    unorm16x4="unorm16x4",
    snorm16x2="snorm16x2",
    snorm16x4="snorm16x4",
    float16x2="float16x2",
    float16x4="float16x4",
    float32="float32",
    float32x2="float32x2",
    float32x3="float32x3",
    float32x4="float32x4",
    uint32="uint32",
    uint32x2="uint32x2",
    uint32x3="uint32x3",
    uint32x4="uint32x4",
    sint32="sint32",
    sint32x2="sint32x2",
    sint32x3="sint32x3",
    sint32x4="sint32x4",
)

#: * "vertex"
#: * "instance"
VertexStepMode = Enum(
    "VertexStepMode",
    vertex="vertex",
    instance="instance",
)

#: * "beginning"
#: * "end"
ComputePassTimestampLocation = Enum(
    "ComputePassTimestampLocation",
    beginning="beginning",
    end="end",
)

#: * "beginning"
#: * "end"
RenderPassTimestampLocation = Enum(
    "RenderPassTimestampLocation",
    beginning="beginning",
    end="end",
)

#: * "load"
#: * "clear"
LoadOp = Enum(
    "LoadOp",
    load="load",
    clear="clear",
)

#: * "store"
#: * "discard"
StoreOp = Enum(
    "StoreOp",
    store="store",
    discard="discard",
)

#: * "occlusion"
#: * "timestamp"
QueryType = Enum(
    "QueryType",
    occlusion="occlusion",
    timestamp="timestamp",
)

#: * "opaque"
#: * "premultiplied"
CanvasAlphaMode = Enum(
    "CanvasAlphaMode",
    opaque="opaque",
    premultiplied="premultiplied",
)

#: * "destroyed"
DeviceLostReason = Enum(
    "DeviceLostReason",
    destroyed="destroyed",
)

#: * "validation"
#: * "out_of_memory"
#: * "internal"
ErrorFilter = Enum(
    "ErrorFilter",
    validation="validation",
    out_of_memory="out-of-memory",
    internal="internal",
)
