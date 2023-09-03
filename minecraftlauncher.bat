@echo off
set APPDATA=%CD%
"C:\Program Files\Java\jre1.8.0_151\bin\javaw.exe" -Xms512m -Xmx1024m -Djava.library.path="client/natives" -cp "client/asm-all-4.1.jar;client/b1.7.3.jar;client/jinput-2.0.5.jar;client/jopt-simple-4.5.jar;client/jutils-1.0.0.jar;client/launchwrapper-1.5.jar;client/lwjgl_util-2.9.0.jar;client/lwjgl-2.9.0.jar;" net.minecraft.client.Minecraft "Kakao" "12345"