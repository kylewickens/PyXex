import const
from indents import Indents
from struct import *
from Crypto.Cipher import AES

const.XEX_COMPRESSION = [
    'XEX_COMPRESSION_NONE',
    'XEX_COMPRESSION_BASIC',
    'XEX_COMPRESSION_NORMAL',
    'XEX_COMPRESSION_DELTA']

const.XEX_COMPRESSION_NONE = 0
const.XEX_COMPRESSION_BASIC = 1
const.XEX_COMPRESSION_NORMAL = 2
const.XEX_COMPRESSION_DELTA = 3

const.XEX_ENCRYPTION = [
    'XEX_ENCRYPTION_NONE',
    'XEX_ENCRYPTION_NORMAL']

const.XEX_HEADER_ADDITIONAL_TITLE_MEMORY = 0x00040801
const.XEX_HEADER_ALTERNATE_TITLE_IDS = 0x000407FF
const.XEX_HEADER_BASE_REFERENCE = 0x00000405
const.XEX_HEADER_BOUNDING_PATH = 0x000080FF
const.XEX_HEADER_CHECKSUM_TIMESTAMP = 0x00018002
const.XEX_HEADER_DEFAULT_FILESYSTEM_CACHE_SIZE = 0x00020301
const.XEX_HEADER_DEFAULT_STACK_SIZE = 0x00020200
const.XEX_HEADER_DEFAULT_HEAP_SIZE = 0x00020401
const.XEX_HEADER_DELTA_PATCH_DESCRIPTOR = 0x000005FF
const.XEX_HEADER_DEVICE_ID = 0x00008105
const.XEX_HEADER_ENABLED_FOR_CALLCAP = 0x00018102
const.XEX_HEADER_ENABLED_FOR_FASTCAP = 0x00018200
const.XEX_HEADER_ENTRY_POINT = 0x00010100
const.XEX_HEADER_EXECUTION_INFO = 0x00040006
const.XEX_HEADER_EXPORTS_BY_NAME = 0x00E10402
const.XEX_HEADER_FILE_FORMAT_INFO = 0x000003FF
const.XEX_HEADER_GAME_RATINGS = 0x00040310
const.XEX_HEADER_IMAGE_BASE_ADDRESS = 0x00010201
const.XEX_HEADER_IMPORT_LIBRARIES = 0x000103FF
const.XEX_HEADER_LAN_KEY = 0x00040404
const.XEX_HEADER_MULTIDISC_MEDIA_IDS = 0x000406FF
const.XEX_HEADER_ORIGINAL_BASE_ADDRESS = 0x00010001
const.XEX_HEADER_ORIGINAL_PE_NAME = 0x000183FF
const.XEX_HEADER_PAGE_HEAP_SIZE_AND_FLAGS = 0x00028002
const.XEX_HEADER_RESOURCE_INFO = 0x000002FF
const.XEX_HEADER_STATIC_LIBRARIES = 0x000200FF
const.XEX_HEADER_SYSTEM_FLAGS = 0x00030000
const.XEX_HEADER_TITLE_WORKSPACE_SIZE = 0x00040201
const.XEX_HEADER_TLS_INFO = 0x00020104
const.XEX_HEADER_XBOX360_LOGO = 0x000405FF


class Xex:

    ## The constant for the encryption type none.
    # const.XEX_ENCRYPTION_NONE = 0
    const.XEX_ENCRYPTION_NONE = 0
    ## The constant for the encryption type normal.
    # const.XEX_ENCRYPTION_NORMAL = 1
    const.XEX_ENCRYPTION_NORMAL = 1

    ## The constant for the game rating for BBFC (British Board of Film Classification) type universal.
    # const.XEX_RATING_BBFC_UNIVERSAL = 1
    const.XEX_RATING_BBFC_UNIVERSAL = 1
    ## The constant for the game rating for BBFC (British Board of Film Classification) type parental guidance.
    # const.XEX_RATING_BBFC_PG = 5
    const.XEX_RATING_BBFC_PG = 5
    ## The constant for the game rating for BBFC (British Board of Film Classification) type 3 years+.
    # const.XEX_RATING_BBFC_3_PLUS = 0
    const.XEX_RATING_BBFC_3_PLUS = 0
    ## The constant for the game rating for BBFC (British Board of Film Classification) type 7 years+.
    # const.XEX_RATING_BBFC_7_PLUS = 4
    const.XEX_RATING_BBFC_7_PLUS = 4
    ## The constant for the game rating for BBFC (British Board of Film Classification) type 12 years+.
    # const.XEX_RATING_BBFC_12_PLUS = 9
    const.XEX_RATING_BBFC_12_PLUS = 9
    ## The constant for the game rating for BBFC (British Board of Film Classification) type 15 years+.
    # const.XEX_RATING_BBFC_15_PLUS = 12
    const.XEX_RATING_BBFC_15_PLUS = 12
    ## The constant for the game rating for BBFC (British Board of Film Classification) type 16 years+.
    # const.XEX_RATING_BBFC_16_PLUS = 13
    const.XEX_RATING_BBFC_16_PLUS = 13
    ## The constant for the game rating for BBFC (British Board of Film Classification) type 18 years+.
    # const.XEX_RATING_BBFC_18_PLUS = 14
    const.XEX_RATING_BBFC_18_PLUS = 14
    ## The constant for the game rating for BBFC (British Board of Film Classification) type unrated.
    # const.XEX_RATING_BBFC_UNRATED = 0xFF
    const.XEX_RATING_BBFC_UNRATED = 0xFF

    ## The constant for the game rating for Brazilian Advisory Rating System type all ages.
    # const.XEX_RATING_BRAZIL_ALL = 0
    const.XEX_RATING_BRAZIL_ALL = 0
    ## The constant for the game rating for Brazilian Advisory Rating System type 12 years+.
    # const.XEX_RATING_BRAZIL_12_PLUS = 2
    const.XEX_RATING_BRAZIL_12_PLUS = 2
    ## The constant for the game rating for Brazilian Advisory Rating System type 14 years+.
    # const.XEX_RATING_BRAZIL_14_PLUS = 4
    const.XEX_RATING_BRAZIL_14_PLUS = 4
    ## The constant for the game rating for Brazilian Advisory Rating System type 16 years+.
    # const.XEX_RATING_BRAZIL_16_PLUS = 5
    const.XEX_RATING_BRAZIL_16_PLUS = 5
    ## The constant for the game rating for Brazilian Advisory Rating System type 18 years+.
    #  const.XEX_RATING_BRAZIL_18_PLUS = 8
    const.XEX_RATING_BRAZIL_18_PLUS = 8
    ## The constant for the game rating for Brazilian Advisory Rating System type unrated.
    #  const.XEX_RATING_BRAZIL_UNRATED = 0xFF
    const.XEX_RATING_BRAZIL_UNRATED = 0xFF

    ## The constant for the game rating for CERO (Computer Entertainment Rating Organization) type all ages.
    # const.XEX_RATING_CERO_A = 0
    const.XEX_RATING_CERO_A = 0
    ## The constant for the game rating for CERO (Computer Entertainment Rating Organization) type 12 years+.
    # const.XEX_RATING_CERO_B = 2
    const.XEX_RATING_CERO_B = 2
    ## The constant for the game rating for CERO (Computer Entertainment Rating Organization) type 15 years+.
    # const.XEX_RATING_CERO_C = 4
    const.XEX_RATING_CERO_C = 4
    ## The constant for the game rating for CERO (Computer Entertainment Rating Organization) type 17 years+.
    # const.XEX_RATING_CERO_D = 6
    const.XEX_RATING_CERO_D = 6
    ## The constant for the game rating for CERO (Computer Entertainment Rating Organization) type 18 years+.
    # const.XEX_RATING_CERO_Z = 8
    const.XEX_RATING_CERO_Z = 8
    ## The constant for the game rating for CERO (Computer Entertainment Rating Organization) type unrated.
    # const.XEX_RATING_CERO_UNRATED = 0xFF
    const.XEX_RATING_CERO_UNRATED = 0xFF

    ## The constant for the game rating for ESRB (Entertainment Software Rating Board) type early childhood.
    # const.XEX_RATING_ESRB_eC = 0x00
    const.XEX_RATING_ESRB_eC = 0x00
    ## The constant for the game rating for ESRB (Entertainment Software Rating Board) type everyone.
    # const.XEX_RATING_ESRB_E = 0x02
    const.XEX_RATING_ESRB_E = 0x02
    ## The constant for the game rating for ESRB (Entertainment Software Rating Board) type everyone 10 years+.
    # const.XEX_RATING_ESRB_E10 = 0x04
    const.XEX_RATING_ESRB_E10 = 0x04
    ## The constant for the game rating for ESRB (Entertainment Software Rating Board) type teenage.
    # const.XEX_RATING_ESRB_T = 0x06
    const.XEX_RATING_ESRB_T = 0x06
    ## The constant for the game rating for ESRB (Entertainment Software Rating Board) type mature.
    # const.XEX_RATING_ESRB_M = 0x08
    const.XEX_RATING_ESRB_M = 0x08
    ## The constant for the game rating for ESRB (Entertainment Software Rating Board) type adults only.
    # const.XEX_RATING_ESRB_AO = 0x0E
    const.XEX_RATING_ESRB_AO = 0x0E
    ## The constant for the game rating for ESRB (Entertainment Software Rating Board) type unrated.
    # const.XEX_RATING_ESRB_UNRATED = 0xFF
    const.XEX_RATING_ESRB_UNRATED = 0xFF

    ## The constant for the game rating for FPB (Film and Publication Board) type all ages.
    # const.XEX_RATING_FPB_ALL = 0
    const.XEX_RATING_FPB_ALL = 0
    ## The constant for the game rating for FPB (Film and Publication Board) type parental guidance.
    # const.XEX_RATING_FPB_PG = 6
    const.XEX_RATING_FPB_PG = 6
    ## The constant for the game rating for FPB (Film and Publication Board) type 10 years+.
    # const.XEX_RATING_FPB_10_PLUS = 7
    const.XEX_RATING_FPB_10_PLUS = 7
    ## The constant for the game rating for FPB (Film and Publication Board) type 13 years+.
    # const.XEX_RATING_FPB_13_PLUS = 10
    const.XEX_RATING_FPB_13_PLUS = 10
    ## The constant for the game rating for FPB (Film and Publication Board) type 16 years+.
    # const.XEX_RATING_FPB_16_PLUS = 13
    const.XEX_RATING_FPB_16_PLUS = 13
    ## The constant for the game rating for FPB (Film and Publication Board) type 18 years+.
    # const.XEX_RATING_FPB_18_PLUS = 14
    const.XEX_RATING_FPB_18_PLUS = 14
    ## The constant for the game rating for FPB (Film and Publication Board) type unrated.
    # const.XEX_RATING_FPB_UNRATED = 0xFF
    const.XEX_RATING_FPB_UNRATED = 0xFF

    ## The constant for the game rating for KMRB (Korea Media Rating Board) type all ages.
    # const.XEX_RATING_KMRB_ALL = 0
    const.XEX_RATING_KMRB_ALL = 0
    ## The constant for the game rating for KMRB (Korea Media Rating Board) type 12 years+.
    # const.XEX_RATING_KMRB_12_PLUS = 2
    const.XEX_RATING_KMRB_12_PLUS = 2
    ## The constant for the game rating for KMRB (Korea Media Rating Board) type 15 years+.
    # const.XEX_RATING_KMRB_15_PLUS = 4
    const.XEX_RATING_KMRB_15_PLUS = 4
    ## The constant for the game rating for KMRB (Korea Media Rating Board) type 18 years+.
    # const.XEX_RATING_KMRB_18_PLUS = 6
    const.XEX_RATING_KMRB_18_PLUS = 6
    ## The constant for the game rating for KMRB (Korea Media Rating Board) type unrated.
    # const.XEX_RATING_KMRB_UNRATED = 0xFF
    const.XEX_RATING_KMRB_UNRATED = 0xFF

    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - Australia type general exhibition.
    # const.XEX_RATING_OFLC_AU_G = 0
    const.XEX_RATING_OFLC_AU_G = 0
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - Australia type parental guidance.
    # const.XEX_RATING_OFLC_AU_PG = 2
    const.XEX_RATING_OFLC_AU_PG = 2
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - Australia type mature audience.
    # const.XEX_RATING_OFLC_AU_M = 4
    const.XEX_RATING_OFLC_AU_M = 4
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - Australia type 15 years+.
    # const.XEX_RATING_OFLC_AU_MA15_PLUS = 6
    const.XEX_RATING_OFLC_AU_MA15_PLUS = 6
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - Australia type unrated.
    # const.XEX_RATING_OFLC_AU_UNRATED = 0xFF
    const.XEX_RATING_OFLC_AU_UNRATED = 0xFF

    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - New Zealand type general exhibition.
    # const.XEX_RATING_OFLC_NZ_G = 0
    const.XEX_RATING_OFLC_NZ_G = 0
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - New Zealand  type parental guidance.
    # const.XEX_RATING_OFLC_NZ_PG = 2
    const.XEX_RATING_OFLC_NZ_PG = 2
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - New Zealand  type mature audience.
    # const.XEX_RATING_OFLC_NZ_M = 4
    const.XEX_RATING_OFLC_NZ_M = 4
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - New Zealand  type 15 years+.
    # const.XEX_RATING_OFLC_NZ_MA15_PLUS = 6
    const.XEX_RATING_OFLC_NZ_MA15_PLUS = 6
    ## The constant for the game rating for OFLC (Office of Film and Literature Classification) - New Zealand  type unrated.
    # const.XEX_RATING_OFLC_NZ_UNRATED = 0xFF
    const.XEX_RATING_OFLC_NZ_UNRATED = 0xFF

    ## The constant for the game rating for PEGI (Pan European Game Information) type 3 years+.
    # const.XEX_RATING_PEGI_3_PLUS = 0
    const.XEX_RATING_PEGI_3_PLUS = 0
    ## The constant for the game rating for PEGI (Pan European Game Information) type 7 years+.
    # const.XEX_RATING_PEGI_7_PLUS = 4
    const.XEX_RATING_PEGI_7_PLUS = 4
    ## The constant for the game rating for PEGI (Pan European Game Information) type 12 years+.
    # const.XEX_RATING_PEGI_12_PLUS = 9
    const.XEX_RATING_PEGI_12_PLUS = 9
    ## The constant for the game rating for PEGI (Pan European Game Information) type 16 years+.
    # const.XEX_RATING_PEGI_16_PLUS = 13
    const.XEX_RATING_PEGI_16_PLUS = 13
    ## The constant for the game rating for PEGI (Pan European Game Information) type 18 years+.
    # const.XEX_RATING_PEGI_18_PLUS = 14
    const.XEX_RATING_PEGI_18_PLUS = 14
    ## The constant for the game rating for PEGI (Pan European Game Information) type unrated.
    # const.XEX_RATING_PEGI_UNRATED = 0xFF
    const.XEX_RATING_PEGI_UNRATED = 0xFF

    ## The constant for the game rating for PEGI (Pan European Game Information) - Finland type 3 years+.
    # const.XEX_RATING_PEGI_FI_3_PLUS = 0
    const.XEX_RATING_PEGI_FI_3_PLUS = 0
    ## The constant for the game rating for PEGI (Pan European Game Information) - Finland type 7 years+.
    # const.XEX_RATING_PEGI_FI_7_PLUS = 4
    const.XEX_RATING_PEGI_FI_7_PLUS = 4
    ## The constant for the game rating for PEGI (Pan European Game Information) - Finland type 11 years+.
    # const.XEX_RATING_PEGI_FI_11_PLUS = 8
    const.XEX_RATING_PEGI_FI_11_PLUS = 8
    ## The constant for the game rating for PEGI (Pan European Game Information) - Finland type 15 years+.
    # const.XEX_RATING_PEGI_FI_15_PLUS = 12
    const.XEX_RATING_PEGI_FI_15_PLUS = 12
    ## The constant for the game rating for PEGI (Pan European Game Information) - Finland type 18 years+.
    # const.XEX_RATING_PEGI_FI_18_PLUS = 14
    const.XEX_RATING_PEGI_FI_18_PLUS = 14
    ## The constant for the game rating for PEGI (Pan European Game Information) - Finland type unrated.
    # const.XEX_RATING_PEGI_FI_UNRATED = 0xFF
    const.XEX_RATING_PEGI_FI_UNRATED = 0xFF

    ## The constant for the game rating for PEGI (Pan European Game Information) - Portugal type 4 years+.
    # const.XEX_RATING_PEGI_PT_4_PLUS = 1
    const.XEX_RATING_PEGI_PT_4_PLUS = 1
    ## The constant for the game rating for PEGI (Pan European Game Information) - Portugal type 6 years+.
    # const.XEX_RATING_PEGI_PT_6_PLUS = 3
    const.XEX_RATING_PEGI_PT_6_PLUS = 3
    ## The constant for the game rating for PEGI (Pan European Game Information) - Portugal type 12 years+.
    # const.XEX_RATING_PEGI_PT_12_PLUS = 9
    const.XEX_RATING_PEGI_PT_12_PLUS = 9
    ## The constant for the game rating for PEGI (Pan European Game Information) - Portugal type 16 years+.
    # const.XEX_RATING_PEGI_PT_16_PLUS = 13
    const.XEX_RATING_PEGI_PT_16_PLUS = 13
    ## The constant for the game rating for PEGI (Pan European Game Information) - Portugal type 18 years+.
    # const.XEX_RATING_PEGI_PT_18_PLUS = 14
    const.XEX_RATING_PEGI_PT_18_PLUS = 14
    ## The constant for the game rating for PEGI (Pan European Game Information) - Portugal type unrated.
    # const.XEX_RATING_PEGI_PT_UNRATED = 0xFF
    const.XEX_RATING_PEGI_PT_UNRATED = 0xFF

    ## The constant for the game rating for USK (Unterhaltungssoftware SelbstKontrolle) type all ages.
    # const.XEX_RATING_USK_ALL = 0
    const.XEX_RATING_USK_ALL = 0
    ## The constant for the game rating for USK (Unterhaltungssoftware SelbstKontrolle) type 6 years+.
    # const.XEX_RATING_USK_6_PLUS = 2
    const.XEX_RATING_USK_6_PLUS = 2
    ## The constant for the game rating for USK (Unterhaltungssoftware SelbstKontrolle) type 12 years+.
    # const.XEX_RATING_USK_12_PLUS = 4
    const.XEX_RATING_USK_12_PLUS = 4
    ## The constant for the game rating for USK (Unterhaltungssoftware SelbstKontrolle) type 16 years+.
    # const.XEX_RATING_USK_16_PLUS = 6
    const.XEX_RATING_USK_16_PLUS = 6
    ## The constant for the game rating for USK (Unterhaltungssoftware SelbstKontrolle) type 18 years+.
    # const.XEX_RATING_USK_18_PLUS = 8
    const.XEX_RATING_USK_18_PLUS = 8
    ## The constant for the game rating for USK (Unterhaltungssoftware SelbstKontrolle) type unrated.
    # const.XEX_RATING_USK_UNRATED = 0xFF
    const.XEX_RATING_USK_UNRATED = 0xFF

    ## The constant for the section type code.
    # const.XEX_SECTION_CODE = 1
    const.XEX_SECTION_CODE = 1
    ## The constant for the section type data.
    # const.XEX_SECTION_DATA = 2
    const.XEX_SECTION_DATA = 2
    ## The constant for the section type readonly data.
    # const.XEX_SECTION_READONLY_DATA = 3
    const.XEX_SECTION_READONLY_DATA = 3

    ## The retail encryption key.
    XEX_RETAIL_KEY = b'\x20\xB1\x85\xA5\x9D\x28\xFD\xC3\x40\x58\x3F\xBB\x08\x96\xBF\x91'
    ## The development kit encryption key.
    XEX_DEVKIT_KEY = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self, filename):
        """The constructor.
        @param filename The XEX file name."""
        self.data_counter = 0
        if not filename:
            print('invalid xex provided')
            exit(1)

        self.line = Indents()

        self.optional_headers_reset()
        self.sections_reset()

        self.additional_title_memory_reset()
        self.alternate_title_ids_reset()
        self.base_reference_reset()
        self.bounding_path_reset()
        self.checksum_timestamp_reset()
        self.default_filesystem_cache_size_reset()
        self.default_heap_size_reset()
        self.default_stack_size_reset()
        self.delta_patch_descriptor_reset()
        self.device_id_reset()
        self.enabled_for_callcap_reset()
        self.enabled_for_fastcap_reset()
        self.entry_point_reset()
        self.execution_info_reset()
        self.exports_by_name_reset()
        self.file_format_info_reset()
        self.game_ratings_reset()
        self.image_base_address_reset()
        self.import_libraries_reset()
        self.lan_key_reset()
        self.multidisc_media_ids_reset()
        self.original_base_address_reset()
        self.original_pe_name_reset()
        self.page_heap_size_and_flags_reset()
        self.resource_info_reset()
        self.static_libraries_reset()
        self.system_flags_reset()
        self.title_workspace_size_reset()
        self.tls_info_reset()
        self.xbox360_logo_reset()

        self.data = open(filename, 'rb').read()

        self.header_decode()
        self.optional_headers_decode()

        for optional_header in self.optional_headers:
            self.additional_title_memory_decode(optional_header)
            self.alternate_title_ids_decode(optional_header)
            self.base_reference_decode(optional_header)
            self.bounding_path_decode(optional_header)
            self.checksum_timestamp_decode(optional_header)
            self.default_filesystem_cache_size_decode(optional_header)
            self.default_stack_size_decode(optional_header)
            self.default_heap_size_decode(optional_header)
            self.delta_patch_descriptor_decode(optional_header)
            self.device_id_decode(optional_header)
            self.enabled_for_callcap_decode(optional_header)
            self.enabled_for_fastcap_decode(optional_header)
            self.entry_point_decode(optional_header)
            self.execution_info_decode(optional_header)
            self.exports_by_name_decode(optional_header)
            self.file_format_info_decode(optional_header)
            self.game_ratings_decode(optional_header)
            self.image_base_address_decode(optional_header)
            self.import_libraries_decode(optional_header)
            self.lan_key_decode(optional_header)
            self.multidisc_media_ids_decode(optional_header)
            self.original_base_address_decode(optional_header)
            self.original_pe_name_decode(optional_header)
            self.page_heap_size_and_flags_decode(optional_header)
            self.resource_info_decode(optional_header)
            self.static_libraries_decode(optional_header)
            self.system_flags_decode(optional_header)
            self.title_workspace_size_decode(optional_header)
            self.tls_info_decode(optional_header)
            self.xbox360_logo_decode(optional_header)

        self.loader_decode()
        self.sections_decode()

    def key(self, header):
        return header[0]

    def hex8(self, value):
        return '0x' + format(value,  '08x')

    def header_decode(self):
        """To decode the XEX header.

        Offset | Bits	    | Type Information
        ---------|-----------|------------------------
        0x00  |  32       | XEX2 magic.
        0x04  |  32       | Module flags.
        0x08  |  32       | PE data offset.
        0x0C  |  32       | Reserved.
        0x10  |  32       | Certificate offset.
        0x14  |  32       | Optional header count."""
        header_sting = '>4s L L L L L'
        self.data_counter = calcsize(header_sting)
        self.signature, self.module_flags, self.exe_offset, self.unk, self.certificate_offset, self.header_count \
            = unpack(header_sting, self.data[0:self.data_counter])
        if self.signature != b'XEX2':
            print('signature mismatch', self.signature)
            exit(1)

    def header_show(self):
        self.line.output('XEX_HEADER')
        self.line.indent()
        self.line.output('SIGNATURE', self.signature)
        self.line.output_hex8('MODULE_FLAGS', self.module_flags)
        self.line.output_hex8('EXE_OFFSET', self.exe_offset, self.exe_offset)
        self.line.output('UNK', self.unk)
        self.line.output_hex8('CERTIFICATE_OFFSET', self.certificate_offset, self.certificate_offset)
        self.line.output('OPTIONAL_HEADER_COUNT', self.header_count)
        self.line.outdent()

    def loader_decode(self):
        self.data_counter = self.certificate_offset
        loader_string = '> L L 256s L L L 20s L 20s 16s 16s L 20s L L L'
        self.loader_header_size, self.loader_image_size, self.loader_rsa_sig, self.loader_unklength,\
            self.loader_image_flags, self.loader_load_address, self.loader_section_digest, self.loader_import_table_count,\
            self.loader_import_table_digest, self.loader_media_id, self.loader_file_key, self.loader_export_table,\
            self.loader_header_digest, self.loader_game_regions, self.loader_media_flags, self.section_count = \
            unpack(loader_string, self.data[self.data_counter:self.data_counter + calcsize(loader_string)])
        self.data_counter += calcsize(loader_string)

    def loader_show(self):
        self.line.output('XEX_LOADER')
        self.line.indent()
        self.line.output_hex8('HEADER_SIZE', self.loader_header_size, self.loader_header_size)
        self.line.output_hex8('IMAGE_SIZE', self.loader_image_size, self.loader_image_size)
        self.line.output('RSA_SIG', self.loader_rsa_sig)
        self.line.output('UNK_LENGTH', self.loader_unklength)
        self.line.output_hex8('IMAGE_FLAGS', self.loader_image_flags)
        self.line.output_hex8('LOAD_ADDRESS', self.loader_load_address)
        self.line.output('SECTION_DIGEST', self.loader_section_digest)
        self.line.output('IMPORT_TABLE_COUNT', self.loader_import_table_count)
        self.line.output('IMPORT_TABLE_DIGEST', self.loader_import_table_digest)
        self.line.output('MEDIA_ID', self.loader_media_id)
        self.line.output('FILE_KEY', self.loader_file_key)
        self.line.output('EXPORT_TABLE', self.loader_export_table)
        self.line.output('HEADER_DIGEST', self.loader_header_digest)
        self.line.output_hex8('GAME_REGIONS', self.loader_game_regions)
        self.line.output_hex8('MEDIA_FLAGS', self.loader_media_flags)
        self.line.outdent()

    def optional_headers_decode(self):
        optional_header_string = '>L L'
        for i in range(self.header_count):
            self.optional_headers.append(unpack(optional_header_string,
                self.data[self.data_counter:self.data_counter+calcsize(optional_header_string)]))
            self.data_counter += 8

    def optional_headers_reset(self):
        """To reset the optional headers to their default values."""
        self.optional_headers = []

    def sections_decode(self):
        """To decode the XEX sections.

        Offset | Bits	    | Type Information
        ---------|-----------|------------------------
        0x00  |  32       | Page size.
        0x20  |  4         | Section Type.
        0x24  |  28       | Page count.
        0x3C  |  160     | Digest."""
        section_string = '> L L 20s'
        for section in range(self.section_count):
            self.sections.append(unpack(section_string, self.data[self.data_counter:self.data_counter + calcsize(section_string)]))
            self.data_counter += calcsize(section_string)

    def sections_reset(self):
        """To reset the sections their default values."""
        self.sections = []

    def sections_show(self):
        self.line.output('XEX_SECTIONS', self.section_count)
        self.line.indent()
        for section in self.sections:
            self.line.output(self.hex8(section[0]), self.hex8(section[1]), section[2])
        self.line.outdent()

    def additional_title_memory_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ADDITIONAL_TITLE_MEMORY:
            pass

    def additional_title_memory_reset(self):
        """To reset the additional title memory to their default values."""
        pass

    def additional_title_memory_show(self):
        pass

    def alternate_title_ids_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ALTERNATE_TITLE_IDS:
            pass

    def alternate_title_ids_reset(self):
        """To reset the alternate title ids to their default values."""
        pass

    def alternate_title_ids_show(self):
        pass

    def base_reference_decode(self, header):
        if self.key(header) == const.XEX_HEADER_BASE_REFERENCE:
            pass

    def base_reference_reset(self):
        """To reset the base reference to their default values."""
        pass

    def base_reference_show(self):
        pass

    def bounding_path_decode(self, header):
        if self.key(header) == const.XEX_HEADER_BOUNDING_PATH:
            pass

    def bounding_path_reset(self):
        """To reset the bounding patch to their default values."""
        pass

    def bounding_path_show(self):
        pass

    def checksum_timestamp_decode(self, header):
        if self.key(header) == const.XEX_HEADER_CHECKSUM_TIMESTAMP:
            pass

    def checksum_timestamp_reset(self):
        """To reset the checksum timestamp to their default values."""
        pass

    def checksum_timestamp_show(self):
        pass

    def default_filesystem_cache_size_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_FILESYSTEM_CACHE_SIZE:
            pass

    def default_filesystem_cache_size_reset(self):
        """To reset the default filesystem cache size to their default values."""
        pass

    def default_filesystem_cache_size_show(self):
        pass

    def default_heap_size_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_HEAP_SIZE:
            self.exe_heap_size = unpack('>L', self.data[header[1]:header[1] + 4])[0]

    def default_heap_size_reset(self):
        """To reset the heap size to their default values."""
        self.exe_heap_size = 0

    def default_heap_size_show(self):
        self.line.output('XEX_HEADER_DEFAULT_HEAP_SIZE', self.exe_heap_size)

    def default_stack_size_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_STACK_SIZE:
            self.exe_stack_size = unpack('>L', self.data[header[1]:header[1] + 4])[0]

    def default_stack_size_reset(self):
        """To reset the default stack size to their default values."""
        self.exe_stack_size = 0

    def default_stack_size_show(self):
        self.line.output('XEX_HEADER_DEFAULT_STACK_SIZE', self.exe_stack_size)

    def delta_patch_descriptor_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DELTA_PATCH_DESCRIPTOR:
            pass

    def delta_patch_descriptor_reset(self):
        """To reset the delta patch descriptor to their default values."""
        pass

    def delta_patch_descriptor_show(self):
        pass

    def device_id_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_DEVICE_ID:
            pass

    def device_id_reset(self):
        """To reset the device id to their default values."""
        pass

    def device_id_show(self):
        pass

    def enabled_for_callcap_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ENABLED_FOR_CALLCAP:
            pass

    def enabled_for_callcap_reset(self):
        """To reset the enabled for callcap to their default values."""
        pass

    def enabled_for_callcap_show(self):
        pass

    def enabled_for_fastcap_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ENABLED_FOR_FASTCAP:
            pass

    def enabled_for_fastcap_reset(self):
        """To reset the enabled for fastcap to their default values."""
        pass

    def enabled_for_fastcap_show(self):
        pass

    def entry_point_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_ENTRY_POINT:
            self.exe_entry_point = header[1]

    def entry_point_reset(self):
        """To reset the entry point to their default values."""
        self.exe_entry_point = 0

    def entry_point_show(self):
        self.line.output_hex8('XEX_HEADER_ENTRY_POINT', self.exe_entry_point)

    def execution_info_decode(self, header):
        if self.key(header) == const.XEX_HEADER_EXECUTION_INFO:
            execution_info_string = '>L L L L B B B B L'
            self.media_id, self.version, self.base_version, self.title_id, self.platform, self.execution_table, \
            self.disk_number, self.disk_count, self.savegame_id = unpack(execution_info_string, self.data[header[1]:
                header[1] + calcsize(execution_info_string)])

    def execution_info_reset(self):
        """To reset the execution info to their default values."""
        self.media_id = 0
        self.version = 0
        self.base_version = 0
        self.title_id = 0
        self.platform = 0
        self.execution_table = 0
        self.disk_number = 0
        self.disk_count = 0
        self.savegame_id = 0

    def execution_info_show(self):
        self.line.output('XEX_HEADER_EXECUTION_INFO')
        self.line.indent()
        self.line.output('MEDIA_ID', self.media_id)
        self.line.output('VERSION', str(self.version))
        self.line.output('BASE_VERSION', str(self.base_version))
        self.line.output('TITLE_ID', str(self.title_id))
        self.line.output('PLATFORM', self.platform)
        self.line.output('EXECUTION_TABLE', self.execution_table)
        self.line.output('DISK_NUMBER', self.disk_number)
        self.line.output('DISK_COUNT', self.disk_count)
        self.line.output('SAVE_GAME_ID', self.savegame_id)
        self.line.outdent()

    def exports_by_name_decode(self, header):
        if self.key(header) == const.XEX_HEADER_EXPORTS_BY_NAME:
            pass

    def exports_by_name_reset(self):
        """To reset the exports by name to their default values."""
        pass

    def exports_by_name_show(self):
        pass

    def file_format_info_decode(self, header):
        if self.key(header) == const.XEX_HEADER_FILE_FORMAT_INFO:
            self.info_size, self.encryption_type, self.compression_type = unpack('> L H H ', self.data[header[1]:header[1] + 8])
            if self.compression_type == const.XEX_COMPRESSION_BASIC:
                self.block_cont = int((self.info_size - 8) / 8)
                self.blocks = []
                for i in range(self.block_cont):
                    self.blocks.append(unpack('> L L', self.data[header[1] + 8 + (i * 8): header[1] + 8 + (i * 8) + 8]))
            elif self.compression_type == const.XEX_COMPRESSION_NORMAL:
                self.window_size, self.block_size, self.block_hash = unpack('> L L 20s', self.data[header[1] + 8: header[1] + 36])

    def file_format_info_reset(self):
        """To reset the file format info to their default values."""
        self.info_size = 0
        self.encryption_type = 0
        self.compression_type = 0

    def file_format_info_show(self):
        self.line.output('XEX_HEADER_FILE_FORMAT_INFO')
        self.line.indent()
        self.line.output('SIZE', self.info_size)
        self.line.output('ENCRYPTION_TYPE', self.encryption_type,  const.XEX_ENCRYPTION[self.encryption_type])
        self.line.output('COMPRESSION_TYPE', self.compression_type, const.XEX_COMPRESSION[self.compression_type])
        self.line.outdent()

    def game_ratings_decode(self, header):
        if self.key(header) == const.XEX_HEADER_GAME_RATINGS:
            game_ratings_string = '> B B B B B B B B B B B B'
            self.esrb, self.pegi, self.pegifi, self.pegipt, self.bbfc, self.cero, self.usk, self.oflcau, \
            self.oflcnz, self.kmrb, self.brazil, self.fpb = unpack(game_ratings_string,
                self.data[header[1]:header[1] + calcsize(game_ratings_string)])

    def game_ratings_reset(self):
        """To reset the game ratings to their default values."""
        ## The game rating for ESRB (Entertainment Software Rating Board).
        self.esrb = const.XEX_RATING_ESRB_UNRATED
        ## The game rating for PEGI (Pan European Game Information).
        self.pegi = const.XEX_RATING_PEGI_UNRATED
        ## The game rating for PEGI (Pan European Game Information) - Finland.
        self.pegifi = const.XEX_RATING_PEGI_FI_UNRATED
        ## The game rating for PEGI (Pan European Game Information) - Portugal.
        self.pegipt = const.XEX_RATING_PEGI_PT_UNRATED
        ## The game rating for BBFC (British Board of Film Classification).
        self.bbfc = const.XEX_RATING_BBFC_UNRATED
        ## The game rating for CERO (Computer Entertainment Rating Organization).
        self.cero = const.XEX_RATING_CERO_UNRATED
        ## The game rating for USK (Unterhaltungssoftware SelbstKontrolle).
        self.usk = const.XEX_RATING_USK_UNRATED
        ## The game rating for OFLC (Office of Film and Literature Classification) - Australia.
        self.oflcau = const.XEX_RATING_OFLC_AU_UNRATED
        ## The game rating for OFLC (Office of Film and Literature Classification) - New Zealand.
        self.oflcnz = const.XEX_RATING_OFLC_NZ_UNRATED
        ## The game rating for KMRB (Korea Media Rating Board).
        self.kmrb = const.XEX_RATING_KMRB_UNRATED
        ## The game rating for Brazilian Advisory Rating System.
        self.brazil =const.XEX_RATING_BRAZIL_UNRATED
        ## The game rating for FPB (Film and Publication Board).
        self.fpb = const.XEX_RATING_FPB_UNRATED

    def game_ratings_show(self):
        """To display the game ratings."""
        self.line.output('XEX_HEADER_GAME_RATINGS')
        self.line.indent()

        if self.esrb == const.XEX_RATING_ESRB_eC:
            self.line.output_hex2('ESRB', self.esrb, 'XEX_RATING_ESRB_eC')
        elif self.esrb == const.XEX_RATING_ESRB_E:
            self.line.output_hex2('ESRB', self.esrb, 'XEX_RATING_ESRB_E')
        elif self.esrb == const.XEX_RATING_ESRB_E10:
            self.line.output_hex2('ESRB', self.esrb, 'XEX_RATING_ESRB_E10')
        elif self.esrb == const.XEX_RATING_ESRB_T:
            self.line.output_hex2('ESRB', self.esrb, 'XEX_RATING_ESRB_T')
        elif self.esrb == const.XEX_RATING_ESRB_M:
            self.line.output_hex2('ESRB', self.esrb, 'XEX_RATING_ESRB_M')
        elif self.esrb == const.XEX_RATING_ESRB_AO:
            self.line.output_hex2('ESRB', self.esrb, 'XEX_RATING_ESRB_AO')
        elif self.esrb == const.XEX_RATING_ESRB_UNRATED:
            self.line.output_hex2('ESRB', self.esrb, 'XEX_RATING_ESRB_UNRATED')

        if self.pegi == const.XEX_RATING_PEGI_3_PLUS:
            self.line.output_hex2('PEGI', self.pegi, 'XEX_RATING_PEGI_3_PLUS')
        elif self.pegi == const.XEX_RATING_PEGI_7_PLUS:
            self.line.output_hex2('PEGI', self.pegi, 'XEX_RATING_PEGI_7_PLUS')
        elif self.pegi == const.XEX_RATING_PEGI_12_PLUS:
            self.line.output_hex2('PEGI', self.pegi, 'XEX_RATING_PEGI_12_PLUS')
        elif self.pegi == const.XEX_RATING_PEGI_16_PLUS:
            self.line.output_hex2('PEGI', self.pegi, 'XEX_RATING_PEGI_16_PLUS')
        elif self.pegi == const.XEX_RATING_PEGI_18_PLUS:
            self.line.output_hex2('PEGI', self.pegi, 'XEX_RATING_PEGI_18_PLUS')
        elif self.pegi == const.XEX_RATING_PEGI_UNRATED:
            self.line.output_hex2('PEGI', self.pegi, 'XEX_RATING_PEGI_UNRATED')

        if self.pegifi == const.XEX_RATING_PEGI_FI_3_PLUS:
            self.line.output_hex2('PEGIFI', self.pegifi, 'XEX_RATING_PEGI_FI_3_PLUS')
        elif self.pegifi == const.XEX_RATING_PEGI_FI_7_PLUS:
            self.line.output_hex2('PEGIFI', self.pegifi, 'XEX_RATING_PEGI_FI_7_PLUS')
        elif self.pegifi == const.XEX_RATING_PEGI_FI_11_PLUS:
            self.line.output_hex2('PEGIFI', self.pegifi, 'XEX_RATING_PEGI_FI_11_PLUS')
        elif self.pegifi == const.XEX_RATING_PEGI_FI_15_PLUS:
            self.line.output_hex2('PEGIFI', self.pegifi, 'XEX_RATING_PEGI_FI_15_PLUS')
        elif self.pegifi == const.XEX_RATING_PEGI_FI_18_PLUS:
            self.line.output_hex2('PEGIFI', self.pegifi, 'XEX_RATING_PEGI_FI_18_PLUS')
        elif self.pegifi == const.XEX_RATING_PEGI_FI_UNRATED:
            self.line.output_hex2('PEGIFI', self.pegifi, 'XEX_RATING_PEGI_FI_UNRATED')

        if self.pegipt == const.XEX_RATING_PEGI_PT_4_PLUS:
            self.line.output_hex2('PEGIPT', self.pegipt, 'XEX_RATING_PEGI_PT_4_PLUS')
        elif self.pegipt == const.XEX_RATING_PEGI_PT_6_PLUS:
            self.line.output_hex2('PEGIPT', self.pegipt, 'XEX_RATING_PEGI_PT_6_PLUS')
        elif self.pegipt == const.XEX_RATING_PEGI_PT_12_PLUS:
            self.line.output_hex2('PEGIPT', self.pegipt, 'XEX_RATING_PEGI_PT_12_PLUS')
        elif self.pegipt == const.XEX_RATING_PEGI_PT_16_PLUS:
            self.line.output_hex2('PEGIPT', self.pegipt, 'XEX_RATING_PEGI_PT_16_PLUS')
        elif self.pegipt == const.XEX_RATING_PEGI_PT_18_PLUS:
            self.line.output_hex2('PEGIPT', self.pegipt, 'XEX_RATING_PEGI_PT_18_PLUS')
        elif self.pegipt == const.XEX_RATING_PEGI_PT_UNRATED:
            self.line.output_hex2('PEGIPT', self.pegipt, 'XEX_RATING_PEGI_PT_UNRATED')

        if self.bbfc == const.XEX_RATING_BBFC_UNIVERSAL:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_UNIVERSAL')
        elif self.bbfc == const.XEX_RATING_BBFC_PG:
            self.line.output_hex2('BBFC', self.bbfc,  'XEX_RATING_BBFC_PG')
        elif self.bbfc == const.XEX_RATING_BBFC_3_PLUS:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_3_PLUS')
        elif self.bbfc == const.XEX_RATING_BBFC_7_PLUS:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_7_PLUS')
        elif self.bbfc == const.XEX_RATING_BBFC_12_PLUS:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_12_PLUS')
        elif self.bbfc == const.XEX_RATING_BBFC_15_PLUS:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_15_PLUS')
        elif self.bbfc == const.XEX_RATING_BBFC_16_PLUS:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_16_PLUS')
        elif self.bbfc == const.XEX_RATING_BBFC_18_PLUS:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_18_PLUS')
        elif self.bbfc == const.XEX_RATING_BBFC_UNRATED:
            self.line.output_hex2('BBFC', self.bbfc, 'XEX_RATING_BBFC_UNRATED')

        if self.bbfc == const.XEX_RATING_CERO_A:
            self.line.output_hex2('CERO', self.bbfc, 'XEX_RATING_CERO_A')
        elif self.bbfc == const.XEX_RATING_CERO_B:
            self.line.output_hex2('CERO', self.bbfc, 'XEX_RATING_CERO_B')
        elif self.bbfc == const.XEX_RATING_CERO_C:
            self.line.output_hex2('CERO', self.bbfc, 'XEX_RATING_CERO_C')
        elif self.bbfc == const.XEX_RATING_CERO_D:
            self.line.output_hex2('CERO', self.bbfc, 'XEX_RATING_CERO_D')
        elif self.bbfc == const.XEX_RATING_CERO_Z:
            self.line.output_hex2('CERO', self.bbfc, 'XEX_RATING_CERO_Z')
        elif self.bbfc == const.XEX_RATING_CERO_UNRATED:
            self.line.output_hex2('CERO', self.bbfc, 'XEX_RATING_CERO_UNRATED')

        if self.usk == const.XEX_RATING_USK_ALL:
            self.line.output_hex2('USK', self.usk, 'XEX_RATING_USK_ALL')
        elif self.usk == const.XEX_RATING_USK_6_PLUS:
            self.line.output_hex2('USK', self.usk, 'XEX_RATING_USK_6_PLUS')
        elif self.usk == const.XEX_RATING_USK_12_PLUS:
            self.line.output_hex2('USK', self.usk, 'XEX_RATING_USK_12_PLUS')
        elif self.usk == const.XEX_RATING_USK_16_PLUS:
            self.line.output_hex2('USK', self.usk, 'XEX_RATING_USK_16_PLUS')
        elif self.usk == const.XEX_RATING_USK_18_PLUS:
            self.line.output_hex2('USK', self.usk, 'XEX_RATING_USK_18_PLUS')
        elif self.usk ==const.XEX_RATING_USK_UNRATED:
            self.line.output_hex2('USK', self.usk, 'XEX_RATING_USK_UNRATED')

        if self.oflcau == const.XEX_RATING_OFLC_AU_G:
            self.line.output_hex2('OFLCAU', self.oflcau, 'XEX_RATING_OFLC_AU_G')
        elif self.oflcau == const.XEX_RATING_OFLC_AU_PG:
            self.line.output_hex2('OFLCAU', self.oflcau, 'XEX_RATING_OFLC_AU_PG')
        elif self.oflcau == const.XEX_RATING_OFLC_AU_M:
            self.line.output_hex2('OFLCAU', self.oflcau, 'XEX_RATING_OFLC_AU_M')
        elif self.oflcau == const.XEX_RATING_OFLC_AU_MA15_PLUS:
            self.line.output_hex2('OFLCAU', self.oflcau, 'XEX_RATING_OFLC_AU_MA15_PLUS')
        elif self.oflcau == const.XEX_RATING_OFLC_AU_UNRATED:
            self.line.output_hex2('OFLCAU', self.oflcau, 'XEX_RATING_OFLC_AU_UNRATED')

        if self.oflcnz == const.XEX_RATING_OFLC_NZ_G:
            self.line.output_hex2('OFLCNZ', self.oflcnz, 'XEX_RATING_OFLC_NZ_G')
        elif self.oflcnz == const.XEX_RATING_OFLC_NZ_PG:
            self.line.output_hex2('OFLCNZ', self.oflcnz, 'XEX_RATING_OFLC_NZ_PG')
        elif self.oflcnz == const.XEX_RATING_OFLC_NZ_M:
            self.line.output_hex2('OFLCNZ', self.oflcnz, 'XEX_RATING_OFLC_NZ_M')
        elif self.oflcnz == const.XEX_RATING_OFLC_NZ_MA15_PLUS:
            self.line.output_hex2('OFLCNZ', self.oflcnz, 'XEX_RATING_OFLC_NZ_MA15_PLUS')
        elif self.oflcnz == const.XEX_RATING_OFLC_NZ_UNRATED:
            self.line.output_hex2('OFLCNZ', self.oflcnz, 'XEX_RATING_OFLC_NZ_UNRATED')

        if self.kmrb == const.XEX_RATING_KMRB_ALL:
            self.line.output_hex2('KMRB', self.kmrb, 'XEX_RATING_KMRB_ALL')
        elif self.kmrb == const.XEX_RATING_KMRB_12_PLUS:
            self.line.output_hex2('KMRB', self.kmrb, 'XEX_RATING_KMRB_12_PLUS')
        elif self.kmrb == const.XEX_RATING_KMRB_15_PLUS:
            self.line.output_hex2('KMRB', self.kmrb, 'XEX_RATING_KMRB_15_PLUS')
        elif self.kmrb == const.XEX_RATING_KMRB_18_PLUS:
            self.line.output_hex2('KMRB', self.kmrb, 'XEX_RATING_KMRB_18_PLUS')
        elif self.kmrb == const.XEX_RATING_KMRB_UNRATED:
            self.line.output_hex2('KMRB', self.kmrb, 'XEX_RATING_KMRB_UNRATED')

        if self.brazil == const.XEX_RATING_BRAZIL_ALL:
            self.line.output_hex2('BRAZIL', self.brazil, 'XEX_RATING_BRAZIL_ALL')
        elif self.brazil == const.XEX_RATING_BRAZIL_12_PLUS:
            self.line.output_hex2('BRAZIL', self.brazil, 'XEX_RATING_BRAZIL_12_PLUS')
        elif self.brazil == const.XEX_RATING_BRAZIL_14_PLUS:
            self.line.output_hex2('BRAZIL', self.brazil, 'XEX_RATING_BRAZIL_14_PLUS')
        elif self.brazil == const.XEX_RATING_BRAZIL_16_PLUS:
            self.line.output_hex2('BRAZIL', self.brazil, 'XEX_RATING_BRAZIL_16_PLUS')
        elif self.brazil == const.XEX_RATING_BRAZIL_18_PLUS:
            self.line.output_hex2('BRAZIL', self.brazil, 'XEX_RATING_BRAZIL_18_PLUS')
        elif self.brazil == const.XEX_RATING_BRAZIL_UNRATED:
            self.line.output_hex2('BRAZIL', self.brazil, 'XEX_RATING_BRAZIL_UNRATED')

        if self.fpb == const.XEX_RATING_FPB_ALL:
            self.line.output_hex2('FPB', self.fpb, 'XEX_RATING_FPB_ALL')
        elif self.fpb == const.XEX_RATING_FPB_PG:
            self.line.output_hex2('FPB', self.fpb, 'XEX_RATING_FPB_PG')
        elif self.fpb == const.XEX_RATING_FPB_10_PLUS:
            self.line.output_hex2('FPB', self.fpb, 'XEX_RATING_FPB_10_PLUS')
        elif self.fpb == const.XEX_RATING_FPB_13_PLUS:
            self.line.output_hex2('FPB', self.fpb, 'XEX_RATING_FPB_13_PLUS')
        elif self.fpb == const.XEX_RATING_FPB_16_PLUS:
            self.line.output_hex2('FPB', self.fpb, 'XEX_RATING_FPB_16_PLUS')
        elif self.fpb == const.XEX_RATING_FPB_18_PLUS:
            self.line.output_hex2('FPB', self.fpb, 'XEX_RATING_FPB_18_PLUS')
        elif self.fpb == const.XEX_RATING_FPB_UNRATED:
            self.line.output_hex2('FPB', self.fpb, 'XEX_RATING_FPB_UNRATED')

        self.line.outdent()

    def image_base_address_decode(self, header):
        if self.key(header) == const.XEX_HEADER_IMAGE_BASE_ADDRESS:
            self.exe_address = header[1]

    def image_base_address_reset(self):
        """To reset the image base address to their default values."""
        self.exe_address = 0

    def image_base_address_show(self):
        self.line.output_hex8('XEX_HEADER_IMAGE_BASE_ADDRESS', self.exe_address)

    def import_libraries_decode(self, header):
        if self.key(header) == const.XEX_HEADER_IMPORT_LIBRARIES:
            pass

    def import_libraries_reset(self):
        """To reset the import libraries to their default values."""
        pass

    def import_libraries_show(self):
        pass

    def lan_key_decode(self, header):
        if self.key(header) == const.XEX_HEADER_LAN_KEY:
            pass

    def lan_key_reset(self):
        """To reset the LAN key to their default values."""
        pass

    def lan_key_show(self):
        pass

    def multidisc_media_ids_decode(self, header):
        if self.key(header) == const.XEX_HEADER_MULTIDISC_MEDIA_IDS:
            pass

    def multidisc_media_ids_reset(self):
        """To reset the multidisc media ids to their default values."""
        pass

    def multidisc_media_ids_show(self):
        pass

    def original_base_address_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ORIGINAL_BASE_ADDRESS:
            pass

    def original_base_address_reset(self):
        """To reset the original base address to their default values."""
        pass

    def original_base_address_show(self):
        pass

    def original_pe_name_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ORIGINAL_PE_NAME:
            name_length = unpack('>L', self.data[header[1]:header[1] + 4])[0]
            self.original_pe_name = self.data[header[1] + 4:header[1] + 4 + name_length - 1].decode()

    def original_pe_name_reset(self):
        """To reset the original PE name to their default values."""
        self.original_pe_name = ''

    def original_pe_name_show(self):
        self.line.output('XEX_HEADER_ORIGINAL_PE_NAME', self.original_pe_name)

    def page_heap_size_and_flags_decode(self, header):
        if self.key(header) == const.XEX_HEADER_PAGE_HEAP_SIZE_AND_FLAGS:
            pass

    def page_heap_size_and_flags_reset(self):
        """To reset the page heap size and flags to their default values."""
        pass

    def page_heap_size_and_flags_show(self):
        pass

    def resource_info_decode(self, header):
        if self.key(header) == const.XEX_HEADER_RESOURCE_INFO:
            self.resource_info_count = int((header[0] - 4) / 16)
            self.resource_infos = []
            for i in range(self.resource_info_count):
                self.resource_infos.append(unpack('>8s L L', self.data[header[1] + 4 + (i * 16):header[1] + 20 + (i * 16)]))

    def resource_info_reset(self):
        """To reset the resource infomation to their default values."""
        self.resource_info_count = 0

    def resource_info_show(self):
        self.line.output('XEX_HEADER_RESOURCE_INFO', self.resource_info_count)

    def static_libraries_decode(self, header):
        if self.key(header) == const.XEX_HEADER_STATIC_LIBRARIES:
            pass

    def static_libraries_reset(self):
        """To reset the statics libraries to their default values."""
        pass

    def static_libraries_show(self):
        pass

    def system_flags_decode(self, header):
        if self.key(header) == const.XEX_HEADER_SYSTEM_FLAGS:
            self.system_flags = header[1]

    def system_flags_reset(self):
        """To reset the system flags to their default values."""
        self.system_flags = 0

    def system_flags_show(self):
        self.line.output_hex8('XEX_HEADER_SYSTEM_FLAGS', self.system_flags)

    def title_workspace_size_decode(self, header):
        if self.key(header) == const.XEX_HEADER_TITLE_WORKSPACE_SIZE:
            pass

    def title_workspace_size_reset(self):
        """To reset the title workspace to their default values."""
        pass

    def title_workspace_size_show(self):
        pass

    def tls_info_decode(self, header):
        if self.key(header) == const.XEX_HEADER_TLS_INFO:
            tls_string = '>L L L L'
            self.tls_slot_count, self.tls_raw_data_address, self.tls_data_size, self.tls_raw_data_size = unpack(
                tls_string, self.data[header[1]:header[1] + calcsize(tls_string)])

    def tls_info_reset(self):
        """To reset the TLS information to their default values."""
        self.tls_slot_count = 0
        self.tls_raw_data_address = 0
        self.tls_data_size = 0
        self.tls_raw_data_size = 0

    def tls_info_show(self):
        self.line.output('XEX_HEADER_TLS_INFO')
        self.line.indent()
        self.line.output('TLS_SLOT_COUNT', self.tls_slot_count)
        self.line.output_hex8('TLS_RAW_DATA_ADDRESS', self.tls_raw_data_address)
        self.line.output('TLS_RAW_DATA_SIZE', self.tls_raw_data_size)
        self.line.output('TLS_DATA_SIZE', self.tls_data_size)
        self.line.outdent()

    def xbox360_logo_decode(self, header):
        if self.key(header) == const.XEX_HEADER_XBOX360_LOGO:
            pass

    def xbox360_logo_reset(self):
        """To reset the XBOX 360 logo to their default values."""
        pass

    def xbox360_logo_show(self):
        pass

    def decrypt_header_key(self):
        cipher = AES.new(self.XEX_RETAIL_KEY)
        cipher.block_size = 16
        return cipher.decrypt(self.loader_file_key)

    def convert_virtual_address(self, address):
        return address - self.exe_address
