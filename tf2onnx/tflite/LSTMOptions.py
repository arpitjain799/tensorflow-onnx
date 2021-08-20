# SPDX-License-Identifier: Apache-2.0

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LSTMOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LSTMOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsLSTMOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def LSTMOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # LSTMOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LSTMOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # LSTMOptions
    def CellClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LSTMOptions
    def ProjClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LSTMOptions
    def KernelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # LSTMOptions
    def AsymmetricQuantizeInputs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(5)
def LSTMOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def LSTMOptionsAddFusedActivationFunction(builder, fusedActivationFunction):
    """This method is deprecated. Please switch to AddFusedActivationFunction."""
    return AddFusedActivationFunction(builder, fusedActivationFunction)
def AddCellClip(builder, cellClip): builder.PrependFloat32Slot(1, cellClip, 0.0)
def LSTMOptionsAddCellClip(builder, cellClip):
    """This method is deprecated. Please switch to AddCellClip."""
    return AddCellClip(builder, cellClip)
def AddProjClip(builder, projClip): builder.PrependFloat32Slot(2, projClip, 0.0)
def LSTMOptionsAddProjClip(builder, projClip):
    """This method is deprecated. Please switch to AddProjClip."""
    return AddProjClip(builder, projClip)
def AddKernelType(builder, kernelType): builder.PrependInt8Slot(3, kernelType, 0)
def LSTMOptionsAddKernelType(builder, kernelType):
    """This method is deprecated. Please switch to AddKernelType."""
    return AddKernelType(builder, kernelType)
def AddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs): builder.PrependBoolSlot(4, asymmetricQuantizeInputs, 0)
def LSTMOptionsAddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs):
    """This method is deprecated. Please switch to AddAsymmetricQuantizeInputs."""
    return AddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs)
def End(builder): return builder.EndObject()
def LSTMOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)