from typing import Annotated

from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix='/request_file')


@router.post("/files/")
async def request_file_with_file(file: Annotated[bytes, File()]):
    """
    Upload a file using the File parameter.

    :param file: The file to upload.
    :return: A dictionary containing the size of the uploaded file.
    """
    return {"file_size": len(file)}


@router.post("/uploadfile/")
async def request_file_with_upload(file: UploadFile):
    """
    Upload a file using the UploadFile parameter.

    :param file: The file to upload.
    :return: A dictionary containing the filename of the uploaded file.
    """
    return {"filename": file.filename}


@router.post("/optional_uploadfile/")
async def request_file_with_upload_optional(file: UploadFile | None = None):
    """
    Upload an optional file using the UploadFile parameter.

    :param file: The optional file to upload.
    :return: A dictionary containing the filename of the uploaded file, or a message if no file was uploaded.
    """
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


@router.post("/uploadfiles_multi_files/")
async def request_multi_file_with_upload(
        files: Annotated[
            list[UploadFile], File(description="Multiple files as UploadFile")
        ],
):
    """
    Upload multiple files using the UploadFile parameter.

    :param files: A list of files to upload.
    :return: A dictionary containing the filenames of the uploaded files.
    """
    return {"filenames": [file.filename for file in files]}
