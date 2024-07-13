import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta

def get_size_verbose(size: int) -> str:
    if len(str(size)) >= 13:
        return str(round(size/10**12,2)) + " TB" 
    if len(str(size)) >= 10:
        return str(round(size/10**9,2)) + " GB" 
    if len(str(size)) >= 7:
        return str(round(size/10**6,2)) + " MB" 
    if len(str(size)) >= 4:
        return str(round(size/10**3,2)) + " KB" 
    return str(size) + "B" 

# def get_size_verbose(size: int) -> str:
#     file = ["KB","MB","GB", "TB"]
#     for x in range(4,1):
#         if len(str(size)) >= x*3+1:
#             return str(round(size/10**(x*3),2)) + file[x] 
#     return str(size) + "B" 

@dataclass
class Selector:
    min_size: int = -1
    older_than_days: int = -1
    extensions: list[str] = field(default_factory=[])

@dataclass
class File:
    path: str
    size: int
    last_modify_time: datetime

    def is_older_than(self, days: int) -> bool:
        return datetime.now() - self.last_modify_time > timedelta(days=days)

    @staticmethod
    def get_file(path: str) -> 'File':
        return File(path, os.path.getsize(path), datetime.fromtimestamp(os.path.getmtime(path)))


class SearchEngine:
    def traverse_path(self, start_path: str, depth: int, selector: Selector) -> list[File]:
        matching_files = []
        try:
            for f in os.listdir(start_path):
                full_f = os.path.join(start_path, f)
                if os.path.isfile(full_f):
                    file = File.get_file(full_f)
                    if not file.is_older_than(selector.older_than_days):
                        continue
                    if not file.size >= selector.min_size:
                        continue
                    if len(selector.extensions) > 0:
                        ok = False
                        name = file.path.upper()
                        for ext in selector.extensions:
                            if name.endswith(ext.upper()):
                                ok = True
                                break
                        if not ok:
                            continue
                    matching_files.append(file)

                if os.path.isdir(full_f):
                    if depth > 0:
                        extra = self.traverse_path(start_path=full_f, depth=depth - 1, selector=selector)
                        matching_files.extend(extra)
        except PermissionError:
            return []
        return matching_files
        


if __name__ == '__main__':
    # f = File('', 10, last_modify_time=datetime.now() - timedelta(days=10))
    # print(f.is_older_than(15))
    # print(File.get_file('aparser.py'))
    selector = Selector(extensions=['zip'])
    engine = SearchEngine()
    files = engine.traverse_path('C:\\users\\student', depth=2, selector=selector)
    files = sorted(files, key=lambda f: f.size)
    files = files[:20]
    for f in files:
        print(get_size_verbose(f.size*1000))