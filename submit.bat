@echo off
echo ===================================================
echo [Git Update] 提交七日社交渐进与地图玩法 CP 的修改
echo ===================================================
git status
echo.
echo 即将执行以下操作：
echo 1. git add .
echo 2. git commit -m "docs(sevenday): update CP1/CP2/CP3 scope, timeline SVG, and sync HTML/MD"
echo 3. git push
echo.
pause
git add .
git commit -m "docs(sevenday): update CP1/CP2/CP3 scope, timeline SVG, and sync HTML/MD"
git push
echo.
echo 提交完成！
pause
