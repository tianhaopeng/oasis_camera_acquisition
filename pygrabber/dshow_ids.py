#
# python_grabber
#

from comtypes import GUID

GUID_NULL = GUID("{00000000-0000-0000-0000-000000000000}")

class clsids:
    CLSID_FilterGraph              = "{E436EBB3-524F-11CE-9F53-0020AF0BA770}"
    CLSID_SystemDeviceEnum         = "{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}"
    CLSID_SampleGrabber            = "{C1F400A0-3F08-11d3-9F0B-006008039E37}"
    CLSID_CaptureGraphBuilder2     = "{BF87B6E1-8C27-11d0-B3F0-00AA003761C5}"
    CLSID_VideoRendererDefault     = "{6BC1CFFA-8FC1-4261-AC22-CFB4CC38DB50}"
    CLSID_NullRender               = "{C1F400A4-3F08-11D3-9F0B-006008039E37}"
    CLSID_VideoMixingRenderer      = "{B87BEB7B-8D29-423f-AE4D-6582C10175AC}"


class DeviceCategories:
    CLSID_VideoInputDeviceCategory = "{860BB310-5D01-11d0-BD3B-00A0C911CE86}"
    CLSID_LegacyAmFilterCategory   = "{083863F1-70DE-11d0-BD40-00A0C911CE86}"


class MediaTypes:
    Video = "{73646976-0000-0010-8000-00AA00389B71}"


class MediaSubtypes:
    RGB24 = "{e436eb7d-524f-11ce-9f53-0020af0ba770}"


subtypes = {
    '{4C504C43-0000-0010-8000-00AA00389B71}': 'CLPL',
    '{56595559-0000-0010-8000-00AA00389B71}': 'YUYV',
    '{56555949-0000-0010-8000-00AA00389B71}': 'IYUV',
    '{39555659-0000-0010-8000-00AA00389B71}': 'YVU9',
    '{31313459-0000-0010-8000-00AA00389B71}': 'Y411',
    '{50313459-0000-0010-8000-00AA00389B71}': 'Y41P',
    '{32595559-0000-0010-8000-00AA00389B71}': 'YUY2',
    '{55595659-0000-0010-8000-00AA00389B71}': 'YVYU',
    '{59565955-0000-0010-8000-00AA00389B71}': 'UYVY',
    '{31313259-0000-0010-8000-00AA00389B71}': 'Y211',
    '{524a4c43-0000-0010-8000-00AA00389B71}': 'CLJR',
    '{39304649-0000-0010-8000-00AA00389B71}': 'IF09',
    '{414c5043-0000-0010-8000-00AA00389B71}': 'CPLA',
    '{47504A4D-0000-0010-8000-00AA00389B71}': 'MJPG',
    '{4A4D5654-0000-0010-8000-00AA00389B71}': 'TVMJ',
    '{454B4157-0000-0010-8000-00AA00389B71}': 'WAKE',
    '{43434643-0000-0010-8000-00AA00389B71}': 'CFCC',
    '{47504A49-0000-0010-8000-00AA00389B71}': 'IJPG',
    '{6D756C50-0000-0010-8000-00AA00389B71}': 'Plum',
    '{53435644-0000-0010-8000-00AA00389B71}': 'DVCS',
    '{34363248-0000-0010-8000-00AA00389B71}': 'H264',
    '{44535644-0000-0010-8000-00AA00389B71}': 'DVSD',
    '{4656444D-0000-0010-8000-00AA00389B71}': 'MDVF',
    '{e436eb78-524f-11ce-9f53-0020af0ba770}': 'RGB1',
    '{e436eb78-524f-11ce-9f53-0020af0ba770}': 'RGB1',
    '{e436eb79-524f-11ce-9f53-0020af0ba770}': 'RGB4',
    '{e436eb7a-524f-11ce-9f53-0020af0ba770}': 'RGB8',
    '{e436eb7b-524f-11ce-9f53-0020af0ba770}': 'RGB565',
    '{e436eb7c-524f-11ce-9f53-0020af0ba770}': 'RGB555',
    '{e436eb7d-524f-11ce-9f53-0020af0ba770}': 'RGB24',
    '{e436eb7e-524f-11ce-9f53-0020af0ba770}': 'RGB32',
    '{297C55AF-E209-4cb3-B757-C76D6B9C88A8}': 'ARGB1555',
    '{6E6415E6-5C24-425f-93CD-80102B3D1CCA}': 'ARGB4444',
    '{773c9ac0-3274-11d0-B724-00aa006c1A01}': 'ARGB32',
    '{2f8bb76d-b644-4550-acf3-d30caa65d5c5}': 'A2R10G10B10',
    '{576f7893-bdf6-48c4-875f-ae7b81834567}': 'A2B10G10R10',
    '{56555941-0000-0010-8000-00AA00389B71}': 'AYUV',
    '{34344941-0000-0010-8000-00AA00389B71}': 'AI44',
    '{34344149-0000-0010-8000-00AA00389B71}': 'IA44',
    '{32335237-0000-0010-8000-00AA00389B71}': 'RGB32_D3D_DX7_RT',
    '{36315237-0000-0010-8000-00AA00389B71}': 'RGB16_D3D_DX7_RT',
    '{38384137-0000-0010-8000-00AA00389B71}': 'ARGB32_D3D_DX7_RT',
    '{34344137-0000-0010-8000-00AA00389B71}': 'ARGB4444_D3D_DX7_RT',
    '{35314137-0000-0010-8000-00AA00389B71}': 'ARGB1555_D3D_DX7_RT',
    '{32335239-0000-0010-8000-00AA00389B71}': 'RGB32_D3D_DX9_RT',
    '{36315239-0000-0010-8000-00AA00389B71}': 'RGB16_D3D_DX9_RT',
    '{38384139-0000-0010-8000-00AA00389B71}': 'ARGB32_D3D_DX9_RT',
    '{34344139-0000-0010-8000-00AA00389B71}': 'ARGB4444_D3D_DX9_RT',
    '{35314139-0000-0010-8000-00AA00389B71}': 'ARGB1555_D3D_DX9_RT',
    '{32315659-0000-0010-8000-00AA00389B71}': 'YV12',
    '{3231564E-0000-0010-8000-00AA00389B71}': 'NV12',
    '{3131564E-0000-0010-8000-00AA00389B71}': 'NV11',
    '{38303250-0000-0010-8000-00AA00389B71}': 'P208',
    '{38303250-0000-0010-8000-00AA00389B71}': 'P210',
    '{38303250-0000-0010-8000-00AA00389B71}': 'P216',
    '{38303250-0000-0010-8000-00AA00389B71}': 'P010',
    '{38303250-0000-0010-8000-00AA00389B71}': 'P016',
    '{38303250-0000-0010-8000-00AA00389B71}': 'Y210',
    '{38303250-0000-0010-8000-00AA00389B71}': 'Y216',
    '{38303450-0000-0010-8000-00AA00389B71}': 'P408',
    '{3432564E-0000-0010-8000-00AA00389B71}': 'NV24',
    '{4F303234-0000-0010-8000-00AA00389B71}': '420O',
    '{31434D49-0000-0010-8000-00AA00389B71}': 'IMC1',
    '{32434d49-0000-0010-8000-00AA00389B71}': 'IMC2',
    '{33434d49-0000-0010-8000-00AA00389B71}': 'IMC3',
    '{34434d49-0000-0010-8000-00AA00389B71}': 'IMC4',
    '{30343353-0000-0010-8000-00AA00389B71}': 'S340',
    '{32343353-0000-0010-8000-00AA00389B71}': 'S342',
    '{e436eb7f-524f-11ce-9f53-0020af0ba770}': 'Overlay',
    '{e436eb80-524f-11ce-9f53-0020af0ba770}': 'MPEGPacket',
    '{e436eb81-524f-11ce-9f53-0020af0ba770}': 'MPEG1Payload',
    '{00000050-0000-0010-8000-00AA00389B71}': 'MPEG1AudioPayload',
    '{e436eb82-524f-11ce-9f53-0020af0ba770}': 'MPEG1SystemStream',
    '{e436eb84-524f-11ce-9f53-0020af0ba770}': 'MPEG1System',
    '{e436eb85-524f-11ce-9f53-0020af0ba770}': 'MPEG1VideoCD',
    '{e436eb86-524f-11ce-9f53-0020af0ba770}': 'MPEG1Video',
    '{e436eb87-524f-11ce-9f53-0020af0ba770}': 'MPEG1Audio',
    '{e436eb88-524f-11ce-9f53-0020af0ba770}': 'Avi',
    '{3DB80F90-9412-11d1-ADED-0000F8754B99}': 'Asf',
    '{e436eb89-524f-11ce-9f53-0020af0ba770}': 'QTMovie',
    '{617a7072-0000-0010-8000-00AA00389B71}': 'Rpza',
    '{20636d73-0000-0010-8000-00AA00389B71}': 'Smc',
    '{20656c72-0000-0010-8000-00AA00389B71}': 'Rle',
    '{6765706a-0000-0010-8000-00AA00389B71}': 'Jpeg',
    '{e436eb8a-524f-11ce-9f53-0020af0ba770}': 'PCMAudio_Obsolete',
    '{00000001-0000-0010-8000-00AA00389B71}': 'PCM',
    '{e436eb8b-524f-11ce-9f53-0020af0ba770}': 'WAVE',
    '{e436eb8c-524f-11ce-9f53-0020af0ba770}': 'AU',
    '{e436eb8d-524f-11ce-9f53-0020af0ba770}': 'AIFF',
    '{6E8D4A22-310C-11d0-B79A-00AA003767A7}': 'Line21_BytePair',
    '{6E8D4A23-310C-11d0-B79A-00AA003767A7}': 'Line21_GOPPacket',
    '{6E8D4A24-310C-11d0-B79A-00AA003767A7}': 'Line21_VBIRawData',
    '{0AF414BC-4ED2-445e-9839-8F095568AB3C}': '708_608Data',
    '{F52ADDAA-36F0-43F5-95EA-6D866484262A}': 'DtvCcData',
    '{7EA626DB-54DA-437b-BE9F-F73073ADFA3C}': 'CC_CONTAINER',
    '{F72A76E3-EB0A-11D0-ACE4-0000C0CC16BA}': 'TELETEXT',
    '{663DA43C-03E8-4e9a-9CD5-BF11ED0DEF76}': 'VBI',
    '{2791D576-8E7A-466F-9E90-5D3F3083738B}': 'WSS',
    '{01CA73E3-DCE6-4575-AFE1-2BF1C902CAF3}': 'XDS',
    '{A1B3F620-9792-4d8d-81A4-86AF25772090}': 'VPS'
}

