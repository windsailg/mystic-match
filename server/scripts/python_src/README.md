## Possible Issues

- on Windows:

```shell
PS C:\neil_0103\Mystic-Match\python_src> .venv/Scripts/activate
.venv/Scripts/activate : 因為這個系統上已停用指令碼執行，所以無法載入 C:\neil_0103\Mystic-Match\python_src\.venv\Scripts\activate.ps1 檔案。如需詳細資訊，請參閱 about_Execution_Policies，網址為 https:/go.microsoft.com/fwlink/
?LinkID=135170。
位於 線路:1 字元:1
+ .venv/Scripts/activate
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

- try
> https://max07217841.pixnet.net/blog/post/5198261


## Mystic Match - python

- on Windows:

```bash
python -m pip install tensorflow
python -m pip install opencv_python
```