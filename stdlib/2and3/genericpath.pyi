from typing import List
import sys

def exists(path: str) -> bool: ...
def isfile(path: str) -> bool: ...
def isdir(s: str) -> bool: ...
def getsize(filename: str) -> int: ...
def getmtime(filename: str) -> float: ...
def getatime(filename: str) -> float: ...
def getctime(filename: str) -> float: ...
def commonprefix(m: List[str]) -> str: ...

if sys.version_info >= (3, 4):
    def samestat(s1: str, s2: str) -> int: ...
    def samefile(f1: str, f2: str) -> int: ...
    def sameopenfile(fp1: str, fp2: str) -> int: ...