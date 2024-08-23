#imports
import os
import time
import PyPDF2
from docx import Document
from oletools.olevba import VBA_Parser
import pefile
from tabulate import tabulate

try:
    import Pyth3rNalisis.modules.module_log as module_log
except:
    import modules.module_log as module_log

def check_file_metadata(file_path):
    data = []
    try:
        file_stats = os.stat(file_path)
        file_size = file_stats.st_size
        creation_time = time.ctime(file_stats.st_ctime)
        modification_time = time.ctime(file_stats.st_mtime)

        data.append(("File Size", f"{file_size} bytes"))
        data.append(("Creation Time", creation_time))
        data.append(("Modification Time", modification_time))

        if 0 == file_size:
            data.append(("Warning", "The file is empty."))
        if 60 * 60 * 24 > time.time() - file_stats.st_ctime:
            data.append(("Info", "The file was created recently."))

    except Exception as e:
        data.append(("Error", f"Unable to access file metadata: {e}"))

    return data

def check_pdf_metadata(file_path):
    data = []
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            metadata = pdf_reader.metadata

            if metadata:
                for key, value in metadata.items():
                    data.append((key, value))
                    if "/Author" == key and "unknown" in value.lower():
                        data.append(("Warning", f"Suspicious author name found: {value}"))
            else:
                data.append(("Info", "No metadata found in this PDF file."))

    except Exception as e:
        data.append(("Error", f"Unable to access PDF metadata: {e}"))

    return data

def check_docx_metadata(file_path):
    data = []
    try:
        doc = Document(file_path)
        core_properties = doc.core_properties

        data.append(("Title", core_properties.title))
        data.append(("Author", core_properties.author))
        data.append(("Last Modified By", core_properties.last_modified_by))
        data.append(("Created", str(core_properties.created)))
        data.append(("Modified", str(core_properties.modified)))

        if "unknown" == core_properties.author.lower():
            data.append(("Warning", f"Suspicious author name found: {core_properties.author}"))

    except Exception as e:
        data.append(("Error", f"Unable to access DOCX metadata: {e}"))

    return data

def check_ole_metadata(file_path):
    data = []
    try:
        vba_parser = VBA_Parser(file_path)
        metadata = vba_parser.ole_file.get_metadata()

        for key, value in metadata.__dict__.items():
            if value:
                data.append((key, value))
                if "last_saved_by" == key and "unknown" in value.lower():
                    data.append(("Warning", f"Suspicious 'Last Saved By' found: {value}"))

    except Exception as e:
        data.append(("Error", f"Unable to access OLE metadata: {e}"))

    return data

def check_exe_metadata(file_path):
    data = []
    try:
        pe = pefile.PE(file_path)

        data.append(("Time Date Stamp", pe.FILE_HEADER.TimeDateStamp))
        data.append(("Number of Sections", pe.FILE_HEADER.NumberOfSections))
        data.append(("Machine", pe.FILE_HEADER.Machine))

        if 0x50000000 > pe.FILE_HEADER.TimeDateStamp:
            data.append(("Warning", f"Suspiciously old timestamp: {pe.FILE_HEADER.TimeDateStamp}"))

    except Exception as e:
        data.append(("Error", f"Unable to access PE metadata: {e}"))

    return data

def check_metadata(file_path):
    _, declared_file_extension = os.path.splitext(file_path)
    if '.exe' == str(declared_file_extension).lower():
        metadata_results = check_exe_metadata(file_path)
    elif '.vba' == str(declared_file_extension).lower():
        metadata_results = check_ole_metadata(file_path)
    elif '.docx' == str(declared_file_extension).lower():
        metadata_results = check_docx_metadata(file_path)
    elif '.pdf' == str(declared_file_extension).lower():
        metadata_results = check_pdf_metadata(file_path)
    else:
        metadata_results = check_file_metadata(file_path)

    # Printing the table
    if metadata_results:
        headers = ["Metadata Attribute", "Value"]
        print(tabulate(metadata_results, headers=headers, tablefmt="fancy_grid"))
    else:
        module_log.critical('No data returned')