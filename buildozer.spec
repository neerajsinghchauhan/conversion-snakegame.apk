[app]
title = SnakeGame
package.name = snakegame
package.domain = com.example
source.dir = .
source.include_exts = py,kv,png
version = 0.1
requirements = python3==3.9.9, kivy==2.1.0, hostpython3==3.9.9
presplash.filename = snakegamesplash.png
icon.filename = snakegame.png

[buildozer]
log_level = 2
warn_on_root = 1

[buildozer.logcat]
logcat_filters = *:W

[buildozer.android]
android.permissions = INTERNET
android.api = 33

[buildozer.ios]
ios.bundle_name = SnakeGame
