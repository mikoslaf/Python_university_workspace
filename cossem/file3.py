import requests

def get_size_verbose2(size: int) -> str:
    if len(size) >= 13:
        return str(round(size/10*12,2)) + " TB" 
    if len(size) >= 10:
        return str(round(size/10*9,2)) + " GB" 
    if len(size) >= 7:
        return str(round(size/10*6,2)) + " MB" 
    if len(size) >= 4:
        return str(round(size/10*3,2)) + " KB"  
    return str(size) + " KB" 
