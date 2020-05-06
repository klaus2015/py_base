import struct

st = struct.Struct('i4sf')
data = st.pack(1,'我'.encode(),1.65)
print(data)

data = st.unpack(data)
print(data)


data = struct.pack('i4sf',1,b'lucy',1.75)
r = struct.unpack('i4sf',data)
print(r)