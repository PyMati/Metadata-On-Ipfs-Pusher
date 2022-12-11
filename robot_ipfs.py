"""Automatation module"""
import json
import os
import qrcode
import requests


FOLDERS = [
    "ReadyJsonFiles",
    "ReadyQrCodes"
    ]

FILE_SAVE_PATH = "./"

QR = qrcode.QRCode(
        version=14,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=1,
        )

API_KEY = os.environ.get("API_KEY")

PINNING_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

PAYLOAD = {'pinataOptions': '{"cidVersion": 1}',
    'pinataMetadata': '{"name": "CertificateMetadata", "keyvalues": {"company": "NFTificate"}}'}

HEADERS = {
    'Authorization': f'Bearer {API_KEY}'
    }

def prepare_directory():
    """This function creates 2 needed directories in script folder"""
    try:
        os.mkdir(FOLDERS[0])
        os.mkdir(FOLDERS[1])
    except:
        print("Directories already exist")


def metadata_to_json(data: dict, file_save_path, file_number):
    """This function generetes json files from input dictionary (data)"""
    with open(os.path.join(file_save_path, FOLDERS[0], f"0{file_number}.json") , "w") as file:
        data_to_save = json.dumps(data, indent = 4) 
        file.write(data_to_save)
            

def _generate_qr(url, file_save_path, file_number):
    """This function generetes qr codes for json's"""
    QR.add_data(url)
    QR.make(fit=True)
    img = QR.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(file_save_path, FOLDERS[1], f"0{file_number}.png"))


def send_jsons_to_ipfs():
    """This functions has 2 functionalities:
        1. Push json file to IPFS
        2. Generates ipfs URL and save it in Qr code with the same number
    """
    files = []
    for json_file in _get_files()["ReadyJsonFiles"]:
        files.append(('file',(f'{json_file}',open(f'{FOLDERS[0]}/{json_file}','rb'),'application/octet-stream')))
    response = requests.request("POST", PINNING_URL, headers = HEADERS, files = files)
    print(response.text)
    cid = json.loads(response.text)["IpfsHash"]
    _generate_qr(f"ipfs://{cid}", FILE_SAVE_PATH, 0)
       
    
def _get_files():
    """This function returns dictionary with 2 arrays containing files from needed folders"""
    return {FOLDERS[0]: os.listdir(FOLDERS[0]),
            FOLDERS[1]: os.listdir(FOLDERS[1])}


def end_process():
    """This function deletes all files in needed folders"""
    for folder in FOLDERS:
        for filename in _get_files()[folder]:
            file_path = os.path.join(folder, filename)
            os.remove(file_path)


# -------------------Working-Example---------------------#
# prepare_directory()  #You have to initialiaze this command only once
# metadata_to_json({"Name": "Python Developer"}, FILE_SAVE_PATH, 0)
# send_jsons_to_ipfs()
# end_process()
#--------------------------------------------------------#
