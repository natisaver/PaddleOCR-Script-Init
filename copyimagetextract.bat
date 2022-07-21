@ECHO ON

SET FileList=C:\Users\nat\gt\image_list.txt
SET Source=C:\Users\nat\gt
SET Destination=C:\Users\nat\gt\textractgt

FOR /F "USEBACKQ TOKENS=*" %%F IN ("%FileList%") DO XCOPY /F /Y "%Source%\%%~F" "%Destination%\"

GOTO :EOF