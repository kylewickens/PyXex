import const
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

const.XEX_HEADER_BASE_REFERENCE = 0x00000405
const.XEX_HEADER_DEFAULT_STACK_SIZE = 0x00020200
const.XEX_HEADER_DEFAULT_HEAP_SIZE = 0x00020401
const.XEX_HEADER_DELTA_PATCH_DESCRIPTOR = 0x000005FF
const.XEX_HEADER_ENTRY_POINT = 0x00010100
const.XEX_HEADER_EXECUTION_INFO = 0x00040006
const.XEX_HEADER_FILE_FORMAT_INFO = 0x000003FF
const.XEX_HEADER_GAME_RATINGS = 0x00040310
const.XEX_HEADER_IMAGE_BASE_ADDRESS = 0x00010201
const.XEX_HEADER_ORIGINAL_PE_NAME = 0x000183FF
const.XEX_HEADER_RESOURCE_INFO = 0x000002FF
const.XEX_HEADER_SYSTEM_FLAGS = 0x00030000
const.XEX_HEADER_TLS_INFO = 0x00020104

class Xex:

    RETAIL_KEY = b'\x20\xB1\x85\xA5\x9D\x28\xFD\xC3\40\x58\x3F\xBB\x08\x96\xBF\x91'

    def __init__(self, filename):
        self.data_counter = 0
        self.optional_headers = []
        self.sections = []
        if not filename:
            print('invalid xex provided')
            exit(1)

        self.base_reference_reset()
        self.default_heap_size_reset()
        self.default_stack_size_reset()
        self.delta_patch_descriptor_reset()
        self.entry_point_reset()
        self.execution_info_reset()
        self.file_format_info_reset()
        self.game_ratings_reset()
        self.image_base_address_reset()
        self.original_pe_name_reset()
        self.resource_info_reset()
        self.system_flags_reset()
        self.tls_info_reset()

        self.data = open(filename, 'rb').read()

        self.header_decode()
        self.optional_headers_decoder()

        for optional_header in self.optional_headers:
            self.base_reference_decode(optional_header)
            self.default_stack_size_decode(optional_header)
            self.default_heap_size_decode(optional_header)
            self.delta_patch_descriptor_decode(optional_header)
            self.entry_point_decode(optional_header)
            self.execution_info_decode(optional_header)
            self.file_format_info_decode(optional_header)
            self.game_ratings_decode(optional_header)
            self.image_base_address_decode(optional_header)
            self.original_pe_name_decode(optional_header)
            self.resource_info_decode(optional_header)
            self.system_flags_decode(optional_header)
            self.tls_info_decode(optional_header)

        self.data_counter = self.cert_offset
        loader_string = '> L L 256s L L L 20s L 20s 16s 16s L 20s L L L'
        self.loader_header_size, self.loader_image_size, self.loader_rsa_sig, self.loader_unklength,\
        self.loader_image_flags, self.loader_load_address, self.loader_section_digest, self.loader_import_table_count,\
        self.loader_import_table_digest, self.loader_media_id, self.loader_file_key, self.loader_export_table,\
        self.loader_header_digest, self.loader_game_regions, self.loader_media_flags, self.section_count = \
            unpack(loader_string, self.data[self.data_counter:self.data_counter + calcsize(loader_string)])
        self.data_counter += calcsize(loader_string)

        section_string = '> L L 20s'
        for section in range(self.section_count):
            self.sections.append(unpack(section_string, self.data[self.data_counter:self.data_counter + calcsize(section_string)]))
            self.data_counter += calcsize(section_string)

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
        print('XEX_HEADER')
        print('  SIGNATURE =',  self.signature)
        print('  MODULE_FLAGS =',  self.hex8(self.module_flags))
        print('  EXE_OFFSET =',  self.hex8(self.exe_offset),  self.exe_offset)
        print('  UNKNOWN =',  self.unk)
        print('  CERT_OFFSET =',  self.hex8(self.cert_offset),  self.cert_offset)
        print('  OPTIONAL_HEADER_COUNT =',  self.header_count)

    def optional_headers_decoder(self):
        optional_header_string = '>L L'
        for i in range(self.header_count):
            self.optional_headers.append(unpack(optional_header_string,
                                                self.data[self.data_counter:self.data_counter+calcsize(optional_header_string)]))
            self.data_counter += 8

    def base_reference_decode(self, header):
        if self.key(header) == const.XEX_HEADER_BASE_REFERENCE:
            pass

    def base_reference_reset(self):
        pass

    def base_reference_show(self):
        pass

    def default_heap_size_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_HEAP_SIZE:
            self.exe_heap_size = unpack('>L', self.data[header[1]:header[1] + 4])[0]

    def default_heap_size_reset(self):
        self.exe_heap_size = 0

    def default_heap_size_show(self):
        print('XEX_HEADER_DEFAULT_HEAP_SIZE =',  self.exe_heap_size)

    def default_stack_size_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_DEFAULT_STACK_SIZE:
            self.exe_stack_size = unpack('>L', self.data[header[1]:header[1] + 4])[0]

    def default_stack_size_reset(self):
        self.exe_stack_size = 0

    def default_stack_size_show(self):
        print('XEX_HEADER_DEFAULT_STACK_SIZE =',  self.exe_stack_size)

    def delta_patch_descriptor_decode(self, header):
        if self.key(header) == const.XEX_HEADER_DELTA_PATCH_DESCRIPTOR:
            pass

    def delta_patch_descriptor_reset(self):
        pass

    def delta_patch_descriptor_show(self):
        pass

    def entry_point_decode(self,  header):
        if self.key(header) == const.XEX_HEADER_ENTRY_POINT:
            self.entry_point = header[1]

    def entry_point_reset(self):
        self.entry_point = 0

    def entry_point_show(self):
        print('XEX_HEADER_ENTRY_POINT =',  self.hex8(self.entry_point))

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
        print('XEX_HEADER_EXECUTION_INFO')
        print('  MEDIA_ID =',  self.media_id)
        print('  VERSION =',  str(self.version))
        print('  BASE_VERSION =',  str(self.base_version))
        print('  TITLE_ID =',  str(self.title_id))
        print('  PLATFORM =',  self.platform)
        print('  EXECUTION_TABLE =',  self.execution_table)
        print('  DISK_NUMBER =',  self.disk_number)
        print('  DISK_COUNT =',  self.disk_count)
        print('  SAVE_GAME_ID =',  self.savegame_id)

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
        print('XEX_HEADER_FILE_FORMAT_INFO')
        print('  SIZE =', self.info_size)
        print('  ENCRYPTION_TYPE =', self.encryption_type,  const.XEX_ENCRYPTION[self.encryption_type])
        print('  COMPRESSION_TYPE =', self.compression_type, const.XEX_COMPRESSION[self.compression_type])

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
        print('XEX_HEADER_GAME_RATINGS')
        print('  ESRB =',  self.esrb)
        print('  PEGI =',  self.pegi)
        print('  PEGIFI =',  self.pegifi)
        print('  PEGIPT =',  self.pegipt)
        print('  BBFC =',  self.bbfc)
        print('  CERO =',  self.cero)
        print('  USK =',  self.usk)
        print('  OFLCAU =',  self.oflcau)
        print('  OFLCNZ =',  self.oflcnz)
        print('  MRB =',  self.mrb)
        print('  BRAZIL =',  self.brazil)
        print('  FPB =',  self.fpb)

    def image_base_address_decode(self, header):
        if self.key(header) == const.XEX_HEADER_IMAGE_BASE_ADDRESS:
            self.base_image_address = header[1]

    def image_base_address_reset(self):
        self.base_image_address = 0

    def image_base_address_show(self):
        print('XEX_HEADER_IMAGE_BASE_ADDRESS =',  self.hex8(self.base_image_address))

    def original_pe_name_decode(self, header):
        if self.key(header) == const.XEX_HEADER_ORIGINAL_PE_NAME:
            name_length = unpack('>L', self.data[header[1]:header[1] + 4])[0]
            self.original_pe_name = self.data[header[1] + 4:header[1] + 4 + name_length - 1].decode()

    def original_pe_name_reset(self):
        self.original_pe_name = ''

    def original_pe_name_show(self):
        print('XEX_HEADER_ORIGINAL_PE_NAME =',  self.original_pe_name)

    def resource_info_decode(self, header):
        if self.key(header) == const.XEX_HEADER_RESOURCE_INFO:
            self.resource_info_count = int((header[0] - 4) / 16)
            self.resource_infos = []
            for i in range(self.resource_info_count):
                self.resource_infos.append(unpack('>8s L L', self.data[header[1] + 4 + (i * 16):header[1] + 20 + (i * 16)]))

    def resource_info_reset(self):
        self.resource_info_count = 0

    def resource_info_show(self):
        print('XEX_HEADER_RESOURCE_INFO =',  self.resource_info_count)

    def system_flags_decode(self, header):
        if self.key(header) == const.XEX_HEADER_SYSTEM_FLAGS:
            self.system_flags = header[1]

    def system_flags_reset(self):
         self.system_flags = 0

    def system_flags_show(self):
         print('XEX_HEADER_SYSTEM_FLAGS',  self.hex8(self.system_flags))

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
        print('XEX_HEADER_TLS_INFO')
        print('  TLS_SLOT_COUNT =',  self.tls_slot_count)
        print('  TLS_RAW_DATA_ADDRESS =',  self.hex8(self.tls_raw_data_address))
        print('  TLS_RAW_DATA_SIZE =',  self.tls_raw_data_size)
        print('  TLS_DATA_SIZE =',  self.tls_data_size)

    def decrypt_header_key(self):
        cipher = AES.new(self.RETAIL_KEY)
        cipher.block_size = 16
        return cipher.decrypt(self.loader_file_key)

    def convert_virtual_address(self, address):
        return address - self.base_image_address
