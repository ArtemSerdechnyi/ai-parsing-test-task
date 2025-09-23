from enum import StrEnum


class ProcessStatus(StrEnum):
    STARTING = "Starting file processing"
    READING_FILES = "Reading Excel files"
    EXTRACTING_SAMPLES = "Extracting column samples"
    MATCHING_COLUMNS = "Matching columns"
    PREPROCESSING = "Preprocessing column values"
    SUBTRACTING_SUP = "Subtracting SUP domains"
    SAVE_TO_DB = "Save to DB"
    COMPLETED = "Processing completed"
