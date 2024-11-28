@echo off
echo Building PDF Attachment Extractor...
pyinstaller --distpath ../ --workpath build pdf_attachment_extractor.spec 
echo Build completed.

echo Removing build folder...
rd /s /q build
echo Checkout ../pdf_attachment_extractor
pause
