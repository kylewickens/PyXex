#!/usr/bin/python3

import sys
from xex import  Xex

if __name__ == '__main__':
    x = Xex(sys.argv[1])

    x.header_show()
    x.sections_show()
    x.loader_show()

    x.base_reference_show()
    x.default_heap_size_show()
    x.default_stack_size_show()
    x.delta_patch_descriptor_show()
    x.entry_point_show()
    x.execution_info_show()
    x.file_format_info_show()
    x.game_ratings_show()
    x.image_base_address_show()
    x.original_pe_name_show()
    x.resource_info_show()
    x.system_flags_show()
    x.tls_info_show()