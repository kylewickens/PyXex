import const
from indents import Indents
from struct import *
from Crypto.Cipher import AES

const.XEX_COMPRESSION = [
    'XEX_COMPRESSION_NONE',
    'XEX_COMPRESSION_BASIC',
    'XEX_COMPRESSION_NORMAL',
    'XEX_COMPRESSION_DELTA' ]

const.XEX_COMPRESSION_NONE = 0
const.XEX_COMPRESSION_BASIC = 1
const.XEX_COMPRESSION_NORMAL = 2
const.XEX_COMPRESSION_DELTA = 3

const.XEX_ENCRYPTION = [
    'XEX_ENCRYPTION_NONE',
    'XEX_ENCRYPTION_NORMAL' ]

const.XEX_ENCRYPTION_NONE = 0
const.XEX_ENCRYPTION_NORMAL = 1

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
const.XEX_HEADER_ORIGINAL_BASE_ADDRESS = 0x00010001
const.XEX_HEADER_ORIGINAL_PE_NAME = 0x000183FF
const.XEX_HEADER_PAGE_HEAP_SIZE_AND_FLAGS = 0x00028002
const.XEX_HEADER_RESOURCE_INFO = 0x000002FF
const.XEX_HEADER_STATIC_LIBRARIES = 0x000200FF
const.XEX_HEADER_SYSTEM_FLAGS = 0x00030000
const.XEX_HEADER_TITLE_WORKSPACE_SIZE = 0x00040201
const.XEX_HEADER_TLS_INFO = 0x00020104


const.XEX_HEADER_LAN_KEY = 0x00040404
const.XEX_HEADER_XBOX360_LOGO = 0x000405FF
const.XEX_HEADER_MULTIDISC_MEDIA_IDS = 0x000406FF

class Xex:

    RETAIL_KEY = b'\x20\xB1\x85\xA5\x9D\x28\xFD\xC3\x40\x58\x3F\xBB\x08\x96\xBF\x91'
    DEVKIT_KEY = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self, filename):
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
        self.original_base_address_reset()
        self.original_pe_name_reset()
        self.page_heap_size_and_flags_reset()
        self.resource_info_reset()
        self.static_libraries_reset()
        self.system_flags_reset()
        self.title_workspace_size_reset()
        self.tls_info_reset()

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
            self.original_base_address_decode(optional_header)
            self.original_pe_name_decode(optional_header)
            self.page_heap_size_and_flags_decode(optional_header)
            self.resource_info_decode(optional_header)
            self.static_libraries_decode(optional_header)
            self.system_flags_decode(optional_header)
            self.title_workspace_size_decode(optional_header)
            self.tls_info_decode(optional_header)

        self.loader_decode()
        self.sections_decode()

    def key(self, header):
        return header[0]

    def hex8(self, value):
        return '0x' + format(value,  '08x')

    def header_decode(self):
        header_sting = '>4s L L L L L'
        self.data_counter = calcsize(header_sting)
        self.signature, self.module_flags, self.exe_offset, self.unk, self.cert_offset, self.header_count \
            = unpack(header_sting, self.data[0:self.data_counter])
        if self.signature != b'XEX2':
            print('signature mismatch', self.signature)
            exit(1)

    def header_show(self):
        self.line.output('XEX_HEADER')
        self.line.indent()
        self.line.output('SIGNATURE', self.signature)
        self.line.output('MODULE_FLAGS', self.hex8(self.module_flags))
        self.line.output('EXE_OFFSET', self.hex8(self.exe_offset), self.exe_offset)
        self.line.output('UNK', self.unk)
        self.line.output('CERT_OFFSET', self.hex8(self.cert_offset), self.cert_offset)
        self.line.output('OPTIONAL_HEADER_COUNT', self.header_count)
        self.line.outdent()

    def loader_decode(self):
        self.data_counter = self.cert_offset
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
        self.line.output('HEADER_SIZE', self.hex8(self.loader_header_size), self.loader_header_size)
        self.line.output('IMAGE_SIZE', self.hex8(self.loader_image_size), self.loader_image_size)
        self.line.output('RSA_SIG', self.loader_rsa_sig)
        self.line.output('UNK_LENGTH', self.loader_unklength)
        self.line.output('IMAGE_FLAGS', self.hex8(self.loader_image_flags))
        self.line.output('LOAD_ADDRESS', self.hex8(self.loader_load_address))
        self.line.output('SECTION_DIGEST', self.loader_section_digest)
        self.line.output('IMPORT_TABLE_COUNT', self.loader_import_table_count)
        self.line.output('IMPORT_TABLE_DIGEST', self.loader_import_table_digest)
        self.line.output('MEDIA_ID', self.loader_media_id)
        self.line.output('FILE_KEY', self.loader_file_key)
        self.line.output('EXPORT_TABLE', self.loader_export_table)
        self.line.output('HEADER_DIGEST', self.loader_header_digest)
        self.line.output('GAME_REGIONS', self.hex8(self.loader_game_regions))
        self.line.output('MEDIA_FLAGS', self.hex8(self.loader_media_flags))
        self.line.outdent()

    def optional_headers_decode(self):
        optional_header_string = '>L L'
        for i in range(self.header_count):
            self.optional_headers.append(unpack(optional_header_string,
                 self.data[self.data_counter:self.data_counter+calcsize(optional_header_string)]))
            self.data_counter += 8

    def optional_headers_reset(self):
        self.optional_headers = []

    def sections_decode(self):
        section_string = '> L L 20s'
        for section in range(self.section_count):
            self.sections.append(unpack(section_string, self.data[self.data_counter:self.data_counter + calcsize(section_string)]))
            self.data_counter += calcsize(section_string)

    def sections_reset(self):
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
        pass

    def additional_title_memory_show(self):
        pass

    def alternate_title_ids_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ALTERNATE_TITLE_IDS:
            pass

    def alternate_title_ids_reset(self):
        pass

    def alternate_title_ids_show(self):
        pass

    def base_reference_decode(self, header):
        if self.key(header) == const.XEX_HEADER_BASE_REFERENCE:
            pass

    def base_reference_reset(self):
        pass

    def base_reference_show(self):
        pass

    def bounding_path_decode(self, header):
        if self.key(header) == const.XEX_HEADER_BOUNDING_PATH:
            pass

    def bounding_path_reset(self):
        pass

    def bounding_path_show(self):
        pass

    def checksum_timestamp_decode(self, header):
        if self.key(header) == const.XEX_HEADER_CHECKSUM_TIMESTAMP:
            pass

    def checksum_timestamp_reset(self):
        pass

    def checksum_timestamp_show(self):
        pass

    def default_filesystem_cache_size_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_FILESYSTEM_CACHE_SIZE:
            pass

    def default_filesystem_cache_size_reset(self):
        pass

    def default_filesystem_cache_size_show(self):
        pass

    def default_heap_size_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_HEAP_SIZE:
            self.exe_heap_size = unpack('>L', self.data[header[1]:header[1] + 4])[0]

    def default_heap_size_reset(self):
        self.exe_heap_size = 0

    def default_heap_size_show(self):
        self.line.output('XEX_HEADER_DEFAULT_HEAP_SIZE', self.exe_heap_size)

    def default_stack_size_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_STACK_SIZE:
            self.exe_stack_size = unpack('>L', self.data[header[1]:header[1] + 4])[0]

    def default_stack_size_reset(self):
        self.exe_stack_size = 0

    def default_stack_size_show(self):
        self.line.output('XEX_HEADER_DEFAULT_STACK_SIZE', self.exe_stack_size)

    def delta_patch_descriptor_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DELTA_PATCH_DESCRIPTOR:
            pass

    def delta_patch_descriptor_reset(self):
        pass

    def delta_patch_descriptor_show(self):
        pass

    def device_id_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_DEVICE_ID:
            pass

    def device_id_reset(self):
        pass

    def device_id_show(self):
        pass

    def enabled_for_callcap_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ENABLED_FOR_CALLCAP:
            pass

    def enabled_for_callcap_reset(self):
        pass

    def enabled_for_callcap_show(self):
        pass

    def enabled_for_fastcap_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ENABLED_FOR_FASTCAP:
            pass

    def enabled_for_fastcap_reset(self):
        pass

    def enabled_for_fastcap_show(self):
        pass

    def entry_point_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_ENTRY_POINT:
            self.exe_entry_point = header[1]

    def entry_point_reset(self):
        self.exe_entry_point = 0

    def entry_point_show(self):
        self.line.output('XEX_HEADER_ENTRY_POINT', self.hex8(self.exe_entry_point))

    def execution_info_decode(self, header):
        if self.key(header) == const.XEX_HEADER_EXECUTION_INFO:
            execution_info_string = '>L L L L B B B B L'
            self.media_id, self.version, self.base_version, self.title_id, self.platform, self.execution_table, \
            self.disk_number, self.disk_count, self.savegame_id = unpack(execution_info_string, self.data[header[1]:
                header[1] + calcsize(execution_info_string)])

    def execution_info_reset(self):
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
            self.oflcnz, self.mrb, self.brazil, self.fpb = unpack(game_ratings_string,
                self.data[header[1]:header[1] + calcsize(game_ratings_string)])

    def game_ratings_reset(self):
        self.esrb = 0
        self.pegi = 0
        self.pegifi = 0
        self.pegipt = 0
        self.bbfc = 0
        self.cero = 0
        self.usk = 0
        self.oflcau = 0
        self.oflcnz = 0
        self.mrb = 0
        self.brazil = 0
        self.fpb = 0

    def game_ratings_show(self):
        self.line.output('XEX_HEADER_GAME_RATINGS')
        self.line.indent()
        self.line.output('ESRB', self.esrb)
        self.line.output('PEGI', self.pegi)
        self.line.output('PEGIFI', self.pegifi)
        self.line.output('PEGIPT', self.pegipt)
        self.line.output('BBFC', self.bbfc)
        self.line.output('CERO', self.cero)
        self.line.output('USK', self.usk)
        self.line.output('OFLCAU', self.oflcau)
        self.line.output('OFLCNZ', self.oflcnz)
        self.line.output('MRB', self.mrb)
        self.line.output('BRAZIL', self.brazil)
        self.line.output('FPB', self.fpb)
        self.line.outdent()

    def image_base_address_decode(self, header):
        if self.key(header) == const.XEX_HEADER_IMAGE_BASE_ADDRESS:
            self.exe_address = header[1]

    def image_base_address_reset(self):
        self.exe_address = 0

    def image_base_address_show(self):
        self.line.output('XEX_HEADER_IMAGE_BASE_ADDRESS', self.hex8(self.exe_address))

    def import_libraries_decode(self, header):
        if self.key(header) == const.XEX_HEADER_IMPORT_LIBRARIES:
            pass

    def import_libraries_reset(self):
        pass

    def import_libraries_show(self):
        pass

    def original_base_address_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ORIGINAL_BASE_ADDRESS:
            pass

    def original_base_address_reset(self):
        pass

    def original_base_address_show(self):
        pass

    def original_pe_name_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ORIGINAL_PE_NAME:
            name_length = unpack('>L', self.data[header[1]:header[1] + 4])[0]
            self.original_pe_name = self.data[header[1] + 4:header[1] + 4 + name_length - 1].decode()

    def original_pe_name_reset(self):
        self.original_pe_name = ''

    def original_pe_name_show(self):
        self.line.output('XEX_HEADER_ORIGINAL_PE_NAME', self.original_pe_name)

    def page_heap_size_and_flags_decode(self, header):
        if self.key(header) == const.XEX_HEADER_PAGE_HEAP_SIZE_AND_FLAGS:
            pass

    def page_heap_size_and_flags_reset(self):
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
        self.resource_info_count = 0

    def resource_info_show(self):
        self.line.output('XEX_HEADER_RESOURCE_INFO', self.resource_info_count)

    def static_libraries_decode(self, header):
        if self.key(header) == const.XEX_HEADER_STATIC_LIBRARIES:
            pass

    def static_libraries_reset(self):
        pass

    def static_libraries_show(self):
        pass

    def system_flags_decode(self, header):
        if self.key(header) == const.XEX_HEADER_SYSTEM_FLAGS:
            self.system_flags = header[1]

    def system_flags_reset(self):
         self.system_flags = 0

    def system_flags_show(self):
         self.line.output('XEX_HEADER_SYSTEM_FLAGS', self.hex8(self.system_flags))

    def title_workspace_size_decode(self, header):
        if self.key(header) == const.XEX_HEADER_TITLE_WORKSPACE_SIZE:
            pass

    def title_workspace_size_reset(self):
        pass

    def title_workspace_size_show(self):
        pass

    def tls_info_decode(self, header):
        if self.key(header) == const.XEX_HEADER_TLS_INFO:
            tls_string = '>L L L L'
            self.tls_slot_count, self.tls_raw_data_address, self.tls_data_size, self.tls_raw_data_size = unpack(
                tls_string, self.data[header[1]:header[1] + calcsize(tls_string)])

    def tls_info_reset(self):
        self.tls_slot_count = 0
        self.tls_raw_data_address = 0
        self.tls_data_size = 0
        self.tls_raw_data_size = 0

    def tls_info_show(self):
        self.line.output('XEX_HEADER_TLS_INFO')
        self.line.indent()
        self.line.output('TLS_SLOT_COUNT', self.tls_slot_count)
        self.line.output('TLS_RAW_DATA_ADDRESS', self.hex8(self.tls_raw_data_address))
        self.line.output('TLS_RAW_DATA_SIZE', self.tls_raw_data_size)
        self.line.output('TLS_DATA_SIZE', self.tls_data_size)
        self.line.outdent()

    def decrypt_header_key(self):
        cipher = AES.new(self.RETAIL_KEY)
        cipher.block_size = 16
        return cipher.decrypt(self.loader_file_key)

    def convert_virtual_address(self, address):
        return address - self.exe_address
