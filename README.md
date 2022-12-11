# Script documentation

## Constants
| Constant           | Functionality                                                             |
| ----------------- | ------------------------------------------------------------------ |
| FOLDERS | List with 2 requiered folders mentioned in ,,Functions" section. |
| FILE_SAVE_PATH | Standard save path. You can modify it. |
| PINNING_URL, PAYLOAD, HEADERS | IPFS requirements.|
| API_KEY | IPFS Api key. |


## Functions
| Function            | Functionality                                                             |
| ----------------- | ------------------------------------------------------------------ |
| prepare_directory() | Creates 2 folders in current script path. ReadyJsonFiles and ReadyQrCodes. This folders are needed in further processing. |
| metadata_to_json | Creates json file with metadata in ReadyJsonFiles. Take 3 inputs: data as dictionary, path, file number (useful in loops).|
| send_jsons_to_ipfs()| Sends all files from ReadyJsonFiles as 1 folder on IPFS. Creates for it QR code.|
| _get_files() | This function returns dictionary with 2 arrays containing files from needed folders (ReadyJsonFiles and ReadyQrCodes).|
| end_process() | This function deletes all files from needed folders (ReadyJsonFiles and ReadyQrCodes).|

